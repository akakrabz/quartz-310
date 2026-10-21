---
title: "Past Midterm 2 exams"
description: "Seven past ECE 310 Midterm 2 exams (FA2019–SP2025) with folded solutions: what each is good for, a problem-by-problem map of all 62 problems with topic and family, and key slips."
tags: [exam, midterm-2]
---

*Seven past Midterm 2 exams, newest first · 62 problems, folded solutions · [[exams/midterm-2/index|Midterm 2 overview]]*

> [!abstract] In one breath
> - 2 hours (90–110 min in 2019–2021), 7–11 problems, 100 points, no calculator. Unit 3: 18–42 points; rest: sampling, filtering, DFT.
> - Self-test by unit; take SP2025 and FA2024 whole once the scope is out.

## The seven exams

| exam | date | instructors | probs / pts | Unit 3 pts | notes |
|---|---|---|---|---|---|
| [[exams/midterm-2/past-exams/spring-2025\|Spring 2025]] | Apr 9, 2025 | Liang, Snyder | 9 / 100 | 36 | T/F +2/−1/0; first full run |
| [[exams/midterm-2/past-exams/fall-2024\|Fall 2024]] | Nov 6, 2024 | Do, Shomorony, Snyder | 9 / 100 | 41 | T/F with reasons; second full run |
| [[exams/midterm-2/past-exams/fall-2023\|Fall 2023]] | Nov 1, 2023 | Do, Snyder, Moustakides | 7 / 100 | 32 | #4: complex $h$ |
| [[exams/midterm-2/past-exams/spring-2023\|Spring 2023]] | Apr 5, 2023 | Liang, Moon, Snyder | 10 / 100 | 35 | T/F +2/−1/0 |
| [[exams/midterm-2/past-exams/fall-2021\|Fall 2021]] | Nov 9, 2021 | Zhao, Katselis, Kamalabadi | 7 / 100 | 18 | online, open notes, 90 min |
| [[exams/midterm-2/past-exams/spring-2021\|Spring 2021]] | Apr 8, 2021 | Moon, Katselis, Shomorony | 9 / 100 | 36 | online; most DTFT |
| [[exams/midterm-2/past-exams/fall-2019\|Fall 2019]] | Nov 6, 2019 | Kamalabadi, Katselis, Liang | 11 / 100 | 42 | 90 min; every topic |

Unit 3 points count zero-padding T/F as Unit 3 (exam pages: 30, 38, 34 for FA2023, FA2024, SP2025). LSI = LTI.

## How to use these exams

> [!tip] By unit
> - **Unit 3:** SP2025 #2–#4 and FA2024 #2–#4 timed (~50 min). Bank: FA2023 #2, #4; SP2023 #2–#6; FA2021 #2; SP2021 #2, #3, #7; FA2019 #3, #5–#7. [[exams/midterm-2/true-false-bank|T/F bank]] Q1–Q16.
> - **Unit 4:** SP2025 #5, #6; FA2024 #5; FA2023 #3, #5; SP2023 #7, #8; FA2021 #4, #5; SP2021 #8, #9; FA2019 #8(b), #9. T/F Q18–Q29.
> - **Unit 5 ([[5-dft-and-fft/index|DFT]]):** DFT rows below.
> - Repair each lost point by [[problems/index|family]].

> [!trap] Unit 3 traps
> - Real $h$? Check $H_d(-\omega)=H_d^*(\omega)$: FA2024 #4 yes; SP2023 #6, FA2023 #4 no.
> - Magnitude $\ge0$ (FA2024 #3: $H_d(\frac{\pi}{2})=-1$); no extra $\pi$ if the real factor stays $\ge0$ (SP2025 #3).
> - $X_d(\omega)=X(e^{j\omega})$ needs the unit circle in the ROC: FA2023 #1(a), FA2024 #1(a), FA2021 #2.
> - $2\pi$ factors: $\int X_d=2\pi x[0]$ (FA2019 #3); $\delta(\omega-\omega_0)\leftrightarrow\frac{1}{2\pi}e^{j\omega_0n}$ (SP2023 #4).
> - Copies wrap around $\pm\pi$ (SP2025 #2b); every DTFT is $2\pi$-periodic (FA2019 #1(b), (e)).

## Problem by problem

Families: [[problems/dtft-and-inverse-dtft|DTFT]] · [[problems/lti-response-to-sinusoids|sinusoids]] · [[problems/magnitude-phase-and-group-delay|mag/phase]] (Unit 3); [[problems/sampling-and-the-nyquist-rate|sampling]] · [[problems/digital-filtering-of-analog-signals|A/D–D/A]] (Unit 4); DFT problems: [[5-dft-and-fft/index|Unit 5]].

### [[exams/midterm-2/past-exams/spring-2025|Spring 2025]]

| # | pts | asks | family |
|---|---|---|---|
| 1 | 12 | six T/F: inverse DTFT, IDFT, ideal D/A, zero-padding, DFT of a cosine, Hamming | DTFT · DFT |
| 2 | 10 | DTFTs of $x[n]\cos(\frac{2\pi}{5}n)$, $x[n]\cos^2(\frac{2\pi}{5}n)$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 3 | 12 | $\lvert H_d\rvert$, $\angle H_d$ of $x[n] + 2x[n-3] + x[n-6]$ | [[problems/magnitude-phase-and-group-delay\|mag/phase]] |
| 4 | 10 | $H_d = j\omega e^{j\pi\sin\omega}$ on $5 + 2e^{j\frac{\pi}{4}n} + \sin(\frac{\pi}{2}n + \frac{\pi}{4}) + (-1)^n$ | [[problems/lti-response-to-sinusoids\|sinusoids]] |
| 5 | 16 | A/D → LPF → D/A: $X_d$, $Y_d$, $Y_a$; largest $T$, $\omega_c$ | [[problems/digital-filtering-of-analog-signals\|A/D–D/A]] |
| 6 | 12 | sampling periods consistent with sinusoids; $T$ from an alias | [[problems/sampling-and-the-nyquist-rate\|sampling]] |
| 7 | 12 | length-8 DFT: $X_0$; permuted DFT; zero-padding | DFT properties |
| 8 | 6 | $y[n]$ from $Y[m] = X[m]e^{j\frac{3\pi}{4}m}$ | circular shift |
| 9 | 10 | DFT of 16 samples of $\cos(\frac{\pi}{2}n)$ | spectral analysis |

### [[exams/midterm-2/past-exams/fall-2024|Fall 2024]]

| # | pts | asks | family |
|---|---|---|---|
| 1 | 12 | four T/F with reasons: DTFT existence, periodicity, ideal D/A, zero-padding | DTFT · DFT |
| 2 | 8 | $x[n]$ from an ideal high-pass $X_d$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 3 | 12 | $H_d(0)$, $H_d(\frac{\pi}{2})$, $H_d(\pi)$, $\lvert H_d\rvert$ for $\delta[n+2] + \delta[n] + \delta[n-2]$ | [[problems/magnitude-phase-and-group-delay\|mag/phase]] |
| 4 | 12 | $H_d = \lvert\omega\rvert e^{-j\pi\sin\omega}$: real $h$? output for $3 + \cos\frac{\pi n}{6} + j^n$ | [[problems/lti-response-to-sinusoids\|sinusoids]] |
| 5 | 22 | triangle: Nyquist period; $X_d$, $Y_c$ at $T_N$, $2T_N$; largest $T$ | [[problems/digital-filtering-of-analog-signals\|A/D–D/A]] |
| 6 | 8 | analog frequencies in bin $k$ ($f_s = 1000$ Hz, $N = 1024$) | spectral analysis |
| 7 | 6 | smallest $N$ containing $X_d(\frac{2\pi}{5})$, $X_d(\frac{\pi}{3})$ | DFT |
| 8 | 8 | $Y[k]$ of a circularly reversed, shifted $x$ | DFT properties |
| 9 | 12 | two cosines from a 32-point DFT plot | spectral analysis |

### [[exams/midterm-2/past-exams/fall-2023|Fall 2023]]

| # | pts | asks | family |
|---|---|---|---|
| 1 | 16 | eight T/F: DTFT, Hermitian, Nyquist, D/A, zero-padding, leakage, bin ↔ frequency | DTFT · DFT |
| 2 | 6 | $X_d(0)$, $X_d(\pi)$ of a 5-sample pulse | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 3 | 6 | $\Omega_0$ giving $\sin(\frac{\pi}{2}n)$ at 400 Hz | [[problems/sampling-and-the-nyquist-rate\|sampling]] |
| 4 | 18 | $\lvert H_d\rvert$, $\angle H_d$ of $(\frac12 + \cos\omega)e^{j\lvert\omega\rvert}$; output | [[problems/magnitude-phase-and-group-delay\|mag/phase]] · [[problems/lti-response-to-sinusoids\|sinusoids]] |
| 5 | 20 | C/D → $H_d$ → D/C: largest $T$, low-pass then high-pass | [[problems/digital-filtering-of-analog-signals\|A/D–D/A]] |
| 6 | 16 | cosine frequency from 32- and 64-point DFTs | spectral analysis |
| 7 | 18 | DFT conjugation proof; two real DFTs from one | DFT properties |

### [[exams/midterm-2/past-exams/spring-2023|Spring 2023]]

| # | pts | asks | family |
|---|---|---|---|
| 1 | 10 | five T/F: sampling, Nyquist of $x_c(3t)$, zero-padding, IDFT periodicity | DTFT · sampling · DFT |
| 2 | 3 | real $x$: $X_d$ on $[-\pi, 0]$ from $j\omega$ on $[0, \pi]$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 3 | 3 | any $x$: $X_d$ on $[2\pi, 3\pi]$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 4 | 5 | inverse DTFT of $5e^{j\pi\omega}\delta(\omega - \omega_0)$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 5 | 14 | magnitude, phase of $\delta[n] + \delta[n-6]$ | [[problems/magnitude-phase-and-group-delay\|mag/phase]] |
| 6 | 8 | $\omega e^{j\pi\cos\omega}$ on $3 + e^{j\frac{\pi}{3}n} + \sin(\frac{\pi}{2}n + \frac{\pi}{4})$ | [[problems/lti-response-to-sinusoids\|sinusoids]] |
| 7 | 20 | A/D → $H_d$ → D/A at two rates | [[problems/digital-filtering-of-analog-signals\|A/D–D/A]] |
| 8 | 10 | sampling periods consistent with $x[n]$, $y_c(t)$ | [[problems/sampling-and-the-nyquist-rate\|sampling]] |
| 9 | 15 | $X_0$, $X_3$; permuted DFT; zero-padding | DFT properties |
| 10 | 12 | cosines from a 24-point DFT plot | spectral analysis |

### [[exams/midterm-2/past-exams/fall-2021|Fall 2021]]

| # | pts | asks | family |
|---|---|---|---|
| 1 | 15 | five T/F: eigenfunctions, DFT, reconstruction, zero-padding, sampling | DTFT · sampling · DFT |
| 2 | 15 | LCCDE: $H(z)$, $h$, $H_d$; why $H_d \ne H(e^{j\omega})$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 3 | 10 | 8-point DFT at even $k$; DFT of $x[\langle 3-n\rangle_8]\,j^n$ | DFT properties |
| 4 | 15 | sampler → high-pass → D/A at two rates | [[problems/digital-filtering-of-analog-signals\|A/D–D/A]] |
| 5 | 15 | largest $T$; $H_d$ realising $H_a$ | [[problems/digital-filtering-of-analog-signals\|A/D–D/A]] |
| 6 | 15 | linear vs 6-point circular convolution | circular convolution |
| 7 | 15 | DFT peaks of a cosine, $L = 500$, padded to 1024 | spectral analysis |

### [[exams/midterm-2/past-exams/spring-2021|Spring 2021]]

| # | pts | asks | family |
|---|---|---|---|
| 1 | 15 | five T/F: sampling, Nyquist of $x_c(2t)$, $X[0]$, impulse integral | sampling · DFT |
| 2 | 10 | magnitude, phase of $e^{-j4\omega}\sin 2\omega$ | [[problems/magnitude-phase-and-group-delay\|mag/phase]] |
| 3 | 9 | DTFT of $3\delta[n+1] - 3\delta[n-7]$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 4 | 8 | sequence with DFT $e^{-j(\frac{6\pi}{8}k+\pi)}X[k]$ | circular shift |
| 5 | 8 | real $x$ from its 7-point DFT? | DFT symmetry |
| 6 | 9 | CTFT, DTFT or DFT? | (a) [[problems/dtft-and-inverse-dtft\|DTFT]] · DFT |
| 7 | 14 | $A_1$, $A_2$, $\omega_0$ from two sinc DTFTs | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 8 | 15 | Nyquist rate; undersampled V spectrum | [[problems/sampling-and-the-nyquist-rate\|sampling]] |
| 9 | 12 | inputs giving $2\cos(300\pi t)$ | [[problems/sampling-and-the-nyquist-rate\|sampling]] |

### [[exams/midterm-2/past-exams/fall-2019|Fall 2019]]

| # | pts | asks | family |
|---|---|---|---|
| 1 | 20 | ten T/F: DTFT, DFT, circular convolution, FFT | DTFT · DFT |
| 2 | 6 | bins $k = 300, 800$ in Hz; spacing | spectral analysis |
| 3 | 9 | $X_d(0)$, $X_d(\pi)$, $\int X_d$ of 7 samples | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 4 | 5 | sequence with DFT $e^{-j\frac{\pi}{4}k}X[k]$ | circular shift |
| 5 | 8 | inverse DTFT of $e^{-j\omega/3}$ | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 6 | 5 | real $x * h$ with $X_d = e^{-j\omega^2/3}$? | [[problems/dtft-and-inverse-dtft\|DTFT]] |
| 7 | 10 | $1 + z^{-4}$ on $3 + 4\cos(\frac{\pi}{4}n) + e^{j\frac{\pi}{2}n}$ | [[problems/lti-response-to-sinusoids\|sinusoids]] |
| 8 | 10 | D/A of $\delta[n-3]$: ZOH, ideal | [[problems/sampling-and-the-nyquist-rate\|sampling]] |
| 9 | 15 | A/D → LPF → D/A: $H_a$, largest $T$ | [[problems/digital-filtering-of-analog-signals\|A/D–D/A]] |
| 10 | 4 | 32-point DIT FFT flow graph | FFT |
| 11 | 8 | zero-padding for DFT/FFT linear convolution | circular convolution |

## Key slips

Full list: [[0-toolkit/05-errata|errata]].
- **SP2025** #4: $H_d$ jumps at $\pm\pi$; key gives $j\pi(-1)^n$, the real system returns 0.
- **FA2024** #5(b): DTFT sketches on an $\Omega$ axis.
- **FA2023** #5: strict $T$ bounds boxed, equalities used; equality is fine.
- **SP2023** #5(a): exponent should be $-j3\omega$; boxed answer right.
- **FA2021** #5(b): $H_d(0)=H_a(0)=1$, not $0$.
- **FA2019** #8(b): sinc peak at $t=3T$, not $4T$. #10, #11: no key (solved on the page).

## Related
[[exams/midterm-2/index|Midterm 2 overview]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[problems/index|problem families]] · [[exams/midterm-1/past-exams/index|past Midterm 1 exams]] · [[exams/index|all exams]]

### Sources for this page
The seven past Midterm 2 exams with keys (FA2019–SP2025); the exam pages' problem maps.
