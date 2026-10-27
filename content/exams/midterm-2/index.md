---
title: "Midterm 2"
description: "ECE 310 Midterm 2 (Fall 2026, date not yet announced): Units 3–5, Lectures 13–23 (DTFT, frequency response, sampling, the DFT, spectral analysis); past-exam format, problem types per exam, preparation, formula boxes."
tags: [exam, midterm-2]
---

*Midterm 2 · Fall 2026 date not yet announced (past fall exams: early November) · Units 3–5, Lectures 13–23 · [[exams/midterm-2/past-exams/index|seven past exams]] · [[exams/index|Exams]]*

> [!abstract] In one breath
> - Frequency domain: [[3-fourier-analysis/index|Unit 3]] (L13–16), [[4-sampling-and-reconstruction/index|Unit 4]] (L17–19), [[5-dft-and-fft/index|Unit 5]] (L20–23). Lecture 23 (spectral analysis and window functions) is the last lecture covered.
> - Past exams: 2 hours (90–110 min in 2019–2021), 7–11 problems, 100 points, handwritten sheets, no calculator. Unit 3 is 18–42 points.
> - Learn each topic's past problems from its [[concepts/index|topic page]] and family; then take SP2025 and FA2024 whole, timed.

## 1. Scope

| part | lectures | skills (topic pages) |
|---|---|---|
| [[3-fourier-analysis/index\|Unit 3]] | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] (Sep 23) · [[3-fourier-analysis/14-dtft-properties\|L14]] (Sep 25) · [[3-fourier-analysis/15-frequency-response\|L15]] (Oct 2) · [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] (Oct 5, 7) | [[concepts/dtft\|DTFT]] and inverse from definition, [[concepts/dtft-pairs\|pairs]], [[concepts/dtft-properties\|properties]]; $X_d(0)$, $X_d(\pi)$, $\int X_d$, $\int\lvert X_d\rvert^2$; when $X_d(\omega) = X(e^{j\omega})$; [[concepts/frequency-response\|frequency response]] $H_d(\omega)$ from $h$, $H(z)$ or LCCDE; response to sinusoids; [[concepts/magnitude-and-phase-response\|magnitude/phase]] sketches; [[concepts/group-delay\|group delay]] |
| [[4-sampling-and-reconstruction/index\|Unit 4]] | [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion\|L17]] (Oct 9) · [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion\|L18]] (Oct 12) · [[4-sampling-and-reconstruction/19-aliasing\|L19]] (Oct 14) | [[concepts/nyquist-criterion\|Nyquist rate]]; sketch $X_d$ after [[concepts/sampling\|sampling]]; [[concepts/ideal-reconstruction\|ideal D/A]] output; consistent sampling periods ([[concepts/aliasing\|aliasing]]); $T$ and $\omega_c$ for [[concepts/digital-processing-of-analog-signals\|A/D → filter → D/A]] |
| [[5-dft-and-fft/index\|Unit 5]] · DFT | [[5-dft-and-fft/20-discrete-fourier-transform\|L20]] (Oct 16) · [[5-dft-and-fft/21-dft-properties\|L21]] (Oct 19) | [[concepts/dft\|DFT]] values and $X[k]=X_d(2\pi k/N)$; [[concepts/zero-padding\|zero padding]]; [[concepts/circular-shift-and-reversal\|circular shift, reversal]], modulation, conjugation, symmetry ([[concepts/dft-properties\|DFT properties]]); [[concepts/circular-convolution\|circular vs linear convolution]] |
| [[5-dft-and-fft/index\|Unit 5]] · spectral analysis | [[5-dft-and-fft/22-spectral-analysis\|L22]] (Oct 21) · [[5-dft-and-fft/23-spectral-analysis-and-window-functions\|L23]] (Oct 23) | DFT of a finite cosine via the [[concepts/periodic-sinc\|periodic sinc]]; [[concepts/spectral-leakage\|leakage]] vs two clean bins; frequencies and amplitudes from a DFT plot ([[concepts/spectral-analysis\|spectral analysis]]); zero padding as denser sampling; full- and half-lobe [[concepts/frequency-resolution\|separation]], the $N$ needed; rectangular vs Hamming [[concepts/window-functions\|windows]] |

Not tested: [[3-fourier-analysis/12-convolution-as-template-matching|L12]]; the FFT (FA2019 #10) is beyond Lecture 23. Units 1–2 used throughout: the ROC decides whether the DTFT is $X(e^{j\omega})$ (FA2023 #1(a), FA2024 #1(a), FA2021 #2).

Homework: [[homework/hw5|HW5]] (L13–14) · [[homework/hw6|HW6]] (L13–16) · HW7 (L15–18, on [[exams/quiz-2|Quiz 2]]) · later sets on the DFT when posted.

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
| ***Unit 4*** | | | | | | | | |
| T/F on sampling, D/A → [[exams/midterm-2/true-false-bank\|bank]] §4–5 | #1(c) | #1(c) | #1(d,e) | #1(a,b,e) | #1(c,e) | #1(a,b,d) | — | 6/7 |
| [[problems/sampling-and-the-nyquist-rate\|Sampling, Nyquist, aliasing, ideal D/A]] | #6 | #5(a,b) | #3 | #8 | — | #8, #9 | #8 | 6/7 |
| [[problems/digital-filtering-of-analog-signals\|A/D → filter → D/A]] | #5 | #5(b), (c) | #5 | #7 | #4, #5 | — | #9 | 6/7 |
| ***Unit 5*** | | | | | | | | |
| T/F on the DFT, spectral analysis → [[exams/midterm-2/true-false-bank\|bank]] §6–8 | #1(b,e,f) | #1(d) | #1(f,g,h) | #1(d) | #1(b,d) | #1(c,e) | #1(f–j) | 7/7 |
| [[problems/dft-values-and-zero-padding\|DFT values and zero padding]] | #7(a), (c) | #6, #7 | #7(a), (b) | #9(a), (c) | #3(a) | #5, #6 | #2 | 7/7 |
| [[problems/circular-convolution-and-dft-properties\|Circular convolution and DFT properties]] | #7(b), #8 | #8 | #7 | #9(b) | #3(b), #6 | #4 | #4, #11 | 7/7 |
| [[problems/dft-spectral-analysis\|DFT spectral analysis]] | #9 | #9 | #1(g), #6 | #10 | #7 | — | #1(c), (f) | 6/7 |

A problem counts in every row it uses. Zero-padding T/F statements only about the DTFT count as Unit 3. Every A/D → $H_d$ → D/A problem also samples, so sampling is on 7/7. Per-problem detail: [[exams/midterm-2/past-exams/index|past exams]].

> [!exam] Patterns
> - Every exam: a DTFT or inverse DTFT. Snyder's four (SP2023–SP2025) add a magnitude/phase sketch and a sinusoid response.
> - Sampling and DFT properties: 7/7; DFT spectral analysis: 6/7. Circular vs linear convolution: FA2021 #6, FA2019 #11 (the FFT, FA2019 #10, is not in scope).
> - T/F: 16 of 43 statements Unit 3, 12 sampling and D/A, 15 DFT and FFT.
> - Snyder exams, points: T/F 10–16 · DTFT 6–11 · magnitude/phase 12–14 · sinusoids 8–12 · sampling-and-filtering 16–22 · sampling puzzle 6–12 · DFT properties 14–18 · spectral analysis 10–20.

## 4. Preparation

1. **Per topic:** its [[concepts/index|topic page]] (key callouts, folded examples, trap), then its family page and past problems:
   - Unit 3: [[problems/dtft-and-inverse-dtft|DTFTs]] · [[problems/lti-response-to-sinusoids|sinusoids]] · [[problems/magnitude-phase-and-group-delay|magnitude and phase]]; [[demos/practice-drills|drills]]; check SP2025 #3 in the [[demos/frequency-response-explorer|frequency-response explorer]].
   - Unit 4: [[problems/sampling-and-the-nyquist-rate|sampling]] (SP2025 #6, FA2023 #3, SP2023 #8, SP2021 #9) · [[problems/digital-filtering-of-analog-signals|A/D → filter → D/A]] (SP2025 #5, FA2024 #5(c), FA2023 #5, SP2023 #7, FA2021 #4–5, FA2019 #9); [[demos/sampling-explorer|sampling explorer]].
   - Unit 5: [[problems/dft-values-and-zero-padding|DFT values and zero padding]] (SP2025 #7, FA2024 #7, SP2023 #9) · [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]] (SP2025 #8, FA2024 #8, FA2023 #7, FA2021 #6) · [[problems/dft-spectral-analysis|spectral analysis]] (SP2025 #9, FA2024 #9, FA2023 #6, SP2023 #10, FA2021 #7).
2. **Unit 3 self-test:** SP2025 #2–#4 (32 points, ~40 min), then FA2024 #2–#4; T/F bank §1–3. Bank: the other Unit 3 cells, [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8–#9, [[exams/midterm-1/past-exams/fall-2019|FA2019 MT1]] #8–#9.
3. **Whole exams:** [[exams/midterm-2/past-exams/spring-2025|SP2025]] then [[exams/midterm-2/past-exams/fall-2024|FA2024]], timed; the others by topic.
4. **Sheet by hand:** start from §5–§7; [[exams/quiz-2|Quiz 2]] has the Unit 4 sheet in full.

## 5. Unit 3 formulas for your sheet

> [!key] Formulas — Unit 3
> | | formula |
> |---|---|
> | [[concepts/dtft\|DTFT]] and inverse | $X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}$, $\quad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega$ |
> | existence | $2\pi$-periodic; exists if $\sum_n\lvert x[n]\rvert<\infty$; $X_d(\omega)=X(e^{j\omega})$ needs the unit circle in the ROC ($2^nu[n]$: none; $u[n]\leftrightarrow\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$) |
> | free values | $X_d(0)=\sum_n x[n]$, $\quad X_d(\pi)=\sum_n(-1)^n\,x[n]$, $\quad\int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0]$ |
> | Parseval | $\sum_n\lvert x[n]\rvert^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2\,d\omega$ |
> | finite [[concepts/dtft-pairs\|pairs]] | $\delta[n-k]\leftrightarrow e^{-j\omega k}$, $\quad u[n]-u[n-L]\leftrightarrow e^{-j\omega(L-1)/2}\,\frac{\sin(L\omega/2)}{\sin(\omega/2)}$ ($L$ odd, centred at $n=0$: no exponential) |
> | exponentials, $\lvert a\rvert<1$ | $a^nu[n]\leftrightarrow\frac{1}{1-ae^{-j\omega}}$, $\quad n\,a^nu[n]\leftrightarrow\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ |
> | ideal low-pass | $\frac{\sin(\omega_cn)}{\pi n}$ ($\frac{\omega_c}{\pi}$ at $n=0$) $\leftrightarrow$ $1$ for $\lvert\omega\rvert\le\omega_c$, $0$ for $\omega_c<\lvert\omega\rvert\le\pi$ |
> | impulses (one period) | $1\leftrightarrow2\pi\delta(\omega)$, $\quad e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$, $\quad\cos(\omega_0n)\leftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$, $\quad\sin(\omega_0n)\leftrightarrow-j\pi[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |
> | shift, modulation ([[concepts/dtft-properties\|properties]]) | $x[n-k]\leftrightarrow e^{-j\omega k}X_d(\omega)$, $\quad e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$, $\quad x[n]\cos(\omega_0n)\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$ |
> | reversal, conjugation | $x[-n]\leftrightarrow X_d(-\omega)$, $\quad x^*[n]\leftrightarrow X_d^*(-\omega)$, $\quad x$ real $\Leftrightarrow X_d(-\omega)=X_d^*(\omega)$ |
> | $n\,x[n]$, convolution, window | $n\,x[n]\leftrightarrow+j\,\frac{dX_d(\omega)}{d\omega}$ (L14 prints $-j$: erratum), $\quad x[n]*h[n]\leftrightarrow X_d(\omega)H_d(\omega)$, $\quad x[n]w[n]\leftrightarrow\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\theta)\,W_d(\omega-\theta)\,d\theta$ |
> | [[concepts/frequency-response\|frequency response]] | $H_d(\omega)=\sum_n h[n]\,e^{-j\omega n}$; inputs on all $n$: $e^{j\omega_0n}\mapsto H_d(\omega_0)\,e^{j\omega_0n}$, $\quad c\mapsto H_d(0)\,c$, $\quad(-1)^n\mapsto H_d(\pi)\,(-1)^n$ |
> | real $h$ | check $H_d(-\omega)=H_d^*(\omega)$; $A\cos(\omega_0n+\theta)\mapsto A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$ |
> | complex $h$ | $\cos(\omega_0n+\theta)\mapsto\frac12H_d(\omega_0)\,e^{j(\omega_0n+\theta)}+\frac12H_d(-\omega_0)\,e^{-j(\omega_0n+\theta)}$ |
> | [[concepts/magnitude-and-phase-response\|magnitude and phase]] | $H_d(\omega)=e^{-jM\omega}R(\omega)$, $R$ real ($M$ = centre of symmetric taps; antisymmetric: $j\,e^{-jM\omega}R(\omega)$, add $\frac{\pi}{2}$): $\lvert H_d\rvert=\lvert R\rvert$, $\;\angle H_d=-M\omega$, $\pm\pi$ where $R<0$, wrapped into $[-\pi,\pi]$ |
> | [[concepts/group-delay\|group delay]] | $\tau_{gd}(\omega)=-\frac{d\angle H_d(\omega)}{d\omega}$ between jumps; linear phase $-M\omega$ gives $\tau_{gd}=M$ |

## 6. Unit 4 formulas for your sheet

> [!key] Formulas — Unit 4
> | | formula |
> |---|---|
> | [[concepts/sampling\|sampling]] | $x[n]=x_a(nT)$, $f_s=\frac1T$; $X_d(\omega)=\frac1T\sum_{n}X_a\!\left(\frac{\omega-2\pi n}{T}\right)$: copies every $2\pi$, scaled $\frac1T$; $\omega=\Omega T$; $f$ Hz lands at $\omega=2\pi f/f_s$ |
> | [[concepts/nyquist-criterion\|Nyquist]] | $X_a(\Omega)=0$ for $\lvert\Omega\rvert\gt2\pi B$: no overlap $\iff f_s\gt2B\iff T\lt\frac{1}{2B}$ |
> | [[concepts/aliasing\|aliasing]] | $\cos(\Omega_0t)\to\cos(\Omega_0Tn)$; reduce $\Omega_0T$ mod $2\pi$ into $(-\pi,\pi]$; the D/A returns the $f_0-kf_s$ closest to $0$ (sine: sign matters) |
> | [[concepts/ideal-reconstruction\|ideal D/A]] | $x_a(t)=\sum_nx[n]\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right)$, $\mathrm{sinc}(t)=\frac{\sin t}{t}$; $Y_a(\Omega)=T\,Y_d(\Omega T)$ for $\lvert\Omega\rvert\le\frac{\pi}{T}$, $0$ outside |
> | [[concepts/digital-processing-of-analog-signals\|A/D → filter → D/A]] | digital cutoff $\omega_c$ ↔ analog $\omega_c/T$; no aliasing into the passband ⇒ $H_a(\Omega)=H_d(\Omega T)$ on $\lvert\Omega\rvert\lt\frac{\pi}{T}$ |

## 7. Unit 5 formulas for your sheet

> [!key] Formulas — Unit 5
> | | formula |
> |---|---|
> | [[concepts/dft\|DFT]] and inverse | $X[k]=\sum_{n=0}^{N-1}x[n]\,e^{-j\frac{2\pi k}{N}n}$, $\quad x[n]=\frac1N\sum_{k=0}^{N-1}X[k]\,e^{j\frac{2\pi k}{N}n}$, $\quad 0\le n,k\le N-1$; $N$-periodic in $n$ and $k$ |
> | DTFT samples | $X[k]=X_d\!\left(\frac{2\pi k}{N}\right)$; bin $k$ ↔ $\omega_k=\frac{2\pi k}{N}$ ↔ $f_k=\frac{k\,f_s}{N}$ Hz (plus aliases $f_k+mf_s$); $X[0]=\sum_nx[n]$, $X[\frac N2]=\sum_n(-1)^nx[n]$ |
> | [[concepts/zero-padding\|zero padding]] | $L$ zeros appended: $\tilde X[k]=X_d\!\left(\frac{2\pi k}{N+L}\right)$ — the same DTFT, sampled more densely; no new information, no better separation |
> | [[concepts/circular-shift-and-reversal\|shift, modulation]] | $x[\langle n-m\rangle_N]\leftrightarrow e^{-j\frac{2\pi km}{N}}X[k]$, $\quad e^{j\frac{2\pi ln}{N}}x[n]\leftrightarrow X[\langle k-l\rangle_N]$, $\quad\langle n\rangle_N$ = remainder of $n/N$ |
> | reversal, conjugation ([[concepts/dft-properties\|properties]]) | $x[\langle -n\rangle_N]\leftrightarrow X[\langle -k\rangle_N]$, $\quad x^*[n]\leftrightarrow X^*[\langle -k\rangle_N]$; real $x\Leftrightarrow X[\langle -k\rangle_N]=X^*[k]$; Parseval $\sum_n\lvert x[n]\rvert^2=\frac1N\sum_k\lvert X[k]\rvert^2$ |
> | [[concepts/circular-convolution\|circular convolution]] | $x[n]\circledast h[n]=\sum_{m=0}^{N-1}x[m]\,h[\langle n-m\rangle_N]\leftrightarrow X[k]H[k]$; equals $x*h$ when $N\ge N_1+N_2-1$ (pad both) |
> | [[concepts/periodic-sinc\|periodic sinc]] | $C(\omega)=e^{-j\omega(N-1)/2}\,\dfrac{\sin(N\omega/2)}{\sin(\omega/2)}$, $C(0)=N$; zeros at $\omega=\frac{2\pi k}{N}$, $k\ne0$; main lobe width $\frac{4\pi}{N}$ |
> | finite cosine ([[concepts/spectral-leakage\|leakage]]) | $x[n]=A\cos(\omega_0n)$, $0\le n\le N-1$: $X_d(\omega)=\frac A2C(\omega-\omega_0)+\frac A2C(\omega+\omega_0)$, $X[k]=X_d(\frac{2\pi k}{N})$. If $\omega_0=\frac{2\pi k_0}{N}$: two bins of height $\frac{NA}{2}$ at $k_0$ and $N-k_0$; otherwise leakage into every bin |
> | [[concepts/frequency-resolution\|lobe separation]] | full-lobe $\omega_2-\omega_1\gt\frac{4\pi}{N}\iff N\gt\frac{4\pi}{\Delta\omega}$; half-lobe $N\gt\frac{2\pi}{\Delta\omega}$; with $\Delta\omega=2\pi\,\Delta f/f_s$: $N\gt\frac{2f_s}{\Delta f}$ (full), $\frac{f_s}{\Delta f}$ (half). Zero padding does not help; a longer record does |
> | [[concepts/window-functions\|windows]] | $x[n]w[n]\leftrightarrow\frac{1}{2\pi}X_d*W_d$ (not an LTI system). Rectangular $u[n]-u[n-N]$: main lobe $\frac{4\pi}{N}$, first side lobe $-13$ dB. Hamming $0.54-0.46\cos\!\left(\frac{2\pi n}{N-1}\right)$: main lobe $\frac{8\pi}{N}$, side lobes $-42$ dB. Trade-off: narrow main lobe vs low side lobes |

## Related
[[exams/midterm-2/past-exams/index|past exams]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[problems/index|problem families]] · [[concepts/index|topic pages]] · [[supplements/transform-tables|transform tables]] · [[0-toolkit/05-errata|errata]] · [[exams/index|all exams]]

### Sources for this page
Covers, point tables and keys of the seven past Midterm 2 exams (FA2019–SP2025); L12 notes ("not tested"); Lectures 13–23 notes and slides (Fall 2026); numbers checked in `verify/THUB_numbers.py`.
