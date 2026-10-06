---
title: "Past Midterm 2 exams"
description: "All seven past ECE 310 Midterm 2 exams (FA2019–SP2025) with typed problems and folded solutions: what each exam is good for, which problems belong to Unit 3 and can be used as self-tests now, the problem-by-problem map of all 62 problems with topic and problem family, and every slip found in the official keys."
tags: [exam, midterm-2]
---

*Seven past Midterm 2 exams, newest first · 62 problems, every one typed out with a folded solution, the traps that cost points, and the key's slips · every answer checked in Python · overview: [[exams/midterm-2/index|Midterm 2 overview]]*

> [!abstract] In one breath
> A past Midterm 2 is two hours (90–110 minutes in 2019–2021), 7–11 problems and 100 points, with handwritten sheets, no calculator and closed-form answers. Roughly a third of each exam (18–42 points) is Unit 3: True/False items on the DTFT, a DTFT or inverse DTFT, a magnitude/phase plot and a response to sinusoids. The rest is ideal filters, sampling and reconstruction, and the DFT, which come after Lecture 16. **Now:** use the Unit 3 problems listed below as self-tests. **Later:** take Spring 2025 and Fall 2024 whole, under exam conditions, and use the older exams as a problem bank.

## The seven exams

| exam | date | instructors | problems / points | Unit 3 points | format and notes | good for |
|---|---|---|---|---|---|---|
| [[exams/midterm-2/past-exams/spring-2025\|Spring 2025]] | Wed Apr 9, 2025, 7–9 pm | Liang, Snyder | 9 / 100 | 36 | two sheets; T/F +2/−1/0; key's #4 has an ambiguity at $\omega=\pi$ | the most recent Snyder exam: the first full timed run |
| [[exams/midterm-2/past-exams/fall-2024\|Fall 2024]] | Wed Nov 6, 2024, 7–9 pm | Do, Shomorony, Snyder | 9 / 100 | 41 | two sheets; T/F answers need a reason | a clean tour of Lectures 13–16 (#2–#4); the second full run |
| [[exams/midterm-2/past-exams/fall-2023\|Fall 2023]] | Wed Nov 1, 2023, 7–9 pm | Do, Snyder, Moustakides | 7 / 100 | 32 | two sheets; typed key, correct | #4: an even phase, so $h$ is complex |
| [[exams/midterm-2/past-exams/spring-2023\|Spring 2023]] | Wed Apr 5, 2023, 7–9 pm | Liang, Moon, Snyder | 10 / 100 | 35 | one sheet; T/F +2/−1/0; three cosmetic slips in the key | symmetry vs periodicity (#2–#3), a comb's phase (#5), a complex $H_d$ (#6) |
| [[exams/midterm-2/past-exams/fall-2021\|Fall 2021]] | Tue Nov 9, 2021, 8:30–10 pm | Zhao, Katselis, Kamalabadi | 7 / 100 | 18 | online, open notes, 90 min; one typo in the key (#5) | #2: a frequency response that needs impulses; sampling-heavy otherwise |
| [[exams/midterm-2/past-exams/spring-2021\|Spring 2021]] | Thu Apr 8, 2021, 7–8:50 pm | Moon, Katselis, Shomorony | 9 / 100 | 36 | online, one sheet | the most DTFT-heavy: #2, #3, #7 |
| [[exams/midterm-2/past-exams/fall-2019\|Fall 2019]] | Wed Nov 6, 2019, 7–8:30 pm | Kamalabadi, Katselis, Liang | 11 / 100 | 42 | two sheets, 90 min; the key strikes ZOH, circular convolution and FFT as "not on our Midterm 2" | eleven short problems touching every topic once |

"Unit 3 points" counts the problems on Lectures 13–16 plus the Unit 3 True/False parts, including the zero-padding statements (their DTFT half is a Unit 3 fact) and only part (a) of SP2021 #6; the exam pages, which file zero padding under the DFT, give 30, 38 and 34 for FA2023, FA2024 and SP2025 (counted in `verify/FAM_counts.py`). Older exams say **LSI** where the course now says **LTI**.

## How to use these exams

> [!tip] Now, with Unit 3 done
> 1. **Unit 3 self-test, timed (about 50 minutes):** SP2025 #2, #3, #4 and FA2024 #2, #3, #4: modulation, a magnitude/phase plot, a sinusoid response, an inverse DTFT. Use only a handwritten sheet. Grade with the folded solutions.
> 2. **Repair by family:** every lost point goes to [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]], [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] or [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]]: read the recipe and the traps, then do one practice problem.
> 3. **The rest of the Unit 3 problems as a bank:** FA2023 #2, #4; SP2023 #2–#6; FA2021 #2; SP2021 #2, #3, #7; FA2019 #3, #5, #6, #7.
> 4. **True/False:** the Unit 3 sections of the [[exams/midterm-2/true-false-bank|T/F bank]] (Q1–Q16), saying the reason out loud.
>
> **After Lectures 17+:** take SP2025, then FA2024, whole and timed (2 hours, your sheets, no calculator), and repair the same way. Use FA2023, SP2023 and the 2021 and 2019 exams by topic.

> [!trap] The Unit 3 traps that cost the most points
> - **Is $h$ real?** Check $H_d(-\omega)=H_d^*(\omega)$ before using the cosine shortcut: FA2024 #4 passes, SP2023 #6 and FA2023 #4 fail.
> - **The magnitude is never negative:** FA2024 #3 has $H_d(\frac{\pi}{2})=-1$, magnitude 1. And no extra $\pi$ when the real factor never goes negative (SP2025 #3).
> - **$X_d(\omega)=X(e^{j\omega})$ needs the unit circle in the ROC:** FA2023 #1(a), FA2024 #1(a), FA2021 #2.
> - **The $2\pi$ factors:** $\int X_d=2\pi x[0]$ (FA2019 #3), $\delta(\omega-\omega_0)\leftrightarrow\frac{1}{2\pi}e^{j\omega_0n}$ (SP2023 #4).
> - **Periodic copies wrap around $\pm\pi$** (SP2025 #2b), and every DTFT is $2\pi$-periodic (FA2019 #1(b), (e)).

## Problem by problem

Every problem of the seven exams, with its topic and, for Unit 3, its [[problems/index|problem family]] (the same maps open each exam page, with the lectures). Topics after Lecture 16 (ideal filters, sampling and reconstruction, A/D–$H_d$–D/A systems, the DFT, spectral analysis, circular convolution, the FFT) are Lectures 17+, notes coming.

### [[exams/midterm-2/past-exams/spring-2025|Spring 2025]]

| # | pts | what it asks | topic · problem family |
|---|---|---|---|
| 1 | 12 | six True/False statements (graded +2/−1/0): inverse DTFT, inverse DFT, ideal D/A, zero-padding, DFT of a sampled cosine, Hamming window | [[problems/dtft-and-inverse-dtft\|DTFTs]] · sampling, the DFT |
| 2 | 10 | sketch the DTFTs of $x[n]\cos(\frac{2\pi}{5}n)$ and $x[n]\cos^2(\frac{2\pi}{5}n)$ for an ideal low-pass $X_d$ | [[problems/dtft-and-inverse-dtft\|DTFTs]] (modulation) |
| 3 | 12 | $H_d$, $\lvert H_d\rvert$ and $\angle H_d$ for $y[n] = x[n] + 2x[n-3] + x[n-6]$ | [[problems/magnitude-phase-and-group-delay\|magnitude, phase]] |
| 4 | 10 | $H_d = j\omega e^{j\pi\sin\omega}$: output for $5 + 2e^{j\frac{\pi}{4}n} + \sin(\frac{\pi}{2}n + \frac{\pi}{4}) + (-1)^n$ | [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] |
| 5 | 16 | A/D → ideal LPF → D/A: sketch $X_d$, $Y_d$, $Y_a$; largest $T$ and $\omega_c$ to remove everything above 50 Hz | sampling and reconstruction · ideal filters |
| 6 | 12 | which sampling periods are consistent with given sinusoids; $T$ from an aliased output | sampling and aliasing |
| 7 | 12 | DFT of a length-8 signal: $X_0$; $y[n]$ from a permuted, sign-flipped DFT; zero-padding relations | DFT properties |
| 8 | 6 | $y[n]$ from $Y[m] = X[m]e^{j\frac{3\pi}{4}m}$ | DFT properties (circular shift) |
| 9 | 10 | DFT of 16 samples of $\cos(\frac{\pi}{2}n)$, with a sketch | spectral analysis with the DFT |

### [[exams/midterm-2/past-exams/fall-2024|Fall 2024]]

| # | pts | what it asks | topic · problem family |
|---|---|---|---|
| 1 | 12 | four True/False statements with reasons: DTFT existence, $2\pi$-periodicity, ideal D/A, zero-padding | [[problems/dtft-and-inverse-dtft\|DTFTs]] · sampling, the DFT |
| 2 | 8 | real $x[n]$ from a plotted ideal high-pass $X_d(\omega)$ | [[problems/dtft-and-inverse-dtft\|inverse DTFT]] · ideal filters |
| 3 | 12 | $H_d(0)$, $H_d(\frac{\pi}{2})$, $H_d(\pi)$ and a plot of $\lvert H_d\rvert$ for $h = \delta[n+2] + \delta[n] + \delta[n-2]$ | [[problems/magnitude-phase-and-group-delay\|magnitude, phase]] |
| 4 | 12 | $H_d = \lvert\omega\rvert e^{-j\pi\sin\omega}$: is $h$ real? output for $3 + \cos\frac{\pi n}{6} + j^n$ | [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] |
| 5 | 22 | triangle spectrum: Nyquist period; sketch $X_d$ and $Y_c$ at $T_N$ and $2T_N$; largest $T$ for a digital low-pass | sampling and reconstruction · ideal filters |
| 6 | 8 | which analog frequencies (Hz) land in DFT bin $k$ ($f_s = 1000$ Hz, $N = 1024$) | spectral analysis with the DFT |
| 7 | 6 | smallest $N$ whose DFT contains $X_d(\frac{2\pi}{5})$ and $X_d(\frac{\pi}{3})$ | the DFT |
| 8 | 8 | $Y[k]$ for a circularly reversed and shifted copy of $x[n]$ | DFT properties |
| 9 | 12 | $A_1$, $A_2$, $\Omega_1$, $\Omega_2$ of two cosines from a 32-point DFT plot | spectral analysis with the DFT |

### [[exams/midterm-2/past-exams/fall-2023|Fall 2023]]

| # | pts | what it asks | topic · problem family |
|---|---|---|---|
| 1 | 16 | eight True/False statements: DTFT existence, an inverse DTFT, Hermitian symmetry, Nyquist, ideal D/A, zero-padding, DFT leakage, DFT index ↔ DTFT frequency | [[problems/dtft-and-inverse-dtft\|DTFTs]] · sampling, the DFT |
| 2 | 6 | $X_d(0)$ and $X_d(\pi)$ of a 5-sample pulse | [[problems/dtft-and-inverse-dtft\|DTFTs]] |
| 3 | 6 | which $\Omega_0$ turn $\sin(\Omega_0t)$ sampled at 400 Hz into $\sin(\frac{\pi}{2}n)$ | sampling and aliasing |
| 4 | 18 | plot $\lvert H_d\rvert$ and $\angle H_d$ of $(\frac12 + \cos\omega)e^{j\lvert\omega\rvert}$; output for a constant + exponential + sine | [[problems/magnitude-phase-and-group-delay\|magnitude, phase]] · [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] |
| 5 | 20 | C/D → $H_d$ → D/C on a 10 kHz signal: largest $T$ and $H_d$ for a 5 kHz low-pass, then a high-pass | ideal filters · sampling and reconstruction |
| 6 | 16 | cosine of unknown frequency: estimate it from a 32-point DFT, bracket it, explain a 64-point plot | spectral analysis with the DFT |
| 7 | 18 | prove the DFT conjugation property; two real DFTs from one complex DFT | DFT properties |

### [[exams/midterm-2/past-exams/spring-2023|Spring 2023]]

| # | pts | what it asks | topic · problem family |
|---|---|---|---|
| 1 | 10 | five True/False statements (+2/−1/0) | T/F: sampling, Nyquist rate of $x_c(3t)$, zero padding, IDFT periodicity, bandlimited |
| 2 | 3 | $X_d$ of a **real** sequence on $[-\pi, 0]$, given $X_d = j\omega$ on $[0, \pi]$ | DTFT symmetry · [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 3 | 3 | same for an **arbitrary** sequence, on $[2\pi, 3\pi]$ | DTFT periodicity · [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 4 | 5 | inverse DTFT of $5e^{j\pi\omega}\delta(\omega - \omega_0)$ | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 5 | 14 | $H_d$ of $\delta[n] + \delta[n-6]$; plot magnitude and phase | [[problems/magnitude-phase-and-group-delay\|magnitude, phase and group delay]] |
| 6 | 8 | response of $H_d(\omega) = \omega e^{j\pi\cos\omega}$ to $3 + e^{j\frac{\pi}{3}n} + \sin(\frac{\pi}{2}n + \frac{\pi}{4})$ | [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] |
| 7 | 20 | ideal A/D → $H_d$ → ideal D/A: Nyquist rate; sketch $X_d$, $Y_d$ at two sampling rates | sampling · ideal filters · the A/D–$H_d$–D/A system |
| 8 | 10 | sampling periods consistent with a given $x[n]$ and a given $y_c(t)$ | sampling and reconstruction (aliasing) |
| 9 | 15 | $X_0$, $X_3$; $y[n]$ from a permuted DFT; zero-padding relations | the DFT and its properties |
| 10 | 12 | number, amplitudes and frequencies of cosines from a 24-point DFT plot | spectral analysis with the DFT |

### [[exams/midterm-2/past-exams/fall-2021|Fall 2021]]

| # | pts | what it asks | topic · problem family |
|---|---|---|---|
| 1 | 15 | five True/False statements | T/F: eigenfunctions, DFT uniqueness, ideal reconstruction, zero padding, sampling period |
| 2 | 15 | causal LCCDE: $H(z)$, $h[n]$, $H_d(\omega)$; why $H_d \ne H(e^{j\omega})$ | frequency response when the ROC misses $\lvert z\rvert = 1$ · [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 3 | 10 | 8-point DFT at even $k$; DFT of $x[\langle 3-n\rangle_8]\,j^n$ | the DFT and its properties |
| 4 | 15 | sampler → ideal highpass → ideal D/A at two rates: sketch $X_d$, $Y_d$, $Y_a$ | sampling · ideal filters · the A/D–$H_d$–D/A system |
| 5 | 15 | largest $T$ without aliasing; $H_d(\omega)$ that realises a given $H_a(\Omega)$ | the A/D–$H_d$–D/A system |
| 6 | 15 | linear vs 6-point circular convolution; is $N = 7$ enough? | linear vs circular convolution |
| 7 | 15 | DFT peaks of a sampled cosine: $L = 500$, then zero-padded to 1024 | spectral analysis with the DFT |

### [[exams/midterm-2/past-exams/spring-2021|Spring 2021]]

| # | pts | what it asks | topic · problem family |
|---|---|---|---|
| 1 | 15 | five True/False statements | T/F: sampling, Nyquist rate of $x_c(2t)$, DFT $X[0]$, an impulse integral |
| 2 | 10 | sketch magnitude and phase of $e^{-j4\omega}\sin 2\omega$ | [[problems/magnitude-phase-and-group-delay\|magnitude, phase and group delay]] |
| 3 | 9 | DTFT of $3\delta[n+1] - 3\delta[n-7]$ as $Ae^{-jB\omega}\sin(C\omega)$ | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 4 | 8 | the sequence whose 8-point DFT is $e^{-j(\frac{6\pi}{8}k+\pi)}X[k]$ | the DFT and its properties (circular shift) |
| 5 | 8 | is $x$ real, given its 7-point DFT? | the DFT and its properties (symmetry) |
| 6 | 9 | CTFT, DTFT or DFT: match three descriptions | DTFT vs DFT vs CTFT |
| 7 | 14 | $A_1$, $A_2$, $\omega_0$ from the DTFT of two sinc sequences | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] (ideal lowpass pair) |
| 8 | 15 | Nyquist rate; $X_d(\omega)$ after undersampling a V-shaped spectrum; is $x$ real? | sampling and aliasing |
| 9 | 12 | ideal A/D–D/A: $x[n]$ and the two inputs that give $2\cos(300\pi t)$ | sampling and reconstruction (aliasing) |

### [[exams/midterm-2/past-exams/fall-2019|Fall 2019]]

| # | pts | what it asks | topic · problem family |
|---|---|---|---|
| 1 | 20 | ten True/False statements | T/F: DTFT facts, DFT, circular convolution, FFT |
| 2 | 6 | DFT bins $k = 300, 800$ in hertz; bin spacing | spectral analysis with the DFT |
| 3 | 9 | $X_d(0)$, $X_d(\pi)$, $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$ of a 7-sample sequence | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 4 | 5 | the sequence whose 8-point DFT is $e^{-j\frac{\pi}{4}k}X[k]$ | the DFT and its properties (circular shift) |
| 5 | 8 | inverse DTFT of $e^{-j\omega/3}$, $\lvert\omega\rvert \le \pi$, with no complex numbers | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 6 | 5 | can $x * h$ be real when $X_d(\omega) = e^{-j\omega^2/3}$? | DTFT symmetry · [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 7 | 10 | response of $H(z) = 1 + z^{-4}$ to $3 + 4\cos(\frac{\pi}{4}n) + e^{j\frac{\pi}{2}n}$ | [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] |
| 8 | 10 | D/A output for $\delta[n-3]$: ZOH and ideal | sampling and reconstruction (D/A, ZOH) |
| 9 | 15 | A/D → ideal lowpass → D/A: Nyquist interval, overall $H_a(\Omega)$, largest $T$ that keeps it LTI | sampling · ideal filters · the A/D–$H_d$–D/A system |
| 10 | 4 | indices and branch weights in a 32-point DIT FFT flow graph | the FFT |
| 11 | 8 | zeros to pad for DFT- and FFT-based linear convolution | linear vs circular convolution · FFT |

## Answer-key slips at a glance

The official keys are mostly right; where they are not, the exam page says so in a warning box. Full list with the lecture-note typos: [[0-toolkit/05-errata|errata]].

- **Spring 2025** #4: $H_d=j\omega e^{j\pi\sin\omega}$ jumps from $-j\pi$ to $j\pi$ across $\omega=\pm\pi$, so the response to $(-1)^n$ is ambiguous; the key evaluates at $+\pi$ and gets $j\pi(-1)^n$, but $h$ and $(-1)^n$ are real, and the actual system returns 0 (the midpoint).
- **Fall 2024** #5(b): the DTFT sketches are labelled $X_d(\Omega)$ over an $\Omega$ axis (a DTFT is a function of $\omega$); shapes and heights are right. The key writes $\mathrm{sinc}\,x=\frac{\sin x}{x}$ (#1(c)), unlike the course tables.
- **Fall 2023** #5: boxes $T\lt\frac{1}{15000}$ s and $T\lt\frac{1}{20000}$ s (strict), then uses the equalities as the largest periods; equality is fine.
- **Spring 2023** #5(a): the middle line reads $e^{-j3\omega}(e^{j3\omega}+e^{j3\omega})$ (the second exponent should be $-j3\omega$) and sums $x[n]$ for $h[n]$; the boxed answer is right. Cosmetic: a tick at $-\frac{\pi}{2}$ labelled $\frac{\pi}{2}$ in #7(b); subscripts not advanced in #10.
- **Fall 2021** #5(b): the text says "$H_d(0)=0$"; it is $H_d(0)=H_a(0)=1$, as the key's own formula and plot show.
- **Spring 2021** #8: cosmetic, the figure labels the copies $X_c(\Omega/F_s\pm2\pi)$, mixing $\Omega$ and $\omega$.
- **Fall 2019** #8(b): the sketch centres the reconstructed sinc at $t=4T$; for $\delta[n-3]$ the peak is at $t=3T$. #10 and #11 have no key answers (solved on the exam page).

## Related

- [[exams/midterm-2/index|Midterm 2 overview]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[demos/practice-drills|practice drills]] · [[demos/frequency-response-explorer|frequency-response explorer]]
- [[problems/index|Problem families]] · [[3-fourier-analysis/index|Unit 3]] · [[homework/index|homework]] · [[exams/midterm-1/past-exams/index|past Midterm 1 exams]] · [[exams/index|all exams]]

### Sources for this page

- The seven past Midterm 2 exams with their solution keys (FA2019, SP2021, FA2021, SP2023, FA2023, FA2024, SP2025), headers read for dates, instructors, rules and point values; the exam pages of this site, whose "Map of the exam" tables are reproduced in the problem-by-problem section.
- The problem maps `verify/E1_map.json` and `verify/E2_map.json` (topics, points, key slips); counts and the Unit 3 share in `verify/FAM_counts.py`.
