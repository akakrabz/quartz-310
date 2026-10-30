---
title: "Lecture 16 — Magnitude and phase response"
description: "Magnitude response |H_d(ω)| (never negative; linear or dB), phase as a principal angle, factoring out a linear phase, ±π jumps vs 2π wraps, group delay."
tags: [lecture, midterm-2, frequency-response, magnitude-response, phase-response, group-delay]
lecture: 16
---

*Lecture 16 · Mon Oct 5, 2026 (continued Wed Oct 7) · notes + slides "Magnitude and phase response" · prev: [[3-fourier-analysis/15-frequency-response|Lecture 15]] · next: [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]]*

> [!abstract] In one breath
> - $H_d=|H_d|e^{j\angle H_d}$: magnitude $\ge0$ (linear or dB), phase a principal angle in $[-\pi,\pi]$.
> - Symmetric FIR: pull out $e^{-jM\omega}$, leaving a real $A(\omega)$; its sign changes are $\pm\pi$ jumps.
> - Group delay $\tau_{gd}=-\frac{d\angle H_d}{d\omega}$: linear phase delays every frequency equally.

## What was covered

1. **§1 Complex numbers review** (eqs. 1–8, slide 3) → [[concepts/magnitude-and-phase-response|Magnitude and phase response]] §1, [[0-toolkit/01-complex-numbers|Complex numbers]]
2. **§2–2.1 Magnitude response** (eqs. 9–10, slide 4) → [[concepts/magnitude-and-phase-response|Magnitude and phase response]] §2
3. **§2.2 Phase response** (eqs. 11–12, Exercises 1–2 = eqs. 13–27, Figures 1–2, slides 4–9) → [[concepts/magnitude-and-phase-response|Magnitude and phase response]] §3–4
4. **§2.2.1 Group delay** (eqs. 28–30, Figure 3, slides 10–15) → [[concepts/group-delay|Group delay and linear phase]]

## Exercises from this lecture

- Examples 1–3 (slides 5, 7, 8–9; Exercises 1–2), $h=\{\underset{\uparrow}{1},0,1\}$, $\{\underset{\uparrow}{1},0,-1\}$, $\{\underset{\uparrow}{3},2,1\}$: $H_d$, $|H_d|$, $\angle H_d$ → [[concepts/magnitude-and-phase-response|Magnitude and phase response]] §3
- Slide 6 (concept check), which of five $H_k(\omega)$ have $\pm\pi$ jumps → §4
- Slides 10–11, what $e^{-jk\omega}$ does to $e^{j\omega_0n}$ · Exercises 1–2 revisited, image denoising (Figure 3, slides 13–15) → [[concepts/group-delay|Group delay]] §1–3

**Practice:** [[homework/hw6|HW6]] #3(b), #6–#7 · HW7 #1 ([[exams/quiz-2|Quiz 2 page]]) · [[problems/magnitude-phase-and-group-delay|family]] · [[demos/frequency-response-explorer|explorer]]

## Related

[[3-fourier-analysis/index|Unit 3]] · prev: [[3-fourier-analysis/15-frequency-response|Lecture 15]] · next: [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 16 notes (§1–2.2.1, Exercises 1–2, Figs. 1–3) and slides 1–15 (unannotated).
