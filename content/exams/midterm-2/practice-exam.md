---
title: "Practice Midterm 2 (Fall 2026 scope)"
description: "A new full-length practice Midterm 2 in the style of the seven past exams, matched to Fall 2026 scope (Lectures 13–23, HW5–HW9): 9 problems, 100 points, 2 hours, folded solutions."
tags: [exam, midterm-2, practice]
---

*Practice exam, new problems (not a past exam) · 9 problems, 100 points · 2 hours · one handwritten two-sided 8.5×11 in sheet, no calculator · scope Lectures 13–23, HW5–HW9 · the real exam: Wed Nov 4, 7–9 pm · [[exams/midterm-2/index|Midterm 2]] · [[exams/midterm-2/past-exams/index|past exams]]*

> [!abstract] How to use it
> - Sit it in one go: 2 hours, closed book except your sheet, no calculator. Answers in closed form; every number works by hand. Pace: about one minute per point, 20 minutes left to check.
> - Grade with the folded solutions: a True/False item earns its 2 points only with a correct reason; elsewhere give partial credit per step. Add up in the grading table at the end.
> - Repair each miss: the line under each solution links the topic page and the problem family; rework that family's practice, then its past-exam problems.
> - Scope as announced (course website, Oct 30; instructor announcement): no circular-convolution computation and no FFT; DFT properties (#1(e), #1(h), #8) and Lectures 22–23, the last two lectures covered (#1(f)–(g), #9), are in.

## Map of the exam

| # | pts | what it asks | topic pages |
|---|---|---|---|
| 1 | 16 | eight True/False with one-line reasons: ROC and DTFT, linear phase, ZOH vs ideal D/A, A/D–filter–D/A, circular shift, lobe separation, Hamming, Parseval | mixed |
| 2 | 10 | DTFT of $(\frac12)^{\lvert n\rvert}$ from the definition; inverse DTFT of a staircase; sums without series | [[concepts/dtft\|DTFT]] · [[concepts/dtft-pairs\|pairs]] |
| 3 | 10 | a constant, $(-1)^n$ and a cosine through an FIR; angle in the third quadrant | [[concepts/frequency-response\|frequency response]] |
| 4 | 10 | linear-phase FIR: delay, magnitude, phase with $\pi$ jumps, group delay | [[concepts/magnitude-and-phase-response\|magnitude and phase]] · [[concepts/group-delay\|group delay]] |
| 5 | 10 | Nyquist rate; $X_d$ of a sampled triangle with and without overlap | [[concepts/sampling\|sampling]] · [[concepts/nyquist-criterion\|Nyquist]] |
| 6 | 12 | A/D → ideal filter → D/A: $Y_a$; largest $T$ for a low-pass and for a high-pass | [[concepts/digital-processing-of-analog-signals\|A/D → filter → D/A]] |
| 7 | 8 | three sinusoids at $f_s=500$ Hz: aliased samples, recovered $y_a(t)$ | [[concepts/aliasing\|aliasing]] |
| 8 | 12 | DFT values, padding bins, bins in hertz; circular shift, $(-1)^n$, conjugation | [[concepts/dft\|DFT]] · [[concepts/dft-properties\|DFT properties]] |
| 9 | 12 | $\lvert X[k]\rvert$ plot with an on-bin and an off-bin tone; $N$ for lobe separation; rectangular vs Hamming | [[concepts/spectral-analysis\|spectral analysis]] · [[concepts/window-functions\|windows]] |

## Problem 1 · True/False with reasons (16 pts)

> [!question] Problem 1
> Mark each statement **True** or **False** and justify it in one line. *2 points each: 1 for the answer, 1 for the reason.*
>
> (a) $x[n]=\left(\frac12\right)^nu[n]-3^nu[-n-1]$ has a DTFT, and $X_d(\omega)=\dfrac{1}{1-\frac12e^{-j\omega}}+\dfrac{1}{1-3e^{-j\omega}}$.
>
> (b) The FIR filter $y[n]=x[n]+2x[n-1]+3x[n-2]$ has linear phase $\angle H_d(\omega)=-\omega$ (up to jumps of $\pi$), so its group delay is 1 sample at every frequency.
>
> (c) $x[n]=\delta[n]+\delta[n-1]$ is converted to analog with period $T$, once by a zero-order hold (a pulse of height 1 on $0\le t\lt T$ per sample) and once by an ideal D/A. Both outputs equal 1 at $t=\frac{T}{2}$.
>
> (d) A signal bandlimited to 3 kHz is sampled at $f_s=8$ kHz, filtered by an ideal digital low-pass with $\omega_c=\frac{\pi}{4}$ and converted back by an ideal D/A at the same rate. The overall system is an ideal analog low-pass with cutoff 1 kHz.
>
> (e) $x[n]$, $0\le n\le7$, has DFT $X[k]$. Then $y[n]=x[\langle n+2\rangle_8]$ has DFT $Y[k]=e^{-j\frac{\pi}{2}k}X[k]$.
>
> (f) For $x[n]=\cos(0.5\pi n)+\cos(0.6\pi n)$, $0\le n\le47$, the two main lobes of the DFT are full-lobe separated, and zero-padding $x[n]$ to 512 samples would not change their width.
>
> (g) Two equal-amplitude tones $\frac{6\pi}{N}$ apart are full-lobe separated by a length-$N$ rectangular window, and they stay full-lobe separated when a length-$N$ Hamming window is used instead.
>
> (h) The length-4 DFT $X[k]=\{2,\ 2j,\ 2,\ -2j\}$ belongs to a signal with $\sum_{n=0}^{3}\lvert x[n]\rvert^2=4$.

> [!success]- Solution 1
> - **(a) True.** ROCs $\lvert z\rvert\gt\frac12$ and $\lvert z\rvert\lt3$ ($-3^nu[-n-1]\leftrightarrow\frac{1}{1-3z^{-1}}$); the ROC $\frac12\lt\lvert z\rvert\lt3$ contains the unit circle, so $X_d(\omega)=X(e^{j\omega})$.
> - **(b) False.** Taps $\{1,2,3\}$ are not symmetric: $H_d(\frac{\pi}{2})=1-2j-3=-2-2j$, angle $-\frac{3\pi}{4}$, neither $-\frac{\pi}{2}$ nor $-\frac{\pi}{2}+\pi$. The group delay varies with $\omega$.
> - **(c) False.** ZOH: $x_a(\frac{T}{2})=x[0]=1$. Ideal D/A: $\mathrm{sinc}(\frac{\pi}{2})+\mathrm{sinc}(-\frac{\pi}{2})=\frac{2}{\pi}+\frac{2}{\pi}=\frac{4}{\pi}\approx1.27$ (course sinc $\frac{\sin t}{t}$).
> - **(d) True.** $3\lt\frac82$ kHz, so no aliasing and $H_a(\Omega)=H_d(\Omega T)$; cutoff $\frac{\omega_c}{T}=\frac{\pi}{4}\cdot8000=2000\pi$ rad/s $=1$ kHz.
> - **(e) False.** An advance by 2 is a delay by $-2$: $Y[k]=e^{+j\frac{2\pi\cdot2}{8}k}X[k]=e^{j\frac{\pi}{2}k}X[k]$.
> - **(f) True.** $\Delta\omega=0.1\pi\gt\frac{4\pi}{48}\approx0.083\pi$. Padding samples the same DTFT more densely; the lobes stay $\frac{4\pi}{48}$ wide.
> - **(g) False.** Rectangular: $\frac{6\pi}{N}\gt\frac{4\pi}{N}$ ✓. Hamming main lobes are $\frac{8\pi}{N}$ wide: full-lobe needs $\Delta\omega\gt\frac{8\pi}{N}$ ✗.
> - **(h) True.** DFT Parseval: $\frac14(4+4+4+4)=4$. (Indeed $x=\{1,-1,1,1\}$.)

Topic: (a) [[concepts/region-of-convergence|ROC]] · (b) [[concepts/group-delay|group delay]] · (c) [[concepts/ideal-reconstruction|ideal D/A]], ZOH in [[homework/hw8|HW8]] #4 · (d) [[concepts/digital-processing-of-analog-signals|A/D → filter → D/A]] · (e) [[concepts/circular-shift-and-reversal|circular shift]] · (f) [[concepts/frequency-resolution|lobe separation]] · (g) [[concepts/window-functions|windows]] · (h) [[concepts/dft-properties|DFT properties]] · family: [[exams/midterm-2/true-false-bank|T/F bank]]

## Problem 2 · DTFT, inverse DTFT, sums without series (10 pts)

> [!question] Problem 2
> (a) (4 pts) Compute the DTFT of $x_1[n]=\left(\frac12\right)^{\lvert n\rvert}$ from the definition and simplify it to a real function of $\cos\omega$. Check it at $\omega=0$.
>
> (b) (3 pts) The DTFT $X_d(\omega)$ of a signal $x[n]$ is plotted below. Find $x[n]$ as a real closed form; give $x[0]$ and $x[2]$.
>
> <figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 190" width="560" height="190" role="img" aria-label="DTFT equal to 2 for |w| &lt;= pi/4, 1 for pi/4 &lt; |w| &lt;= pi/2, 0 elsewhere in [-pi, pi]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="289.0" y="20.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="44.0" y1="101.8" x2="534.0" y2="101.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="44.0" y1="47.7" x2="534.0" y2="47.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="44.0" y1="156.0" x2="534.0" y2="156.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="289.0" y1="26.0" x2="289.0" y2="156.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="44.0" y1="153.0" x2="44.0" y2="159.0" stroke="currentColor" stroke-width="1"/><text x="44.0" y="170.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="166.5" y1="153.0" x2="166.5" y2="159.0" stroke="currentColor" stroke-width="1"/><text x="166.5" y="170.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="227.8" y1="153.0" x2="227.8" y2="159.0" stroke="currentColor" stroke-width="1"/><text x="227.8" y="170.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="289.0" y1="153.0" x2="289.0" y2="159.0" stroke="currentColor" stroke-width="1"/><text x="289.0" y="170.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="350.2" y1="153.0" x2="350.2" y2="159.0" stroke="currentColor" stroke-width="1"/><text x="350.2" y="170.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="411.5" y1="153.0" x2="411.5" y2="159.0" stroke="currentColor" stroke-width="1"/><text x="411.5" y="170.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="534.0" y1="153.0" x2="534.0" y2="159.0" stroke="currentColor" stroke-width="1"/><text x="534.0" y="170.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="286.0" y1="101.8" x2="292.0" y2="101.8" stroke="currentColor" stroke-width="1"/><text x="40.0" y="105.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="286.0" y1="47.7" x2="292.0" y2="47.7" stroke="currentColor" stroke-width="1"/><text x="40.0" y="51.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><text x="534.0" y="150.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="44.0,156.0 166.5,156.0 166.5,101.8 227.8,101.8 227.8,47.7 350.2,47.7 350.2,101.8 411.5,101.8 411.5,156.0 534.0,156.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/></svg><figcaption><strong>Problem 2(b).</strong> X<sub>d</sub>(ω) = 2 for |ω| ≤ π/4, 1 for π/4 &lt; |ω| ≤ π/2, 0 for π/2 &lt; |ω| ≤ π.</figcaption></figure>
>
> (c) (3 pts) For the $x[n]$ of (b), find $\sum_nx[n]$, $\sum_n(-1)^nx[n]$ and $\sum_nx^2[n]$ without summing a series.

> [!success]- Solution 2
> **(a)** Split at $n=0$, two geometric series ($\lvert\frac12e^{\pm j\omega}\rvert\lt1$):
> $$
> \begin{aligned}
> X_{1,d}(\omega)&=\sum_{n=0}^{\infty}\left(\tfrac12e^{-j\omega}\right)^n+\sum_{n=1}^{\infty}\left(\tfrac12e^{j\omega}\right)^n\\
> &=\frac{1}{1-\frac12e^{-j\omega}}+\frac{\frac12e^{j\omega}}{1-\frac12e^{j\omega}}
> =\frac{1-\frac14}{1+\frac14-\frac12\left(e^{j\omega}+e^{-j\omega}\right)}\\
> &=\frac{\frac34}{\frac54-\cos\omega}
> =\boldsymbol{\frac{3}{5-4\cos\omega}}
> \end{aligned}
> $$
> Check: $X_{1,d}(0)=3=\sum_n(\frac12)^{\lvert n\rvert}=1+2\cdot1$. (Also $X_{1,d}(\pi)=\frac13$.)
>
> **(b)** The staircase is two ideal low-passes of height 1, cutoffs $\frac{\pi}{2}$ and $\frac{\pi}{4}$, added:
> $$
> x[n]=\frac{1}{2\pi}\int_{-\pi/2}^{\pi/2}e^{j\omega n}d\omega+\frac{1}{2\pi}\int_{-\pi/4}^{\pi/4}e^{j\omega n}d\omega
> =\boldsymbol{\frac{\sin(\frac{\pi}{2}n)}{\pi n}+\frac{\sin(\frac{\pi}{4}n)}{\pi n}}
> $$
> $\boldsymbol{x[0]=\frac12+\frac14=\frac34}$ (area $\frac{3\pi}{2}$ over $2\pi$); $\boldsymbol{x[2]=\frac{\sin\pi}{2\pi}+\frac{\sin(\pi/2)}{2\pi}=\frac{1}{2\pi}}$.
>
> **(c)**
> $$
> \begin{gathered}
> \textstyle\sum_nx[n]=X_d(0)=\boldsymbol{2},\qquad\sum_n(-1)^nx[n]=X_d(\pi)=\boldsymbol{0},\\
> \textstyle\sum_nx^2[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d\rvert^2d\omega=\frac{1}{2\pi}\left(4\cdot\frac{\pi}{2}+1\cdot\frac{\pi}{2}\right)=\boldsymbol{\frac54}.
> \end{gathered}
> $$
> Slips: wrong band widths (the $\lvert X_d\rvert^2=4$ band is $\frac{\pi}{2}$ wide, each $\lvert X_d\rvert^2=1$ band $\frac{\pi}{4}$); using $2$ instead of $2^2=4$.

Topic: [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|Parseval]] · family: [[problems/dtft-and-inverse-dtft|DTFTs and inverse DTFTs]]

## Problem 3 · A constant, an alternating sequence and a cosine (10 pts)

> [!question] Problem 3
> An LTI system is described by $y[n]=x[n]+2x[n-2]+x[n-3]$.
>
> (a) (2 pts) Find the frequency response $H_d(\omega)$.
>
> (b) (4 pts) Evaluate $H_d(0)$ and $H_d(\pi)$, and $\lvert H_d(\frac{\pi}{3})\rvert$ and $\angle H_d(\frac{\pi}{3})$ (principal value in $[-\pi,\pi]$).
>
> (c) (4 pts) Find the output for $x[n]=3+2(-1)^n+4\cos\left(\frac{\pi}{3}n+\frac{\pi}{6}\right)$, $-\infty\lt n\lt\infty$.

> [!success]- Solution 3
> **(a)** $\boldsymbol{H_d(\omega)=1+2e^{-j2\omega}+e^{-j3\omega}}$.
>
> **(b)** $H_d(0)=1+2+1=\boldsymbol{4}$, $\;H_d(\pi)=1+2-1=\boldsymbol{2}$.
> $$
> H_d\left(\tfrac{\pi}{3}\right)=1+2e^{-j\frac{2\pi}{3}}+e^{-j\pi}=1+\left(-1-j\sqrt3\right)-1=-1-j\sqrt3 .
> $$
> $\boldsymbol{\lvert H_d(\frac{\pi}{3})\rvert=2}$; the point $(-1,-\sqrt3)$ is in the third quadrant, so $\boldsymbol{\angle H_d(\frac{\pi}{3})=-\pi+\frac{\pi}{3}=-\frac{2\pi}{3}}$ (not $\arctan\sqrt3=\frac{\pi}{3}$).
>
> **(c)** Real taps, so $h$ is real and a cosine is scaled by $\lvert H_d\rvert$ and shifted by $\angle H_d$; $c\mapsto H_d(0)\,c$, $(-1)^n\mapsto H_d(\pi)(-1)^n$:
> $$
> \begin{aligned}
> y[n]&=4\cdot3+2\cdot2\,(-1)^n+4\cdot2\cos\left(\tfrac{\pi}{3}n+\tfrac{\pi}{6}-\tfrac{2\pi}{3}\right)\\
> &=\boldsymbol{12+4(-1)^n+8\sin\left(\tfrac{\pi}{3}n\right)}
> \end{aligned}
> $$
> Slips: angle $\pm\frac{\pi}{3}$ from the calculator-style arctangent; $H_d(\pi)$ taken as $1+2+1$.

Topic: [[concepts/frequency-response|frequency response]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] · family: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]]

## Problem 4 · Linear phase with jumps (10 pts)

> [!question] Problem 4
> An FIR filter is $y[n]=x[n]-x[n-2]+x[n-4]$.
>
> (a) (2 pts) Write $H_d(\omega)=e^{-jM\omega}R(\omega)$ with $R(\omega)$ real.
>
> (b) (3 pts) Sketch $\lvert H_d(\omega)\rvert$ for $-\pi\le\omega\le\pi$; label its zeros and its values at $0$, $\frac{\pi}{3}$, $\frac{\pi}{2}$ and $\pi$.
>
> (c) (3 pts) Sketch $\angle H_d(\omega)$ for $-\pi\le\omega\le\pi$ as a principal value; label every jump.
>
> (d) (2 pts) Give the group delay, and the output for $x[n]=\cos(\frac{\pi}{2}n)$.

> [!success]- Solution 4
> **(a)** Symmetric about $n=2$; pull out $e^{-j2\omega}$:
> $$
> \begin{aligned}
> H_d(\omega)&=1-e^{-j2\omega}+e^{-j4\omega}=e^{-j2\omega}\left(e^{j2\omega}-1+e^{-j2\omega}\right)\\
> &=\boldsymbol{e^{-j2\omega}\left(2\cos2\omega-1\right)},\qquad M=2,\quad R(\omega)=2\cos2\omega-1 .
> \end{aligned}
> $$
> **(b)** $\lvert H_d(\omega)\rvert=\lvert2\cos2\omega-1\rvert$, even, period $\pi$:
>
> | $\omega$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{5\pi}{6}$ | $\pi$ |
> |---|---|---|---|---|---|---|---|
> | $R(\omega)$ | $1$ | $0$ | $-2$ | $-3$ | $-2$ | $0$ | $1$ |
> | $\lvert H_d\rvert$ | $1$ | $0$ | $2$ | $3$ | $2$ | $0$ | $1$ |
>
> Zeros at $\pm\frac{\pi}{6}$, $\pm\frac{5\pi}{6}$; peak 3 at $\pm\frac{\pi}{2}$; a cosine-shaped arch between the zeros, small bumps of height 1 at $0$ and $\pm\pi$.
>
> **(c)** $-2\omega$ where $R\gt0$, $-2\omega+\pi$ where $R\lt0$, wrapped into $[-\pi,\pi]$; odd in $\omega$:
> $$
> \angle H_d(\omega)=\begin{cases}-2\omega, & 0\le\omega\lt\frac{\pi}{6}\\ \pi-2\omega, & \frac{\pi}{6}\lt\omega\lt\frac{5\pi}{6}\\ 2\pi-2\omega, & \frac{5\pi}{6}\lt\omega\le\pi\end{cases}
> $$
> and $\angle H_d(-\omega)=-\angle H_d(\omega)$.
> Slope $-2$ throughout: from 0 down to $-\frac{\pi}{3}$; **jump $+\pi$ at $\frac{\pi}{6}$** to $\frac{2\pi}{3}$, through 0 at $\frac{\pi}{2}$, down to $-\frac{2\pi}{3}$; **jump $+\pi$ at $\frac{5\pi}{6}$** to $\frac{\pi}{3}$, down to 0 at $\pi$. Mirror (odd) for $\omega\lt0$.
>
> **(d)** $\boldsymbol{\tau_{gd}=2}$ samples (slope $-2$ between the jumps, which sit at zeros of $H_d$). $H_d(\frac{\pi}{2})=e^{-j\pi}(-3)=3$, so $\boldsymbol{y[n]=3\cos(\frac{\pi}{2}n)}$. Check: $x[n-2]=-\cos(\frac{\pi}{2}n)$, $x[n-4]=\cos(\frac{\pi}{2}n)$.
>
> Slips: plotting $2\cos2\omega-1$ as the magnitude (negative values); a phase of $-\pi$ at $\frac{\pi}{2}$ (the sign of $R$ cancels it).

Topic: [[concepts/magnitude-and-phase-response|magnitude and phase]] · [[concepts/group-delay|group delay]] · family: [[problems/magnitude-phase-and-group-delay|magnitude, phase, group delay]]

## Problem 5 · Sampling a triangle, with and without overlap (10 pts)

> [!question] Problem 5
> $x_a(t)$ has the CTFT $X_a(\Omega)$ in the left panel below: a triangle of height 1, zero for $\lvert\Omega\rvert\ge800\pi$ rad/s. It is sampled, $x[n]=x_a(nT)$. (The right panel belongs to Problem 6.)
>
> <figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 200" width="640" height="200" role="img" aria-label="Left: triangle X_a of height 1 from -800pi to 800pi rad/s. Right: ideal low-pass H_d equal to 1 for |w| &lt;= w_c" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="175.0" y="20.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">X<tspan baseline-shift="sub" style="font-size:75%">a</tspan>(Ω)</text><line x1="40.0" y1="54.0" x2="310.0" y2="54.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="166.0" x2="310.0" y2="166.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="175.0" y1="26.0" x2="175.0" y2="166.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="67.0" y1="163.0" x2="67.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="67.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−800π</text><line x1="175.0" y1="163.0" x2="175.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="175.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="283.0" y1="163.0" x2="283.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="283.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">800π</text><line x1="172.0" y1="54.0" x2="178.0" y2="54.0" stroke="currentColor" stroke-width="1"/><text x="36.0" y="58.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="310.0" y="160.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">Ω</text><polyline points="40.0,166.0 67.0,166.0 175.0,54.0 283.0,166.0 310.0,166.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="490.0" y="20.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω), Problem 6(a)</text><line x1="360.0" y1="54.0" x2="620.0" y2="54.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="166.0" x2="620.0" y2="166.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="490.0" y1="26.0" x2="490.0" y2="166.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="360.0" y1="163.0" x2="360.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="360.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="425.0" y1="163.0" x2="425.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="425.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−ω<tspan baseline-shift="sub" style="font-size:75%">c</tspan></text><line x1="490.0" y1="163.0" x2="490.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="490.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="555.0" y1="163.0" x2="555.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="555.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">ω<tspan baseline-shift="sub" style="font-size:75%">c</tspan></text><line x1="620.0" y1="163.0" x2="620.0" y2="169.0" stroke="currentColor" stroke-width="1"/><text x="620.0" y="180.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="487.0" y1="54.0" x2="493.0" y2="54.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="58.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="620.0" y="160.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="360.0,166.0 425.0,166.0 425.0,54.0 555.0,54.0 555.0,166.0 620.0,166.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/></svg><figcaption><strong>Problems 5 and 6.</strong> Left: the input spectrum X<sub>a</sub>(Ω), a triangle of height 1 that reaches 0 at ±800π rad/s (400 Hz). Right: the ideal digital low-pass of Problem 6(a), 1 for |ω| ≤ ω<sub>c</sub> and 0 for ω<sub>c</sub> &lt; |ω| ≤ π.</figcaption></figure>
>
> (a) (2 pts) Find the Nyquist rate (Hz) and the Nyquist sampling period.
>
> (b) (3 pts) Sketch $X_d(\omega)$ for $-\pi\le\omega\le\pi$ when $T=\frac{1}{1600}$ s.
>
> (c) (4 pts) Sketch $X_d(\omega)$ for $-\pi\le\omega\le\pi$ when $T=\frac{1}{600}$ s. Label heights and break points.
>
> (d) (1 pt) From your sketch in (c), find $x[0]$, and check it against $x_a(0)$.

> [!success]- Solution 5
> $X_d(\omega)=\frac1T\sum_kX_a\left(\frac{\omega-2\pi k}{T}\right)$: copies every $2\pi$, height $\frac1T$, central copy ending at $\omega=800\pi T$.
>
> **(a)** $B=\frac{800\pi}{2\pi}=400$ Hz: $\boldsymbol{f_N=800}$ **Hz**, $\boldsymbol{T_N=\frac{1}{800}}$ **s** $=1.25$ ms (equality is harmless here: $X_a(\pm800\pi)=0$).
>
> **(b)** Edge $\frac{800\pi}{1600}=\frac{\pi}{2}$, no overlap: $\boldsymbol{X_d(\omega)=1600\left(1-\frac{2\lvert\omega\rvert}{\pi}\right)}$ for $\lvert\omega\rvert\le\frac{\pi}{2}$, $0$ for $\frac{\pi}{2}\lt\lvert\omega\rvert\le\pi$.
>
> **(c)** $f_s=600\lt800$ Hz: edge $\frac{800\pi}{600}=\frac{4\pi}{3}\gt\pi$, overlap. On $[0,\pi]$ the central copy is $600\left(1-\frac{3\omega}{4\pi}\right)$; the copy at $2\pi$ adds $600\left(1-\frac{3(2\pi-\omega)}{4\pi}\right)$ for $\omega\ge\frac{2\pi}{3}$, and the sum is $600\left(2-\frac32\right)=300$:
> $$
> \boldsymbol{X_d(\omega)=\begin{cases}600-\frac{450}{\pi}\lvert\omega\rvert, & \lvert\omega\rvert\le\frac{2\pi}{3}\\ 300, & \frac{2\pi}{3}\le\lvert\omega\rvert\le\pi\end{cases}}
> $$
> A roof falling from 600 at $0$ to 300 at $\pm\frac{2\pi}{3}$, then flat at 300 out to $\pm\pi$ (where it meets the next period).
>
> **(d)** Area under (c) over $2\pi$:
> $$
> x[0]=\frac{1}{2\pi}\cdot2\left[\frac{600+300}{2}\cdot\frac{2\pi}{3}+300\cdot\frac{\pi}{3}\right]=\frac{300\pi+100\pi}{\pi}=\boldsymbol{400},
> $$
> equal to $x_a(0)=\frac{1}{2\pi}\cdot\frac12\cdot1600\pi=400$: aliasing changes the spectrum's shape, never the samples.

Topic: [[concepts/sampling|sampling]] · [[concepts/nyquist-criterion|Nyquist criterion]] · family: [[problems/sampling-and-the-nyquist-rate|sampling and the Nyquist rate]]

## Problem 6 · A digital filter between ideal converters (12 pts)

> [!question] Problem 6
> The $x_a(t)$ of Problem 5 passes through an ideal A/D with period $T$, a digital filter $H_d(\omega)$, and an ideal D/A with the same $T$, giving $y_a(t)$.
>
> (a) (5 pts) Let $T=\frac{1}{1200}$ s and $H_d$ the ideal low-pass with $\omega_c=\frac{\pi}{2}$ (right panel of the figure in Problem 5). Sketch $X_d(\omega)$, $Y_d(\omega)$ and $Y_a(\Omega)$ with labels. Which analog cutoff, in Hz, does the system realise?
>
> (b) (4 pts) We want $y_a(t)$ to be $x_a(t)$ with every frequency above 100 Hz removed and everything below 100 Hz unchanged. Find the largest $T$ and the cutoff $\omega_c$ of the ideal digital low-pass.
>
> (c) (3 pts) Now we want to keep only the frequencies above 100 Hz, with an ideal digital high-pass ($H_d=1$ for $\omega_c\le\lvert\omega\rvert\le\pi$, 0 otherwise). Find the largest $T$ and $\omega_c$. Why is this $T$ smaller than in (b)?

> [!success]- Solution 6(a)
> Edge $800\pi T=\frac{2\pi}{3}\lt\pi$: no aliasing.
> - $X_d$: triangle of height **1200**, edges $\pm\frac{2\pi}{3}$, repeated every $2\pi$.
> - $Y_d=H_dX_d$: the triangle cut at $\pm\frac{\pi}{2}$, where $X_d=1200\left(1-\frac{\pi/2}{2\pi/3}\right)=\boldsymbol{300}$; zero for $\frac{\pi}{2}\lt\lvert\omega\rvert\le\pi$.
> - $Y_a(\Omega)=T\,Y_d(\Omega T)$ for $\lvert\Omega\rvert\lt\frac{\pi}{T}=1200\pi$: height **1** at 0, cut at $\Omega=\frac{\pi/2}{T}=600\pi$ rad/s with value $\boldsymbol{\frac14}$, zero beyond. So $Y_a=X_a$ for $\lvert\Omega\rvert\le600\pi$: a cutoff of **300 Hz**.

> [!success]- Solution 6(b)–(c)
> **(b)** $\omega_c=2\pi\cdot100\cdot T=200\pi T$. Aliasing above the cutoff is harmless, so only the copy centred at $2\pi$, which starts at $2\pi-800\pi T$, must stay out of the passband:
> $$
> \begin{gathered}
> 200\pi T\le2\pi-800\pi T\iff T\le\frac{1}{500}\ \text{s},\\
> \boldsymbol{T=\frac{1}{500}\ \text{s},\qquad\omega_c=\frac{200\pi}{500}=\frac{2\pi}{5}}.
> \end{gathered}
> $$
> The D/A covers $\lvert\Omega\rvert\lt500\pi$, enough for the $200\pi$ rad/s passband. The Nyquist period $\frac{1}{800}$ s also works but is not the largest.
>
> **(c)** The output contains 100–400 Hz, so the D/A must reach 400 Hz ($\frac{\pi}{T}\ge800\pi$) and no copy may enter $[\omega_c,\pi]$:
> $$
> \boldsymbol{T=\frac{1}{800}\ \text{s},\quad\omega_c=\frac{200\pi}{800}=\frac{\pi}{4}}
> $$
> (the copies just touch at $\pm\pi$, where $X_d=0$). A low-pass discards the top of the band, so that part may alias; a high-pass keeps it, so nothing may.

Topic: [[concepts/digital-processing-of-analog-signals|A/D → filter → D/A]] · [[concepts/ideal-reconstruction|ideal D/A]] · family: [[problems/digital-filtering-of-analog-signals|digital filtering of analog signals]]

## Problem 7 · Three sinusoids through A/D and D/A (8 pts)

> [!question] Problem 7
> $x_a(t)=3\cos\left(200\pi t+\frac{\pi}{4}\right)+2\sin(700\pi t)+5\cos(1000\pi t)$ is sampled at $f_s=500$ Hz and reconstructed by an ideal D/A at the same rate.
>
> (a) (2 pts) What is the Nyquist rate of $x_a(t)$?
>
> (b) (3 pts) Write $x[n]$ with every digital frequency in $[0,\pi]$.
>
> (c) (3 pts) Find the D/A output $y_a(t)$.

> [!success]- Solution 7
> **(a)** Highest frequency 500 Hz: $\boldsymbol{1000}$ **Hz**. At 500 Hz two terms alias.
>
> **(b)** $\omega=\frac{2\pi f}{f_s}$: 100 Hz $\to\frac{2\pi}{5}$; 350 Hz $\to\frac{7\pi}{5}\equiv-\frac{3\pi}{5}$; 500 Hz $\to2\pi\equiv0$:
> $$
> \begin{aligned}
> x[n]&=3\cos\left(\tfrac{2\pi}{5}n+\tfrac{\pi}{4}\right)+2\sin\left(-\tfrac{3\pi}{5}n\right)+5\cos(2\pi n)\\
> &=\boldsymbol{5+3\cos\left(\tfrac{2\pi}{5}n+\tfrac{\pi}{4}\right)-2\sin\left(\tfrac{3\pi}{5}n\right)}
> \end{aligned}
> $$
> **(c)** The D/A turns $\omega\in[0,\pi]$ into $\frac{\omega f_s}{2\pi}$ Hz: $\frac{2\pi}{5}\to100$ Hz, $\frac{3\pi}{5}\to150$ Hz, $0\to$ DC:
> $$
> \boldsymbol{y_a(t)=5+3\cos\left(200\pi t+\tfrac{\pi}{4}\right)-2\sin(300\pi t)}
> $$
> Slips: $+2\sin(300\pi t)$ (a folded sine changes sign); dropping the 500 Hz term (sampled at $f_s$ it is the constant 5, not 0).

Topic: [[concepts/aliasing|aliasing]] · [[concepts/ideal-reconstruction|ideal D/A]] · family: [[problems/sampling-and-the-nyquist-rate|sampling and the Nyquist rate]]

## Problem 8 · DFT values and properties (12 pts)

> [!question] Problem 8
> Let $\{x[n]\}_{n=0}^{7}=\{3,\ 1,\ -2,\ 0,\ 1,\ 2,\ 0,\ -1\}$ have DFT $\{X[k]\}_{k=0}^{7}=\{X_0,X_1,\dots,X_7\}$.
>
> (a) (3 pts) Compute $X[0]$, $X[4]$ and $X[2]$.
>
> (b) (2 pts) $z[n]$ is $x[n]$ zero-padded to length 24, with DFT $Z[k]$. Give $Z[6]$, $Z[12]$ and $Z[18]$ as numbers. Which $Z[k]$ equal one of the $X[m]$?
>
> (c) (2 pts) The samples are $x[n]=x_a(n/f_s)$ with $f_s=2.4$ kHz. What is the bin spacing of $X[k]$ and of $Z[k]$ in Hz? Which analog frequency does $X[2]$ sample, and which does $Z[18]$?
>
> (d) (2 pts) $\{y[n]\}_{n=0}^{7}=\{0,\ 1,\ 2,\ 0,\ -1,\ 3,\ 1,\ -2\}$. Express $Y[k]$ in terms of $X[k]$, and give $Y[2]$ as a number.
>
> (e) (3 pts) Find, as lists, the signal $v[n]$ with DFT $V[k]=\{X_4,X_5,X_6,X_7,X_0,X_1,X_2,X_3\}$ and the signal $w[n]$ with DFT $W[k]=X^*[k]$.

> [!success]- Solution 8
> **(a)** $X[0]=\sum_nx[n]=\boldsymbol{4}$; $\;X[4]=\sum_n(-1)^nx[n]=3-1-2-0+1-2+0+1=\boldsymbol{0}$. For $k=2$, $e^{-j\frac{2\pi\cdot2}{8}n}=(-j)^n=\{1,-j,-1,j,1,-j,-1,j\}$:
> $$
> X[2]=3-j+2+0+1-2j+0-j=\boldsymbol{6-4j}.
> $$
> **(b)** $Z[k]=X_d(\frac{2\pi k}{24})$ and $X[m]=X_d(\frac{2\pi m}{8})=Z[3m]$: **every third bin** of $Z$ is an $X$ value, the others are new DTFT samples.
> $\boldsymbol{Z[6]=X[2]=6-4j}$, $\;\boldsymbol{Z[12]=X[4]=0}$, $\;\boldsymbol{Z[18]=X[6]=X^*[2]=6+4j}$ ($x$ real).
>
> **(c)** $f_k=\frac{kf_s}{N}$: **300 Hz** per bin for $X$, **100 Hz** for $Z$. $X[2]\leftrightarrow\boldsymbol{600}$ **Hz**; $Z[18]\leftrightarrow1800$ Hz $\equiv1800-2400=\boldsymbol{-600}$ **Hz**, the negative-frequency partner of 600 Hz (hence $Z[18]=Z^*[6]$).
>
> **(d)** $y[0]=x[3]$, $y[1]=x[4]$, …: $y[n]=x[\langle n+3\rangle_8]$, a circular advance by 3 (delay by 5):
> $$
> \begin{gathered}
> \boldsymbol{Y[k]=e^{j\frac{2\pi\cdot3}{8}k}X[k]=e^{j\frac{3\pi}{4}k}X[k]},\\
> Y[2]=e^{j\frac{3\pi}{2}}(6-4j)=-j(6-4j)=\boldsymbol{-4-6j}.
> \end{gathered}
> $$
> **(e)** $V[k]=X[\langle k-4\rangle_8]$, a frequency shift by $\frac N2$: $v[n]=e^{j\frac{2\pi\cdot4}{8}n}x[n]=(-1)^nx[n]$,
> $$
> \boldsymbol{v[n]=\{3,\ -1,\ -2,\ 0,\ 1,\ -2,\ 0,\ 1\}}.
> $$
> Conjugation $x^*[n]\leftrightarrow X^*[\langle -k\rangle_8]$, so $X^*[k]\leftrightarrow x^*[\langle -n\rangle_8]=x[\langle -n\rangle_8]$ (real $x$), which keeps $x[0]$ and reverses the rest:
> $$
> \boldsymbol{w[n]=\{3,\ -1,\ 0,\ 2,\ 1,\ 0,\ -2,\ 1\}}.
> $$
> Slips: $e^{-j\frac{3\pi}{4}k}$ (wrong direction); reversing all eight values, $\{-1,0,2,1,0,-2,1,3\}$.

Topic: [[concepts/dft|DFT]] · [[concepts/zero-padding|zero padding]] · [[concepts/circular-shift-and-reversal|circular shift and reversal]] · [[concepts/dft-properties|DFT properties]] · family: [[problems/dft-values-and-zero-padding|DFT values and zero padding]] · [[problems/circular-convolution-and-dft-properties|DFT properties]]

## Problem 9 · Reading a DFT plot; resolution and windows (12 pts)

> [!question] Problem 9
> $x_a(t)=A_1\cos(2\pi f_1t)+A_2\cos(2\pi f_2t)$ with $0\lt f_1\lt f_2\lt1600$ Hz, $A_1$ and $A_2$ positive integers, both frequencies multiples of 50 Hz. It is sampled at $f_s=3.2$ kHz, and the 32-point DFT of $\{x[n]\}_{n=0}^{31}$ has the magnitude below (rectangular window).
>
> <figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="Stem plot of |X[k]| for k = 0..31 with peaks of 49 at k = 4 and 28 and a broad hump of about 10.2 at k = 8, 9 and 23, 24" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="329.0" y="20.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X[k]|, 0 ≤ k ≤ 31</text><line x1="44.0" y1="173.3" x2="614.0" y2="173.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="44.0" y1="140.5" x2="614.0" y2="140.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="44.0" y1="107.8" x2="614.0" y2="107.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="44.0" y1="75.1" x2="614.0" y2="75.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="44.0" y1="42.4" x2="614.0" y2="42.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="44.0" y1="206.0" x2="614.0" y2="206.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="58.0" y1="26.0" x2="58.0" y2="206.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="58.0" y1="203.0" x2="58.0" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="58.0" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="127.9" y1="203.0" x2="127.9" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="127.9" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">4</text><line x1="197.9" y1="203.0" x2="197.9" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="197.9" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">8</text><line x1="267.8" y1="203.0" x2="267.8" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="267.8" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">12</text><line x1="337.7" y1="203.0" x2="337.7" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="337.7" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">16</text><line x1="407.7" y1="203.0" x2="407.7" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="407.7" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">20</text><line x1="477.6" y1="203.0" x2="477.6" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="477.6" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">24</text><line x1="547.6" y1="203.0" x2="547.6" y2="209.0" stroke="currentColor" stroke-width="1"/><text x="547.6" y="220.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">28</text><line x1="55.0" y1="173.3" x2="61.0" y2="173.3" stroke="currentColor" stroke-width="1"/><text x="40.0" y="177.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">10</text><line x1="55.0" y1="140.5" x2="61.0" y2="140.5" stroke="currentColor" stroke-width="1"/><text x="40.0" y="144.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">20</text><line x1="55.0" y1="107.8" x2="61.0" y2="107.8" stroke="currentColor" stroke-width="1"/><text x="40.0" y="111.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">30</text><line x1="55.0" y1="75.1" x2="61.0" y2="75.1" stroke="currentColor" stroke-width="1"/><text x="40.0" y="79.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">40</text><line x1="55.0" y1="42.4" x2="61.0" y2="42.4" stroke="currentColor" stroke-width="1"/><text x="40.0" y="46.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">50</text><text x="614.0" y="200.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">k</text><line x1="58.0" y1="206.0" x2="58.0" y2="202.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="58.0" cy="202.7" r="3.2" fill="var(--accent)"/><line x1="75.5" y1="206.0" x2="75.5" y2="202.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="75.5" cy="202.7" r="3.2" fill="var(--accent)"/><line x1="93.0" y1="206.0" x2="93.0" y2="202.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="93.0" cy="202.5" r="3.2" fill="var(--accent)"/><line x1="110.4" y1="206.0" x2="110.4" y2="202.2" stroke="var(--accent)" stroke-width="1.6"/><circle cx="110.4" cy="202.2" r="3.2" fill="var(--accent)"/><line x1="127.9" y1="206.0" x2="127.9" y2="45.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="127.9" cy="45.6" r="3.2" fill="var(--accent)"/><line x1="145.4" y1="206.0" x2="145.4" y2="200.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="145.4" cy="200.7" r="3.2" fill="var(--accent)"/><line x1="162.9" y1="206.0" x2="162.9" y2="198.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="162.9" cy="198.9" r="3.2" fill="var(--accent)"/><line x1="180.4" y1="206.0" x2="180.4" y2="194.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="180.4" cy="194.6" r="3.2" fill="var(--accent)"/><line x1="197.9" y1="206.0" x2="197.9" y2="172.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="197.9" cy="172.5" r="3.2" fill="var(--accent)"/><line x1="215.3" y1="206.0" x2="215.3" y2="172.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="215.3" cy="172.8" r="3.2" fill="var(--accent)"/><line x1="232.8" y1="206.0" x2="232.8" y2="194.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="232.8" cy="194.9" r="3.2" fill="var(--accent)"/><line x1="250.3" y1="206.0" x2="250.3" y2="199.2" stroke="var(--accent)" stroke-width="1.6"/><circle cx="250.3" cy="199.2" r="3.2" fill="var(--accent)"/><line x1="267.8" y1="206.0" x2="267.8" y2="201.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="267.8" cy="201.0" r="3.2" fill="var(--accent)"/><line x1="285.3" y1="206.0" x2="285.3" y2="201.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="285.3" cy="201.9" r="3.2" fill="var(--accent)"/><line x1="302.8" y1="206.0" x2="302.8" y2="202.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="302.8" cy="202.4" r="3.2" fill="var(--accent)"/><line x1="320.3" y1="206.0" x2="320.3" y2="202.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="320.3" cy="202.6" r="3.2" fill="var(--accent)"/><line x1="337.7" y1="206.0" x2="337.7" y2="202.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="337.7" cy="202.7" r="3.2" fill="var(--accent)"/><line x1="355.2" y1="206.0" x2="355.2" y2="202.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="355.2" cy="202.6" r="3.2" fill="var(--accent)"/><line x1="372.7" y1="206.0" x2="372.7" y2="202.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="372.7" cy="202.4" r="3.2" fill="var(--accent)"/><line x1="390.2" y1="206.0" x2="390.2" y2="201.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="390.2" cy="201.9" r="3.2" fill="var(--accent)"/><line x1="407.7" y1="206.0" x2="407.7" y2="201.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="407.7" cy="201.0" r="3.2" fill="var(--accent)"/><line x1="425.2" y1="206.0" x2="425.2" y2="199.2" stroke="var(--accent)" stroke-width="1.6"/><circle cx="425.2" cy="199.2" r="3.2" fill="var(--accent)"/><line x1="442.7" y1="206.0" x2="442.7" y2="194.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="442.7" cy="194.9" r="3.2" fill="var(--accent)"/><line x1="460.1" y1="206.0" x2="460.1" y2="172.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="460.1" cy="172.8" r="3.2" fill="var(--accent)"/><line x1="477.6" y1="206.0" x2="477.6" y2="172.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="477.6" cy="172.5" r="3.2" fill="var(--accent)"/><line x1="495.1" y1="206.0" x2="495.1" y2="194.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="495.1" cy="194.6" r="3.2" fill="var(--accent)"/><line x1="512.6" y1="206.0" x2="512.6" y2="198.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="512.6" cy="198.9" r="3.2" fill="var(--accent)"/><line x1="530.1" y1="206.0" x2="530.1" y2="200.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="530.1" cy="200.7" r="3.2" fill="var(--accent)"/><line x1="547.6" y1="206.0" x2="547.6" y2="45.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="547.6" cy="45.6" r="3.2" fill="var(--accent)"/><line x1="565.0" y1="206.0" x2="565.0" y2="202.2" stroke="var(--accent)" stroke-width="1.6"/><circle cx="565.0" cy="202.2" r="3.2" fill="var(--accent)"/><line x1="582.5" y1="206.0" x2="582.5" y2="202.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="582.5" cy="202.5" r="3.2" fill="var(--accent)"/><line x1="600.0" y1="206.0" x2="600.0" y2="202.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="600.0" cy="202.7" r="3.2" fill="var(--accent)"/><text x="127.9" y="37.6" text-anchor="middle" fill="var(--accent)" style="font-size:11px">49</text><text x="547.6" y="37.6" text-anchor="middle" fill="var(--accent)" style="font-size:11px">49</text><text x="180.4" y="186.6" text-anchor="middle" fill="var(--accent)" style="font-size:10px">3.5</text><text x="232.8" y="186.9" text-anchor="middle" fill="var(--accent)" style="font-size:10px">3.4</text><text x="442.7" y="186.9" text-anchor="middle" fill="var(--accent)" style="font-size:10px">3.4</text><text x="495.1" y="186.6" text-anchor="middle" fill="var(--accent)" style="font-size:10px">3.5</text><text x="199.9" y="164.5" text-anchor="end" fill="var(--accent)" style="font-size:10px">10.3</text><text x="462.1" y="164.8" text-anchor="end" fill="var(--accent)" style="font-size:10px">10.2</text><text x="213.3" y="164.8" text-anchor="start" fill="var(--accent)" style="font-size:10px">10.2</text><text x="475.6" y="164.5" text-anchor="start" fill="var(--accent)" style="font-size:10px">10.3</text></svg><figcaption><strong>Problem 9.</strong> |X[k]| of the 32 samples. Labelled: 49 at k = 4 and 28; 3.5, 10.3, 10.2, 3.4 at k = 7 to 10, mirrored at k = 25 down to 22; every other bin lies between 1.0 and 2.2.</figcaption></figure>
>
> (a) (3 pts) One component lies exactly on a DFT bin. Which one? Find its frequency in Hz, its $\omega$ and its amplitude.
>
> (b) (3 pts) Find $f_2$ and $\omega_2$. Explain why $\frac{2\lvert X[8]\rvert}{N}$ underestimates $A_2$, and find $A_2$ using $\lvert C(\frac{\pi}{N})\rvert=\frac{1}{\sin(\pi/2N)}\approx\frac{2N}{\pi}$ (the periodic sinc half a bin from its peak).
>
> (c) (3 pts) A new recording at the same $f_s$ holds two equal-amplitude tones at 400 Hz and 450 Hz. Find the smallest $N$, and the record length in ms, for full-lobe separation with a rectangular window, and with a Hamming window. Would zero-padding the 32-sample record to 1024 points separate them?
>
> (d) (3 pts) Your lab partner multiplies the 32 samples by a Hamming window before the DFT and claims: "the peak at $k=4$ gets narrower, and $A_1$ is still $\frac{2\lvert X_w[4]\rvert}{N}$." Correct both claims, and say what the window does to the leakage of the $f_2$ tone.

> [!success]- Solution 9
> Bin spacing $\frac{f_s}{N}=100$ Hz; $\omega_k=\frac{2\pi k}{32}$. Bins $k\gt16$ mirror $k\lt16$ (real $x$).
>
> **(a)** Bin 4 (mirror 28) is a lone spike; its neighbours (1.2–1.6) are only the other tone's leakage. An on-bin cosine has height $\frac{AN}{2}=16A$:
> $$
> \boldsymbol{f_1=400\ \text{Hz},\quad\omega_1=\frac{2\pi\cdot4}{32}=\frac{\pi}{4},\quad A_1=3}
> $$
> ($\lvert X[4]\rvert=49$: $16A_1=48$ plus about 1 of leakage from the other tone; $A_1$ is an integer.)
>
> **(b)** Two nearly equal tallest bins, 8 and 9 (10.3, 10.2), with sloping neighbours (3.5, 3.4): one main lobe centred halfway, $k_0=8.5$ (800 or 900 Hz, on the 50 Hz grid, would be a lone spike like bin 4):
> $$
> \boldsymbol{f_2=850\ \text{Hz},\qquad\omega_2=\frac{2\pi\cdot8.5}{32}=\frac{17\pi}{32}}.
> $$
> Bins 8 and 9 sample the lobe half a bin from its peak, not at it (leakage, the picket-fence loss), so they sit below $\frac{A_2N}{2}=16A_2$:
> $$
> \lvert X[8]\rvert\approx\frac{A_2}{2}\cdot\frac{2N}{\pi}=\frac{32A_2}{\pi}\approx10.2A_2\quad\Rightarrow\quad\boldsymbol{A_2=1}.
> $$
> The naive $\frac{2\cdot10.3}{32}\approx0.64$ is $\frac{2}{\pi}$ of the truth.
>
> **(c)** $\Delta\omega=\frac{2\pi\cdot50}{3200}=\frac{\pi}{32}$.
> - Rectangular, main lobe $\frac{4\pi}{N}$: $N\gt\frac{4\pi}{\Delta\omega}=128$ $\Rightarrow$ $\boldsymbol{N=129}$, $\frac{129}{3200}\approx$ **40.3 ms** (any record longer than $\frac{2}{\Delta f}=40$ ms).
> - Hamming, main lobe $\frac{8\pi}{N}$: $N\gt256$ $\Rightarrow$ $\boldsymbol{N=257}$, about **80.3 ms**.
> - Padding: **no**. 32 samples give lobes $\frac{4\pi}{32}=\frac{\pi}{8}$ wide, four times $\Delta\omega$; padding samples the same merged lobe more finely.
>
> **(d)** Both claims are wrong.
> - Hamming **widens** the main lobe to $\frac{8\pi}{N}$ (the $k=4$ peak now spreads over bins 3–5, about 11, 25, 11) in exchange for side lobes at $-42$ dB instead of $-13$ dB.
> - An on-bin peak is $\frac{A_1}{2}\sum_nw[n]$, with $\sum_nw[n]\approx0.54N$ (16.8 for $N=32$): $\lvert X_w[4]\rvert\approx25.3$, so $A_1=\frac{2\lvert X_w[4]\rvert}{\sum_nw[n]}=3$; dividing by $N$ gives about 1.6.
> - The $f_2$ tone's leakage into far bins ($k=11$ to 16) drops from 1.0–2.1 to below 0.1; its own lobe widens and its tallest bins drop to about 6.9.

Topic: [[concepts/spectral-leakage|spectral leakage]] · [[concepts/spectral-analysis|spectral analysis]] · [[concepts/frequency-resolution|lobe separation]] · [[concepts/window-functions|windows]] · family: [[problems/dft-spectral-analysis|DFT spectral analysis]]

## Grading

| problem | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | total |
|---|---|---|---|---|---|---|---|---|---|---|
| points | 16 | 10 | 10 | 10 | 10 | 12 | 8 | 12 | 12 | 100 |
| yours | | | | | | | | | | |

By unit: Unit 3 (#1(a)–(b), #2–#4) 34 points · Unit 4 (#1(c)–(d), #5–#7) 34 · Unit 5 (#1(e)–(h), #8–#9) 32. A unit under about two-thirds of its points: go back to its topic pages and families before the next timed run ([[exams/midterm-2/past-exams/spring-2025|SP2025]], then [[exams/midterm-2/past-exams/fall-2024|FA2024]]).

## Related
[[exams/midterm-2/index|Midterm 2]] · [[exams/midterm-2/past-exams/index|past exams]] · [[exams/midterm-2/true-false-bank|T/F bank]] · [[problems/index|problem families]] · [[concepts/index|topic pages]] · [[demos/practice-drills|drills]] · [[exams/index|all exams]]

### Sources for this page
New problems in the format and point weights of the seven past Midterm 2 exams (FA2019–SP2025); scope from the course website (Oct 30) and the instructor's announcement; numbers checked in `verify/MT2_PRACTICE_numbers.py`, figures from `verify/MT2_PRACTICE_figs.py`.
