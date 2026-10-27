---
title: "Lecture 2 — Complex numbers and elementary signals"
description: "Rectangular and polar form, magnitude and phase (quadrant rule), principal angle, Euler; the n = 0 marker, Kronecker delta, unit step, sinusoids, exponentials."
tags: [lecture, midterm-1, complex-numbers, signals]
lecture: 2
---

*Lecture 2 · Wed Aug 26, 2026 · notes + slides "Math preliminaries, complex numbers" · prev: [[1-signals-and-systems/01-digital-signals|Lecture 1]] · next: [[1-signals-and-systems/03-system-properties|Lecture 3]]*

> [!abstract] In one breath
> - $x = a + jb = Re^{j\theta}$: add in rectangular form, multiply and divide in polar; Euler converts.
> - Phase needs the quadrant rule; angles repeat every $2\pi$.
> - Building blocks: $\delta[n]$, $u[n]$, $A\sin(\omega_0 n + \theta)$, $Ba^n$.

## What was covered

1. **§1 Complex numbers**: §1.1 rectangular form (eqs. 1–5, Fig. 1), §1.2 polar form (eqs. 6–10), §1.3 magnitude and phase (eqs. 11–13: quadrant rule, principal angle), §1.4 Euler's identities (eqs. 14–20) → [[concepts/complex-exponential|Complex exponential]] §1
2. **§2 Common discrete-time signal representations** ($n = 0$ marker; eqs. 21–24, Fig. 2) → [[concepts/discrete-time-signal|Discrete-time signal]] §4 · [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/unit-step|Unit step]] · [[concepts/complex-exponential|Complex exponential]] §2

## Exercises from this lecture

- Eqs. 3–5, $(1+j2)/(3-j)$; slides 7–8, $\lvert x\rvert$ and $\angle x$ of $-4 + j3$, $j2$, $-3.10$; slide 12, $j2 + \sqrt2\,e^{-j\pi/4}$ and $j3/(1-j)$ → [[concepts/complex-exponential|Complex exponential]] §1
- Slide 13, reading $x[-1]$, $x[0]$, $x[5]$ off a marked sequence → [[concepts/discrete-time-signal|Discrete-time signal]] §4
- Slides 14–15, sketch $-2\delta[n+3]$ and $u[3-n]$; $\{2, 0, \underset{\uparrow}{3}, -1, -4\}$ in deltas → [[concepts/kronecker-delta|Kronecker delta]] §2 · [[concepts/unit-step|Unit step]] §1
- HW1 #4, roots of $z^4 = \pm1$ → [[0-toolkit/01-complex-numbers|toolkit]] · [[concepts/complex-exponential|Complex exponential]] §1

**Practice:** [[homework/hw1|HW1]] #1, #3, #4 · [[problems/z-transform-with-roc|z-transform with ROC]] · [[problems/unbounded-outputs-and-pole-matching|pole matching]]

## Related

[[1-signals-and-systems/index|Unit 1]] · prev: [[1-signals-and-systems/01-digital-signals|Lecture 1]] · next: [[1-signals-and-systems/03-system-properties|Lecture 3]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 2 notes (§1.1–1.4, §2, Figs. 1–2) and annotated slides, Aug 26, 2026; HW1 #1, #3–4.
