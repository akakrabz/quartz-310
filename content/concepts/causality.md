---
title: "Causality"
description: "A causal system never uses a future input: y[n0] depends only on x[n] for n ≤ n0. For LTI systems this is h[n] = 0 for n < 0, i.e. an ROC outside the largest pole. Tests, fast rules and the T/F traps."
tags: [concept, systems, roc, midterm-1]
aliases: ["causal", "causal system", "non-causal", "noncausal", "anti-causal", "causal signal"]
---

> [!key] Definitions
> - **Any system (Lecture 3):** causal iff the output at time $n_0$ depends only on inputs (and outputs) at times $n\le n_0$: present and past, never future.
> - **LTI system (Lecture 4):** causal $\iff$ $h[n]=0$ for $n<0$.
> - **Rational $H(z)$ (Lecture 11):** causal $\iff$ the ROC is the exterior of a circle, including $\infty$: $\lvert z\rvert>\lvert p_{\max}\rvert$.
> - **Vocabulary:** a *causal signal* is zero for $n<0$; an **anti-causal** system uses only future inputs ($h[n]=0$ for $n\ge0$); **non-causal** means some future input is used.

> [!recipe] Testing a formula
> For every term $x[g(n)]$ you need $g(n)\le n$ **for all** $n$ (Lecture 3, Ex. 6: $x[n]+x[n-2]-x[n-4]$ is causal). To disprove, find **one** $n$ that reaches ahead: $x[\lvert n\rvert]$ at $n=-3$ needs $x[3]$; $x[2n]$ at $n=1$ needs $x[2]$; $x[0]$ at $n=-1$ is a future sample. For an LTI system just look at $h$ (or the ROC).

**Worked example ([[exams/midterm-1/past-exams/fall-2019|FA2019 #3]]).** The LTI system maps $2\delta[n-2]$ to $\delta[n-1]+2\delta[n-2]+\delta[n-3]$, so $h[n]=\tfrac12\delta[n+1]+\delta[n]+\tfrac12\delta[n-1]$. Since $h[-1]=\tfrac12\neq0$ the system is **not causal**: $y[n]=\tfrac12x[n+1]+x[n]+\tfrac12x[n-1]$ uses the next input.

| form of the system | causal? | examples from exams and homework |
|---|---|---|
| memoryless: only $x[n]$ at the same $n$ (any gain in $n$) | yes | $\lvert n\rvert x[n]$, $e^{x[n]+1}$, $\log(\lvert n\rvert+1)\,x[n]$, $(0.2)^{\lvert n\rvert}\log x[n]$ |
| past inputs and outputs only | yes | $\lvert x[n]-x[n-1]\rvert$, $y[n]=y[n-5]+x[n]+10x[n-1]$ |
| convolution with $h[n]=0$ for $n<0$ | yes | $x*j^nu[n]$, $x*(-1)^nu[n]$ |
| a future sample $x[n+k]$, $k>0$ | no | $x[n]x[n+1]$ |
| index map that reaches ahead | no | $x[\lvert n\rvert]$, $x[2n]$, $x[\lvert n\rvert+n]$, $2x[\lvert n\rvert]+10$ |
| a sample at a fixed time | no | $x[n]x[0]$, $x[3]x[n]$, $x[n]/x[2]$, $\sin(x[n])+x[0]$ |
| convolution with $h[n]\neq0$ for some $n<0$ | no | $x*2^nu[-n]$, $x*u[n+1]$ |

> [!trap] T/F statements on causality
> - "$y[n]=\sum_\ell h[\ell]\,x[n-\ell]$ must be causal" is False ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1a]]): with $h=\delta[n+1]$ the output is $x[n+1]$.
> - **Right-sided is not causal** ([[exams/midterm-1/past-exams/spring-2023|SP2023 #1c]] F): $(\frac12)^nu[n+3]$ is right-sided with $h[-3]=8$.
> - **Left-sided (reaching to $-\infty$) can never be causal** ([[exams/midterm-1/past-exams/fall-2025|FA2025 #1d]] T; strictly, $\delta[n]$ is both, see [[0-toolkit/05-errata|errata]]).
> - **Causal $*$ causal is causal** ([[exams/midterm-1/past-exams/fall-2025|FA2025 #1b]] T): the start index is $0+0$.
> - **Causality is not time-invariance**: [[exams/midterm-1/past-exams/fall-2023|FA2023 #1a]] and [[exams/midterm-1/past-exams/fall-2019|FA2019 #1f]] are False ($y=n\,x[n]$ is causal and time-varying).
> - **The difference equation alone does not fix causality** ([[exams/midterm-1/past-exams/fall-2019|FA2019 #1a]] T): $y[n]-\frac12y[n-1]=x[n]$ is solved by $(\frac12)^nu[n]$ (ROC $\lvert z\rvert>\frac12$) and by $-(\frac12)^nu[-n-1]$ (ROC $\lvert z\rvert<\frac12$).
> - **Stable plus a pole outside the unit circle forces a non-causal system** ([[exams/midterm-1/past-exams/fall-2023|FA2023 #1f]] T, [[exams/midterm-1/past-exams/spring-2025|SP2025 #1e]] T): the ROC must contain $\lvert z\rvert=1$, so it lies inside that pole.
> - Causality is a property of the **system**, not of the input starting at $n=0$.

**Where it appears.** [[1-signals-and-systems/03-system-properties|Lecture 3]] §2.3, [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §2.1, [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] (an LCCDE with only non-negative shifts is causal), [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.1 (ROC shapes, Table 1). The Causal column of every property table (7/7); [[exams/midterm-1/past-exams/spring-2025|SP2025 #3b]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #3]], and the non-causal recursions of [[exams/midterm-1/past-exams/fall-2025|FA2025 #7b]] and [[exams/midterm-1/past-exams/fall-2024|FA2024 #8a]]. Drill: [[problems/classifying-system-properties]], [[problems/two-sided-systems-as-recursions]], [[exams/midterm-1/true-false-bank]].

**Related.** [[concepts/sided-sequences|sided sequences]] · [[concepts/region-of-convergence|ROC]] · [[concepts/impulse-response|impulse response]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/lccde|LCCDE]] · [[concepts/time-invariance|time-invariance]] · [[concepts/linearity|linearity]]

### Sources for this page
Lecture 3 §2.3 (Ex. 6) and slides 10–11; Lecture 4 §2.1; Lecture 11 §1.1 and Table 1; past-exam property tables and T/F items (answers in `verify/exams/property_bank.py`, `tf_bank.py`); FA2019 #3 checked in `verify/concepts/verify_systems.py`.
