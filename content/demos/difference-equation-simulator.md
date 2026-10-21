---
title: "Demo — Difference-equation simulator (recursion, poles, stability, resonance)"
description: "Enter a causal LCCDE and an input; the demo runs the recursion, draws poles, zeros and ROC, and says whether the system is stable and whether this output stays bounded."
tags: [demo, lccde, stability, z-transform, midterm-1]
---

*Demo · pairs with [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/09-transfer-functions|Lecture 9]] and [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · concepts: [[concepts/lccde]], [[concepts/bibo-stability]], [[concepts/marginal-stability]]*

<div class="ece-demo">
<iframe src="/static/demos/difference-equation/" title="Difference-equation simulator — interactive demo" loading="lazy" style="height:1450px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/difference-equation/).

**Input.** Standard form $y[n] + \sum_{k\ge1} a_k\,y[n-k] = \sum_{k\ge0} b_k\,x[n-k]$, causal, at rest (the `b, a` of `lfilter`). Shows $x[n]$, $y[n]$, poles ×, zeros ○, input poles ◇ and zeros □, the causal ROC, a system verdict and an output verdict.

## What to try

1. **Real-time recursion:** $y[n] = \tfrac12 y[n-1] + x[n]$; with $u[n]$ the step response is $2 - (\tfrac12)^n$.
2. **Sign flip:** Lecture 5 Exercise 1, $y[n] = \tfrac14 y[n-1] - x[n] + \tfrac12 x[n-2]$, is $a = (1, -\tfrac14)$, $b = (-1, 0, \tfrac12)$: $h[0], h[1], h[2] = -1, -\tfrac14, \tfrac{7}{16}$.
3. **Cancellation, [[homework/hw4|HW4 #6]]:** $(1 + \tfrac12 z^{-1})^2$ denominator, one pole cancelled; $(-1)^n u[n]$ gives $y[n] = [2(-1)^n - (-\tfrac12)^n]u[n]$.
4. **Resonance:** accumulator with $u[n]$ gives $n+1$; with $(-1)^n u[n]$, bounded. [[exams/midterm-1/past-exams/spring-2021|SP2021 #5]]: $\cos(\pi n/2)u[n]$ resonates with $\pm j$, $\cos(\pi n/3)u[n]$ does not.
5. **[[exams/midterm-1/past-exams/fall-2025|FA2025 #8]] trap:** pole $e^{j2/3}$ is at $\approx 0.21\pi$, not $2\pi/3$; $\sin(\pi n/2)u[n]$ is unbounded via the pole at $j$.
6. **[[exams/midterm-1/past-exams/spring-2025|SP2025 #6]]:** pole $e^{j\pi/4}$. Unbounded: $e^{j\pi n/4}u[n]$, $\cos(\pi n/4)u[n]$, $4^nu[n]$. Bounded: $u[n]$, $e^{-j\pi n/4}u[n]$, $e^{-j3\pi n/4}u[n]$.
7. **Which pole is cancelled:** SP2025 #8 input cancels the unstable pole (bounded); FA2025 #6 cancels only $-\tfrac23$ ($3(2)^n$ survives); [[exams/midterm-1/past-exams/fall-2019|FA2019 #10]] cancels the input's pole at $2$.
8. **SP2025 #7:** a = `1, 3/2, -1`; only b = `1, 0, -4` ($\alpha=\pm2$) is stable.
9. **Butterworth nudge:** $a_2$ from $0.17157$ to $1.01$ moves poles from $\pm0.414j$ to $\pm1.005j$; growth is slow (about ×4.4 over 300 samples).

> [!trap]
> - Marginally stable is still not BIBO stable.
> - The plot shows $N+1$ samples: slow divergence looks flat; trust the pole verdict.
> - Type exact values: $0.7071$ is not $\tfrac{\sqrt2}{2}$.

Causal, at-rest systems with inputs from $n=0$ only; run two-sided systems as backward recursions ([[problems/two-sided-systems-as-recursions]]).

## Related
[[concepts/lccde]] · [[concepts/transfer-function]] · [[concepts/poles-and-zeros]] · [[concepts/pole-zero-cancellation]] · [[problems/lccde-to-transfer-function-and-response]] · [[problems/unbounded-outputs-and-pole-matching]] · [[problems/parameters-for-stability]] · [[demos/pole-zero-and-roc-explorer]] · [[supplements/demo-notebooks|course notebooks]]

### Sources for this page
Lecture 5 notes §1 (Eqs. 3–7, Exercise 1); Lecture 9; Lecture 11 notes §1.2; HW4 #6; SP2021 #5, FA2025 #6, #8, SP2025 #6–8, FA2019 #10 keys; notebooks `demo_difference_equations`, `demo_stability`.
