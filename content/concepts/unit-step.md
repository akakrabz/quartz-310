---
title: "Unit step"
description: "u[n] = 1 for n ≥ 0: shifted and flipped steps, windows u[n−a] − u[n−b], products of steps, δ[n] = u[n] − u[n−1], and the accumulator u[n] * u[n] = (n+1)u[n]."
tags: [concept, signals, midterm-1]
aliases: ["u[n]", "step", "unit step", "unit-step", "step function", "window", "rectangular window"]
---

*Lecture 2 (Wed Aug 26) §2 · [[homework/hw1|HW1]] #1, #3 · [[homework/hw2|HW2]] #3, #5c · families: [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/infinite-length-convolution|Infinite-length convolution]]*

> [!abstract] In one breath
> - $u[n]$ switches on at $n = 0$ and stays on; $u[n_0 - n]$ runs left and is on for $n \le n_0$.
> - Differences and products of steps make windows; count the samples ($u[n]-u[n-N]$ has $N$).
> - $\delta[n] = u[n]-u[n-1]$; $u[n]$ is bounded but not summable.

## 1. Definition and identities

> [!key] Unit step (Lecture 2, eq. 22)
> $$
> \begin{gathered}
> u[n]=\begin{cases}1, & n\ge0\\ 0, & n<0\end{cases}
> \qquad
> \delta[n]=u[n]-u[n-1],
> \\[4pt]
> u[n]=\sum_{k=-\infty}^{n}\delta[k]=\sum_{k=0}^{\infty}\delta[n-k].
> \end{gathered}
> $$
> Scale, shift, flip: $4u[3-n]$ is $4$ for $n \le 3$, $0$ for $n > 3$ (notes); $5u[2-n]$ (notes Fig. 2b). $z$-domain: $u[n]\leftrightarrow\dfrac{1}{1-z^{-1}}$, ROC $\lvert z\rvert>1$; and $-u[-n-1]\leftrightarrow\dfrac{1}{1-z^{-1}}$, ROC $\lvert z\rvert<1$ ([[concepts/z-transform-pairs|pairs]]).

> [!question] Lecture 2, slides 14–15: sketch $u[3-n]$.

> [!success]- Answer
> $1$ for $n \le 3$, $0$ for $n \ge 4$: a step running left, edge where the argument $3-n$ is zero.

## 2. Reading step expressions

| expression | equals 1 for | remark |
|---|---|---|
| $u[n-a]$ | $n\ge a$ | delayed step |
| $u[-n]$ | $n\le0$ | flipped; contains $n=0$ |
| $u[-n-1]$ | $n\le-1$ | the one in anti-causal pairs; excludes $n=0$ |
| $u[n_0-n]$ | $n\le n_0$ | Lecture 2: $4u[3-n]=4$ for $n\le3$ |
| $u[n-a]-u[n-b]$, $a<b$ | $a\le n\le b-1$ | window of $b-a$ samples |
| $u[n-a]\,u[b-n]$, $a\le b$ | $a\le n\le b$ | window of $b-a+1$ samples |

> [!recipe] Reading step expressions
> Find where each factor is 1, intersect (products) or subtract (differences), then list the samples.
> - [[homework/hw1|HW1]] #1b: $(\frac23)^n\big(u[n+2]-u[n-3]\big)$ lives on $-2\le n\le2$: $\{\frac94,\ \frac32,\ \underset{\uparrow}{1},\ \frac23,\ \frac49\}$.
> - [[homework/hw1|HW1]] #1c: $n\,u[n]\,u[n-4]=n\,u[n-4]$ (the later step wins).
> - [[exams/midterm-1/past-exams/fall-2024|FA2024 #5b]]: $u[n-1]\,u[3-n]=\delta[n-1]+\delta[n-2]+\delta[n-3]$, so $X(z)=z^{-1}+z^{-2}+z^{-3}$, ROC $z\neq0$.
> - [[exams/midterm-1/past-exams/fall-2025|FA2025 #5b]]: $u[n]-u[n-8]$ has 8 samples, $X(z)=\sum_{k=0}^{7}z^{-k}$, ROC $z\neq0$.

## 3. Steps inside convolution sums

$u[k]$ keeps $k \ge 0$, $u[n-k]$ keeps $k \le n$; no surviving $k$ ⇒ $y[n] = 0$ ([[concepts/convolution|convolution]] §4). $h * u[n]$ is the [[concepts/step-response|step response]]; $u[n]*u[n]=(n+1)u[n]$.

> [!trap]
> - **$u[n]-u[n-N]$ has $N$ samples** ($n=0,\dots,N-1$), not $N+1$.
> - **$u[-n]$ vs. $u[-n-1]$**: only the first contains $n=0$. The anti-causal pair $-a^nu[-n-1]$ needs the second.
> - **$n\,u[n+1]\neq n\,u[n]$**: the $n=-1$ sample is $-1$, so $n\,u[n+1]=n\,u[n]-\delta[n+1]$ (FA2023 #5; FA2025 #3b's $n\,u[n+1]u[-n+1]=\{-1,\ \underset{\uparrow}{0},\ 1\}$).
> - **$h=u[n]$ is the classic bounded-but-unstable system** (the accumulator $y[n]=\sum_{k\le n}x[k]$): $\sum\lvert u[n]\rvert=\infty$, and $u[n]*u[n]=(n+1)u[n]$ grows ([[concepts/bibo-stability|BIBO stability]], [[concepts/marginal-stability|marginal stability]]).
> - **$h[n-4]$ shifts every $n$, including the step**: $u[n-4]$, not $u[n]$.

> [!exam] Steps set the limits of every sum
> Windows and shifted steps appear in z-transform and convolution problems; no standalone step problem.
> [[exams/midterm-1/past-exams/fall-2023|FA2023 #4, #5]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #5a, #5b]] · [[exams/midterm-1/past-exams/fall-2025|FA2025 #3b, #5b]]

**Where it appears:** [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] §2, [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §2.2.3, [[2-z-transform/06-the-z-transform|Lecture 6]] (Exercise 1: $\mathcal{Z}\{u[n]\}$), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1; [[homework/hw1|HW1]] #1, #3; [[homework/hw2|HW2]] #3, #5c; families [[problems/z-transform-with-roc|z-transform with ROC]] and [[problems/infinite-length-convolution|infinite-length convolution]].

## Related
[[concepts/kronecker-delta|Kronecker delta]] · [[concepts/step-response|step response]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/z-transform-pairs|z-transform pairs]]

### Sources for this page
Lecture 2 §2 (eq. 22, the $4u[3-n]$ example, Fig. 2b) and slides 14–15; Lecture 6 Exercise 1; Lecture 11 §1.2.1; HW1 #1, #3 and HW2 #3 solutions; FA2023 #4–#5, FA2024 #5, FA2025 #3b and #5b.
