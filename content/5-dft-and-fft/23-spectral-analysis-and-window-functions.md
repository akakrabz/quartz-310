---
title: "Lecture 23 — Spectral analysis and window functions"
description: "Full-lobe and half-lobe separation criteria (N > 4π/Δω, 2π/Δω); the guitar example; rectangular vs Hamming windows, lobe width vs side-lobe attenuation; windowing is not LTI."
tags: [lecture, midterm-2, dft, spectral-analysis]
lecture: 23
---

*Lecture 23 · Fri Oct 23, 2026 · notes + slides "Spectral analysis and window functions" · prev: [[5-dft-and-fft/22-spectral-analysis|Lecture 22]] · next: Lecture 24 (to come) · last Midterm 2 lecture*

> [!abstract] In one breath
> - Two equal tones are resolved when their main lobes separate: $N\gt\frac{4\pi}{\Delta\omega}$ (full), $N\gt\frac{2\pi}{\Delta\omega}$ (half); zero padding does not help.
> - A finite signal is $x[n]w[n]$, so every component becomes a copy of the window's spectrum $W_d(\omega)$.
> - Rectangular: half-width $\frac{2\pi}{N}$, side lobes $-13$ dB; Hamming: $\frac{4\pi}{N}$, $-42$ dB. Narrow lobe or low side lobes, not both.

## What was covered

1. **§1 Brief overview of the spectral analysis problem** (eqs. 1–4, Figure 1, slides 3–5) → [[concepts/spectral-analysis|spectral analysis]] · [[concepts/periodic-sinc|periodic sinc]]
2. **§2 Separating main lobes of components** (eqs. 5–15, Exercise 1, slides 6–8) → [[concepts/frequency-resolution|frequency resolution]]
3. **§3 Window functions** (eqs. 16–21, Figures 2–4, slides 9–12) → [[concepts/window-functions|window functions]] §1–4
4. **§3.1 Window function design tradeoff** (slide 13) → [[concepts/window-functions|window functions]] §5

## Exercises from this lecture

- Exercise 1 / Example 1 (slide 8), guitar E2/F2 at 8 kHz: samples and time for full-lobe separation; does $f_s$ change the time → [[concepts/frequency-resolution|frequency resolution]] §2
- Notes example (eq. 16), $\cos(0.5\pi n)+\frac1{10}\cos(0.625\pi n)$, $N=64$, rectangular vs Hamming → [[concepts/window-functions|window functions]] §1, §4

**Practice:** [[problems/dft-spectral-analysis|DFT spectral analysis family]] · [[exams/midterm-2/true-false-bank|T/F bank]] §7

## Related
[[5-dft-and-fft/index|Unit 5]] · [[5-dft-and-fft/22-spectral-analysis|Lecture 22]] · [[concepts/index|Concepts]] · [[exams/midterm-2/index|Midterm 2]]

### Sources for this page
Snyder, Lecture 23 notes (§1–3.1, eqs. 1–21, Figures 1–4, Exercise 1) and slides (Example 1), Oct 23, 2026.
