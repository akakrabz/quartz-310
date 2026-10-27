---
title: "Right-, left- and two-sided sequences"
description: "Where a sequence is nonzero (right-sided, left-sided, two-sided, finite) fixes the shape of its ROC and, for an impulse response, causality: causal, anti-causal or non-causal."
tags: [concept, signals, z-transform, roc]
aliases: ["right-sided", "left-sided", "two-sided", "anti-causal", "sided sequences"]
---

*Lectures 7 (Wed Sep 9) §1 and 11 (Fri Sep 18) §1.1 · [[homework/hw3|HW3]] #1, #3(c), [[homework/hw4|HW4]] #1 · families: [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/all-possible-rocs|all possible ROCs]]*

> [!abstract] In one breath
> - Right-sided ($x[n]=0$ for $n<n_0$) → ROC outside a circle; left-sided ($x[n]=0$ for $n>n_0$) → inside; two-sided → a ring; finite → everything but maybe $0$, $\infty$.
> - Samples at $n<0$ cost $z=\infty$; samples at $n>0$ cost $z=0$.
> - For $h[n]$: causal, anti-causal or non-causal; causal $\iff$ ROC includes $z=\infty$.

## 1. Definitions

> [!key] Definitions (Lecture 7 §1, Lecture 11 §1.1)
> - **Right-sided:** $x[n] = 0$ for $n < n_0$. **Left-sided:** $x[n] = 0$ for $n > n_0$ ($n_0$ any sign).
> - **Two-sided:** neither. **Finite-length:** both.
> - Impulse response: **causal** $h[n]=0$ for $n<0$ (present and past only); **anti-causal** $h[n]=0$ for $n\ge0$ (future only); otherwise **non-causal** (some future and some present/past). (Lecture 11 notes print "Non-causal – a system is *causal* if…"; read "non-causal".)

## 2. ROC shape by extent

| sequence | example | ROC | as $h[n]$ |
|---|---|---|---|
| right-sided, $n_0 \ge 0$ | $\left(\frac12\right)^n u[n]$ | $\lvert z\rvert > \frac12$ (includes $\infty$) | causal |
| right-sided, $n_0 < 0$ | $\left(\frac12\right)^n u[n+2]$ | $\frac12 < \lvert z\rvert < \infty$ | non-causal |
| left-sided, $n_0 \le -1$ | $-2^n u[-n-1]$ | $\lvert z\rvert < 2$ (includes $0$) | anti-causal |
| left-sided, $n_0 > 0$ | $3^n u[-n+2]$ | $0 < \lvert z\rvert < 3$ | non-causal |
| two-sided | $\left(\frac12\right)^{\lvert n\rvert}$ | $\frac12 < \lvert z\rvert < 2$ | non-causal |
| finite, around $n=0$ | $\delta[n+1]+\delta[n]+\delta[n-1]$ | $0 < \lvert z\rvert < \infty$ | non-causal |

- Samples at $n<0$ give $z^{\lvert n\rvert}$ (lose $z=\infty$); samples at $n>0$ give $z^{-n}$ (lose $z=0$). Lecture 7: $\delta[n]+\delta[n-1]\leftrightarrow1+z^{-1}$, $\lvert z\rvert>0$; $\delta[n+1]+\delta[n]\leftrightarrow z+1$, $\lvert z\rvert<\infty$; their sum $0<\lvert z\rvert<\infty$.
- Rational transforms: right-sided starting at $n\ge0$ → $\lvert z\rvert>\lvert p_{\max}\rvert$; left-sided ending at $n\le-1$ → $\lvert z\rvert<\lvert p_{\min}\rvert$ ([[concepts/region-of-convergence|ROC rules]]).
- FA2025 #5a: $e^{j\pi n/3}u[n+4]\leftrightarrow\dfrac{e^{-j4\pi/3}z^{4}}{1-e^{j\pi/3}z^{-1}}$, ROC $1<\lvert z\rvert<\infty$.
- Two-sided $h = h_r + h_l$, $h_r = h[n]u[n]$, $h_l = h[n]u[-n-1]$: stable iff the annulus contains $\lvert z\rvert=1$; the anti-causal part runs as a backward recursion ([[problems/two-sided-systems-as-recursions|Two-sided systems as recursions]]). Left-sided systems run backward in time (Lecture 11 slide 7: $y[n] = 3y[n+1] + x[n+1]$, $H(z) = \dfrac{z}{1-3z}$, $\lvert z\rvert < \tfrac13$).

> [!trap]
> - Right-sided is not causal: $\delta[n+1]$ ([[exams/midterm-1/past-exams/spring-2023|SP2023]] T/F (c)).
> - "Left-sided can never be causal" is marked True by the key ([[exams/midterm-1/past-exams/fall-2025|FA2025]] T/F (d)); strictly, $\delta[n]$ is both ([[0-toolkit/05-errata|errata]]).
> - Two-sided can be stable: $\left(\frac12\right)^{\lvert n\rvert}$; stable with poles $\frac14$ and $3$ must be two-sided.
> - $u[-n]$ includes $n=0$, $u[-n-1]$ does not.
> - Typed Lecture 7 slide 7 writes "left-sided: $x[n]=0,\ n<n_0$"; read $n>n_0$ ([[0-toolkit/05-errata|errata]]).

> [!exam] On the exams
> Sidedness decides the ROC in every z-transform and all-possible-ROCs problem; causal/anti-causal labels in T/F.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #5a, #7, T/F (d)]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #5b]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 T/F (c)]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #8]]

**Where it appears:** [[2-z-transform/07-z-transform-properties|L7]] §1, [[2-z-transform/11-bibo-stability-and-causality|L11]] §1.1 (Fig. 1); [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/all-possible-rocs|All possible ROCs (inverse z by partial fractions)]], [[problems/two-sided-systems-as-recursions|Two-sided systems as recursions]]; [[homework/hw3|HW3]] #1, #3(c), [[homework/hw4|HW4]] #1.

## Related
[[concepts/region-of-convergence]] · [[concepts/causality]] · [[concepts/bibo-stability]] · [[concepts/inverse-z-transform]] · [[concepts/z-transform-pairs]]

### Sources for this page
Lecture 7 notes §1 (rules 4–5); Lecture 11 notes §1.1 (eqs. 15–18, Fig. 1, Table 1) and slides 6–7; FA2025 #5a/#7, SP2025 #5b keys and T/F items cited.
