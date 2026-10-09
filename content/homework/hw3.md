---
title: "HW3 · The z-transform, its properties, and its inverse"
description: "Worked solutions to ECE 310 Homework 3 (Fall 2026): five z-transforms with their ROCs, new transforms from old ones by properties (shift, scaling, modulation, differentiation, convolution), inverse transforms by inspection and partial fractions, and the poles, zeros, ROC and impulse response of a right-sided system, with the rubric lessons and the past-exam problems that reuse each idea."
tags: [homework, midterm-1, z-transform, roc]
---

*Homework 3 · due Fri Sep 18, 2026 (Gradescope) · Lectures 6–8, plus the transfer-function vocabulary of Lecture 9 · 100 points (30 + 30 + 24 + 16) · official solutions v1.0 · prev: [[homework/hw2|HW2]] · next: [[homework/hw4|HW4]] · [[homework/index|all homework]]*

> [!abstract] What HW3 trains
> Six of the seven past Midterm 1 exams have a "z-transform with ROC" problem and all seven have an "inverse z / PFE" problem. HW3 drills both: compute $X(z)$ **and** its ROC from the definition or from pairs (#1), get new transforms from old ones with properties instead of sums (#2), go backwards by inspection and by partial fractions (#3), and read poles, zeros, ROC and $h[n]$ off a transfer function (#4).

| # | skill | problem family · lecture |
|---|---|---|
| 1 | $X(z)$ + ROC: shifted deltas, a shifted exponential, a two-sided signal, $a^{\lvert n\rvert}$, a finite-length signal | [[problems/z-transform-with-roc\|z-transform with ROC]] · [[2-z-transform/06-the-z-transform\|L6]] |
| 2 | properties: shift, multiplication by $a^n$, modulation by a cosine, differentiation ($n\,x[n]$), convolution | [[problems/z-transform-with-roc\|z-transform with ROC]] · [[2-z-transform/07-z-transform-properties\|L7]] |
| 3 | inverse $z$: FIR by inspection, a delayed pair, ROC → sidedness, PFE | [[problems/all-possible-rocs\|inverse z / PFE / ROCs]] · [[2-z-transform/08-inverse-z-transform\|L8]] |
| 4 | poles and zeros, ROC of a right-sided system, pole-zero plot, $h[n]$ by PFE | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z) ↔ response]] · [[2-z-transform/09-transfer-functions\|L9]] |

> [!tip] What the rubric punished (the exam grades the same way)
> - **#1: a correct $X(z)$ with a wrong or missing ROC earned 3 of 6 points.** The ROC is half the answer, every time.
> - #2: −1 for an ROC that misses one side of the boundary (e.g. $\lvert z\rvert>\tfrac13$ when $z=\infty$ must be excluded) or drops the absolute value ($z>\tfrac13$); −1.5 for a minor slip in $X(z)$.
> - #3: −2 for a numerical mistake in one or two terms. PFE coefficients are where these happen: check them by recombining, or with `residuez` (end of the page).
> - #4: the sketch is graded separately for zeros, poles and ROC (−1 each).

## Problem 1 — five z-transforms and their ROCs

> [!question] Problem 1 (30 pts)
> For each discrete-time signal, (i) determine the z-transform and (ii) state the region of convergence (ROC).
>
> (a) $x_1[n] = \delta[n+3] + 4\delta[n] - \delta[n-2]$
>
> (b) $x_2[n] = \left(\tfrac34\right)^{n+3} u[n-2]$
>
> (c) $x_3[n] = 3^n u[-n] + 2^{-n} u[n]$
>
> (d) $x_4[n] = \left(\tfrac14\right)^{\lvert n\rvert}$
>
> (e) $x_5[n] = n\left(\tfrac12\right)^n \big(u[n] - u[n-5]\big)$

> [!success]- Solution (a) — shifted deltas
> $x_1[n] = \{1,\ 0,\ 0,\ \underset{\uparrow}{4},\ 0,\ -1\}$, running from $n=-3$ to $n=2$. Each $\delta[n-k]$ contributes $z^{-k}$:
> $$
> X_1(z) = z^{3} + 4 - z^{-2}.
> $$
> The term $z^{3}$ blows up at $z=\infty$ (a sample at $n<0$) and $z^{-2}$ blows up at $z=0$ (a sample at $n>0$), so both points are excluded.
>
> **Answer.** $X_1(z) = z^{3} + 4 - z^{-2}$, **ROC: $0 < \lvert z\rvert < \infty$**.

> [!success]- Solution (b) — make the exponent match the shift of the step
> The step starts at $n=2$, so rewrite the exponent as $(n-2)$ plus a constant:
> $$
> x_2[n] = \left(\tfrac34\right)^{5}\left(\tfrac34\right)^{n-2}u[n-2].
> $$
> Now use $\left(\tfrac34\right)^n u[n] \leftrightarrow \dfrac{1}{1-\frac34 z^{-1}}$ ($\lvert z\rvert > \tfrac34$) and the delay property (a delay by 2 multiplies by $z^{-2}$):
> $$
> X_2(z) = \left(\tfrac34\right)^{5}\frac{z^{-2}}{1-\frac34 z^{-1}} = \frac{243}{1024}\cdot\frac{z^{-2}}{1-\frac34 z^{-1}} .
> $$
> From the definition instead: $\sum_{n=2}^{\infty}\left(\tfrac34\right)^{n+3}z^{-n}$ is geometric with ratio $\tfrac34 z^{-1}$ and converges iff $\lvert \tfrac34 z^{-1}\rvert < 1$.
>
> **Answer.** $X_2(z) = \dfrac{(3/4)^{5}\,z^{-2}}{1-\frac34 z^{-1}}$, **ROC: $\lvert z\rvert > \tfrac34$** (causal, so $z=\infty$ is included).

> [!warning] Typo in the official solution, 1(b)
> One intermediate line of the key reads $\dfrac{(3/4)^{3}z^{-2}}{1-(3/4)z^{-1}}$, which drops the factor $(3/4)^{2}$ produced by the substitution $k = n-2$. The next line ("simplifying the numerator") has the correct $(3/4)^{5}$; the key's final answer is right.

> [!success]- Solution (c) — a left-sided piece that includes n = 0
> Split into the two pieces and sum each geometric series.
>
> Right-sided part: $\displaystyle\sum_{n=0}^{\infty}2^{-n}z^{-n} = \frac{1}{1-\frac12 z^{-1}}$, converging for $\lvert z\rvert > \tfrac12$.
>
> Left-sided part (substitute $k=-n$): $\displaystyle\sum_{n=-\infty}^{0}3^{n}z^{-n} = \sum_{k=0}^{\infty}\left(\frac{z}{3}\right)^{k} = \frac{1}{1-\frac13 z}$, converging for $\lvert z\rvert < 3$. In powers of $z^{-1}$: $\dfrac{1}{1-\frac13 z} = \dfrac{-3z^{-1}}{1-3z^{-1}}$ (multiply top and bottom by $-3z^{-1}$).
>
> The ROC is the overlap $\tfrac12 < \lvert z\rvert < 3$, which is non-empty, so the transform exists.
>
> **Answer.** $X_3(z) = \dfrac{1}{1-\frac12 z^{-1}} + \dfrac{1}{1-\frac13 z} = \dfrac{1}{1-\frac12 z^{-1}} - \dfrac{3z^{-1}}{1-3z^{-1}}$, **ROC: $\tfrac12 < \lvert z\rvert < 3$**.

> [!trap] 3ⁿu[−n] is not the table's left-sided pair
> The table pair $-a^{n}u[-n-1] \leftrightarrow \dfrac{1}{1-az^{-1}}$, $\lvert z\rvert < \lvert a\rvert$, stops at $n=-1$. This signal also has the sample at $n=0$: $3^{n}u[-n] = \delta[n] + 3^{n}u[-n-1]$, whose transform is $1 - \dfrac{1}{1-3z^{-1}} = \dfrac{-3z^{-1}}{1-3z^{-1}}$. Writing $\pm\dfrac{1}{1-3z^{-1}}$ is the classic slip.

> [!success]- Solution (d) — a^|n| gives a reciprocal pair of poles
> For $n\ge0$, $x_4[n] = \left(\tfrac14\right)^n$; for $n\le-1$, $x_4[n] = \left(\tfrac14\right)^{-n} = 4^{n}$. So
> $$
> x_4[n] = \left(\tfrac14\right)^{n}u[n] + 4^{n}u[-n-1] = \left(\tfrac14\right)^{n}u[n] - \Big(-4^{n}u[-n-1]\Big).
> $$
> The first term gives $\dfrac{1}{1-\frac14 z^{-1}}$ for $\lvert z\rvert > \tfrac14$; the second is **minus** the left-sided pair with $a=4$, i.e. $-\dfrac{1}{1-4z^{-1}}$ for $\lvert z\rvert < 4$.
>
> **Answer.** $X_4(z) = \dfrac{1}{1-\frac14 z^{-1}} - \dfrac{1}{1-4z^{-1}} = \dfrac{-\frac{15}{4}z^{-1}}{\left(1-\frac14 z^{-1}\right)\left(1-4z^{-1}\right)}$, **ROC: $\tfrac14 < \lvert z\rvert < 4$**.
>
> The key's geometric-series form $\dfrac{1}{1-\frac14 z^{-1}} + \dfrac{\frac14 z}{1-\frac14 z}$ is the same function. Poles at $a$ and $1/a$ are the fingerprint of $a^{\lvert n\rvert}$.

> [!success]- Solution (e) — finite length: list the samples
> $u[n]-u[n-5]$ keeps $n = 0,1,2,3,4$ (five samples). Multiply by $n\left(\tfrac12\right)^n$:
> $$
> x_5[n] = \{\underset{\uparrow}{0},\ \tfrac12,\ \tfrac12,\ \tfrac38,\ \tfrac14\} = \tfrac12\delta[n-1] + \tfrac12\delta[n-2] + \tfrac38\delta[n-3] + \tfrac14\delta[n-4].
> $$
> **Answer.** $X_5(z) = \tfrac12 z^{-1} + \tfrac12 z^{-2} + \tfrac38 z^{-3} + \tfrac14 z^{-4}$, **ROC: $\lvert z\rvert > 0$** (every $z\neq0$; $z=\infty$ is included because no sample sits at $n<0$).

> [!trap] Finite-length ROCs: check both ends
> Only two points can be missing from a finite-length signal's ROC: $z=0$ (if a sample sits at $n>0$) and $z=\infty$ (if a sample sits at $n<0$). (a) loses both, (e) loses only $z=0$. "ROC: all $z$" for (a) costs the point.

**On the exam:** [[exams/midterm-1/past-exams/fall-2024|FA2024 #5(c)]] is 1(c) almost verbatim ($3^{-n}u[n] + 3^{n}u[-n]$, ROC $\tfrac13 < \lvert z\rvert < 3$); [[exams/midterm-1/past-exams/spring-2025|SP2025 #5(b)]] ($3^n u[-n+2]$) is the left-sided trap of 1(c) with a shift; [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]] and [[exams/midterm-1/past-exams/fall-2025|FA2025 #5(b)]] are finite-length like 1(a) and 1(e). Recipe: [[problems/z-transform-with-roc|z-transform with ROC]].

## Problem 2 — properties instead of sums

> [!question] Problem 2 (30 pts)
> We are given the z-transform pair
> $$
> x[n] \overset{\mathcal{Z}}{\longleftrightarrow} X(z) = \frac{1}{1-\frac13 z^{-1}},\qquad \text{ROC: } \lvert z\rvert > \tfrac13 .
> $$
> Using properties of the z-transform, determine the z-transform of each of the following signals and state the ROC.
>
> (a) $x_1[n] = x[n+3]$
>
> (b) $x_2[n] = 2^{n}x[n]$
>
> (c) $x_3[n] = \cos\!\left(\tfrac{\pi}{4}n\right)x[n]$
>
> (d) $x_4[n] = n(n-2)\,x[n-1]$
>
> (e) $x_5[n] = \left(\tfrac15\right)^{n}u[n] * x[n]$

(Here $x[n] = \left(\tfrac13\right)^n u[n]$, which is handy for checking.)

> [!success]- Solution (a) — time shift
> Shift property: $x[n-n_0] \leftrightarrow z^{-n_0}X(z)$, here with $n_0 = -3$.
>
> **Answer.** $X_1(z) = \dfrac{z^{3}}{1-\frac13 z^{-1}}$, **ROC: $\tfrac13 < \lvert z\rvert < \infty$**.
>
> The advance puts samples at $n=-3,-2,-1$, so $z=\infty$ must now be excluded: this is exactly the "missing one side of the boundary" deduction.

> [!success]- Solution (b) — multiplication by a^n (z-scaling)
> $a^{n}x[n] \leftrightarrow X\!\left(\dfrac{z}{a}\right)$ with ROC $\lvert a\rvert R_x$. With $a=2$, every $z^{-1}$ becomes $2z^{-1}$:
> $$
> X_2(z) = \frac{1}{1-\frac13\,(2z^{-1})} = \frac{1}{1-\frac23 z^{-1}} .
> $$
> Direct check: $2^n\left(\tfrac13\right)^n u[n] = \left(\tfrac23\right)^n u[n]$.
>
> **Answer.** $X_2(z) = \dfrac{1}{1-\frac23 z^{-1}}$, **ROC: $\lvert z\rvert > \tfrac23$** (the pole and the ROC boundary both scale by $\lvert a\rvert = 2$).

> [!success]- Solution (c) — a cosine is two complex scalings
> Euler: $\cos\!\left(\tfrac{\pi}{4}n\right) = \tfrac12\left(e^{j\pi n/4} + e^{-j\pi n/4}\right)$, and $e^{\pm j\pi n/4}$ is an $a^n$ with $\lvert a\rvert = 1$, so each half just rotates the pole:
> $$
> X_3(z) = \frac12\left[\frac{1}{1-\frac13 e^{j\pi/4}z^{-1}} + \frac{1}{1-\frac13 e^{-j\pi/4}z^{-1}}\right]
> = \frac{1-\frac{\sqrt2}{6}z^{-1}}{1-\frac{\sqrt2}{3}z^{-1}+\frac19 z^{-2}} .
> $$
> For the combined form use $(1-az^{-1})(1-a^{*}z^{-1}) = 1-2\,\mathrm{Re}(a)\,z^{-1}+\lvert a\rvert^{2}z^{-2}$ with $a = \tfrac13 e^{j\pi/4}$: $2\,\mathrm{Re}(a) = \tfrac{\sqrt2}{3}$ and $\lvert a\rvert^2 = \tfrac19$.
>
> **Answer.** Either form above, **ROC: $\lvert z\rvert > \tfrac13$** (unchanged, because $\lvert e^{\pm j\pi/4}\rvert = 1$). The poles sit at $\tfrac13 e^{\pm j\pi/4}$.

> [!trap] Which way does the pole rotate?
> $e^{j\omega_0 n}x[n] \leftrightarrow X\!\left(e^{-j\omega_0}z\right)$: the pole moves to $\tfrac13 e^{+j\omega_0}$, the **same** angle as the modulating exponential. In 2(c) both signs appear, so a slip is invisible; for a single exponential such as $e^{j\pi n/3}u[n+4]$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #5(a)]]) it is the whole answer.

> [!success]- Solution (d) — shift first, then differentiate (twice)
> The factors of $n$ multiply the **shifted** signal, so start from $g[n] = x[n-1]$:
> $$
> G(z) = z^{-1}X(z) = \frac{z^{-1}}{1-\frac13 z^{-1}} = \frac{1}{z-\frac13},\qquad \lvert z\rvert > \tfrac13 .
> $$
> Differentiation: $n\,g[n] \leftrightarrow -zG'(z)$. Applying it twice (product rule): ${n^{2}g[n] \leftrightarrow -z\tfrac{d}{dz}\big(-zG'(z)\big)} = zG'(z) + z^{2}G''(z)$. Since $n(n-2) = n^2 - 2n$,
> $$
> X_4(z) = \underbrace{zG' + z^{2}G''}_{n^{2}g[n]} \;-\; 2\underbrace{\left(-zG'\right)}_{n\,g[n]} = 3zG'(z) + z^{2}G''(z).
> $$
> With $G' = -\dfrac{1}{\left(z-\frac13\right)^{2}}$ and $G'' = \dfrac{2}{\left(z-\frac13\right)^{3}}$:
> $$
> X_4(z) = -\frac{3z}{\left(z-\frac13\right)^{2}} + \frac{2z^{2}}{\left(z-\frac13\right)^{3}} = \frac{-3z\left(z-\frac13\right)+2z^{2}}{\left(z-\frac13\right)^{3}} = \frac{z-z^{2}}{\left(z-\frac13\right)^{3}} .
> $$
> **Answer.** $X_4(z) = \dfrac{z-z^{2}}{\left(z-\frac13\right)^{3}} = \dfrac{z^{-2}-z^{-1}}{\left(1-\frac13 z^{-1}\right)^{3}}$, **ROC: $\lvert z\rvert > \tfrac13$** (differentiation does not change the ROC, and the result is proper, so $z=\infty$ stays in).
>
> **Sanity check (worth 30 seconds on the exam).** $x_4[n] = n(n-2)\left(\tfrac13\right)^{n-1}u[n-1]$ starts $x_4[1] = -1$, $x_4[2] = 0$, $x_4[3] = \tfrac13$, $x_4[4] = \tfrac{8}{27}$, and long division of the answer gives $-z^{-1} + 0\cdot z^{-2} + \tfrac13 z^{-3} + \tfrac{8}{27}z^{-4} + \cdots$ ✓. The key's alternative form $\dfrac{27z-27z^{2}}{(3z-1)^{3}}$ is the same function.

> [!trap] Differentiate the right transform
> Applying $-z\,\frac{d}{dz}$ to $X(z)$ and multiplying by $z^{-1}$ afterwards computes the transform of $(n-1)(n-3)\,x[n-1]$, not of $n(n-2)\,x[n-1]$. The derivative acts on the transform of whatever the $n$ multiplies, here $x[n-1]$.

> [!success]- Solution (e) — convolution becomes multiplication
> $\left(\tfrac15\right)^n u[n] \leftrightarrow \dfrac{1}{1-\frac15 z^{-1}}$ ($\lvert z\rvert > \tfrac15$), and convolution ↔ product, with ROC at least the intersection of the two ROCs.
>
> **Answer.** $X_5(z) = \dfrac{1}{\left(1-\frac15 z^{-1}\right)\left(1-\frac13 z^{-1}\right)}$, **ROC: $\lvert z\rvert > \tfrac13$**.
>
> Bonus (cover-up at $z = \tfrac13$ and $z = \tfrac15$): $x_5[n] = \left[\tfrac52\left(\tfrac13\right)^n - \tfrac32\left(\tfrac15\right)^n\right]u[n]$, the same result as grinding out the convolution sum ([[problems/infinite-length-convolution|infinite-length convolution]]).

**On the exam:** [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] is 2(d) in miniature ($(n+1)x[n]$ with $X = 1/(1-\tfrac12 z^{-1})$); [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]] ($n\,u[n+1]$) and [[exams/midterm-1/past-exams/fall-2024|FA2024 #5(a)]] ($(n+1)u[n-1]$) combine differentiation with a shift; [[exams/midterm-1/past-exams/fall-2025|FA2025 #5(c)]] ($\cos^2(\pi n/4)u[n]$) is 2(c) after one Euler step.

## Problem 3 — inverse transforms

> [!question] Problem 3 (24 pts)
> The transfer function $H(z)$ and ROC of several systems are given. Determine the corresponding impulse response $h[n]$ of each system.
>
> (a) $H_1(z) = 1 - \tfrac23 z^{-1} + \tfrac49 z^{-2} - \tfrac{8}{27}z^{-3}$, ROC: $z\neq0$
>
> (b) $H_2(z) = \dfrac{3z^{-2}}{1+2z^{-1}}$, ROC: $\lvert z\rvert > 2$
>
> (c) $H_3(z) = \dfrac{1}{1-\frac14 z^{-1}} + \dfrac{1}{1-\frac32 z^{-1}}$, ROC: $\tfrac14 < \lvert z\rvert < \tfrac32$
>
> (d) $H_4(z) = \dfrac{1}{\left(1-\frac23 z^{-1}\right)\left(1-z^{-1}\right)}$, ROC: $\lvert z\rvert > 1$

> [!success]- Solution (a) — a polynomial in z⁻¹ is read off term by term
> $z^{-k} \leftrightarrow \delta[n-k]$:
>
> **Answer.** $h_1[n] = \delta[n] - \tfrac23\delta[n-1] + \tfrac49\delta[n-2] - \tfrac{8}{27}\delta[n-3] = \left(-\tfrac23\right)^{n}\big(u[n]-u[n-4]\big)$, i.e. $h_1 = \{\underset{\uparrow}{1},\ -\tfrac23,\ \tfrac49,\ -\tfrac{8}{27}\}$: causal FIR, consistent with the ROC $z\neq0$.

> [!success]- Solution (b) — a pair times a delay
> $\dfrac{1}{1+2z^{-1}} = \dfrac{1}{1-(-2)z^{-1}}$ with $\lvert z\rvert > 2$ (outside the pole) is the right-sided $(-2)^n u[n]$. The factor $3z^{-2}$ scales by 3 and delays by 2, and the delay applies to the **whole** sequence:
>
> **Answer.** $h_2[n] = 3(-2)^{n-2}u[n-2]$ (not $3(-2)^{n}u[n-2]$).

> [!success]- Solution (c) — the ROC decides each term's side
> The ROC $\tfrac14 < \lvert z\rvert < \tfrac32$ lies **outside** the pole $\tfrac14$, so that term is right-sided; it lies **inside** the pole $\tfrac32$, so that term is left-sided ($-a^{n}u[-n-1]$).
>
> **Answer.** $h_3[n] = \left(\tfrac14\right)^{n}u[n] - \left(\tfrac32\right)^{n}u[-n-1]$.
>
> It is two-sided, and stable because the ROC contains $\lvert z\rvert = 1$ (a preview of [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]).

> [!success]- Solution (d) — partial fractions, then both terms right-sided
> $$
> H_4(z) = \frac{A_1}{1-\frac23 z^{-1}} + \frac{A_2}{1-z^{-1}},
> $$
> $$
> A_1 = \left.\frac{1}{1-z^{-1}}\right|_{z^{-1}=\frac32} = \frac{1}{1-\frac32} = -2,\qquad
> A_2 = \left.\frac{1}{1-\frac23 z^{-1}}\right|_{z^{-1}=1} = \frac{1}{1-\frac23} = 3 .
> $$
> The ROC $\lvert z\rvert > 1$ is outside both poles, so both terms are right-sided.
>
> **Answer.** $h_4[n] = \left[3 - 2\left(\tfrac23\right)^{n}\right]u[n]$.
>
> Checks: $h_4[0] = 1 = H_4(\infty)$ ✓. Also $H_4$ is an accumulator $\frac{1}{1-z^{-1}}$ applied to $\left(\tfrac23\right)^n u[n]$, and $\sum_{k=0}^{n}\left(\tfrac23\right)^k = 3-2\left(\tfrac23\right)^n$ ✓. Not stable: $h_4[n]\to3$, because the pole at $z=1$ keeps the unit circle out of the ROC $\lvert z\rvert > 1$.

**On the exam:** [[exams/midterm-1/past-exams/fall-2019|FA2019 #6]] ($Y = 1 + z^{-100} + \frac{1}{1-5z^{-1}}$, find $y$) is 3(a) + 3(b) by inspection; the "ROC picks each term's side" step of 3(c) and the PFE of 3(d) are in every inverse-z problem: [[exams/midterm-1/past-exams/fall-2023|FA2023 #6(a)]], [[exams/midterm-1/past-exams/fall-2025|FA2025 #7(a)]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]]. Recipe: [[problems/all-possible-rocs|all possible ROCs]].

## Problem 4 — a right-sided system

> [!question] Problem 4 (16 pts)
> Consider a right-sided LTI system with transfer function
> $$
> H(z) = \frac{1-3z^{-1}}{1+\frac16 z^{-1}-\frac13 z^{-2}} .
> $$
> (a) Determine the poles and zeros of $H(z)$. (b) Determine the ROC of $H(z)$ and sketch the pole-zero plot. (c) Determine the impulse response $h[n]$ of this system.

> [!success]- Solution (a) — multiply through by z² before reading off zeros
> $$
> H(z) = \frac{z^{2}-3z}{z^{2}+\frac16 z-\frac13} = \frac{z\,(z-3)}{\left(z-\frac12\right)\left(z+\frac23\right)} .
> $$
> Check: $\left(z-\tfrac12\right)\left(z+\tfrac23\right) = z^2 + \tfrac16 z - \tfrac13$ ✓. In powers of $z^{-1}$ the denominator is $\left(1+\tfrac23 z^{-1}\right)\left(1-\tfrac12 z^{-1}\right)$.
>
> **Answer.** Zeros at $z = 0$ and $z = 3$; poles at $z = \tfrac12$ and $z = -\tfrac23$.

> [!warning] The key lists only the zero at z = 3
> In positive powers the numerator is $z^2 - 3z = z(z-3)$, so $H(0) = 0$ and $z = 0$ is a zero too. The key's own pole-zero plot shows both; list both.

> [!success]- Solution (b) — right-sided means outside the outermost pole
> **Answer.** ROC: $\lvert z\rvert > \max\left(\tfrac12,\ \tfrac23\right)$, i.e. **$\lvert z\rvert > \tfrac23$**. Sketch: × at $\tfrac12$ and $-\tfrac23$, ○ at $0$ and $3$, everything outside the circle of radius $\tfrac23$ shaded (figure below).
>
> The ROC contains the unit circle, so the system is also BIBO stable. Not asked here, but on an exam it is usually the next question.

> [!success]- Solution (c) — PFE with the factored denominator
> $$
> H(z) = \frac{1-3z^{-1}}{\left(1+\frac23 z^{-1}\right)\left(1-\frac12 z^{-1}\right)} = \frac{A_1}{1+\frac23 z^{-1}} + \frac{A_2}{1-\frac12 z^{-1}},
> $$
> $$
> \begin{aligned}
> A_1 &= \left.\frac{1-3z^{-1}}{1-\frac12 z^{-1}}\right|_{z^{-1}=-\frac32} = \frac{1+\frac92}{1+\frac34} = \frac{22}{7},\\
> A_2 &= \left.\frac{1-3z^{-1}}{1+\frac23 z^{-1}}\right|_{z^{-1}=2} = \frac{1-6}{1+\frac43} = -\frac{15}{7}.
> \end{aligned}
> $$
> The system is right-sided, so both terms are right-sided.
>
> **Answer.** $h[n] = \dfrac{22}{7}\left(-\dfrac23\right)^{n}u[n] - \dfrac{15}{7}\left(\dfrac12\right)^{n}u[n]$.
>
> Checks: $h[0] = \tfrac{22}{7}-\tfrac{15}{7} = 1 = H(\infty)$ ✓. From the recursion $y[n] = -\tfrac16 y[n-1] + \tfrac13 y[n-2] + x[n] - 3x[n-1]$ we get $h[1] = -\tfrac16 - 3 = -\tfrac{19}{6}$, and the formula gives $-\tfrac{44}{21} - \tfrac{15}{14} = -\tfrac{19}{6}$ ✓.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 290" width="640" height="290" role="img" aria-label="Pole-zero plot of HW3 problem 4 with the ROC shaded" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M40.0,34.0 H560.0 V266.0 H40.0 Z M202.0,150.0 A52.0,52.0 0 1 0 98.0,150.0 A52.0,52.0 0 1 0 202.0,150.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><rect x="40" y="34" width="520" height="232" fill="none" stroke="currentColor" stroke-width="0.6" opacity="0.35"/><line x1="40.0" y1="150.0" x2="558.0" y2="150.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="564.0,150.0 558.0,146.7 558.0,153.3" fill="currentColor"/><line x1="150.0" y1="266.0" x2="150.0" y2="36.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="150.0,30.0 146.7,36.0 153.3,36.0" fill="currentColor"/><text x="562.0" y="166.0" text-anchor="end" fill="currentColor" style="font-size:11px;">Re</text><text x="156.0" y="42.0" text-anchor="start" fill="currentColor" style="font-size:11px;">Im</text><circle cx="150.0" cy="150.0" r="78.0" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="5 4" opacity="0.75"/><circle cx="150.0" cy="150.0" r="52.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="228.0" y1="146.0" x2="228.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="234.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">1</text><line x1="306.0" y1="146.0" x2="306.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="306.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">2</text><line x1="384.0" y1="146.0" x2="384.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="384.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">3</text><line x1="72.0" y1="146.0" x2="72.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="64.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">−1</text><circle cx="150.0" cy="150.0" r="6.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="384.0" cy="150.0" r="6.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><line x1="183.0" y1="144.0" x2="195.0" y2="156.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="183.0" y1="156.0" x2="195.0" y2="144.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="92.0" y1="144.0" x2="104.0" y2="156.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="92.0" y1="156.0" x2="104.0" y2="144.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="384.0" y="136.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">zero at 3</text><text x="142.0" y="170.0" text-anchor="end" fill="currentColor" style="font-size:12px;">0</text><line x1="415.0" y1="201.0" x2="425.0" y2="211.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="415.0" y1="211.0" x2="425.0" y2="201.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="434.0" y="210.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">poles: z = ½ and z = −⅔</text><circle cx="420.0" cy="230.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="434.0" y="234.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">zeros: z = 0 and z = 3</text><text x="206.2" y="222.2" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">unit circle</text><text x="410.0" y="70.0" text-anchor="start" fill="var(--accent)" style="font-size:14px;font-weight:600;">ROC: |z| &gt; 2/3</text><text x="410.0" y="88.0" text-anchor="start" fill="currentColor" style="font-size:12px;">(right-sided: outside the</text><text x="410.0" y="104.0" text-anchor="start" fill="currentColor" style="font-size:12px;">largest pole; contains |z| = 1,</text><text x="410.0" y="120.0" text-anchor="start" fill="currentColor" style="font-size:12px;">so the system is also stable)</text></svg><figcaption><strong>Poles at ½ and −⅔ (×), zeros at 0 and 3 (○); right-sided, so the ROC is everything outside the circle through the largest pole.</strong> The zero at z = 0 comes from writing H(z) in positive powers: H(z) = z(z−3)/((z−½)(z+⅔)). A zero may sit outside the ROC boundary, as z = 3 does here; only poles are excluded from the ROC.</figcaption></figure>

> [!trap] Zeros are allowed inside the ROC
> Only poles are excluded from an ROC. The zero at $z=3$ sits inside $\lvert z\rvert > \tfrac23$ and the zero at $z=0$ outside it; neither matters for the ROC. "The ROC cannot contain any poles or zeros" is False on [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(b)]] for exactly this reason.

**On the exam:** "poles, zeros and ROC of a causal system" opens [[exams/midterm-1/past-exams/fall-2023|FA2023 #7(a)]], [[exams/midterm-1/past-exams/spring-2023|SP2023 #5(a)]] and [[exams/midterm-1/past-exams/fall-2025|FA2025 #6]]; the same $H \to h$ partial-fraction step is [[exams/midterm-1/past-exams/fall-2019|FA2019 #10]]. Recipe: [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]].

## Checking PFE coefficients in Python

`scipy.signal.residuez(b, a)` returns the coefficients $A_k$ (`r`), the poles $p_k$ (`p`) and any direct terms (`k`) of $H(z) = \sum_k \frac{A_k}{1-p_k z^{-1}} + \dots$, which is exactly the course's PFE form. The ROC is still your job: `lfilter` on an impulse always produces the **causal** inverse.

```python
import numpy as np
from scipy import signal

b = [1, -3]                        # 1 - 3z^-1
a = [1, 1/6, -1/3]                 # 1 + (1/6)z^-1 - (1/3)z^-2
r, p, k = signal.residuez(b, a)    # H = sum r_i / (1 - p_i z^-1) + k
print("A_k:", np.round(r, 4), " p_k:", np.round(p, 4), " k:", k)
print("22/7 =", round(22/7, 4), " -15/7 =", round(-15/7, 4))

n = np.arange(8)
h = signal.lfilter(b, a, (n == 0).astype(float))   # causal impulse response
closed = 22/7 * (-2/3)**n - 15/7 * (1/2)**n
print(np.allclose(h, closed), np.round(h[:4], 4))
```

```text
A_k: [-2.1429  3.1429]  p_k: [ 0.5    -0.6667]  k: []
22/7 = 3.1429  -15/7 = -2.1429
True [ 1.     -3.1667  0.8611 -1.1991]
```

## Related

[[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/partial-fraction-expansion|partial fraction expansion]] · [[concepts/poles-and-zeros|poles and zeros]] · [[0-toolkit/02-geometric-series|geometric series]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · next: [[homework/hw4|HW4]]

### Sources for this page

- ECE 310 Fall 2026 Homework 3 (due Sep 18) and the official HW3 solutions, version 1.0 (Jung Ki & Hao), including the grading rubric quoted above.
- Lecture notes 6–9 (z-transform, properties, inverse z-transform, transfer functions).
- Past Midterm 1 exams cited in the "On the exam" lines (FA2025, SP2025, FA2024, FA2023, SP2023, SP2021, FA2019).
- Every answer on this page was re-derived and checked numerically (partial sums of the z-transform at test points inside each ROC, `lfilter` against the closed forms, `residuez` for the PFEs).
