---
title: "Lecture 23 — Spectral analysis and window functions"
description: "Full-lobe and half-lobe separation criteria (N > 4π/Δω, 2π/Δω); the guitar example; rectangular vs Hamming windows, lobe width vs side-lobe attenuation; windowing is not LTI."
tags: [lecture, midterm-2, dft, spectral-analysis]
lecture: 23
---

*Lecture 23 · Fri Oct 23 (§1), Mon Oct 26 (§2–3), demos Oct 28, 2026 · "Spectral analysis and window functions" · prev: [[5-dft-and-fft/22-spectral-analysis|Lecture 22]] · next: [[5-dft-and-fft/24-short-time-fourier-transform-and-spectrograms|Lecture 24]] (bonus, beyond Midterm 2) · last Midterm 2 lecture*

> [!abstract] In one breath
> - Two equal tones are resolved when their main lobes separate: $N\gt\frac{4\pi}{\Delta\omega}$ (full), $N\gt\frac{2\pi}{\Delta\omega}$ (half); padding does not help.
> - A finite signal is $x[n]w[n]$, so every component becomes a copy of the window's spectrum $W_d(\omega)$.
> - Rectangular: half-width $\frac{2\pi}{N}$, side lobes $-13$ dB; Hamming: $\frac{4\pi}{N}$, $-42$ dB. Narrow lobe or low side lobes, not both.

> [!lecture] In lecture — L23, Oct 26
> Two challenges, two tools. Close frequencies: more samples — after the guitar example, "challenge one of two, complete." Weak tones beside strong ones: ask where side lobes come from (the rectangular window we implicitly chose) and taper it; Hamming lowers them but doubles the lobe width, "we can't get one for free." MT2 (Oct 30): windows and criteria "to the extent they're used on homework."

## What was covered

1. **§1 Brief overview of the spectral analysis problem** (eqs. 1–4, Figure 1, slides 3–5) → [[concepts/spectral-analysis|spectral analysis]] · [[concepts/periodic-sinc|periodic sinc]]
2. **§2 Separating main lobes of components** (eqs. 5–15, Exercise 1, slides 6–8) → [[concepts/frequency-resolution|frequency resolution]]
3. **§3 Window functions** (eqs. 16–21, Figures 2–4, slides 9–12) → [[concepts/window-functions|window functions]] §1–4
4. **§3.1 Window function design tradeoff** (slide 13) → [[concepts/window-functions|window functions]] §5

## Exercises from this lecture

- Exercise 1 / Example 1 (slide 8), guitar E2/F2 at 8 kHz: samples and time for full-lobe separation; does $f_s$ matter → [[concepts/frequency-resolution|frequency resolution]] §2
- Notes example (eq. 16), $\cos(0.5\pi n)+\frac1{10}\cos(0.625\pi n)$, $N=64$, rectangular vs Hamming → [[concepts/window-functions|window functions]] §1, §4

**Practice:** [[problems/dft-spectral-analysis|DFT spectral analysis family]] · [[exams/midterm-2/true-false-bank|T/F bank]] §7

## Related
[[5-dft-and-fft/index|Unit 5]] · [[5-dft-and-fft/22-spectral-analysis|Lecture 22]] · [[concepts/index|Concepts]] · [[exams/midterm-2/index|Midterm 2]]

### Sources for this page
Snyder, Lecture 23 notes (§1–3.1, eqs. 1–21, Figures 1–4, Exercise 1), slides (Example 1), Oct 23–28, 2026; lecture recording Oct 26 (condensed); lecture recording Oct 30 (condensed).
