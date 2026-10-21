---
title: "Classifying system properties (the L / TI / C / S table)"
description: "The yes/no table of Linear, Time-invariant, Causal, Stable that opens every Midterm 1: fast rules that fill a cell in seconds, a recipe per row, the classic traps, three practice problems."
tags: [problem-family, problem, systems, stability, midterm-1]
family_frequency: "7 of 7 exams"
typical_points: "12"
lectures: [3, 4]
---

*Problem family · problem #2 on six of seven past exams (#3 on SP2021) · 12 points, one per cell · [[1-signals-and-systems/03-system-properties|Lecture 3]], [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]*

## What it looks like on the exam

Three systems × **Linear**, **Time-invariant** (older exams: shift-invariant, LSI), **Causal**, **Stable** (BIBO); yes/no, no proofs. Grading varies: SP2025 does not deduct for wrong answers; FA2019 #2 used +2 / −1 / 0. Proof versions are homework (HW1 #5–6, HW2 #1–2).

- [[exams/midterm-1/past-exams/fall-2025|FA2025 #2]]: $\lvert n\rvert\,x[n]$; $\ \lvert x[n]-x[n-1]\rvert$; $\ x[n]*2^n u[-n]$. #4(a): is $y[n]=\frac1L\sum_{k=0}^{L-1}x[n-Sk]$ L? TI?
- [[exams/midterm-1/past-exams/spring-2025|SP2025 #2]]: $x[n]*j^n u[n]$; $\ 2x[\lvert n\rvert]+10$; $\ e^{x[n]+1}$.
- [[exams/midterm-1/past-exams/fall-2024|FA2024 #2]]: $x[n]\,x[n+1]$; $\ \dfrac{x[n]}{\lvert n\rvert+1}$; $\ \sin(x[n])+x[0]$.
- [[exams/midterm-1/past-exams/fall-2023|FA2023 #2]]: $\log(\lvert n\rvert+1)\,x[n]$; $\ x[n]*u[n+1]$; $\ x[n]+3$.
- [[exams/midterm-1/past-exams/spring-2023|SP2023 #2]] (worked in the Midterm 1 review): $x[n]*(-1)^n u[n]$; $\ \dfrac{x[n]}{x[2]}$; $\ \cos^2\!\left(\tfrac{\pi}{2}n\right)x[n]$.
- [[exams/midterm-1/past-exams/spring-2021|SP2021 #3]] (24 pts): $x[n]\cos\!\left(\tfrac{\pi(n-2)}{3}\right)$; $\ x[3]\,x[n]$; $\ (0.8+0.8j)^n x[n]$.
- [[exams/midterm-1/past-exams/fall-2019|FA2019 #2]] (L / SI / C only): $x[\lvert n\rvert+n]$; $\ (0.2)^{\lvert n\rvert}\log x[n]$.
- Homework: [[homework/hw1|HW1 #5–6]], [[homework/hw2|HW2 #1–2]]; Lecture 3 exercises 1–7.

> [!success]- Answers (L / TI / C / S)
> | exam | system | L | TI | C | S | deciding reason |
> |---|---|---|---|---|---|---|
> | FA25 | $\lvert n\rvert x[n]$ | Y | N | Y | N | $x=1$ gives $\lvert n\rvert$ |
> | FA25 | $\lvert x[n]-x[n-1]\rvert$ | N | Y | Y | Y | $\lvert\cdot\rvert$; $\le 2B$ |
> | FA25 | $x*2^n u[-n]$ | Y | Y | N | Y | $h[-1]=\tfrac12\neq0$; $\sum\lvert h\rvert = 2$ |
> | SP25 | $x*j^n u[n]$ | Y | Y | Y | N | $\lvert h[n]\rvert=1$ for all $n\ge0$ |
> | SP25 | $2x[\lvert n\rvert]+10$ | N | N | N | Y | $+10$; index warp; $y[-3]$ needs $x[3]$ |
> | SP25 | $e^{x[n]+1}$ | N | Y | Y | Y | $\le e^{B+1}$ |
> | FA24 | $x[n]x[n+1]$ | N | Y | N | Y | product; uses $x[n+1]$ |
> | FA24 | $x[n]/(\lvert n\rvert+1)$ | Y | N | Y | Y | $n$-gain, $\le 1$ |
> | FA24 | $\sin(x[n])+x[0]$ | N | N | N | Y | $\sin$; fixed $x[0]$ |
> | FA23 | $\log(\lvert n\rvert+1)x[n]$ | Y | N | Y | N | gain unbounded |
> | FA23 | $x*u[n+1]$ | Y | Y | N | N | $h[-1]=1$; $\sum\lvert h\rvert=\infty$ |
> | FA23 | $x[n]+3$ | N | Y | Y | Y | $T\{0\}=3\neq0$ |
> | SP23 | $x*(-1)^n u[n]$ | Y | Y | Y | N | $\lvert h\rvert = 1$ forever |
> | SP23 | $x[n]/x[2]$ | N | N | N | N | $T\{2x\}=T\{x\}$; uses $x[2]$; $x[2]\to0$ |
> | SP23 | $\cos^2(\tfrac{\pi}{2}n)x[n]$ | Y | N | Y | Y | gain $1,0,1,0,\dots$ |
> | SP21 | $x[n]\cos(\tfrac{\pi(n-2)}{3})$ | Y | N | Y | Y | same pattern |
> | SP21 | $x[3]x[n]$ | N | N | N | Y | product; fixed future sample |
> | SP21 | $(0.8+0.8j)^n x[n]$ | Y | N | Y | N | $\lvert 0.8+0.8j\rvert\approx1.13>1$ |
> | FA19 | $x[\lvert n\rvert+n]$ | Y | N | N | (Y) | $y[n]=x[2n]$ for $n>0$; S not asked |
> | FA19 | $(0.2)^{\lvert n\rvert}\log x[n]$ | N | N | Y | (N) | $\log$; $n$-gain; S not asked |
>
> FA2025 #4(a): L and TI, a convolution with an FIR $h$. Every system with reasons: [[exams/midterm-1/system-property-bank|system-property bank]].

## The recipe

| feature in $y[n]=T\{x\}[n]$ | L | TI | C | S |
|---|---|---|---|---|
| $y = x*h$ (a convolution) | Y | Y | Y iff $h[n]=0$ for $n<0$ | Y iff $\sum_n \lvert h[n]\rvert<\infty$ |
| additive constant ($x[n]+3$, $2x[\lvert n\rvert]+10$) | **N** | — | — | — |
| nonlinear function of the input ($x^2$, $\lvert x\rvert$, $e^x$, $\sin x$, $\log x$, $x[n]x[n+1]$, $x[n]/x[2]$) | **N** | — | — | — |
| gain that depends on $n$ ($g[n]\,x[n]$, $g$ not constant) | Y | **N** | Y | Y iff $g$ bounded |
| index other than $n-n_0$ ($x[-n]$, $x[2n]$, $x[\lvert n\rvert]$, $x[n^2]$) | Y | **N** | usually **N** | Y |
| fixed sample ($x[0]$, $x[2]$, $x[3]$) | usually N | **N** | **N** | — |
| uses $x[n+1]$, $x[n+k]$ with $k>0$, or a sum up to $+\infty$ | — | — | **N** | — |
| memoryless continuous function of $x$ ($e^x$, $\sin x$, $x^{10}$, $\lvert x\rvert$) | N | Y | Y | Y |
| $\log x[n]$ | N | — | — | **N** ($x\to0^+$) |
| running sum $\sum_{k\le n}x[k]$ (accumulator) | Y | Y | Y | **N** ($u[n]\mapsto(n+1)u[n]$) |

A dash: decide from the other features.

> [!recipe] Fill one row
> 1. **Convolution with known $h$?** L = Y, TI = Y; C iff $h[n]=0$ for $n<0$; S iff $\sum\lvert h\rvert<\infty$. Done.
> 2. **Linear:** $x=0$ gives $y\ne0$ → N. Every term "(no $x$) × one sample of $x$" → Y. Products, powers, $\lvert\cdot\rvert$, $e$, $\sin$, $\log$, division by a sample → N.
> 3. **Time-invariant:** every sample read as $x[n-k]$, $k$ constant, $n$ nowhere else → Y. $n$-gain, warped index, fixed sample → N. $n$ in sum limits: substitute $m=n-k$ first (Practice 3).
> 4. **Causal:** every index read $\le n$ **for every $n$, negative included**: $x[\lvert n\rvert]$ at $n=-3$ reads $x[3]$.
> 5. **Stable:** with $\lvert x\rvert\le B$, bound $\lvert y\rvert$ over all $n$, both directions; no division by samples, no $\log$, no unbounded accumulation.
> 6. **Proofs (homework):** superposition with $ax_1+bx_2$; compare $T\{x[\cdot-n_0]\}$ (shift inside $x$ only) with $y[n-n_0]$; one bounded input with unbounded output disproves S.

> [!trap] Where the points go
> - **$x[n]+3$ is not linear:** $T\{0\}\neq0$.
> - **A bounded or periodic gain is still time-varying:** $\cos^2(\tfrac{\pi}{2}n)\,x[n]$, $x[n]/(\lvert n\rvert+1)$. Shifting the input never shifts $g[n]$.
> - **A convolution is always L and TI;** judge C and S on the side where $h$ lives: $2^nu[-n]$ is summable ($\sum=2$); $u[n+1]$, $j^nu[n]$, $(-1)^nu[n]$ are not.
> - **Causality only checked for $n\ge0$:** $x[\lvert n\rvert]$, $x[n]x[0]$ fail at $n=-1$.
> - **Magnitudes:** $\lvert0.8+0.8j\rvert=0.8\sqrt2\approx1.13$; $\log(\lvert n\rvert+1)$ is still unbounded.

## Practice problems

> [!question] Practice 1 — table (12 cells)
> L / TI / C / S for (a) $y[n]=x[n]*\left(\tfrac12\right)^n u[n+2]$ (b) $y[n]=x[n]+x[-n]$ (c) $y[n]=\displaystyle\sum_{k=-\infty}^{n}x[k]$ (d) $y[n]=\cos(x[n])\,x[n-1]$.

> [!success]- Solution
> | system | L | TI | C | S | reason |
> |---|---|---|---|---|---|
> | (a) | Y | Y | N | Y | $h[-2]=4$, $h[-1]=2\neq0$; $\sum\lvert h\rvert=8$ |
> | (b) | Y | N | N | Y | index $-n$; $n=-1$ reads $x[1]$; $\lvert y\rvert\le2B$ |
> | (c) | Y | Y | Y | N | $h=u[n]$; $x=u[n]$ gives $(n+1)u[n]$ |
> | (d) | N | Y | Y | Y | $x=u[n]$: $y[1]=\cos1\approx0.540$; $x=2u[n]$: $y[1]=2\cos2\approx-0.832\neq2\cos 1$; $\lvert y\rvert\le B$ |

> [!question] Practice 2 — prove or give a counterexample
> $y[n]=x[n]+\left(\tfrac12\right)^n x[n-1]$.

> [!success]- Solution
> **L — yes:**
> $$
> y_3[n]=a x_1[n]+b x_2[n]+\left(\tfrac12\right)^n\big(a x_1[n-1]+b x_2[n-1]\big)=a\,y_1[n]+b\,y_2[n].
> $$
> **TI — no:** $\delta[n-1]\mapsto\delta[n-1]+\tfrac14\delta[n-2]$; $\delta[n-2]\mapsto\delta[n-2]+\tfrac18\delta[n-3]$, not $\delta[n-2]+\tfrac14\delta[n-3]$.
> **C — yes:** reads $x[n]$, $x[n-1]$.
> **S — no:** $x=u[-n]$ gives $y[n]=1+2^{-n}$ for $n\le0$, e.g. $y[-10]=1025$.

> [!question] Practice 3 — recognize a convolution
> $y[n]=\displaystyle\sum_{k=n-2}^{\infty}\left(\tfrac13\right)^{k-n}x[k]$. Find $h[n]$, then the four cells.

> [!success]- Solution
> $$
> h[n]=\left(\tfrac13\right)^{-n}u[2-n]=3^n u[2-n]=\{\dots,\tfrac19,\tfrac13,\underset{\uparrow}{1},3,9\}.
> $$
> Convolution: **L = Y, TI = Y**. **C = N**: $h[-1]=\tfrac13\neq0$. **S = Y**: $\sum\lvert h\rvert = 9+3+1+\tfrac12=\tfrac{27}{2}$.

## Related

[[exams/midterm-1/system-property-bank|System-property bank]] · [[exams/midterm-1/true-false-bank|T/F bank]] · [[concepts/lti-system|LTI system]] · [[concepts/bibo-stability|BIBO stability]] · [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · [[problems/finite-length-convolution|finite-length convolution]]

### Sources for this page

Lecture 3–4 notes and slides; HW1 #5–6, HW2 #1–2 with solutions; past Midterm 1 property tables FA2019–FA2025 with keys; Midterm 1 review slides.
