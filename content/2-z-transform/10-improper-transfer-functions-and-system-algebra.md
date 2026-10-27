---
title: "Lecture 10 — Improper transfer functions and system algebra"
description: "Improper H(z) (input taps reaching as far back as feedback taps): long division then PFE, or PFE of 1/A(z) plus shifts; series multiplies, parallel adds."
tags: [lecture, midterm-1, z-transform, lccde, systems]
lecture: 10
---

*Lecture 10 · Wed Sep 16, 2026 · notes + slides "Transfer functions and LTI system response: Part 2" · prev: [[2-z-transform/09-transfer-functions|Lecture 9]] · next: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

> [!abstract] In one breath
> - PFE needs a **proper** $H(z)$ (degrees counted in $z^{-1}$). Improper: long-divide first (quotient → impulses, remainder → PFE), or expand $1/A(z)$ and add shifted copies.
> - Series multiplies ($h_1*h_2 \leftrightarrow H_1H_2$), parallel adds ($h_1+h_2 \leftrightarrow H_1+H_2$): any network collapses to one $H(z)$.

## What was covered

1. **§1 Improper rational expressions** (eqs. 1–3), **§1.1 Applying polynomial long-division** (eqs. 4–11, Exercise 1, slides 4–8), **§1.2 A simpler approach** (eqs. 12–14) → [[concepts/partial-fraction-expansion|Partial fraction expansion]] §3; drill → [[0-toolkit/04-factoring-and-long-division|long division]].
2. **§2 System algebra** (eqs. 15–20, Table 1, Fig. 1, slide 11) → [[concepts/system-algebra|System algebra]]; stable wholes from unstable parts → [[concepts/pole-zero-cancellation|pole-zero cancellation]].

## Exercises from this lecture

- Exercise 1 (notes, slides 4–8), causal $y[n]=2y[n-1]+3y[n-2]+x[n]-3x[n-1]+x[n-2]+4x[n-3]$, by long division then cover-up, and again with the numerator-1 trick ($g[n]-3g[n-1]+g[n-2]+4g[n-3]$); proper or improper? $\frac{z(z-4)}{z^2-5z+6}$ (HW4 #3a) → [[concepts/partial-fraction-expansion|PFE]] §3.
- Slide 11, five-block network ($H_1$, then $H_5$ in parallel with $H_2$ followed by $H_3 \parallel H_4$), overall $H(z)$ → [[concepts/system-algebra|system algebra]] §2.

**Practice:** [[homework/hw4|HW4]] #3, #5 · [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]] · [[problems/finding-h-from-input-output-pairs|finding h]] · [[exams/midterm-1/true-false-bank|T/F bank]]

## Related

[[2-z-transform/index|Unit 2]] · prev: [[2-z-transform/09-transfer-functions|Lecture 9]] · next: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 10 notes (§1 improper expressions, §1.1 Exercise 1, §1.2 numerator-1 approach, §2 system algebra, Table 1, Fig. 1) and slides 1–11; HW4 #3(a).
