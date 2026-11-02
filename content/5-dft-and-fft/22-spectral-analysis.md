---
title: "Lecture 22 — Spectral analysis with the DFT"
description: "DTFT and DFT of a finite-length cosine (periodic sinc); spectral leakage; the spectral analysis problem; zero padding for a denser view; the two challenges."
tags: [lecture, midterm-2, dft, spectral-analysis]
lecture: 22
---

*Lecture 22 · Wed Oct 21, Fri Oct 23, 2026 · "Spectral analysis with the DFT" · prev: [[5-dft-and-fft/21-dft-properties|Lecture 21]] · next: [[5-dft-and-fft/23-spectral-analysis-and-window-functions|Lecture 23]]*

> [!abstract] In one breath
> - Length-$N$ cosine: DTFT $\frac A2C(\omega\mp\omega_0)$, periodic-sinc lobes of height $N$, width $\frac{4\pi}{N}$.
> - DFT: two clean bins iff $\frac{\omega_0N}{2\pi}$ is an integer, else leakage.
> - Spectral analysis: find the sinusoids; padding refines the view; two challenges.

> [!lecture] In lecture — L22, Oct 21
> The first application: with the DFT and spectral analysis "we really start to take this theory" somewhere "with a very clear, practical implementation in mind." Part 1 defines the problem and the key challenge; part 2 (Oct 23–26) gives solutions and criteria; part 3 (optional) is not testable. Say the DFT *evaluates* the DTFT, not samples. On MT2: parts 1 and 2; "circular convolution will not be on midterm two."

## What was covered

1. **§1.1 DTFT of a finite-length sinusoid** (eqs. 1–10, Figure 1, slides 4–6) → [[concepts/periodic-sinc|periodic sinc]]
2. **§1.2 DFT of a finite-length sinusoid** (eqs. 11–14, Figure 2, slides 7–9; Oct 23) → [[concepts/spectral-leakage|spectral leakage]]
3. **§2 Spectral analysis** (eqs. 15–17, Figure 3, slide 11) → [[concepts/spectral-analysis|spectral analysis]] §1–2
4. **§2.1 Zero-padding** (slide 12) → [[concepts/zero-padding|zero padding]] §3
5. **§2.2 Challenges of separating frequency components** → [[concepts/spectral-analysis|spectral analysis]] §3

## Exercises from this lecture

- Example 1 (slide 6), read $\omega_0$, $N$, $A$ off a plot; exercise (rectangle pair + modulation) → [[concepts/periodic-sinc|periodic sinc]] §1–2
- Notes example (eqs. 13–14), $\cos(\frac\pi3n)$, $N=24$ vs $22$; Example 2 (slide 10), two/four nonzero bins? → [[concepts/spectral-leakage|spectral leakage]] §2
- Notes example (eq. 17), tones $0.55\pi$, $0.65\pi$, $N=32$, padded to $128$ → [[concepts/spectral-analysis|spectral analysis]] §2

**Practice:** HW9 #4–5 · [[problems/dft-spectral-analysis|DFT spectral analysis family]] · [[exams/midterm-2/true-false-bank|T/F bank]] §7

## Related
[[5-dft-and-fft/index|Unit 5]] · [[5-dft-and-fft/21-dft-properties|Lecture 21]] · [[5-dft-and-fft/23-spectral-analysis-and-window-functions|Lecture 23]] · [[concepts/index|Concepts]]

### Sources for this page
Snyder, Lecture 22 notes (§1–2.2, eqs. 1–17, Figures 1–3), slides (Examples 1–2), Oct 21–23, 2026; lecture recording Oct 21 (condensed).
