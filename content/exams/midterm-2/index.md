---
title: "Midterm 2"
description: "ECE 310 Midterm 2 (Fall 2026 date and scope not yet announced): Units 3–5 (DTFT, frequency response, sampling, the DFT); past-exam format, problem types per exam, preparation, Unit 3 formula box."
tags: [exam, midterm-2]
---

*Midterm 2 · Fall 2026 date and scope not announced (past fall exams: early November) · Units 3–5 · [[exams/midterm-2/past-exams/index|seven past exams]] · [[exams/index|Exams]]*

> [!abstract] In one breath
> - Frequency domain: [[3-fourier-analysis/index|Unit 3]] (L13–16), [[4-sampling-and-reconstruction/index|Unit 4]] (L17–19), [[5-dft-and-fft/index|Unit 5]] (DFT, from L20).
> - Past exams: 2 hours (90–110 min in 2019–2021), 7–11 problems, 100 points, handwritten sheets, no calculator. Unit 3 is 18–42 points.
> - Learn each lecture's past problems as it is taught; take whole exams once the scope is announced.

## 1. Scope

| part | lectures | skills |
|---|---|---|
| [[3-fourier-analysis/index\|Unit 3]] | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] (Sep 23) · [[3-fourier-analysis/14-dtft-properties\|L14]] (Sep 25) · [[3-fourier-analysis/15-frequency-response\|L15]] (Oct 2) · [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] (Oct 5, 7) | DTFT and inverse from definition, pairs, properties; $X_d(0)$, $X_d(\pi)$, $\int X_d$, $\int\lvert X_d\rvert^2$; when $X_d(\omega) = X(e^{j\omega})$; $H_d(\omega)$ from $h$, $H(z)$ or LCCDE; response to sinusoids; magnitude/phase sketches; group delay |
| [[4-sampling-and-reconstruction/index\|Unit 4]] | [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion\|L17]] (Oct 9) · [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion\|L18]] (Oct 12) · [[4-sampling-and-reconstruction/19-aliasing\|L19]] (Oct 14) | Nyquist rate; sketch $X_d$ after sampling; ideal D/A output; consistent sampling periods; $T$ and $\omega_c$ for A/D → $H_d$ → D/A |
| [[5-dft-and-fft/index\|Unit 5]] | [[5-dft-and-fft/20-discrete-fourier-transform\|L20]] (Oct 16) · [[5-dft-and-fft/21-dft-properties\|L21]] (Oct 19) · later lectures to come | DFT values; DFT properties (circular shift, symmetry, zero-padding); circular vs linear convolution; spectral analysis from a DFT plot |

Unit 5 (Lectures 20–21) starts the DFT and its properties. Not tested: [[3-fourier-analysis/12-convolution-as-template-matching|L12]]. Units 1–2 used throughout: the ROC decides whether the DTFT is $X(e^{j\omega})$ (FA2023 #1(a), FA2024 #1(a), FA2021 #2).

Homework: [[homework/hw5|HW5]] (L13–14) · [[homework/hw6|HW6]] (L13–16) · HW7 (L15–18, on [[exams/quiz-2|Quiz 2]]) · later sets.

## 2. Format (past exams)

| | FA2019–SP2025 |
|---|---|
| when | fall: Nov 6 2019, Nov 9 2021, Nov 1 2023, Nov 6 2024 (evenings); spring: early April |
| length | 2 hours (SP2023–SP2025); 90 min FA2019, FA2021; 110 min SP2021 |
| size | 7–11 problems, 100 points (SP2025: 12 + 10 + 12 + 10 + 16 + 12 + 12 + 6 + 10) |
| sheets | two (FA2019, FA2023, FA2024, SP2025); one (SP2021, SP2023); FA2021 online, open notes. No calculator |
| answers | closed form; show all work |
| True/False | problem 1, 10–20 points; +2 / −1 / 0 on SP2023, SP2025; reasons required on FA2024 |

## 3. Problem types × past exams

| problem type | [[exams/midterm-2/past-exams/spring-2025\|SP25]] | [[exams/midterm-2/past-exams/fall-2024\|FA24]] | [[exams/midterm-2/past-exams/fall-2023\|FA23]] | [[exams/midterm-2/past-exams/spring-2023\|SP23]] | [[exams/midterm-2/past-exams/fall-2021\|FA21]] | [[exams/midterm-2/past-exams/spring-2021\|SP21]] | [[exams/midterm-2/past-exams/fall-2019\|FA19]] | exams |
|---|---|---|---|---|---|---|---|---|
| ***Unit 3*** | | | | | | | | |
| T/F on DTFT → [[exams/midterm-2/true-false-bank\|bank]] §1–3 | #1(a,d) | #1(a,b,d) | #1(a–c,f) | #1(c) | #1(a) | — | #1(a–e) | 6/7 |
| [[problems/dtft-and-inverse-dtft\|DTFTs and inverse DTFTs]] | #2 | #2 | #2 | #2, #3, #4 | #2 | #3, #6(a), #7 | #3, #5, #6 | 7/7 |
| [[problems/lti-response-to-sinusoids\|Response to sinusoids]] | #4 | #4 | #4(b) | #6 | — | — | #7 | 5/7 |
| [[problems/magnitude-phase-and-group-delay\|Magnitude, phase, group delay]] | #3 | #3 | #4(a) | #5 | — | #2 | — | 5/7 |
| *Unit 3 points* | 36 | 41 | 32 | 35 | 18 | 36 | 42 | 18–42 |
| ***Units 4–5*** | | | | | | | | |
| T/F on sampling, D/A, DFT, FFT → [[exams/midterm-2/true-false-bank\|bank]] §4–8 | #1(b,c,e,f) | #1(c,d) | #1(d,e,g,h) | #1(a,b,d,e) | #1(b–e) | #1(a–e) | #1(f–j) | 7/7 |
| [[problems/sampling-and-the-nyquist-rate\|Sampling, Nyquist, aliasing, ideal D/A]] | #6 | #5(a,b) | #3 | #8 | — | #8, #9 | #8 | 6/7 |
| [[problems/digital-filtering-of-analog-signals\|A/D → H_d → D/A]] | #5 | #5(b), (c) | #5 | #7 | #4, #5 | — | #9 | 6/7 |
| DFT computation and properties ([[5-dft-and-fft/20-discrete-fourier-transform\|L20]], [[5-dft-and-fft/21-dft-properties\|L21]]) | #7, #8 | #7, #8 | #7 | #9 | #3 | #4, #5, #6(b) | #4 | 7/7 |
| DFT spectral analysis | #9 | #6, #9 | #6 | #10 | #7 | — | #2 | 6/7 |
| Linear vs circular convolution, FFT | — | — | — | — | #6 | — | #10, #11 | 2/7 |

A problem counts in every row it uses. Zero-padding T/F statements only about the DTFT count as Unit 3. Every A/D → $H_d$ → D/A problem also samples, so sampling is on 7/7. Per-problem detail: [[exams/midterm-2/past-exams/index|past exams]].

> [!exam] Patterns
> - Every exam: a DTFT or inverse DTFT. Snyder's four (SP2023–SP2025) add a magnitude/phase sketch and a sinusoid response.
> - Sampling and DFT properties: 7/7; DFT spectral analysis: 6/7. Circular convolution and the FFT: only 2019 and 2021.
> - T/F: 16 of 43 statements Unit 3, 12 sampling and D/A, 15 DFT and FFT.
> - Snyder exams, points: T/F 10–16 · DTFT 6–11 · magnitude/phase 12–14 · sinusoids 8–12 · sampling-and-filtering 16–22 · sampling puzzle 6–12 · DFT properties 14–18 · spectral analysis 10–20.

## 4. Preparation

1. **Per lecture:** read it, do its folded questions, then its family page and past problems:
   - Unit 3: [[problems/dtft-and-inverse-dtft|DTFTs]] · [[problems/lti-response-to-sinusoids|sinusoids]] · [[problems/magnitude-phase-and-group-delay|magnitude and phase]]; [[demos/practice-drills|drills]]; check SP2025 #3 in the [[demos/frequency-response-explorer|frequency-response explorer]].
   - Unit 4: [[problems/sampling-and-the-nyquist-rate|sampling]] (SP2025 #6, FA2023 #3, SP2023 #8, SP2021 #9) · [[problems/digital-filtering-of-analog-signals|A/D → H_d → D/A]] (SP2025 #5, FA2024 #5(c), FA2023 #5, SP2023 #7, FA2021 #4–5, FA2019 #9); [[demos/sampling-explorer|sampling explorer]].
   - Unit 5: DFT properties SP2025 #7–#8, FA2024 #8; spectral analysis SP2025 #9, FA2024 #9.
2. **Unit 3 self-test:** SP2025 #2–#4 (32 points, ~40 min), then FA2024 #2–#4; T/F bank §1–3. Bank: the other Unit 3 cells, [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8–#9, [[exams/midterm-1/past-exams/fall-2019|FA2019 MT1]] #8–#9.
3. **Once the scope is out:** [[exams/midterm-2/past-exams/spring-2025|SP2025]] then [[exams/midterm-2/past-exams/fall-2024|FA2024]] whole, timed; others by topic.
4. **Sheet by hand:** start from §5; add later topics.

## 5. Unit 3 formulas for your sheet

> [!key] Formulas — Unit 3
> | | formula |
> |---|---|
> | DTFT and inverse | $X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}$, $\quad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega$ |
> | existence | $2\pi$-periodic; exists if $\sum_n\lvert x[n]\rvert<\infty$; $X_d(\omega)=X(e^{j\omega})$ needs the unit circle in the ROC ($2^nu[n]$: none; $u[n]\leftrightarrow\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$) |
> | free values | $X_d(0)=\sum_n x[n]$, $\quad X_d(\pi)=\sum_n(-1)^n\,x[n]$, $\quad\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$ |
> | Parseval | $\sum_n\lvert x[n]\rvert^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2\,d\omega$ |
> | finite pairs | $\delta[n-k]\leftrightarrow e^{-j\omega k}$, $\quad u[n]-u[n-L]\leftrightarrow e^{-j\omega(L-1)/2}\,\frac{\sin(L\omega/2)}{\sin(\omega/2)}$ ($L$ odd, centred at $n=0$: no exponential) |
> | exponentials, $\lvert a\rvert<1$ | $a^nu[n]\leftrightarrow\frac{1}{1-ae^{-j\omega}}$, $\quad n\,a^nu[n]\leftrightarrow\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ |
> | ideal low-pass | $\frac{\sin(\omega_cn)}{\pi n}$ ($\frac{\omega_c}{\pi}$ at $n=0$) $\leftrightarrow$ $1$ for $\lvert\omega\rvert\le\omega_c$, $0$ for $\omega_c<\lvert\omega\rvert\le\pi$ |
> | impulses (one period) | $1\leftrightarrow2\pi\delta(\omega)$, $\quad e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$, $\quad\cos(\omega_0n)\leftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$, $\quad\sin(\omega_0n)\leftrightarrow-j\pi[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |
> | shift, modulation | $x[n-k]\leftrightarrow e^{-j\omega k}X_d(\omega)$, $\quad e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$, $\quad x[n]\cos(\omega_0n)\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$ |
> | reversal, conjugation | $x[-n]\leftrightarrow X_d(-\omega)$, $\quad x^*[n]\leftrightarrow X_d^*(-\omega)$, $\quad x$ real $\Leftrightarrow X_d(-\omega)=X_d^*(\omega)$ |
> | $n\,x[n]$, convolution, window | $n\,x[n]\leftrightarrow+j\,\frac{dX_d(\omega)}{d\omega}$ (L14 prints $-j$: erratum), $\quad x[n]*h[n]\leftrightarrow X_d(\omega)H_d(\omega)$, $\quad x[n]w[n]\leftrightarrow\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\theta)\,W_d(\omega-\theta)\,d\theta$ |
> | frequency response | $H_d(\omega)=\sum_n h[n]\,e^{-j\omega n}$; inputs on all $n$: $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$, $\quad c\mapsto H_d(0)\,c$, $\quad(-1)^n\mapsto H_d(\pi)\,(-1)^n$ |
> | real $h$ | check $H_d(-\omega)=H_d^*(\omega)$; $A\cos(\omega_0n+\theta)\mapsto A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$ |
> | complex $h$ | $\cos(\omega_0n+\theta)\mapsto\frac12H_d(\omega_0)\,e^{j(\omega_0n+\theta)}+\frac12H_d(-\omega_0)\,e^{-j(\omega_0n+\theta)}$ |
> | magnitude and phase | $H_d(\omega)=e^{-jM\omega}R(\omega)$, $R$ real ($M$ = centre of symmetric taps; antisymmetric: $j\,e^{-jM\omega}R(\omega)$, add $\frac{\pi}{2}$): $\lvert H_d\rvert=\lvert R\rvert$, $\;\angle H_d=-M\omega$, $\pm\pi$ where $R<0$, wrapped into $[-\pi,\pi]$ |
> | group delay | $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$ between jumps; linear phase $-M\omega$ gives $\tau_{gd}=M$ |

## Related
[[exams/midterm-2/past-exams/index|past exams]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[problems/index|problem families]] · [[supplements/transform-tables|transform tables]] · [[0-toolkit/05-errata|errata]] · [[exams/index|all exams]]

### Sources for this page
Covers, point tables and keys of the seven past Midterm 2 exams (FA2019–SP2025); L12 notes ("not tested"); Lectures 13–21 notes and slides (Fall 2026).
