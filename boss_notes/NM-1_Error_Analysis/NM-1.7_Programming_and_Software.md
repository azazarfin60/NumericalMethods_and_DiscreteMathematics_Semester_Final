[← Previous: NM-1.6 Taylor Series](NM-1.6_Taylor_Series.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2 Root Finding Overview →](../NM-2_Root_Finding/_Topic_Overview.md)

---

# NM-1.7: Programming and Software

> ⚫ **Never examined.** This note exists for reading flow. Skim it in 2 minutes to connect the ideas, but do not spend precious revision time memorizing it.

## What This Is

Once you have a mathematical model and an error-controlled numerical algorithm, you need to turn it into executable software. 

In textbook numerical analysis (Jain §1.1.1–1.1.3), developing numerical software follows a 3-phase lifecycle:
1. **Mathematical formulation:** Define the physical system, identify inputs and outputs, and define mathematical validity checks.
2. **Algorithm design:** Select a stable numerical scheme, specify required tolerance levels, and formulate error calculation steps.
3. **Coding and validation:** Convert the algorithm into a flowchart and write source code in a programming language (like C, FORTRAN, or Python) or a matrix environment like MATLAB.

## Key Idea: Tools of the Trade

- **Languages:** Historically, **FORTRAN** (FORmula TRANslation) was favored for its high-performance numerical libraries (like IMSL). Today, **C/C++** is standard for embedded real-time systems, while **Python** (NumPy/SciPy) and **MATLAB** (Matrix Laboratory) dominate rapid engineering prototyping.
- **Floating-point precision (IEEE 754):**
  * **Single precision (float):** Uses 32 bits, giving about 7 significant decimal digits ($10^{-38}$ to $10^{38}$).
  * **Double precision (double):** Uses 64 bits, giving about 15–16 significant decimal digits ($10^{-308}$ to $10^{308}$). Standard numerical algorithms (like MATLAB) default to double precision to prevent catastrophic accumulation of round-off error.

## 🔗 Move On

This subtopic has **never appeared** in any RUET exam paper from 2017 to 2024. If you are preparing for your semester final, skip right ahead to the next topic: **Root Finding**.

---

[← Previous: NM-1.6 Taylor Series](NM-1.6_Taylor_Series.md) | [📂 Topic Overview](_Topic_Overview.md) | [🏠 Master Index](../00_Index.md) | [Next: NM-2 Root Finding Overview →](../NM-2_Root_Finding/_Topic_Overview.md)
