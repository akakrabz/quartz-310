---
title: "Lecture 18 — Ideal digital-to-analog conversion"
description: "Reconstruction formula as a convolution, ideal low-pass G_a, sinc interpolation, the slide-9 sketch, the A/D → H_d → D/A semicircle example; pointers to concept pages."
tags: [lecture, midterm-2, sampling, reconstruction, sinc, ctft, dtft]
lecture: 18
---

*Lecture 18 · Mon Oct 12, 2026 · notes + slides "Ideal digital-to-analog conversion" · prev: [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · next: [[4-sampling-and-reconstruction/19-aliasing|Lecture 19]]*

> [!abstract] In one breath
> - D/A: place $x[n]$ at $t=nT$ and interpolate, $x_a(t)=\sum_nx[n]\,g(t-nT)=x_s(t)*g(t)$.
> - Ideal $g$: low-pass $G_a=T$ on $|\Omega|\le\frac{\pi}{T}$, so $g(t)=\mathrm{sinc}\!\left(\frac{\pi t}{T}\right)$. Keeps the central copy, undoes the $\frac1T$.
> - With a digital filter between the converters, $Y_a(\Omega)=T\,Y_d(\Omega T)$ on $|\Omega|\lt\frac{\pi}{T}$: one analog filter with cutoff $\omega_c/T$.

## What was covered

1. **§1 Ideal reconstruction of bandlimited signals** (eqs. 1–14, Figures 1–3; slides 4–8) → [[concepts/ideal-reconstruction|Ideal reconstruction]] §1–3
2. **Sketching ideal D/A conversion** (slide 9) → [[concepts/ideal-reconstruction|Ideal reconstruction]] §4
3. **Overall sampling system example** (slides 10–11) → [[concepts/digital-processing-of-analog-signals|Digital processing of analog signals]]

## Exercises from this lecture

- Slide 9, $x[n]=3\delta[n-1]+\delta[n-4]$ through an ideal D/A with $T=2$ s → [[concepts/ideal-reconstruction|Ideal reconstruction]] §4
- Slide 10, the semicircle to $60\pi$ rad/s through a low-pass with $\omega_c=\frac{\pi}{2}$ at $T=\frac{1}{80}$ s: $X_d$, $Y_d$, $Y_a$ → [[concepts/digital-processing-of-analog-signals|Digital processing of analog signals]] §2
- Slide 11, the same at $T=\frac{1}{50}$ s (aliasing outside the passband) → [[concepts/digital-processing-of-analog-signals|Digital processing of analog signals]] §2–3

**Practice:** HW7 #4 ([[exams/quiz-2|Quiz 2 page]]) · [[problems/digital-filtering-of-analog-signals|family]] · [[demos/sampling-explorer|explorer]]

## Related

[[4-sampling-and-reconstruction/index|Unit 4]] · prev [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · next [[4-sampling-and-reconstruction/19-aliasing|Lecture 19]] · [[concepts/index|Concepts]] · [[concepts/convolution|convolution]] · [[concepts/frequency-response|frequency response]]

### Sources for this page

Snyder, ECE 310 Lecture 18 notes (§1, eqs. 1–14, Figures 1–3) and slides of Oct 12, 2026 with the inked deck (slides 4–11).
