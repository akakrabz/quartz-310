---
title: "ECE 310 · Digital Signal Processing"
description: "Study notes for ECE 310 (DSP, UIUC Fall 2026), organised by topic: 52 topic pages with definitions, worked examples and traps; lecture pages pointing to them; problem families, homework walkthroughs, demos, drills, past exams with folded solutions."
---

Notes for **ECE 310 — Digital Signal Processing** (UIUC, Fall 2026, Profs. Snyder and Kamalabadi), from Prof. Snyder's notes and slides, homework and past exams. By **topic**: one page per idea ([[concepts/index|all topics]]).

## How to learn

> [!tip] A path through each topic
> 1. **Topic page** (concept page): definitions, worked examples, traps.
> 2. **Lecture pages**: what each lecture covered, pointing to the topics.
> 3. **Folded questions**: answer first.
> 4. **Problem families**, one exam problem type each.
> 5. **Homework**, then the walkthrough.
> 6. **Drills and demos.**
> 7. **Past exams**, timed; repair misses by family.

## Course map

### [[0-toolkit/index|Toolkit]] — complex numbers, geometric series, sketching, factoring, [[0-toolkit/05-errata|errata]]

### [[1-signals-and-systems/index|Unit 1 · Signals and systems]] — Lectures 1–5
- **Signals:** [[concepts/discrete-time-signal|discrete-time signal]] · [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/unit-step|unit step]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/sided-sequences|sided sequences]]
- **System properties:** [[concepts/linearity|linearity]] · [[concepts/time-invariance|time-invariance]] · [[concepts/causality|causality]] · [[concepts/lti-system|LTI system]]
- **LTI toolkit:** [[concepts/impulse-response|impulse response]] · [[concepts/step-response|step response]] · [[concepts/convolution|convolution]] · [[concepts/lccde|LCCDE]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/block-diagram|block diagram]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]

*Lectures: [[1-signals-and-systems/01-digital-signals|1]] · [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|2]] · [[1-signals-and-systems/03-system-properties|3]] · [[1-signals-and-systems/04-impulse-response-and-convolution|4]] · [[1-signals-and-systems/05-difference-equations-and-block-diagrams|5]]*

### [[2-z-transform/index|Unit 2 · The z-transform and LTI systems]] — Lectures 6–11
- **z-domain:** [[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|pairs]] · [[concepts/z-transform-properties|properties]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/partial-fraction-expansion|partial fractions]] · [[concepts/transfer-function|transfer function]] · [[concepts/system-algebra|system algebra]]
- **Stability:** [[concepts/bibo-stability|BIBO stability]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/marginal-stability|marginal stability]]

*Lectures: [[2-z-transform/06-the-z-transform|6]] · [[2-z-transform/07-z-transform-properties|7]] · [[2-z-transform/08-inverse-z-transform|8]] · [[2-z-transform/09-transfer-functions|9]] · [[2-z-transform/10-improper-transfer-functions-and-system-algebra|10]] · [[2-z-transform/11-bibo-stability-and-causality|11]]*

### [[3-fourier-analysis/index|Unit 3 · Fourier analysis and frequency response]] — Lectures 12–16
- **Fourier analysis:** [[concepts/periodic-signals|periodic signals]] · [[concepts/fourier-series|Fourier series]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]]
- **Frequency response:** [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase]] · [[concepts/group-delay|group delay]] · [[concepts/template-matching|template matching]]

*Lectures: [[3-fourier-analysis/12-convolution-as-template-matching|12]] (not tested) · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|13]] · [[3-fourier-analysis/14-dtft-properties|14]] · [[3-fourier-analysis/15-frequency-response|15]] · [[3-fourier-analysis/16-magnitude-and-phase-response|16]]*

### [[4-sampling-and-reconstruction/index|Unit 4 · Sampling and reconstruction]] — Lectures 17–19
- [[concepts/sampling|sampling]] · [[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/ideal-reconstruction|ideal reconstruction]] · [[concepts/aliasing|aliasing]] · [[concepts/digital-processing-of-analog-signals|A/D → filter → D/A]]

*Lectures: [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|17]] · [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|18]] · [[4-sampling-and-reconstruction/19-aliasing|19]]*

### [[5-dft-and-fft/index|Unit 5 · The DFT and FFT]] — Lectures 20–23
- **DFT:** [[concepts/dft|DFT]] · [[concepts/zero-padding|zero padding]] · [[concepts/circular-shift-and-reversal|circular shift and reversal]] · [[concepts/dft-properties|DFT properties]] · [[concepts/circular-convolution|circular convolution]]
- **Spectral analysis:** [[concepts/periodic-sinc|periodic sinc]] · [[concepts/spectral-leakage|spectral leakage]] · [[concepts/spectral-analysis|spectral analysis]] · [[concepts/frequency-resolution|frequency resolution]] · [[concepts/window-functions|window functions]]

*Lectures: [[5-dft-and-fft/20-discrete-fourier-transform|20]] · [[5-dft-and-fft/21-dft-properties|21]] · [[5-dft-and-fft/22-spectral-analysis|22]] · [[5-dft-and-fft/23-spectral-analysis-and-window-functions|23]]*

### Practice
[[problems/index|Problem families]] (18) · [[homework/index|Homework]] (HW7: [[exams/quiz-2|Quiz 2]]) · [[demos/practice-drills|Practice drills]] · [[demos/index|Demos]]

### Exams
[[exams/index|Exams hub]]
- **Midterm 1** (L1–11, Sep 30): [[exams/midterm-1/index|review guide]] · [[exams/midterm-1/cheat-sheet|cheat sheet]] · [[exams/midterm-1/true-false-bank|T/F]] and [[exams/midterm-1/system-property-bank|system-property]] banks · [[exams/midterm-1/past-exams/index|past exams]]
- **Quiz 2** (L13–18): [[exams/quiz-2|review]]
- **Midterm 2** (Units 3–5, L13–23, **Wed Nov 4, 7–9 pm**): [[exams/midterm-2/index|review guide]] · [[exams/midterm-2/practice-exam|practice midterm]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[exams/midterm-2/past-exams/index|past exams]]

### Reference
[[concepts/index|All topics]], one line each ([[concepts/concept-map.canvas|concept map]], Units 1–2) · [[supplements/index|Supplements]] (summary, tables, notation)

## Conventions

| | this site | also seen |
|---|---|---|
| signals | $x[n]$, $h[n]$, $y[n]$; integer $n$ | $x(t)$ = continuous time |
| elementary | $\delta[n]$ (Kronecker), $u[n]$ | "unit pulse response" = $h[n]$ |
| $n = 0$ | arrow: $\{1,\ \underset{\uparrow}{2},\ 3\}$ ⇒ $x[0] = 2$ | bold or underlined |
| convolution | $x[n]*h[n]$ | $(x*h)[n]$ |
| system class | LTI | LSI (old exams) |
| z-transforms | powers of $z^{-1}$: $\dfrac{1}{1-az^{-1}}$ | $\dfrac{z}{z-a}$ |
| ROC | always stated: $\lvert z\rvert>a$ | |
| LCCDE (L9) | $y[n]+\sum_k a_k\,y[n-k] = \sum_k b_k\,x[n-k]$, $\;H(z) = \dfrac{\sum_k b_kz^{-k}}{1+\sum_k a_kz^{-k}}$ (`lfilter(b, a)`) | L5: $y[n] = \sum_i b_i\,y[n-i]+\sum_j c_j\,x[n-j]$, signs flipped |
| partial fractions | $\sum_k \dfrac{A_k}{1-p_kz^{-1}}$, $A_k$ by cover-up | `residuez` |
| DTFT | $X_d(\omega) = \sum_n x[n]e^{-j\omega n}$, on $[-\pi,\pi]$, rad/sample | $X(e^{j\omega})$ — equal if the ROC contains the unit circle |
| frequency response | $H_d(\omega)$; $\lvert H_d\rvert\ge0$; $\angle H_d\in[-\pi,\pi]$ | $H(e^{j\omega})$; a sign-changing amplitude is not the magnitude |
| impulses | $\delta[n]$: one sample, height 1; $\delta(\omega)$, $\delta(t)$: Dirac, area 1 | |
| continuous time | $x_a(t)$, $X_c(\Omega)$ or $X_a(\Omega)$, rad/s; $\omega=\Omega T$; $\mathrm{sinc}(t)=\frac{\sin t}{t}$ | $X(\Omega)$ in L13; tables: $\frac{\sin\pi x}{\pi x}$ |
| DFT | $X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$; $\langle n\rangle_N$ = $n$ mod $N$ | against $\omega_k=2\pi k/N$ or $f_k=kf_s/N$ |
| exam citations | FA2024 MT2 #4 = Fall 2024, Midterm 2, problem 4 | FA2024 #4 on Midterm 1 pages |

## Callouts

> [!key]
> Result to remember.

> [!recipe]
> Procedure.

> [!trap]
> Point-losing mistake.

> [!exam]
> Exam appearances.

> [!intuition]
> The picture behind it.

> [!derivation]-
> Folded derivation.

> [!question]
> Answer first.

> [!success]- Answer
> Folded solution.

*Status (Oct 30, 2026): Lectures 1–23 (Lecture 23 = last Midterm 2 content); walkthroughs HW1–HW6, [[homework/hw8|HW8]], [[homework/hw9|HW9]]. **Midterm 2: Wed Nov 4, 7–9 pm** (HW5–9, L13–23): [[exams/midterm-2/index|review guide]] · [[exams/midterm-2/practice-exam|practice midterm]].*

### Sources for this page
Snyder, ECE 310 notes and slides L1–23 (Fall 2026); notation supplement; exam cover pages.
