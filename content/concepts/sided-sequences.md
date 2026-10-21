---
title: "Right-, left- and two-sided sequences"
description: "Where a sequence is nonzero (right-sided, left-sided, two-sided, finite) fixes the shape of its ROC and, for an impulse response, causality: causal, anti-causal or non-causal."
tags: [concept, signals, z-transform, roc]
aliases: ["right-sided", "left-sided", "two-sided", "anti-causal"]
---

> [!key] Definitions (Lectures 7 and 11)
> - **Right-sided:** $x[n] = 0$ for $n < n_0$. **Left-sided:** $x[n] = 0$ for $n > n_0$.
> - **Two-sided:** neither. **Finite-length:** both.
> - Impulse response: **causal** $h[n]=0$ for $n<0$; **anti-causal** $h[n]=0$ for $n\ge0$; otherwise **non-causal**.

| sequence | example | ROC | as $h[n]$ |
|---|---|---|---|
| right-sided, $n_0 \ge 0$ | $\left(\frac12\right)^n u[n]$ | $\lvert z\rvert > \frac12$ (includes $\infty$) | causal |
| right-sided, $n_0 < 0$ | $\left(\frac12\right)^n u[n+2]$ | $\frac12 < \lvert z\rvert < \infty$ | non-causal |
| left-sided, $n_0 \le -1$ | $-2^n u[-n-1]$ | $\lvert z\rvert < 2$ (includes $0$) | anti-causal |
| left-sided, $n_0 > 0$ | $3^n u[-n+2]$ | $0 < \lvert z\rvert < 3$ | non-causal |
| two-sided | $\left(\frac12\right)^{\lvert n\rvert}$ | $\frac12 < \lvert z\rvert < 2$ | non-causal |
| finite, around $n=0$ | $\delta[n+1]+\delta[n]+\delta[n-1]$ | $0 < \lvert z\rvert < \infty$ | non-causal |

- Samples at $n<0$ give $z^{|n|}$ (lose $z=\infty$); samples at $n>0$ give $z^{-n}$ (lose $z=0$).
- FA2025 #5a: $e^{j\pi n/3}u[n+4]\leftrightarrow\dfrac{e^{-j4\pi/3}z^{4}}{1-e^{j\pi/3}z^{-1}}$, ROC $1<|z|<\infty$.
- Two-sided $h = h_r + h_l$: stable iff the annulus contains $|z|=1$; the anti-causal part runs as a backward recursion ([[problems/two-sided-systems-as-recursions]]).

> [!trap]
> - Right-sided is not causal: $\delta[n+1]$ ([[exams/midterm-1/past-exams/spring-2023|SP2023]] T/F (c)).
> - "Left-sided can never be causal" is marked True by the key ([[exams/midterm-1/past-exams/fall-2025|FA2025]] T/F (d)); strictly, $\delta[n]$ is both ([[0-toolkit/05-errata|errata]]).
> - Two-sided can be stable: $\left(\frac12\right)^{|n|}$; stable with poles $\frac14$ and $3$ must be two-sided.
> - $u[-n]$ includes $n=0$, $u[-n-1]$ does not.

**Where it appears:** [[2-z-transform/07-z-transform-properties|L7]], [[2-z-transform/11-bibo-stability-and-causality|L11]]; [[problems/z-transform-with-roc]], [[problems/all-possible-rocs]]; [[homework/hw3|HW3]] #1, #3(c), [[homework/hw4|HW4]] #1.

## Related
[[concepts/region-of-convergence]] · [[concepts/causality]] · [[concepts/bibo-stability]] · [[concepts/inverse-z-transform]] · [[concepts/z-transform-pairs]]

### Sources for this page
Lecture 7 notes §1; Lecture 11 notes §1.1 (Eqs. 15–18, Fig. 1, Table 1); FA2025 #5a/#7, SP2025 #5b keys and T/F items cited.
