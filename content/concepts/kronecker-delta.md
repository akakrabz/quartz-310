---
title: "Kronecker delta (unit impulse)"
description: "δ[n] = 1 at n = 0 and 0 elsewhere: sifting, the decomposition x[n] = Σ x[k] δ[n−k] behind convolution, δ[n] = u[n] − u[n−1], and the 'δ of a function' T/F traps."
tags: [concept, signals, convolution, midterm-1]
aliases: ["unit impulse", "unit pulse", "Kronecker delta", "impulse", "delta"]
---

> [!key] Definition and the four identities (Lectures 2 and 4)
> $$
> \delta[n]=\begin{cases}1, & n=0\\ 0, & n\neq0\end{cases}
> $$
> - **Sifting:** $x[n]\,\delta[n-k]=x[k]\,\delta[n-k]$ and $\sum_n x[n]\,\delta[n-k]=x[k]$.
> - **Decomposition:** $x[n]=\sum_{k=-\infty}^{\infty}x[k]\,\delta[n-k]$, the reason every [[concepts/lti-system|LTI system]] is a [[concepts/convolution|convolution]].
> - **Convolution:** $x[n]*\delta[n-k]=x[n-k]$; the [[concepts/impulse-response|impulse response]] is $h[n]=T\{\delta[n]\}$.
> - **Step link:** $\delta[n]=u[n]-u[n-1]$ and $u[n]=\sum_{k=-\infty}^{n}\delta[k]$ ([[concepts/unit-step|unit step]]).
>
> $z$-domain: $\delta[n-k]\leftrightarrow z^{-k}$, ROC all $z$ except $0$ (if $k>0$) or $\infty$ (if $k<0$).

**Decomposition at work ([[0-midterm-1/past-exams/fall-2025|FA2025 #3b]]).** $x[n]=n\,u[n+1]\,u[-n+1]=\{-1,\ \underset{\uparrow}{0},\ 1\}=-\delta[n+1]+\delta[n-1]$, so for any $h$, $x*h=-h[n+1]+h[n-1]$: no sum to evaluate.

> [!recipe] A delta of a function: $\sum_n x[n]\,\delta[f(n)]$
> $\delta[f(n)]=1$ exactly at the **integers** where $f(n)=0$. Solve $f(n)=0$ over $\mathbb{Z}$ and add up $x$ there.
> - [[0-midterm-1/past-exams/fall-2019|FA2019 #1g]]: $\sum_n x[n]\,\delta[2^nu[n]-8]=4$. For $n\ge0$, $2^n=8$ only at $n=3$; for $n<0$ the argument is $-8$. So the sum is $x[3]=4$ and "then $x[3]=2$" is **False**.
> - [[0-midterm-1/past-exams/spring-2021|SP2021 #1e]]: $\sum_n x[n]\,\delta[4\cos(2\pi n+\frac{\pi}{2})-6\sin(\pi n)]=4$. The argument is $0$ at **every** integer, so the sum is $\sum_n x[n]=4$ and "then $\sum_n x[n]=3$" is **False**.

> [!trap]
> - **Not the Dirac delta**: $\delta[0]=1$ (finite), there is no integral or area, and $\delta[2n]=\delta[n]$ (no $1/\lvert a\rvert$ factor).
> - **Three different operations**: product $x[n]\,\delta[n-k]=x[k]\,\delta[n-k]$ (a sequence), sum $\sum_n x[n]\,\delta[n-k]=x[k]$ (a number), convolution $x*\delta[n-k]=x[n-k]$ (the whole signal shifted).
> - **Solve $f(n)=0$ over the integers only**: no solution gives $0$, every $n$ a solution gives $\sum_n x[n]$.
> - $\delta[n]$ is technically **both causal and left-sided**, the caveat behind [[0-midterm-1/past-exams/fall-2025|FA2025 #1d]] ([[0-toolkit/05-errata|errata]]). Older exams say *unit pulse*.

**Where it appears.** [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] §2, [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §1.1 (Eq. 6; the notes' "$=\delta[3]$" should read $x[3]$); [[homework/hw1|HW1]] #1, #3; [[homework/hw2|HW2]] #3 ($\delta=u[n]-u[n-1]$) and #4 (build $\delta$ out of shifted inputs); T/F [[0-midterm-1/past-exams/fall-2019|FA2019 #1g]], [[0-midterm-1/past-exams/spring-2021|SP2021 #1e]]; [[problems/finding-h-from-input-output-pairs]], [[problems/infinite-length-convolution]].

**Related.** [[concepts/unit-step|unit step]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[concepts/impulse-response|impulse response]] · [[concepts/convolution|convolution]] · [[concepts/z-transform-pairs|z-transform pairs]]

### Sources for this page
Lecture 2 §2 (Eq. 21); Lecture 4 §1.1 (Eq. 6) and §2.1 (identity); HW1 #1, #3; HW2 #3–#4; FA2019 #1g, SP2021 #1e (page render checked), FA2025 #3b. Checked in `verify/concepts/verify_signals.py` and `verify_glossary_time.py`.
