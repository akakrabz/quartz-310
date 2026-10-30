---
title: "Lecture 13 — Fourier analysis and the DTFT"
description: "Periodic signals and discrete-time frequency, CTFS, CTFT, DTFS, and the DTFT X_d(ω) = Σ x[n]e^{−jωn}: definition, inverse, existence, 2π-periodicity."
tags: [lecture, midterm-2, dtft, fourier-series, fourier-analysis]
lecture: 13
---

*Lecture 13 · Wed Sep 23, 2026 · notes + slides "Fourier analysis" · prev: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] · next: [[3-fourier-analysis/14-dtft-properties|Lecture 14]]*

> [!abstract] In one breath
> - Orthogonal harmonics give the Fourier-series weights; $T_0\to\infty$ gives the Fourier transform.
> - Discrete time: frequencies $2\pi$ apart coincide, so $N_0$ harmonics suffice (DTFS) and every DTFT is $2\pi$-periodic.
> - DTFT $X_d(\omega)=\sum_nx[n]e^{-j\omega n}$, exists if $\sum_n|x[n]|<\infty$ (CTFS, DTFS: starred, not on exams).

## What was covered

1. **§1.1 Continuous-time signals** (eqs. 1–11, slides 3, 7) → [[concepts/periodic-signals|Periodic signals]] §1
2. **§1.2 Discrete-time signals** (eqs. 12–18, slides 4–6) → [[concepts/periodic-signals|Periodic signals]] §2
3. **§2 Continuous-time Fourier series** (eqs. 19–25, Figure 1, slides 8–10) → [[concepts/fourier-series|Fourier series]] §1
4. **§2.1 Continuous-time Fourier transform** (eqs. 26–28, slides 11–12) → [[concepts/fourier-series|Fourier series]] §2
5. **§3 Discrete-time Fourier series** (eqs. 29–40, Exercise 1, slide 13) → [[concepts/fourier-series|Fourier series]] §3
6. **§4 Discrete-time Fourier transform** (eqs. 41–49, Exercise 2, Figure 2, slides 14–16) → [[concepts/dtft|DTFT]] §1–2

## Exercises from this lecture

- Slide 6, which signals equal $\sin(\frac{\pi}{3}n)$ → [[concepts/periodic-signals|Periodic signals]] §2
- Figure 1 / slide 10, sawtooth $x(t)=t$ → [[concepts/fourier-series|Fourier series]] §1 · Exercise 1, DTFS of the periodic pulse → §3
- Exercise 2 / Figure 2, DTFT of the pulse → [[concepts/dtft|DTFT]] §2 · slides 15–16, $\{\underset{\uparrow}{1},0,1,0,1\}$ and the sequence behind $2j\sin\omega$ → §4

**Practice:** [[homework/hw5|HW5]] #1–#2 · [[homework/hw6|HW6]] #1, #3 · [[problems/dtft-and-inverse-dtft|family]] · [[exams/quiz-2|Quiz 2]]

## Related

[[3-fourier-analysis/index|Unit 3]] · prev: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] · next: [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 13 notes (§§1–4, Exercises 1–2, Figs. 1–2) and slides (annotated 5, 6, 15, 16).
