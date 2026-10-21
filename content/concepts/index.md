---
title: "Concepts"
description: "ECE 310 glossary: one short page per idea (definition, how to compute or test it, traps, links to lectures, homework and exam problems), Units 1–5."
tags: [concept]
---

*Concepts · one idea per page: definition, method, traps, where it is used · [[concepts/concept-map.canvas|concept map]] (Units 1–2) · graph view, top right*

### Signals
- [[concepts/discrete-time-signal|Discrete-time signal]]: $x[n]$, $n\in\mathbb{Z}$; mark $n=0$; shift, flip, decimate.
- [[concepts/kronecker-delta|Kronecker delta]] $\delta[n]$: sifting; any signal as shifted deltas.
- [[concepts/unit-step|Unit step]] $u[n]$: windows $u[n]-u[n-N]$; $\delta[n]=u[n]-u[n-1]$.
- [[concepts/complex-exponential|Complex exponential]]: $a^n=r^ne^{j\omega n}$; Euler; principal angle.
- [[concepts/sided-sequences|Sided sequences]]: right-, left-, two-sided; the ROC each forces.

### System properties
- [[concepts/linearity|Linearity]]: superposition; zero in, zero out.
- [[concepts/time-invariance|Time-invariance]]: shift in, same shift out; $x[2n]$, $x[\lvert n\rvert]$.
- [[concepts/causality|Causality]]: no future inputs; LTI: $h[n]=0$ for $n<0$.
- [[concepts/lti-system|LTI system]]: $y=x*h$.

### LTI toolkit
- [[concepts/impulse-response|Impulse response]]: $h[n]=T\{\delta[n]\}$ from a formula, LCCDE or data.
- [[concepts/step-response|Step response]]: $g[n]=h[n]*u[n]$; $h[n]=g[n]-g[n-1]$.
- [[concepts/convolution|Convolution]]: properties, start/end/length, hand methods.
- [[concepts/lccde|Difference equation (LCCDE)]]: two sign conventions; initial rest; `lfilter`.
- [[concepts/fir-and-iir|FIR and IIR]]: FIR always stable.
- [[concepts/block-diagram|Block diagram]]: delays, gains, adders; direct form I.
- [[concepts/eigenfunctions-of-lti-systems|Eigenfunctions of LTI systems]]: $z^n\mapsto H(z)z^n$.

### z-domain
- [[concepts/z-transform|z-transform]]: $X(z)=\sum_n x[n]z^{-n}$, always with ROC.
- [[concepts/region-of-convergence|Region of convergence]]: rings bounded by poles; sidedness, causality, stability.
- [[concepts/poles-and-zeros|Poles and zeros]]: pole-zero plot.
- [[concepts/z-transform-pairs|z-transform pairs]]: $\delta[n]$, $a^nu[n]$, $-a^nu[-n-1]$, $na^nu[n]$, cosine, sine.
- [[concepts/z-transform-properties|z-transform properties]]: linearity, shift, $a^n$, $n$, reversal, convolution.
- [[concepts/inverse-z-transform|Inverse z-transform]]: inspection, partial fractions; ROC decides.
- [[concepts/partial-fraction-expansion|Partial fraction expansion]]: cover-up; long division if improper.
- [[concepts/transfer-function|Transfer function]]: $H(z)=Y(z)/X(z)$; from an LCCDE.
- [[concepts/system-algebra|System algebra]]: series multiplies, parallel adds.

### Stability
- [[concepts/bibo-stability|BIBO stability]]: definition, $\sum\lvert h[n]\rvert<\infty$, ROC contains unit circle.
- [[concepts/pole-zero-cancellation|Pole-zero cancellation]]: inputs that tame unstable systems; stable cascades.
- [[concepts/marginal-stability|Marginal stability]]: unit-circle poles; only resonant inputs blow up.

### Frequency domain (Unit 3)
- [[concepts/template-matching|Template matching]]: matched filter peaks where the input looks like the pattern.
- [[concepts/fourier-series|Fourier series]]: harmonics by orthogonality; road to the transforms.
- [[concepts/dtft|DTFT]]: $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$; $2\pi$-periodic; $=X(e^{j\omega})$ when ROC contains unit circle.
- [[concepts/dtft-pairs|DTFT pairs]]: $\delta$, $a^nu[n]$, pulse, $e^{j\omega_0n}$, cosine, sine, $u[n]$, ideal low-pass.
- [[concepts/dtft-properties|DTFT properties]]: shift, modulation, convolution, windowing, Parseval, Hermitian symmetry.
- [[concepts/frequency-response|Frequency response]]: $H_d(\omega)$; eigenvalue of $e^{j\omega n}$.
- [[concepts/magnitude-and-phase-response|Magnitude and phase response]]: linear or dB; principal phase with jumps.
- [[concepts/group-delay|Group delay and linear phase]]: $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$.

### Sampling (Unit 4)
- [[concepts/sampling|Sampling]]: impulse-train model; copies every $2\pi/T$, scaled $1/T$; $\omega=\Omega T$.
- [[concepts/nyquist-criterion|Nyquist criterion]]: $f_s \gt 2B$; Nyquist rate $2B$; guard band.
- [[concepts/ideal-reconstruction|Ideal reconstruction]]: sinc interpolation; low-pass of height $T$; $Y_a(\Omega)=T\,Y_d(\Omega T)$.
- [[concepts/aliasing|Aliasing]]: overlapping copies; tone returns at the $f_0-kf_s$ closest to 0.

### DFT (Unit 5)
- [[concepts/dft|DFT]]: $X[k]=X_d(2\pi k/N)$, $N$-periodic; zero padding.
- [[concepts/circular-convolution|Circular convolution]]: $\sum_m x[m]h[\langle n-m\rangle_N]\leftrightarrow X[k]H[k]$; equals linear convolution when padded to $N\ge N_1+N_2-1$.

Older pages with an *In Unit 3* paragraph: [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/convolution|convolution]] · [[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|ROC]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/transfer-function|transfer function]] · [[concepts/poles-and-zeros|poles and zeros]].

Most tested: [[exams/midterm-1/index|Midterm 1 review guide]] · [[problems/index|problem families]].

### Sources for this page
Snyder, Lectures 1–21 notes (Fall 2026); [[supplements/course-summary|course summary]]; [[exams/midterm-1/past-exams/index|past Midterm 1]] and [[exams/midterm-2/past-exams/index|Midterm 2]] exams.
