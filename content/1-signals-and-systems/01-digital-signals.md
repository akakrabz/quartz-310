---
title: "Lecture 1 — Digital signals: sampling, sequences and index transformations"
description: "What a signal is; continuous- vs discrete-time, analog vs digital; sampling x[n] = x(nT); why process digitally; the n = 0 marker and index maps."
tags: [lecture, midterm-1, signals]
lecture: 1
---

*Lecture 1 · Mon Aug 24, 2026 · notes + slides "Introduction to digital signals" · next: [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]]*

> [!abstract] In one breath
> - Signal: a measurable quantity ordered by time, space or another variable.
> - Continuous-time $x(t)$, $t\in\mathbb{R}$; discrete-time $x[n]$, $n\in\mathbb{Z}$; sampling: $x[n] = x(nT)$.
> - Digital = discrete-time + quantized values; this course treats values as continuous.

## What was covered

1. **§1 What is a signal?** (Fig. 1: audio, financial, image, graph signals) → [[concepts/discrete-time-signal|Discrete-time signal]] §1
2. **§2 Continuous-time vs. discrete-time signals** (eq. 1, Fig. 2, the 44.1 kHz example; analog vs. digital) → [[concepts/discrete-time-signal|Discrete-time signal]] §2 · [[concepts/sampling|Sampling]]
3. **§3 Why use digital signals?** (four reasons) → [[concepts/discrete-time-signal|Discrete-time signal]] §3
4. **Beyond the notes: sequences and index maps** ($n = 0$ marker, $x[an+b]$) → [[concepts/discrete-time-signal|Discrete-time signal]] §4–5

## Exercises from this lecture

- No worked examples in the notes; Fig. 2, the sampled cosine $x[n] = \cos(\pi n/8)$ → [[concepts/discrete-time-signal|Discrete-time signal]] §2
- HW1 #2, $x[-n+3]$ and $x[2n+1]$ → [[concepts/discrete-time-signal|Discrete-time signal]] §5 · [[0-toolkit/03-sketching-and-transforming-signals|sketching signals]]

**Practice:** [[homework/hw1|HW1]] #1–#3 · [[problems/finite-length-convolution|finite-length convolution]] (the arrow) · [[problems/classifying-system-properties|classifying system properties]] (index maps)

## Related

[[1-signals-and-systems/index|Unit 1]] · next: [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 1 notes (§1–3, Figs. 1–2) and slides, Aug 24, 2026; HW1 #1–#3.
