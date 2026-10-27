---
title: "Lecture 6 — The z-transform and the region of convergence"
description: "zⁿ as eigenfunction of LTI systems with eigenvalue H(z); the z-transform sum and its ROC; u[n] vs −u[−n−1]; aⁿu[n]; pole-zero plots; the table of pairs."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 6
---

*Lecture 6 · Fri Sep 4, 2026 · notes + slides "z-transform" · prev: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] · next: [[2-z-transform/07-z-transform-properties|Lecture 7]]*

> [!abstract] In one breath
> - $z_0^{\,n}$ (all $n$) through any LTI system → $H(z_0)\,z_0^{\,n}$, $H(z) = \sum_k h[k]z^{-k}$.
> - z-transform $X(z) = \sum_n x[n]z^{-n}$; it converges only on the ROC.
> - $u[n]$ and $-u[-n-1]$ share $\frac{1}{1-z^{-1}}$; only the ROC tells them apart.

## What was covered

1. **§1 Motivation for the z-transform** (eqs. 1–9; slides 3–6) → [[concepts/eigenfunctions-of-lti-systems|Eigenfunctions of LTI systems]] §1.
2. **§2 The z-transform** (eqs. 10–22, Exercises 1–2, Fig. 1, Table 1) → [[concepts/z-transform|z-transform]] §1–3; Table 1 → [[concepts/z-transform-pairs|z-transform pairs]]; ROC shapes → [[concepts/region-of-convergence|region of convergence]].
3. **§2.1 Linear algebra intuition** (eqs. 23–25, optional) → [[concepts/z-transform|z-transform]] §4.

## Exercises from this lecture

- Exercise 1 (notes; slide 8), $u[n]$ and $-u[-(n+1)]$: same formula, ROC $\lvert z\rvert>1$ vs $\lvert z\rvert<1$ → [[concepts/z-transform|z-transform]] §2.
- Exercise 2 (notes; slide 9, complex $a$), $a^nu[n]\leftrightarrow\frac{1}{1-az^{-1}}$, $\lvert z\rvert>\lvert a\rvert$ → [[concepts/z-transform|z-transform]] §2.
- Fig. 1, pole-zero plots of $u[n]$, $(-\tfrac13)^nu[n]$, $\cos(\tfrac{2\pi}{3}n)u[n]$ → [[concepts/z-transform|z-transform]] §3.
- Slide 6, filtering a sum of exponentials by $\lvert H(z_k)\rvert$ → [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] §1.

**Practice:** [[homework/hw3|HW3]] #1 · [[problems/z-transform-with-roc|z-transform with ROC]] · [[demos/pole-zero-and-roc-explorer|ROC explorer]]

## Related

[[2-z-transform/index|Unit 2]] · prev: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] · next: [[2-z-transform/07-z-transform-properties|Lecture 7]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 6 notes (§1, §2 with Exercises 1–2, Fig. 1, Table 1, §2.1) and annotated slides (Sep 4, 2026).
