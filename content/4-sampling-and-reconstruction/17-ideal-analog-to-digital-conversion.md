---
title: "Lecture 17 — Ideal analog-to-digital conversion"
description: "Ideal sampling as an impulse train, the sampled spectrum X_s(Ω), ω = ΩT and X_d(ω), bandlimited signals and the Nyquist criterion; pointers to concept pages."
tags: [lecture, midterm-2, sampling, nyquist, ctft, dtft]
lecture: 17
---

*Lecture 17 · Fri Oct 9, 2026 · notes + slides "Ideal analog-to-digital conversion" · prev: [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] · next: [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Lecture 18]]*

> [!abstract] In one breath
> - Sampling = multiplying by an impulse train: the spectrum is copied every $2\pi/T$ rad/s, each copy scaled by $\frac1T$.
> - With $\omega=\Omega T$ the copies sit every $2\pi$: that is the DTFT $X_d(\omega)$.
> - Bandlimited to $B$ Hz: copies stay apart iff $f_s\gt2B$ (Nyquist). Below, they overlap: aliasing.

## What was covered

1. **§1 Ideal sampling of analog signals** (eqs. 1–11, Figure 1, Example 1) → [[concepts/sampling|Sampling]] §1–2
2. **§1.1 Converting to a discrete-time sequence** (eqs. 12–16, Figure 2) → [[concepts/sampling|Sampling]] §3
3. **§2 Nyquist criteria** (eqs. 17–21, Figure 3, Example 2) → [[concepts/nyquist-criterion|Nyquist criterion]] §1–2

## Exercises from this lecture

- Example 1 (slide 6), the box $\operatorname{rect}(\Omega/20\pi)$ sampled at $T=\frac{1}{20}$ and $\frac{1}{10}$ s → [[concepts/sampling|Sampling]] §2
- Slide 7, sampling $\cos(\Omega_0t)$ to read off $\omega=\Omega T$ → [[concepts/sampling|Sampling]] §3
- Example 2 (slides 10–12), the triangle to $100\pi$ rad/s at $150/100/75$ Hz → [[concepts/nyquist-criterion|Nyquist criterion]] §2

**Practice:** HW7 #3 ([[exams/quiz-2|Quiz 2 page]]) · [[problems/sampling-and-the-nyquist-rate|family]] · [[demos/sampling-explorer|explorer]]

## Related

[[4-sampling-and-reconstruction/index|Unit 4]] · prev [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] · next [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Lecture 18]] · [[concepts/index|Concepts]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-properties|DTFT properties]] (windowing)

### Sources for this page

Snyder, ECE 310 Lecture 17 notes (§1–2, eqs. 1–21, Figures 1–3) and slides of Oct 9, 2026 with the inked deck.
