---
title: "Interactive demos"
description: "Small browser apps and Python snippets that go with the ECE 310 notes: convolution, difference equations, pole-zero plots with every ROC, and autograded drills."
tags: [demo]
---

- [[demos/convolution-explorer|Convolution explorer]]: flip, shift, multiply, add. It shows the overlap table, $y = Hx$ in matrix form, and where $n=0$ lands, with presets for every past-exam convolution.
- [[demos/difference-equation-simulator|Difference-equation simulator]]: runs a causal LCCDE sample by sample and draws its poles and zeros. It tells you whether the system is stable, marginally stable or unstable, and whether *this* input gives a bounded output.
- [[demos/pole-zero-and-roc-explorer|Pole-zero plot and every possible ROC]]: type $H(z)$ in powers of $z^{-1}$ and click through all of its ROCs to see causality, stability, the partial fractions and $h[n]$ for each one. Presets cover the homework and past-exam problems.
- [[demos/python-demos|Python demos]]: the course notebooks cut down to eight runnable numpy/scipy snippets, from `np.convolve` with index bookkeeping to `lfilter`, `residuez`, `tf2zpk` and a bounded input with an unbounded output.
- [[0-midterm-1/practice-drills|Practice drills]]: randomized, autograded Midterm 1 drills on convolution, system properties, and partial fractions with ROCs, with hints and worked solutions.

The demos show every answer, so they are best used for **checking** hand work. On the exam you have no calculator and must write answers in closed form.

### Sources for this page

The demo pages themselves; the course notebooks in `ece310-demos-main` (see [[supplements/demo-notebooks]]).
