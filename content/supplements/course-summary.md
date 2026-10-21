---
title: "Course summary sheet"
description: "The course's ECE 310 summary (review.pdf) transcribed: notation, system properties, LSI systems, LCCDEs, z-transform, stability and its z-transform table, then the Unit 3 and later items linked."
tags: [supplement, midterm-1, systems, z-transform, dtft]
---

*Supplement · `suppliment/review.pdf` ("ECE 310: Summary", 8 pages) · Midterm 1 on pages 1–3, Unit 3 from page 3*

## 1. Notation

| | textbook | class |
|---|---|---|
| DTFT | $X(e^{j\omega})$ | $X_d(\omega)$ |
| CTFT | $X(j\Omega)$ | $X_c(\Omega)$ |
| convolution | $x[n]*h[n]$ | $(x*h)[n]$ |

More: [[supplements/notation-translation|notation translation]].

## 2. Midterm 1 content

- **Sample vs signal:** $x[n]$ is a number; $\{x[n]\}$ the whole sequence ([[concepts/discrete-time-signal|discrete-time signal]]).
- **Linear:** $S\{a_1x_1[n] + a_2x_2[n]\} = a_1S\{x_1[n]\} + a_2S\{x_2[n]\}$ ([[concepts/linearity|linearity]]).
- **Shift-invariant:** if $\{y[n]\} = S\{x[m]\}$, then $\{y[n-n_0]\} = S\{x[m-n_0]\}$ ([[concepts/time-invariance|time invariance]]).
- **Causal:** $y[n]$ depends only on $x[m]$, $m\le n$ ([[concepts/causality|causality]]).
- **BIBO stable:** $\lvert x[n]\rvert < B_{\text{in}}$ ⇒ $\lvert y[n]\rvert < B_{\text{out}}$ ([[concepts/bibo-stability|BIBO stability]]).
- **LSI** (the lectures' LTI): $y[n] = \sum_{k}x[k]\,h[n-k]$; $Y(z) = H(z)X(z)$; $Y_d(\omega) = H_d(\omega)X_d(\omega)$ ([[concepts/convolution|convolution]], [[concepts/transfer-function|transfer function]], [[concepts/frequency-response|frequency response]]).
- **LCCDE:**

$$
\begin{gathered}
y[n] = -a_1y[n-1] - \dots - a_Ky[n-K] + b_0x[n] + \dots + b_Lx[n-L],\\
H(z) = \frac{b_0 + b_1z^{-1} + \dots + b_Lz^{-L}}{1 + a_1z^{-1} + \dots + a_Kz^{-K}} = \frac{B(z)}{A(z)} .
\end{gathered}
$$

Same sign convention as Lecture 9 and `lfilter`; Lecture 5 uses $+$ on feedback ([[concepts/lccde|LCCDE]]).
- **z-transform:** $X(z) = \sum_{n}x[n]z^{-n}$ with its ROC ([[concepts/z-transform|z-transform]]).
- **Stable LSI:** $\sum_{n}\lvert h[n]\rvert < \infty$; causal: all poles inside $|z|=1$. General (Lecture 11): ROC contains $\lvert z\rvert = 1$.

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $a^n u[n]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $-a^n u[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert<\lvert a\rvert$ |
| $ax[n] + by[n]$ | $aX(z) + bY(z)$ | $\mathrm{ROC}_X\cap\mathrm{ROC}_Y$ (at least) |
| $x[n-n_0]$ | $z^{-n_0}X(z)$ | $\mathrm{ROC}_X$ except $0$ or $\infty$ |
| $a^n x[n]$ | $X(a^{-1}z)$ | $\lvert a\rvert\,\mathrm{ROC}_X$ |
| $n\,x[n]$ | $-z\dfrac{dX(z)}{dz}$ | $\mathrm{ROC}_X$ |
| $x[-n]$ | $X(1/z)$ | $1/\mathrm{ROC}_X$ |
| $x^*[n]$ | $X^*(z^*)$ | $\mathrm{ROC}_X$ |

"(at least)" is added: a cancelled pole can enlarge the ROC. Procedures (cover-up, long division, pole matching) are on the [[exams/midterm-1/cheat-sheet|cheat sheet]].

## 3. Unit 3 and later (pages 3–8)

- CTFT, DTFT and its properties ($X_d(\omega) = X(z)\vert_{z=e^{j\omega}}$ if the ROC includes $|z|=1$, periodicity, symmetry, windowing, Parseval): [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]], [[concepts/dtft-properties|DTFT properties]].
- Signal as a sum of sinusoids: [[concepts/fourier-series|Fourier series]], [[concepts/template-matching|template matching]].
- Sinusoidal response: $\cos(\omega_0 n + \phi) \to \lvert H_d(\omega_0)\rvert\cos(\omega_0 n + \phi + \angle H_d(\omega_0))$ for real $h$: [[3-fourier-analysis/15-frequency-response|Lecture 15]].
- Linear and generalized linear phase: [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]], [[concepts/group-delay|group delay]].
- Later: sampling, aliasing, DAC; DFT, FFT, circular convolution; linear convolution via zero-padding, length $L + M - 1$ ([[problems/finite-length-convolution|finite-length convolution]]); FIR and IIR design; up/downsampling; convolution as a matrix product; LMS.

## Related
[[supplements/transform-tables|transform tables]] · [[exams/midterm-1/cheat-sheet|cheat sheet]] · [[3-fourier-analysis/index|Unit 3]]

### Sources for this page
`suppliment/review.pdf` pages 1–8; Lectures 5, 9, 11 notes (conventions); Lectures 12–16 (Unit 3 links).
