---
title: "Lecture 8 — The inverse z-transform"
description: "x[n] from X(z) without the contour integral: inspection, table pairs plus shifts, partial fractions by cover-up, conjugate poles into cosines, sides from the ROC."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 8
---

*Lecture 8 · Fri Sep 11, 2026 · notes + slides "Inverse z-transform" · prev: [[2-z-transform/07-z-transform-properties|Lecture 7]] · next: [[2-z-transform/09-transfer-functions|Lecture 9]]*

> [!abstract] In one breath
> - Reshape $X(z)$ into table entries: polynomial → impulses; proper rational → partial fractions $\sum_k \frac{A_k}{1-p_kz^{-1}}$, each $A_k$ by cover-up.
> - The ROC picks each term's side: poles inside the inner circle → right-sided, outside the outer circle → left-sided.

## What was covered

1. **§1 Common forms of the z-transform** (eqs. 1–7) and **§2 The inverse z-transform** (eqs. 8–14, Example 1) → [[concepts/inverse-z-transform|Inverse z-transform]] §1–2.
2. **§2.2 Partial fraction expansion by cover-up** (eqs. 15–31, Exercises 1–2; slides Examples 1(d), 2) → [[concepts/partial-fraction-expansion|Partial fraction expansion]] §1–2.
3. **All possible ROCs** (slides, Example 3, annotated ROC table) → [[concepts/region-of-convergence|Region of convergence]] §3.

## Exercises from this lecture

- Example 1(a)–(c) (slides), by inspection → [[concepts/inverse-z-transform|inverse z-transform]] §2.
- Exercise 1 (notes), $\frac{2-z^{-1}}{1-\frac73z^{-1}+\frac23z^{-2}}$, all three ROCs; Example 2 (slides), $\frac{2-z^{-1}}{1+\frac23z^{-1}-\frac13z^{-2}}$ right-sided; Example 1(d) (slides), poles $1$, $-\tfrac23$, $2$ → [[concepts/partial-fraction-expansion|PFE]] §1.
- Exercise 2 (notes), $\frac{3-\frac32z^{-1}}{1-z^{-1}+z^{-2}}$ causal, conjugate poles $e^{\pm j\pi/3}$ → [[concepts/partial-fraction-expansion|PFE]] §2.
- Example 3 (slides), all ROCs of $\frac{1}{(1-\frac43z^{-1})(1-\frac23z^{-1})}$ → [[concepts/region-of-convergence|ROC]] §3.

**Practice:** [[homework/hw3|HW3]] #3 · [[homework/hw4|HW4]] #1 · [[problems/all-possible-rocs|all possible ROCs]] · [[demos/pole-zero-and-roc-explorer|ROC explorer]]

## Related

[[2-z-transform/index|Unit 2]] · prev: [[2-z-transform/07-z-transform-properties|Lecture 7]] · next: [[2-z-transform/09-transfer-functions|Lecture 9]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 8 notes (§1–2, Exercises 1–2) and slides (Examples 1–3, annotated ROC table).
