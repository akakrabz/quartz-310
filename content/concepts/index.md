---
title: "Concepts"
description: "The glossary of ECE 310 Midterm 1: one short page per idea (definition, how to test or compute it, the traps exams punish, and links to every lecture, homework and past-exam problem that uses it)."
tags: [concept]
---

Lectures tell the story in order; **concept pages** are the glossary you consult out of order. Each one is short and self-contained: the definition, how to test or compute it, the mistakes that cost points, and links back to the lectures that develop it and the exam problems that test it. Open the graph view (top right of any page) to see how they connect. All 28 pages are in scope for Midterm 1 (Lectures 1–11).

### Signals
- [[concepts/discrete-time-signal|Discrete-time signal]]: a sequence $x[n]$, $n\in\mathbb{Z}$; always mark $n=0$; shifting, flipping and decimating the index.
- [[concepts/kronecker-delta|Kronecker delta]] $\delta[n]$: the unit impulse; sifting, and every signal as a sum of shifted deltas.
- [[concepts/unit-step|Unit step]] $u[n]$: steps, windows $u[n]-u[n-N]$, and $\delta[n]=u[n]-u[n-1]$.
- [[concepts/complex-exponential|Complex exponential]]: $a^n=r^ne^{j\omega n}$; Euler's identities, principal angle, growth vs. decay.
- [[concepts/sided-sequences|Sided sequences]]: right-, left- and two-sided; causal vs. anti-causal; the ROC shape each one forces.

### System properties
- [[concepts/linearity|Linearity]]: superposition; the zero-in/zero-out test; what makes a system nonlinear.
- [[concepts/time-invariance|Time-invariance]]: shift in, same shift out; how to test index maps like $x[2n]$ and $x[\lvert n\rvert]$.
- [[concepts/causality|Causality]]: the output never uses a future input; for LTI, $h[n]=0$ for $n<0$.
- [[concepts/lti-system|LTI system]]: linear + time-invariant $\Rightarrow$ $y=x*h$; one sequence describes the whole system.

### LTI toolkit
- [[concepts/impulse-response|Impulse response]]: $h[n]=T\{\delta[n]\}$; how to get it from a formula, an LCCDE, or an input–output pair.
- [[concepts/step-response|Step response]]: $g[n]=h[n]*u[n]$, the running sum of $h$; $h[n]=g[n]-g[n-1]$.
- [[concepts/convolution|Convolution]]: the sum, its properties, start/end/length rules, three hand methods, `np.convolve`.
- [[concepts/lccde|Difference equation (LCCDE)]]: the two sign conventions, recursion at initial rest, `lfilter`.
- [[concepts/fir-and-iir|FIR and IIR]]: finite vs. infinite impulse response; FIR is always stable; feedback does not always mean IIR.
- [[concepts/block-diagram|Block diagram]]: delays, gains, adders; direct form I; reading an LCCDE off a diagram.
- [[concepts/eigenfunctions-of-lti-systems|Eigenfunctions of LTI systems]]: $z^n$ in, $H(z)z^n$ out; the reason the z-transform exists.

### z-domain
- [[concepts/z-transform|z-transform]]: $X(z)=\sum_n x[n]z^{-n}$, never without its ROC.
- [[concepts/region-of-convergence|Region of convergence]]: rings bounded by poles; what the ROC says about sidedness, causality and stability.
- [[concepts/poles-and-zeros|Poles and zeros]]: roots of the denominator and numerator; the pole-zero plot.
- [[concepts/z-transform-pairs|z-transform pairs]]: the pairs to know by heart ($\delta[n]$, $a^nu[n]$, $-a^nu[-n-1]$, $na^nu[n]$, cosine and sine).
- [[concepts/z-transform-properties|z-transform properties]]: linearity, shift, multiplication by $a^n$ or $n$, time reversal, convolution.
- [[concepts/inverse-z-transform|Inverse z-transform]]: inspection and partial fractions; the ROC decides which sequence you get.
- [[concepts/partial-fraction-expansion|Partial fraction expansion]]: $A_k/(1-p_kz^{-1})$ terms by cover-up; long division first if $H(z)$ is improper.
- [[concepts/transfer-function|Transfer function]]: $H(z)=Y(z)/X(z)=\mathcal{Z}\{h[n]\}$, read off an LCCDE by inspection.
- [[concepts/system-algebra|System algebra]]: series multiplies ($H_1H_2$, $h_1*h_2$), parallel adds ($H_1+H_2$, $h_1+h_2$).

### Stability
- [[concepts/bibo-stability|BIBO stability]]: three equivalent tests (definition, $\sum\lvert h[n]\rvert<\infty$, ROC contains the unit circle) and the classic T/F traps.
- [[concepts/pole-zero-cancellation|Pole-zero cancellation]]: a zero on top of a pole removes it; inputs that tame unstable systems, cascades that become stable.
- [[concepts/marginal-stability|Marginal stability]]: poles on the unit circle; unstable, but only inputs that resonate with a pole blow up.

**Most tested** (every one of the 7 past exams): [[concepts/bibo-stability|stability]] and [[concepts/causality|causality]] T/F statements, the [[concepts/linearity|linear]]/[[concepts/time-invariance|shift-invariant]]/causal/stable table, [[concepts/convolution|finite convolution]], and [[concepts/transfer-function|transfer functions]] with [[concepts/region-of-convergence|ROCs]]. See [[0-midterm-1/index|the Midterm 1 survival guide]].

### Sources for this page
Lecture notes 1–11 (Snyder), the course summary ([[supplements/course-summary]]), and the problem map of the seven past exams ([[0-midterm-1/past-exams/index]]).
