---
title: "Discrete-time signal"
description: "A sequence x[n] defined only at integers n: the n = 0 marker, sampling x[n] = x(nT), and the index operations (shift, flip, decimate) that exams use in sketches, convolutions and property tables."
tags: [concept, signals, midterm-1]
aliases: ["discrete-time signal", "sequence", "digital signal", "x[n]", "signal", "sample"]
---

> [!key] Definition (Lectures 1–2)
> A **discrete-time signal** is a sequence $x[n]$ defined only for integers $n\in\mathbb{Z}$ (square brackets; $x(t)$ is continuous-time). Sampling with period $T$ gives $x[n]=x(nT)$. **Digital** means discrete-time *and* discrete-valued; the course treats the values as continuous. A finite sequence is listed with the $n=0$ sample marked:
> $$
> x[n]=\{0,\ \underset{\uparrow}{4},\ -2,\ 0,\ 3,\ 1\}\quad\Longleftrightarrow\quad x[-1]=0,\ x[0]=4,\ x[1]=-2,\ \dots
> $$
> Every signal is a sum of scaled, shifted impulses, $x[n]=\sum_k x[k]\,\delta[n-k]$ ([[concepts/kronecker-delta|Kronecker delta]]); the building blocks are $\delta[n]$, the [[concepts/unit-step|unit step]] $u[n]$, sinusoids $A\sin(\omega_0n+\theta)$ and [[concepts/complex-exponential|exponentials]] $Ba^n$.

| operation | formula | effect |
|---|---|---|
| delay / advance | $x[n-n_0]$ / $x[n+n_0]$ ($n_0>0$) | shift right / left by $n_0$ |
| flip | $x[-n]$ | mirror about $n=0$ |
| flip and shift | $x[-n+n_0]=x[-(n-n_0)]$ | flip, then shift **right** by $n_0$ |
| decimate | $x[2n]$ | keep the even-indexed samples, squeezed together |
| fold | $x[\lvert n\rvert]$ | copy the right half onto the left |

> [!recipe] Sketching $y[n]=x[f(n)]$
> Do not guess the order of operations: tabulate. For each $n$ compute $f(n)$, read $x$ there, and mark the new $n=0$.
>
> [[homework/hw1|HW1]] #2: $x[n]=\{2,\ 4,\ \underset{\uparrow}{1},\ 0,\ -2,\ 5,\ 7,\ 3\}$. Then $y[n]=x[-n+3]$ has $y[0]=x[3]=5$, $y[-2]=x[5]=3$, $y[5]=x[-2]=2$:
> $$
> y[n]=\{3,\ 7,\ \underset{\uparrow}{5},\ -2,\ 0,\ 1,\ 4,\ 2\}\quad(-2\le n\le5),
> $$
> the flip of $x$ moved right by 3. And $z[n]=x[2n+1]=\{4,\ \underset{\uparrow}{0},\ 5,\ 3\}$ on $-1\le n\le2$: the samples $x[-2],x[0],x[2],x[4]$ are gone.

> [!trap]
> - **Always mark $n=0$.** $\{1,2,3\}$ without an arrow is not an answer; convolution results are graded on where the arrow sits.
> - **$x[-n+3]$ shifts right after the flip** ($x[-(n-3)]$), not left. When in doubt, tabulate.
> - **Decimation loses samples**: $x[2n]$ cannot be undone, and $x[n/2]$ is undefined for odd $n$.
> - **$n$ is an integer**: $\cos(2\pi n)=1$ and $\sin(\pi n)=0$ for every $n$ ([[0-midterm-1/past-exams/spring-2021|SP2021 #1e]]), and frequencies $\omega$ and $\omega+2\pi$ produce the same samples.
> - **Bounded is not summable**: $\lvert u[n]\rvert\le1$, yet $\sum_n u[n]=\infty$. This is exactly the bounded-but-unstable $h$ of [[concepts/bibo-stability|BIBO stability]].
> - "Signal" vs. "sample": $x[n]$ may mean the whole sequence or the single number at index $n$ (course summary).

**Where it appears.** [[1-signals-and-systems/01-digital-signals|Lecture 1]] §2, [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] §2; [[homework/hw1|HW1]] #1–#3; [[0-toolkit/03-sketching-and-transforming-signals]]. Every convolution problem depends on the $n=0$ bookkeeping ([[problems/finite-length-convolution]]), e.g. [[0-midterm-1/past-exams/fall-2025|FA2025 #3b]] where $x[n]=n\,u[n+1]\,u[-n+1]=\{-1,\ \underset{\uparrow}{0},\ 1\}$; index maps like $x[2n]$, $x[\lvert n\rvert]$ fill the property tables ([[problems/classifying-system-properties]]).

**Related.** [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/unit-step|unit step]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/convolution|convolution]] · [[concepts/time-invariance|time-invariance]]

### Sources for this page
Lecture 1 §2 (Eq. 1); Lecture 2 §2 (notation, elementary signals); HW1 #1–#3 and solutions; course summary (signal vs. sample); FA2025 #3b; SP2021 #1e. HW1 #2 and the FA2025 window checked in `verify/concepts/verify_signals.py` and `verify_glossary_time.py`.
