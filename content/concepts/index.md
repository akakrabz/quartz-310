---
title: "Concepts · topic map"
description: "The topic map of ECE 310: 52 topic pages (Units 1–5), one per idea, each with definitions, key equations, worked examples, figures, traps and the exam problems that use it. The primary study pages."
tags: [concept]
---

*Concepts (topic pages) · 52 pages, one idea each · the primary study pages: definitions, key equations, worked examples (folded answers), figures, traps, exam problems · lectures: [[index|home]] · [[concepts/concept-map.canvas|concept map]] (Units 1–2) · graph view, top right*

Each topic page absorbs what the lectures said about it: the notes' definitions and equations (with lecture and equation numbers), the worked examples, the figures and the recipe. The lecture pages only say what each lecture covered and point here. Study a topic here, then its problem family.

## Unit 1 · Signals and systems

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

## Unit 2 · The z-transform and LTI systems

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

## Unit 3 · Fourier analysis and frequency response
- [[concepts/periodic-signals|Periodic signals and discrete-time frequency]]: $x[n+N_0]=x[n]$; $\cos(\omega_0n)$ periodic only if $\omega_0/2\pi$ is rational; frequencies $2\pi$ apart are the same sequence: $\cos(\frac{17\pi}{3}n)=\cos(\frac{5\pi}{3}n)$.
- [[concepts/fourier-series|Fourier series]]: harmonics by orthogonality; road to the transforms.
- [[concepts/dtft|DTFT]]: $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$; $2\pi$-periodic; $=X(e^{j\omega})$ when ROC contains unit circle.
- [[concepts/dtft-pairs|DTFT pairs]]: $\delta$, $a^nu[n]$, pulse, $e^{j\omega_0n}$, cosine, sine, $u[n]$, ideal low-pass.
- [[concepts/dtft-properties|DTFT properties]]: shift, modulation, convolution, windowing, Parseval, Hermitian symmetry.
- [[concepts/frequency-response|Frequency response]]: $H_d(\omega)$; eigenvalue of $e^{j\omega n}$.
- [[concepts/magnitude-and-phase-response|Magnitude and phase response]]: linear or dB; principal phase with jumps.
- [[concepts/group-delay|Group delay and linear phase]]: $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$.
- [[concepts/template-matching|Template matching]] (L12, not tested): matched filter peaks where the input looks like the pattern.

## Unit 4 · Sampling and reconstruction
- [[concepts/sampling|Sampling]]: impulse-train model; copies every $2\pi/T$, scaled $1/T$; $\omega=\Omega T$.
- [[concepts/nyquist-criterion|Nyquist criterion]]: $f_s \gt 2B$; Nyquist rate $2B$; guard band.
- [[concepts/ideal-reconstruction|Ideal reconstruction]]: sinc interpolation; low-pass of height $T$; $Y_a(\Omega)=T\,Y_d(\Omega T)$.
- [[concepts/aliasing|Aliasing]]: overlapping copies; tone returns at the $f_0-kf_s$ closest to 0.
- [[concepts/digital-processing-of-analog-signals|Digital processing of analog signals]]: A/D → $H_d$ → D/A; $Y_a(\Omega)=T\,Y_d(\Omega T)$; acts as $H_a(\Omega)=H_d(\Omega T)$ if nothing aliases; analog cutoff $\omega_c/T$.

## Unit 5 · The DFT and spectral analysis

### DFT (Lectures 20–21)
- [[concepts/dft|DFT]]: $X[k]=X_d(2\pi k/N)$, $k=0,\dots,N-1$; inverse; $N$-periodic in $n$ and $k$.
- [[concepts/zero-padding|Zero padding]]: append $L$ zeros: same DTFT, denser DFT grid $X_d(\frac{2\pi k}{N+L})$; no new information, no better lobe separation.
- [[concepts/circular-shift-and-reversal|Circular shift, reversal and modulo indexing]]: $\langle n\rangle_N$; $x[\langle n-m\rangle_N]\leftrightarrow e^{-j2\pi km/N}X[k]$; $x[\langle -n\rangle_N]$ keeps $x[0]$, $\leftrightarrow X[\langle -k\rangle_N]$.
- [[concepts/dft-properties|DFT properties]]: Table 1 — linearity, shift, modulation, reversal, conjugation ($x^*[n]\leftrightarrow X^*[\langle -k\rangle_N]$), real $x$ ⇒ Hermitian $X$, Parseval.
- [[concepts/circular-convolution|Circular convolution]]: $\sum_m x[m]h[\langle n-m\rangle_N]\leftrightarrow X[k]H[k]$; equals linear convolution when padded to $N\ge N_1+N_2-1$.

### Spectral analysis (Lectures 22–23)
- [[concepts/periodic-sinc|Periodic sinc (Dirichlet) function]]: $C(\omega)=e^{-j\omega(N-1)/2}\frac{\sin(N\omega/2)}{\sin(\omega/2)}$: height $N$, main lobe $4\pi/N$, nulls at $2\pi k/N$; a length-$N$ cosine has $X_d(\omega)=\frac A2C(\omega-\omega_0)+\frac A2C(\omega+\omega_0)$.
- [[concepts/spectral-leakage|Spectral leakage]]: an on-bin cosine ($\omega_0=2\pi k/N$) gives two bins of height $NA/2$; a fractional number of periods spreads the tone over every bin.
- [[concepts/spectral-analysis|Spectral analysis with the DFT]]: the hub — read $M$, $A_m$, $\omega_m$ of $\sum_m A_m\cos(\omega_mn)$ from a DFT plot (bin $k$ ↔ $\omega_k=2\pi k/N$ ↔ $f_k=kf_s/N$); two challenges: close frequencies, unequal amplitudes.
- [[concepts/frequency-resolution|Lobe separation and frequency resolution]]: full-lobe $N\gt4\pi/\Delta\omega$ (record time $2/\Delta f$), half-lobe $N\gt2\pi/\Delta\omega$; a longer record resolves, zero padding does not.
- [[concepts/window-functions|Window functions]]: $x[n]w[n]\leftrightarrow\frac{1}{2\pi}X_d*W_d$; rectangular: half-width $2\pi/N$, side lobes $-13$ dB; Hamming $0.54-0.46\cos\frac{2\pi n}{N-1}$: half-width $4\pi/N$, $-42$ dB; windowing is multiplication, not an LTI system.

Most tested: [[exams/midterm-1/index|Midterm 1 review guide]] · [[exams/midterm-2/index|Midterm 2 overview]] · [[problems/index|problem families]].

### Sources for this page
Snyder, Lectures 1–23 notes (Fall 2026); [[supplements/course-summary|course summary]]; [[exams/midterm-1/past-exams/index|past Midterm 1]] and [[exams/midterm-2/past-exams/index|Midterm 2]] exams.
