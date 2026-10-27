---
title: "Causality"
description: "A causal system never uses a future input: y[n0] depends only on x[n], n ≤ n0. LTI: h[n] = 0 for n < 0; H(z): ROC outside the largest pole, reaching infinity. Tests, T/F traps."
tags: [concept, systems, roc, midterm-1]
aliases: ["causal", "causal system", "non-causal", "noncausal", "anti-causal", "causal signal", "right-sided system", "left-sided system"]
---

*Lectures 3 (Fri Aug 28) §2.3, 4 (Mon Aug 31) §2.1 and 11 (Fri Sep 18) §1.1 · [[homework/hw2|HW2]] #1–#2 · families: [[problems/classifying-system-properties|Classifying system properties]], [[problems/two-sided-systems-as-recursions|Two-sided systems as recursions]]*

> [!abstract] In one breath
> - Causal ⇔ $y[n]$ uses only present and past inputs (and outputs); one future sample at one $n$ breaks it. Check negative $n$.
> - LTI: causal ⇔ $h[n] = 0$ for $n < 0$ ⇔ ROC is $\lvert z\rvert > \lvert p_{\max}\rvert$ (includes $\infty$).
> - Causality is independent of linearity, time-invariance and stability.

## 1. Definitions

> [!key] Causality
> - **Any system (Lecture 3 §2.3):** causal iff the output at time $n_0$ depends only on inputs (and outputs) at times $n\le n_0$: present and past, never future. $y[n]$ never uses $x[m]$ with $m > n$.
> - **LTI system (Lecture 4, eq. 13):** causal $\iff$ $h[n]=0$ for $n<0$: the flipped, shifted $h$ never reaches into the future.
> - **Rational $H(z)$ (Lecture 11, eq. 13):** causal $\iff$ the ROC is the exterior of a circle, including $\infty$: $\lvert z\rvert>\lvert p_{\max}\rvert$.
> - **Vocabulary (Lecture 11):** a *causal signal* is zero for $n<0$; an **anti-causal** system uses only future inputs ($h[n]=0$ for $n\ge0$); **non-causal** means some future input is used.

## 2. Testing a formula

> [!recipe] Causality check (Lecture 3)
> For each term $x[g(n)]$: is $g(n) \le n$ for **every** integer $n$, negative ones included? Any $n$ with $g(n) > n$ is a counterexample. Coefficients ($n$, $\cos(\pi n/3)$) do not select samples. For an LTI system just look at $h$ (or the ROC).

> [!question] Notes Exercise 6 and slide 10: causal?
> (E6) $y[n] = x[n] + x[n-2] - x[n-4]$ (S1) $y[n] = \tfrac13\big(x[n] + x[n-1] + x[n-2]\big)$ (S2) $y[n] = x[\lvert n\rvert]$

> [!success]- Answers
> **E6, S1 causal**: indices $n$, $n-2$, $n-4$ (and $n$, $n-1$, $n-2$) are all $\le n$.
> **S2 non-causal**: $y[-2] = x[2]$ (the notes take $n = -3$: $y[-3] = x[3]$), a future input; harmless for $n \ge 0$, but one $n$ is enough.

> [!question] Extra practice (slide 11): causal?
> (1) $y[n] = x[\lvert n\rvert - n]$ (2) $y[n] = (n+1)\,(x[n] - x[n-1])$ (3) $y[n] = e^{x[n]}$ (4) $y[n] = x[n]\,x[0]$

> [!success]- Answers
> 1. Non-causal: $y[-1] = x[\lvert -1\rvert - (-1)] = x[2]$.
> 2. Causal: $x[n]$ and $x[n-1]$; the factor $(n+1)$ is irrelevant.
> 3. Causal.
> 4. Non-causal: $y[-1] = x[-1]\,x[0]$ needs the future $x[0]$.

## 3. Causality from h[n] and from the ROC

**Right- and left-sided sequences (Lecture 11, eqs. 9–12).** Right-sided: $h[n] = 0$ for $n < n_0$, ROC $\lvert z\rvert > a$; left-sided: $h[n] = 0$ for $n > n_0$, ROC $\lvert z\rvert < a$. A right-sided $h$ with $n_0 < 0$ excludes $\infty$ ($a < \lvert z\rvert < \infty$); a left-sided $h$ with $n_0 > 0$ excludes $0$. Hence (Lecture 11, Table 1, eqs. 13–14):

| ROC shape of $H(z)$ | causality type | sided | stable iff |
|---|---|---|---|
| $\lvert z\rvert > \lvert p_{\max}\rvert$ | causal | right | $\lvert p_{\max}\rvert < 1$ |
| $\lvert z\rvert < \lvert p_{\min}\rvert$ | anti-causal | left | $\lvert p_{\min}\rvert > 1$ |
| $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$ | non-causal, right-sided | right | $\lvert p_{\max}\rvert < 1$ |

Two-sided $h = h_l + h_r$: ROC at least $\lvert p_{\max}\rvert < \lvert z\rvert < \lvert p_{\min}\rvert$, non-causal. Details and stability: [[concepts/region-of-convergence|ROC]], [[concepts/sided-sequences|sided sequences]], [[concepts/bibo-stability|BIBO stability]].

**Worked example ([[exams/midterm-1/past-exams/fall-2019|FA2019 #3]]).** The LTI system maps $2\delta[n-2]$ to $\delta[n-1]+2\delta[n-2]+\delta[n-3]$, so $h[n]=\tfrac12\delta[n+1]+\delta[n]+\tfrac12\delta[n-1]$. Since $h[-1]=\tfrac12\neq0$ the system is **not causal**: $y[n]=\tfrac12x[n+1]+x[n]+\tfrac12x[n-1]$ uses the next input (FIR, pole at $\infty$, ROC $0 < \lvert z\rvert < \infty$).

## 4. Reading causality off a formula

| form of the system | causal? | examples from exams and homework |
|---|---|---|
| memoryless: only $x[n]$ at the same $n$ (any gain in $n$) | yes | $\lvert n\rvert x[n]$, $e^{x[n]+1}$, $\log(\lvert n\rvert+1)\,x[n]$, $(0.2)^{\lvert n\rvert}\log x[n]$ |
| past inputs and outputs only | yes | $\lvert x[n]-x[n-1]\rvert$, $y[n]=y[n-5]+x[n]+10x[n-1]$ |
| convolution with $h[n]=0$ for $n<0$ | yes | $x*j^nu[n]$, $x*(-1)^nu[n]$ |
| a future sample $x[n+k]$, $k>0$ | no | $x[n]x[n+1]$ |
| index map that reaches ahead | no | $x[\lvert n\rvert]$, $x[2n]$ ($y[1] = x[2]$), $x[\lvert n\rvert+n]$, $2x[\lvert n\rvert]+10$ |
| a sample at a fixed time | no | $x[n]x[0]$, $x[3]x[n]$, $x[n]/x[2]$, $\sin(x[n])+x[0]$ |
| convolution with $h[n]\neq0$ for some $n<0$ | no | $x*2^nu[-n]$, $x*u[n+1]$ |

All four properties in one table: [[concepts/lti-system|LTI system]] §3. An LCCDE with only non-negative shifts runs causally ([[concepts/lccde|LCCDE]]), but the equation alone does not fix causality.

> [!trap]
> - "$y[n]=\sum_\ell h[\ell]\,x[n-\ell]$ must be causal" is False ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1a]]): with $h=\delta[n+1]$ the output is $x[n+1]$.
> - **Right-sided is not causal** ([[exams/midterm-1/past-exams/spring-2023|SP2023 #1c]] F): $(\frac12)^nu[n+3]$ has $h[-3]=8$. **Left-sided (reaching to $-\infty$) can never be causal** ([[exams/midterm-1/past-exams/fall-2025|FA2025 #1d]] T; strictly, $\delta[n]$ is both, see [[0-toolkit/05-errata|errata]]).
> - **Causal $*$ causal is causal** ([[exams/midterm-1/past-exams/fall-2025|FA2025 #1b]] T): the start index is $0+0$.
> - **Causality is not time-invariance**: [[exams/midterm-1/past-exams/fall-2023|FA2023 #1a]] and [[exams/midterm-1/past-exams/fall-2019|FA2019 #1f]] are False ($y=n\,x[n]$ is causal and time-varying). It is a property of the **system**, not of an input starting at $n=0$.
> - **The difference equation alone does not fix causality** ([[exams/midterm-1/past-exams/fall-2019|FA2019 #1a]] T): $y[n]-\frac12y[n-1]=x[n]$ is solved by $(\frac12)^nu[n]$ (ROC $\lvert z\rvert>\frac12$) and by $-(\frac12)^nu[-n-1]$ (ROC $\lvert z\rvert<\frac12$).
> - **Stable plus a pole outside the unit circle forces a non-causal system** ([[exams/midterm-1/past-exams/fall-2023|FA2023 #1f]] T, [[exams/midterm-1/past-exams/spring-2025|SP2025 #1e]] T): the ROC must contain $\lvert z\rvert=1$, so it lies inside that pole.

> [!exam] The Causal column of the property table (7 of 7) and the ROC T/F items
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #1b, #1d, #1e, #2, #7b]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1a, #1b, #1e, #2, #3b]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #2, #8a]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1a, #1f, #2]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1b, #1c, #2]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #3]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1a, #1f, #2, #3]] · [[exams/midterm-1/system-property-bank|bank]] · [[exams/midterm-1/true-false-bank|T/F bank]]

**Where it appears:** [[1-signals-and-systems/03-system-properties|Lecture 3]] §2.3 (Exercise 6, slides 10–11), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §2.1 (eq. 13), [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] §1, [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] §1.1 (eqs. 8–14, Table 1); [[homework/hw2|HW2]] #1–#2; [[problems/classifying-system-properties|classifying system properties]], [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]], [[demos/practice-drills|practice drills]].

## Related
[[concepts/sided-sequences|sided sequences]] · [[concepts/region-of-convergence|ROC]] §4 (ROC/causality/stability table) · [[concepts/bibo-stability|BIBO stability]] §3 (slides 6–7 corner table) · [[concepts/impulse-response|impulse response]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/lccde|LCCDE]] · [[concepts/time-invariance|time-invariance]] · [[concepts/linearity|linearity]] · [[concepts/lti-system|LTI system]]

### Sources for this page
Lecture 3 §2.3 (Exercise 6) and slides 10–11 with the annotated deck; Lecture 4 §2.1 (eq. 13); Lecture 11 §1.1 (eqs. 8–14) and Table 1; past-exam property tables and T/F items; FA2019 #3.
