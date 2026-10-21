---
title: "Unit 1 · Signals and systems"
description: "Lectures 1–5: sequences and complex numbers, the four system properties, impulse response and convolution, difference equations. Tested on Midterm 1."
tags: [midterm-1, signals, systems, convolution, lccde]
---

*Unit 1 · Lectures 1–5 · Midterm 1 · next: [[2-z-transform/index|Unit 2]]*

- Signals (L1–2), then four system properties (L3), then LTI systems: one $h[n]$, output by convolution (L4), run as difference equations (L5).

| # | page | one line |
|---|---|---|
| 1 | [[1-signals-and-systems/01-digital-signals\|Digital signals]] | $x[n] = x(nT)$; where $n = 0$ is; $x[an+b]$: shift first, then flip or compress |
| 2 | [[1-signals-and-systems/02-complex-numbers-and-elementary-signals\|Complex numbers and elementary signals]] | polar form, quadrant rule; Euler; roots of unity; geometric sums; $\delta$, $u$, sinusoids |
| 3 | [[1-signals-and-systems/03-system-properties\|System properties]] | linear, time-invariant, causal, stable: prove generally, disprove by counterexample |
| 4 | [[1-signals-and-systems/04-impulse-response-and-convolution\|Impulse response and convolution]] | $h = T(\delta)$; LTI ⇔ $y = x * h$; hand methods; $h$ from data |
| 5 | [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|Difference equations and block diagrams]] | LCCDE at rest = LTI; FIR vs IIR; recursion; L5 vs L9 signs; direct form I |

> [!key] The unit on one card
> - **Sequences:** $\delta[n] = u[n] - u[n-1]$; $x[n] = \sum_k x[k]\,\delta[n-k]$. For $x[an+b]$ shift by $b$, then flip or compress by $a$.
> - **Complex numbers:** $\lvert a+jb\rvert = \sqrt{a^2+b^2}$; phase needs $\pm\pi$ in the left half-plane; $e^{j\theta} = \cos\theta + j\sin\theta$, $\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}$, $\sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$; $z^N = c$ has $N$ roots spaced $2\pi/N$.
> - **Geometric sums:** $\sum_{k=0}^{N-1} a^k = \frac{1-a^N}{1-a}$, $\sum_{k=0}^{\infty} a^k = \frac{1}{1-a}$ for $\lvert a\rvert < 1$.
> - **Properties:** linear ⇔ superposition; time-invariant ⇔ $y[n-n_0] = T(x[n-n_0])$; causal ⇔ no future inputs; BIBO stable ⇔ bounded in, bounded out. All four independent.
> - **LTI:** $y[n] = \sum_k x[k]\,h[n-k]$; causal ⇔ $h[n] = 0$ for $n<0$; stable ⇔ $\sum_n\lvert h[n]\rvert < \infty$; cascade $h_1 * h_2$, parallel $h_1 + h_2$.
> - **Finite convolution:** start $= n_s + m_s$, end $= n_e + m_e$, length $N + M - 1$; check $\sum y = \sum x \cdot \sum h$.
> - **LCCDEs:** at rest LTI; no feedback ⇒ FIR (stable); $y[n] = a\,y[n-1] + x[n]$ has $h[n] = a^n u[n]$; L9/SciPy form flips feedback signs.

> [!exam] Exam
> Midterm 1 families fed by this unit (count of 7 past exams):
> [[problems/classifying-system-properties|property table]] 7 · [[problems/finite-length-convolution|finite convolution]] 7 · [[problems/infinite-length-convolution|infinite convolution]] 5 · [[problems/finding-h-from-input-output-pairs|finding h]] 7 · [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z)]] 7 · [[exams/midterm-1/true-false-bank|True/False]] 7 · also [[problems/two-sided-systems-as-recursions|two-sided recursions]]. Map: [[exams/midterm-1/past-exams/index|past exams]].

**Homework:** [[homework/hw1|HW1]] · [[homework/hw2|HW2]] · **Demos:** [[demos/convolution-explorer|convolution explorer]] · [[demos/difference-equation-simulator|difference-equation simulator]] · [[demos/practice-drills|drills]]

## Related
[[2-z-transform/index|Unit 2]] · [[concepts/convolution|convolution]] · [[concepts/lti-system|LTI system]] · [[concepts/lccde|LCCDE]] · [[0-toolkit/05-errata|errata]]

### Sources for this page
Snyder, ECE 310 Lectures 1–5 notes and slides (Fall 2026); past Midterm 1 exams FA2019–FA2025.
