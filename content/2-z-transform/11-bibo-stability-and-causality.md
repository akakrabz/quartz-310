---
title: "Lecture 11 — BIBO stability and causality in the z-domain"
description: "Third BIBO test (ROC contains the unit circle); ROC shape ⇔ causal, anti-causal, two-sided; stability from the poles; FIR always stable; marginal stability, pole matching."
tags: [lecture, midterm-1, stability, roc, z-transform]
lecture: 11
---

*Lecture 11 · Fri Sep 18, 2026 · notes + slides "BIBO stability and causality" · prev: [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] · next: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]]*

> [!abstract] In one breath
> - LTI BIBO stable $\iff \sum_n \lvert h[n]\rvert < \infty \iff$ ROC of $H(z)$ contains $\lvert z\rvert = 1$.
> - Causal ⇔ ROC outside a circle to $\infty$; causal and stable ⇔ all poles inside the unit circle.
> - Marginally stable (poles on $\lvert z\rvert=1$): only a matching input pole gives an unbounded output.

## What was covered

1. **§1 BIBO stability in the z-domain** (eqs. 1–7) → [[concepts/bibo-stability|BIBO stability]] §2.
2. **§1.1 Identifying causal and non-causal systems** (eqs. 8–18, Figs. 1–2, slides 6–7, Table 1) → [[concepts/bibo-stability|BIBO stability]] §3, [[concepts/region-of-convergence|ROC]] §4, [[concepts/causality|causality]].
3. **§1.2 Unstable inputs and marginal stability** (eqs. 19–20, slides 12–14) and **§1.2.1 Marginal stability** (eqs. 21–28, slides 15–18, lecture exercise) → [[concepts/marginal-stability|Marginal stability]] §1–3.

## Exercises from this lecture

- Slide 7, $y[n]=3y[n+1]+x[n+1]$ → [[concepts/sided-sequences|sided sequences]] §2.
- Slides 10–11, the stable $h[n]$ of two $H(z)$; can FIR be unstable? → [[concepts/bibo-stability|BIBO stability]] §3.
- Slides 12–14, $3^nu[n]$ and $(-1)^nu[n]$ → [[concepts/marginal-stability|marginal stability]] §1.
- Slides 16–17, notes example $a=b=1$, lecture exercise → [[concepts/marginal-stability|marginal stability]] §2.
- Slide 18, eight inputs, $\frac{1}{(1-jz^{-1})(1+z^{-1})(1-\frac23z^{-1})}$ → [[concepts/marginal-stability|marginal stability]] §3.

**Practice:** [[homework/hw4|HW4]] #2–4 · [[problems/unbounded-outputs-and-pole-matching|pole matching]] · [[problems/parameters-for-stability|stability parameters]]

## Related

[[2-z-transform/index|Unit 2]] · prev: [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] · next: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 11 notes (§1–1.2.1, Figs. 1–2, Table 1) and slides 1–18.
