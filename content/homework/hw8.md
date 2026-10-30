---
title: "HW8 · Aliasing of sinusoids, sampled spectra, D/A conversion, digital filtering of analog signals"
description: "ECE 310 Homework 8 (due Oct 23) with folded solutions matching the official key: aliased sinusoids, choosing T, sampled spectra, ZOH and ideal D/A, largest T for digital filtering of analog signals."
tags: [homework, midterm-2, sampling, aliasing]
---

*Homework 8 · due Fri Oct 23, 2026, 11:59 pm (Gradescope) · [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lectures 17]]–[[4-sampling-and-reconstruction/19-aliasing|19]] · topics: [[concepts/aliasing|aliasing]], [[concepts/sampling|sampling]], [[concepts/nyquist-criterion|Nyquist criterion]], [[concepts/ideal-reconstruction|ideal reconstruction]], [[concepts/digital-processing-of-analog-signals|A/D → filter → D/A]] · 6 problems, 100 points · official solutions v1.1 agree with every answer here · prev: HW7 ([[exams/quiz-2|Quiz 2 page]]) · next: HW9 (walkthrough after its Oct 30 due date) · [[homework/index|all homework]]*

> [!abstract] In one breath
> - $\cos(\Omega_0t)$ sampled at $T$ gives $\cos(\Omega_0Tn)$; $\Omega_0T$ is known only up to sign and $2\pi k$, so neither $\Omega_0$ nor $T$ is unique.
> - $X_d(\omega)=\frac1T\sum_kX_a\!\left(\frac{\omega-2\pi k}{T}\right)$: copies every $2\pi$; no aliasing iff $T\lt\frac{1}{2B}$ (strict).
> - A/D → $H_d$ → ideal D/A acts as one analog filter when no copy lands where $H_d\ne0$; aliasing elsewhere is harmless.

| # | Skill | Links |
|---|---|---|
| 1 | Every $\Omega_0$ behind a sampled cosine | [[concepts/aliasing\|aliasing]] · [[4-sampling-and-reconstruction/19-aliasing\|L19]] |
| 2 | Choosing $T$; non-uniqueness | [[problems/sampling-and-the-nyquist-rate\|sampling and the Nyquist rate]] |
| 3 | Sampled spectrum; $T_{\max}$ | [[concepts/sampling\|sampling]] · [[concepts/nyquist-criterion\|Nyquist criterion]] |
| 4 | Zero-order hold and ideal D/A | [[concepts/ideal-reconstruction\|ideal reconstruction]] · [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion\|L18]] |
| 5 | Largest bandwidth keeping A/D → LPF → D/A LTI | [[concepts/digital-processing-of-analog-signals\|A/D → filter → D/A]] |
| 6 | Band-pass with aliasing outside the passband | [[problems/digital-filtering-of-analog-signals\|digital filtering of analog signals]] |

## Problem 1 — two analog frequencies, one sampled cosine

> [!question] Problem 1
> The sequence $x[n]=\cos\!\left(\frac{\pi}{3}n\right)$, $-\infty\lt n\lt\infty$, was obtained by sampling the continuous-time signal $x_a(t)=\cos(\Omega_0t)$, $-\infty\lt t\lt\infty$, at a sampling rate of 1000 samples/sec. What are two possible values of $\Omega_0$ that could have resulted in the sequence $x[n]$?

> [!success]- Solution
> $T=10^{-3}$ s, $x[n]=\cos(\Omega_0Tn)$. Integer $n$: the argument counts only mod $2\pi$, and cosine is even, so
> $$
> \Omega_0T=\pm\frac{\pi}{3}+2\pi k\quad\Rightarrow\quad\Omega_0=\frac{\pm\frac{\pi}{3}+2\pi k}{T}=\frac{1000\pi(6k\pm1)}{3}\ \text{rad/s}.
> $$
> **Answer** (any two): $\Omega_0=\frac{1000\pi}{3}\approx1047$ rad/s (166.7 Hz, the principal alias), $\frac{5000\pi}{3}\approx5236$ rad/s (833.3 Hz), $\frac{7000\pi}{3}$, $\frac{11000\pi}{3}$, …

**On the exam:** [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #3: $\sin(\Omega_0t)$ at 400 Hz gives $\sin(\frac{\pi}{2}n)$ → which $\Omega_0$ (a sine is odd: the minus branch flips the sign).

## Problem 2 — choosing the sampling period

> [!question] Problem 2
> The continuous-time signal $x_a(t)=\sin(10\pi t)+\cos(20\pi t)$ is sampled with a sampling period $T$ to obtain the discrete-time signal $x[n]=\sin\!\left(\frac{\pi}{5}n\right)+\cos\!\left(\frac{2\pi}{5}n\right)$.
>
> a) Determine a choice for $T$ consistent with this information.
>
> b) Is your choice for $T$ in part (a) unique? If so, explain why. If not, specify another choice of $T$ consistent with the information given.

> [!success]- Solution (a)
> Match term by term (the frequencies $\frac{\pi}{5}\ne\frac{2\pi}{5}$ cannot swap):
> $$
> \begin{gathered}
> \sin:\ 10\pi T=\tfrac{\pi}{5}+2\pi k_1\ \Rightarrow\ T=\tfrac{1}{50}+\tfrac{k_1}{5}\quad(\text{odd: no minus branch}),\\
> \cos:\ 20\pi T=\pm\tfrac{2\pi}{5}+2\pi k_2\ \Rightarrow\ T=\pm\tfrac{1}{50}+\tfrac{k_2}{10}.
> \end{gathered}
> $$
> $k_1=k_2=0$: **$T=\frac{1}{50}$ s $=20$ ms** ($10\pi\cdot\frac1{50}=\frac{\pi}{5}$, $20\pi\cdot\frac1{50}=\frac{2\pi}{5}$).

> [!success]- Solution (b)
> **Not unique.** Both sets share $T=\frac{1+10k}{50}$, $k=0,1,2,\dots$ (the cosine's minus branch $\frac{5k_2-1}{50}$ never meets the sine's set). E.g. $T=\frac{11}{50}$ s:
> $$
> \sin\!\left(\tfrac{11\pi}{5}n\right)=\sin\!\left(\tfrac{\pi}{5}n+2\pi n\right),\qquad\cos\!\left(\tfrac{22\pi}{5}n\right)=\cos\!\left(\tfrac{2\pi}{5}n+4\pi n\right).
> $$
> Only $T=\frac1{50}$ s meets Nyquist ($f_s=50\gt20$ Hz); the others alias both tones onto the same samples.

**On the exam:** [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #8: two cosines → two possible $T$ · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6.

## Problem 3 — a sampled cosine at two sampling periods

> [!question] Problem 3
> The continuous-time signal $x_a(t)=\cos(400\pi t)$ is sampled with a sampling period $T$ to obtain a discrete-time signal $x[n]=x_a(nT)$.
>
> a) Compute and sketch the magnitude of the continuous-time Fourier transform of $x_a(t)$ and the discrete-time Fourier transform of $x[n]$ for $T=1$ ms.
>
> b) Repeat part (a) for $T=2$ ms.
>
> c) What is the maximum sampling period $T_{\max}$ such that no aliasing occurs in the sampling process?

> [!success]- Solution (a)
> $$
> X_a(\Omega)=\pi\big[\delta(\Omega-400\pi)+\delta(\Omega+400\pi)\big]:
> $$
> impulses of weight $\pi$ at $\pm400\pi$ rad/s ($\pm200$ Hz), the same for (b). $\omega_0=\Omega_0T=400\pi\cdot10^{-3}=0.4\pi$, $x[n]=\cos(0.4\pi n)$:
> $$
> X_d(\omega)=\pi\sum_{k=-\infty}^{\infty}\big[\delta(\omega-0.4\pi-2\pi k)+\delta(\omega+0.4\pi-2\pi k)\big].
> $$
> In $[-2\pi,2\pi]$: weight $\pi$ at $\pm0.4\pi$ and $\pm1.6\pi$. The weight stays $\pi$: $\delta\!\left(\frac{\omega-\omega_0}{T}\right)=T\,\delta(\omega-\omega_0)$ cancels the $\frac1T$.

> [!success]- Solution (b)
> $\omega_0=400\pi\cdot0.002=0.8\pi$, $x[n]=\cos(0.8\pi n)$: impulses of weight $\pi$ at $\pm0.8\pi$ and $\pm1.2\pi$ in $[-2\pi,2\pi]$. Still $\lt\pi$: no aliasing ($f_s=500\gt400$ Hz).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" width="640" height="400" role="img" aria-label="Three impulse plots: |X_a| with impulses of weight pi at plus and minus 400 pi; |X_d| for T = 1 ms with impulses at plus/minus 0.4 pi and 1.6 pi; |X_d| for T = 2 ms at plus/minus 0.8 pi and 1.2 pi" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="330.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X<tspan baseline-shift="sub" style="font-size:75%">a</tspan>(Ω)| (both parts)</text><line x1="40.0" y1="100.0" x2="620.0" y2="100.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="30.0" x2="330.0" y2="100.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="136.7" y1="97.0" x2="136.7" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="136.7" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−400π</text><line x1="330.0" y1="97.0" x2="330.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="330.0" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="523.3" y1="97.0" x2="523.3" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="523.3" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">400π</text><text x="620.0" y="94.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">Ω (rad/s)</text><line x1="136.7" y1="100.0" x2="136.7" y2="50.0" stroke="var(--hi)" stroke-width="2"/><path d="M131.7,52.0 L136.7,44.0 L141.7,52.0 Z" fill="var(--hi)"/><text x="142.7" y="48.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">(π)</text><line x1="523.3" y1="100.0" x2="523.3" y2="50.0" stroke="var(--hi)" stroke-width="2"/><path d="M518.3,52.0 L523.3,44.0 L528.3,52.0 Z" fill="var(--hi)"/><text x="529.3" y="48.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">(π)</text><text x="330.0" y="154.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)|, T = 1 ms: ω<tspan baseline-shift="sub" style="font-size:75%">0</tspan> = 0.4π</text><line x1="40.0" y1="230.0" x2="620.0" y2="230.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="160.0" x2="330.0" y2="230.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="60.2" y1="227.0" x2="60.2" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="60.2" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="114.2" y1="227.0" x2="114.2" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="114.2" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1.6π</text><line x1="195.1" y1="227.0" x2="195.1" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="195.1" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="276.0" y1="227.0" x2="276.0" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="276.0" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−0.4π</text><line x1="330.0" y1="227.0" x2="330.0" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="330.0" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="384.0" y1="227.0" x2="384.0" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="384.0" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0.4π</text><line x1="464.9" y1="227.0" x2="464.9" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="464.9" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="545.8" y1="227.0" x2="545.8" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="545.8" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1.6π</text><line x1="599.8" y1="227.0" x2="599.8" y2="233.0" stroke="currentColor" stroke-width="1"/><text x="599.8" y="244.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><text x="620.0" y="224.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><line x1="195.1" y1="160.0" x2="195.1" y2="230.0" stroke="var(--muted)" stroke-width="0.8" stroke-dasharray="3 3"/><line x1="464.9" y1="160.0" x2="464.9" y2="230.0" stroke="var(--muted)" stroke-width="0.8" stroke-dasharray="3 3"/><line x1="384.0" y1="230.0" x2="384.0" y2="180.0" stroke="var(--hi)" stroke-width="2"/><path d="M379.0,182.0 L384.0,174.0 L389.0,182.0 Z" fill="var(--hi)"/><text x="390.0" y="178.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">(π)</text><line x1="276.0" y1="230.0" x2="276.0" y2="180.0" stroke="var(--hi)" stroke-width="2"/><path d="M271.0,182.0 L276.0,174.0 L281.0,182.0 Z" fill="var(--hi)"/><text x="282.0" y="178.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">(π)</text><line x1="545.8" y1="230.0" x2="545.8" y2="180.0" stroke="var(--accent)" stroke-width="2"/><path d="M540.8,182.0 L545.8,174.0 L550.8,182.0 Z" fill="var(--accent)"/><line x1="114.2" y1="230.0" x2="114.2" y2="180.0" stroke="var(--accent)" stroke-width="2"/><path d="M109.2,182.0 L114.2,174.0 L119.2,182.0 Z" fill="var(--accent)"/><text x="330.0" y="284.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)|, T = 2 ms: ω<tspan baseline-shift="sub" style="font-size:75%">0</tspan> = 0.8π</text><line x1="40.0" y1="360.0" x2="620.0" y2="360.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="290.0" x2="330.0" y2="360.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="60.2" y1="357.0" x2="60.2" y2="363.0" stroke="currentColor" stroke-width="1"/><text x="60.2" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="168.1" y1="357.0" x2="168.1" y2="363.0" stroke="currentColor" stroke-width="1"/><text x="168.1" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1.2π</text><line x1="222.1" y1="357.0" x2="222.1" y2="363.0" stroke="currentColor" stroke-width="1"/><text x="222.1" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−0.8π</text><line x1="330.0" y1="357.0" x2="330.0" y2="363.0" stroke="currentColor" stroke-width="1"/><text x="330.0" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="437.9" y1="357.0" x2="437.9" y2="363.0" stroke="currentColor" stroke-width="1"/><text x="437.9" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0.8π</text><line x1="491.9" y1="357.0" x2="491.9" y2="363.0" stroke="currentColor" stroke-width="1"/><text x="491.9" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1.2π</text><line x1="599.8" y1="357.0" x2="599.8" y2="363.0" stroke="currentColor" stroke-width="1"/><text x="599.8" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><text x="620.0" y="354.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><line x1="195.1" y1="290.0" x2="195.1" y2="360.0" stroke="var(--muted)" stroke-width="0.8" stroke-dasharray="3 3"/><line x1="464.9" y1="290.0" x2="464.9" y2="360.0" stroke="var(--muted)" stroke-width="0.8" stroke-dasharray="3 3"/><line x1="437.9" y1="360.0" x2="437.9" y2="310.0" stroke="var(--hi)" stroke-width="2"/><path d="M432.9,312.0 L437.9,304.0 L442.9,312.0 Z" fill="var(--hi)"/><text x="443.9" y="308.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">(π)</text><line x1="222.1" y1="360.0" x2="222.1" y2="310.0" stroke="var(--hi)" stroke-width="2"/><path d="M217.1,312.0 L222.1,304.0 L227.1,312.0 Z" fill="var(--hi)"/><text x="228.1" y="308.0" text-anchor="start" fill="var(--hi)" style="font-size:11px">(π)</text><line x1="491.9" y1="360.0" x2="491.9" y2="310.0" stroke="var(--accent)" stroke-width="2"/><path d="M486.9,312.0 L491.9,304.0 L496.9,312.0 Z" fill="var(--accent)"/><line x1="168.1" y1="360.0" x2="168.1" y2="310.0" stroke="var(--accent)" stroke-width="2"/><path d="M163.1,312.0 L168.1,304.0 L173.1,312.0 Z" fill="var(--accent)"/></svg><figcaption><strong>HW8 #3: two impulses in Ω become impulses at ±ΩT, repeated every 2π.</strong> Red: the copy in [−π, π]; teal: the neighbouring copies; dashed lines at ±π. No aliasing at either T: 200 Hz is below fs/2 = 500 Hz (1 ms) and 250 Hz (2 ms).</figcaption></figure>

> [!success]- Solution (c)
> $B=200$ Hz: $T\lt\frac{1}{2B}=\frac{1}{400}$ s, **$T_{\max}=2.5$ ms** (a strict bound: at $T=2.5$ ms, $\omega_0=\pi$, and a sine at 200 Hz would sample to zeros).

**On the exam:** [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(a), (b): $X_d$ at $T_N$ and $2T_N$ · [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #4.

## Problem 4 — zero-order hold and ideal D/A of four samples

> [!question] Problem 4
> The input to a D/A converter is $\{x[n]\}=\{-1,\ \underset{\uparrow}{0},\ 0,\ 3\}$ with sampling interval $T$. Determine the output of the D/A converter if the D/A converter is (a) a ZOH, and (b) an ideal D/A.

> [!success]- Solution
> The arrow marks $n=0$: $x[-1]=-1$, $x[2]=3$, so $x[n]=-\delta[n+1]+3\delta[n-2]$.
>
> **(a)** ZOH (ungraded in the key; not in Lecture 18): holds each sample for one period, pulse $u(t)-u(t-T)$:
> $$
> x_{\text{ZOH}}(t)=-\big[u(t+T)-u(t)\big]+3\big[u(t-2T)-u(t-3T)\big]:
> $$
> $-1$ on $[-T,0)$, $3$ on $[2T,3T)$, $0$ elsewhere.
>
> **(b)** Ideal D/A, $x_a(t)=\sum_nx[n]\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right)$ with $\mathrm{sinc}(u)=\frac{\sin u}{u}$:
> $$
> x_a(t)=-\mathrm{sinc}\!\left(\frac{\pi(t+T)}{T}\right)+3\,\mathrm{sinc}\!\left(\frac{\pi(t-2T)}{T}\right).
> $$
> $x_a(-T)=-1$, $x_a(2T)=3$, zero at every other $nT$; nonzero between samples.

**On the exam:** [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #8: zero-order hold and ideal D/A of $\delta[n-3]$.

## Problem 5 — when is A/D → low-pass → D/A still LTI?

> [!question] Problem 5
> Consider the following system with uniform sampling:
> $$
> x_a(t)\ \xrightarrow{\ \text{A/D},\ T\ }\ x[n]\ \to\ \boxed{H_d(\omega)}\ \to\ y[n]\ \to\ \boxed{\text{D/A (ideal)}}\ \to\ y_a(t)
> $$
> The discrete-time system $H_d(\omega)$ is an ideal low-pass filter with cutoff frequency $\frac{\pi}{8}$.
>
> (a) If $x_a(t)$ is bandlimited to 5 kHz, what is the maximum value of $T$ that will avoid aliasing in the A/D converter?
>
> (b) If $\frac1T=10$ kHz, determine the maximum bandwidth of $x_a(t)$ allowed such that the overall system from $x_a(t)$ to $y_a(t)$ behaves as an LTI system.

> [!success]- Solution (a)
> $T\lt\frac{1}{2B}=\frac{1}{10000}$ s: **$T_{\max}=0.1$ ms** (strict bound).

> [!success]- Solution (b)
> LTI needs only the passband $\lvert\omega\rvert\lt\frac{\pi}{8}$ alias-free. Band $\omega_B=2\pi BT$; the $k=1$ copy covers $[2\pi-\omega_B,\ 2\pi+\omega_B]$:
> $$
> 2\pi-2\pi BT\ge\frac{\pi}{8}\ \Rightarrow\ B\le\frac{15}{16T}=\frac{15}{16}\cdot10\ \text{kHz}=9375\ \text{Hz}.
> $$
> **Answer.** $B_{\max}=9375$ Hz. Then $y_a$ is $x_a$ through an ideal analog low-pass with cutoff $\frac{\pi/8}{T}$, i.e. 625 Hz; content aliased above 625 Hz is removed. Beyond 9375 Hz, e.g. a 9500 Hz tone aliases to 500 Hz and passes: not LTI.

**On the exam:** [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #9(c): largest $T\gt T_{NYQ}$ that keeps the system LSI.

## Problem 6 — a band-pass for speech, with and without aliasing

> [!question] Problem 6
> A speech signal $x_a(t)$ is assumed to be bandlimited to 12 kHz. It is desired to filter this signal with a bandpass filter that will pass the frequencies between 300 Hz and 6 kHz by using a digital filter $H_d(\omega)$ sandwiched between an A/D and an ideal D/A.
>
> (a) Determine the Nyquist sampling rate for the input signal.
>
> (b) Sketch the frequency response $H_{d,1}(\omega)$ for the necessary discrete-time filter, when sampling at the Nyquist rate.
>
> (c) Find the largest sampling period $T$ for which the A/D, digital filter response ($H_{d,2}(\omega)$), and D/A can perform the desired filtering function. (Hint: some amount of aliasing may be permissible during A/D conversion for this part.)
>
> (d) For the system using $T$ from part (c), sketch the necessary $H_{d,2}(\omega)$.

> [!success]- Solution (a), (b)
> **(a)** $f_s=2B=24$ kHz ($T=\frac{1}{24000}$ s $\approx41.7\ \mu$s).
>
> **(b)** $\omega=\frac{2\pi f}{f_s}$: $300$ Hz → $\frac{2\pi\cdot300}{24000}=\frac{\pi}{40}$, $6$ kHz → $\frac{\pi}{2}$:
> $$
> H_{d,1}(\omega)=\begin{cases}1, & \frac{\pi}{40}\le\lvert\omega\rvert\le\frac{\pi}{2}\\ 0, & \text{otherwise in }[-\pi,\pi]\end{cases},\qquad 2\pi\text{-periodic}.
> $$

> [!success]- Solution (c), (d)
> **(c)** Aliasing may hit only the stop band. The first copy starts at $\frac{2\pi}{T}-2\pi(12000)$ and must stay above the passband edge $2\pi(6000)$:
> $$
> \frac1T-12000\ge6000\ \Rightarrow\ \frac1T\ge18\ \text{kHz},\qquad T_{\max}=\frac{1}{18000}\ \text{s}\approx55.6\ \mu\text{s}.
> $$
> 9–12 kHz folds onto 6–9 kHz, outside the passband; 6 kHz $\lt\frac{f_s}{2}=9$ kHz, so the ideal D/A keeps the band.
>
> **(d)** At 18 kHz: $300$ Hz → $\frac{\pi}{30}$, $6$ kHz → $\frac{2\pi}{3}$:
> $$
> H_{d,2}(\omega)=\begin{cases}1, & \frac{\pi}{30}\le\lvert\omega\rvert\le\frac{2\pi}{3}\\ 0, & \text{otherwise in }[-\pi,\pi]\end{cases},\qquad 2\pi\text{-periodic}.
> $$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 270" width="640" height="270" role="img" aria-label="Two band-pass frequency responses on [-pi, pi]: H_d1 equals 1 for pi/40 to pi/2 in magnitude of omega; H_d2 equals 1 for pi/30 to 2pi/3" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="330.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">H<tspan baseline-shift="sub" style="font-size:75%">d,1</tspan>(ω), f<tspan baseline-shift="sub" style="font-size:75%">s</tspan> = 24 kHz</text><line x1="40.0" y1="46.2" x2="620.0" y2="46.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="100.0" x2="620.0" y2="100.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="30.0" x2="330.0" y2="100.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="61.5" y1="97.0" x2="61.5" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="61.5" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="195.7" y1="97.0" x2="195.7" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="195.7" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="330.0" y1="97.0" x2="330.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="330.0" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="464.3" y1="97.0" x2="464.3" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="464.3" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="598.5" y1="97.0" x2="598.5" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="598.5" y="114.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="327.0" y1="46.2" x2="333.0" y2="46.2" stroke="currentColor" stroke-width="1"/><text x="36.0" y="50.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="620.0" y="94.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="61.5,100.0 195.7,100.0 195.7,46.2 323.3,46.2 323.3,100.0 336.7,100.0 336.7,46.2 464.3,46.2 464.3,100.0 598.5,100.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="340.7" y="40.2" text-anchor="start" fill="var(--hi)" style="font-size:11px">±π/40</text><text x="330.0" y="149.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">H<tspan baseline-shift="sub" style="font-size:75%">d,2</tspan>(ω), f<tspan baseline-shift="sub" style="font-size:75%">s</tspan> = 18 kHz</text><line x1="40.0" y1="171.2" x2="620.0" y2="171.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="225.0" x2="620.0" y2="225.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="155.0" x2="330.0" y2="225.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="61.5" y1="222.0" x2="61.5" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="61.5" y="239.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="151.0" y1="222.0" x2="151.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="151.0" y="239.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π/3</text><line x1="330.0" y1="222.0" x2="330.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="330.0" y="239.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="509.0" y1="222.0" x2="509.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="509.0" y="239.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π/3</text><line x1="598.5" y1="222.0" x2="598.5" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="598.5" y="239.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="327.0" y1="171.2" x2="333.0" y2="171.2" stroke="currentColor" stroke-width="1"/><text x="36.0" y="175.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="620.0" y="219.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="61.5,225.0 151.0,225.0 151.0,171.2 321.0,171.2 321.0,225.0 339.0,225.0 339.0,171.2 509.0,171.2 509.0,225.0 598.5,225.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="343.0" y="165.2" text-anchor="start" fill="var(--hi)" style="font-size:11px">±π/30</text></svg><figcaption><strong>HW8 #6: the same 300 Hz – 6 kHz band-pass at two sampling rates.</strong> Band edges at ω = 2πf/fs; a small stop band around ω = 0 removes everything below 300 Hz. Both responses repeat every 2π.</figcaption></figure>

**On the exam:** [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #5: largest $T$ and $H_d$ for a low-pass and a high-pass of a 10 kHz signal · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #5(b) · [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(c).

> [!trap] Traps
> - Samples fix $\Omega_0T$ only up to $\pm$ and $2\pi k$; a sine allows only the $+$ sign.
> - DTFT impulses of a sampled cosine keep weight $\pi$, not $\frac{\pi}{T}$.
> - Nyquist is strict: $T\lt\frac{1}{2B}$; "$T_{\max}$" names the bound.
> - The arrow marks $n=0$: $\{-1,\underset{\uparrow}{0},0,3\}$ starts at $n=-1$.
> - With a filter after the A/D only the passband must be alias-free: compare the first copy's lower edge with the passband edge, not with $B$.

## Related

[[concepts/aliasing|aliasing]] · [[concepts/sampling|sampling]] · [[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/ideal-reconstruction|ideal reconstruction]] · [[concepts/digital-processing-of-analog-signals|A/D → filter → D/A]] · families: [[problems/sampling-and-the-nyquist-rate|sampling]], [[problems/digital-filtering-of-analog-signals|digital filtering of analog signals]] · [[demos/sampling-explorer|sampling explorer]] · [[exams/quiz-2|Quiz 2 (HW7)]]

### Sources for this page

ECE 310 Fall 2026 HW8 and official solutions v1.1 (Nick & Mia); Lecture 17–19 notes (Snyder); Singer–Munson notes (zero-order hold); past Midterm 2 exams cited above.
