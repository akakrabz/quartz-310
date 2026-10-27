---
title: "Lecture 12 — Convolution as template matching"
description: "Convolution as a sliding inner product; matched filter h[n] = t[−n]; 2-D convolution of images, shape and line-feature kernels. Not tested."
tags: [lecture, convolution, template-matching, unit-3]
lecture: 12
---

*Lecture 12 · Mon Sep 21, 2026 · notes + slides "Convolution as template matching" · prev: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · next: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]]*

> [!abstract] In one breath
> - Each convolution output is an inner product with the flipped, shifted kernel: a similarity score.
> - Matched filter $h[n]=t[-n]$: the output peaks at copies of the template.
> - 2-D: the same flip–slide–multiply–add over an image. Not tested (slide 2).

## What was covered

1. **§1 Identifying patterns in signals** (inner product, slide 5) → [[concepts/template-matching|Template matching]] §1, [[concepts/convolution|Convolution]]
2. **§1.1 Matched filters** (eqs. 1–2, Figures 1–2, slides 3–5) → [[concepts/template-matching|Template matching]] §2
3. **§2 Two-dimensional convolution** (eq. 3, Figure 3, slide 6) → [[concepts/template-matching|Template matching]] §3
4. **§2.1 Two-dimensional pattern matching example** (Figures 4–6, slides 7–10) → [[concepts/template-matching|Template matching]] §4
5. **§2.2 Highlighting features in handwritten digits** (eqs. 4–5, Figures 7–9, slides 11–14) → [[concepts/template-matching|Template matching]] §5

## Exercises from this lecture

- Slide 5, what convolution computes at each shift → [[concepts/template-matching|Template matching]] §1
- Slides 3–5 / Figures 1–2, sawtooth template, five copies → §2 · slide 6 / Figure 3, three pixels of a 2-D convolution → §3

**Practice:** none (not on homework or exams) · [[demos/convolution-explorer|convolution explorer]] · [[demos/python-demos|Python demos]]

## Related

[[3-fourier-analysis/index|Unit 3]] · prev: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · next: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 12 notes (§1–2.2, eqs. 1–5, Figs. 1–9); slides 1–14.
