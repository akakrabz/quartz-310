---
title: "Demo — Pole-zero plot and every possible ROC"
description: "Type H(z) in powers of z⁻¹ or pick a preset; see poles and zeros, every valid ROC with causality and stability, the PFE coefficients, and h[n] as formula and stem plot."
tags: [demo, z-transform, roc, stability, midterm-1]
---

*Demo · pairs with [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] and [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · concepts: [[concepts/region-of-convergence]], [[concepts/partial-fraction-expansion]], [[concepts/bibo-stability]], [[concepts/pole-zero-cancellation]]*

<div class="ece-demo">
<iframe src="/static/demos/pole-zero-roc/" title="Pole-zero plot and ROC explorer — interactive demo" loading="lazy" style="height:1500px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/pole-zero-roc/).

**Input.** Coefficients of $z^{0}, z^{-1}, \dots$: numerator b, denominator a ($a[0]=1$), the `b, a` of `lfilter`. $\dfrac{2 - z^{-1}}{1 - \frac73 z^{-1} + \frac23 z^{-2}}$ is b = `2, -1`, a = `1, -7/3, 2/3`; factors such as `(1, -1/3)(1, -2)` also work.

## What to try

1. **Every ROC, [[exams/midterm-1/past-exams/fall-2023|FA2023 #6]]:** poles $\tfrac12$, $2$ give three ROCs. The $A_k$ ($\tfrac13$, $\tfrac23$) never change; only each pole's side does.
2. **Three ROCs, not four, [[exams/midterm-1/past-exams/fall-2019|FA2019 #7]]:** b = `2, -(1/2 + exp(j*pi/3))`, a = `(1, -exp(j*pi/3))(1, -1/2)`. Pole $\tfrac12$ left with $e^{j\pi/3}$ right would need an empty region.
3. **Stability picks the ROC, [[exams/midterm-1/past-exams/fall-2025|FA2025 #7]]:** $\tfrac23<|z|<2$ is stable, $h[n] = -\tfrac54\left(-\tfrac23\right)^n u[n] - \tfrac94(-2)^n u[-n-1]$. HW4 #1(a) has a pole at $-1$: no stable ROC.
4. **Complex poles → cosine:** Lecture 8, Exercise 2 gives $3\cos\left(\tfrac{\pi}{3}n\right)u[n]$; [[exams/midterm-1/past-exams/spring-2021|SP2021 #5]] gives $3\sin\left(\tfrac{\pi}{2}n\right)u[n]$. Both marginally stable.
5. **Improper, Lecture 10:** $C_0=\tfrac59$, $C_1=-\tfrac43$, $A_1=\tfrac{7}{36}$ at 3, $A_2=\tfrac14$ at $-1$. Innermost ROC is $0<|z|<1$ (non-causal, not anti-causal).
6. **Cancellation removes an ROC:** SP2025 #8 output loses the pole at $-\tfrac32$; FA2019 #10(d) cascade is stable. Numerator `(2, -3)(1, 1.5001)` gives a near-cancellation warning and keeps all three ROCs.
7. **Parameter for stability, [[exams/midterm-1/past-exams/spring-2025|SP2025 #7]]:** a = `1, 3/2, -1` (poles $-2$, $\tfrac12$). b = `1, 0, -4` cancels $-2$: stable. b = `1, 0, 4`: unstable.
8. **Repeated pole:** no simple-pole $A_k$; $h[n] = (n+1)\left(\tfrac12\right)^n u[n]$ plotted numerically.

> [!trap]
> - No positive powers of $z$: shift $h[n]$ by hand for a time advance (HW4 #1(b)).
> - Cancellation needs agreement to $10^{-7}$; fractions are a display of floating-point roots.
> - Not a frequency-response tool: use the [[demos/frequency-response-explorer|frequency-response explorer]].

> [!exam]
> Inverse z, PFE, all possible ROCs and pole matching: 7/7 past Midterm 1 exams; parameters for stability: 3/7.
> - [[problems/all-possible-rocs]] · [[problems/unbounded-outputs-and-pole-matching]] · [[problems/parameters-for-stability]] · [[0-toolkit/05-errata|errata]]

## Related
[[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros]] · [[concepts/inverse-z-transform]] · [[concepts/marginal-stability]] · [[concepts/transfer-function]] · [[demos/python-demos|Python demos]] · [[demos/index|all demos]]

### Sources for this page
Lecture 8 notes (Exercises 1–2); Lecture 10 notes (Exercise 1); Lecture 11 notes (Table 1); HW3 #4, HW4 #1; FA2025 #6–8, SP2025 #7–8, FA2023 #6, SP2021 #5, FA2019 #7, #10 keys.
