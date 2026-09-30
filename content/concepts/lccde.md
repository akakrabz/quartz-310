---
title: "Linear constant-coefficient difference equation (LCCDE)"
description: "The recursion behind every practical LTI system: the two sign conventions of Lectures 5 and 9, initial rest, running the recursion, reading off H(z), and scipy.signal.lfilter."
tags: [concept, lccde, systems, z-transform, midterm-1]
aliases: ["difference equation", "LCCDE", "linear constant-coefficient difference equation", "recursion", "recursive system"]
---

> [!key] Standard form (Lecture 9, used on this site and by `lfilter`)
> $$
> \begin{gathered}
> y[n]+\sum_{k=1}^{N}a_k\,y[n-k]=\sum_{k=0}^{M-1}b_k\,x[n-k]
> \\[4pt] \Big\Downarrow \\[4pt]
> H(z)=\frac{Y(z)}{X(z)}=\frac{\sum_{k=0}^{M-1}b_k\,z^{-k}}{1+\sum_{k=1}^{N}a_k\,z^{-k}}
> \end{gathered}
> $$
> **Lecture 5 writes the same system as** $y[n]=\sum_{i=1}^{K}b_i\,y[n-i]+\sum_{j=0}^{M-1}c_j\,x[n-j]$: the feedback coefficients carry the **opposite sign** ($a_i=-b_i$), and Lecture 5's letter $b$ means *feedback* while Lecture 9's $b_k$ are the *input* coefficients ($=c_j$).
> Standing assumption: **initial rest** (zero initial conditions), which makes the system LTI; with only non-negative shifts it is causal and runs forward in time.

**Running it.** Solve for the newest output, $y[n]=-\sum_k a_k\,y[n-k]+\sum_k b_k\,x[n-k]$, and step forward from rest. Lecture 5: $y[n]=\frac12y[n-1]+x[n]$ with $x=\delta$ gives $1,\frac12,\frac14,\dots$, i.e. $h[n]=(\frac12)^nu[n]$. With $N=0$ (no feedback) the impulse response is just the $b_k$ list: [[concepts/fir-and-iir|FIR]]. Feedback usually makes it IIR, unless the poles cancel.

> [!recipe] LCCDE $\leftrightarrow$ $H(z)$
> 1. Move every $y$ term to the left and divide by the coefficient of $y[n]$.
> 2. Transform term by term with $x[n-k]\leftrightarrow z^{-k}X(z)$, $y[n-k]\leftrightarrow z^{-k}Y(z)$; solve for $Y/X$.
> 3. Factor the denominator for the poles; the ROC comes from causality or stability, **not** from the equation.
> 4. Backwards: cross-multiply $Y(z)\,A(z)=X(z)\,B(z)$ and read the coefficients off.
>
> [[0-midterm-1/past-exams/fall-2025|FA2025 #6]]: $y[n]=\frac43y[n-1]+\frac43y[n-2]+x[n]-x[n-2]$ gives
> $$
> H(z)=\frac{1-z^{-2}}{1-\frac43z^{-1}-\frac43z^{-2}}=\frac{1-z^{-2}}{(1-2z^{-1})(1+\frac23z^{-1})},
> $$
> poles $2,-\frac23$, zeros $\pm1$, causal ROC $\lvert z\rvert>2$ (not stable). Backwards, [[0-midterm-1/past-exams/spring-2025|SP2025 #8]]: $(1-\frac12z^{-1})(1+\frac32z^{-1})=1+z^{-1}-\frac34z^{-2}$, so $H=\frac{2-3z^{-1}}{1+z^{-1}-\frac34z^{-2}}$ is $y[n]+y[n-1]-\frac34y[n-2]=2x[n]-3x[n-1]$.

```python
import numpy as np
from scipy.signal import lfilter
# Lecture 5 form: y[n] = 1/2 y[n-1] + 1/2 y[n-2] + 3x[n] - 2x[n-1] + x[n-2]
# lfilter form:   y[n] - 1/2 y[n-1] - 1/2 y[n-2] = 3x[n] - 2x[n-1] + x[n-2]
b = [3, -2, 1]          # feed-forward: coefficients of x[n-k]
a = [1, -0.5, -0.5]     # 1 + a1 z^-1 + a2 z^-2 : signs FLIPPED vs Lecture 5
d = np.zeros(8); d[0] = 1
print(lfilter(b, a, d))            # impulse response, by recursion at initial rest
print(np.roots(a))                 # poles of H(z)
```

```text
[ 3.        -0.5        2.25       0.875      1.5625     1.21875
  1.390625   1.3046875]
[ 1.  -0.5]
```

The pole at $z=1$ is not cancelled ($3-2+1\neq0$), so $h[n]\to\frac{2}{1+1/2}=\frac43$: this Lecture 5 block-diagram example is not BIBO stable. The recursion hides that; the poles do not.

> [!trap]
> - **Sign flip between the forms.** `lfilter(b, a, x)` wants `a = [1, a1, …, aN]` from the Lecture 9 form; $y[n]-\frac12y[n-1]=x[n]$ is `a = [1, -0.5]`.
> - **Normalize first**: $y[n-2]+2y[n]=\dots$ ([[homework/hw2|HW2]] #1b) must be divided by 2 before reading coefficients.
> - **The equation does not fix causality** ([[0-midterm-1/past-exams/fall-2019|FA2019 #1a]] T): $y[n]-\frac12y[n-1]=x[n]$ has the causal solution $(\frac12)^nu[n]$ and the anti-causal $-(\frac12)^nu[-n-1]$. Two-sided systems are run as one forward and one backward recursion ([[problems/two-sided-systems-as-recursions]]).
> - **Sign bookkeeping costs points** (even the official [[0-midterm-1/past-exams/spring-2021|SP2021 #6]] key slipped): $y[n]=2y[n-3]-x[n]+x[n-3]$ has $h[0]=-1$, $h[3]=2h[0]+1=-1$, $H=\frac{-1+z^{-3}}{1-2z^{-3}}$ ([[0-toolkit/05-errata|errata]]).
> - An LCCDE has **finitely many poles** ([[0-midterm-1/past-exams/fall-2024|FA2024 #1d]] T); $y[n]=y[n-3]+x[n]$ has three distinct poles, the cube roots of unity ([[0-midterm-1/past-exams/fall-2024|FA2024 #1e]] T).
> - At least as many delayed input terms as feedback terms (numerator degree ≥ denominator degree in $z^{-1}$) gives an **improper** $H(z)$: long division first ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]).

**Where it appears.** [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] §1, [[2-z-transform/09-transfer-functions|Lecture 9]] §1.1, [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]; [[homework/hw2|HW2]] #1, [[homework/hw4|HW4]] #6. Problem families: [[problems/lccde-to-transfer-function-and-response]] (7/7: [[0-midterm-1/past-exams/fall-2025|FA2025 #6]], [[0-midterm-1/past-exams/spring-2025|SP2025 #8]], [[0-midterm-1/past-exams/fall-2024|FA2024 #6]], [[0-midterm-1/past-exams/fall-2023|FA2023 #6, #7]], [[0-midterm-1/past-exams/spring-2023|SP2023 #5, #6]], [[0-midterm-1/past-exams/spring-2021|SP2021 #6]], [[0-midterm-1/past-exams/fall-2019|FA2019 #10]]), [[problems/parameters-for-stability]] (SP2025 #7, FA2024 #8, FA2023 #8), [[problems/two-sided-systems-as-recursions]]. Try it: [[demos/difference-equation-simulator]].

**Related.** [[concepts/transfer-function|transfer function]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/block-diagram|block diagram]] · [[concepts/impulse-response|impulse response]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/causality|causality]] · [[concepts/z-transform-properties|z-transform properties]] (shift)

### Sources for this page
Lecture 5 §1 (Eq. 1, Eqs. 5–7, Exercise 1, Eq. 12); Lecture 9 §1.1 (Eqs. 4–7, Exercise 1); Lecture 10 §1; HW2 #1, HW4 #6; FA2025 #6, SP2025 #8, SP2021 #6, FA2019 #1a, FA2024 #1d–e. Checked in `verify/concepts/verify_glossary_time.py`, `verify_signals.py`, `verify_systems.py`; the snippet was run as shown.
