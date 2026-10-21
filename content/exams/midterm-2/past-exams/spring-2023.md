---
title: "Spring 2023 · Midterm 2"
description: "Spring 2023 ECE 310 Midterm 2 (Liang, Moon, Snyder) with folded solutions: T/F, DTFT symmetry vs periodicity, inverse DTFT of an impulse, a comb filter, a complex response, an odd undersampled spectrum, aliased cosines, DFT problems."
tags: [exam, midterm-2]
---

*Wed Apr 5, 2023 · 7:00–9:00 pm · Profs. Liang, Moon, Snyder · 10 problems, 100 points · one handwritten two-sided sheet, no calculator · "calculate / determine / find" means closed form · T/F +2 / −1 / 0 blank · typed key.*

> [!abstract] What this exam adds
> First Snyder MT2, close to ours: symmetry vs periodicity (#2–#3), comb magnitude/phase with $\pi$ jumps (#5), complex $h[n]$ making a real sine imaginary (#6), an odd spectrum that cancels when undersampled (#7). Key answers right; three cosmetic slips.

## Map of the exam

| # | pts | what it asks | topic · problem family | lectures |
|---|---|---|---|---|
| 1 | 10 | five True/False statements (+2/−1/0) | T/F: sampling, Nyquist rate of $x_c(3t)$, zero padding, IDFT periodicity, bandlimited | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]], [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion\|L17]] (sampling, Nyquist rate, bandlimited), [[5-dft-and-fft/20-discrete-fourier-transform\|L20]] (d) (DFT) |
| 2 | 3 | $X_d$ of a **real** sequence on $[-\pi, 0]$, given $X_d = j\omega$ on $[0, \pi]$ | DTFT symmetry · [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] | [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 3 | 3 | same for an **arbitrary** sequence, on $[2\pi, 3\pi]$ | DTFT periodicity · [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] |
| 4 | 5 | inverse DTFT of $5e^{j\pi\omega}\delta(\omega - \omega_0)$ | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] | [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 5 | 14 | $H_d$ of $\delta[n] + \delta[n-6]$; plot magnitude and phase | [[problems/magnitude-phase-and-group-delay\|magnitude, phase and group delay]] | [[3-fourier-analysis/15-frequency-response\|L15]], [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] |
| 6 | 8 | response of $H_d(\omega) = \omega e^{j\pi\cos\omega}$ to $3 + e^{j\frac{\pi}{3}n} + \sin(\frac{\pi}{2}n + \frac{\pi}{4})$ | [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] | [[3-fourier-analysis/15-frequency-response\|L15]] |
| 7 | 20 | ideal A/D → $H_d$ → ideal D/A: Nyquist rate; sketch $X_d$, $Y_d$ at two sampling rates | sampling · ideal filters · [[problems/digital-filtering-of-analog-signals\|digital filtering of analog signals]] | [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion\|L17]] (Nyquist rate, the sketches of $X_d$), [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion\|L18]], [[4-sampling-and-reconstruction/19-aliasing\|L19]] |
| 8 | 10 | sampling periods consistent with a given $x[n]$ and a given $y_c(t)$ | [[problems/sampling-and-the-nyquist-rate\|sampling and the Nyquist rate]] · reconstruction | [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion\|L17]] (which $T$ give $x[n]$), [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion\|L18]] (D/A), [[4-sampling-and-reconstruction/19-aliasing\|L19]] (the aliased output) |
| 9 | 15 | $X_0$, $X_3$; $y[n]$ from a permuted DFT; zero-padding relations | the DFT and its properties | [[5-dft-and-fft/20-discrete-fourier-transform\|L20]], [[5-dft-and-fft/21-dft-properties\|L21]] |
| 10 | 12 | number, amplitudes and frequencies of cosines from a 24-point DFT plot | spectral analysis with the DFT | [[5-dft-and-fft/20-discrete-fourier-transform\|L20]] (bin frequencies); DFT of a cosine later |

## Problem 1 · True/False (10 pts)

> [!question] Problem 1
> Answer **True** or **False** to each of the following statements: *Grading:* Correct answer = 2 pt.; Incorrect answer = −1 pt. No answer = 0 pts.
>
> (a) By sampling a continuous-time signal $x_c(t) = \cos(\pi^3 t)$ with some sampling period $T$, it is possible to obtain a discrete time signal $x[n] = \cos(3\pi n/4)$.
>
> (b) If the Nyquist sampling rate for a continuous-time signal $x_c(t)$ is $F_s$, then the Nyquist sampling rate for $y_c(t) = x_c(3t)$ is $F_s/3$.
>
> (c) Suppose $x[n]$ is a finite-length signal with DTFT $X_d(\omega)$. We zero-pad $x[n]$ with some number of zeros to obtain $y[n]$ with DTFT $Y_d(\omega)$. It follows then that $X_d(\omega) = Y_d(\omega)$.
>
> (d) If $x[n]$ is the inverse DFT of $\{1, 2, 3, 4\}$, then $x[n]$ must be zero for $n \lt 0$ or $n \gt 3$.
>
> (e) If $x_c(t)$ is a bandlimited continuous-time signal, then there must exist a finite $\Omega_{\max}$ such that $X_a(\Omega) = 0$ for $\lvert\Omega\rvert \gt \Omega_{\max}$, where $X_a(\Omega)$ is the CTFT of $x_c(t)$.

> [!success]- Solution 1
> - **(a) True.** $\pi^3 \approx 31$ rad/s; $T = \frac{3}{4\pi^2}$ s gives $\pi^3 T = \frac{3\pi}{4}$.
> - **(b) False.** Compressing time by 3 stretches the spectrum by 3: $3F_s$.
> - **(c) True.** Appended zeros add nothing to $\sum_n x[n]e^{-j\omega n}$.
> - **(d) False.** $x[n] = \frac1N\sum_k X[k]e^{j\frac{2\pi}{N}kn}$ is $N$-periodic: at $n = 4$ it returns $x[0] = 2.5$.
> - **(e) True.** Definition of bandlimited.

> [!trap] Where points go
> - With +2/−1/0 a guess right with probability $p$ is worth $3p - 1$; blank only if $p \lt \frac13$.

## Problem 2 · Symmetry: a real sequence (3 pts)

> [!question] Problem 2
> Let $X_d(\omega)$ be the DTFT of a *real-valued* sequence $x[n]$. We further assume that $X_d(\omega) = j\omega$ for $0 \le \omega \le \pi$. We then have (*select one answer only*):
>
> (a) $X_d(\omega) = \omega$ for $-\pi \le \omega \le 0$ · (b) $X_d(\omega) = -\omega$ for $-\pi \le \omega \le 0$ · (c) $X_d(\omega) = j\omega$ for $-\pi \le \omega \le 0$ · (d) $X_d(\omega) = -j\omega$ for $-\pi \le \omega \le 0$ · (e) None of the above

> [!success]- Solution 2
> **(c).** Real $x$ ⇒ $X_d(-\omega) = X_d^*(\omega)$; for $-\pi \le \omega \le 0$:
> $$
> X_d(\omega) = X_d^*(-\omega) = \left(j(-\omega)\right)^* = (-j\omega)^* = \boldsymbol{j\omega}.
> $$

> [!trap] Where points go
> - (d) by "odd extension": conjugation and the sign flip cancel for $j\omega$.

## Problem 3 · Periodicity: an arbitrary sequence (3 pts)

> [!question] Problem 3
> Let $X_d(\omega)$ be the DTFT of an *arbitrary* sequence $x[n]$. We further assume that $X_d(\omega) = j\omega$ for $0 \le \omega \le \pi$. We then have (*select one answer only*):
>
> (a) $X_d(\omega) = \omega$ for $2\pi \le \omega \le 3\pi$ · (b) $X_d(\omega) = -\omega$ for $2\pi \le \omega \le 3\pi$ · (c) $X_d(\omega) = j\omega$ for $2\pi \le \omega \le 3\pi$ · (d) $X_d(\omega) = -j\omega$ for $2\pi \le \omega \le 3\pi$ · (e) None of the above

> [!success]- Solution 3
> **(e).** Only periodicity: for $2\pi \le \omega \le 3\pi$,
> $$
> X_d(\omega) = X_d(\omega - 2\pi) = j(\omega - 2\pi),
> $$
> none of (a)–(d).

## Problem 4 · Inverse DTFT of an impulse (5 pts)

> [!question] Problem 4
> Calculate the inverse DTFT, $x[n]$, of $X_d(\omega) = 5e^{j\pi\omega}\delta(\omega - \omega_0)$, where $\omega_0$ is a constant.

> [!success]- Solution 4
> Sifting ($\omega_0 \in (-\pi, \pi)$):
> $$
> x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi}5e^{j\pi\omega}\delta(\omega - \omega_0)e^{j\omega n}\,d\omega = \frac{5}{2\pi}\int_{-\pi}^{\pi}e^{j\omega(\pi + n)}\delta(\omega - \omega_0)\,d\omega
> $$
> $$
> \boldsymbol{x[n] = \frac{5}{2\pi}e^{j\omega_0(\pi + n)}}
> $$
> $= \frac{5}{2\pi}e^{j\pi\omega_0}\,e^{j\omega_0 n}$: a complex exponential at $\omega_0$ with constant phase.

> [!trap] Where points go
> - Keep the $\frac{1}{2\pi}$; $e^{j\pi\omega}$ is not a time shift here, sifting evaluates it at $\omega_0$.

## Problem 5 · Magnitude and phase of a comb (14 pts)

> [!question] Problem 5
> We have an LSI system with the following unit pulse response given by $h[n]$: $h[n] = \delta[n] + \delta[n-6]$.
>
> (a) Determine the frequency response $H_d(\omega)$ of this LTI system.
>
> (b) Plot the magnitude response $\lvert H_d(\omega)\rvert$ and phase response $\angle H_d(\omega)$ for $-\pi \le \omega \le \pi$. Make sure to carefully label your axes.

> [!success]- Solution 5
> **(a)** Factor out the midpoint $n = 3$:
> $$
> \boldsymbol{H_d(\omega) = 1 + e^{-j6\omega} = e^{-j3\omega}\left(e^{j3\omega} + e^{-j3\omega}\right) = 2e^{-j3\omega}\cos(3\omega)}
> $$
> **(b)** $\lvert H_d(\omega)\rvert = 2\lvert\cos 3\omega\rvert$: zeros at $\pm\frac{\pi}{6}, \pm\frac{\pi}{2}, \pm\frac{5\pi}{6}$; maxima 2 at $0, \pm\frac{\pi}{3}, \pm\frac{2\pi}{3}, \pm\pi$. $\angle H_d(\omega) = -3\omega + \angle\cos 3\omega$: sawtooth from $\frac{\pi}{2}$ to $-\frac{\pi}{2}$, $\pi$ jump at every zero, 0 at $0, \pm\frac{\pi}{3}, \pm\frac{2\pi}{3}, \pm\pi$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="magnitude 2|cos 3w| and sawtooth phase between -pi/2 and pi/2" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="175.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| = 2|cos 3ω|</text><line x1="40.0" y1="131.7" x2="310.0" y2="131.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="53.5" x2="310.0" y2="53.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="210.0" x2="310.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="175.0" y1="30.0" x2="175.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="40.0" y1="207.0" x2="40.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="40.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="107.5" y1="207.0" x2="107.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="107.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="175.0" y1="207.0" x2="175.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="175.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="242.5" y1="207.0" x2="242.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="242.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="310.0" y1="207.0" x2="310.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="310.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="172.0" y1="131.7" x2="178.0" y2="131.7" stroke="currentColor" stroke-width="1"/><text x="36.0" y="135.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="172.0" y1="53.5" x2="178.0" y2="53.5" stroke="currentColor" stroke-width="1"/><text x="36.0" y="57.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><text x="310.0" y="204.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="40.0,53.5 41.2,54.0 42.4,55.7 44.9,62.4 47.3,73.6 49.9,89.4 55.3,134.6 62.5,210.0 69.3,138.1 74.4,94.2 79.2,66.4 81.4,58.3 83.7,54.1 85.0,53.5 86.3,54.1 88.9,59.2 91.5,69.4 94.2,84.8 99.9,130.7 107.5,210.0 113.8,142.9 118.5,101.1 122.9,72.4 125.0,63.1 127.0,56.8 128.4,54.4 129.8,53.5 131.2,54.0 132.6,56.1 135.4,64.7 138.4,79.4 144.4,126.5 152.5,210.0 160.2,129.5 166.0,83.1 168.8,68.0 171.5,58.2 174.1,53.8 175.4,53.6 176.8,54.7 179.0,59.6 181.2,68.0 185.8,96.2 190.8,139.8 197.5,210.0 205.0,131.6 210.6,85.7 213.3,70.1 215.9,59.7 218.5,54.3 219.8,53.5 221.0,53.9 223.3,57.7 225.6,65.4 230.4,93.2 235.6,137.6 242.5,210.0 248.8,143.4 253.5,101.4 257.8,72.6 259.9,63.2 261.9,57.0 263.3,54.5 264.7,53.5 266.1,54.0 267.5,55.9 270.4,64.3 273.3,78.9 279.4,126.1 287.5,210.0 294.7,134.6 300.1,89.4 302.7,73.6 305.1,62.4 307.6,55.7 308.8,54.0 310.0,53.5" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="495.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="360.0" y1="210.0" x2="630.0" y2="210.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="165.0" x2="630.0" y2="165.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="75.0" x2="630.0" y2="75.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="30.0" x2="630.0" y2="30.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="120.0" x2="630.0" y2="120.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="495.0" y1="30.0" x2="495.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="360.0" y1="117.0" x2="360.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="360.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="427.5" y1="117.0" x2="427.5" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="427.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="495.0" y1="117.0" x2="495.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="495.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="562.5" y1="117.0" x2="562.5" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="562.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="630.0" y1="117.0" x2="630.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="492.0" y1="210.0" x2="498.0" y2="210.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π</text><line x1="492.0" y1="165.0" x2="498.0" y2="165.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="169.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="492.0" y1="120.0" x2="498.0" y2="120.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="124.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="492.0" y1="75.0" x2="498.0" y2="75.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="79.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="492.0" y1="30.0" x2="498.0" y2="30.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="34.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π</text><text x="630.0" y="114.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="360.0,120.0 382.5,164.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="382.5,75.1 427.5,164.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="427.5,75.1 472.5,164.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="472.5,75.1 517.5,164.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="517.5,75.1 562.5,164.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="562.5,75.1 607.5,164.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="607.5,75.1 630.0,120.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/></svg><figcaption><strong>SP2023 #5(b): h[n] = δ[n] + δ[n − 6].</strong> |H<sub>d</sub>| = 2|cos 3ω| has six zeros in (−π, π], at ±π/6, ±π/2, ±5π/6. Between zeros the phase falls with slope −3 (it is −3ω plus a multiple of π), running from π/2 down to −π/2, and it jumps by +π at every zero (a sign flip of cos 3ω).</figcaption></figure>

> [!warning] Answer-key erratum — #5(a)
> The key's middle line reads $e^{-j3\omega}(e^{j3\omega} + e^{j3\omega})$; the second exponent should be $-j3\omega$. The boxed answer is right.

> [!trap] Where points go
> - Jumps are $\pi$ (sign flips of $2\cos 3\omega$), not $2\pi$ wraps; group delay 3.

## Problem 6 · A complex-valued frequency response (8 pts)

> [!question] Problem 6
> The frequency response of an LSI system is $H_d(\omega) = \omega e^{j\pi\cos\omega}$, $\lvert\omega\rvert \le \pi$. Compute the response of this system $y[n]$ to the following input signal:
> $$
> x[n] = 3 + e^{j\frac{\pi}{3}n} + \sin\left(\frac{\pi}{2}n + \frac{\pi}{4}\right).
> $$

> [!success]- Solution 6
> Frequencies $0$, $\frac{\pi}{3}$, $\pm\frac{\pi}{2}$:
> $$
> H_d(0) = 0,\qquad H_d\!\left(\tfrac{\pi}{3}\right) = \tfrac{\pi}{3}e^{j\pi/2} = j\tfrac{\pi}{3},\qquad H_d\!\left(\tfrac{\pi}{2}\right) = \tfrac{\pi}{2},\qquad H_d\!\left(-\tfrac{\pi}{2}\right) = -\tfrac{\pi}{2}.
> $$
> $\theta = \frac{\pi}{2}n + \frac{\pi}{4}$, $\sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2j}$:
> $$
> \frac{\frac{\pi}{2}e^{j\theta} - \left(-\frac{\pi}{2}\right)e^{-j\theta}}{2j} = \frac{\pi}{2}\cdot\frac{e^{j\theta} + e^{-j\theta}}{2j} = -j\frac{\pi}{2}\cos\theta .
> $$
> $$
> \boldsymbol{y[n] = \frac{\pi}{3}e^{j\left(\frac{\pi}{3}n + \frac{\pi}{2}\right)} - j\frac{\pi}{2}\cos\left(\frac{\pi}{2}n + \frac{\pi}{4}\right)}
> $$
> $H_d(-\omega) \ne H_d^*(\omega)$: $h[n]$ complex, so no real-system shortcut.

> [!trap] Where points go
> - The shortcut gives the wrong $\frac{\pi}{2}\sin(\frac{\pi}{2}n + \frac{\pi}{4})$; split into exponentials.

## Problem 7 · An odd spectrum through A/D, $H_d$, D/A (20 pts)

> [!question] Problem 7
> Consider the process of a bandlimited continuous-time signal $x_c(t)$ via the system shown below.
>
> (a) What is the Nyquist rate for the signal $x_c(t)$ (i.e., no aliasing at the A/D converter)? Answer the rate in Hz.
>
> (b) Sketch the DTFT $X_d(\omega)$ and $Y_d(\omega)$ at $T = \frac14\cdot 10^{-3}$ for $-\pi \le \omega \le \pi$. Please carefully label your axes.
>
> (c) Sketch the DTFT $X_d(\omega)$ and $Y_d(\omega)$ at $T = \frac13\cdot 10^{-3}$ for $-\pi \le \omega \le \pi$. Please carefully label your axes.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 350" width="640" height="350" role="img" aria-label="ideal A/D, H_d, ideal D/A; odd triangle spectrum; odd band filter" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="14.0" y1="45.0" x2="70.4" y2="45.0" stroke="currentColor" stroke-width="1.4"/><path d="M76.0,45.0 L69.0,41.9 L69.0,48.1 Z" fill="currentColor"/><text x="45.0" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:13px">x<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(t)</text><rect x="76.0" y="25.0" width="88" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="120.0" y="50.0" text-anchor="middle" fill="currentColor" style="font-size:13px">ideal A/D</text><line x1="120.0" y1="87.0" x2="120.0" y2="71.6" stroke="currentColor" stroke-width="1.4"/><path d="M120.0,66.0 L116.8,73.0 L123.2,73.0 Z" fill="currentColor"/><text x="120.0" y="101.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-style:italic">T</text><line x1="164.0" y1="45.0" x2="220.4" y2="45.0" stroke="currentColor" stroke-width="1.4"/><path d="M226.0,45.0 L219.0,41.9 L219.0,48.1 Z" fill="currentColor"/><text x="195.0" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:13px">x[n]</text><rect x="226.0" y="25.0" width="88" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="270.0" y="50.0" text-anchor="middle" fill="currentColor" style="font-size:13px">H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="314.0" y1="45.0" x2="370.4" y2="45.0" stroke="currentColor" stroke-width="1.4"/><path d="M376.0,45.0 L369.0,41.9 L369.0,48.1 Z" fill="currentColor"/><text x="345.0" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:13px">y[n]</text><rect x="376.0" y="25.0" width="88" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="420.0" y="50.0" text-anchor="middle" fill="currentColor" style="font-size:13px">ideal D/A</text><line x1="420.0" y1="87.0" x2="420.0" y2="71.6" stroke="currentColor" stroke-width="1.4"/><path d="M420.0,66.0 L416.9,73.0 L423.1,73.0 Z" fill="currentColor"/><text x="420.0" y="101.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-style:italic">T</text><line x1="464.0" y1="45.0" x2="520.4" y2="45.0" stroke="currentColor" stroke-width="1.4"/><path d="M526.0,45.0 L519.0,41.9 L519.0,48.1 Z" fill="currentColor"/><text x="495.0" y="37.0" text-anchor="middle" fill="currentColor" style="font-size:13px">y<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(t)</text><text x="175.0" y="144.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">X<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(Ω)</text><line x1="40.0" y1="225.0" x2="310.0" y2="225.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="175.0" y1="150.0" x2="175.0" y2="300.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="67.0" y1="222.0" x2="67.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="67.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−4</text><line x1="94.0" y1="222.0" x2="94.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="94.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3</text><line x1="121.0" y1="222.0" x2="121.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="121.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2</text><line x1="175.0" y1="222.0" x2="175.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="175.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="229.0" y1="222.0" x2="229.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="229.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2</text><line x1="256.0" y1="222.0" x2="256.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="256.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3</text><line x1="283.0" y1="222.0" x2="283.0" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="283.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">4</text><line x1="172.0" y1="282.7" x2="178.0" y2="282.7" stroke="currentColor" stroke-width="1"/><text x="36.0" y="286.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">−1</text><line x1="172.0" y1="167.3" x2="178.0" y2="167.3" stroke="currentColor" stroke-width="1"/><text x="36.0" y="171.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><polyline points="40.0,225.0 67.0,225.0 94.0,282.7 121.0,225.0 229.0,225.0 256.0,167.3 283.0,225.0 310.0,225.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="175.0" y="340.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">Ω in units of π·10³ rad/s</text><text x="490.0" y="144.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="360.0" y1="225.0" x2="620.0" y2="225.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="490.0" y1="150.0" x2="490.0" y2="300.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="392.5" y1="222.0" x2="392.5" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="392.5" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π/4</text><line x1="457.5" y1="222.0" x2="457.5" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="457.5" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="522.5" y1="222.0" x2="522.5" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="522.5" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="587.5" y1="222.0" x2="587.5" y2="228.0" stroke="currentColor" stroke-width="1"/><text x="587.5" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π/4</text><line x1="487.0" y1="282.7" x2="493.0" y2="282.7" stroke="currentColor" stroke-width="1"/><text x="356.0" y="286.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">−1</text><line x1="487.0" y1="167.3" x2="493.0" y2="167.3" stroke="currentColor" stroke-width="1"/><text x="356.0" y="171.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="620.0" y="219.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="360.0,225.0 392.5,225.0 392.5,167.3 457.5,167.3 457.5,225.0 522.5,225.0 522.5,282.7 587.5,282.7 587.5,225.0 620.0,225.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/></svg><figcaption><strong>SP2023 #7: the system and the two spectra.</strong> X<sub>c</sub>(Ω) is real and odd: a triangle of height +1 on 2π·10³…4π·10³ (peak at 3π·10³) and its negative mirror image. H<sub>d</sub>(ω) is +1 on −3π/4 &lt; ω &lt; −π/4, −1 on π/4 &lt; ω &lt; 3π/4, 0 elsewhere.</figcaption></figure>

> [!success]- Solution 7(a)–(b)
> **(a)** $\Omega_{\max} = 4\pi\cdot10^3$ rad/s, $f_{\max} = 2$ kHz: Nyquist rate $\boldsymbol{4\ \text{kHz}}$.
>
> **(b)** $T = \frac14$ ms, $F_s = 4$ kHz (Nyquist). $2\pi\cdot10^3 \to \frac{\pi}{2}$, $3\pi\cdot10^3 \to \frac{3\pi}{4}$, $4\pi\cdot10^3 \to \pi$; height $\frac1T = 4000$:
> - $X_d$: triangle $+4000$ on $[\frac{\pi}{2}, \pi]$ (peak at $\frac{3\pi}{4}$), its negative on $[-\pi, -\frac{\pi}{2}]$ (trough $-4000$ at $-\frac{3\pi}{4}$). No overlap.
> - $Y_d = H_d X_d$, nonzero on $\frac{\pi}{2} \le \lvert\omega\rvert \le \frac{3\pi}{4}$: right, $H_d = -1$: ramp 0 at $\frac{\pi}{2}$ to $-4000$ at $\frac{3\pi}{4}$; left, $H_d = +1$: $-4000$ at $-\frac{3\pi}{4}$ rising to 0 at $-\frac{\pi}{2}$.
>
> $Y_d$ real and even ⇒ $y[n]$ real.

> [!success]- Solution 7(c)
> $T = \frac13$ ms, $F_s = 3$ kHz, below Nyquist. $2\pi\cdot10^3 \to \frac{2\pi}{3}$, $3\pi\cdot10^3 \to \pi$, $4\pi\cdot10^3 \to \frac{4\pi}{3}$ (height 3000). The positive triangle sits on $[\frac{2\pi}{3}, \frac{4\pi}{3}]$; the negative one, shifted by $2\pi$, lands on the same interval. They cancel:
> $$
> \boldsymbol{X_d(\omega) = 0,\quad x[n] = 0,\quad Y_d(\omega) = 0 \quad\text{for all }\omega}
> $$
> Time domain: $x_c(t) = 2j\,g(t)\sin(3\pi\cdot10^3\,t)$, and at $t = n/3000$, $\sin(\pi n) = 0$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" width="640" height="400" role="img" aria-label="sampled spectra for SP2023 problem 7" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="180.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(b) X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω), T = ¼ ms</text><line x1="50.0" y1="156.0" x2="310.0" y2="156.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="44.0" x2="310.0" y2="44.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="100.0" x2="310.0" y2="100.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="180.0" y1="30.0" x2="180.0" y2="170.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="50.0" y1="97.0" x2="50.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="50.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="82.5" y1="97.0" x2="82.5" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="82.5" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π/4</text><line x1="115.0" y1="97.0" x2="115.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="115.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="180.0" y1="97.0" x2="180.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="180.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="245.0" y1="97.0" x2="245.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="245.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="277.5" y1="97.0" x2="277.5" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="277.5" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π/4</text><line x1="310.0" y1="97.0" x2="310.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="310.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="177.0" y1="156.0" x2="183.0" y2="156.0" stroke="currentColor" stroke-width="1"/><text x="46.0" y="160.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−4000</text><line x1="177.0" y1="44.0" x2="183.0" y2="44.0" stroke="currentColor" stroke-width="1"/><text x="46.0" y="48.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">4000</text><text x="310.0" y="94.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="50.0,100.0 82.5,156.0 115.0,100.0 245.0,100.0 277.5,44.0 310.0,100.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="500.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(b) Y<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω), T = ¼ ms</text><line x1="370.0" y1="156.0" x2="630.0" y2="156.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="44.0" x2="630.0" y2="44.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="100.0" x2="630.0" y2="100.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="500.0" y1="30.0" x2="500.0" y2="170.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="370.0" y1="97.0" x2="370.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="370.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="402.5" y1="97.0" x2="402.5" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="402.5" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π/4</text><line x1="435.0" y1="97.0" x2="435.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="435.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="500.0" y1="97.0" x2="500.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="500.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="565.0" y1="97.0" x2="565.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="565.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="597.5" y1="97.0" x2="597.5" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="597.5" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π/4</text><line x1="630.0" y1="97.0" x2="630.0" y2="103.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="497.0" y1="156.0" x2="503.0" y2="156.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="160.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−4000</text><line x1="497.0" y1="44.0" x2="503.0" y2="44.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="48.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">4000</text><text x="630.0" y="94.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="370.0,100.0 402.5,100.0 402.6,155.9 435.0,100.0 565.0,100.0 597.4,155.9 597.5,100.0 630.0,100.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="340.0" y="234.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(c) T = ⅓ ms: the k = 0 copy (solid) and the k = ±1 copies (dashed) cancel</text><line x1="50.0" y1="350.0" x2="630.0" y2="350.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="250.0" x2="630.0" y2="250.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="300.0" x2="630.0" y2="300.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="340.0" y1="240.0" x2="340.0" y2="360.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="50.0" y1="297.0" x2="50.0" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="50.0" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="146.7" y1="297.0" x2="146.7" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="146.7" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π/3</text><line x1="340.0" y1="297.0" x2="340.0" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="340.0" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="533.3" y1="297.0" x2="533.3" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="533.3" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π/3</text><line x1="630.0" y1="297.0" x2="630.0" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="374.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="337.0" y1="350.0" x2="343.0" y2="350.0" stroke="currentColor" stroke-width="1"/><text x="46.0" y="354.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−3000</text><line x1="337.0" y1="250.0" x2="343.0" y2="250.0" stroke="currentColor" stroke-width="1"/><text x="46.0" y="254.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">3000</text><text x="630.0" y="294.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="50.0,350.0 146.7,300.0 533.3,300.0 630.0,250.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="50.0,300.0 533.3,300.0 630.0,350.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="50.0,250.0 146.7,300.0 630.0,300.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="50.0,300.0 630.0,300.0" fill="none" stroke="var(--hi)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/></svg><figcaption><strong>SP2023 #7(b)–(c).</strong> (b) At the Nyquist rate (T = ¼ ms) the band maps to π/2 ≤ |ω| ≤ π with height 1/T = 4000; H<sub>d</sub> keeps the inner halves (π/2 to 3π/4 in magnitude) and flips the sign of the right one, so Y<sub>d</sub> is two negative ramps. (c) At T = ⅓ ms both analog triangles map onto ω = π with opposite signs: the sum (red) is zero, so x[n] = 0 and Y<sub>d</sub> = 0.</figcaption></figure>

> [!note] Key sketch label
> In the key's (b) sketches the tick at $-\frac{\pi}{2}$ lacks its minus sign; shapes are right.

> [!trap] Where points go
> - (b): both ramps point down. (c): aliasing cancels exactly here.

## Problem 8 · Sampling periods from aliased cosines (10 pts)

> [!question] Problem 8
> Consider the sampling and reconstruction system shown below. The input to the ideal A/D is $x_c(t) = 2\cos\left(100\pi t + \frac{\pi}{4}\right) + \cos(300\pi t)$.
>
> (a) If the output of A/D is $x[n] = 2\cos\left(\frac14\pi n + \frac{\pi}{4}\right) + \cos\left(\frac34\pi n\right)$, determine two choices for $T$ consistent with the information.
>
> (b) If the output of the ideal D/A is $y_c(t) = 2\cos\left(100\pi t + \frac{\pi}{4}\right) + 1$, determine the value of $T$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 110" width="560" height="110" role="img" aria-label="block diagram ideal A/D followed by ideal D/A" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="20.0" y1="40.0" x2="114.4" y2="40.0" stroke="currentColor" stroke-width="1.4"/><path d="M120.0,40.0 L113.0,36.9 L113.0,43.1 Z" fill="currentColor"/><text x="70.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:13px">x<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(t)</text><rect x="120.0" y="20.0" width="110" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="175.0" y="45.0" text-anchor="middle" fill="currentColor" style="font-size:13px">ideal A/D</text><line x1="175.0" y1="82.0" x2="175.0" y2="66.6" stroke="currentColor" stroke-width="1.4"/><path d="M175.0,61.0 L171.8,68.0 L178.2,68.0 Z" fill="currentColor"/><text x="175.0" y="96.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-style:italic">T</text><line x1="230.0" y1="40.0" x2="324.4" y2="40.0" stroke="currentColor" stroke-width="1.4"/><path d="M330.0,40.0 L323.0,36.9 L323.0,43.1 Z" fill="currentColor"/><text x="280.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:13px">x[n]</text><rect x="330.0" y="20.0" width="110" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="385.0" y="45.0" text-anchor="middle" fill="currentColor" style="font-size:13px">ideal D/A</text><line x1="385.0" y1="82.0" x2="385.0" y2="66.6" stroke="currentColor" stroke-width="1.4"/><path d="M385.0,61.0 L381.9,68.0 L388.1,68.0 Z" fill="currentColor"/><text x="385.0" y="96.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-style:italic">T</text><line x1="440.0" y1="40.0" x2="534.4" y2="40.0" stroke="currentColor" stroke-width="1.4"/><path d="M540.0,40.0 L533.0,36.9 L533.0,43.1 Z" fill="currentColor"/><text x="490.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:13px">y<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(t)</text></svg><figcaption><strong>Sampling and reconstruction</strong>: an ideal A/D and an ideal D/A with the same interval T.</figcaption></figure>

> [!success]- Solution 8
> **(a)** The phased term fixes the sign: $100\pi T = \frac{\pi}{4} + 2\pi k$:
> $$
> T = \frac{1 + 8k}{400}\ \text{s},\ k \ge 0:\qquad \boldsymbol{T_1 = \frac{1}{400}\ \text{s},\quad T_2 = \frac{9}{400}\ \text{s}}
> $$
> Then $300\pi T = \frac{3\pi}{4} + 6\pi k \equiv \frac{3\pi}{4}$ automatically.
>
> **(b)** $300\pi$ aliases to DC: $300\pi T = 2\pi k$, $T = \frac{k}{150}$. $100\pi$ must not alias: $100\pi T \lt \pi$, $T \lt \frac{1}{100}$. Only $k = 1$:
> $$
> \boldsymbol{T = \frac{1}{150}\ \text{s}}
> $$
> $x[n] = 2\cos\left(\frac{2\pi}{3}n + \frac{\pi}{4}\right) + 1$.

> [!trap] Where points go
> - (b): $T = \frac{2}{150}$ also sends $300\pi$ to DC but aliases $100\pi$.

## Problem 9 · DFT shift, modulation and zero padding (15 pts)

> [!question] Problem 9
> For all parts of this question, let $\{x[n]\}_{n=0}^{5} = \{1, 2, -3, -4, 5, 6\}$ be a length-6 signal with DFT $\{X[k]\}_{k=0}^{5} = \{X_0, X_1, X_2, X_3, X_4, X_5\}$.
>
> (a) Compute $X_0$ and $X_3$.
>
> (b) The DFT of another length-6 signal $\{y[n]\}_{n=0}^{5}$ is given by $\{Y[k]\}_{k=0}^{5} = \{X_4, -X_5, X_0, -X_1, X_2, -X_3\}$. Determine the signal $y[n]$.
>
> (c) Suppose we zero-pad $x[n]$ with 24 zeros to obtain $\{z[n]\}_{n=0}^{29}$ with corresponding DFT $\{Z[k]\}_{k=0}^{29}$. Which of the following relations is true? (Circle all that are true. More than one may be true.)
> i. $X[0] = Z[0]$ · ii. $X[1] = Z[4]$ · iii. $X[2] = Z[10]$ · iv. $X[1] = Z^*[25]$ · v. $X[2] = Z^*[22]$

> [!success]- Solution 9
> **(a)** $X_0 = \sum x[n] = 1 + 2 - 3 - 4 + 5 + 6 = \boldsymbol{7}$; $X_3 = \sum x[n]\,(-1)^n = 1 - 2 - 3 + 4 + 5 - 6 = \boldsymbol{-1}$.
>
> **(b)** $Y[k] = (-1)^k X[\langle k-2\rangle_6]$: $X[\langle k-2\rangle_6]$ is modulation by $e^{j\frac{2\pi}{6}2n} = e^{j\frac{2\pi}{3}n}$; $(-1)^k = e^{-j\frac{2\pi}{6}3k}$ is a circular shift by 3:
> $$
> \boldsymbol{y[n] = e^{j\frac{2\pi}{3}n}\,x[\langle n-3\rangle_6]} = \{\underset{\uparrow}{-4},\ 5e^{j2\pi/3},\ 6e^{j4\pi/3},\ 1,\ 2e^{j2\pi/3},\ -3e^{j4\pi/3}\}
> $$
> **(c)** $Z[k] = X_d(\frac{2\pi k}{30})$, $X[k] = X_d(\frac{2\pi k}{6}) = Z[5k]$.
> - **i. True** ($k = 0$). **ii. False:** $X[1] = Z[5]$. **iii. True:** $X[2] = Z[10]$.
> - **iv. True:** $Z[25] = X_d(\frac{5\pi}{3}) = X_d(-\frac{\pi}{3}) = X_d^*(\frac{\pi}{3}) = X^*[1]$.
> - **v. False:** $X[2] = Z^*[30 - 10] = Z^*[20]$, not $Z^*[22]$.

> [!trap] Where points go
> - (b): alternating signs are a circular shift by $N/2 = 3$, not a negation.

## Problem 10 · Cosines from a DFT plot (12 pts)

> [!question] Problem 10
> An analog signal $x_a(t)$ is known to be composed of $M$ spectral components such that $x_a(t) = \sum_{m=1}^{M}A_m\cos(\Omega_m t)$. The analog signal is sampled with sampling period $T = \frac{1}{12{,}000}$ s to create digital signal $\{x[n]\}_{n=0}^{23} = \{x_a(nT)\}_{n=0}^{23}$ with DFT $X[k]$. The DFT magnitude spectrum $\lvert X[k]\rvert$ is given in the below image. You may assume that $x_a(t)$ is sampled above the Nyquist rate and thus no aliasing occurs.
>
> (a) Determine the number of spectral components $M$.
>
> (b) Determine the amplitudes of each spectral component $\{A_m\}_{m=1}^{M}$.
>
> (c) Determine the analog radial frequencies of each spectral component $\{\Omega_m\}_{m=1}^{M}$. (Please use consistent subscripts between parts (b) and (c))

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="640" height="230" role="img" aria-label="DFT magnitude stem plot with peaks 6, 12, 9 at k=1,6,9 and mirror images" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="50.0" y1="161.3" x2="610.0" y2="161.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="137.6" x2="610.0" y2="137.6" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="113.9" x2="610.0" y2="113.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="90.2" x2="610.0" y2="90.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="66.5" x2="610.0" y2="66.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="42.8" x2="610.0" y2="42.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="185.0" x2="610.0" y2="185.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="68.2" y1="25.0" x2="68.2" y2="185.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="68.2" y1="182.0" x2="68.2" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="68.2" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="113.7" y1="182.0" x2="113.7" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="113.7" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2</text><line x1="159.3" y1="182.0" x2="159.3" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="159.3" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">4</text><line x1="204.8" y1="182.0" x2="204.8" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="204.8" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">6</text><line x1="250.3" y1="182.0" x2="250.3" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="250.3" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">8</text><line x1="295.9" y1="182.0" x2="295.9" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="295.9" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">10</text><line x1="341.4" y1="182.0" x2="341.4" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="341.4" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">12</text><line x1="386.9" y1="182.0" x2="386.9" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="386.9" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">14</text><line x1="432.4" y1="182.0" x2="432.4" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="432.4" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">16</text><line x1="478.0" y1="182.0" x2="478.0" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="478.0" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">18</text><line x1="523.5" y1="182.0" x2="523.5" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="523.5" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">20</text><line x1="569.0" y1="182.0" x2="569.0" y2="188.0" stroke="currentColor" stroke-width="1"/><text x="569.0" y="199.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">22</text><line x1="65.2" y1="161.3" x2="71.2" y2="161.3" stroke="currentColor" stroke-width="1"/><text x="46.0" y="165.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="65.2" y1="137.6" x2="71.2" y2="137.6" stroke="currentColor" stroke-width="1"/><text x="46.0" y="141.6" text-anchor="end" fill="var(--muted)" style="font-size:11px">4</text><line x1="65.2" y1="113.9" x2="71.2" y2="113.9" stroke="currentColor" stroke-width="1"/><text x="46.0" y="117.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">6</text><line x1="65.2" y1="90.2" x2="71.2" y2="90.2" stroke="currentColor" stroke-width="1"/><text x="46.0" y="94.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">8</text><line x1="65.2" y1="66.5" x2="71.2" y2="66.5" stroke="currentColor" stroke-width="1"/><text x="46.0" y="70.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">10</text><line x1="65.2" y1="42.8" x2="71.2" y2="42.8" stroke="currentColor" stroke-width="1"/><text x="46.0" y="46.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">12</text><text x="610.0" y="179.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">k</text><line x1="68.2" y1="185.0" x2="68.2" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="68.2" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="91.0" y1="185.0" x2="91.0" y2="113.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="91.0" cy="113.9" r="3.2" fill="var(--accent)"/><text x="91.0" y="106.9" text-anchor="middle" fill="var(--accent)" style="font-size:11px">6</text><line x1="113.7" y1="185.0" x2="113.7" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="113.7" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="136.5" y1="185.0" x2="136.5" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="136.5" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="159.3" y1="185.0" x2="159.3" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="159.3" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="182.0" y1="185.0" x2="182.0" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="182.0" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="204.8" y1="185.0" x2="204.8" y2="42.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="204.8" cy="42.8" r="3.2" fill="var(--accent)"/><text x="204.8" y="35.8" text-anchor="middle" fill="var(--accent)" style="font-size:11px">12</text><line x1="227.6" y1="185.0" x2="227.6" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="227.6" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="250.3" y1="185.0" x2="250.3" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="250.3" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="273.1" y1="185.0" x2="273.1" y2="78.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="273.1" cy="78.3" r="3.2" fill="var(--accent)"/><text x="273.1" y="71.3" text-anchor="middle" fill="var(--accent)" style="font-size:11px">9</text><line x1="295.9" y1="185.0" x2="295.9" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="295.9" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="318.6" y1="185.0" x2="318.6" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="318.6" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="341.4" y1="185.0" x2="341.4" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="341.4" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="364.1" y1="185.0" x2="364.1" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="364.1" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="386.9" y1="185.0" x2="386.9" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="386.9" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="409.7" y1="185.0" x2="409.7" y2="78.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="409.7" cy="78.3" r="3.2" fill="var(--accent)"/><text x="409.7" y="71.3" text-anchor="middle" fill="var(--accent)" style="font-size:11px">9</text><line x1="432.4" y1="185.0" x2="432.4" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="432.4" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="455.2" y1="185.0" x2="455.2" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="455.2" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="478.0" y1="185.0" x2="478.0" y2="42.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="478.0" cy="42.8" r="3.2" fill="var(--accent)"/><text x="478.0" y="35.8" text-anchor="middle" fill="var(--accent)" style="font-size:11px">12</text><line x1="500.7" y1="185.0" x2="500.7" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="500.7" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="523.5" y1="185.0" x2="523.5" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="523.5" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="546.3" y1="185.0" x2="546.3" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="546.3" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="569.0" y1="185.0" x2="569.0" y2="185.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="569.0" cy="185.0" r="3.2" fill="var(--accent)"/><line x1="591.8" y1="185.0" x2="591.8" y2="113.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="591.8" cy="113.9" r="3.2" fill="var(--accent)"/><text x="591.8" y="106.9" text-anchor="middle" fill="var(--accent)" style="font-size:11px">6</text><text x="330.0" y="18.0" text-anchor="middle" fill="currentColor" style="font-size:13px">|X[k]|, N = 24</text></svg><figcaption><strong>SP2023 #10: the 24-point DFT magnitude</strong> (redrawn from the exam plot): |X[k]| = 6 at k = 1, 23; 12 at k = 6, 18; 9 at k = 9, 15; zero elsewhere.</figcaption></figure>

> [!success]- Solution 10
> Whole number of cycles: $\lvert X[k_0]\rvert = \lvert X[N-k_0]\rvert = \frac{AN}{2} = 12A$.
>
> **(a)** Mirror pairs $(1, 23)$, $(6, 18)$, $(9, 15)$: $\boldsymbol{M = 3}$.
>
> **(b)** $\boldsymbol{A_1 = \frac{6}{12} = \frac12,\quad A_2 = \frac{12}{12} = 1,\quad A_3 = \frac{9}{12} = \frac34}$.
>
> **(c)** $\Omega = \frac{2\pi k}{24}\cdot 12000 = 1000\pi k$ rad/s:
> $$
> \boldsymbol{\Omega_1 = 1000\pi,\quad \Omega_2 = 6000\pi,\quad \Omega_3 = 9000\pi\ \text{rad/s}}
> $$
> (500 Hz, 3 kHz, 4.5 kHz, below $F_s/2 = 6$ kHz.)

> [!warning] Answer-key erratum — #10
> The key labels all three amplitudes $A_1$ and all three frequencies $\Omega_1$, though the problem asks for consistent subscripts. The values are right.

## Related

[[exams/midterm-2/past-exams/index|All past exams]] · previous: [[exams/midterm-2/past-exams/fall-2023|Fall 2023]] · next: [[exams/midterm-2/past-exams/fall-2021|Fall 2021]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/group-delay|group delay]] · [[exams/midterm-1/past-exams/spring-2023|Spring 2023 · Midterm 1]]

### Sources for this page

ECE 310 Midterm Exam 2, Spring 2023 (Liang, Moon, Snyder), typed key (ECE_310_Exam_2_Solutions_Spring_2023.pdf); figures redrawn.
