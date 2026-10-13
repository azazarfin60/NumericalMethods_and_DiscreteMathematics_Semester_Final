# Year-wise Explanations

One file per past paper: `2017_explanation.md` through `2024_explanation.md`.

Same questions as `../answers_exam_style/`, written to be read rather than
copied. Every step is named. The reason a formula is chosen is stated. Common
mistakes are called out.

This layer is governed by `writing_style.md`, **not** by `exam_register.md`.
The exam-style layer is a formal answer script, so it carries no second person
and no commentary. This layer is an explanation, so it may address the reader
and explain at length. The distinction is deliberate and the two layers must not
be written in the same voice.

## Gates on this layer

| Gate | What it enforces |
| :-- | :-- |
| **V5** | Every boxed result is character identical to the exam-style origin, including boxes containing `\text{}`, `\frac{}` or `\begin{bmatrix}`. |
| **V10b** | The P2 register: no em dash, no _Furthermore_/_Moreover_/_Consequently_, every question heading exists in the paper, and no self-correction narration survives. |

V5 once reported GREEN while checking 6 of 25 boxes, because its pattern could
not match a box containing braces and most boxes do. It now counts braces rather
than matching them, so a GREEN means the boxes were actually compared. See
§22.1 of `../ANSWER_BUILD_PLAN.md`.

V10b replaces the P1 register linter here. Running `lint_register.py` against
this directory reports violations that are not violations, because it checks the
answer-script rules.

## The rule that matters

**Every boxed result here is character identical to the one in
`../answers_exam_style/`.** Both files are checked by gate V5. If the exam-style
file says `3.4934`, this file says `3.4934`, not `3.49` and not `3.4934 rad`.

This layer adds reasoning around a number. It never changes the number.

**A box is a claim that the sentence inside it is this section's answer.** So if
P1 does not box something, P2 must not box it either. Boxes are the answer layer's
job, and P2 inherits them. `2024_explanation.md` had boxed a total-error claim
that P1 stated differently and, worse, incorrectly: P2 had dropped data error
entirely and claimed the terms "each pull the other way", when in fact they can
also reinforce.

## Before writing a section

Copy the question text from `PreviousYearQuestions/` and check the draft's
heading characters against it. Five sections of `2024_explanation.md` were
rewritten because they were drafted from memory of the question and answered a
question that was not the one asked. The headings read well and the content was
wrong. R3 in V10b catches this by comparing every heading to the P1 heading set,
but reading the paper first is the cheaper route.

**A correct heading is not sufficient.** The census section of
`2024_explanation.md` is headed "estimate the population for the year 1995" and
carries the right marks, and it answers 1955 instead, using 2017's question and
2017's answer of $96.8368$ where P1 has $20.1888$. What caught it was V5, once
V5 could see the box: a number belonging to no P1 box belongs to no P1 section.
Both layers can agree on a heading and still be about different questions, so
check the body against the paper, not just the heading against P1.

## How a block reads

The heading is printed as the paper prints it, with the marks under it rather
than inside it, so the heading line stays comparable to the exam-style file.

```
### **(c) Fit a straight line to the $x$ and $y$ values in the following table.**

*[Marks: 04, CO: 1]*

**The method.** Least squares picks the line $y = a + bx$ that minimises the sum
of squared vertical residuals. Differentiating with respect to $a$ and to $b$ and
setting both to zero gives the two **normal equations**:

$$\begin{aligned}
na + b\sum x &= \sum y \\
a\sum x + b\sum x^2 &= \sum xy
\end{aligned}$$

> [!warning] Watch this
> Swapping the two equations is the common slip. Read off which coefficient
> multiplies which sum before substituting. The safeguard is the centroid check:
> a line that does not pass through $(\bar x, \bar y)$ has had its equations
> swapped.

**Solve.** ...
$$\boxed{y = 0.0714 + 0.8393x}$$
```

## Rules

| Rule | What it means |
| :-- | :-- |
| Boxed numbers copied, never retyped | Gate V5 compares them character for character. |
| No invented questions | Nothing here that is not in the paper (Rule C). No practice, similar, or bonus drills. V10b and V9 check this. |
| No self-correction narration | A draft must not argue with itself. Resolve it before closing the file. |
| LaTeX fences on their own lines | `$$` sits alone. Never glued to content. |
| Callouts for traps | Use `> [!warning]` and `> [!note]`. |
| Every diagram P1 carries is carried here | A question that refers to a figure cannot be answered without it. |
| Diagram assets | Linked via relative paths (`diagrams/` or shared assets). |

No em dashes. No `Furthermore`, `Moreover`, `Consequently`. Plain words.