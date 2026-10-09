---
title: "Interactive demos"
description: "Small browser apps and Python snippets that go with the ECE 310 notes: convolution, difference equations, pole-zero plots with every ROC, frequency response with magnitude, phase and group delay, and autograded drills."
tags: [demo]
---

- [[demos/convolution-explorer|Convolution explorer]]: flip, shift, multiply, add. It shows the overlap table, $y = Hx$ in matrix form, and where $n=0$ lands, with presets for every past-exam convolution.
- [[demos/difference-equation-simulator|Difference-equation simulator]]: runs a causal LCCDE sample by sample and draws its poles and zeros. It tells you whether the system is stable, marginally stable or unstable, and whether *this* input gives a bounded output.
- [[demos/pole-zero-and-roc-explorer|Pole-zero plot and every possible ROC]]: type $H(z)$ in powers of $z^{-1}$ and click through all of its ROCs to see causality, stability, the partial fractions and $h[n]$ for each one. Presets cover the homework and past-exam problems.
- [[demos/frequency-response-explorer|Frequency-response explorer]]: type FIR taps or a difference equation, or drag poles and zeros, and see $\lvert H_d(\omega)\rvert$ (linear or dB), the phase with its $\pm\pi$ jumps (principal or unwrapped) and the group delay. A cursor at $\omega_0$ shows what $\cos(\omega_0 n + \theta)$ turns into, with the convolution sum as a check. Presets cover the Lecture 16 examples, moving averages, first-order and pole-zero filters, and three Midterm 2 problems.
- [[demos/python-demos|Python demos]]: the course notebooks cut down to eight runnable numpy/scipy snippets, from `np.convolve` with index bookkeeping to `lfilter`, `residuez`, `tf2zpk` and a bounded input with an unbounded output.
- [[demos/practice-drills|Practice drills]]: ten randomized, autograded drills with hints and worked solutions. Units 1–2: convolution, system properties, partial fractions with ROCs, stability, unbounded outputs, True/False. Unit 3: DTFT values, the response to sinusoids, and magnitude, phase and group delay of linear-phase filters.

The demos show every answer, so they work best for **checking** hand work and for building intuition: change one number and watch what moves. Do the problem on paper first. That is also the skill the exams test, where there is no calculator and answers are written in closed form.

### Sources for this page

The demo pages themselves; the course notebooks in `ece310-demos-main` (see [[supplements/demo-notebooks]]).
