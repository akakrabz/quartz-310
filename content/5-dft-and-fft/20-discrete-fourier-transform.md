---
title: "Lecture 20 — The discrete Fourier transform"
description: "Why the DTFT cannot be computed; DFT analysis and synthesis equations; X[k] = X_d(2πk/N); N-periodicity; zero padding; the DFT matrix."
tags: [lecture, midterm-2, dft]
lecture: 20
---

*Lecture 20 · Fri Oct 16, 2026 · notes + slides "Discrete Fourier transform" · prev: [[4-sampling-and-reconstruction/19-aliasing|Lecture 19]] · next: [[5-dft-and-fft/21-dft-properties|Lecture 21]]*

> [!abstract] In one breath
> - A computer cannot evaluate the DTFT: the sum is infinite and $\omega$ is continuous.
> - The DFT keeps $N$ samples and $N$ frequencies: $X[k]=X_d\!\left(\frac{2\pi k}{N}\right)$, $0\le k\le N-1$.
> - $X[k]$ and the inverse DFT are $N$-periodic; zero padding samples the same $X_d(\omega)$ more densely.

## What was covered

1. **§1 Computing the DTFT** (eqs. 1–7, slides 3–5) → [[concepts/dft|DFT]] §1
2. **§2 Discrete Fourier transform** (eqs. 8–9, slide 6) → [[concepts/dft|DFT]] §2
3. **§2.1 Relationship between DTFT and DFT** (eqs. 10–12, Figure 1) → [[concepts/dft|DFT]] §2.1
4. **§2.2 N-periodicity of the DFT** (eqs. 13–19, slides 9–10) → [[concepts/dft|DFT]] §3
5. **§2.3 Zero-padding** (eqs. 20–31, Exercise 1, slides 11–13) → [[concepts/zero-padding|zero padding]]
6. **§2.4 Linear algebra formulation** (eqs. 32–45, optional) → [[concepts/dft|DFT]] §4

## Exercises from this lecture

- Notes Exercise 1, length-16 $x[n]$ padded to 64: which $\tilde X[k]$ equal $X[1]$, $X[9]$ → [[concepts/zero-padding|zero padding]] §2
- Slides Zero-padding Example 1 (slide 12), padded to 48: $Y[k]$ equal to $X[0]$, $X[1]$, $X[4]$ → [[concepts/zero-padding|zero padding]] §2
- Slides Zero-padding Example 2 (slide 13), smallest $N$ holding $X_d(\frac\pi5)$, $X_d(\frac\pi3)$ → [[concepts/zero-padding|zero padding]] §2
- Lecture exercise, columns of $\mathbf W$ orthogonal → [[concepts/dft|DFT]] §4

**Practice:** [[problems/dft-values-and-zero-padding|DFT values and zero padding family]] · [[exams/midterm-2/true-false-bank|T/F bank]] §3, §6

## Related
[[5-dft-and-fft/index|Unit 5]] · [[4-sampling-and-reconstruction/19-aliasing|Lecture 19]] · [[5-dft-and-fft/21-dft-properties|Lecture 21]] · [[concepts/index|Concepts]]

### Sources for this page
Snyder, Lecture 20 notes (§1–2.4, eqs. 1–45, Figure 1, Exercise 1) and slides 3–13, Oct 16, 2026.
