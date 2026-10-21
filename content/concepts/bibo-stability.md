---
title: "BIBO stability"
description: "Bounded input ⇒ bounded output. Three equivalent tests (definition, absolutely summable h[n], ROC contains the unit circle), the HW4 proof, recurring T/F traps."
tags: [concept, stability, systems, midterm-1]
aliases: ["BIBO stable", "BIBO stability", "stability", "stable", "unstable", "bounded-input bounded-output"]
---

> [!key] Three equivalent tests
> 1. **Any system:** $\lvert x[n]\rvert\le B_x<\infty$ for all $n$ $\Rightarrow$ $\lvert y[n]\rvert\le B_y<\infty$ for all $n$.
> 2. **LTI:** stable $\iff$
> $$
> \sum_{n=-\infty}^{\infty}\lvert h[n]\rvert<\infty .
> $$
> 3. **LTI:** stable $\iff$ ROC of $H(z)$ contains $\lvert z\rvert=1$. Causal: all poles $\lvert p\rvert<1$. Poles counted **after** cancellation.

- **FIR ⇒ stable.** A pole on $|z|=1$ is unstable ([[concepts/marginal-stability|marginal stability]]).
- **Not LTI:** bound $\lvert y\rvert$ by $B_x$, or give one bounded input with unbounded output ($x=1$ into $\lvert n\rvert x[n]$).
- $a^nu[n]$ summable iff $\lvert a\rvert<1$; $a^nu[-n-1]$ iff $\lvert a\rvert>1$.

> [!derivation]- Proof: $\sum\lvert h\rvert<\infty\iff$ BIBO stable (HW4 #2)
> **Sufficiency.**
> $$
> \lvert y[n]\rvert\le\sum_k\lvert h[k]\rvert\,\lvert x[n-k]\rvert\le B_x\sum_k\lvert h[k]\rvert<\infty .
> $$
> **Necessity.** If $\sum_k\lvert h[k]\rvert=\infty$, take $x[n]=h^*[-n]/\lvert h[-n]\rvert$ (0 where $h[-n]=0$); then $y[0]=\sum_k\lvert h[k]\rvert=\infty$.

> [!trap]
> - Bounded $h$ is not stable: $h=u[n]$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #1a]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #1c]]); $\sum\lvert h\rvert$ is an LTI-only test ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1b]]).
> - Stable system, unbounded input: output can be bounded ($h=\delta[n]-2\delta[n-1]$ maps $2^nu[n]$ to $\delta[n]$). Unstable system: only *some* bounded input blows up.
> - Two unstable systems can combine to a stable one, in parallel ($u[n]+(\delta[n]-u[n])$) or series ($\frac{1-2z^{-1}}{1-3z^{-1}}\cdot\frac{1-3z^{-1}}{1-2z^{-1}}=1$, both causal). Unstable in series with stable likewise ([[homework/hw4|HW4]] #5, pole-zero cancellation).
> - Two-sided can be stable: $(\tfrac12)^{\lvert n\rvert}$. A formula without an ROC does not decide stability ([[exams/midterm-1/past-exams/fall-2024|FA2024 #1f]]).

**Where it appears:** [[1-signals-and-systems/03-system-properties|L3]], [[1-signals-and-systems/04-impulse-response-and-convolution|L4]], [[2-z-transform/11-bibo-stability-and-causality|L11]], [[3-fourier-analysis/14-dtft-properties|L14]]; [[homework/hw4|HW4]] #2–#5; [[problems/classifying-system-properties]], [[problems/unbounded-outputs-and-pole-matching]], [[problems/parameters-for-stability]]; [[exams/midterm-1/true-false-bank]].

## Related
[[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]] · [[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/causality|causality]]

### Sources for this page
Lecture 3 §2.4; Lecture 4 §2.1; Lecture 11 §1, Table 1; Lecture 14 §1; HW4 #2, #3, #5 solutions; Midterm 1 T/F items.
