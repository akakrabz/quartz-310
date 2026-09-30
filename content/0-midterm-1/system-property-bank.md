---
title: "System-property bank"
description: "Every system from the seven past Midterm 1 property tables (Linear / Time-invariant / Causal / Stable), plus HW1 #5–6, HW2 #1 and the Lecture 3 practice list, with the official answers, a one-line reason per row, and the fast rules that decide each box."
tags: [midterm-1, exam, problem-family]
family_frequency: "7 of 7 exams"
typical_points: "12"
lectures: [3, 4]
---

*Problem family · on 7 of 7 past exams (FA2025 #2, SP2025 #2, FA2024 #2, FA2023 #2, SP2023 #2, SP2021 #3, FA2019 #2) · 12 pts (SP2021: 24) · [[1-signals-and-systems/03-system-properties|Lecture 3]], [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · recipe and proofs: [[problems/classifying-system-properties|Classifying system properties]]*

> [!abstract] How to use this page
> Every exam has a table of three systems with four Yes/No boxes each: **Linear, Time-invariant (= shift-invariant), Causal, (BIBO) Stable**. §1 lists the rules that decide nearly every box in seconds. §2–§4 give 46 rows: all 20 systems from the exam tables, the 5 homework systems, and the 21 from Lecture 3 (one of which repeats an exam system). Cover the four answer columns, fill them in, then check the reason column. Every row was also cross-checked numerically (superposition with random inputs, a shift test, a perturb-the-future test, and a battery of bounded inputs).

> [!exam] How the problem is graded
> No proofs are asked. FA2023: "you will only be graded on your answers in the boxes". SP2025: "points will not be deducted for incorrect answers". FA2019 #2 (L/SI/C only, no stability) graded **+2 / −1 / 0** per box. SP2021 gave 24 points for 12 boxes. Fill in every box.

## 1. The fast rules

> [!recipe] Decide each box with these rules
> **Linear?** The test is superposition. Zero in must give zero out, and scaling by $a = -1$ or $a = 2$ breaks most impostors.
> 1. **An additive constant ⇒ not linear:** $x[n]+3$, $2x[\lvert n\rvert]+10$ (zero in gives 3 or 10 out).
> 2. **Any nonlinear operation on the *values* ⇒ not linear:** $\lvert\cdot\rvert$, powers, $e^{(\cdot)}$, $\log$, $\sin$, $\max$, median, clipping, products of samples ($x[n]x[n+1]$, $x[3]x[n]$), ratios ($x[n]/x[2]$).
> 3. **Linear operations:** multiplying by a function of $n$ ($\lvert n\rvert x[n]$, $\cos^2(\tfrac\pi2 n)x[n]$), re-indexing ($x[2n]$, $x[\lvert n\rvert]$), adding shifted copies, and convolution with a fixed $h$.
>
> **Time-invariant?** Shift the input by $n_0$ and compare with the output shifted by $n_0$.
> 4. **$n$ outside the brackets ⇒ time-varying:** $\lvert n\rvert x[n]$, $\log(\lvert n\rvert+1)x[n]$, $(0.8+0.8j)^n x[n]$, $\cos(\tfrac\pi3(n-2))\,x[n]$. (The one exception is a factor that is constant on the integers, e.g. $\cos^2(\pi n) = 1$.)
> 5. **Index other than $n-k$ ⇒ time-varying:** $x[2n]$, $x[\lvert n\rvert]$, $x[\lvert n\rvert+n]$, $x[3n]$.
> 6. **A stored sample $x[0]$, $x[2]$ or $x[3]$ ⇒ time-varying *and* non-causal.** $y[n]$ for $n$ below that index needs a future sample.
>
> **Causal?** Look for any input index larger than $n$.
> 7. **$x[f(n)]$: test a negative *and* a positive $n$.** $x[\lvert n\rvert]$ fails at $n = -3$ ($x[3]$). $x[2n]$ fails at $n = 1$ ($x[2]$). $x[\lvert n\rvert+n]$ fails at $n = 1$ ($x[2]$).
> 8. **Convolution with a fixed $h$ ⇒ LTI; causal iff $h[n] = 0$ for $n<0$:** $u[n+1]$ and $2^n u[-n]$ fail.
>
> **Stable?** Every bounded input must give a bounded output.
> 9. **Convolution: stable iff $\sum_n\lvert h[n]\rvert < \infty$.** $2^n u[-n]$ sums to 2 ✓. $j^n u[n]$, $(-1)^n u[n]$ and $u[n+1]$ have $\lvert h\rvert = 1$ forever ✗ (bounded $h$ is not enough).
> 10. **Memoryless $g(x[n])$: stable iff $g$ maps bounded values to bounded values.** $e^{x}$, $\sin$, $\sin^2$, $\lvert\cdot\rvert$, $x^p$, clip and max are fine. $\ln\lvert x\rvert$ fails at $x = 0$, and so does division by $x[2]$ when $x[2] = 0$.
> 11. **Gain that depends on $n$: stable iff the gain is bounded.** $\lvert n\rvert$, $\log(\lvert n\rvert+1)$, $n$, $(n+1)$ and $\lvert 0.8+0.8j\rvert^n = 1.13^n$ are unbounded ✗. $\tfrac{1}{\lvert n\rvert+1}$, $(\tfrac12)^{\lvert n\rvert}$ and $\cos(\cdot)$ are bounded ✓. A difference does not rescue an unbounded gain: $n(x[n]-x[n-1])$ with $x = (-1)^n$ gives $2n(-1)^n$.

## 2. The exam tables (all 20 systems)

All answers match the official keys. FA2019 used "shift-varying" (SV) for time-varying and "LSI" for LTI.

| system | L | TI | C | S | why | exam |
|---|---|---|---|---|---|---|
| $y[n] = \lvert n\rvert\,x[n]$ | Yes | No | Yes | No | gain $\lvert n\rvert$ depends on $n$ (TV) and is unbounded: $x = 1$ gives $\lvert n\rvert$ | [[0-midterm-1/past-exams/fall-2025\|FA2025 #2]] |
| $y[n] = \lvert x[n]-x[n-1]\rvert$ | No | Yes | Yes | Yes | $\lvert\cdot\rvert$ fails $a=-1$; only present/past samples; $\lvert y\rvert \le 2B$ | [[0-midterm-1/past-exams/fall-2025\|FA2025 #2]] |
| $y[n] = x[n] * 2^n u[-n]$ | Yes | Yes | No | Yes | convolution ⇒ LTI; $h[-1] = \tfrac12 \ne 0$ ⇒ non-causal; $\sum_{n\le0}2^n = 2$ | [[0-midterm-1/past-exams/fall-2025\|FA2025 #2]] |
| $y[n] = x[n] * j^n u[n]$ | Yes | Yes | Yes | No | $h = 0$ for $n<0$; $\lvert h[n]\rvert = 1$ for all $n \ge 0$; $x = j^n u[n]$ gives $(n+1)j^n$ | [[0-midterm-1/past-exams/spring-2025\|SP2025 #2]] |
| $y[n] = 2x[\lvert n\rvert] + 10$ | No | No | No | Yes | $+10$ ⇒ not linear; $x[\lvert n\rvert]$ ⇒ TV; $y[-1] = 2x[1]+10$ (future); $\lvert y\rvert \le 2B+10$ | [[0-midterm-1/past-exams/spring-2025\|SP2025 #2]] |
| $y[n] = e^{x[n]+1}$ | No | Yes | Yes | Yes | $x = 0$ gives $e \ne 0$; memoryless; $\lvert y\rvert \le e^{B+1}$ | [[0-midterm-1/past-exams/spring-2025\|SP2025 #2]] |
| $y[n] = x[n]\,x[n+1]$ | No | Yes | No | Yes | product of samples; $x[n+1]$ is a future sample; $\lvert y\rvert \le B^2$ | [[0-midterm-1/past-exams/fall-2024\|FA2024 #2]] |
| $y[n] = \frac{1}{\lvert n\rvert+1}\,x[n]$ | Yes | No | Yes | Yes | gain depends on $n$ but is $\le 1$ | [[0-midterm-1/past-exams/fall-2024\|FA2024 #2]] |
| $y[n] = \sin(x[n]) + x[0]$ | No | No | No | Yes | $\sin$ nonlinear; stored $x[0]$ ⇒ TV, and $y[-1]$ needs $x[0]$; $\lvert y\rvert \le 1+B$ | [[0-midterm-1/past-exams/fall-2024\|FA2024 #2]] |
| $y[n] = \log(\lvert n\rvert+1)\,x[n]$ | Yes | No | Yes | No | gain grows (slowly!) without bound: $x = 1$ gives $\log(\lvert n\rvert+1)$ | [[0-midterm-1/past-exams/fall-2023\|FA2023 #2]] |
| $y[n] = x[n] * u[n+1]$ | Yes | Yes | No | No | $h[-1] = 1$ ⇒ non-causal; $\sum\lvert h\rvert = \infty$ | [[0-midterm-1/past-exams/fall-2023\|FA2023 #2]] |
| $y[n] = x[n] + 3$ | No | Yes | Yes | Yes | zero in gives 3 out (affine, not linear) | [[0-midterm-1/past-exams/fall-2023\|FA2023 #2]] |
| $y[n] = x[n] * (-1)^n u[n]$ | Yes | Yes | Yes | No | $\lvert h\rvert = 1$ for $n \ge 0$; $x = (-1)^n u[n]$ gives $(n+1)(-1)^n$ | [[0-midterm-1/past-exams/spring-2023\|SP2023 #2]] |
| $y[n] = \dfrac{x[n]}{x[2]}$ | No | No | No | No | scaling $x$ leaves $y$ unchanged; stored $x[2]$ ⇒ TV, and $y[0]$ needs $x[2]$; bounded input with $x[2] = 0$ ⇒ division by zero | [[0-midterm-1/past-exams/spring-2023\|SP2023 #2]] |
| $y[n] = \cos^2(\tfrac\pi2 n)\,x[n]$ | Yes | No | Yes | Yes | gain is 1 at even $n$, 0 at odd $n$: $\delta[n]$ passes, $\delta[n-1]$ is blocked | [[0-midterm-1/past-exams/spring-2023\|SP2023 #2]] |
| $y[n] = x[n]\cos(\tfrac\pi3(n-2))$ | Yes | No | Yes | Yes | the $-2$ is inside the cosine, not the input: an $n$-dependent gain, $\le 1$ | [[0-midterm-1/past-exams/spring-2021\|SP2021 #3]] |
| $y[n] = x[3]\,x[n]$ | No | No | No | Yes | doubling $x$ quadruples $y$; stored $x[3]$ ⇒ TV and non-causal; $\lvert y\rvert \le B^2$ | [[0-midterm-1/past-exams/spring-2021\|SP2021 #3]] |
| $y[n] = (0.8+0.8j)^n\,x[n]$ | Yes | No | Yes | No | $\lvert 0.8+0.8j\rvert = 0.8\sqrt2 \approx 1.13 > 1$: $x = 1$ gives $\lvert y\rvert = 1.13^n \to \infty$ | [[0-midterm-1/past-exams/spring-2021\|SP2021 #3]] |
| $y[n] = x[\lvert n\rvert+n]$ | Yes | No | No | *(Yes)* | index is $2n$ for $n \ge 0$ and $0$ for $n<0$ ⇒ TV; $y[1] = x[2]$ ⇒ non-causal | [[0-midterm-1/past-exams/fall-2019\|FA2019 #2(a)]] |
| $y[n] = (0.2)^{\lvert n\rvert}\log(x[n])$ | No | No | Yes | *(No)* | $\log$ nonlinear; $n$-dependent factor ⇒ SV; memoryless ⇒ causal; $\log 0 = -\infty$ | [[0-midterm-1/past-exams/fall-2019\|FA2019 #2(b)]] |

*(Italic)* entries: FA2019 #2 did not ask about stability; these are our answers.

> [!trap] Where the points go
> - **Bounded $h$ is not a stable system.** $j^n u[n]$, $(-1)^n u[n]$ and $u[n+1]$ are all bounded by 1 and all unstable. Only $\sum\lvert h\rvert$ counts.
> - **"$x$ is bounded, so $\lvert n\rvert x[n]$ is bounded."** No: the gain is unbounded. Same for $\log(\lvert n\rvert+1)$, even though it grows slowly.
> - **Affine is not linear.** $x[n]+3$ fails the zero-in-zero-out test.
> - **$x[\lvert n\rvert]$ and $x[2n]$ "look causal" for $n \ge 0$.** Check negative $n$ for $x[\lvert n\rvert]$ and positive $n$ for $x[2n]$.
> - **$\cos(\tfrac\pi3(n-2))$ is not a delay.** It multiplies $x[n]$ by a gain that depends on $n$, which makes the system time-varying.
> - **$e^{x[n]}$ is stable, $\ln\lvert x[n]\rvert$ is not.** A bounded exponent gives a bounded result; $\ln 0 = -\infty$.

## 3. Homework systems (HW1 #5–6, HW2 #1)

The homework asked only **linear** and **time-invariant**. The *italic* causal/stable entries are our answers.

| system | L | TI | C | S | why | source |
|---|---|---|---|---|---|---|
| clipping: $y = b$ if $x[n] \ge b$, $x[n]$ if $a<x[n]<b$, $a$ if $x[n] \le a$ | No | Yes | *Yes* | *Yes* | $a=-2$, $b=2$: $T(3) = 2$ but $T(6) = 2 \ne 2\cdot2$; the rule ignores $n$; $\lvert y\rvert \le \max(\lvert a\rvert,\lvert b\rvert)$ | [[homework/hw1\|HW1 #5]] |
| windowing: $y[n] = x[n]$ for $0 \le n \le N-1$, else 0 | Yes | No | *Yes* | *Yes* | $y = w[n]\,x[n]$ with the fixed window $w = u[n]-u[n-N]$: an $n$-dependent gain $\le 1$ | [[homework/hw1\|HW1 #6]] |
| $y[n] = y[n-5] + x[n] + 10x[n-1]$ | Yes | Yes | *Yes* | *No* | LCCDE at initial rest ⇒ LTI; $H = \frac{1+10z^{-1}}{1-z^{-5}}$ has 5 poles **on** $\lvert z\rvert = 1$ | [[homework/hw2\|HW2 #1(a)]] |
| $y[n-2] + 2y[n] = \cos(\tfrac\pi6 n)\,x[n]$ | Yes | No | *Yes* | *Yes* | input times $\cos(\tfrac\pi6 n)$ ⇒ TV; then a fixed recursion with poles $\pm j/\sqrt2$, inside the unit circle | [[homework/hw2\|HW2 #1(b)]] |
| $y[n] = (\tfrac12)^{\lvert n\rvert}\,x[n]$ | Yes | No | *Yes* | *Yes* | $n$-dependent gain $\le 1$ | [[homework/hw2\|HW2 #1(c)]] |

## 4. Lecture 3 practice list

From the Lecture 3 slides ("practice" and "extra practice" slides), the annotated in-class slides, and the exercises in the lecture notes.

| system | L | TI | C | S | why |
|---|---|---|---|---|---|
| $\tfrac12 x[n] + \tfrac12 x[n-1]$ | Yes | Yes | Yes | Yes | two-point average (FIR) |
| $x[n] + 1$ | No | Yes | Yes | Yes | additive constant |
| $\lvert x[n]\rvert$ | No | Yes | Yes | Yes | $a = -1$ fails |
| $e^{x[n]}$ | No | Yes | Yes | Yes | $\lvert y\rvert \le e^{B}$ |
| $n(x[n]-x[n-1])$ | Yes | No | Yes | No | $x = (-1)^n$ gives $2n(-1)^n$ |
| $\max\{0, x[n]\}$ | No | Yes | Yes | Yes | $a = -1$ fails ($x = 1$ gives 1, $x = -1$ gives 0) |
| $x[n]\,x[0]$ (annotated slides) | No | No | No | Yes | product; stored $x[0]$ |
| $x[n]-x[n-1]$ | Yes | Yes | Yes | Yes | first difference (FIR) |
| $x[2n]$ | Yes | No | No | Yes | downsampler; $y[1] = x[2]$ |
| $x[\lvert n\rvert]$ | Yes | No | No | Yes | $y[-3] = x[3]$ |
| $\tfrac13(x[n]+x[n-1]+x[n-2])$ | Yes | Yes | Yes | Yes | three-point average |
| $x[\lvert n\rvert-n]$ | Yes | No | No | Yes | $x[0]$ for $n \ge 0$; $y[-1] = x[2]$ |
| $(n+1)(x[n]-x[n-1])$ | Yes | No | Yes | No | unbounded gain |
| $\sin^2(x[n])$ | No | Yes | Yes | Yes | $0 \le y \le 1$ |
| $\ln\lvert x[n]\rvert$ | No | Yes | Yes | No | $x[n] = 0$ gives $-\infty$ |
| $x[n]/(\lvert n\rvert+1)$ | Yes | No | Yes | Yes | same as FA2024 |
| $\mathrm{median}\{x[n],x[n-1],x[n-2]\}$ | No | Yes | Yes | Yes | the median of a sum is not the sum of the medians |
| $x^p[n]$, $p>0$, $p \ne 1$ (notes Ex. 2) | No | Yes | Yes | Yes | $T(ax) = a^p T(x)$ |
| $n\,x[3n]$ (notes Ex. 5) | Yes | No | No | No | $y[1] = x[3]$; unbounded gain |
| $x[n]+x[n-2]-x[n-4]$ (notes Ex. 6) | Yes | Yes | Yes | Yes | FIR |
| $x^{10}[n] + e^{x[n]}$ (notes Ex. 7) | No | Yes | Yes | Yes | $\lvert y\rvert < \beta^{10} + e^{\beta}$ |

## 5. Notes on the keys

> [!note] No disagreement with the official keys
> All 20 exam rows match the keys. Things worth knowing if you must justify an answer:
> - **SP2023, $x[n]/x[2]$, Stable = No** rests on the bounded input with $x[2] = 0$ (division by zero). For any input with $x[2] \ne 0$ the output is bounded by $B/\lvert x[2]\rvert$, so cite $x[2] = 0$. **Linear = No** because homogeneity fails: $\dfrac{a\,x[n]}{a\,x[2]} = \dfrac{x[n]}{x[2]} \ne a\,y[n]$.
> - **SP2021, $(0.8+0.8j)^n x[n]$:** the key's margin note writes the base as $\sqrt{1.28}\,e^{j\pi/4}$, which "goes to $\infty$ as $n \to \infty$". The growth is only toward $+\infty$; toward $-\infty$ it decays, but one direction is enough.
> - **FA2019 #2** asked L/SI/C only. **HW1–HW2** asked L/TI only.

> [!warning] Answer-key erratum (HW1 solution #5(b))
> The linearity counterexample ($x_1 = 1$, $x_2 = n^2$, $a = 0$, $b = 4$) prints $T(x_1)+T(x_2) = \{\dots,5,4,2,\underset{\uparrow}{1},2,4,5,\dots\}$. At $n = \pm2$ the value is $T(1) + T(4) = 1 + 4 = 5$, so the line should read $\{\dots,5,5,2,\underset{\uparrow}{1},2,5,5,\dots\}$. The comparison line $T(x_1+x_2) = \{\dots,4,4,2,\underset{\uparrow}{1},2,4,4,\dots\}$ is right, and so is the conclusion (not linear). See also [[0-toolkit/05-errata|Errata]].

## 6. Python: causality and stability of the convolution rows

For $y = x*h$ the whole question is two numbers: is $h$ zero for $n<0$, and does $\sum\lvert h\rvert$ stop growing?

```python
import numpy as np
k = np.arange(-300, 301)
u = lambda k: (k >= 0).astype(float)
rows = {"x * 2^n u[-n]   (FA25)": 2.0**np.minimum(k, 0) * u(-k),
        "x * j^n u[n]    (SP25)": 1j**k * u(k),
        "x * u[n+1]      (FA23)": u(k + 1),
        "x * (-1)^n u[n] (SP23)": (-1.0)**k * u(k)}
for name, h in rows.items():
    past = np.abs(h[k < 0]).max()                  # causal  <=>  h[n] = 0 for n < 0
    s1, s2 = (np.abs(h[np.abs(k) <= N]).sum() for N in (100, 300))
    print(f"{name}: max|h[n<0]| = {past:.1f}   sum|h| to |n|=100, 300: {s1:5.1f} {s2:5.1f}")
```

```text
x * 2^n u[-n]   (FA25): max|h[n<0]| = 0.5   sum|h| to |n|=100, 300:   2.0   2.0
x * j^n u[n]    (SP25): max|h[n<0]| = 0.0   sum|h| to |n|=100, 300: 101.0 301.0
x * u[n+1]      (FA23): max|h[n<0]| = 1.0   sum|h| to |n|=100, 300: 102.0 302.0
x * (-1)^n u[n] (SP23): max|h[n<0]| = 0.0   sum|h| to |n|=100, 300: 101.0 301.0
```

Nonzero past ⇒ non-causal (FA25, FA23). A partial sum that keeps growing with the window ⇒ unstable (SP25, FA23, SP23). Only $2^n u[-n]$ settles, at 2.

## Related

[[problems/classifying-system-properties|Classifying system properties (recipe)]] · [[0-midterm-1/true-false-bank|True/False bank]] · [[concepts/linearity|Linearity]] · [[concepts/time-invariance|Time-invariance]] · [[concepts/causality|Causality]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/lti-system|LTI system]] · [[concepts/convolution|Convolution]] · [[1-signals-and-systems/03-system-properties|Lecture 3]]

### Sources for this page

- Official keys: FA2025 #2, SP2025 #2, FA2024 #2, FA2023 #2, SP2023 #2 (tables), SP2021 #3 (handwritten), FA2019 #2 (handwritten, L/SI/C only).
- HW1 #5–#6 and HW2 #1 with official solutions (L/TI only); Lecture 3 slides (practice and extra-practice slides, annotated in-class version) and Lecture 3 notes, Exercises 1–7.
- Numerical cross-check of every row and of every specific claim on this page: `verify/exams/property_bank.py` (57 checks, all passing).
