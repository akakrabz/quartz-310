---
title: "Unit 1 · Signals and systems"
description: "Topics of Lectures 1–5: sequences and complex numbers, the four system properties, impulse response and convolution, difference equations. Tested on Midterm 1."
tags: [midterm-1, signals, systems, convolution, lccde]
---

*Unit 1 · Lectures 1–5 · Midterm 1 · next: [[2-z-transform/index|Unit 2]]*

- Signals (L1–2), four system properties (L3), LTI systems: one $h[n]$, output by convolution (L4), run as difference equations (L5).

## Topics

**Signals**
- [[concepts/discrete-time-signal|Discrete-time signal]] — $x[n]=x(nT)$; mark $n=0$; $x[an+b]$: shift, then flip or compress.
- [[concepts/kronecker-delta|Kronecker delta]] — sifting; signals as shifted deltas.
- [[concepts/unit-step|Unit step]] — window $u[n]-u[n-N]$; $\delta[n]=u[n]-u[n-1]$.
- [[concepts/complex-exponential|Complex exponential]] — polar form, Euler, roots of unity.
- [[concepts/sided-sequences|Sided sequences]] — right-, left-, two-sided.

**System properties**
- [[concepts/linearity|Linearity]] — superposition; disprove by counterexample.
- [[concepts/time-invariance|Time-invariance]] — shift in, same shift out.
- [[concepts/causality|Causality]] — no future inputs; LTI: $h[n]=0$, $n<0$.
- [[concepts/lti-system|LTI system]] — $y=x*h$.

**LTI toolkit**
- [[concepts/impulse-response|Impulse response]] — $h=T(\delta)$ from formula, LCCDE or data.
- [[concepts/step-response|Step response]] — $g=h*u$; $h[n]=g[n]-g[n-1]$.
- [[concepts/convolution|Convolution]] — hand methods; start, end, length.
- [[concepts/lccde|Difference equation (LCCDE)]] — at rest = LTI; L5 vs L9 signs.
- [[concepts/fir-and-iir|FIR and IIR]] — FIR always stable.
- [[concepts/block-diagram|Block diagram]] — delays, gains, adders.
- [[concepts/eigenfunctions-of-lti-systems|Eigenfunctions]] — $z^n\mapsto H(z)z^n$.

## Lectures
1. [[1-signals-and-systems/01-digital-signals|Digital signals]] (Aug 24)
2. [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Complex numbers and elementary signals]] (Aug 26)
3. [[1-signals-and-systems/03-system-properties|System properties]] (Aug 28)
4. [[1-signals-and-systems/04-impulse-response-and-convolution|Impulse response and convolution]] (Aug 31)
5. [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Difference equations and block diagrams]] (Sep 2)

> [!key] The unit on one card
> - **Sequences:** $\delta[n] = u[n] - u[n-1]$; $x[n] = \sum_k x[k]\,\delta[n-k]$. $x[an+b]$: shift by $b$, then flip or compress by $a$.
> - **Complex numbers:** $\lvert a+jb\rvert = \sqrt{a^2+b^2}$; phase: $\pm\pi$ in the left half-plane; $e^{j\theta} = \cos\theta + j\sin\theta$, $\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}$, $\sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$; $z^N = c$ has $N$ roots spaced $2\pi/N$.
> - **Geometric sums:** $\sum_{k=0}^{N-1} a^k = \frac{1-a^N}{1-a}$, $\sum_{k=0}^{\infty} a^k = \frac{1}{1-a}$ ($\lvert a\rvert < 1$).
> - **Properties:** linear ⇔ superposition; time-invariant ⇔ $y[n-n_0] = T(x[n-n_0])$; causal ⇔ no future inputs; BIBO stable ⇔ bounded in, bounded out; all four independent.
> - **LTI:** $y[n] = \sum_k x[k]\,h[n-k]$; causal ⇔ $h[n] = 0$ for $n<0$; stable ⇔ $\sum_n\lvert h[n]\rvert < \infty$; cascade $h_1 * h_2$, parallel $h_1 + h_2$.
> - **Finite convolution:** start $= n_s + m_s$, end $= n_e + m_e$, length $N + M - 1$; $\sum y = \sum x \cdot \sum h$.
> - **LCCDEs:** at rest LTI; no feedback ⇒ FIR; $y[n] = a\,y[n-1] + x[n]$ has $h[n] = a^n u[n]$; L9/SciPy form flips the feedback signs.

> [!exam] Exam
> Midterm 1 families (count of 7 past exams): [[problems/classifying-system-properties|property table]] 7 · [[problems/finite-length-convolution|finite convolution]] 7 · [[problems/infinite-length-convolution|infinite convolution]] 5 · [[problems/finding-h-from-input-output-pairs|finding h]] 7 · [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z)]] 7 · [[exams/midterm-1/true-false-bank|True/False]] 7 · [[problems/two-sided-systems-as-recursions|two-sided recursions]] 2. Map: [[exams/midterm-1/past-exams/index|past exams]].

**Homework:** [[homework/hw1|HW1]] · [[homework/hw2|HW2]] · **Demos:** [[demos/convolution-explorer|convolution]] · [[demos/difference-equation-simulator|LCCDE simulator]] · [[demos/practice-drills|drills]]

## Related
[[2-z-transform/index|Unit 2]] · [[concepts/index|Concepts]] · [[0-toolkit/05-errata|errata]]

### Sources for this page
Snyder, ECE 310 Lectures 1–5 notes and slides (Fall 2026); past Midterm 1 exams.
