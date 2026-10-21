---
title: "Interactive demos"
description: "Browser apps and Python snippets for the ECE 310 notes: convolution, difference equations, pole-zero plots with every ROC, frequency response, sampling, autograded drills."
tags: [demo]
---

*Demos · do the problem on paper first, then check it here*

- [[demos/convolution-explorer|Convolution explorer]]: flip, shift, multiply, add; overlap table, $y = Hx$, where $n=0$ lands; past-exam presets.
- [[demos/difference-equation-simulator|Difference-equation simulator]]: runs a causal LCCDE; poles, zeros; stable, marginal or unstable; bounded output for this input?
- [[demos/pole-zero-and-roc-explorer|Pole-zero plot and every possible ROC]]: $H(z)$ in powers of $z^{-1}$; each ROC with causality, stability, partial fractions, $h[n]$.
- [[demos/frequency-response-explorer|Frequency-response explorer]]: taps, LCCDE or dragged poles and zeros; $\lvert H_d(\omega)\rvert$ (linear/dB), phase, group delay; output for $\cos(\omega_0 n + \theta)$; Lecture 16 and Midterm 2 presets.
- [[demos/sampling-explorer|Sampling explorer]]: slide the sampling rate across Nyquist; copies of $X_s(\Omega)$ and $X_d(\omega)$ separate, touch, overlap; Lecture 17 and past-exam presets.
- [[demos/python-demos|Python demos]]: four numpy/scipy snippets from the course notebooks (`np.convolve`, `lfilter`, `residuez`, a bounded input with unbounded output).
- [[demos/practice-drills|Practice drills]]: ten randomized, autograded drills with hints. Units 1–2: convolution, properties, PFE with ROCs, stability, unbounded outputs, T/F. Unit 3: DTFT values, sinusoid response, magnitude/phase/group delay.

### Sources for this page
The demo pages; course notebooks `ece310-demos-main` ([[supplements/demo-notebooks|demo notebooks]]).
