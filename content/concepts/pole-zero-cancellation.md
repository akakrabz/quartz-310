---
title: "Pole-zero cancellation"
description: "A factor (1 − p z⁻¹) in both numerator and denominator cancels: the mode pⁿ disappears, the ROC can grow, and an unstable system or input can give a bounded output."
tags: [concept, z-transform, roc, stability]
aliases: ["pole-zero cancellation", "cancellation"]
---

> [!key] The rule
> A zero and a pole at the **same** $p$ cancel: $p^n$ never appears, and the ROC is set by the poles that **remain**. Hence
> $$
> \text{ROC}\{X_1X_2\} \supseteq R_1\cap R_2, \qquad \text{ROC}\{aX_1+bX_2\} \supseteq R_1\cap R_2 .
> $$

- **Inside one $H(z)$:** HW4 #6: $\frac{1+\frac12 z^{-1}}{(1+\frac12 z^{-1})^2} = \frac{1}{1+\frac12 z^{-1}}$. SP2025 #7: zeros $\pm\alpha$ cancel the pole at $-2$ only for $\alpha^2=4$.
- **Series** $H_1H_2$, **input vs system** $HX$ (Lecture 11: $h = 3^nu[n]$, $x = \delta[n]-3\delta[n-1]$ gives $y=\delta[n]$), **sums** ($u[n] + (\delta[n]-u[n]) = \delta[n]$).

> [!example] FA2025 #6: $H(z) = \dfrac{1-z^{-2}}{(1-2z^{-1})(1+\frac23 z^{-1})}$, causal; $x[n] = 3\delta[n]+2\delta[n-1]$
> $X(z)=3\left(1+\frac23 z^{-1}\right)$ cancels the pole $-\frac23$.

> [!success]- Answer
> $$
> Y(z) = \frac{3\left(1-z^{-2}\right)}{1-2z^{-1}}
> \quad\Longrightarrow\quad
> y[n] = 3(2)^n u[n] - 3(2)^{n-2}u[n-2].
> $$

> [!example] HW4 #5: cascade whose ROC grows
> $h_1 \leftrightarrow \frac{z^{-1}}{(1-z^{-1})(1-\frac12 z^{-1})}$, $|z|>1$ (unstable); $h_2 \leftrightarrow \frac{1-z^{-1}}{1-\frac14 z^{-1}}$ (stable). $H_1H_2 = \frac{z^{-1}}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})}$, $|z|>\tfrac12$: $h[n] = 4\left(\tfrac12\right)^n u[n] - 4\left(\tfrac14\right)^n u[n]$, **stable**.

> [!trap]
> - Only exact matches cancel: FA2025 #8a, zero at $\frac34$ does not cancel the pole $-3$.
> - $\alpha=\pm j2$ gives zeros at $\pm2j$: nothing cancels (SP2025 #7).
> - ROC may grow (SP2021 #7: $\text{ROC}_Y = |z|>1$).
> - "Cascade of two unstable systems cannot be stable" ([[exams/midterm-1/past-exams/spring-2021|SP2021]] T/F (c)) and "one unstable factor makes the cascade unstable" ([[exams/midterm-1/past-exams/fall-2019|FA2019]] T/F (d)): both False.

**Where it appears:** [[2-z-transform/07-z-transform-properties|L7]], [[2-z-transform/09-transfer-functions|L9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]], [[2-z-transform/11-bibo-stability-and-causality|L11]]; [[problems/unbounded-outputs-and-pole-matching]], [[problems/parameters-for-stability]]; [[homework/hw4|HW4]] #5–#6.

## Related
[[concepts/poles-and-zeros]] · [[concepts/region-of-convergence]] · [[concepts/system-algebra]] · [[concepts/marginal-stability]] · [[concepts/bibo-stability]]

### Sources for this page
Lecture 7 §2 and slide Example 2; Lecture 9 §1.2; Lecture 11 §1.2, slide 13; HW4 #5–#6 solutions; Midterm 1 keys cited.
