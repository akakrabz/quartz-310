---
title: "Midterm 2 True/False bank"
description: "All 43 True/False statements from the seven past ECE 310 Midterm 2 exams (FA2019–SP2025), grouped by topic, with the official answer and a one-to-two-sentence reason folded away for self-testing; the 16 statements on Unit 3 (DTFT, frequency response, zero padding and the DTFT) come first, the 27 on later topics (sampling, ideal D/A, the DFT, the FFT) are marked as such."
tags: [midterm-2, exam, problem-family, dtft]
family_frequency: "7 of 7 Midterm 2 exams"
typical_points: "10–20"
lectures: [13, 14, 15]
---

*Problem family · on 7 of 7 past Midterm 2 exams, always problem 1 · 10–20 pts (FA2019: 20; SP2021, FA2021: 15; FA2023: 16; FA2024, SP2025: 12; SP2023: 10) · Unit 3: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]], [[3-fourier-analysis/15-frequency-response|Lecture 15]] · later topics: Lectures 17+ (notes coming) · 43 statements, 24 of them False*

> [!abstract] How to use this page
> Every statement is typed as it appeared on the exam, with its source linked. Say **True** or **False** out loud, *then* open the folded **Answer**: it holds the official answer and a short reason, usually a counterexample or a one-line calculation. Sections 1–3 hold the 16 statements on [[3-fourier-analysis/index|Unit 3]] (Q1–Q16, plus Q17, a DFT statement tagged *(later)* that sits beside its zero-padding twins) and can be used now; sections 4–8 test **later topics** (sampling, ideal D/A conversion, the DFT, the FFT) that come after Lecture 16. Each of those carries a *(later)* tag: read them now as a preview, and come back after the lectures.

> [!exam] How the problem looks
> Always problem 1, and on Midterm 2 it leans on the newest material: of the 43 statements only 16 are about the DTFT and frequency response. Formats: ten × 2 pts (FA2019), five × 3 pts (SP2021, FA2021), five × 2 pts (SP2023), eight × 2 pts (FA2023), four × 3 pts **with a reason of at most two sentences** (FA2024), six × 2 pts (SP2025). SP2023 and SP2025 print the rule **+2 correct, −1 wrong, 0 blank**; a guess that is right with probability $p$ is then worth $3p-1$ points, so a coin flip ($+0.5$) still beats a blank, and only a guess worse than one-in-three should be left empty.

## The counterexample kit

Most Midterm 2 statements are decided by one of a handful of facts. Keep them on your sheet:

> [!key] Seven facts that decide most statements
> - **Every DTFT is $2\pi$-periodic**, finite signal or not: $e^{-j(\omega+2\pi)n}=e^{-j\omega n}$ for integer $n$. "Zero for $\lvert\omega\rvert\gt\frac{\pi}{4}$" is therefore impossible unless $X_d\equiv0$.
> - **$X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ only when the ROC contains $\lvert z\rvert=1$.** The standing counterexample is $2^nu[n]$ (ROC $\lvert z\rvert\gt2$, no DTFT).
> - **Real $x[n]$ $\iff$ $X_d(-\omega)=X_d^*(\omega)$** (even magnitude, odd phase). The cosine rule $\cos\to\lvert H_d\rvert\cos(\cdot+\angle H_d)$ needs exactly this.
> - **Only $e^{j\omega_0n}$ is an eigenfunction**; a cosine is a sum of two, scaled by $H_d(\omega_0)$ and $H_d(-\omega_0)$.
> - **Appending zeros never changes the DTFT**; it only gives the DFT a finer grid of samples of the same $X_d$.
> - *(later)* **The inverse DFT is $N$-periodic in $n$; the inverse DTFT of a finite sum is finite.**
> - *(later)* **An ideal D/A turns each sample into a sinc**, never into an impulse.

## 1. The DTFT: existence, periodicity, uniqueness, symmetry

The definition and its first consequences. See [[concepts/dtft|DTFT]], [[concepts/dtft-properties|DTFT properties]], [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]].

**Q1** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(a) · A discrete-time signal $x[n]$ with z-transform $X(z)$ always has a finite DTFT $X_d(\omega)$ given by $X(z)$ evaluated at $z = e^{j\omega}$, i.e. evaluate $X(z)$ along the unit-circle.

> [!success]- Answer
> **False.** Only when the ROC contains the unit circle. $x[n]=2^nu[n]$ has $X(z)=\dfrac{1}{1-2z^{-1}}$, $\lvert z\rvert\gt2$, but no DTFT: $\sum\lvert x[n]\rvert=\infty$.

**Q2** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(a) · The z-transform of $x[n] = 2^nu[n]$ is given by $X(z) = \dfrac{1}{1-2z^{-1}}$, $\lvert z\rvert \gt 2$. Therefore, the DTFT of $x[n]$ is given by $X_d(\omega) = \dfrac{1}{1-2e^{-j\omega}}$.

> [!success]- Answer
> **False.** The ROC $\lvert z\rvert\gt2$ misses the unit circle, so $z=e^{j\omega}$ may not be substituted; $2^nu[n]$ is not absolutely summable and has no DTFT. (FA2024 asked for the reason: one sentence about the ROC is enough.)

**Q3** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(b) · The DTFT $X_d(\omega)$ of a finite-length signal $x[n]$ is $2\pi$-periodic.

> [!success]- Answer
> **True.** Every DTFT is $2\pi$-periodic, since $e^{-j(\omega+2\pi)n}=e^{-j\omega n}$ for integer $n$. Finite length only guarantees that the DTFT exists.

**Q4** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(e) · The DTFT $X_d(\omega)$ of a discrete-time signal $x[n]$ is periodic only when $x[n]$ has infinite length.

> [!success]- Answer
> **False.** Same fact as Q3, read the other way: periodicity comes from $n$ being an integer, not from the length of $x$.

**Q5** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(b) · Suppose that $x[n]$ is bandlimited to $\frac{\pi}{4}$. Then, its DTFT $X_d(\omega) = 0$ for $\lvert\omega\rvert \gt \frac{\pi}{4}$.

> [!success]- Answer
> **False.** $X_d(\omega+2\pi)=X_d(\omega)$, so whatever lies in $\lvert\omega\rvert\lt\frac{\pi}{4}$ reappears near $\pm2\pi$, where $\lvert\omega\rvert\gt\frac{\pi}{4}$ (for example $X_d(2\pi)=X_d(0)$). "Bandlimited to $\frac{\pi}{4}$" means $X_d(\omega)=0$ for $\frac{\pi}{4}\lt\lvert\omega\rvert\le\pi$; the copies near $\pm2\pi$ are always there.

**Q6** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(c) · The DTFT of the finite-length signal $x[n] = \cos\left(\frac{\pi}{32}n\right)$, $n = 0, 1, \dots, 15$ is given by the formula $X_d(\omega) = \pi\left[\delta\left(\omega - \frac{\pi}{32}\right) + \delta\left(\omega + \frac{\pi}{32}\right)\right]$.

> [!success]- Answer
> **False.** Impulses belong to a cosine that lasts forever (and the pair would need $2\pi$-periodic copies too). Sixteen samples give a finite sum: two shifted Dirichlet kernels, smooth and nonzero almost everywhere.

**Q7** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(a) · If $x[n]$ is the inverse DTFT of $X_d(\omega) = 1 + 2e^{-j\omega} + 3e^{-j2\omega} + 4e^{-j3\omega}$, then $x[n]$ must be zero for $n \lt 0$ and $n \gt 3$.

> [!success]- Answer
> **True.** The DTFT is unique, and $\delta[n-n_0]\leftrightarrow e^{-j\omega n_0}$ reads off $x=\{\underset{\uparrow}{1},\ 2,\ 3,\ 4\}$, zero everywhere else. Contrast Q35, the same numbers as a DFT.

**Q8** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(b) · Let $x[n]$ be a discrete-time signal with DTFT $X_d(\omega) = e^{-j\omega/2}$, $-\pi \le \omega \le \pi$. The corresponding signal $x[n] = \delta\big[n - \tfrac12\big]$.

> [!success]- Answer
> **False.** $n$ is an integer, so $\delta[n-\frac12]$ is not a signal. The inverse DTFT is $x[n]=\dfrac{\sin\big(\pi(n-\frac12)\big)}{\pi(n-\frac12)}$, a sinc sampled half-way between its zeros ($x[0]=x[1]=\frac{2}{\pi}$). [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #5 asks for the same thing with a delay of $\frac13$.

**Q9** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(c) · The DTFT of a real-valued signal is always Hermitian symmetric.

> [!success]- Answer
> **True.** $x$ real $\Rightarrow$ $X_d(-\omega)=X_d^*(\omega)$: even magnitude, odd phase ([[3-fourier-analysis/14-dtft-properties|Lecture 14]]).

## 2. Frequency response and sinusoids

What an LTI system does to a sinusoid, and when the real-system shortcut is allowed. See [[concepts/frequency-response|frequency response]], [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]], [[3-fourier-analysis/15-frequency-response|Lecture 15]], and the family [[problems/lti-response-to-sinusoids|LTI response to sinusoids]].

**Q10** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(d) · An LSI system has transfer function $H(z)$. Suppose that the output of the system to the input $x[n] = \cos(\omega_0 n + \phi)$ is $y[n] = \lvert H(e^{j\omega_0})\rvert\cos\left(\omega_0 n + \phi + \angle H(e^{j\omega_0})\right)$ for any $\omega_0, \phi$, where $H(e^{j\omega}) = H(z)\big|_{z=e^{j\omega}}$. Then, the system $h[n]$ can be either real or complex.

> [!success]- Answer
> **False.** Split the cosine: the output is $\tfrac12\big[H_d(\omega_0)e^{j(\omega_0n+\phi)}+H_d(-\omega_0)e^{-j(\omega_0n+\phi)}\big]$. It equals the stated formula for every $\omega_0,\phi$ only if $H_d(-\omega_0)=H_d^*(\omega_0)$, which means $h[n]$ is **real**.

**Q11** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(a) · $x[n] = \cos(\omega_0 n)$ is an eigenfunction of a stable LTI system.

> [!success]- Answer
> **False.** Only $e^{j\omega_0n}$ is an eigenfunction of every LTI system. A cosine comes out as a multiple of itself only if $H_d(\omega_0)=H_d(-\omega_0)$; the one-sample delay (stable) already returns $\cos(\omega_0n-\omega_0)$.

## 3. Zero padding: the DTFT does not change

Appending zeros adds nothing to $\sum_n x[n]e^{-j\omega n}$. These six statements are the most repeated idea on Midterm 2; the first four need only the DTFT, Q16–Q17 also use the DFT *(later)*.

**Q12** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(a) · Zero padding a finite-length signal can change its DTFT.

> [!success]- Answer
> **False.** The appended zeros contribute $0\cdot e^{-j\omega n}$. Zero padding changes the **DFT** (a finer grid of samples of the same $X_d$), never the DTFT.

**Q13** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(c) · Suppose $x[n]$ is a finite-length signal with DTFT $X_d(\omega)$. We zero-pad $x[n]$ with some number of zeros to obtain $y[n]$ with DTFT $Y_d(\omega)$. It follows then that $X_d(\omega) = Y_d(\omega)$.

> [!success]- Answer
> **True.** Same sum, same DTFT.

**Q14** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(f) · Let $\{x[n]\}_{n=0}^{N-1}$ be a length-$N$ signal with DTFT $X_d(\omega)$ and $\{y[n]\}_{n=0}^{M+N-1}$ be $x[n]$ zero-padded with $M$ zeros. The DTFT of $y[n]$ given by $Y_d(\omega)$ is equal to $X_d(\omega)$.

> [!success]- Answer
> **True.** As Q13.

**Q15** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(d) · Let $x[n]$ be a length-$N$ signal with DTFT $X_d(\omega)$. We zero-pad $x[n]$ to length-$3N$ to obtain $y[n]$ with DTFT $Y_d(\omega)$. We may say that $X_d(\omega) = Y_d(3\omega)$.

> [!success]- Answer
> **False.** $Y_d(\omega)=X_d(\omega)$. Inserting two zeros **between** samples (upsampling) would give $X_d(3\omega)$; appending zeros at the end does nothing to the DTFT.

**Q16** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(d) · A length-$N$ signal $x[n]$ with DTFT $X_d(\omega)$ and DFT $X[k]$ is zero-padded with $N$ zeros to length-$2N$ to form $y[n]$. Then, $X[k] = Y[2k]$ and $X_d(\omega) = Y_d(\omega)$. *(DFT half: later)*

> [!success]- Answer
> **True.** $Y_d=X_d$, and the $2N$-point DFT samples it twice as densely: $Y[2k]=X_d\big(\frac{2\pi\cdot2k}{2N}\big)=X_d\big(\frac{2\pi k}{N}\big)=X[k]$. Both halves need their reason.

**Q17** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(d) · Assume $x[n]$ is a finite-duration sequence of length 20, and $y[n]$ is obtained by zero-padding $x[n]$ to length 32. That is, $y[n] = x[n]$, for $n = 0, 1, \dots, 19$, and $y[n] = 0$, $n = 20, 21, \dots, 31$. Let $\{X[m]\}_{m=0}^{19}$ and $\{Y[m]\}_{m=0}^{31}$ be the DFT of $\{x[n]\}_{n=0}^{19}$ and $\{y[n]\}_{n=0}^{31}$, respectively, then $X[10] = Y[16]$. *(later)*

> [!success]- Answer
> **True.** $X[10]=X_d\big(\frac{2\pi\cdot10}{20}\big)=X_d(\pi)$ and $Y[16]=X_d\big(\frac{2\pi\cdot16}{32}\big)=X_d(\pi)$.

## 4. Sampling and the Nyquist rate *(later)*

Lectures 17+ (notes coming): $x[n]=x_c(nT)$, $\omega=\Omega T$, aliasing, the Nyquist rate.

**Q18** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(a) · By sampling a continuous-time signal $x_c(t) = \cos(17\pi t)$ with some sampling period $T$, it is possible to obtain a discrete time signal $x[n] = \cos(3\pi n/4)$.

> [!success]- Answer
> **True.** $x[n]=\cos(17\pi Tn)$; $T=\frac{3}{68}$ s gives $17\pi T=\frac{3\pi}{4}$.

**Q19** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(a) · By sampling a continuous-time signal $x_c(t) = \cos(\pi^3 t)$ with some sampling period $T$, it is possible to obtain a discrete time signal $x[n] = \cos(3\pi n/4)$.

> [!success]- Answer
> **True.** $\pi^3$ is just a number: $T=\frac{3}{4\pi^2}$ s gives $\pi^3T=\frac{3\pi}{4}$.

**Q20** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(b) · If the Nyquist sampling rate for a continuous-time signal $x_c(t)$ is $F_s$, then the Nyquist sampling rate for $y_c(t) = x_c(2t)$ is $2F_s$.

> [!success]- Answer
> **True.** $x_c(2t)\leftrightarrow\frac12X_c(\Omega/2)$: compressing time by 2 doubles the highest frequency.

**Q21** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(b) · If the Nyquist sampling rate for a continuous-time signal $x_c(t)$ is $F_s$, then the Nyquist sampling rate for $y_c(t) = x_c(3t)$ is $F_s/3$.

> [!success]- Answer
> **False.** Compressing time by 3 stretches the spectrum by 3: the Nyquist rate is $3F_s$.

**Q22** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(e) · If $x_c(t)$ is a bandlimited continuous-time signal, then there must exist a finite $\Omega_{\max}$ such that $X_a(\Omega) = 0$ for $\lvert\Omega\rvert \gt \Omega_{\max}$, where $X_a(\Omega)$ is the CTFT of $x_c(t)$.

> [!success]- Answer
> **True.** That is the definition of bandlimited.

**Q23** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(d) · Every continuous-time signal has a minimum sampling frequency to avoid aliasing during analog-to-digital conversion.

> [!success]- Answer
> **False.** Only bandlimited signals have a Nyquist rate. A signal with energy at arbitrarily high frequencies (a rectangular pulse) aliases at every sampling rate.

**Q24** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(e) · Increasing the sampling period shrinks the corresponding DTFT.

> [!success]- Answer
> **False.** An analog frequency $\Omega$ lands at $\omega=\Omega T$, so a larger $T$ **stretches** the spectrum outward in $\omega$ (toward $\pi$, and past it into aliasing); only the height $\frac1T$ shrinks. The key: "The corresponding DTFT would be expanded."

**Q25** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(d) · The value of $\int_3^{\infty}(t+1)\delta(t)\,dt$ is 0.

> [!success]- Answer
> **True.** The impulse sits at $t=0$, outside $[3,\infty)$; sifting only fires inside the limits. (A continuous-time warm-up: no sampling needed.)

## 5. Ideal D/A conversion and reconstruction *(later)*

**Q26** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(e) · A discrete-time signal is given by $x[n] = 4\delta[n-2]$. We pass $x[n]$ to an ideal D/A converter with sampling period $T$ to recover $x_a(t)$. The recovered continuous-time signal is given by $x_a(t) = 4\delta(n - 2T)$.

> [!success]- Answer
> **False.** An ideal D/A interpolates with sincs: $x_a(t)=4\,\dfrac{\sin\big(\pi(t-2T)/T\big)}{\pi(t-2T)/T}$. (The statement also mixes $n$ and $t$.)

**Q27** · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(c) · A discrete-time signal $x[n] = 2\delta[n-5]$ is passed to an ideal D/A converter with sampling period $T$ to recover $x_a(t)$. The recovered signal is given by $x_a(t) = 2\delta(t - 5T)$.

> [!success]- Answer
> **False.** One sample becomes one sinc: $x_a(t)=2\,\dfrac{\sin\big(\pi(t-5T)/T\big)}{\pi(t-5T)/T}$, which is 2 at $t=5T$, 0 at the other sample instants and nonzero in between.

**Q28** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(c) · Let $x[n] = \delta[n-2] + 2\delta[n-4]$. We recover $x_a(t)$ by performing ideal digital-to-analog conversion with sampling period $T = 1$ s. Then, $x_a(t) = 0$ at $t = 3$ s.

> [!success]- Answer
> **True.** $x_a(t)=\mathrm{sinc}(t-2)+2\,\mathrm{sinc}(t-4)$ with $\mathrm{sinc}\,u=\frac{\sin\pi u}{\pi u}$; both sincs vanish at $t=3$. Ideal interpolation passes through every sample, and $x[3]=0$.

**Q29** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(c) · The ideal reconstruction filter is causal.

> [!success]- Answer
> **False.** Its impulse response $\frac{\sin(\pi t/T)}{\pi t/T}$ is nonzero for $t\lt0$.

## 6. The DFT and its properties *(later)*

**Q30** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(i) · Let $\{x[n]\}_{n=0}^{5} = \{1, -1, -2, 3, 4, -3\}$. Consider the corresponding 6-point DFT $\{X[k]\}_{k=0}^{5}$. Then, $X[0] = 0$.

> [!success]- Answer
> **False.** $X[0]=\sum_nx[n]=2$.

**Q31** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(e) · Let $\{x[n]\}_{n=0}^{7} = \{1, -1, 6, 7, 9, -6, -7, 9\}$. Consider the corresponding 8-point DFT $\{X[k]\}_{k=0}^{7}$. Then, $X[0] = 0$.

> [!success]- Answer
> **False.** $X[0]=\sum_nx[n]=18$.

**Q32** · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(c) · If $\{x[n]\}_{n=0}^{5}$ is real-valued and $\{X[k]\}_{k=0}^{5}$ is its DFT, then $X[0]$ is real-valued.

> [!success]- Answer
> **True.** $X[0]=\sum_nx[n]$, a sum of real numbers.

**Q33** · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(b) · Two different sequences of same length can have the same DFT.

> [!success]- Answer
> **False.** The DFT is invertible: the inverse DFT recovers $x$ from $X$.

**Q34** · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(d) · If $x[n]$ is the inverse DFT of $\{1, 2, 3, 4\}$, then $x[n]$ must be zero for $n \lt 0$ or $n \gt 3$.

> [!success]- Answer
> **False.** The inverse-DFT formula $x[n]=\frac1N\sum_kX[k]e^{j\frac{2\pi}{N}kn}$ is $N$-periodic in $n$: $x[4]=x[0]=2.5$.

**Q35** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(b) · If $x[n]$ is the inverse DFT of $X[k] = \{1, 2, 3, 4\}$, $0 \le k \le 3$, then $x[n]$ must be zero for $n \lt 0$ and $n \gt 3$.

> [!success]- Answer
> **False.** As Q34 (it came back two years later). Set it beside Q7: the same four numbers as a DTFT give a finite sequence, as a DFT a periodic one.

**Q36** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(h) · The DTFT and DFT of a length-14 sequence $x[n]$ are given by $X_d(\omega)$ and $X[k]$, respectively. We know then that $X[11] = X_d\left(-\tfrac{3\pi}{7}\right)$.

> [!success]- Answer
> **True.** $X[k]=X_d\big(\frac{2\pi k}{N}\big)$, so $X[11]=X_d\big(\frac{11\pi}{7}\big)=X_d\big(\frac{11\pi}{7}-2\pi\big)=X_d\big(-\frac{3\pi}{7}\big)$ by $2\pi$-periodicity (a Unit 3 fact doing the work).

## 7. Spectral analysis with the DFT *(later)*

**Q37** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(f) · The 64-point DFT of the finite-length signal $x[n] = \cos\left(\frac{\pi}{16}n\right)$, $0 \le n \le 63$ has only two nonzero elements.

> [!success]- Answer
> **True.** $\frac{\pi}{16}=\frac{2\pi\cdot2}{64}$: exactly two cycles in 64 samples, so $X[2]=X[62]=32$ and the other 62 bins are 0.

**Q38** · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(g) · The DFT of $\{x[n]\}_{n=0}^{23} = \cos\left(\tfrac{\pi}{8}n\right)$ will only have two non-zero values.

> [!success]- Answer
> **False.** The period is 16, so 24 samples hold 1.5 periods ($\frac{\pi}{8}=\frac{2\pi k}{24}$ needs $k=1.5$): the cosine leaks into all 24 bins.

**Q39** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(e) · An analog signal $x_a(t) = \cos(50\pi t)$ is sampled at $f_s = 50$ Hz for 1 second to obtain $\{x[n]\}_{n=0}^{49}$. The DFT of $x[n]$, $X[k]$, is non-zero for only one value of $k$ for $0 \le k \le 49$.

> [!success]- Answer
> **True.** $x[n]=\cos(\pi n)=(-1)^n=e^{j\frac{2\pi\cdot25}{50}n}$: one exponential exactly on bin 25, so $X[25]=50$ and the other 49 bins are 0.

**Q40** · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(f) · Applying the Hamming window for spectral analysis leads to lower sidelobes and narrower main lobes in spectral components.

> [!success]- Answer
> **False.** A trade: much lower sidelobes (about $-42$ dB against $-13$ dB for the rectangular window) for a main lobe about **twice as wide**.

## 8. Circular convolution and the FFT *(later)*

**Q41** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(g) · Linear convolution can be computed as a circular convolution via zero-padding.

> [!success]- Answer
> **True.** Pad both sequences to $N\ge L_x+L_h-1$; the $N$-point circular convolution then equals the linear one.

**Q42** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(h) · Circular convolution can be applied to two finite duration sequences with arbitrary lengths.

> [!success]- Answer
> **False** (the key's answer). An $N$-point circular convolution combines two length-$N$ sequences; sequences of different lengths must first be padded to a common $N$.

**Q43** · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(j) · FFT is just an efficient algorithm to evaluate DFT.

> [!success]- Answer
> **True.** The FFT returns exactly the DFT values, in about $N\log_2N$ operations instead of $N^2$.

## 9. Patterns that recur

> [!key] Eight patterns (with the statements that use them)
> 1. **"The DTFT is $X(e^{j\omega})$" — check the ROC first.** False whenever the ROC misses $\lvert z\rvert=1$; $2^nu[n]$ appears twice (Q1, Q2).
> 2. **Every DTFT is $2\pi$-periodic.** Any claim tying periodicity to length, or saying $X_d=0$ for all $\lvert\omega\rvert$ beyond some value, is False (Q3–Q5); periodicity also turns DFT bin $k$ into a negative frequency (Q36).
> 3. **Impulses in $X_d$ need a sinusoid that never ends** (Q6); a fractional delay is a sinc, not a shifted $\delta$ (Q8).
> 4. **Uniqueness:** a finite sum of $e^{-j\omega n_0}$ is the DTFT of a finite sequence and of nothing else (Q7). The DFT version is False, because the inverse DFT is periodic (Q34, Q35).
> 5. **Real signal $\iff$ Hermitian DTFT.** That is what licenses the real-sinusoid shortcut (Q9, Q10); a cosine is never an eigenfunction (Q11).
> 6. **Zero padding never changes the DTFT** (Q12–Q16) and only refines the DFT grid (Q16, Q17). Six statements in seven years: the single most repeated idea.
> 7. *(later)* **Sampling maps $\Omega$ to $\omega=\Omega T$ modulo $2\pi$.** Some $T$ always maps a cosine to a given digital frequency (Q18, Q19); time compression raises the Nyquist rate (Q20, Q21); only bandlimited signals have one (Q22, Q23); a larger $T$ stretches the DTFT (Q24).
> 8. *(later)* **Ideal D/A gives sincs** (Q26–Q29), and **a DFT of a sampled cosine is clean only for a whole number of periods** (Q37–Q39).

> [!trap] Where points actually go
> - Answering from the look of the formula: $X_d=\frac{1}{1-2e^{-j\omega}}$ (Q2) and $\pi[\delta(\omega-\frac{\pi}{32})+\delta(\omega+\frac{\pi}{32})]$ (Q6) are well-formed and wrong.
> - Mixing up appending zeros (DTFT unchanged) with inserting zeros (frequency axis compressed): Q15.
> - Reading "shrinks" in Q24 as the height instead of the frequency axis.
> - On the +2/−1/0 exams, leaving statements blank out of caution: a 50/50 guess averages $+0.5$.

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

## Python: zero padding and leakage in a few lines

Q12–Q16 and Q37–Q38 in code: the DTFT of a padded signal is the same function, the longer DFT samples it more densely, and a cosine is clean in the DFT only for a whole number of periods.

```python
import numpy as np

x = np.array([1.0, 2, 3, 4])
dtft = lambda s, w: np.sum(s * np.exp(-1j * w * np.arange(len(s))))
y = np.r_[x, np.zeros(8)]                                  # zero-padded to length 12
print("X_d(1.0) =", np.round(dtft(x, 1.0), 6), " Y_d(1.0) =", np.round(dtft(y, 1.0), 6))
print("4-point DFT :", np.round(np.fft.fft(x), 3))
print("12-point DFT, every 3rd bin:", np.round(np.fft.fft(y)[::3], 3))
for N, w0 in [(64, np.pi / 16), (24, np.pi / 8)]:              # FA2019 #1(f), FA2023 #1(g)
    X = np.fft.fft(np.cos(w0 * np.arange(N)))
    print(f"N = {N}, w0 = pi/{round(np.pi / w0)}: nonzero bins =", int(np.sum(np.abs(X) > 1e-9)))
```

```text
X_d(1.0) = (-3.127806-4.975314j)  Y_d(1.0) = (-3.127806-4.975314j)
4-point DFT : [10.+0.j -2.+2.j -2.+0.j -2.-2.j]
12-point DFT, every 3rd bin: [10.+0.j -2.+2.j -2.+0.j -2.-2.j]
N = 64, w0 = pi/16: nonzero bins = 2
N = 24, w0 = pi/8: nonzero bins = 24
```

The padded signal has the same DTFT value at $\omega=1$, and every third bin of its 12-point DFT repeats the 4-point DFT (the same $X_d$ sampled at $\frac{2\pi k}{4}=\frac{2\pi\cdot3k}{12}$). Two whole periods in 64 samples give two nonzero bins; one and a half periods in 24 samples leak into all 24.

## Related

[[exams/midterm-2/index|Midterm 2 overview]] · [[exams/midterm-2/past-exams/index|past Midterm 2 exams]] · [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/frequency-response|frequency response]] · [[exams/midterm-1/true-false-bank|Midterm 1 True/False bank]] · [[demos/practice-drills|practice drills]]

### Sources for this page

- Official solutions of ECE 310 Midterm 2: FA2019 #1, SP2021 #1, FA2021 #1, SP2023 #1, FA2023 #1, FA2024 #1, SP2025 #1 (answers read off the keys; FA2019's is handwritten), and the typed statements on this site's exam pages.
- Lectures 13–15 (DTFT definition, existence, periodicity, symmetry; frequency response and eigenfunctions). The sampling, D/A and DFT statements belong to Lectures 17+, not yet in these notes; their reasons follow the official keys.
- Every numerical claim (the DFT values and bin counts, $x[4]$ of the inverse DFT, $X[11]=X_d(-\frac{3\pi}{7})$, the zero-padding identities, the sinc values, the Hamming sidelobe level and main-lobe width) is checked in `verify/FAM_tfbank.py`, which also writes the deck file `mt2_tf_bank.json` and checks every answer against the exam maps.
