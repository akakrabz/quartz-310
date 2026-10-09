---
title: "Course summary sheet"
description: "The course's own ECE 310 summary (review.pdf) transcribed and organised: the Midterm 1 parts in full — notation, system properties, LSI systems and convolution, LCCDEs, the z-transform, stability and the z-transform table — then the Unit 3 items (CTFT, DTFT and its properties, the sinusoidal response) linked to Lectures 12–16, and the later parts listed."
tags: [supplement, midterm-1, systems, z-transform, dtft]
---

*Supplement · `suppliment/review.pdf` ("ECE 310: Summary", 8 pages) · Midterm 1 content is on pages 1–3, the DTFT and the frequency response (Unit 3) on page 3*

This is the instructors' one-document summary of the whole course. Pages 1–3 are exactly the Midterm 1 toolkit; pages 3–8 are the rest of the semester, starting with Unit 3. Below, the Midterm 1 parts are transcribed in full (in the summary's own notation, with a note wherever it differs from the lectures), and each item is linked to the page on this site that develops it.

## 1. Notation

- Discrete-domain signal $x[n]$; continuous-domain signal $x(t)$. Discrete-domain frequency $\omega$; continuous-domain frequency $\Omega$.
- Textbook vs class notation:

| | textbook | class |
|---|---|---|
| DTFT | $X(e^{j\omega})$ | $X_d(\omega)$ |
| CTFT | $X(j\Omega)$ | $X_c(\Omega)$ |
| convolution | $x[n]*h[n]$ | $(x*h)[n]$ |

"The textbook notation explicitly indicates that the DTFT is a special case of the z-transform and the CTFT is a special case of the Laplace transform." More translations: [[supplements/notation-translation|notation translation]].

## 2. Key concepts and equations (Midterm 1)

**Signal vs sample.** A *sample* $x[n]$ is the value at index $n$ — a number. A *signal* $x$ or $\{x[n]\}$ is the whole sequence of samples — an array. ([[concepts/discrete-time-signal|discrete-time signal]])

**System.** A mapping $S$ from an input signal to an output signal: $\{y[n]\} = S\{x[m]\}$, or sample by sample $y[n] = S_n\{x[m]\}$.

**System properties** — $S$ has the property if and only if:

- **Linear:** $S\{a_1x_1[n] + a_2x_2[n]\} = a_1S\{x_1[n]\} + a_2S\{x_2[n]\}$. ([[concepts/linearity|linearity]])
- **Shift-invariant** (time-invariant): if $\{y[n]\} = S\{x[m]\}$ then $\{y[n-n_0]\} = S\{x[m-n_0]\}$, for a fixed $n_0$. ([[concepts/time-invariance|time invariance]])
- **Causal:** $y[n] = S_n\{x[m]\}$ depends only on $x[m]$ with $m\le n$. ([[concepts/causality|causality]])
- **Stable (BIBO):** if $\lvert x[n]\rvert < B_{\text{in}} < \infty$ for all $n$, then $\lvert y[n]\rvert < B_{\text{out}} < \infty$ for all $n$. ([[concepts/bibo-stability|BIBO stability]])

These four definitions are the whole of the [[problems/classifying-system-properties|system-property table]] that opens every exam.

**LSI (linear and shift-invariant) system** — the lectures' "LTI". If $S$ is LSI with impulse response $\{h[n]\} = S\{\delta[n]\}$, then

- in the time domain it is a convolution: $y[n] = (x*h)[n] = \sum_{k\in\mathbb Z}x[k]\,h[n-k] = \sum_{k\in\mathbb Z}h[k]\,x[n-k]$ ([[concepts/convolution|convolution]], [[concepts/lti-system|LTI system]]);
- in the z-domain: $Y(z) = H(z)X(z)$, with $H(z)$ the transfer function = z-transform of the impulse response ([[concepts/transfer-function|transfer function]]);
- in the frequency (DTFT) domain: $Y_d(\omega) = H_d(\omega)X_d(\omega)$, where $H_d(\omega)$ is the frequency response ([[concepts/frequency-response|frequency response]], [[3-fourier-analysis/15-frequency-response|Lecture 15]]).

**LCCDE** (linear constant-coefficient difference equation):

$$
\begin{gathered}
y[n] = -a_1y[n-1] - \dots - a_Ky[n-K] + b_0x[n] + \dots + b_Lx[n-L],\\
n = 0,1,2,\dots
\end{gathered}
$$

Equivalently, in the z-domain (zero initial conditions): $Y(z) = H(z)X(z)$ with

$$
H(z) = \frac{b_0 + b_1z^{-1} + \dots + b_Lz^{-L}}{1 + a_1z^{-1} + \dots + a_Kz^{-K}} = \frac{B(z)}{A(z)} .
$$

"This is the general form of realizable (practical) causal LSI systems. It can be realized in block diagrams by direct form I or II. The roots of the numerator $B(z)$ are the zeros of $H(z)$, the roots of the denominator $A(z)$ are the poles of $H(z)$."

> [!note] Matching this to the lectures
> The minus signs on the $a_k$ make this the same convention as Lecture 9 ($y[n] + \sum a_k y[n-k] = \sum b_k x[n-k]$) and as `scipy.signal.lfilter(b, a, x)`; Lecture 5 writes the feedback terms with a plus sign ([[0-toolkit/05-errata|errata]] lists the difference). "Roots of $B(z)$" means roots after multiplying through by the right power of $z$ — poles and zeros at $z=0$ and $\infty$ count too ([[0-toolkit/04-factoring-and-long-division|factoring]]). See [[concepts/lccde|LCCDE]], [[concepts/block-diagram|block diagrams]].

**z-transform:** $\{x[n]\} \overset{\mathcal Z}{\longleftrightarrow} X(z) = \sum_{n\in\mathbb Z}x[n]z^{-n}$, and the ROC is the region of $z$ where the sum converges. ([[concepts/z-transform|z-transform]], [[concepts/region-of-convergence|ROC]], [[0-toolkit/02-geometric-series|geometric series]])

**LSI stable:** an LSI system with impulse response $h[n]$ is stable if and only if

- in the time domain: $\sum_{n\in\mathbb Z}\lvert h[n]\rvert < +\infty$;
- equivalently, in the z-domain (assuming causality): all poles are inside the unit circle.

> [!key] The general version (Lecture 11)
> Without assuming causality: stable ⇔ the ROC of $H(z)$ contains the unit circle $\lvert z\rvert = 1$. Causal ⇔ the ROC is the outside of a circle and includes $\infty$. The summary's "all poles inside the unit circle" is the special case of both at once. See [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] and [[problems/parameters-for-stability|parameters for stability]].

**The summary's z-transform table** (page 3):

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $a^n u[n]$ (right-sided sequence) | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $-a^n u[-n-1]$ (left-sided sequence) | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert<\lvert a\rvert$ |
| $ax[n] + by[n]$ | $aX(z) + bY(z)$ | $\mathrm{ROC}_X\cap\mathrm{ROC}_Y$ (at least) |
| $x[n-n_0]$ (fixed $n_0$) | $z^{-n_0}X(z)$ | $\mathrm{ROC}_X$ except $0$ or $\infty$ |
| $a^n x[n]$ | $X(a^{-1}z)$ | $\lvert a\rvert\,\mathrm{ROC}_X$ |
| $n\,x[n]$ | $-z\dfrac{dX(z)}{dz}$ | $\mathrm{ROC}_X$ |
| $x[-n]$ | $X(1/z)$ | $1/\mathrm{ROC}_X$ |
| $x^*[n]$ | $X^*(z^*)$ | $\mathrm{ROC}_X$ |

(Every row checked numerically with the full tables in [[supplements/transform-tables|transform tables]]; "at least" added — a cancelled pole can enlarge the ROC.)

> [!tip] Using this on exam night
> These three pages plus the transform table are a complete skeleton for the handwritten sheet; what they leave out is procedure — convolution bookkeeping, the PFE cover-up rule, long division, ROC-from-sidedness, pole matching. Those are on the [[exams/midterm-1/cheat-sheet|cheat sheet]] page.

## 3. The rest of the summary — Unit 3 and later

Listed in the summary's order (pages 3–8). The first four items are Unit 3 ([[3-fourier-analysis/index|Lectures 12–16]]); the rest come after Lecture 16.

- Continuous-time Fourier transform (CTFT) pair, $X_c(\Omega)$ — [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]].
- Discrete-time Fourier transform (DTFT) pair, $X_d(\omega)$; DTFT properties: relation to the z-transform $X_d(\omega) = X(z)\vert_{z=e^{j\omega}}$ if the ROC includes the unit circle, $2\pi$-periodicity, conjugate symmetry for real signals, windowing, Parseval — [[concepts/dtft|DTFT]], [[concepts/dtft-properties|DTFT properties]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]]; the pairs the summary leaves out are on [[concepts/dtft-pairs|DTFT pairs]].
- Signal representation via the Fourier transform (a signal as a weighted sum of sinusoids) — [[concepts/fourier-series|Fourier series]] and [[concepts/template-matching|template matching]] ([[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]]: each $X_d(\omega)$ scores how much of $e^{j\omega n}$ the signal holds).
- Sinusoidal response of an LSI system: $e^{j\omega_0 n} \to H_d(\omega_0)e^{j\omega_0 n}$; for real $h$, $\cos(\omega_0 n + \phi) \to \lvert H_d(\omega_0)\rvert\cos(\omega_0 n + \phi + \angle H_d(\omega_0))$ (the frequency-domain face of [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]]) — [[3-fourier-analysis/15-frequency-response|Lecture 15]], [[concepts/frequency-response|frequency response]].
- Sampling (ADC) and aliasing; DAC — ideal and zero-order hold.
- DFT and inverse DFT, DFT properties (relation to the DTFT, circular shift, circular convolution).
- Linear convolution of finite-length sequences via zero-padding: output length $N = L + M - 1$ — **this length rule is Midterm 1 material** ([[problems/finite-length-convolution|finite-length convolution]]).
- FFT (decimation in time, butterflies); spectral analysis with the DFT and windowing.
- Linear-phase and generalized-linear-phase filters; FIR GLP symmetry conditions; the ideal low-pass filter. (The summary's GLP phase, $\alpha\omega+\beta$ plus $\pi$ wherever the real amplitude $A(\omega)$ is negative, is the phase rule of [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]; see [[concepts/group-delay|group delay]].)
- FIR filter design by windowing (Hamming); IIR design by the bilinear transformation.
- Downsampling and upsampling in the frequency domain.
- Signals as vectors; the normalized DFT matrix; linear systems as matrices.
- Linear regression; **convolution written as a matrix product** $y = X^T w$ — the "convolution matrix" the past exam keys use for finite convolutions (FA2019 #4, SP2021 #2); machine learning and adaptive filters, gradient descent, LMS.

Lectures 12–16 are developed in [[3-fourier-analysis/index|Unit 3]].

### Sources for this page

`suppliment/review.pdf` pages 1–8 (pages 2–3 rendered to confirm the table); Lecture 5, 9 and 11 notes for the notes on conventions; Lectures 12–16 for the Unit 3 links. The length rule, the convolution-matrix form and the LCCDE sign convention are checked in `verify/hub/supp_summary.py`; the table rows in `verify/hub/supp_tables.py`.
