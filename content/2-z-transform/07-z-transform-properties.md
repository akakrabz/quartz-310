---
title: "Lecture 7 — Properties of the z-transform"
description: "X(z) is undefined outside its ROC; the ROC rules (no poles, connected, sided shapes); the properties table with ROCs: shift, convolution, differentiation, scaling, reversal, conjugation."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 7
---

*Lecture 7 · Wed Sep 9, 2026 · notes + slides "z-transform properties" · prev: [[2-z-transform/06-the-z-transform|Lecture 6]] · next: [[2-z-transform/08-inverse-z-transform|Lecture 8]]*

> [!abstract] In one breath
> - The ROC is part of $X(z)$: outside it the transform is undefined, even where the formula returns a number.
> - ROC: no poles, connected; right-sided → outside the largest pole, left-sided → inside the smallest.
> - Properties (shift, convolution, $n\,x[n]$, $a^nx[n]$, $x[-n]$) build every transform from a few pairs.

## What was covered

1. **§1 Overview of the z-transform** (eqs. 1–5, ROC rules, Example 1) → [[concepts/region-of-convergence|Region of convergence]] §1–2; definitions → [[concepts/sided-sequences|sided sequences]].
2. **§2 Key properties of the z-transform** (eqs. 6–22, Table 1, Examples 2–3) → [[concepts/z-transform-properties|z-transform properties]]; Example 2's cancelled pole → [[concepts/pole-zero-cancellation|pole-zero cancellation]].

## Exercises from this lecture

- Example 1 (slides), ROC of $\frac{1+3z^{-1}}{1+\frac74z^{-1}-\frac12z^{-2}}$, right- and left-sided → [[concepts/region-of-convergence|ROC]] §2.
- Shift examples (slides), $u[n-3]$, $u[n+2]$; shift via convolution → [[concepts/z-transform-properties|properties]] §2.
- Example 2 (slides), $x_1*x_2$ with $c=\pm1$: ROC the intersection, or larger → [[concepts/z-transform-properties|properties]] §3.
- Example 3 (slides), $2^n\,n\,(\tfrac13)^nu[n]$ two ways → [[concepts/z-transform-properties|properties]] §4.
- Time-reversal proof; $2^nu[-n]$ → [[concepts/z-transform-properties|properties]] §5.

**Practice:** [[homework/hw3|HW3]] #1–2 · [[problems/z-transform-with-roc|z-transform with ROC]] · [[supplements/transform-tables|transform tables]]

## Related

[[2-z-transform/index|Unit 2]] · prev: [[2-z-transform/06-the-z-transform|Lecture 6]] · next: [[2-z-transform/08-inverse-z-transform|Lecture 8]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 7 notes (§1–2, Table 1, derivations, exercises) and slides (Examples 1–3).
