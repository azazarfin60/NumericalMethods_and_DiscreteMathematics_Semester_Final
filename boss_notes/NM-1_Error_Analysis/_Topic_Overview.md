# NM-1: Error Analysis

> **Section:** Section A (Numerical Methods)  
> **Subtopics in this folder:** 7 files (NM-1.1 through NM-1.7)  
> **Exam weight:** Appears in 8/8 papers (100% frequency), typically worth 10–14 marks (almost always the entirety of Question 1).

---

## 📖 How to Read This Topic

Error Analysis is the gateway to numerical methods. Question 1 in Section A almost always comes directly from this folder.

Start with **NM-1.1** to get the big picture: why numerical methods exist, why algebra fails on real-world circuits, and how numerical and analytical solutions differ. Next, read **NM-1.2** for mathematical modeling and **NM-1.3** to nail the difference between accuracy and precision.

Then dive into the mathematical core:
- **NM-1.4** classifies every error you will ever meet into three clean families.
- **NM-1.5** teaches you how to compute absolute, relative, and percentage errors, plus how errors snowball through formulas.
- **NM-1.6** is the heavy hitter: Taylor series, truncation error bounds, and why evaluating $e^{-x}$ directly can destroy your calculations.
- **NM-1.7** gives a quick, 2-minute skim of programming tools (C, FORTRAN, MATLAB) for reading flow.

**Suggested reading time:** ~45 minutes for the entire topic folder.

---

## 📑 Subtopic Index

| # | File | Priority | Exam Freq | Reading Time | Core Concept |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | [NM-1.1: Foundations](NM-1.1_Foundations.md) | 🔴 | 7/8 years | ~8 min | Numerical vs. analytical, why ECE needs them |
| 2 | [NM-1.2: Mathematical Modeling](NM-1.2_Mathematical_Modeling.md) | 🟡 ⚠️ | 2 appearances | ~6 min | 5 modeling steps, reactor cooling example |
| 3 | [NM-1.3: Accuracy and Precision](NM-1.3_Accuracy_and_Precision.md) | 🟠 | 2 appearances | ~6 min | Bullseye analogy, adding approximate numbers |
| 4 | [NM-1.4: Error Types](NM-1.4_Error_Types.md) | 🔴 | 6/8 years | ~8 min | Inherent vs. truncation vs. round-off |
| 5 | [NM-1.5: Error Propagation](NM-1.5_Error_Propagation.md) | 🔴 | 4/8 years | ~8 min | Relative error, log differentiation |
| 6 | [NM-1.6: Taylor Series](NM-1.6_Taylor_Series.md) | 🔴 ⚠️ | 6/8 years | ~10 min | Remainder bounds, catastrophic cancellation |
| 7 | [NM-1.7: Programming and Software](NM-1.7_Programming_and_Software.md) | ⚫ | Never | ~2 min | Software lifecycle, MATLAB, C, FORTRAN |

---

## 🎯 Exam Pattern for This Topic

Question 1 on your paper almost always draws from NM-1. The question is usually split into 3 or 4 parts:

1. **Part (a) -- Theory definition (3–4 marks):** Usually from NM-1.1 (define numerical method, compare with analytical, explain why ECE engineers need it) or NM-1.2 (modeling steps and importance).
2. **Part (b) -- Error classification or definition (3–4 marks):** Usually from NM-1.4 (round-off vs. truncation, how errors enter) or NM-1.3 (accuracy vs. precision with examples).
3. **Part (c) -- Calculation problem (3–4 marks):** Almost always from NM-1.5 (error propagation with $u = 5xy^2/z^3$, or voltmeter comparison) or NM-1.6 (Taylor expansion of $e^x$, $\ln 3$, or evaluating $e^{-5}$).

**Most common question combinations:**
- **Combination 1:** NM-1.1 (Analytical vs Numerical) + NM-1.4 (Round-off vs Truncation) + NM-1.6 (Taylor expansion / terms required).
- **Combination 2:** NM-1.1 (Why ECE needs numerical methods) + NM-1.5 (Error representations: voltmeter or current) + NM-1.5 / NM-1.6 (Propagation or Taylor series).

---

## 🔗 Topic Connections

- **Prerequisite:** First-year calculus (derivatives, limits, basic Taylor theorem).
- **Leads to:** [NM-2: Root Finding](../NM-2_Root_Finding/_Topic_Overview.md) -- every root-finding algorithm uses the iterative improvement and error tolerances established here.
- **Pairs with in exam:** Often appears as the standalone opening block of Section A, setting the pace for the entire examination.
