---
title: "Unit 1 · Signals and systems"
description: "Lectures 1–5: sequences and complex numbers, the four system properties, impulse response and convolution, and difference equations. The time-domain half of Midterm 1."
tags: [midterm-1, signals, systems, convolution, lccde]
---

Signals first, then systems, then the one class of systems the course cares about. Lectures 1–2 set up the language: sequences indexed by integers, the $n = 0$ marker, $\delta[n]$ and $u[n]$, complex numbers and Euler's formula. Lecture 3 asks four yes/no questions about any system (linear? time-invariant? causal? stable?). Lecture 4 shows that the systems passing the first two tests, the LTI systems, are completely described by one sequence $h[n]$ and act by convolution. Lecture 5 gives the practical description of those systems, the difference equation, which is how filters actually run. Unit 2 ([[2-z-transform/index|the z-transform]]) then redoes all of this with algebra instead of sums.

| # | page | one line |
|---|---|---|
| 1 | [[1-signals-and-systems/01-digital-signals\|Digital signals: sampling, sequences and index transformations]] | $x[n] = x(nT)$; analog vs digital; where $n = 0$ is; $x[an+b]$: shift first, then flip or compress (HW1 #2) |
| 2 | [[1-signals-and-systems/02-complex-numbers-and-elementary-signals\|Complex numbers and elementary signals]] | rectangular ↔ polar with the quadrant rule; Euler's identities; roots of unity; geometric sums; $\delta$, $u$, sinusoids, $Ba^n$ |
| 3 | [[1-signals-and-systems/03-system-properties\|Discrete-time systems: linearity, time-invariance, causality, stability]] | prove with a general argument, disprove with one counterexample; the property table in 30 seconds |
| 4 | [[1-signals-and-systems/04-impulse-response-and-convolution\|Impulse response and convolution]] | $h = T(\delta)$; LTI ⇔ $y = x * h$; flip-shift-multiply-add; table, matrix, sum and δ-split methods; finding $h$ from data |
| 5 | [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|Difference equations and block diagrams]] | LCCDE at rest = LTI; FIR vs IIR; running the recursion in real time; Lecture 5 vs Lecture 9 signs; direct form I |

## Key results of the unit

- **Sequences:** $\delta[n-k]$ and the edge of $u[n-k]$ sit where the argument is zero; $\delta[n] = u[n] - u[n-1]$; $x[n] = \sum_k x[k]\,\delta[n-k]$.
- **Index maps:** for $x[an+b]$ shift by $b$ first, then flip or compress by $a$ (or evaluate the index sample by sample).
- **Complex numbers:** $\lvert a+jb\rvert = \sqrt{a^2+b^2}$; the phase needs $\pm\pi$ in the left half-plane; $e^{j\theta} = \cos\theta + j\sin\theta$, $\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}$, $\sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$; $z^N = c$ has $N$ roots spaced $2\pi/N$ apart.
- **Geometric sums:** $\sum_{k=0}^{N-1} a^k = \frac{1-a^N}{1-a}$, $\sum_{k=0}^{\infty} a^k = \frac{1}{1-a}$ for $\lvert a\rvert < 1$.
- **System properties:** linear ⇔ superposition; time-invariant ⇔ $y[n-n_0] = T(x[n-n_0])$; causal ⇔ no future inputs; BIBO stable ⇔ bounded in gives bounded out. The four are independent of each other.
- **LTI systems:** $y[n] = x[n] * h[n] = \sum_k x[k]\,h[n-k]$; causal ⇔ $h[n] = 0$ for $n<0$; stable ⇔ $\sum_n\lvert h[n]\rvert < \infty$; cascade $h_1 * h_2$ (order irrelevant), parallel $h_1 + h_2$.
- **Finite convolution:** start $= n_s + m_s$, end $= n_e + m_e$, length $N + M - 1$; sum check $\sum y = \sum x \cdot \sum h$.
- **LCCDEs:** at rest they are LTI; no feedback ⇒ FIR (always stable), feedback ⇒ usually IIR; $y[n] = a\,y[n-1] + x[n]$ has $h[n] = a^n u[n]$. In the Lecture 9 / SciPy form the feedback coefficients change sign.

## Exam problem families this unit feeds

| family | past exams | lectures |
|---|---|---|
| [[problems/classifying-system-properties\|System-property table]] (12 points) | 7 of 7 | L3 (+ L4 for convolution rows) |
| [[problems/finite-length-convolution\|Finite-length convolution]] | 7 of 7 | L4 (+ L1 for the index) |
| [[problems/infinite-length-convolution\|Infinite or mixed convolution]] | 5 of 7 | L4 (+ L2 geometric sums) |
| [[problems/finding-h-from-input-output-pairs\|Finding $h$ from input–output pairs]] | 7 of 7 | L4 (+ L9 on later exams) |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ $H(z)$ ↔ response]] | 7 of 7 | L5 → L9 |
| [[0-midterm-1/true-false-bank\|True/False]] | 7 of 7 | L3 and L4 supply about half of the statements |

Also from this unit: the complex-number fluency behind every z-transform problem ([[problems/z-transform-with-roc]], [[problems/unbounded-outputs-and-pole-matching]]) and the recursions of [[problems/two-sided-systems-as-recursions]]. The full map of past problems is in [[0-midterm-1/past-exams/index|past exams]]; the homework for this unit is [[homework/hw1|HW1]] and [[homework/hw2|HW2]].

**Try it:** [[demos/convolution-explorer|convolution explorer]] · [[demos/difference-equation-simulator|difference-equation simulator]] · [[0-midterm-1/practice-drills|practice drills]]

Every worked example and number in this unit is checked by the scripts in `verify/lectures/` (`l1_signals.py` … `l5_lccde.py`) against NumPy/SciPy and the official keys; where a key is wrong (SP2021 #6, SP2025 #4(a)) the pages say so and [[0-toolkit/05-errata|errata]] lists it.
