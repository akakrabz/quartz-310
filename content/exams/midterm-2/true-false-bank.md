---
title: "Midterm 2 True/False bank"
description: "All 43 True/False statements from the seven past ECE 310 Midterm 2 exams (FA2019–SP2025), grouped by topic, each with the official answer and a one-sentence reason folded away."
tags: [midterm-2, exam, problem-family, dtft]
family_frequency: "7 of 7 Midterm 2 exams"
typical_points: "10–20"
lectures: [13, 14, 15]
---

*Problem family · 7 of 7 past Midterm 2 exams, always problem 1 · 10–20 pts · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]]–[[3-fourier-analysis/15-frequency-response|L15]], [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]]–[[4-sampling-and-reconstruction/19-aliasing|L19]], [[5-dft-and-fft/20-discrete-fourier-transform|L20]]–[[5-dft-and-fft/23-spectral-analysis-and-window-functions|L23]] · 43 statements, 24 False*

> [!exam] How the problem looks
> Formats: 10 × 2 (FA2019), 5 × 3 (SP2021, FA2021), 5 × 2 (SP2023), 8 × 2 (FA2023), 4 × 3 with a ≤ 2-sentence reason (FA2024), 6 × 2 (SP2025). SP2023/SP2025 grade +2 / −1 / 0: a guess right with probability $p$ is worth $3p-1$.

## The counterexample kit

> [!key] Seven facts that decide most statements
> - **Every DTFT is $2\pi$-periodic**: $e^{-j(\omega+2\pi)n}=e^{-j\omega n}$.
> - **$X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ only if the ROC contains $\lvert z\rvert=1$** (counterexample $2^nu[n]$).
> - **Real $x[n]$ $\iff$ $X_d(-\omega)=X_d^*(\omega)$**; the cosine rule needs it.
> - **Only $e^{j\omega_0n}$ is an eigenfunction.**
> - **Appending zeros never changes the DTFT**; it refines the DFT grid.
> - **The inverse DFT is $N$-periodic in $n$** ([[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]]); the inverse DTFT of a finite sum is finite.
> - **An ideal D/A turns each sample into a sinc** ([[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Lecture 18]]).

## 1. The DTFT: existence, periodicity, uniqueness, symmetry

[[concepts/dtft|DTFT]] · [[concepts/dtft-properties|DTFT properties]]

**Q1** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(a) · A discrete-time signal $x[n]$ with z-transform $X(z)$ always has a finite DTFT $X_d(\omega)$ given by $X(z)$ evaluated at $z = e^{j\omega}$, i.e. evaluate $X(z)$ along the unit-circle.

> [!success]- Answer
> **False.** $x[n]=2^nu[n]$ has $X(z)=\dfrac{1}{1-2z^{-1}}$, $\lvert z\rvert\gt2$, but $\sum\lvert x[n]\rvert=\infty$: no DTFT.

**Q2** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(a) · The z-transform of $x[n] = 2^nu[n]$ is given by $X(z) = \dfrac{1}{1-2z^{-1}}$, $\lvert z\rvert \gt 2$. Therefore, the DTFT of $x[n]$ is given by $X_d(\omega) = \dfrac{1}{1-2e^{-j\omega}}$.

> [!success]- Answer
> **False.** The ROC $\lvert z\rvert\gt2$ misses the unit circle, so $z=e^{j\omega}$ may not be substituted.

**Q3** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(b) · The DTFT $X_d(\omega)$ of a finite-length signal $x[n]$ is $2\pi$-periodic.

> [!success]- Answer
> **True.** $e^{-j(\omega+2\pi)n}=e^{-j\omega n}$ for integer $n$.

**Q4** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(e) · The DTFT $X_d(\omega)$ of a discrete-time signal $x[n]$ is periodic only when $x[n]$ has infinite length.

> [!success]- Answer
> **False.** Periodicity comes from integer $n$, not from length (Q3).

**Q5** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(b) · Suppose that $x[n]$ is bandlimited to $\frac{\pi}{4}$. Then, its DTFT $X_d(\omega) = 0$ for $\lvert\omega\rvert \gt \frac{\pi}{4}$.

> [!success]- Answer
> **False.** $X_d(2\pi)=X_d(0)$; "bandlimited to $\frac{\pi}{4}$" means $X_d(\omega)=0$ for $\frac{\pi}{4}\lt\lvert\omega\rvert\le\pi$.

**Q6** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(c) · The DTFT of the finite-length signal $x[n] = \cos\left(\frac{\pi}{32}n\right)$, $n = 0, 1, \dots, 15$ is given by the formula $X_d(\omega) = \pi\left[\delta\left(\omega - \frac{\pi}{32}\right) + \delta\left(\omega + \frac{\pi}{32}\right)\right]$.

> [!success]- Answer
> **False.** Sixteen samples give two shifted Dirichlet kernels, nonzero almost everywhere; impulses need an endless cosine.

**Q7** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(a) · If $x[n]$ is the inverse DTFT of $X_d(\omega) = 1 + 2e^{-j\omega} + 3e^{-j2\omega} + 4e^{-j3\omega}$, then $x[n]$ must be zero for $n \lt 0$ and $n \gt 3$.

> [!success]- Answer
> **True.** By uniqueness and $\delta[n-n_0]\leftrightarrow e^{-j\omega n_0}$, $x=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4\}$ (contrast Q35).

**Q8** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(b) · Let $x[n]$ be a discrete-time signal with DTFT $X_d(\omega) = e^{-j\omega/2}$, $-\pi \le \omega \le \pi$. The corresponding signal $x[n] = \delta\big[n - \tfrac12\big]$.

> [!success]- Answer
> **False.** $x[n]=\dfrac{\sin\big(\pi(n-\frac12)\big)}{\pi(n-\frac12)}$, with $x[0]=x[1]=\frac{2}{\pi}$.

**Q9** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(c) · The DTFT of a real-valued signal is always Hermitian symmetric.

> [!success]- Answer
> **True.** $X_d(-\omega)=X_d^*(\omega)$: even magnitude, odd phase.

## 2. Frequency response and sinusoids

[[concepts/frequency-response|frequency response]] · [[problems/lti-response-to-sinusoids|LTI response to sinusoids]]

**Q10** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(d) · An LSI system has transfer function $H(z)$. Suppose that the output of the system to the input $x[n] = \cos(\omega_0 n + \phi)$ is $y[n] = \lvert H(e^{j\omega_0})\rvert\cos\left(\omega_0 n + \phi + \angle H(e^{j\omega_0})\right)$ for any $\omega_0, \phi$, where $H(e^{j\omega}) = H(z)\big|_{z=e^{j\omega}}$. Then, the system $h[n]$ can be either real or complex.

> [!success]- Answer
> **False.** Output $\tfrac12\big[H_d(\omega_0)e^{j(\omega_0n+\phi)}+H_d(-\omega_0)e^{-j(\omega_0n+\phi)}\big]$ matches for all $\omega_0,\phi$ only if $H_d(-\omega_0)=H_d^*(\omega_0)$, i.e. $h[n]$ **real**.

**Q11** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(a) · $x[n] = \cos(\omega_0 n)$ is an eigenfunction of a stable LTI system.

> [!success]- Answer
> **False.** A one-sample delay (stable) returns $\cos(\omega_0n-\omega_0)$.

## 3. Zero padding: the DTFT does not change

[[concepts/zero-padding|zero padding]] · [[problems/dft-values-and-zero-padding|DFT values and zero padding]]

**Q12** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(a) · Zero padding a finite-length signal can change its DTFT.

> [!success]- Answer
> **False.** Appended zeros contribute $0\cdot e^{-j\omega n}$; only the DFT changes.

**Q13** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(c) · Suppose $x[n]$ is a finite-length signal with DTFT $X_d(\omega)$. We zero-pad $x[n]$ with some number of zeros to obtain $y[n]$ with DTFT $Y_d(\omega)$. It follows then that $X_d(\omega) = Y_d(\omega)$.

> [!success]- Answer
> **True.** Same sum, same DTFT.

**Q14** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(f) · Let $\{x[n]\}_{n=0}^{N-1}$ be a length-$N$ signal with DTFT $X_d(\omega)$ and $\{y[n]\}_{n=0}^{M+N-1}$ be $x[n]$ zero-padded with $M$ zeros. The DTFT of $y[n]$ given by $Y_d(\omega)$ is equal to $X_d(\omega)$.

> [!success]- Answer
> **True.** As Q13.

**Q15** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(d) · Let $x[n]$ be a length-$N$ signal with DTFT $X_d(\omega)$. We zero-pad $x[n]$ to length-$3N$ to obtain $y[n]$ with DTFT $Y_d(\omega)$. We may say that $X_d(\omega) = Y_d(3\omega)$.

> [!success]- Answer
> **False.** $Y_d(\omega)=X_d(\omega)$; $X_d(3\omega)$ would be upsampling (zeros between samples).

**Q16** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(d) · A length-$N$ signal $x[n]$ with DTFT $X_d(\omega)$ and DFT $X[k]$ is zero-padded with $N$ zeros to length-$2N$ to form $y[n]$. Then, $X[k] = Y[2k]$ and $X_d(\omega) = Y_d(\omega)$. *(DFT half: [[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]])*

> [!success]- Answer
> **True.** $Y_d=X_d$ and $Y[2k]=X_d\big(\frac{2\pi\cdot2k}{2N}\big)=X_d\big(\frac{2\pi k}{N}\big)=X[k]$.

**Q17** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(d) · Assume $x[n]$ is a finite-duration sequence of length 20, and $y[n]$ is obtained by zero-padding $x[n]$ to length 32. That is, $y[n] = x[n]$, for $n = 0, 1, \dots, 19$, and $y[n] = 0$, $n = 20, 21, \dots, 31$. Let $\{X[m]\}_{m=0}^{19}$ and $\{Y[m]\}_{m=0}^{31}$ be the DFT of $\{x[n]\}_{n=0}^{19}$ and $\{y[n]\}_{n=0}^{31}$, respectively, then $X[10] = Y[16]$. *([[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]])*

> [!success]- Answer
> **True.** $X[10]=X_d\big(\frac{2\pi\cdot10}{20}\big)=X_d(\pi)=X_d\big(\frac{2\pi\cdot16}{32}\big)=Y[16]$.

## 4. Sampling and the Nyquist rate

[[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · [[problems/sampling-and-the-nyquist-rate|sampling and the Nyquist rate]]

**Q18** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(a) · By sampling a continuous-time signal $x_c(t) = \cos(17\pi t)$ with some sampling period $T$, it is possible to obtain a discrete time signal $x[n] = \cos(3\pi n/4)$.

> [!success]- Answer
> **True.** $T=\frac{3}{68}$ s gives $17\pi T=\frac{3\pi}{4}$.

**Q19** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(a) · By sampling a continuous-time signal $x_c(t) = \cos(\pi^3 t)$ with some sampling period $T$, it is possible to obtain a discrete time signal $x[n] = \cos(3\pi n/4)$.

> [!success]- Answer
> **True.** $T=\frac{3}{4\pi^2}$ s gives $\pi^3T=\frac{3\pi}{4}$.

**Q20** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(b) · If the Nyquist sampling rate for a continuous-time signal $x_c(t)$ is $F_s$, then the Nyquist sampling rate for $y_c(t) = x_c(2t)$ is $2F_s$.

> [!success]- Answer
> **True.** $x_c(2t)\leftrightarrow\frac12X_c(\Omega/2)$: highest frequency doubles.

**Q21** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(b) · If the Nyquist sampling rate for a continuous-time signal $x_c(t)$ is $F_s$, then the Nyquist sampling rate for $y_c(t) = x_c(3t)$ is $F_s/3$.

> [!success]- Answer
> **False.** The spectrum stretches by 3: $3F_s$.

**Q22** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(e) · If $x_c(t)$ is a bandlimited continuous-time signal, then there must exist a finite $\Omega_{\max}$ such that $X_a(\Omega) = 0$ for $\lvert\Omega\rvert \gt \Omega_{\max}$, where $X_a(\Omega)$ is the CTFT of $x_c(t)$.

> [!success]- Answer
> **True.** Definition of bandlimited.

**Q23** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(d) · Every continuous-time signal has a minimum sampling frequency to avoid aliasing during analog-to-digital conversion.

> [!success]- Answer
> **False.** Only bandlimited signals have a Nyquist rate; a rectangular pulse aliases at every rate.

**Q24** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(e) · Increasing the sampling period shrinks the corresponding DTFT.

> [!success]- Answer
> **False.** $\omega=\Omega T$: larger $T$ **stretches** the spectrum (key: "would be expanded"); only the height $\frac1T$ shrinks.

**Q25** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(d) · The value of $\int_3^{\infty}(t+1)\delta(t)\,dt$ is 0.

> [!success]- Answer
> **True.** The impulse at $t=0$ lies outside $[3,\infty)$.

## 5. Ideal D/A conversion and reconstruction

[[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Lecture 18]]: $x_a(t)=\sum_nx[n]\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right)$, $\mathrm{sinc}(t)=\frac{\sin t}{t}$.

**Q26** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(e) · A discrete-time signal is given by $x[n] = 4\delta[n-2]$. We pass $x[n]$ to an ideal D/A converter with sampling period $T$ to recover $x_a(t)$. The recovered continuous-time signal is given by $x_a(t) = 4\delta(n - 2T)$.

> [!success]- Answer
> **False.** $x_a(t)=4\,\dfrac{\sin\big(\pi(t-2T)/T\big)}{\pi(t-2T)/T}$ (the statement also mixes $n$ and $t$).

**Q27** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(c) · A discrete-time signal $x[n] = 2\delta[n-5]$ is passed to an ideal D/A converter with sampling period $T$ to recover $x_a(t)$. The recovered signal is given by $x_a(t) = 2\delta(t - 5T)$.

> [!success]- Answer
> **False.** $x_a(t)=2\,\dfrac{\sin\big(\pi(t-5T)/T\big)}{\pi(t-5T)/T}$: 2 at $t=5T$, 0 at other sample instants.

**Q28** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(c) · Let $x[n] = \delta[n-2] + 2\delta[n-4]$. We recover $x_a(t)$ by performing ideal digital-to-analog conversion with sampling period $T = 1$ s. Then, $x_a(t) = 0$ at $t = 3$ s.

> [!success]- Answer
> **True.** $x_a(t)=\mathrm{sinc}(\pi(t-2))+2\,\mathrm{sinc}(\pi(t-4))$ (course sinc) vanishes at $t=3$, matching $x[3]=0$.

**Q29** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(c) · The ideal reconstruction filter is causal.

> [!success]- Answer
> **False.** $\frac{\sin(\pi t/T)}{\pi t/T}$ is nonzero for $t\lt0$.

## 6. The DFT and its properties ([[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]], [[5-dft-and-fft/21-dft-properties|Lecture 21]])

[[concepts/dft|DFT]] · [[problems/dft-values-and-zero-padding|DFT values and zero padding]]

**Q30** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(i) · Let $\{x[n]\}_{n=0}^{5} = \{1, -1, -2, 3, 4, -3\}$. Consider the corresponding 6-point DFT $\{X[k]\}_{k=0}^{5}$. Then, $X[0] = 0$.

> [!success]- Answer
> **False.** $X[0]=\sum_nx[n]=2$.

**Q31** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(e) · Let $\{x[n]\}_{n=0}^{7} = \{1, -1, 6, 7, 9, -6, -7, 9\}$. Consider the corresponding 8-point DFT $\{X[k]\}_{k=0}^{7}$. Then, $X[0] = 0$.

> [!success]- Answer
> **False.** $X[0]=\sum_nx[n]=18$.

**Q32** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(c) · If $\{x[n]\}_{n=0}^{5}$ is real-valued and $\{X[k]\}_{k=0}^{5}$ is its DFT, then $X[0]$ is real-valued.

> [!success]- Answer
> **True.** $X[0]=\sum_nx[n]$ is real.

**Q33** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(b) · Two different sequences of same length can have the same DFT.

> [!success]- Answer
> **False.** The DFT is invertible.

**Q34** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(d) · If $x[n]$ is the inverse DFT of $\{1, 2, 3, 4\}$, then $x[n]$ must be zero for $n \lt 0$ or $n \gt 3$.

> [!success]- Answer
> **False.** $x[n]=\frac1N\sum_kX[k]e^{j\frac{2\pi}{N}kn}$ is $N$-periodic: $x[4]=x[0]=2.5$.

**Q35** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(b) · If $x[n]$ is the inverse DFT of $X[k] = \{1, 2, 3, 4\}$, $0 \le k \le 3$, then $x[n]$ must be zero for $n \lt 0$ and $n \gt 3$.

> [!success]- Answer
> **False.** As Q34; contrast Q7 (same numbers as a DTFT).

**Q36** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(h) · The DTFT and DFT of a length-14 sequence $x[n]$ are given by $X_d(\omega)$ and $X[k]$, respectively. We know then that $X[11] = X_d\left(-\tfrac{3\pi}{7}\right)$.

> [!success]- Answer
> **True.** $X[11]=X_d\big(\frac{11\pi}{7}\big)=X_d\big(\frac{11\pi}{7}-2\pi\big)=X_d\big(-\frac{3\pi}{7}\big)$.

## 7. Spectral analysis with the DFT ([[5-dft-and-fft/20-discrete-fourier-transform|Lecture 20]], [[5-dft-and-fft/22-spectral-analysis|Lecture 22]]–[[5-dft-and-fft/23-spectral-analysis-and-window-functions|Lecture 23]])

[[concepts/spectral-analysis|spectral analysis]] · [[problems/dft-spectral-analysis|DFT spectral analysis]]

**Q37** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(f) · The 64-point DFT of the finite-length signal $x[n] = \cos\left(\frac{\pi}{16}n\right)$, $0 \le n \le 63$ has only two nonzero elements.

> [!success]- Answer
> **True.** $\frac{\pi}{16}=\frac{2\pi\cdot2}{64}$: $X[2]=X[62]=32$, other 62 bins 0.

**Q38** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(g) · The DFT of $\{x[n]\}_{n=0}^{23} = \cos\left(\tfrac{\pi}{8}n\right)$ will only have two non-zero values.

> [!success]- Answer
> **False.** Period 16, 1.5 periods in 24 samples ($k=1.5$): leaks into all 24 bins.

**Q39** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(e) · An analog signal $x_a(t) = \cos(50\pi t)$ is sampled at $f_s = 50$ Hz for 1 second to obtain $\{x[n]\}_{n=0}^{49}$. The DFT of $x[n]$, $X[k]$, is non-zero for only one value of $k$ for $0 \le k \le 49$.

> [!success]- Answer
> **True.** $x[n]=\cos(\pi n)=(-1)^n=e^{j\frac{2\pi\cdot25}{50}n}$: $X[25]=50$, others 0.

**Q40** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(f) · Applying the Hamming window for spectral analysis leads to lower sidelobes and narrower main lobes in spectral components.

> [!success]- Answer
> **False.** Lower sidelobes (about $-42$ dB vs $-13$ dB) but a main lobe about **twice as wide**.

## 8. Circular convolution ([[5-dft-and-fft/21-dft-properties|Lecture 21]]) and the FFT (later)

[[concepts/circular-convolution|circular convolution]] · [[problems/circular-convolution-and-dft-properties|circular convolution and DFT properties]]

**Q41** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(g) · Linear convolution can be computed as a circular convolution via zero-padding.

> [!success]- Answer
> **True.** Pad both to $N\ge L_x+L_h-1$.

**Q42** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(h) · Circular convolution can be applied to two finite duration sequences with arbitrary lengths.

> [!success]- Answer
> **False** (key's answer). $N$-point circular convolution needs two length-$N$ sequences; pad first.

**Q43** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(j) · FFT is just an efficient algorithm to evaluate DFT.

> [!success]- Answer
> **True.** Same values in about $N\log_2N$ operations instead of $N^2$.

## 9. Patterns that recur

> [!key] Eight patterns
> 1. "DTFT is $X(e^{j\omega})$": check the ROC (Q1, Q2).
> 2. $2\pi$-periodicity (Q3–Q5, Q36).
> 3. Impulses need endless sinusoids (Q6); fractional delay is a sinc (Q8).
> 4. DTFT of a finite sum is finite (Q7); inverse DFT is periodic (Q34, Q35).
> 5. Real ⇔ Hermitian, licensing the cosine rule (Q9, Q10); cosines aren't eigenfunctions (Q11).
> 6. Zero padding never changes the DTFT (Q12–Q16), refines the DFT grid (Q16, Q17): most repeated idea.
> 7. $\omega=\Omega T$ mod $2\pi$ (Q18–Q24).
> 8. Ideal D/A gives sincs (Q26–Q29); a cosine's DFT is clean only for whole periods (Q37–Q39).

> [!trap] Where points actually go
> - Well-formed but wrong formulas (Q2, Q6); appending vs inserting zeros (Q15); "shrinks" read as height (Q24); blanks on +2/−1/0 exams.

## 10. Answers by exam

| exam, problem | answers in order | on this page |
|---|---|---|
| [[exams/midterm-2/past-exams/spring-2025\|SP2025 #1]] (12 pts, +2/−1/0) | T F T F T F | Q7, Q35, Q28, Q15, Q39, Q40 |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024 #1]] (12 pts, with reasons) | F T F T | Q2, Q3, Q27, Q16 |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023 #1]] (16 pts) | F F T F F T F T | Q1, Q8, Q9, Q23, Q26, Q14, Q38, Q36 |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #1]] (10 pts, +2/−1/0) | T F T F T | Q19, Q21, Q13, Q34, Q22 |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021 #1]] (15 pts) | F F F T F | Q11, Q33, Q29, Q17, Q24 |
| [[exams/midterm-2/past-exams/spring-2021\|SP2021 #1]] (15 pts) | T T T T F | Q18, Q20, Q32, Q25, Q31 |
| [[exams/midterm-2/past-exams/fall-2019\|FA2019 #1]] (20 pts) | F F F F F T T F F T | Q12, Q5, Q6, Q10, Q4, Q37, Q41, Q42, Q30, Q43 |

## Related

[[exams/midterm-2/index|Midterm 2 overview]] · [[exams/midterm-2/past-exams/index|past Midterm 2 exams]] · [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[exams/midterm-1/true-false-bank|Midterm 1 True/False bank]] · [[demos/practice-drills|practice drills]]

### Sources for this page

Official keys of ECE 310 Midterm 2 #1, FA2019–SP2025 (FA2019 handwritten); Lectures 13–21.
