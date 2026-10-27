---
title: "DFT spectral analysis"
description: "Midterm 2 spectral-analysis problems: the DFT of a finite cosine (clean bins or leakage), amplitudes and frequencies from a DFT plot, bins in hertz, zero padding, lobe-separation criteria, rectangular vs Hamming windows."
tags: [problem-family, problem, dft, spectral-analysis, midterm-2]
family_frequency: "6 of 7 Midterm 2 exams"
typical_points: "10–16"
lectures: [22, 23]
---

*Problem family · six of seven past Midterm 2 exams (not SP2021) · one 10–16-point problem plus True/False items · [[5-dft-and-fft/22-spectral-analysis|Lecture 22]], [[5-dft-and-fft/23-spectral-analysis-and-window-functions|Lecture 23]] · in the course: Lecture 22 Examples 1–2, Lecture 23 Example 1*

## What it looks like on the exam

- **A** DFT of $N$ samples of a cosine: two bins of height $\frac{AN}{2}$, or leakage everywhere; sketch it.
- **B** Read a DFT plot: how many cosines, their amplitudes $A_m=\frac{2\lvert X[k_m]\rvert}{N}$, their frequencies $\Omega_m=\frac{2\pi k_m}{N}f_s$.
- **C** Unknown frequency between bins: estimate, bracket, and explain a zero-padded plot.
- **D** Where the peaks land before and after padding; smallest $N$ to separate two tones; which window.
- **E** True/False: whole periods, Hamming window, impulses vs lobes.

Exams write $\lambda_0$ or $\omega_0$ for the digital frequency, $x_c(t)$, $\Omega$ in rad/s.

| instance | given → asked |
|---|---|
| [[exams/midterm-2/past-exams/fall-2019\|FA2019]] #1(c), (f) | T/F: DTFT of 16 samples of $\cos(\frac{\pi}{32}n)$ is two impulses? 64-point DFT of $\cos(\frac{\pi}{16}n)$ has two nonzero bins? |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021]] #7 | $\cos(10\pi t)$ at 100 Hz for 5 s ($L=500$) → bins of the largest $\lvert X[k]\rvert$; after padding to $N=1024$ |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023]] #10 | 24-point $\lvert X[k]\rvert$ plot, $T=\frac{1}{12000}$ s, peaks 6, 12, 9 at $k=1,6,9$ (and mirrors) → $M$, $A_m$, $\Omega_m$ |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023]] #6 | 32-point DFT of $\cos(\lambda_0n)$, tallest bin $k=7$, $\lvert X[8]\rvert\gt\lvert X[6]\rvert$ → estimate $\lambda_0$; tightest $[a,b]$; what made a 64-point plot |
| FA2023 #1(g) | T/F: 24 samples of $\cos(\frac{\pi}{8}n)$: only two nonzero DFT values? |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024]] #9 | $A_1\cos\Omega_1t+A_2\cos\Omega_2t$ at 64 Hz for 0.5 s; 32-point plot with 48 at $k=3$, 32 at $k=8$ → $A_1,A_2,\Omega_1,\Omega_2$ |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025]] #9 | $\{\cos(\frac{\pi}{2}n)\}_{n=0}^{15}$ → DFT, sketched |
| SP2025 #1(e), (f) | T/F: $\cos(50\pi t)$ at 50 Hz for 1 s: one nonzero bin? Hamming: lower sidelobes and narrower main lobe? |
| course | L22 Example 1: $\omega_0$, $N$, $A$ from a $\lvert X_d\rvert$ plot · Example 2: $\sin(\frac{\pi}{11}n)$, $N=33$; $\sin(\frac{3\pi}{5}n)$, $N=20$; $\cos(\frac{\pi}{4}n)+\cos(\frac{\pi}{3}n)$, $N=48$: two or four nonzero bins? · L23 Example 1: guitar notes 82 and 87 Hz at 8 kHz, full-lobe $N$ and time · bins in hertz: [[problems/dft-values-and-zero-padding\|DFT values family]] · [[exams/midterm-2/true-false-bank\|T/F bank]] Q37–Q40 |

> [!success]- Answers
> | instance | answer |
> |---|---|
> | FA2019 #1 | (c) F: a finite cosine gives two periodic sincs, nonzero almost everywhere. (f) T: $\frac{\pi}{16}=\frac{2\pi\cdot2}{64}$, $X[2]=X[62]=32$ |
> | FA2021 #7 | $\omega_0=\frac{\pi}{10}$. (a) $\frac{2\pi k}{500}=\frac{\pi}{10}$: $k=25$ and $475$ ($\lvert X\rvert=250$, rest 0). (b) $k=51.2$: nearest $k=51$ and $973$ ($\lvert X[51]\rvert\approx245.6$) |
> | SP2023 #10 | $\frac{AN}{2}=12A$: $M=3$; $A=\frac12,1,\frac34$; $\Omega=\frac{2\pi k}{24}\cdot12000=1000\pi k$: $1000\pi$, $6000\pi$, $9000\pi$ rad/s |
> | FA2023 #6 | (a) $\lambda_0\approx\frac{2\pi\cdot7}{32}=\frac{7\pi}{16}$. (b) centre between bins 7 and 7.5: $\frac{7\pi}{16}\le\lambda_0\le\frac{15\pi}{32}$. (c) zero-padded to 64: even bins equal the old ones, odd bins are new samples of the same DTFT |
> | FA2023 #1(g) | F: period 16, 1.5 periods in 24 samples ($k=1.5$): all 24 bins nonzero |
> | FA2024 #9 | $N=32$, $\Omega=\frac{2\pi k}{32}\cdot64=4\pi k$; height $16A$: $A_1=3$, $A_2=2$, $\Omega_1=12\pi$, $\Omega_2=32\pi$ rad/s |
> | SP2025 #9 | $\frac{\pi}{2}=\frac{2\pi\cdot4}{16}$: $X[4]=X[12]=8$, other bins 0 |
> | SP2025 #1 | (e) T: $\cos(\pi n)=(-1)^n$, $X[25]=50$ only. (f) F: sidelobes $-42$ vs $-13$ dB, main lobe twice as wide |
> | course | L22 Ex. 1: main lobe $\frac{4\pi}{N}=\frac{\pi}{4}$ gives $N=16$, height $\frac{AN}{2}=64$ gives $A=8$ · Ex. 2: $k_0=\frac{\omega_0N}{2\pi}=1.5$ (leaks, 33 nonzero); $6$ (two bins, $\mp10j$); $6$ and $8$ (four bins, height 24) · L23 Ex. 1: $N\gt\frac{4\pi}{2\pi\cdot5/8000}=3200$, $0.4$ s; doubling $f_s$ doubles $N$, same $0.4$ s |

## The recipe

> [!recipe] Finite cosine, DFT plot, resolution
> $$
> \begin{gathered}
> x[n]=A\cos(\omega_0n),\ 0\le n\le N-1\quad\Longrightarrow\\
> X_d(\omega)=\tfrac A2C(\omega-\omega_0)+\tfrac A2C(\omega+\omega_0),\\
> C(\omega)=e^{-j\frac{\omega}{2}(N-1)}\,\frac{\sin(\frac N2\omega)}{\sin(\frac12\omega)},\qquad C(0)=N,\qquad X[k]=X_d\!\left(\tfrac{2\pi k}{N}\right).
> \end{gathered}
> $$
> $C$ is zero at every nonzero multiple of $\frac{2\pi}{N}$; main lobe width $\frac{4\pi}{N}$.
> 1. **Bins ↔ frequencies.** $\omega_k=\frac{2\pi k}{N}$, $f_k=\frac{kf_s}{N}$, $\Omega_k=2\pi f_k$; a tone at $\omega_0$ sits at $k_0=\frac{\omega_0N}{2\pi}=\frac{f_0N}{f_s}$ (cycles in the record), mirror at $N-k_0$; the record lasts $\frac N{f_s}$ s.
> 2. **Whole periods or leakage.** $k_0$ integer: the bins hit both lobe peaks and every zero, so exactly two nonzero bins, $X[k_0]=X[N-k_0]=\frac{AN}{2}$ (sine: $\mp j\frac{AN}{2}$; $\omega_0=\pi$: one bin, $AN$). Otherwise every bin is nonzero, tallest at the nearest integers, below $\frac{AN}{2}$.
> 3. **Read a plot.** Mirror pairs in $0\lt k\lt\frac N2$ count $M$; $A_m=\frac{2\lvert X[k_m]\rvert}{N}$; $\Omega_m=\frac{2\pi k_m}{N}f_s$ rad/s; check $f_m\lt\frac{f_s}{2}$.
> 4. **Between bins.** $\omega_0\approx\omega_{k^*}$ at the tallest bin; the taller neighbour gives the side, and the tallest bin keeps the centre within half a bin: $\frac{2\pi k^*}{N}\le\omega_0\le\frac{2\pi(k^*+\frac12)}{N}$. Two equally tall bins: halfway.
> 5. **Zero padding** to $M$ points samples the same $X_d$ at $\frac{2\pi k}{M}$: old bins reappear at $k\frac MN$, lobes keep width $\frac{4\pi}{N}$, the peak stays below $\frac{AN}{2}$ unless a bin lands on $\omega_0$. It never separates two tones.
> 6. **Resolution and windows.** Full-lobe $N\gt\frac{4\pi}{\Delta\omega}=\frac{2f_s}{\Delta f}$, half-lobe $N\gt\frac{2\pi}{\Delta\omega}=\frac{f_s}{\Delta f}$; the time $\frac N{f_s}$ is independent of $f_s$. Rectangular: main lobe $\frac{4\pi}{N}$, sidelobes $-13$ dB. Hamming $0.54-0.46\cos\frac{2\pi n}{N-1}$: $\frac{8\pi}{N}$ and $-42$ dB, for a much weaker second tone, at twice the $N$.

> [!trap] Where the points go
> - **Height is $\frac{AN}{2}$**, not $A$ or $AN$ (FA2024 #9, SP2023 #10); the mirror is at $N-k_0$, not $-k_0$ (SP2025 #9).
> - **A fraction of a period leaks everywhere.** $\cos(\frac{\pi}{8}n)$, 24 samples: 1.5 periods (FA2023 #1(g)); but $\cos(\pi n)=(-1)^n$ is one bin, $k=\frac N2$ (SP2025 #1(e)).
> - **Padding refines the grid, not the resolution.** Lobes keep width $\frac{4\pi}{N}$; the peak drops from 250 to about 245.6 (FA2021 #7(b), FA2023 #6(c)).
> - **Hamming trades width for sidelobes**: lower sidelobes and a wider main lobe (SP2025 #1(f)).
> - **Units and grid.** $\omega_k=\frac{2\pi k}{N}$, not $\frac{\pi k}{N}$ or $\frac{2\pi k}{N-1}$; answer in the units asked ($12\pi$ rad/s, not 6 Hz or $\frac{3\pi}{16}$) (FA2023 #6(a), FA2024 #9).

## Practice problems

> [!question] Practice 1 — two tones, two record lengths
> $x_c(t)=3\cos(2\pi\cdot250t)+\cos(2\pi\cdot1000t)$ is sampled at $f_s=4$ kHz. (a) With $N=64$ samples: the digital frequencies and the bins $k_0$ of both tones. (b) The 64-point DFT. (c) With $N=60$ instead: which tone still gives clean bins, and is the 1 kHz bin still $\frac{AN}{2}$? (d) Hertz per bin at $N=64$.

> [!success]- Solution
> **(a)** $\omega=\frac{2\pi f}{f_s}$: $\frac{\pi}{8}$ and $\frac{\pi}{2}$; $k_0=\frac{\omega_0N}{2\pi}=4$ and $16$: whole periods (4 and 16 cycles).
> **(b)** $X[4]=X[60]=\frac{3\cdot64}{2}=96$, $X[16]=X[48]=\frac{64}{2}=32$, all other bins 0.
> **(c)** $k_0=\frac{60}{16}=3.75$ (leaks: $\lvert X[4]\rvert\approx82.1$, $\lvert X[3]\rvert\approx26.0$, not 90) and $k_0=15$ (whole). Bin 15 is no longer clean: the 1 kHz tone contributes exactly 30, the leaking 250 Hz tone adds $\frac32C(\frac{\pi}{2}-\frac{\pi}{8})+\frac32C(\frac{\pi}{2}+\frac{\pi}{8})\approx2.12-1.62j$, so $\lvert X[15]\rvert\approx32.2$; every one of the 60 bins is nonzero.
> **(d)** $\frac{f_s}{N}=62.5$ Hz per bin: 250 Hz is bin 4, 1 kHz bin 16.

> [!question] Practice 2 — how long to record?
> Two equal-amplitude tones at 440 Hz and 466 Hz, $f_s=8$ kHz. (a) Samples and seconds for full-lobe separation. (b) For half-lobe separation. (c) A 128-sample record is zero-padded to 4096 points: are the tones separated? (d) Repeat (a) at $f_s=16$ kHz. (e) The 466 Hz tone is 20 times weaker than the other: which window, and how many samples for full-lobe separation then?

> [!success]- Solution
> $\Delta\omega=\frac{2\pi\cdot26}{8000}$.
> **(a)** $N\gt\frac{4\pi}{\Delta\omega}=\frac{2\cdot8000}{26}=615.4$: $N=616$ samples, $\frac{616}{8000}=77$ ms.
> **(b)** $N\gt\frac{2\pi}{\Delta\omega}=307.7$: $308$ samples, $38.5$ ms.
> **(c)** No. Half-width $\frac{2\pi}{128}$ is $62.5$ Hz, more than the 26 Hz spacing: the two main lobes merge into one lobe (its peak near 453 Hz), and padding only samples that same DTFT more finely.
> **(d)** $\Delta\omega$ halves, so $N\gt1230.8$: $1231$ samples, still $77$ ms: $\frac N{f_s}\gt\frac{2}{\Delta f}$ regardless of $f_s$.
> **(e)** Hamming: rectangular sidelobes ($-13$ dB, about $0.22$) would bury a tone at $0.05$. Main lobe $\frac{8\pi}{N}$, so $N\gt\frac{8\pi}{\Delta\omega}=1230.8$: $1231$ samples, $154$ ms.

> [!question] Practice 3 — a leaky peak
> $x[n]=\cos(\omega_0n)$, $0\le n\le39$. The 40-point DFT has its tallest bin at $k=9$ with $\lvert X[9]\rvert=19.0$, and $\lvert X[10]\rvert=4.39\gt\lvert X[8]\rvert=3.42$. (a) Estimate $\omega_0$. (b) The tightest interval for $\omega_0$. (c) The record is padded to 80 points: which bins repeat the old values, and can the new peak reach 20? (d) With the true $\omega_0=0.46\pi$ and 50 samples instead, what would the two tallest bins look like?

> [!success]- Solution
> **(a)** $\omega_0\approx\frac{2\pi\cdot9}{40}=0.45\pi$.
> **(b)** Bin 10 taller than bin 8: centre above bin 9; bin 9 tallest: within half a bin. $0.45\pi\le\omega_0\le\frac{2\pi\cdot9.5}{40}=0.475\pi$. (The record was made with $\omega_0=0.46\pi$, $k_0=9.2$.)
> **(c)** $\tilde X[2k]=X[k]$; odd bins are new. $k_0$ becomes $18.4$, still off-grid: the tallest bins are $\lvert\tilde X[18]\rvert=19.0$ (old bin 9) and $\lvert\tilde X[19]\rvert\approx17.6$; nothing reaches $\frac N2=20$.
> **(d)** $k_0=\frac{0.46\pi\cdot50}{2\pi}=11.5$: two nearly equal bins, $\lvert X[11]\rvert\approx\lvert X[12]\rvert\approx\frac12\lvert C(0.02\pi)\rvert\approx15.9$ (15.86 and 15.99 with the mirror lobe), well below 25.

## Related

[[concepts/spectral-analysis|Spectral analysis]] · [[concepts/periodic-sinc|periodic sinc]] · [[concepts/spectral-leakage|spectral leakage]] · [[concepts/frequency-resolution|frequency resolution]] · [[concepts/window-functions|window functions]] · [[concepts/zero-padding|zero padding]] · [[concepts/dft|DFT]] · [[problems/dft-values-and-zero-padding|DFT values and zero padding]] · [[problems/sampling-and-the-nyquist-rate|sampling and the Nyquist rate]] · [[exams/midterm-2/index|Midterm 2]]

### Sources for this page

Lecture 22 notes (eqs. 8–12, Fig. 2–3) and slides (Examples 1–2); Lecture 23 notes (eqs. 8–10, 20–21, Exercise 1) and slides 7–13; past Midterm 2 exams FA2019–SP2025 with keys. Practice problems are new (verified numerically).
