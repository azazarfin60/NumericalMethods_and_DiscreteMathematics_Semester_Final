---
title: "DM-3.7 · System Specification & Consistency"
tags:
  - numerical-methods
  - discrete-mathematics
  - topicwise
---





[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.6 Translation: English → Logic](DM-3.6_Translation_English_to_Logic.md) | [Next: DM-3.8 Normal Forms & Functional Completeness →](DM-3.8_Normal_Forms_and_Functional_Completeness.md)

---

# DM-3.7 · System Specification & Consistency

Every block below is copied from `../answers_exam_style/`, which is the
only place an answer is authored. A number here is the same number, character
for character, as the one it came from.


### [2024 Q.5(c)]

**Question.** Are these system specifications consistent?

**Solution.**

> The system is in multiuser state if and only if it is operating normally, the
> kernel is functioning. The kernel is not functioning or the system is in
> interrupt mode. If the system is not in multiuser state, then it is in
> interrupt mode. The system is not in interrupt mode.

**Assign variables**

| Symbol | Meaning |
| :-- | :-- |
| $p$ | system is in multiuser state |
| $q$ | kernel is functioning |
| $r$ | system is in interrupt mode |

**Translate each sentence.**

1. "in multiuser state if and only if it is operating normally, the kernel is
   functioning":
   $p \leftrightarrow q$
2. "The kernel is not functioning or the system is in interrupt mode":
   $\neg q \lor r$
3. "If the system is not in multiuser state, then it is in interrupt mode":
   $\neg p \to r$, which is $p \lor r$
4. "The system is not in interrupt mode":
   $\neg r$

**Test all eight assignments.**

| $p$ | $q$ | $r$ | (1) $p \leftrightarrow q$ | (2) $\neg q \lor r$ | (3) $p \lor r$ | (4) $\neg r$ | all four |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| F | F | F | T | T | F | T | **F** |
| F | F | T | T | T | T | F | F |
| F | T | F | F | F | F | T | F |
| F | T | T | F | T | T | F | F |
| T | F | F | F | T | T | T | **F** |
| T | F | T | F | T | T | F | F |
| T | T | F | T | F | T | T | F |
| T | T | T | T | T | T | F | F |

No row satisfies all four.

**Reason without a table.** Specification 4 forces $r = F$. Specification 2 then
forces $\neg q$, so $q = F$. Specification 1 forces $p = F$. Specification 3 then reads
$p \lor r = F \lor F = F$, a contradiction.

$$
\boxed{\text{The specifications are INCONSISTENT: no assignment satisfies all four}}
$$

> [!warning] Where the contradiction comes from
> Sentence 4 says the system is **never** in interrupt mode. Sentence 2 then
> forces the kernel to be broken. Sentence 1 ties multiuser state to a
> working kernel, so the system cannot be in multiuser state either. Sentence 3
> says a system that is not in multiuser state must be in interrupt mode, which
> sentence 4 has already ruled out. The set describes a machine that cannot
> exist. In practice this means one of the four requirements is a typo, usually
> sentence 4.

---

---

**Also asked here.**

- *2024 Q.6(b)* is the same question as [[DM-3.8_Normal_Forms_and_Functional_Completeness|DM-3.8]], which is written in `DM-3.8`.
- *CT-04 Q.2(b)* is the same question as [[DM-3.8_Normal_Forms_and_Functional_Completeness|DM-3.8]], which is written in `DM-3.8`.
- *CT-04 Q.2(c)* is the same question as [[DM-3.2_Logical_Connectives_and_Truth_Tables|DM-3.2]], which is written in `DM-3.2`.
- *CT-04 Q.3(c)* is the same question as [[DM-3.2_Logical_Connectives_and_Truth_Tables|DM-3.2]], which is written in `DM-3.2`.

---

**Answered in phase P6, in `../CT_Questions/`.**

- *CT-04 Q.2(a)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.
- *CT-04 Q.3(b)* is a class-test question. Its answer is in `../CT_Questions/CT_answers_exam_style.md`, with the reasoning in `../CT_Questions/CT_answers_explanation.md`.

---

[🏠 Subtopic Index](00_Index.md) | [← Prev: DM-3.6 Translation: English → Logic](DM-3.6_Translation_English_to_Logic.md) | [Next: DM-3.8 Normal Forms & Functional Completeness →](DM-3.8_Normal_Forms_and_Functional_Completeness.md)
