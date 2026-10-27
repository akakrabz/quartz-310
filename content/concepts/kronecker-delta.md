---
title: "Kronecker delta (unit impulse)"
description: "δ[n] = 1 at n = 0 and 0 elsewhere: sifting, the decomposition x[n] = Σ x[k] δ[n−k] behind convolution, δ[n] = u[n] − u[n−1], and the 'δ of a function' T/F traps."
tags: [concept, signals, convolution, midterm-1]
aliases: ["unit impulse", "unit pulse", "Kronecker delta", "impulse", "delta", "sifting", "sifting property"]
---

*Lectures 2 (Wed Aug 26) §2 and 4 (Mon Aug 31) §1.1 · [[homework/hw1|HW1]] #1, #3 · [[homework/hw2|HW2]] #3–#4 · families: [[problems/finding-h-from-input-output-pairs|Finding h from input–output pairs]], [[problems/infinite-length-convolution|Infinite-length convolution]]*

> [!abstract] In one breath
> - $\delta[n]$ is one sample of height 1 at $n = 0$; **not** the Dirac delta.
> - Every signal is $\sum_k x[k]\,\delta[n-k]$: sample $k$ is an impulse at $k$ of height $x[k]$. This is why LTI systems are convolutions.
> - Product, sum and convolution with $\delta[n-k]$ are three different operations.

## 1. Definition

> [!key] Kronecker delta (Lecture 2, eq. 21)
> $$
> \delta[n]=\begin{cases}1, & n=0\\ 0, & n\neq0\end{cases}
> $$
> Unit impulse, unit pulse. Scale and shift: $3\delta[n-10]$ is $3$ at $n = 10$ only; $-2\delta[n+3]$ is $-2$ at $n = -3$. Any signal is a sum of scaled, shifted deltas.

$z$-domain: $\delta[n-k]\leftrightarrow z^{-k}$, ROC all $z$ except $0$ (if $k>0$) or $\infty$ (if $k<0$) ([[concepts/z-transform-pairs|pairs]]).

## 2. Signals as sums of shifted impulses

Each sample is an impulse at $k$ with height $x[k]$. Lecture 4, slide 4:
$$
\begin{aligned}
x[n] &= \cos\!\left(\tfrac{\pi}{4}n\right)\big(u[n] - u[n-8]\big) = \Big\{\underset{\uparrow}{1},\ \tfrac{\sqrt2}{2},\ 0,\ -\tfrac{\sqrt2}{2},\ -1,\ -\tfrac{\sqrt2}{2},\ 0,\ \tfrac{\sqrt2}{2}\Big\} \\
&= \delta[n] + \tfrac{\sqrt2}{2}\delta[n-1] - \tfrac{\sqrt2}{2}\delta[n-3] - \delta[n-4] - \tfrac{\sqrt2}{2}\delta[n-5] + \tfrac{\sqrt2}{2}\delta[n-7].
\end{aligned}
$$
Notes (eq. 5), sine version: $\sin(\tfrac{\pi}{4}n)\big(u[n]-u[n-8]\big) = \tfrac{\sqrt2}{2}\delta[n-1] + \delta[n-2] + \tfrac{\sqrt2}{2}\delta[n-3] - \tfrac{\sqrt2}{2}\delta[n-5] - \delta[n-6] - \tfrac{\sqrt2}{2}\delta[n-7]$.

> [!key] Sifting and decomposition (Lecture 4, eq. 6)
> $$
> x[n] = \sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k].
> $$
> At fixed $n$ only $k = n$ survives: $x[3] = \cdots + x[3]\delta[0] + \cdots = x[3]$ (the notes' "$= \delta[3]$" is a [[0-toolkit/05-errata|typo]]). Product form $x[n]\,\delta[n-k]=x[k]\,\delta[n-k]$; sum form $\sum_n x[n]\,\delta[n-k]=x[k]$. The decomposition is the reason every [[concepts/lti-system|LTI system]] is a [[concepts/convolution|convolution]].

> [!question] Lecture 2, slides 14–15: sketch $x[n] = -2\delta[n+3]$; write $x[n] = \{2, 0, \underset{\uparrow}{3}, -1, -4\}$ in terms of $\delta[n]$.

> [!success]- Answer
> $-2\delta[n+3]$: $-2$ at $n = -3$, zero elsewhere. $x[n] = 2\delta[n+2] + 3\delta[n] - \delta[n-1] - 4\delta[n-2]$.

**Decomposition at work ([[exams/midterm-1/past-exams/fall-2025|FA2025 #3b]]).** $x[n]=n\,u[n+1]\,u[-n+1]=\{-1,\ \underset{\uparrow}{0},\ 1\}=-\delta[n+1]+\delta[n-1]$, so for any $h$, $x*h=-h[n+1]+h[n-1]$: no sum to evaluate. The same idea computes finite-with-infinite convolutions ([[concepts/convolution|convolution]] §5).

## 3. The identities

> [!key] Four identities (Lectures 2 and 4)
> - **Sifting:** $x[n]\,\delta[n-k]=x[k]\,\delta[n-k]$ and $\sum_n x[n]\,\delta[n-k]=x[k]$.
> - **Decomposition:** $x[n]=\sum_{k=-\infty}^{\infty}x[k]\,\delta[n-k]$.
> - **Convolution (Lecture 4, eq. 12):** $x[n]*\delta[n] = x[n]$, $x[n]*\delta[n-k]=x[n-k]$; the [[concepts/impulse-response|impulse response]] is $h[n]=T\{\delta[n]\}$.
> - **Step link:** $\delta[n]=u[n]-u[n-1]$ and $u[n]=\sum_{k=-\infty}^{n}\delta[k]$ ([[concepts/unit-step|unit step]]).

## 4. A delta of a function

> [!recipe] $\sum_n x[n]\,\delta[f(n)]$
> $\delta[f(n)]=1$ exactly at the **integers** where $f(n)=0$. Solve $f(n)=0$ over $\mathbb{Z}$ and add up $x$ there.
> - [[exams/midterm-1/past-exams/fall-2019|FA2019 #1g]]: $\sum_n x[n]\,\delta[2^nu[n]-8]=4$. For $n\ge0$, $2^n=8$ only at $n=3$; for $n<0$ the argument is $-8$. So the sum is $x[3]=4$ and "then $x[3]=2$" is **False**.
> - [[exams/midterm-1/past-exams/spring-2021|SP2021 #1e]]: $\sum_n x[n]\,\delta[4\cos(2\pi n+\frac{\pi}{2})-6\sin(\pi n)]=4$. The argument is $0$ at **every** integer, so the sum is $\sum_n x[n]=4$ and "then $\sum_n x[n]=3$" is **False**.

> [!trap]
> - **Not the Dirac delta**: $\delta[0]=1$ (finite), there is no integral or area, and $\delta[2n]=\delta[n]$ (no $1/\lvert a\rvert$ factor).
> - **Three different operations**: product $x[n]\,\delta[n-k]=x[k]\,\delta[n-k]$ (a sequence), sum $\sum_n x[n]\,\delta[n-k]=x[k]$ (a number), convolution $x*\delta[n-k]=x[n-k]$ (the whole signal shifted).
> - **Solve $f(n)=0$ over the integers only**: no solution gives $0$, every $n$ a solution gives $\sum_n x[n]$.
> - $\delta[n]$ is technically **both causal and left-sided**, the caveat behind [[exams/midterm-1/past-exams/fall-2025|FA2025 #1d]] ([[0-toolkit/05-errata|errata]]). Older exams say *unit pulse*.

> [!exam] Sifting T/F items and impulse decompositions
> No standalone problem; sifting appears in T/F, the decomposition in every "finite with infinite" convolution and in finding $h$ from input–output pairs.
> [[exams/midterm-1/past-exams/fall-2019|FA2019 #1g]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1e]] · [[exams/midterm-1/past-exams/fall-2025|FA2025 #1d, #3b]] · [[homework/hw1|HW1]] #1, #3 · [[homework/hw2|HW2]] #3–#4

**Where it appears:** [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] §2 (eq. 21), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §1.1 (eqs. 5–6) and §2.1 (eq. 12); [[homework/hw1|HW1]] #1, #3; [[homework/hw2|HW2]] #3 ($\delta=u[n]-u[n-1]$) and #4 (build $\delta$ out of shifted inputs); [[problems/finding-h-from-input-output-pairs|finding h]], [[problems/infinite-length-convolution|infinite-length convolution]].

## Related
[[concepts/unit-step|unit step]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[concepts/impulse-response|impulse response]] · [[concepts/convolution|convolution]] · [[concepts/z-transform-pairs|z-transform pairs]]

### Sources for this page
Lecture 2 §2 (eq. 21) and slides 14–15; Lecture 4 §1.1 (eqs. 5–6, slide 4) and §2.1 (eq. 12); HW1 #1, #3; HW2 #3–#4; FA2019 #1g, SP2021 #1e, FA2025 #1d, #3b.
