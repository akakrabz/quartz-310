---
title: "Lecture 25 — Fast Fourier transform"
description: "Cost of the DFT sum, O(N²); the twiddle factor; radix-2 decimation in time and its merging equations; length-4 and length-8 examples; butterfly diagrams; N log N."
tags: [lecture, dft, fft]
lecture: 25
---

*Lecture 25 · Wed Oct 28 (§1), Fri Oct 30 (§2–2.1, start of Example 1), Fri Nov 6 (Examples 1–3, §2.2, code demo), 2026 · "Fast Fourier transform" · prev: [[5-dft-and-fft/24-short-time-fourier-transform-and-spectrograms|Lecture 24]] · next: [[5-dft-and-fft/26-fast-convolution-via-the-dft|Lecture 26]] · first lecture after the Midterm 2 material*

> [!abstract] In one breath
> - The DFT sum costs $N^2$ multiply-adds; the FFT computes the same DFT in $N\log_2N$.
> - Split into even and odd samples, take two half-length DFTs, merge: $X[k]=A[k]+W_N^kB[k]$, $X[k+\frac N2]=A[k]-W_N^kB[k]$.
> - A butterfly diagram draws each pair of merging equations; reading branch weights from one is the homework skill.

> [!lecture] In lecture — L25, Oct 30 and Nov 6
> The lecture was split by Midterm 2: "it's a challenging concept, period, let alone if we talk about it and then we take a full week off because of an exam." After the recap: "The FFT is confusing … There are many other versions of the FFT. We're not going to show you them. We just want you to have a little bit of an understanding of just this specific version."

## What was covered

1. **§1 Directly computing the DFT:** multiply-adds, $O(N^2)$, big-O (eqs. 1–3, slide 3) → [[concepts/fast-fourier-transform|FFT]] §1
2. **§2 Fast Fourier transform:** $O(N\log N)$, twiddle factor (eqs. 4–5, slides 4–5) → [[concepts/fast-fourier-transform|FFT]] §2
3. **§2.1 Decimation-in-time FFT:** derivation and merging equations, summary of the algorithm (eqs. 6–25, slides 6–9) → [[concepts/fast-fourier-transform|FFT]] §3–4
4. **§2.2 Butterfly diagrams** (Figures 1–2, slides 12–13) → [[concepts/butterfly-diagram|butterfly diagram]] §1–2
5. **Cost per stage and the Python demo** (Nov 6) → [[concepts/fast-fourier-transform|FFT]] §5

## Exercises from this lecture

- Example 1 (slide 10), length-4 DFT → [[concepts/fast-fourier-transform|FFT]] §4
- Example 2 (slide 11) and notes Exercise 1 (eqs. 26–39), length-8 DFT → [[concepts/fast-fourier-transform|FFT]] §4
- Example 3 (slide 14), weights $a$–$e$ in a partial length-16 diagram → [[concepts/butterfly-diagram|butterfly diagram]] §3

**Practice:** [[homework/hw10|HW10]] #1 · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2 #10]]

## Related
[[5-dft-and-fft/index|Unit 5]] · [[concepts/dft|DFT]] · [[concepts/fast-convolution|fast convolution]] · [[concepts/index|Concepts]]

### Sources for this page
Snyder, Lecture 25 notes (§1–2.2, eqs. 1–39, Figures 1–2) and annotated slides 1–14, Oct 28 – Nov 6, 2026; lecture recordings Oct 28, Oct 30, Nov 6 and the makeup recording posted Nov 6 (condensed).
