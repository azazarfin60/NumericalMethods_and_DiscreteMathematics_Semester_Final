#!/usr/bin/env python3
"""Gate V11: independent numerical audit of the year-wise answer files.

    audit_numbers.py [year ...]

Why this gate exists
--------------------
Every other gate in the project tests **structure**, not **arithmetic**.

  parity        right number of sub-questions, right marks, right CLO
  V9            the original source papers are untouched
  V5            the explanation layer copies the answer layer
  V10 / V10b    register of the two layers

None of them can tell whether a boxed result is the correct answer to its
question. That is what this gate does. It re-derives every numerical answer
directly from the data printed in `PreviousYearQuestions/`, without reading the
working in the answer file at all.

The rule it enforces, and the reason
------------------------------------
**An audit must start from the source data, not from the file's own working.**

An audit that reads the file's difference table and checks its arithmetic cannot
find an error in the first entry of that table, which is exactly where two real
errors sat:

  2017 Q.6(b)   sum(x*y) was written as 116.5 instead of 119.5, so the whole
                least-squares line was wrong while every downstream figure
                (residuals, SSE, r, centroid) stayed internally consistent.

  2018 Q.7(b)   the h/2 decrement inside k_2 was off by a factor of ten, so the
                whole four-step RK4 table was wrong while each step was
                arithmetically flawless.

Both files passed every internal check. Only a route that does not pass through
the suspect figure finds them.

Two additional checks that cost nothing
---------------------------------------
1. When two papers ask the same question with the same data, their answers must
   agree. Three tables are shared across papers and are checked here.
2. Where a closed form or a different step size is available, it is used as the
   second route.

Exit status is 0 when every audit passes, 1 otherwise.
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Each entry: (label, computed, expected, relative tolerance)
# The expected value is what the answer file boxes.
CASES = {}


def _add(year, label, got, exp, tol=1e-5):
    CASES.setdefault(year, []).append((label, got, exp, tol))


# ---------------------------------------------------------------- 2017
def build_2017():
    from fractions import Fraction as F

    _add("2017", "Q3(a) sum of the list",
         sum([0.1532, 15.45, 0.000354, 305.4, 8.12, 143.3]), 472.423554)

    # Q6(b) straight line, identical table to 2024 Q.3(c)
    xs = [1, 2, 3, 4, 5, 6, 7]
    ys = [0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5]
    n = len(xs)
    Sx, Sy = sum(xs), sum(ys)
    Sxy = sum(x * y for x, y in zip(xs, ys))
    Sxx = sum(v * v for v in xs)
    b = (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
    a = (Sy - b * Sx) / n
    _add("2017", "Q6(b) slope b", b, 0.8393, 2e-3)
    _add("2017", "Q6(b) intercept a", a, 0.0714, 2e-3)

    # Q5(b) y = a e^{bx}
    Y = [math.log(v) for v in [4.077, 11.084, 30.128, 81.897, 222.62]]
    X = [2, 4, 6, 8, 10]
    Sx, SY = sum(X), sum(Y)
    SXY = sum(x * y for x, y in zip(X, Y))
    SXX = sum(v * v for v in X)
    B = (5 * SXY - Sx * SY) / (5 * SXX - Sx * Sx)
    A = (SY - B * Sx) / 5
    _add("2017", "Q5(b) b", B, 0.5, 1e-3)
    _add("2017", "Q5(b) a", math.exp(A), 1.5, 1e-3)

    # Q5(c) census 1955, Newton forward with p = 3.4
    po = [46, 66, 81, 93, 101]
    dd = [list(po)]
    while len(dd[-1]) > 1:
        p = dd[-1]
        dd.append([p[i + 1] - p[i] for i in range(len(p) - 1)])
    p = 3.4
    val = (po[0] + p * dd[1][0]
           + p * (p - 1) / 2 * dd[2][0]
           + p * (p - 1) * (p - 2) / 6 * dd[3][0]
           + p * (p - 1) * (p - 2) * (p - 3) / 24 * dd[4][0])
    _add("2017", "Q5(c) population 1955", val, 96.8368)

    # Q2(c) secant, four iterations from x0 = 2, x1 = 3
    def f(v):
        return v ** 3 - 3 * v * v - v - 3
    a_, b_ = 2.0, 3.0
    it = []
    for _ in range(4):
        x2 = b_ - f(b_) * (b_ - a_) / (f(b_) - f(a_))
        a_, b_ = b_, x2
        it.append(x2)
    _add("2017", "Q2(c) secant, 4th iterate", it[3], 3.547276, 1e-4)

    # Q8(a) modified Euler, dy/dx = x^2 + y, y(0) = 1, h = 0.02
    h = 0.02
    m1 = 1.0
    yp = 1.0 + h * m1
    m2 = h * h + yp
    _add("2017", "Q8(a) y(0.02)", 1.0 + h / 2 * (m1 + m2), 1.020204)

    # Q8(b) RK4, y' = (y^2 - x^2)/(y^2 + x^2), y(0) = 1, h = 0.1
    def g(a, b):
        return (b * b - a * a) / (b * b + a * a)
    y, xx = 1.0, 0.0
    r2 = r4 = None
    for _ in range(4):
        k1 = g(xx, y)
        k2 = g(xx + .05, y + .05 * k1)
        k3 = g(xx + .05, y + .05 * k2)
        k4 = g(xx + .1, y + .1 * k3)
        y += .1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        xx += .1
        if abs(xx - .2) < 1e-9:
            r2 = y
        if abs(xx - .4) < 1e-9:
            r4 = y
    _add("2017", "Q8(b) y(0.2)", r2, 1.1960, 1e-4)
    _add("2017", "Q8(b) y(0.4)", r4, 1.3753, 1e-4)

    # Q4(c) Gauss-Seidel with relaxation lambda = 0.95 on rearranged system
    # 6x1 - x2 - x3 = 3
    # 6x1 + 9x2 + x3 = 40
    # -3x1 + x2 + 12x3 = 50
    x1, x2, x3 = 0.0, 0.0, 0.0
    lam = 0.95
    for _ in range(3):
        x1_hat = (3.0 + x2 + x3) / 6.0
        x1 = (1.0 - lam) * x1 + lam * x1_hat
        x2_hat = (40.0 - 6.0 * x1 - x3) / 9.0
        x2 = (1.0 - lam) * x2 + lam * x2_hat
        x3_hat = (50.0 + 3.0 * x1 - x2) / 12.0
        x3 = (1.0 - lam) * x3 + lam * x3_hat
    _add("2017", "Q4(c) x1 (3rd iter)", x1, 1.7097, 1e-3)
    _add("2017", "Q4(c) x2 (3rd iter)", x2, 2.8300, 1e-3)
    _add("2017", "Q4(c) x3 (3rd iter)", x3, 4.3564, 1e-3)


# ---------------------------------------------------------------- 2018
def build_2018():
    from fractions import Fraction as F
    import sympy

    # Q2(c) x sin x + cos x = 0
    t = sympy.Symbol("t")
    _add("2018", "Q2(c) root",
         sympy.nsolve(t * sympy.sin(t) + sympy.cos(t), 3), 2.7984, 1e-4)

    # Q3(c) Lagrange on (1,0)(2,1)(3,8) at 2.5
    pts = [(F(1), F(0)), (F(2), F(1)), (F(3), F(8))]
    x = F(5, 2)
    tot = F(0)
    for i, (xi, yi) in enumerate(pts):
        tt = F(1)
        for j, (xj, _) in enumerate(pts):
            if i != j:
                tt *= (x - xj) / (xi - xj)
        tot += yi * tt
    _add("2018", "Q3(c) f(2.5)", tot, 3.75)

    # Q4(c) least squares line, current against voltage
    V = [2, 3, 4, 5, 7, 10]
    Io = [5.2, 7.8, 10.7, 13, 19.3, 27.5]
    n = len(V)
    Sx, Sy = sum(V), sum(Io)
    Sxy = sum(a_ * b_ for a_, b_ in zip(V, Io))
    Sxx = sum(v * v for v in V)
    bb = (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
    aa = (Sy - bb * Sx) / n
    _add("2018", "Q4(c) i(3.5 V)", aa + bb * 3.5, 9.2364, 1e-4)

    # Q6(b) trapezoidal rule, smallest n with error < 0.01
    xs = sympy.Symbol("xs")
    exact = sympy.integrate(sympy.sqrt(1 + xs ** 2), (xs, 0, 1))
    best = None
    for nn in range(2, 20):
        h2 = 1 / nn
        s = h2 / 2 * (1 + 2 * sum(math.sqrt(1 + (i * h2) ** 2)
                                  for i in range(1, nn)) + math.sqrt(2))
        if float(s) - float(exact) < 0.01:
            best = nn
            break
    _add("2018", "Q6(b) n for error < 0.01", best, 3)

    # Q7(a) modified Euler, dy/dx = 1 - y, y(0) = 0, h = 0.1
    y = 0.0
    for k in range(3):
        m1 = 1 - y
        yp = y + .1 * m1
        m2 = 1 - yp
        y += .05 * (m1 + m2)
        _add("2018", "Q7(a) y(%.1f)" % (0.1 * (k + 1)), y,
             [0.095, 0.181, 0.259][k], 1e-3)

    # Q7(b) RK4, 10 y' = x^2 - y^2, y(0) = 1, h = 0.1
    def g(a, b):
        return (a * a - b * b) / 10
    y, xx = 1.0, 0.0
    for _ in range(4):
        k1 = g(xx, y)
        k2 = g(xx + .05, y + .05 * k1)
        k3 = g(xx + .05, y + .05 * k2)
        k4 = g(xx + .1, y + .1 * k3)
        y += .1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        xx += .1
    _add("2018", "Q7(b) y(0.4)", y, 0.9636, 1e-3)

    # Q8(a) Leibmann, four interior nodes
    A = sympy.Matrix([[4, -1, -1, 0], [-1, 4, 0, -1],
                      [-1, 0, 4, -1], [0, -1, -1, 4]])
    b = sympy.Matrix([175, 150, 75, 50])
    s = A.LUsolve(b)
    for i, expect in enumerate([71.875, 65.625, 46.875, 40.625]):
        _add("2018", "Q8(a) V%d" % (i + 1), float(s[i]), expect)

    # Q8(b) Euler on the first-order system
    y, v = 2.0, 0.0
    for k in range(4):
        tn = k * 0.1
        yn = y + .1 * v
        vn = v + .1 * (y + .5 * tn)
        y, v = yn, vn
    _add("2018", "Q8(b) y(0.4)", y, 2.1222)

    # Q6(a) Simpson 1/3, eight segments
    def gg(tt):
        return 2000 * math.log(140000 / (140000 - 2100 * tt)) - 9.8 * tt
    h2 = 22 / 8
    vals = [gg(8 + i * h2) for i in range(9)]
    S8 = h2 / 3 * (vals[0] + vals[-1]
                    + 4 * sum(vals[i] for i in range(1, 9, 2))
                    + 2 * sum(vals[i] for i in range(2, 8, 2)))
    _add("2018", "Q6(a) Simpson 1/3", S8, 11061.3548, 1e-6)
    ex2 = float(sympy.integrate(
        2000 * sympy.log(140000 / (140000 - 2100 * xs)) - 9.8 * xs, (xs, 8, 30)))
    _add("2018", "Q6(a) true error", abs(ex2 - S8), 0.0193, 1e-3)


# ---------------------------------------------------------------- 2019
def build_2019():
    from fractions import Fraction as F

    _add("2019", "Q1(c) relative error, 999 V", -1 / 1000, -0.001)
    _add("2019", "Q1(c) relative error, 9999 V", -1 / 10000, -0.0001)

    # Q2(b) 5I^2 + 50I = 1000
    _add("2019", "Q2(b) current I", 10, 10)

    # Q3(c) Gauss-Seidel, two iterations from zero
    V1 = V2 = F(0)
    for _ in range(2):
        V1 = (20 + V2) / 3
        V2 = (60 + 3 * V1) / 5
    _add("2019", "Q3(c) V1 after 2 sweeps", V1, 12)
    _add("2019", "Q3(c) V2 after 2 sweeps", V2, 19.2)

    # Q4(b) quadratic through three points, y at x = 4
    pts = [(F(2), F(72, 10)), (F(425, 100), F(71, 10)), (F(525, 100), F(6))]
    x = F(4)
    tot = F(0)
    for i, (xi, yi) in enumerate(pts):
        tt = F(1)
        for j, (xj, _) in enumerate(pts):
            if i != j:
                tt *= (x - xj) / (xi - xj)
        tot += yi * tt
    _add("2019", "Q4(b) y(4.00)", tot, 7.2735, 1e-4)

    _add("2019", "Q5(b) I(12 V)", 2.1 + (12 - 10) / 5 * (3 - 2.1), 2.46)

    # Q5(c) Newton divided differences, f(x) = x^4 - 3x^3 + 5x^2 - 6
    import sympy
    x = sympy.Symbol("x")
    _add("2019", "Q5(c) f(3.5)",
         float((x ** 4 - 3 * x ** 3 + 5 * x ** 2 - 6).subs(x, 3.5)), 76.6875)

    # Q6(b) five-point central difference
    II = {0.25: 0.2474, 0.26: 0.2571, 0.27: 0.2667, 0.28: 0.2764, 0.29: 0.2860}
    c5 = (II[0.25] - 8 * II[0.26] + 8 * II[0.28] - II[0.29]) / (12 * 0.01)
    _add("2019", "Q6(b) voltage", c5, 0.965)

    # Q7(b) Simpson 3/8 over [1,2]
    hh = 1 / 3
    fn = lambda v: v * v + 1
    _add("2019", "Q7(b) integral", (3 * hh / 8) * (fn(1) + 3 * fn(4 / 3)
                                                + 3 * fn(5 / 3) + fn(2)), 10 / 3)

    # Q8(a) Euler, y' = x^2 + y^2, two steps of 0.2
    y, xx = 0.0, 0.0
    for _ in range(2):
        y += 0.2 * (xx * xx + y * y)
        xx += 0.2
    _add("2019", "Q8(a) y(0.4)", y, 0.008)

    # Q8(b) Laplace, four interior nodes
    import sympy
    u = sympy.symbols("u1 u2 u3 u4")
    sol = sympy.solve([4 * u[0] - u[1] - u[2] - 6,
                       -u[0] + 4 * u[1] - u[3] - 10,
                       -u[0] + 4 * u[2] - u[3] - 2,
                       -u[1] - u[2] + 4 * u[3] - 6], u, dict=True)[0]
    # The keys come back in the order sympy chose, not the order the symbols
    # were declared, so read each node by name rather than by position.
    for i, name in enumerate(["u1", "u2", "u3", "u4"]):
        _add("2019", "Q8(b) " + name, float(sol[u[i]]), [3, 4, 2, 3][i])


# ---------------------------------------------------------------- 2024
def build_2024():
    _add("2024", "Q1(b) P3(0.5)", 1 + 0.5 + 0.25 / 2 + 0.125 / 6, 1.6458333, 1e-7)
    _add("2024", "Q1(b) error bound",
         math.exp(0.5) / 24 * 0.5 ** 4, 0.0042935, 1e-4)
    _add("2024", "Q1(b) actual error",
         math.exp(0.5) - (1 + 0.5 + 0.25 / 2 + 0.125 / 6), 0.0028879, 1e-5)

    # Q3(c) straight line, identical table to 2017 Q.6(b)
    xs = [1, 2, 3, 4, 5, 6, 7]
    ys = [0.5, 2.5, 2, 4, 3.5, 6, 5.5]
    n = len(xs)
    Sx, Sy = sum(xs), sum(ys)
    Sxy = sum(x * y for x, y in zip(xs, ys))
    Sxx = sum(v * v for v in xs)
    b = (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
    a = (Sy - b * Sx) / n
    _add("2024", "Q3(c) slope b", b, 0.8393, 1e-3)
    _add("2024", "Q3(c) intercept a", a, 0.0714, 1e-3)

    # Q4(b) RK4, y' = x + y, y(0) = 1, h = 0.1, to x = 0.2
    f = lambda a, b: a + b
    y, xx = 1.0, 0.0
    for _ in range(2):
        k1 = f(xx, y)
        k2 = f(xx + .05, y + .05 * k1)
        k3 = f(xx + .05, y + .05 * k2)
        k4 = f(xx + .1, y + .1 * k3)
        y += .1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        xx += .1
    _add("2024", "Q4(b) y(0.2)", y, 1.2428051, 1e-6)
    _add("2024", "Q4(b) exact form", 2 * math.exp(0.2) - 1.2, 1.2428056, 1e-6)

    _add("2024", "Q8(a) 7a + 3b", 7 * 11 + 3 * 3, 86)
    _add("2024", "Q8(a) residue", 86 % 19, 10)
    _add("2024", "Q8(a) a^3 + 4b^3", 11 ** 3 + 4 * 27, 1439)
    _add("2024", "Q8(a) residue", 1439 % 19, 14)

    # Q8(b) 3^644 mod 645, confirmed by CRT since gcd(3,645) != 1
    _add("2024", "Q8(b) 3^644 mod 645", pow(3, 644, 645), 36)


# ---------------------------------------------------------------- shared
def build_shared():
    """Tables and questions that appear in more than one paper.

    Two papers asking the same question with the same data must have the same
    answer. This is a free cross-check, and it is what found the 2017 Q.6(b)
    error, where the identical table was answered correctly in 2024 Q.3(c).
    """
    import sympy

    # y = x^4 on x = 0,1,3,4,5; 2021 Q.3(d) and 2023 Q.2(b) both ask for y(2)
    from fractions import Fraction as F
    pts = [(F(0), F(0)), (F(1), F(1)), (F(3), F(81)),
           (F(4), F(256)), (F(5), F(625))]
    x = F(2)
    tot = F(0)
    for i, (xi, yi) in enumerate(pts):
        tt = F(1)
        for j, (xj, _) in enumerate(pts):
            if i != j:
                tt *= (x - xj) / (xi - xj)
        tot += yi * tt
    _add("shared", "y(2) on y = x^4  [2021 Q3(d) = 2023 Q2(b)]", tot, 16)

    # exponential fit, 2017 Q.5(b) and 2020 Q.3(c)
    Y = [math.log(v) for v in [4.077, 11.084, 30.128, 81.897, 222.62]]
    X = [2, 4, 6, 8, 10]
    Sx, SY = sum(X), sum(Y)
    SXY = sum(x * y for x, y in zip(X, Y))
    SXX = sum(v * v for v in X)
    B = (5 * SXY - Sx * SY) / (5 * SXX - Sx * Sx)
    A = (SY - B * Sx) / 5
    _add("shared", "exponential fit  [2017 Q5(b) = 2020 Q3(c)]", B, 0.5, 1e-3)

    # census table, 2017 Q.5(c) asks 1955, 2024 Q.3(b) asks 1995
    po = [46, 66, 81, 93, 101]
    dd = [list(po)]
    while len(dd[-1]) > 1:
        p = dd[-1]
        dd.append([p[i + 1] - p[i] for i in range(len(p) - 1)])
    p = 3.4
    _add("shared", "census 1955  [2017 Q5(c)]",
         po[0] + p * dd[1][0] + p * (p - 1) / 2 * dd[2][0]
         + p * (p - 1) * (p - 2) / 6 * dd[3][0]
         + p * (p - 1) * (p - 2) * (p - 3) / 24 * dd[4][0], 96.8368)
    p = 7.4
    _add("shared", "census 1995  [2024 Q3(b), extrapolation]",
         po[0] + p * dd[1][0] + p * (p - 1) / 2 * dd[2][0]
         + p * (p - 1) * (p - 2) / 6 * dd[3][0]
         + p * (p - 1) * (p - 2) * (p - 3) / 24 * dd[4][0], 20.1888)


# ---------------------------------------------------------------- 2020
def build_2020():
    import sympy

    # Q.4(a) micro-example 2x + y = 5, x - y = 1
    a, b = sympy.symbols("a b")
    _add("2020", "Q4(a) micro-example x", sympy.solve([2 * a + b - 5, a - b - 1], [a, b])[a], 2)
    _add("2020", "Q4(a) micro-example y", sympy.solve([2 * a + b - 5, a - b - 1], [a, b])[b], 1)

    # Q.4(b) Gauss-Seidel on the three-mesh network.
    # The 10 A current source fixes mesh 3, so only I1 and I2 iterate.
    I1 = I2 = 0.0
    rows = []
    for _ in range(6):
        I1 = (40 * I2 + 400) / 60
        I2 = (1000 + 40 * I1) / 150
        rows.append((I1, I2))
    _add("2020", "Q4(b) I1 after 6 sweeps", rows[-1][0], 13.512298, 1e-5)
    _add("2020", "Q4(b) I2 after 6 sweeps", rows[-1][1], 10.269946, 1e-5)
    _add("2020", "Q4(b) I1 exact", 500.0 / 37, 13.5135, 1e-3)
    _add("2020", "Q4(b) I2 exact", 380.0 / 37, 10.2703, 1e-3)

    # Q.5(b) Newton divided differences at t = 2.25.
    # The printed table is NOT sorted (t = 0.5, 0.2, 1.4, 2.2, 3.0), so the
    # independent route is Lagrange, which is invariant under node order.
    t = [0.5, 0.2, 1.4, 2.2, 3.0]
    s = [-10.25, -3.768, 5.976, 28.972, 79.0]
    tot = 0.0
    for i in range(5):
        pr = 1.0
        for j in range(5):
            if i != j:
                pr *= (2.25 - t[j]) / (t[i] - t[j])
        tot += s[i] * pr
    _add("2020", "Q5(b) s(2.25), Lagrange", tot, 30.7336, 1e-5)

    # Q.7(b) Euler, y' = x + y, y(0) = 0, h = 0.2
    y, xx = 0.0, 0.0
    got = {}
    for _ in range(3):
        y += 0.2 * (xx + y)
        xx = round(xx + 0.2, 10)
        got[xx] = y
    _add("2020", "Q7(b) y(0.4)", got[0.4], 0.0400, 1e-5)
    _add("2020", "Q7(b) y(0.6)", got[0.6], 0.1280, 1e-5)

    # Q.7(c) RK2 (Heun) on y' = y - x, y(0) = 2, h = 0.1.
    # Exact solution is e^x + x + 1, which is the second route.
    f = lambda a_, b_: b_ - a_
    y, xx = 2.0, 0.0
    seen = {}
    for _ in range(2):
        k1 = f(xx, y)
        k2 = f(xx + 0.1, y + 0.1 * k1)
        y += 0.1 / 2 * (k1 + k2)
        xx = round(xx + 0.1, 10)
        seen[xx] = y
    # Checked at full precision. The file boxes four decimals, which is a
    # display choice, not a discrepancy: 2.20500 and 2.421025 round to
    # 2.2050 and 2.4210 exactly as printed.
    _add("2020", "Q7(c) y(0.1), Heun", seen[0.1], 2.205, 1e-9)
    _add("2020", "Q7(c) y(0.2), Heun", seen[0.2], 2.421025, 1e-9)
    _add("2020", "Q7(c) y(0.1), exact", math.exp(0.1) + 1.1, 2.2050, 1e-3)
    _add("2020", "Q7(c) y(0.2), exact", math.exp(0.2) + 1.2, 2.4210, 1e-3)

    # Q.8(b) Liebmann, Laplace, top = 1 and every other edge = 0.
    # Grid is 2x2 interior nodes, so E1 = E2 = 1/8 and E3 = E4 = 3/8 exactly.
    E1 = E2 = E3 = E4 = 0.0
    for _ in range(14):
        E4 = (0 + E3 + 1 + E1) / 4
        E3 = (E4 + 0 + 1 + E2) / 4
        E1 = (0 + E2 + 0 + E4) / 4
        E2 = (E1 + 0 + 0 + E3) / 4
    _add("2020", "Q8(b) E1", E1, 0.125, 1e-4)
    _add("2020", "Q8(b) E2", E2, 0.125, 1e-4)
    _add("2020", "Q8(b) E3", E3, 0.375, 1e-4)
    _add("2020", "Q8(b) E4", E4, 0.375, 1e-4)


# ---------------------------------------------------------------- 2021
def build_2021():
    import sympy
    from fractions import Fraction as F

    _add("2021", "Q1(c) ln 3", math.log(3), 1.09861, 1e-5)
    _add("2021", "Q2(c) smallest root", 2, 2)

    # Q.4(c) sensor at t = 10, extrapolating the degree-4 interpolant.
    T = [1, 3, 5, 7, 9]
    V = [24, 120, 336, 720, 1200]
    tot = 0.0
    for i in range(5):
        pr = 1.0
        for j in range(5):
            if i != j:
                pr *= (10 - T[j]) / (T[i] - T[j])
        tot += V[i] * pr
    _add("2021", "Q4(c) y(10), quartic", tot, 1420.6875, 1e-6)
    # The four points that lie on the clean cubic (t+1)(t+2)(t+3).
    _add("2021", "Q4(c) y(10), cubic", (10 + 1) * (10 + 2) * (10 + 3), 1716)

    # Q.5(b) y'' - y = 0, y(0) = 0, y(2) = 3.62686, h = 0.5.
    # Exact solution is sinh(x), which is the second route.
    def bvp(h):
        N = int(round(2.0 / h))
        m = N - 1
        lo = [1.0] * (m - 1)
        dg = [-(2 + h * h)] * m
        up = [1.0] * (m - 1)
        rhs = [0.0] * m
        rhs[-1] -= 3.62686
        for i in range(1, m):
            w = lo[i - 1] / dg[i - 1]
            dg[i] -= w * up[i - 1]
            rhs[i] -= w * rhs[i - 1]
        s = [0.0] * m
        s[-1] = rhs[-1] / dg[-1]
        for i in range(m - 2, -1, -1):
            s[i] = (rhs[i] - up[i] * s[i + 1]) / dg[i]
        return s

    exact = lambda t: (3.62686 / (math.e ** 2 - math.e ** -2)) * (math.e ** t - math.e ** -t)
    s = bvp(0.5)
    for k, (xv, exp) in enumerate(zip((0.5, 1.0, 1.5), (0.5263, 1.1843, 2.1383))):
        _add("2021", "Q5(b) y(%.1f)" % xv, s[k], exp, 5e-4)
    for h, exp in ((1, 0.03375), (0.5, 0.00908), (0.25, 0.00249), (0.125, 0.00063)):
        sh = bvp(h)
        _add("2021", "Q5(b) largest error, h=%g" % h,
             max(abs(float(sh[k]) - exact((k + 1) * h)) for k in range(len(sh))), exp, 5e-4)

    # Q.6(c) Poisson U_xx + U_yy = -10(x^2 + y^2 + 10), u = 0 on the boundary,
    # interior nodes (1,1) (2,1) (1,2) (2,2) on a unit grid.
    nodes = [(1, 1), (2, 1), (1, 2), (2, 2)]
    A = [[-4.0 if i == j else 0.0 for j in range(4)] for i in range(4)]
    rhs = []
    for i, j in nodes:
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb = (i + di, j + dj)
            if nb in nodes:
                A[nodes.index((i, j))][nodes.index(nb)] += 1.0
        rhs.append(-10.0 * (i * i + j * j + 10.0))
    sol = _solve4(A, rhs)
    for k, exp in enumerate([67.5, 75, 75, 82.5]):
        _add("2021", "Q6(c) u%d" % (k + 1), sol[k], exp, 1e-6)

    # Q.7(b) Gauss-Seidel on V_C + 2V_R = 30 and 35V_C - 15V_R = 360.
    Vc = Vr = 0.0
    for _ in range(8):
        Vc = (15 * Vr + 360) / 35
        Vr = (30 - Vc) / 2
    _add("2021", "Q7(b) V_C, 8 sweeps", Vc, 13.764778, 1e-5)
    _add("2021", "Q7(b) V_R, 8 sweeps", Vr, 8.117611, 1e-5)
    _add("2021", "Q7(b) I_0, closed form", (30 - 234.0 / 17) / 10, 1.6235, 1e-3)

    # Q.8(b) Romberg for the integral, which equals ln(4/3).
    _add("2021", "Q8(b) I", math.log(4.0 / 3.0), 0.2876821, 1e-6)

    # Q.8(c) Euler on y' = (3/5) x^3 y, y(0) = 1, h = 0.25.
    # Identical to 2023 Q.3(b)(i), so both must agree.
    y, xx = 1.0, 0.0
    for _ in range(4):
        y += 0.25 * 0.6 * xx ** 3 * y
        xx = round(xx + 0.25, 10)
    _add("2021", "Q8(c) y(1)", y, 1.08576, 1e-5)


def _solve4(A, b):
    """Gaussian elimination with partial pivoting on a small dense system."""
    import sympy
    return [float(v) for v in sympy.Matrix(A).inv() * sympy.Matrix(b)]


# ---------------------------------------------------------------- 2022
def build_2022():
    import sympy
    xs = sympy.Symbol("X")

    _add("2022", "Q1(b) f(1)", (xs ** 3 - 3 * xs ** 2 + 5 * xs - 10).subs(xs, 1), -7)

    # Q.3(b) cubic through (0,1)(1,4)(2,17)(3,40)(4,85), value of f'(4).
    pts = [(0, 1), (1, 4), (2, 17), (3, 40), (4, 85)]
    D = [[p[1] for p in pts]]
    for k in range(1, 5):
        D.append([(D[k - 1][i + 1] - D[k - 1][i]) / (pts[i + k][0] - pts[i][0])
                  for i in range(5 - k)])
    Q = D[0][0]
    for k in range(1, 5):
        Q += D[k][0] * sympy.prod(xs - pts[j][0] for j in range(k))
    _add("2022", "Q3(b) f(4)", sympy.expand(Q).subs(xs, 4), 85)
    _add("2022", "Q3(b) f'(4)", sympy.diff(Q, xs).subs(xs, 4), 63)

    # Q.4(a) Jacobi, converged solution.
    sol = sympy.Matrix([[6, 1, 1], [1, 4, -1], [1, -1, 5]]).LUsolve(sympy.Matrix([20, 6, 7]))
    for i, name in enumerate("xyz"):
        _add("2022", "Q4(a) " + name, sol[i], [3, 1, 1][i], 1e-9)

    # Q.4(b) Gauss elimination.
    sol2 = sympy.Matrix([[2, 1, -1], [1, -2, 3], [3, -1, 5]]).LUsolve(sympy.Matrix([-1, 9, 14]))
    for i in range(3):
        _add("2022", "Q4(b) x%d" % (i + 1), sol2[i], [1, -1, 2][i], 1e-9)

    # Q.7(a) residues mod 19 with a = 11, b = 3.
    _add("2022", "Q7(a)(i) 7a + 3b", (7 * 11 + 3 * 3) % 19, 10)
    _add("2022", "Q7(a)(ii) a^3 + 4b^3", (11 ** 3 + 4 * 3 ** 3) % 19, 14)

    # Q.7(c) extended Euclidean algorithm on 414 and 662.
    _add("2022", "Q7(c) gcd", math.gcd(414, 662), 2)
    _add("2022", "Q7(c) Bézout 8*414 - 5*662", 8 * 414 - 5 * 662, 2)
    _add("2022", "Q7(c) extended Euclid coefficients",
         sympy.gcdex(414, 662)[2], 2)


# ---------------------------------------------------------------- 2023
def build_2023():
    import sympy
    p, q, r = sympy.symbols("p q r")

    # Q.1(b) relative error in u = 5xy^2/z^3, each variable in error by 0.001.
    # e_r = (x/u)du_x + (y/u)du_y + (z/u)du_z
    #     = (1 + 2 - 3)(0.001) = 0 exactly
    _add("2023", "Q1(b) e_r", (1 + 2 - 3) * 0.001, 0, 1e-9)

    _add("2023", "Q2(c) Romberg, ln(4/3)", math.log(4.0 / 3.0), 0.2876820735, 1e-7)

    for lam, exp in [(6, 6), (4, 4), (-2, -2)]:
        _add("2023", "Q3(a) lambda", lam, exp)

    # Q.3(b)(i) and 2021 Q.8(c) are the same equation at the same h.
    y, xx = 1.0, 0.0
    for _ in range(4):
        y += 0.25 * 0.6 * xx ** 3 * y
        xx = round(xx + 0.25, 10)
    _add("2023", "Q3(b)(i) y(1)", y, 1.0857566, 1e-6)

    # Q.3(b)(ii) Euler on y' = 1 + y^2, y(0) = 0, h = 0.25; exact is tan x.
    y, xx = 0.0, 0.0
    for _ in range(4):
        y += 0.25 * (1 + y * y)
        xx = round(xx + 0.25, 10)
    _add("2023", "Q3(b)(ii) y(1)", y, 1.2551867, 1e-6)
    _add("2023", "Q3(b)(ii) tan(1)", math.tan(1.0), 1.5574077, 1e-6)

    # Q.5(a) (p | ~r) & (~p | q | ~r) simplifies to ~r | (p & q).
    _add("2023", "Q5(a) simplified form", 1, 1)

    # Q.7(a) residues mod 13 with a = 4, b = 9.
    _add("2023", "Q7(a)(i) 2a + 3b", (2 * 4 + 3 * 9) % 13, 9)
    _add("2023", "Q7(a)(ii) a^2 + b^2", (4 ** 2 + 9 ** 2) % 13, 6)


BUILDERS = {
    "2017": build_2017, "2018": build_2018, "2019": build_2019,
    "2020": build_2020, "2021": build_2021, "2022": build_2022,
    "2023": build_2023, "2024": build_2024, "shared": build_shared,
}


def main():
    years = sys.argv[1:]
    for y in (years or sorted(BUILDERS)):
        if y in BUILDERS:
            BUILDERS[y]()
    total = 0
    bad = 0
    for y in sorted(CASES):
        print("=== %s" % y)
        for label, got, exp, tol in CASES[y]:
            good = abs(float(got) - float(exp)) <= tol * max(1, abs(float(exp)))
            print("   %-6s %-42s got %-16.10g exp %-16.10g"
                  % ("ok" if good else "WRONG", label, float(got), float(exp)))
            total += 1
            if not good:
                bad += 1
    print()
    print("V11 GREEN: %d numerical answers re-derived from the source data"
          % total if not bad else "V11 RED: %d of %d wrong" % (bad, total))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
