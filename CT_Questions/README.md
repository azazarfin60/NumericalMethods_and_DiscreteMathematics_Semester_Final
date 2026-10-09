# Class Test Answers

Two files, written in P6:

| File | What it holds |
| :-- | :-- |
| `CT_answers_exam_style.md` | Exam-style answers to CT-01, CT-02A, CT-02B and CT-04 |
| `CT_answers_explanation.md` | The same answers with the reasoning shown |

**19 parts** across four tests. They are part of the 202 manifest rows.

## The marks problem

Class tests print marks at **question** level, never at part level.

| Test | Printed | Per part |
| :-- | :-- | :-- |
| CT-01 | `**Marks:** 10` per question | not printed |
| CT-02A | nothing at all | not printed |
| CT-02B | nothing at all | not printed |
| CT-04 | `**Marks:** 6`, `7`, `7` per question | not printed |

So a part heading carries:

```
**[Marks: not printed in source]**
```

and never a guessed split. CT-02A and CT-02B have no marks anywhere in the file,
so they carry the same line. `scripts/answer_manifest.csv` keeps the question
total in `marks_question` and leaves `marks_part` empty, which is the same
distinction in machine-readable form.

CT-04 Q.3 prints `7` and notes that the original script said `6`. The source
note is carried forward rather than silently resolved.

## Navigation

Cross references use wikilinks, for example `[[NM-4.6_Lagranges_Interpolation|NM-4.6 · Lagrange's Interpolation]]`.
Paths are not written by hand.

No em dashes. Plain words.