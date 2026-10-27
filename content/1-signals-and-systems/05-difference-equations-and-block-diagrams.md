---
title: "Lecture 5 — Difference equations and block diagrams"
description: "LCCDEs as descriptions of LTI systems: FIR (no feedback) versus IIR (feedback), impulse responses of recursions by superposition, the sign conventions, direct-form I block diagrams."
tags: [lecture, midterm-1, systems, lccde]
lecture: 5
---

*Lecture 5 · Wed Sep 2, 2026 · notes + slides "Difference equations and block diagrams" · prev: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · next: [[2-z-transform/06-the-z-transform|Lecture 6]]*

> [!abstract] In one breath
> - An LCCDE: each output a fixed linear combination of current/past inputs and past outputs; at rest it is LTI.
> - No feedback: $h[n]$ = the input coefficients (FIR). Feedback: $h[n]$ can ring forever (IIR).
> - Block diagrams: delays, gains, adders.

## What was covered

1. **§1 Linear constant-coefficient difference equations** (eq. 1, initial rest, sign conventions) → [[concepts/lccde|LCCDE]] §1–2
2. **§1.1 Finite impulse response systems** (eqs. 2–4, moving average) → [[concepts/fir-and-iir|FIR and IIR]] §2
3. **§1.2 Infinite impulse response systems** (eqs. 5–11, Exercise 1) → [[concepts/fir-and-iir|FIR and IIR]] §3
4. **§2 Block diagrams** (Figs. 1–4, eq. 12, direct form I) → [[concepts/block-diagram|Block diagram]]

## Exercises from this lecture

- Eqs. 5–7, $h[n]$ of $y[n] = \frac12 y[n-1] + x[n]$; slides Example 1, $y[n] = \frac13 y[n-1] + x[n]$ → [[concepts/fir-and-iir|FIR and IIR]] §3
- Exercise 1, $y[n] = \frac14 y[n-1] - x[n] + \frac12 x[n-2]$; slides Example 2, $y[n] = \frac13 y[n-1] + x[n] - 3x[n-1] + x[n-2]$ → [[concepts/fir-and-iir|FIR and IIR]] §3
- Eq. 12 and Fig. 4, direct form I of $y[n] = \frac12 y[n-1] + \frac12 y[n-2] + 3x[n] - 2x[n-1] + x[n-2]$ → [[concepts/block-diagram|Block diagram]] §1–2

**Practice:** [[homework/hw2|HW2]] #1 · [[problems/lccde-to-transfer-function-and-response|LCCDE → $H(z)$ → response]] · [[problems/two-sided-systems-as-recursions|two-sided recursions]] · [[demos/difference-equation-simulator|simulator]]

## Related

[[1-signals-and-systems/index|Unit 1]] · prev: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] · next: [[2-z-transform/06-the-z-transform|Lecture 6]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 5 notes (§1–2, Exercise 1, Fig. 4) and slides (Examples 1–2), Sep 2, 2026.
