---
title: "Unit step"
description: "u[n] = 1 for n ≥ 0: shifted and flipped steps, windows u[n−a] − u[n−b], products of steps, δ[n] = u[n] − u[n−1], and the accumulator u[n] * u[n] = (n+1)u[n]."
tags: [concept, signals, midterm-1]
aliases: ["u[n]", "step", "unit step", "unit-step", "step function"]
---

> [!key] Definition and identities (Lecture 2)
> $$
> \begin{gathered}
> u[n]=\begin{cases}1, & n\ge0\\ 0, & n<0\end{cases}
> \qquad
> \delta[n]=u[n]-u[n-1],
> \\[4pt]
> u[n]=\sum_{k=-\infty}^{n}\delta[k]=\sum_{k=0}^{\infty}\delta[n-k].
> \end{gathered}
> $$
> $z$-domain: $u[n]\leftrightarrow\dfrac{1}{1-z^{-1}}$, ROC $\lvert z\rvert>1$; and $-u[-n-1]\leftrightarrow\dfrac{1}{1-z^{-1}}$, ROC $\lvert z\rvert<1$ ([[concepts/z-transform-pairs|pairs]]).

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

> [!trap]
> - **$u[n]-u[n-N]$ has $N$ samples** ($n=0,\dots,N-1$), not $N+1$.
> - **$u[-n]$ vs. $u[-n-1]$**: only the first contains $n=0$. The anti-causal pair $-a^nu[-n-1]$ needs the second.
> - **$n\,u[n+1]\neq n\,u[n]$**: the $n=-1$ sample is $-1$, so $n\,u[n+1]=n\,u[n]-\delta[n+1]$ (FA2023 #5; FA2025 #3b's $n\,u[n+1]u[-n+1]=\{-1,\ \underset{\uparrow}{0},\ 1\}$).
> - **$h=u[n]$ is the classic bounded-but-unstable system** (the accumulator $y[n]=\sum_{k\le n}x[k]$): $\sum\lvert u[n]\rvert=\infty$, and $u[n]*u[n]=(n+1)u[n]$ grows ([[concepts/bibo-stability|BIBO stability]], [[concepts/marginal-stability|marginal stability]]).

**Where it appears.** [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] §2, [[2-z-transform/06-the-z-transform|Lecture 6]] (Exercise 1: $\mathcal{Z}\{u[n]\}$), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.2.1; [[homework/hw1|HW1]] #1, #3; [[homework/hw2|HW2]] #3, #5c. Exams: [[exams/midterm-1/past-exams/fall-2023|FA2023 #4, #5]], [[exams/midterm-1/past-exams/fall-2024|FA2024 #5a, #5b]], [[exams/midterm-1/past-exams/fall-2025|FA2025 #3b, #5b]]; families [[problems/z-transform-with-roc]] and [[problems/infinite-length-convolution]].

**Related.** [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/step-response|step response]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/z-transform-pairs|z-transform pairs]]

### Sources for this page
Lecture 2 §2 (Eq. 22 and the $4u[3-n]$ example); Lecture 6 Exercise 1; Lecture 11 §1.2.1; HW1 #1, #3 and HW2 #3 solutions; FA2023 #4–#5, FA2024 #5, FA2025 #3b and #5b. Checked in `verify/concepts/verify_signals.py` and `verify_glossary_time.py`.
