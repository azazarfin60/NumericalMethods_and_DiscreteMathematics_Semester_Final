#!/usr/bin/env node
// normalize-vault-math.mjs
// Authoritative check for MARKDOWN-GUIDE.md rule 1.1 ($$ fence glued to content)
// and rule 1.8 (eaten escapes).
//
// WHY THIS EXISTS
// micromark's flow-math construct only CLOSES a $$ block on a line that is
// nothing but $$. A $$ glued to the end of a content line is ordinary text
// inside the block, so the block never closes and runs on to the end of the
// file, swallowing every heading, table and equation after it into one red
// KaTeX error box. Obsidian's MathJax closes on that happily, which is why the
// defect survives authoring.
//
// This script tracks real fence state (unlike a grep), skips fenced code and
// inline code spans, and understands blockquote and list prefixes.
//
// USAGE
//   node scripts/normalize-vault-math.mjs .            check only, exit 1 on defects
//   node scripts/normalize-vault-math.mjs . --write    repair what is repairable
//
// EXIT CODES
//   0  clean
//   1  defects found (and, with --write, defects that could not be repaired)
//
// SCOPE
//   Checks:  rule 1.1 (glued fence), 1.3 (odd $$ count), 1.4 (bare environment)
//   Repairs: glued fences, and the eaten-escape families of rule 1.8.

import { readFileSync, writeFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative, resolve, extname } from 'node:path';

const args = process.argv.slice(2);
const WRITE = args.includes('--write');
const rootArg = args.find((a) => !a.startsWith('--')) ?? '.';

// ---------------------------------------------------------------- file walk

function* walk(dir) {
  for (const name of readdirSync(dir)) {
    if (name === '.git' || name === 'node_modules') continue;
    const p = join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) yield* walk(p);
    else if (extname(p) === '.md') yield p;
  }
}

// ------------------------------------------------------- line classification

const RE_FENCE = /^\s{0,3}(`{3,}|~{3,})/;      // ``` or ~~~ opening/closing
const RE_BULLET = /^\s*(?:[-*+]|\d{1,9}[.)])(\s+|$)/; // list item marker

/** True when the line sits inside a markdown TABLE row. */
function isTableLine(raw) {
  const t = raw.trim();
  return t.startsWith('|') && t.endsWith('|') && t.length > 1;
}

/**
 * True when this line holds only self-contained $$...$$ spans, that is every
 * $$ pairs up on this same line with non-empty content between each pair.
 * Inline code spans and HTML tags are blanked first, so a documented
 * `$$x$$` example inside backticks does not count.
 *
 * Returns true, or null when the line is not self-contained.
 */
function pairedSpans(content) {
  let s = content.replace(/`+[^`]*`+/g, (m) => ' '.repeat(m.length));
  s = s.replace(/<[^>]*>/g, (m) => ' '.repeat(m.length));
  const parts = s.split('$$');
  if (parts.length < 3) return null;
  if (parts.length % 2 === 0) return null;      // odd fence count on one line
  for (let i = 1; i < parts.length; i += 2) {
    if (parts[i].trim() === '') return null;    // empty span between fences
  }
  return true;
}

/**
 * Split a raw line into { prefix, content } where prefix is the container
 * decoration micromark strips before it looks at the line: blockquote markers
 * and list indentation. Everything after that is "content".
 */
function splitPrefix(raw) {
  let rest = raw;
  let prefix = '';

  // blockquote markers, possibly nested:  > > text
  for (;;) {
    const m = /^(\s{0,3}>\s?)/.exec(rest);
    if (!m) break;
    prefix += m[1];
    rest = rest.slice(m[1].length);
  }

  // list item marker, only at the very start of the container
  const b = RE_BULLET.exec(rest);
  if (b) {
    prefix += b[0];
    rest = rest.slice(b[0].length);
  }

  return { prefix, content: rest };
}

/**
 * True when `content` is nothing but $$ (allowing surrounding whitespace).
 *
 * Leading whitespace matters: inside a list item the continuation lines are
 * indented, so a correct fence reads "  $$". micromark strips the container
 * indentation before it decides whether a line is a fence, so the check has to
 * do the same.
 */
function isBareFence(content) {
  return /^\s*\$\$[ \t]*$/.test(content);
}

/**
 * A line is a DEFECTIVE fence if it touches $$ but is neither a bare fence nor
 * a line whose $$ occurrences all pair up within it.
 *
 * The forms micromark handles are:
 *   - a bare `$$` on its own line, which opens or closes a display block
 *   - one or more complete `$$...$$` spans on a single line, which rule 1.2
 *     calls display maths wherever it appears
 *
 * The second form is why the papers are clean: every LaTeX array in
 * PreviousYearQuestions/ is a `$$\begin{array}...\end{array}$$` span sitting in
 * a table cell, which is the exception MARKDOWN-GUIDE.md rule 1.1 names.
 * Anything else is a fence glued to content.
 */
function fenceDefect(content) {
  if (!content.includes('$$')) return null;
  if (isBareFence(content)) return null;
  if (pairedSpans(content) === true) return null;
  return true;
}

/**
 * Strip the container prefix AND any continuation indentation, returning the
 * text micromark actually evaluates for a fence decision. An indented $$ inside
 * a list item is a fence; an indented \begin{aligned} is still an environment.
 */
function bare(raw) {
  return splitPrefix(raw).content.replace(/^\s+/, '');
}

// The eaten-escape families of rule 1.8: a shell ate the backslash and left
// the command tail at the start of a line.
const EATEN = /^(ight|ightarrow|ho|rac|egin|pprox|ext|imes|eft)(?![a-zA-Z])/;

// ------------------------------------------------------------- per-file scan

function scan(file, text) {
  const lines = text.split('\n');
  const defects = [];
  const repairs = [];

  let inCode = false;
  let codeFence = '';
  let mathOpen = false;      // are we inside a $$ ... $$ block?
  let mathOpenLine = 0;

  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i];
    const n = i + 1;

    // --- fenced code: skip everything inside, track state -----------------
    const f = RE_FENCE.exec(raw);
    if (f) {
      const marker = f[1][0];
      const len = f[1].length;
      if (!inCode) {
        inCode = true;
        codeFence = marker.repeat(len);
      } else if (marker === codeFence[0] && len >= codeFence.length) {
        inCode = false;
        codeFence = '';
      }
      continue;
    }
    if (inCode) continue;

    // --- inline code spans: strip them so $$ inside ` ` is ignored --------
    const noInline = raw.replace(/`+[^`]*`+/g, (m) => ' '.repeat(m.length));

    // rule 1.8: eaten escape at line start (content, not container prefix)
    const { prefix, content } = splitPrefix(noInline);
    const c = content.replace(/^\s+/, '');
    if (EATEN.test(content)) {
      // repairable: restore a leading backslash if the command is known
      const tail = EATEN.exec(content)[1];
      const fixed = content.replace(
        new RegExp('^' + tail),
        '\\' + tail
      );
      defects.push({ line: n, rule: '1.8', msg: 'eaten escape: command tail "' + tail + '" at line start' });
      repairs.push({ line: n, kind: 'eaten', from: raw, to: prefix + fixed });
      continue;
    }

    // --- rule 1.1: the fence-state check ---------------------------------
    if (fenceDefect(c)) {
      defects.push({
        line: n,
        rule: '1.1',
        msg: mathOpen
          ? '$$ glued to content on a line inside an OPEN math block opened at line ' + mathOpenLine + ' (this is not a closing fence)'
          : '$$ glued to content; micromark will not treat this as a fence',
      });
      // Repair: put the fence alone on its own line, content after it.
      //
      // The paired-opening case needs the scan state, not just this line.
      // When $$x = 1$$ appears on one line, that line is BOTH the opening
      // and the closing fence, and the content sits between them. Emitting a
      // bare closing fence for it would close the block that this very line
      // opened, and the following lines would fall outside the maths.
      // Work on the trimmed content so an indented fence inside a list item
      // behaves the same as a top-level one. The original indentation is
      // re-emitted through the indent variable.
      const indent = /^\s*/.exec(content)[0];
      const idx = c.indexOf('$$');
      const head = c.slice(0, idx).trimEnd();
      const tailTxt = c.slice(idx + 2);
      const endsWithFence = tailTxt.trimEnd().endsWith('$$');
      const inner = endsWithFence
        ? tailTxt.trimEnd().slice(0, -2).trim()
        : tailTxt.trim();

      if (head === '') {
        // Opening fence with trailing content, or a paired $$...$$ on one line.
        if (endsWithFence) {
          // Paired form: this line is both fences. Emit a balanced block.
          repairs.push({
            line: n,
            kind: 'paired',
            from: raw,
            to: prefix + indent + '$$\n' + prefix + indent + inner + '\n' + prefix + indent + '$$',
          });
          mathOpen = false;
          mathOpenLine = 0;
        } else {
          // Glued OPENING:  $$\begin{aligned}
          // Split off the fence only. The matching closing fence lives further
          // down the source (commonly as \end{aligned}$$), and that line gets its
          // own repair. Emitting a closing fence here would end the block before
          // the environment is finished.
          repairs.push({
            line: n,
            kind: 'open',
            from: raw,
            to: prefix + indent + '$$\n' + prefix + indent + inner,
          });
          mathOpen = true;
          mathOpenLine = n;
        }
      } else if (tailTxt.trim() === '') {
        // Closing fence glued to the end of a content line:  x = 1$$
        repairs.push({
          line: n,
          kind: 'close',
          from: raw,
          to: prefix + indent + head + '\n' + prefix + indent + '$$',
        });
        mathOpen = false;
        mathOpenLine = 0;
      } else {
        // Content, then $$ in the middle, then more content. Not repairable
        // without knowing the author's intent, so record it and stop.
        repairs.push({ line: n, kind: 'unrepairable', from: raw, to: raw });
        if (!mathOpen) { mathOpen = true; mathOpenLine = n; }
      }
      continue;
    }

    if (isBareFence(content)) {
      if (mathOpen) {
        mathOpen = false;
        mathOpenLine = 0;
      } else {
        mathOpen = true;
        mathOpenLine = n;
      }
      continue;
    }

    // whole-line display span: state unchanged, math not "open" after it

    // --- rule 1.4: an environment outside any $$ block -------------------
    // Inside a tracked math block this is correct and expected: the
    // \end{aligned} line correctly has no $$ of its own. So only flag an
    // environment when we are NOT inside a math block, and when neither this
    // line nor the previous one carries a $$ fence.
    if (!mathOpen &&
        /^\s*\\(?:begin|end)\{(?:aligned|cases|array|matrix|gather|bmatrix|pmatrix)/.test(content)) {
      const prev = i > 0 ? splitPrefix(lines[i - 1]).content : '';
      if (!content.includes('$$') && !prev.includes('$$')) {
        defects.push({
          line: n,
          rule: '1.4',
          msg: 'environment outside any $$ block: no $$ fence on this line or the previous one',
        });
      }
    }
  }

  if (mathOpen) {
    defects.push({
      line: mathOpenLine,
      rule: '1.3',
      msg: 'unclosed display block opened here; runs to end of file and swallows everything after it',
    });
  }

  return { lines, defects, repairs };
}

function applyRepairs(file, scanResult) {
  const byLine = new Map();
  for (const r of scanResult.repairs) byLine.set(r.line, r);
  const out = scanResult.lines.map((raw, i) => {
    const r = byLine.get(i + 1);
    return r ? r.to : raw;
  });
  writeFileSync(file, out.join('\n'));
}

// ------------------------------------------------------------------- report

const files = [...walk(resolve(rootArg))].sort();
let totalDefects = 0;
let totalRepaired = 0;
const byRule = new Map();

for (const f of files) {
  const text = readFileSync(f, 'utf8');
  const res = scan(f, text);
  if (!res.defects.length) continue;

  totalDefects += res.defects.length;
  const rel = relative(process.cwd(), f) || f;
  console.log(rel);
  for (const d of res.defects) {
    console.log('  ' + d.line + '  [rule ' + d.rule + ']  ' + d.msg);
  }
  if (WRITE && res.repairs.length) {
    applyRepairs(f, res);
    totalRepaired += res.repairs.length;
    console.log('  repaired ' + res.repairs.length + ' line(s)');
  } else if (res.repairs.length) {
    console.log('  ' + res.repairs.length + ' line(s) repairable with --write');
  }

  for (const d of res.defects) byRule.set(d.rule, (byRule.get(d.rule) ?? 0) + 1);
}

console.log('');
console.log('files scanned : ' + files.length);
console.log('defects found : ' + totalDefects +
  (byRule.size ? '  (' + [...byRule].sort().map(([r, c]) => 'rule ' + r + ': ' + c).join(', ') + ')' : ''));
if (WRITE) console.log('lines repaired: ' + totalRepaired);

if (totalDefects === 0) {
  console.log('clean');
  process.exit(0);
}
if (WRITE) {
  // Re-scan to see whether the repair actually fixed everything.
  let remaining = 0;
  for (const f of files) remaining += scan(f, readFileSync(f, 'utf8')).defects.length;
  if (remaining === 0) {
    console.log('all defects repaired');
    process.exit(0);
  }
  console.log('remaining after repair: ' + remaining + ' (not mechanically repairable)');
  process.exit(1);
}
process.exit(1);