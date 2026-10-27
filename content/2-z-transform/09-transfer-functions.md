---
title: "Lecture 9 — Transfer functions and LTI system response"
description: "Y(z) = H(z)X(z); LCCDE ⇄ H(z) in both directions and the Lecture 5 vs Lecture 9 sign convention; poles, zeros, order; FIR vs IIR."
tags: [lecture, midterm-1, z-transform, lccde, systems]
lecture: 9
---

*Lecture 9 · Mon Sep 14, 2026 · notes + slides "Transfer functions and LTI system response: Part 1" · prev: [[2-z-transform/08-inverse-z-transform|Lecture 8]] · next: [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]*

> [!abstract] In one breath
> - Convolution becomes multiplication: $Y(z) = H(z)X(z)$, with transfer function $H(z) = Y(z)/X(z) = \mathcal{Z}\{h[n]\}$.
> - z-transform an LCCDE: each delay becomes $z^{-k}$, giving $H(z)$ in one line; read it backwards for the LCCDE.
> - Uncancelled finite poles ⇒ IIR; none ⇒ FIR.

## What was covered

1. **§1 LTI system response with the z-transform** (eqs. 1–3) → [[concepts/transfer-function|Transfer function]] §1.
2. **§1.1 Transfer functions and LCCDEs** (eqs. 4–12, both directions, Exercise 1, the Lecture 5 sign convention) → [[concepts/transfer-function|Transfer function]] §2; [[concepts/lccde|LCCDE]].
3. **§1.2 Characterizing transfer functions** (poles, zeros, order; Fig. 1 FIR/IIR flowchart) → [[concepts/poles-and-zeros|Poles and zeros]] §2; the rule → [[concepts/fir-and-iir|FIR and IIR]].

## Exercises from this lecture

- Exercise 1 (notes; slides with $\tfrac13$), $h[n]$ of the causal $y[n]=\tfrac12y[n-1]+x[n]$; Exercise 2 (slides), $y[n]=\tfrac13y[n-1]+x[n]-3x[n-1]+x[n-2]$, an improper $H$; Exercise 3 (slides), $y[n]=\tfrac12y[n-1]+\tfrac3{16}y[n-2]+x[n]-3x[n-1]$ by cover-up → [[concepts/transfer-function|transfer function]] §2.
- Feedback yet FIR, $y[n]=y[n-1]+x[n]-x[n-2]$ → [[concepts/poles-and-zeros|poles and zeros]] §2.

**Practice:** [[homework/hw3|HW3]] #4 · [[homework/hw4|HW4]] #3–6 · [[problems/lccde-to-transfer-function-and-response|LCCDE → H(z) → response]] · [[demos/difference-equation-simulator|simulator]]

## Related

[[2-z-transform/index|Unit 2]] · prev: [[2-z-transform/08-inverse-z-transform|Lecture 8]] · next: [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 9 notes (§1, §1.1 with Exercise 1, §1.2, Fig. 1); slides 1–8 (Exercises 1–3); Lecture 5 notes eq. (1).
