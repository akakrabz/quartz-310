---
title: "System-property bank"
description: "Every system from the seven past Midterm 1 property tables, plus HW1 #5–6, HW2 #1 and the Lecture 3 practice list, with official answers, a one-line reason per row, and the fast rules."
tags: [midterm-1, exam, problem-family]
family_frequency: "7 of 7 exams"
typical_points: "12"
lectures: [3, 4]
---

*Problem family · 7 of 7 past exams (FA2025 #2, SP2025 #2, FA2024 #2, FA2023 #2, SP2023 #2, SP2021 #3, FA2019 #2) · 12 pts (SP2021: 24) · [[1-signals-and-systems/03-system-properties|Lecture 3]], [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · recipe: [[problems/classifying-system-properties|Classifying system properties]]*

> [!exam] How the problem is graded
> Three systems × four boxes (Linear, Time-invariant, Causal, Stable); no proofs. FA2023 grades boxes only; SP2025 deducts nothing for wrong boxes; FA2019 #2 (L/SI/C) graded +2 / −1 / 0. Fill every box.

## 1. The fast rules

> [!recipe] Decide each box with these rules
> **Linear?** Zero in ⇒ zero out; try $a = -1$, $a = 2$.
> 1. **Additive constant ⇒ not linear:** $x[n]+3$, $2x[\lvert n\rvert]+10$.
> 2. **Nonlinear operation on values ⇒ not linear:** $\lvert\cdot\rvert$, powers, $e^{(\cdot)}$, $\log$, $\sin$, $\max$, median, clipping, $x[n]x[n+1]$, $x[3]x[n]$, $x[n]/x[2]$.
> 3. **Linear:** gains in $n$ ($\lvert n\rvert x[n]$, $\cos^2(\tfrac\pi2 n)x[n]$), re-indexing ($x[2n]$, $x[\lvert n\rvert]$), sums of shifts, convolution.
>
> **Time-invariant?** Shift the input by $n_0$, compare with the shifted output.
> 4. **$n$ outside the brackets ⇒ time-varying:** $\lvert n\rvert x[n]$, $\log(\lvert n\rvert+1)x[n]$, $(0.8+0.8j)^n x[n]$, $\cos(\tfrac\pi3(n-2))\,x[n]$ (unless constant on integers, e.g. $\cos^2(\pi n) = 1$).
> 5. **Index other than $n-k$ ⇒ time-varying:** $x[2n]$, $x[\lvert n\rvert]$, $x[\lvert n\rvert+n]$, $x[3n]$.
> 6. **Stored sample $x[0]$, $x[2]$, $x[3]$ ⇒ time-varying *and* non-causal.**
>
> **Causal?** Any input index larger than $n$?
> 7. **$x[f(n)]$: test negative and positive $n$.** $x[\lvert n\rvert]$ at $n = -3$; $x[2n]$, $x[\lvert n\rvert+n]$ at $n = 1$.
> 8. **Convolution: causal iff $h[n] = 0$ for $n<0$:** $u[n+1]$, $2^n u[-n]$ fail.
>
> **Stable?**
> 9. **Convolution: iff $\sum_n\lvert h[n]\rvert < \infty$.** $2^n u[-n]$ sums to 2 ✓; $j^n u[n]$, $(-1)^n u[n]$, $u[n+1]$ ✗.
> 10. **Memoryless $g(x[n])$: iff $g$ maps bounded to bounded.** $e^{x}$, $\sin$, $\sin^2$, $\lvert\cdot\rvert$, $x^p$, clip, max ✓; $\ln\lvert x\rvert$, division by $x[2]$ ✗ (at 0).
> 11. **Gain in $n$: iff bounded.** $\lvert n\rvert$, $\log(\lvert n\rvert+1)$, $n$, $(n+1)$, $1.13^n$ ✗; $\tfrac{1}{\lvert n\rvert+1}$, $(\tfrac12)^{\lvert n\rvert}$, $\cos(\cdot)$ ✓. $n(x[n]-x[n-1])$ with $x = (-1)^n$ gives $2n(-1)^n$.

## 2. The exam tables (all 20 systems)

All match the official keys; FA2019 writes SV for time-varying, LSI for LTI.

| system | L | TI | C | S | why | exam |
|---|---|---|---|---|---|---|
| $y[n] = \lvert n\rvert\,x[n]$ | Yes | No | Yes | No | gain $\lvert n\rvert$ depends on $n$ (TV) and is unbounded: $x = 1$ gives $\lvert n\rvert$ | [[exams/midterm-1/past-exams/fall-2025\|FA2025 #2]] |
| $y[n] = \lvert x[n]-x[n-1]\rvert$ | No | Yes | Yes | Yes | $\lvert\cdot\rvert$ fails $a=-1$; only present/past samples; $\lvert y\rvert \le 2B$ | [[exams/midterm-1/past-exams/fall-2025\|FA2025 #2]] |
| $y[n] = x[n] * 2^n u[-n]$ | Yes | Yes | No | Yes | convolution ⇒ LTI; $h[-1] = \tfrac12 \ne 0$ ⇒ non-causal; $\sum_{n\le0}2^n = 2$ | [[exams/midterm-1/past-exams/fall-2025\|FA2025 #2]] |
| $y[n] = x[n] * j^n u[n]$ | Yes | Yes | Yes | No | $h = 0$ for $n<0$; $\lvert h[n]\rvert = 1$ for all $n \ge 0$; $x = j^n u[n]$ gives $(n+1)j^n$ | [[exams/midterm-1/past-exams/spring-2025\|SP2025 #2]] |
| $y[n] = 2x[\lvert n\rvert] + 10$ | No | No | No | Yes | $+10$ ⇒ not linear; $x[\lvert n\rvert]$ ⇒ TV; $y[-1] = 2x[1]+10$ (future); $\lvert y\rvert \le 2B+10$ | [[exams/midterm-1/past-exams/spring-2025\|SP2025 #2]] |
| $y[n] = e^{x[n]+1}$ | No | Yes | Yes | Yes | $x = 0$ gives $e \ne 0$; memoryless; $\lvert y\rvert \le e^{B+1}$ | [[exams/midterm-1/past-exams/spring-2025\|SP2025 #2]] |
| $y[n] = x[n]\,x[n+1]$ | No | Yes | No | Yes | product of samples; $x[n+1]$ is a future sample; $\lvert y\rvert \le B^2$ | [[exams/midterm-1/past-exams/fall-2024\|FA2024 #2]] |
| $y[n] = \frac{1}{\lvert n\rvert+1}\,x[n]$ | Yes | No | Yes | Yes | gain depends on $n$ but is $\le 1$ | [[exams/midterm-1/past-exams/fall-2024\|FA2024 #2]] |
| $y[n] = \sin(x[n]) + x[0]$ | No | No | No | Yes | $\sin$ nonlinear; stored $x[0]$ ⇒ TV, and $y[-1]$ needs $x[0]$; $\lvert y\rvert \le 1+B$ | [[exams/midterm-1/past-exams/fall-2024\|FA2024 #2]] |
| $y[n] = \log(\lvert n\rvert+1)\,x[n]$ | Yes | No | Yes | No | gain grows (slowly!) without bound: $x = 1$ gives $\log(\lvert n\rvert+1)$ | [[exams/midterm-1/past-exams/fall-2023\|FA2023 #2]] |
| $y[n] = x[n] * u[n+1]$ | Yes | Yes | No | No | $h[-1] = 1$ ⇒ non-causal; $\sum\lvert h\rvert = \infty$ | [[exams/midterm-1/past-exams/fall-2023\|FA2023 #2]] |
| $y[n] = x[n] + 3$ | No | Yes | Yes | Yes | zero in gives 3 out (affine, not linear) | [[exams/midterm-1/past-exams/fall-2023\|FA2023 #2]] |
| $y[n] = x[n] * (-1)^n u[n]$ | Yes | Yes | Yes | No | $\lvert h\rvert = 1$ for $n \ge 0$; $x = (-1)^n u[n]$ gives $(n+1)(-1)^n$ | [[exams/midterm-1/past-exams/spring-2023\|SP2023 #2]] |
| $y[n] = \dfrac{x[n]}{x[2]}$ | No | No | No | No | scaling $x$ leaves $y$ unchanged; stored $x[2]$ ⇒ TV, and $y[0]$ needs $x[2]$; bounded input with $x[2] = 0$ ⇒ division by zero | [[exams/midterm-1/past-exams/spring-2023\|SP2023 #2]] |
| $y[n] = \cos^2(\tfrac\pi2 n)\,x[n]$ | Yes | No | Yes | Yes | gain is 1 at even $n$, 0 at odd $n$: $\delta[n]$ passes, $\delta[n-1]$ is blocked | [[exams/midterm-1/past-exams/spring-2023\|SP2023 #2]] |
| $y[n] = x[n]\cos(\tfrac\pi3(n-2))$ | Yes | No | Yes | Yes | the $-2$ is inside the cosine, not the input: an $n$-dependent gain, $\le 1$ | [[exams/midterm-1/past-exams/spring-2021\|SP2021 #3]] |
| $y[n] = x[3]\,x[n]$ | No | No | No | Yes | doubling $x$ quadruples $y$; stored $x[3]$ ⇒ TV and non-causal; $\lvert y\rvert \le B^2$ | [[exams/midterm-1/past-exams/spring-2021\|SP2021 #3]] |
| $y[n] = (0.8+0.8j)^n\,x[n]$ | Yes | No | Yes | No | $\lvert 0.8+0.8j\rvert = 0.8\sqrt2 \approx 1.13 > 1$: $x = 1$ gives $\lvert y\rvert = 1.13^n \to \infty$ | [[exams/midterm-1/past-exams/spring-2021\|SP2021 #3]] |
| $y[n] = x[\lvert n\rvert+n]$ | Yes | No | No | *(Yes)* | index is $2n$ for $n \ge 0$ and $0$ for $n<0$ ⇒ TV; $y[1] = x[2]$ ⇒ non-causal | [[exams/midterm-1/past-exams/fall-2019\|FA2019 #2(a)]] |
| $y[n] = (0.2)^{\lvert n\rvert}\log(x[n])$ | No | No | Yes | *(No)* | $\log$ nonlinear; $n$-dependent factor ⇒ SV; memoryless ⇒ causal; $\log 0 = -\infty$ | [[exams/midterm-1/past-exams/fall-2019\|FA2019 #2(b)]] |

*(Italic)* entries: FA2019 #2 did not ask about stability; these are our answers.

> [!trap] Where the points go
> - Bounded $h$ ($j^n u[n]$, $(-1)^n u[n]$, $u[n+1]$) is not stable; only $\sum\lvert h\rvert$ counts.
> - Unbounded gains ($\lvert n\rvert$, $\log(\lvert n\rvert+1)$) break stability even for bounded $x$.
> - $\cos(\tfrac\pi3(n-2))$ is a gain, not a delay; $\ln\lvert x\rvert$ is unstable, $e^{x}$ is not.

## 3. Homework systems (HW1 #5–6, HW2 #1)

Homework asked L and TI only; *italic* C/S entries are ours.

| system | L | TI | C | S | why | source |
|---|---|---|---|---|---|---|
| clipping: $y = b$ if $x[n] \ge b$, $x[n]$ if $a<x[n]<b$, $a$ if $x[n] \le a$ | No | Yes | *Yes* | *Yes* | $a=-2$, $b=2$: $T(3) = 2$ but $T(6) = 2 \ne 2\cdot2$; the rule ignores $n$; $\lvert y\rvert \le \max(\lvert a\rvert,\lvert b\rvert)$ | [[homework/hw1\|HW1 #5]] |
| windowing: $y[n] = x[n]$ for $0 \le n \le N-1$, else 0 | Yes | No | *Yes* | *Yes* | $y = w[n]\,x[n]$ with the fixed window $w = u[n]-u[n-N]$: an $n$-dependent gain $\le 1$ | [[homework/hw1\|HW1 #6]] |
| $y[n] = y[n-5] + x[n] + 10x[n-1]$ | Yes | Yes | *Yes* | *No* | LCCDE at initial rest ⇒ LTI; $H = \frac{1+10z^{-1}}{1-z^{-5}}$ has 5 poles **on** $\lvert z\rvert = 1$ | [[homework/hw2\|HW2 #1(a)]] |
| $y[n-2] + 2y[n] = \cos(\tfrac\pi6 n)\,x[n]$ | Yes | No | *Yes* | *Yes* | input times $\cos(\tfrac\pi6 n)$ ⇒ TV; then a fixed recursion with poles $\pm j/\sqrt2$, inside the unit circle | [[homework/hw2\|HW2 #1(b)]] |
| $y[n] = (\tfrac12)^{\lvert n\rvert}\,x[n]$ | Yes | No | *Yes* | *Yes* | $n$-dependent gain $\le 1$ | [[homework/hw2\|HW2 #1(c)]] |

## 4. Lecture 3 practice list

From the Lecture 3 slides (practice, extra practice, annotated) and notes exercises.

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
> - **SP2023 $x[n]/x[2]$:** Stable = No needs the input with $x[2] = 0$; Linear = No since $\dfrac{a\,x[n]}{a\,x[2]} = \dfrac{x[n]}{x[2]} \ne a\,y[n]$.
> - **SP2021 $(0.8+0.8j)^n x[n]$:** key writes $\sqrt{1.28}\,e^{j\pi/4}$, "goes to $\infty$ as $n \to \infty$"; one direction suffices.

> [!warning] Answer-key erratum (HW1 solution #5(b))
> For the key's counterexample ($x_1 = 1$, $x_2 = n^2$, clip to $[a, b] = [0, 4]$) it prints $T(x_1)+T(x_2) = \{\dots,5,4,2,\underset{\uparrow}{1},2,4,5,\dots\}$; at $n = \pm2$ it is $T(1) + T(4) = 1 + 4 = 5$, so $\{\dots,5,5,2,\underset{\uparrow}{1},2,5,5,\dots\}$. The conclusion (not linear) stands; see [[0-toolkit/05-errata|Errata]].

## Related

[[problems/classifying-system-properties|Classifying system properties (recipe)]] · [[exams/midterm-1/true-false-bank|True/False bank]] · [[concepts/linearity|Linearity]] · [[concepts/time-invariance|Time-invariance]] · [[concepts/causality|Causality]] · [[concepts/bibo-stability|BIBO stability]]

### Sources for this page

Official keys FA2019–FA2025 (#2; SP2021 #3); HW1 #5–6, HW2 #1 solutions; Lecture 3 slides and notes, Exercises 1–7.
