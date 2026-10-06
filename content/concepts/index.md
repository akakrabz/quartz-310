---
title: "Concepts"
description: "The glossary of ECE 310: one short page per idea (definition, how to test or compute it, the traps exams punish, and links to every lecture, homework and past-exam problem that uses it) — 28 ideas from Units 1–2 and 8 from Unit 3, the DTFT and frequency response."
tags: [concept]
---

Lectures tell the story in order; **concept pages** are the glossary you consult out of order. Each one is short and self-contained: the definition, how to test or compute it, the mistakes that cost points, and links back to the lectures that develop it and the exam problems that test it. Open the graph view (top right of any page) to see how they connect, or the [[concepts/concept-map.canvas|concept map]], which lays out the Units 1–2 ideas on one canvas with labelled arrows for what depends on what. 28 pages cover Units 1–2 (Lectures 1–11) and 8 more cover Unit 3 (Lectures 12–16).

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

### Frequency domain (Unit 3)
- [[concepts/template-matching|Template matching]]: convolution with a time-reversed pattern (a matched filter) peaks where the input looks like the pattern; the same idea in 2-D for images.
- [[concepts/fourier-series|Fourier series]]: a periodic signal as a sum of harmonics, with coefficients found by orthogonality; the road from Fourier series to the Fourier transforms.
- [[concepts/dtft|DTFT]]: $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$ and its inverse; $2\pi$-periodic; exists for absolutely summable $x$; equals $X(e^{j\omega})$ when the ROC contains the unit circle.
- [[concepts/dtft-pairs|DTFT pairs]]: $\delta[n]$, $a^nu[n]$, the rectangular pulse, $e^{j\omega_0n}$, cosine and sine (with Dirac impulses), $u[n]$ and the ideal lowpass.
- [[concepts/dtft-properties|DTFT properties]]: shift, modulation, convolution, windowing, Parseval, Hermitian symmetry for real signals.
- [[concepts/frequency-response|Frequency response]]: $H_d(\omega)$, the DTFT of $h[n]$ and the eigenvalue of $e^{j\omega n}$; how a real system scales and shifts a sinusoid.
- [[concepts/magnitude-and-phase-response|Magnitude and phase response]]: $\lvert H_d(\omega)\rvert$ on a linear or dB scale, and the phase as a principal angle with its jumps.
- [[concepts/group-delay|Group delay and linear phase]]: $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$; linear phase delays every frequency by the same number of samples.

Eight older pages carry a short *In Unit 3* paragraph on how the frequency domain extends them: [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] (the frequency response is the eigenvalue on the unit circle), [[concepts/complex-exponential|complex exponential]] (its DTFT is an impulse), [[concepts/convolution|convolution]] (template matching; convolution ↔ product of DTFTs), [[concepts/z-transform|z-transform]] and [[concepts/region-of-convergence|ROC]] (the DTFT is $X(z)$ on the unit circle when the ROC contains it), [[concepts/bibo-stability|BIBO stability]] (stable ⇔ the DTFT sum of $h$ converges absolutely), [[concepts/transfer-function|transfer function]] ($H_d(\omega)=H(e^{j\omega})$) and [[concepts/poles-and-zeros|poles and zeros]] (they shape $\lvert H_d(\omega)\rvert$).

**Most tested on Midterm 1** (all seven past exams): [[concepts/bibo-stability|stability]] and [[concepts/causality|causality]] T/F statements, the [[concepts/linearity|linear]]/[[concepts/time-invariance|shift-invariant]]/causal/stable table, [[concepts/convolution|finite convolution]], and [[concepts/transfer-function|transfer functions]] with [[concepts/region-of-convergence|ROCs]] — see the [[exams/midterm-1/index|Midterm 1 review guide]]. On the past Midterm 2 exams the Unit 3 pages carry three problem families — DTFTs and inverse DTFTs, responses to sinusoids, and magnitude, phase and group delay — listed on [[problems/index|problem families]].

### Sources for this page
Lecture notes 1–16 (Snyder), the course summary ([[supplements/course-summary]]), the problem map of the seven past Midterm 1 exams ([[exams/midterm-1/past-exams/index]]) and the past Midterm 2 exams ([[exams/midterm-2/past-exams/index]]).
