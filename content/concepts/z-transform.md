---
title: "z-transform"
description: "X(z) = Σ x[n] z⁻ⁿ with its region of convergence: turns convolution into multiplication and LCCDEs into algebra; its poles decide causality and stability."
tags: [concept, z-transform, roc]
aliases: ["z transform", "X(z)"]
---

> [!key] Definition (Lecture 6)
> $$
> X(z) = \sum_{n=-\infty}^{\infty} x[n]\,z^{-n}, \qquad z \in \mathbb{C}, \qquad x[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; X(z)
> $$
> Valid on the [[concepts/region-of-convergence|ROC]]. **The ROC is part of the transform.**

- **Why:** $z^n$ into an LTI system gives $H(z)\,z^n$ ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]); convolution becomes $Y(z)=H(z)X(z)$.
- **ROC is a ring:** only $|z|$ affects convergence.
- **Unit circle:** $X(e^{j\omega})=X_d(\omega)$ when the ROC contains $|z|=1$; $2^nu[n]$ has a z-transform but no DTFT.

> [!example] Lecture 6, Exercises 1–2
> $$
> \begin{gathered}
> u[n]\leftrightarrow\frac{1}{1-z^{-1}},\ |z|>1;\qquad -u[-n-1]\leftrightarrow\frac{1}{1-z^{-1}},\ |z|<1;\\
> a^nu[n]\leftrightarrow\frac{1}{1-az^{-1}},\ |z|>|a| .
> \end{gathered}
> $$
> Finite: $\{\underset{\uparrow}{1},\ -\tfrac14,\ \tfrac{1}{16}\}\leftrightarrow 1 - \tfrac14 z^{-1} + \tfrac{1}{16}z^{-2}$, ROC $z\neq0$.

> [!recipe] Find $X(z)$ and its ROC
> 1. Split $x[n]$ into [[concepts/z-transform-pairs|table rows]] (Euler; $a^n u[n-k] = a^k\,a^{n-k}u[n-k]$; right + left parts).
> 2. Transform each with its ROC, using [[concepts/z-transform-properties|properties]].
> 3. Add; ROC = intersection (empty ⇒ no transform).
> 4. State the ROC, including $z=0$, $z=\infty$.

> [!trap]
> - No ROC, incomplete answer (rubrics deduct even a missing $|\cdot|$).
> - $z^{-n}$, not $z^n$: sample at $n=-3$ multiplies $z^{3}$.
> - Left-sided pair has a minus: $-a^nu[-n-1]$.
> - A sinusoid for all $n$ has an empty ROC ([[exams/midterm-1/past-exams/spring-2025|SP2025]] T/F (c)).

**Where it appears:** [[2-z-transform/06-the-z-transform|L6]]–[[2-z-transform/11-bibo-stability-and-causality|L11]], [[3-fourier-analysis/14-dtft-properties|L14]]; [[problems/z-transform-with-roc]] (6/7 exams); [[homework/hw3|HW3]], [[homework/hw4|HW4]].

## Related
[[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/z-transform-properties]] · [[concepts/inverse-z-transform]] · [[concepts/poles-and-zeros]] · [[concepts/transfer-function]] · [[demos/pole-zero-and-roc-explorer]]

### Sources for this page
Lecture 6 notes §1–2 (Exercises 1–2, Table 1); Lecture 7 §1; Lecture 8 slides Example 1(a); Lecture 14 §1; HW3 rubric.
