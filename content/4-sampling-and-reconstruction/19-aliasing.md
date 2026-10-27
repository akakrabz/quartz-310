---
title: "Lecture 19 — The aliasing effect"
description: "Nyquist criterion from ω = ΩT, aliasing defined, sampling exactly at the Nyquist rate, sin(100πt) at four rates, the folding recipe; pointers to concept pages."
tags: [lecture, midterm-2, sampling, aliasing, nyquist, dtft]
lecture: 19
---

*Lecture 19 · Wed Oct 14, 2026 · notes + slides "Aliasing effect" · prev: [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Lecture 18]] · next: [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]]*

> [!abstract] In one breath
> - Sampling maps $\Omega$ to $\omega=\Omega T$; nothing is lost if the band edge lands inside $(-\pi,\pi)$: $f_s\gt2B$.
> - Below the Nyquist rate the copies overlap: **aliasing**. The ideal D/A returns a different signal, for good.
> - A sinusoid comes back at its principal alias $\hat\omega\in(-\pi,\pi]$, i.e. at $\hat\Omega=\hat\omega/T$.

## What was covered

1. **§1 Nyquist criterion** (eqs. 1–5, Figure 1) → [[concepts/nyquist-criterion|Nyquist criterion]] §3
2. **§2 Aliasing effect** (above, at and below the rate; the definition) → [[concepts/aliasing|Aliasing]] §1 · at exactly $2B$ → [[concepts/nyquist-criterion|Nyquist criterion]] §4
3. **§2.1 Aliasing of sinusoidal signals** (eqs. 6–17, Figures 2–3) → [[concepts/aliasing|Aliasing]] §2–4

## Exercises from this lecture

- Slide 7, $\sin(\Omega_0t)$ sampled exactly at the Nyquist rate (eqs. 9–11) → [[concepts/nyquist-criterion|Nyquist criterion]] §4
- Slides 9–13, $\sin(100\pi t)$ at $160$, $120$, $80$, $40$ Hz (eqs. 12–17): $\omega_k$, alias, $x_k[n]$, $\hat\Omega_k$ → [[concepts/aliasing|Aliasing]] §3
- Slide 19, two $\Omega_0$ that give $\cos\!\left(\frac{\pi}{3}n\right)$ at $f_s=100$ Hz → [[concepts/aliasing|Aliasing]] §4

**Practice:** HW7 #4 ([[exams/quiz-2|Quiz 2 page]]) · [[problems/sampling-and-the-nyquist-rate|family]] · [[problems/digital-filtering-of-analog-signals|allowed aliasing]] · [[demos/sampling-explorer|explorer]]

## Related

[[4-sampling-and-reconstruction/index|Unit 4]] · prev [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Lecture 18]] · next [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]] · [[concepts/index|Concepts]] · [[concepts/sampling|sampling]] · [[concepts/ideal-reconstruction|ideal reconstruction]] · [[concepts/dtft-pairs|DTFT pairs]]

### Sources for this page

Snyder, Lecture 19 notes (§1–§2.1, eqs. 1–17, Figures 1–3) and slides of Oct 14, 2026 (slides 3–19, slide 7 inked).
