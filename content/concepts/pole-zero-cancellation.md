---
title: "Pole-zero cancellation"
description: "A factor (1 − p z⁻¹) in both numerator and denominator cancels: the mode pⁿ disappears, the ROC can grow, and an unstable system or input can give a bounded output."
tags: [concept, z-transform, roc, stability]
aliases: ["pole-zero cancellation", "cancellation"]
---

*Lectures 7 (Wed Sep 9) §2, 9 §1.2, 10 §2 and 11 (Fri Sep 18) §1.2 · [[homework/hw4|HW4]] #5–#6 · families: [[problems/unbounded-outputs-and-pole-matching|pole matching]], [[problems/parameters-for-stability|parameters for stability]]*

> [!abstract] In one breath
> - A zero and a pole at the same $p$ cancel: the mode $p^n$ never appears and the ROC is set by the remaining poles.
> - Hence "at least the intersection" for products and sums; the ROC can grow (Lecture 7, Example 2).
> - Cancel before judging stability, causality or FIR/IIR; an input zero on an unstable pole gives a bounded output.

## 1. The rule

> [!key] The rule
> A zero and a pole at the **same** $p$ cancel: $p^n$ never appears, and the ROC is set by the poles that **remain**. Hence
> $$
> \text{ROC}\{X_1X_2\} \supseteq R_1\cap R_2, \qquad \text{ROC}\{aX_1+bX_2\} \supseteq R_1\cap R_2 .
> $$
> $H$ neither blows up nor vanishes at a cancelled pole; it is gone for ROC, stability and FIR/IIR (Lecture 9 §1.2).

## 2. Where it happens

- **Convolution of two signals:** Lecture 7, Example 2 ($c=-1$): the zero of $X_1$ at $-1$ cancels the pole of $X_2$ and the ROC grows from $\lvert z\rvert>1$ to $\lvert z\rvert>\tfrac12$ — worked with its figure on [[concepts/z-transform-properties|z-transform properties]] §3.
- **Inside one $H(z)$:** HW4 #6: $\frac{1+\frac12 z^{-1}}{(1+\frac12 z^{-1})^2} = \frac{1}{1+\frac12 z^{-1}}$. SP2025 #7: zeros $\pm\alpha$ cancel the pole at $-2$ only for $\alpha^2=4$. Feedback yet FIR: $y[n] = y[n-1] + x[n] - x[n-2]$ has $H = 1 + z^{-1}$ ([[concepts/fir-and-iir|FIR and IIR]]).
- **Series** $H_1H_2$ and **sums** $H_1+H_2$ ([[concepts/system-algebra|system algebra]]): $u[n] * (\delta[n] - \delta[n-1]) = \delta[n]$ (series, one unstable); $u[n] + (\delta[n]-u[n]) = \delta[n]$ (parallel, both unstable).
- **Input vs system** $HX$ (Lecture 11 slides 12–13): $h = 3^nu[n]$, $x = \delta[n]-3\delta[n-1]$ gives $Y(z)=\frac{1-3z^{-1}}{1-3z^{-1}}=1$, $y=\delta[n]$ ([[concepts/marginal-stability|marginal stability]] §1).

## 3. Worked examples

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

> [!exam] On the exams
> Output for a short input whose zero cancels a system pole; parameters that place a zero on a bad pole; T/F on cascades of unstable systems.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #6, #8a, T/F (f)]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #7]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #7, T/F (c)]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 T/F (d)]] · families: [[problems/unbounded-outputs-and-pole-matching|pole matching]], [[problems/parameters-for-stability|parameters for stability]]

**Where it appears:** [[2-z-transform/07-z-transform-properties|L7]] §2 (Example 2), [[2-z-transform/09-transfer-functions|L9]] §1.2, [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]] §2, [[2-z-transform/11-bibo-stability-and-causality|L11]] §1.2; [[problems/unbounded-outputs-and-pole-matching|Unbounded outputs and pole matching]], [[problems/parameters-for-stability|Parameters for stability]]; [[homework/hw4|HW4]] #5–#6.

## Related
[[concepts/poles-and-zeros]] · [[concepts/region-of-convergence]] · [[concepts/system-algebra]] · [[concepts/marginal-stability]] · [[concepts/bibo-stability]] · [[concepts/z-transform-properties]] · [[concepts/fir-and-iir]]

### Sources for this page
Lecture 7 §2 and slide Example 2; Lecture 9 §1.2; Lecture 11 §1.2, slide 13; HW4 #5–#6 solutions; Midterm 1 keys cited.
