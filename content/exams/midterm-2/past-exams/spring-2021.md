---
title: "Spring 2021 · Midterm 2"
description: "The Spring 2021 ECE 310 Midterm 2 (Moon, Katselis, Shomorony) typed out problem by problem with folded worked solutions: five T/F statements, a magnitude/phase sketch, a DTFT in A e^{-jBω} sin(Cω) form, two DFT-property problems, CTFT vs DTFT vs DFT, amplitudes read off a two-step spectrum, undersampling that flattens a spectrum, and the two inputs behind one reconstructed cosine."
tags: [exam, midterm-2]
---

*Thu Apr 8, 2021 · 7:00–8:50 pm · Profs. Moon, Katselis, Shomorony · 9 problems, 100 points · online exam: one handwritten two-sided 8.5″ × 11″ sheet, no books or electronic devices; solutions written on paper, photographed and uploaded to Gradescope · typed key*

> [!abstract] What this exam adds
> The most DTFT-heavy exam of the set. For this unit: a **magnitude and phase sketch of a sinusoid times a linear phase** (#2, where the sequence is purely imaginary so the phase is *not* odd), a DTFT forced into the **form $Ae^{-jB\omega}\sin(C\omega)$** (#3), and **amplitudes read off a two-step lowpass spectrum** (#7). The later topics: DFT circular shift with an extra sign (#4), a reality test from DFT values (#5), CTFT vs DTFT vs DFT (#6), undersampling by exactly 2 that makes the spectrum **flat** (#8), and the **two inputs** behind one reconstructed cosine (#9). The typed key is correct; two cosmetic points (the #2 phase sketch is not wrapped, the #8 figure mixes $\Omega$ and $\omega$ in its labels) are noted below.

## Map of the exam

| # | pts | what it asks | topic · problem family | lectures |
|---|---|---|---|---|
| 1 | 15 | five True/False statements | T/F: sampling, Nyquist rate of $x_c(2t)$, DFT $X[0]$, an impulse integral | Lectures 17+ (not yet in these notes) |
| 2 | 10 | sketch magnitude and phase of $e^{-j4\omega}\sin 2\omega$ | [[problems/magnitude-phase-and-group-delay\|magnitude, phase and group delay]] | [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] |
| 3 | 9 | DTFT of $3\delta[n+1] - 3\delta[n-7]$ as $Ae^{-jB\omega}\sin(C\omega)$ | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]], [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] |
| 4 | 8 | the sequence whose 8-point DFT is $e^{-j(\frac{6\pi}{8}k+\pi)}X[k]$ | the DFT and its properties (circular shift) | Lectures 17+ (not yet in these notes) |
| 5 | 8 | is $x$ real, given its 7-point DFT? | the DFT and its properties (symmetry) | Lectures 17+ (not yet in these notes) |
| 6 | 9 | CTFT, DTFT or DFT: match three descriptions | DTFT vs DFT vs CTFT | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]], Lectures 17+ (not yet in these notes) |
| 7 | 14 | $A_1$, $A_2$, $\omega_0$ from the DTFT of two sinc sequences | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] (ideal lowpass pair) | [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]], [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 8 | 15 | Nyquist rate; $X_d(\omega)$ after undersampling a V-shaped spectrum; is $x$ real? | sampling and aliasing | Lectures 17+ (not yet in these notes) |
| 9 | 12 | ideal A/D–D/A: $x[n]$ and the two inputs that give $2\cos(300\pi t)$ | sampling and reconstruction (aliasing) | Lectures 17+ (not yet in these notes) |

## Problem 1 · True/False (15 pts)

*Topic: sampling and the DFT — Lectures 17+ (not yet in these notes); (d) needs only the sifting property of the continuous-time impulse.*

> [!question] Problem 1
> Answer **True** or **False** to each of the following statements:
>
> (a) By sampling a continuous-time signal $x_c(t) = \cos(17\pi t)$ with some sampling period $T$, it is possible to obtain a discrete time signal $x[n] = \cos(3\pi n/4)$.
>
> (b) If the Nyquist sampling rate for a continuous-time signal $x_c(t)$ is $F_s$, then the Nyquist sampling rate for $y_c(t) = x_c(2t)$ is $2F_s$.
>
> (c) If $\{x[n]\}_{n=0}^{5}$ is real-valued and $\{X[k]\}_{k=0}^{5}$ is its DFT, then $X[0]$ is real-valued.
>
> (d) The value of $\int_3^{\infty}(t+1)\delta(t)\,dt$ is 0.
>
> (e) Let $\{x[n]\}_{n=0}^{7} = \{1, -1, 6, 7, 9, -6, -7, 9\}$. Consider the corresponding 8-point DFT $\{X[k]\}_{k=0}^{7}$. Then, $X[0] = 0$.

> [!success]- Solution 1
> - **(a) True.** $x[n] = x_c(nT) = \cos(17\pi T n)$; $T = \frac{3}{68}$ s gives $17\pi T = \frac{3\pi}{4}$. (Any $T$ with $17\pi T = \pm\frac{3\pi}{4} + 2\pi k$ works.)
> - **(b) True.** $x_c(2t) \leftrightarrow \frac12 X_c(\Omega/2)$: compressing time by 2 doubles the highest frequency, so the Nyquist rate doubles.
> - **(c) True.** $X[0] = \sum_n x[n]$, a sum of real numbers.
> - **(d) True.** $\delta(t)$ sits at $t = 0$, outside $[3, \infty)$, so the integral is 0. (Sifting would give $(0+1) = 1$ only if the range contained $t = 0$.)
> - **(e) False.** $X[0] = \sum_n x[n] = 1 - 1 + 6 + 7 + 9 - 6 - 7 + 9 = 18$.

> [!trap] Where points go
> - **(d)** Writing 1 by reflex: the sifting property only fires when the impulse is inside the limits.
> - **(a)** After sampling, frequencies are only defined modulo $2\pi$; ask whether *some* $T$ maps $17\pi$ onto $\pm\frac{3\pi}{4} + 2\pi k$; for a cosine of nonzero frequency the answer is always yes.

## Problem 2 · Magnitude and phase of $e^{-j4\omega}\sin 2\omega$ (10 pts)

*Topic: magnitude and phase response — [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]] · [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]].*

> [!question] Problem 2
> Let $X_d(\omega) = e^{-j4\omega}\sin(2\omega)$. Sketch the magnitude and phase of $X_d(\omega)$ (label your plots carefully).

> [!success]- Solution 2
> $\lvert e^{-j4\omega}\rvert = 1$ and $\sin 2\omega$ is real, so
> $$
> \lvert X_d(\omega)\rvert = \lvert\sin 2\omega\rvert,\qquad \angle X_d(\omega) = -4\omega + \begin{cases}0, & \sin 2\omega \gt 0\\ \pm\pi, & \sin 2\omega \lt 0\end{cases}\quad(\text{mod } 2\pi).
> $$
> Magnitude: zeros at $0, \pm\frac{\pi}{2}, \pm\pi$, peaks of 1 at $\pm\frac{\pi}{4}, \pm\frac{3\pi}{4}$. Phase, as a principal value in $[-\pi, \pi]$:
>
> | interval | $\angle X_d(\omega)$ | runs from → to |
> |---|---|---|
> | $(-\pi, -\frac{3\pi}{4})$ | $-4\omega - 4\pi$ | $0 \to -\pi$ |
> | $(-\frac{3\pi}{4}, -\frac{\pi}{2})$ | $-4\omega - 2\pi$ | $\pi \to 0$ |
> | $(-\frac{\pi}{2}, 0)$ | $-4\omega - \pi$ | $\pi \to -\pi$ |
> | $(0, \frac{\pi}{4})$ | $-4\omega$ | $0 \to -\pi$ |
> | $(\frac{\pi}{4}, \frac{\pi}{2})$ | $-4\omega + 2\pi$ | $\pi \to 0$ |
> | $(\frac{\pi}{2}, \pi)$ | $-4\omega + 3\pi$ | $\pi \to -\pi$ |
>
> (checked on a dense grid against `np.angle`.)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="magnitude |sin 2w| and wrapped linear phase of slope -4" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="175.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| = |sin 2ω|</text><line x1="40.0" y1="60.0" x2="310.0" y2="60.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="210.0" x2="310.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="175.0" y1="30.0" x2="175.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="40.0" y1="207.0" x2="40.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="40.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="73.8" y1="207.0" x2="73.8" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="73.8" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="107.5" y1="207.0" x2="107.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="107.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="141.2" y1="207.0" x2="141.2" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="141.2" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="175.0" y1="207.0" x2="175.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="175.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="208.8" y1="207.0" x2="208.8" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="208.8" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="242.5" y1="207.0" x2="242.5" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="242.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="276.2" y1="207.0" x2="276.2" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="276.2" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="310.0" y1="207.0" x2="310.0" y2="213.0" stroke="currentColor" stroke-width="1"/><text x="310.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="172.0" y1="60.0" x2="178.0" y2="60.0" stroke="currentColor" stroke-width="1"/><text x="36.0" y="64.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="310.0" y="204.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="40.0,210.0 50.8,137.7 58.9,94.4 62.7,79.2 66.5,68.6 70.1,62.2 71.9,60.5 73.8,60.0 75.6,60.5 77.4,62.2 81.0,68.6 84.8,79.2 88.6,94.4 96.7,137.7 107.5,210.0 117.5,142.7 125.0,101.0 128.5,85.7 131.9,73.9 135.2,65.8 138.6,61.2 140.6,60.1 142.5,60.3 144.5,61.7 146.5,64.5 150.6,73.9 154.7,88.4 158.9,107.7 163.4,132.8 175.0,210.0 187.1,130.0 191.8,104.3 196.2,84.9 200.6,70.7 204.8,62.5 206.9,60.5 209.0,60.0 211.1,60.9 213.2,63.2 216.3,69.2 219.4,78.1 226.0,105.6 233.0,145.7 242.5,210.0 253.9,134.0 258.3,109.4 262.4,90.0 266.5,75.3 270.4,65.4 272.4,62.4 274.4,60.6 276.2,60.0 278.2,60.6 281.6,64.6 285.0,72.3 288.5,83.9 292.1,99.1 299.7,141.1 310.0,210.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="495.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) (principal value)</text><line x1="360.0" y1="210.0" x2="630.0" y2="210.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="30.0" x2="630.0" y2="30.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="120.0" x2="630.0" y2="120.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="495.0" y1="30.0" x2="495.0" y2="210.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="360.0" y1="117.0" x2="360.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="360.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="393.8" y1="117.0" x2="393.8" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="393.8" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="427.5" y1="117.0" x2="427.5" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="427.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="461.2" y1="117.0" x2="461.2" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="461.2" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="495.0" y1="117.0" x2="495.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="495.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="528.8" y1="117.0" x2="528.8" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="528.8" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="562.5" y1="117.0" x2="562.5" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="562.5" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="596.2" y1="117.0" x2="596.2" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="596.2" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px"></text><line x1="630.0" y1="117.0" x2="630.0" y2="123.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="224.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="492.0" y1="210.0" x2="498.0" y2="210.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π</text><line x1="492.0" y1="120.0" x2="498.0" y2="120.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="124.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="492.0" y1="30.0" x2="498.0" y2="30.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="34.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π</text><text x="630.0" y="114.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="360.1,120.2 393.7,209.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="393.8,30.0 427.4,119.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="427.6,30.2 494.9,209.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="495.1,120.2 528.7,209.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="528.8,30.0 562.4,119.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="562.6,30.2 629.9,209.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/></svg><figcaption><strong>SP2021 #2: X<sub>d</sub>(ω) = e<sup>−j4ω</sup> sin 2ω.</strong> Magnitude |sin 2ω| (zeros at 0, ±π/2, ±π; peaks 1 at ±π/4, ±3π/4). Phase: slope −4, plus π wherever sin 2ω &lt; 0, wrapped into [−π, π]; the gaps at 0 and ±π/2 are the sign flips (jumps of π), those at π/4 and −3π/4 are 2π wraps (at −π/4 and 3π/4 the phase passes through 0 without a break).</figcaption></figure>

> [!note] The phase is not odd here
> $\sin 2\omega = \frac{e^{j2\omega} - e^{-j2\omega}}{2j}$ gives $x[n] = \frac{1}{2j}\left(\delta[n-2] - \delta[n-6]\right)$, a **purely imaginary** sequence. So $X_d(-\omega) = -X_d^*(\omega)$: the magnitude is still even, but the phase obeys $\angle X_d(-\omega) = \pi - \angle X_d(\omega)$ instead of being odd. The key draws $-4\omega$ as one line from 0 to $-2\pi$ on $(0, \frac{\pi}{2})$ and on $(-\pi, -\frac{\pi}{2})$ instead of wrapping at $\frac{\pi}{4}$ and $-\frac{3\pi}{4}$; those angles agree mod $2\pi$, so both sketches are right. State which range you use.

> [!trap] Where points go
> - $\lvert X_d\rvert = \sin 2\omega$ (negative on half the axis) is the classic loss; the sign belongs in the phase as a jump of $\pi$.
> - Do not mirror the phase about $\omega = 0$ by habit: odd phase needs a real sequence.

## Problem 3 · A DTFT in the form $Ae^{-jB\omega}\sin(C\omega)$ (9 pts)

*Topic: computing a DTFT and pulling out a linear phase — [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]].*

> [!question] Problem 3
> The DTFT of $x[n] = 3\delta[n+1] - 3\delta[n-7]$ can be written as $X_d(\omega) = Ae^{-jB\omega}\sin(C\omega)$. Determine the (possibly complex) values of $A$, $B$, and $C$.

> [!success]- Solution 3
> The two samples sit at $n = -1$ and $n = 7$; factor out the midpoint $n = 3$:
> $$
> X_d(\omega) = 3e^{j\omega} - 3e^{-j7\omega} = 3e^{-j3\omega}\left(e^{j4\omega} - e^{-j4\omega}\right) = 3e^{-j3\omega}\cdot 2j\sin(4\omega) = 6j\,e^{-j3\omega}\sin(4\omega)
> $$
> $$
> \boldsymbol{A = 6j,\qquad B = 3,\qquad C = 4}
> $$
> ($A = -6j$, $C = -4$ is the same function.) (checked on a dense grid.)

> [!trap] Where points go
> - $e^{j\theta} - e^{-j\theta} = 2j\sin\theta$: the $j$ goes into $A$, which is why the problem says "possibly complex".
> - $B$ is the midpoint of the two sample positions, $\frac{-1+7}{2} = 3$, and $C$ is half their distance, $\frac{7-(-1)}{2} = 4$.

## Problem 4 · Circular shift with a sign (8 pts)

*Topic: the DFT and its properties (circular shift) — Lectures 17+ (not yet in these notes).*

> [!question] Problem 4
> Let $\{X[k]\}_{k=0}^{7}$ be the 8-point DFT of $x[n] = \{1, -2, 3, -4, 5, -6, 7, -8\}$. Determine the sequence $\{y[n]\}_{n=0}^{7}$ whose DFT is $Y[k] = e^{-j\left(\frac{6\pi}{8}k + \pi\right)}X[k]$, $k = 0, 1, \dots, 7$.

> [!success]- Solution 4
> $e^{-j\pi} = -1$ and $\frac{6\pi}{8}k = \frac{2\pi}{8}k\cdot 3$, so $Y[k] = -e^{-j\frac{2\pi}{8}3k}X[k]$: a circular shift by 3, then a sign flip.
> $$
> y[n] = -x[\langle n-3\rangle_8]:\qquad x[\langle n-3\rangle_8] = \{-6,\ 7,\ -8,\ 1,\ -2,\ 3,\ -4,\ 5\}
> $$
> $$
> \boldsymbol{y[n] = \{\underset{\uparrow}{6},\ -7,\ 8,\ -1,\ 2,\ -3,\ 4,\ -5\}}
> $$

```python
import numpy as np
x = np.array([1, -2, 3, -4, 5, -6, 7, -8])
k = np.arange(8)
y = np.fft.ifft(np.exp(-1j*(6*np.pi/8*k + np.pi)) * np.fft.fft(x))
print(np.round(y.real, 12))
```

```text
[ 6. -7.  8. -1.  2. -3.  4. -5.]
```

> [!trap] Where points go
> - The $\pi$ is a constant phase, not part of the shift: it negates every sample.
> - Shift by 3 means $y[0]$ comes from $x[\langle -3\rangle_8] = x[5]$.

## Problem 5 · Real or not, from the DFT (8 pts)

*Topic: the DFT and its properties (conjugate symmetry) — Lectures 17+ (not yet in these notes).*

> [!question] Problem 5
> Let $\{X[k]\}_{k=0}^{6} = \{-2, -4j, 3, 5, 3, 4j, -2j\}$ be the 7-point DFT of a signal $\{x[n]\}_{n=0}^{6}$. Is $\{x[n]\}_{n=0}^{6}$ real? Justify your answer.

> [!success]- Solution 5
> **Not real.** Fastest: the inverse DFT at $n = 0$ is the average of the $X[k]$,
> $$
> x[0] = \frac17\sum_{k=0}^{6}X[k] = \frac{-2 - 4j + 3 + 5 + 3 + 4j - 2j}{7} = \frac{9 - 2j}{7},
> $$
> which is complex. Equivalently, a real $x$ needs $X[k] = X^*[\langle -k\rangle_7]$, and $X[1] = -4j$ while $X^*[6] = 2j$.

> [!trap] Where points go
> - $X[0] = -2$ being real proves nothing; check the pairs $k \leftrightarrow N - k$ (here all three pairs fail).

## Problem 6 · CTFT, DTFT or DFT? (9 pts)

*Topic: which transform — DTFT ([[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]]) vs DFT and CTFT — Lectures 17+ (not yet in these notes).*

> [!question] Problem 6
> For each statement below, decide whether it best describes the CTFT, the DTFT or the DFT. You need not show your work and no partial credit will be given.
>
> (a) Suppose that a signal $x[n]$ satisfies $\sum_{n=-\infty}^{\infty}\lvert x[n]\rvert \lt \infty$ (i.e., it is absolutely summable). Then, this transform can be easily computed if the corresponding z-transform is known.
>
> (b) This transform can be applied to recorded data of finite length using a computer.
>
> (c) This transform is defined for infinitely many values of its frequency variable and it is typically **not** periodic as a function of its frequency variable.

> [!success]- Solution 6
> - **(a) DTFT.** Absolute summability puts the unit circle in the ROC, and then $X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$.
> - **(b) DFT.** Finitely many samples in, finitely many numbers out.
> - **(c) CTFT.** The DTFT is also defined for every $\omega$, but it is $2\pi$-periodic; the DFT has only $N$ values.

## Problem 7 · Amplitudes from a two-step spectrum (14 pts)

*Topic: the ideal-lowpass DTFT pair — [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]].*

> [!question] Problem 7
> The DTFT of the signal $x[n] = A_1\dfrac{\sin(\omega_0 n)}{\omega_0 n} + A_2\dfrac{\sin(2\omega_0 n)}{2\omega_0 n}$ is as shown below. Determine the constants $A_1$, $A_2$, and $\omega_0$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 200" width="640" height="200" role="img" aria-label="staircase spectrum with heights 2 and 1" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="60.0" y1="105.8" x2="580.0" y2="105.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="60.0" y1="51.7" x2="580.0" y2="51.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="60.0" y1="160.0" x2="580.0" y2="160.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="320.0" y1="30.0" x2="320.0" y2="160.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="60.0" y1="157.0" x2="60.0" y2="163.0" stroke="currentColor" stroke-width="1"/><text x="60.0" y="174.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="146.7" y1="157.0" x2="146.7" y2="163.0" stroke="currentColor" stroke-width="1"/><text x="146.7" y="174.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π/3</text><line x1="233.3" y1="157.0" x2="233.3" y2="163.0" stroke="currentColor" stroke-width="1"/><text x="233.3" y="174.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/3</text><line x1="320.0" y1="157.0" x2="320.0" y2="163.0" stroke="currentColor" stroke-width="1"/><text x="320.0" y="174.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="406.7" y1="157.0" x2="406.7" y2="163.0" stroke="currentColor" stroke-width="1"/><text x="406.7" y="174.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/3</text><line x1="493.3" y1="157.0" x2="493.3" y2="163.0" stroke="currentColor" stroke-width="1"/><text x="493.3" y="174.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π/3</text><line x1="580.0" y1="157.0" x2="580.0" y2="163.0" stroke="currentColor" stroke-width="1"/><text x="580.0" y="174.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="317.0" y1="105.8" x2="323.0" y2="105.8" stroke="currentColor" stroke-width="1"/><text x="56.0" y="109.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="317.0" y1="51.7" x2="323.0" y2="51.7" stroke="currentColor" stroke-width="1"/><text x="56.0" y="55.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><text x="580.0" y="154.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="60.0,160.0 146.7,160.0 146.7,105.8 233.3,105.8 233.3,51.7 406.7,51.7 406.7,105.8 493.3,105.8 493.3,160.0 580.0,160.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="330.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:13px">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text></svg><figcaption><strong>SP2021 #7: the given DTFT.</strong> X<sub>d</sub>(ω) = 2 for |ω| &lt; π/3, 1 for π/3 &lt; |ω| &lt; 2π/3, 0 for 2π/3 &lt; |ω| ≤ π.</figcaption></figure>

> [!success]- Solution 7
> The pair $\dfrac{\sin(Wn)}{\pi n} \leftrightarrow 1$ for $\lvert\omega\rvert \le W$ (0 for $W \lt \lvert\omega\rvert \le \pi$) scales to
> $$
> \frac{\sin(Wn)}{Wn} = \frac{\pi}{W}\cdot\frac{\sin(Wn)}{\pi n} \leftrightarrow \frac{\pi}{W}\ \text{ on } \lvert\omega\rvert \le W .
> $$
> So the first term is a rectangle of height $\frac{A_1\pi}{\omega_0}$ on $\lvert\omega\rvert \le \omega_0$ and the second one of height $\frac{A_2\pi}{2\omega_0}$ on $\lvert\omega\rvert \le 2\omega_0$; they stack.
>
> - Outer edge: $2\omega_0 = \frac{2\pi}{3}$, so $\boldsymbol{\omega_0 = \frac{\pi}{3}}$.
> - Outer step: $\frac{A_2\pi}{2\omega_0} = 1$, so $\boldsymbol{A_2 = \frac{2\omega_0}{\pi} = \frac23}$.
> - Inner step: $\frac{A_1\pi}{\omega_0} + 1 = 2$, so $\boldsymbol{A_1 = \frac{\omega_0}{\pi} = \frac13}$.
>
> (checked: the inverse DTFT of the staircase matches $x[n]$ with these constants for $\lvert n\rvert \le 40$.)

> [!trap] Where points go
> - Using height 1 for $\frac{\sin(Wn)}{Wn}$: that height belongs to $\frac{\sin(Wn)}{\pi n}$. The factor $\frac{\pi}{W}$ is the whole problem.
> - The two rectangles **add** on $\lvert\omega\rvert \lt \frac{\pi}{3}$; the inner height 2 is not $\frac{A_1\pi}{\omega_0}$ alone.

## Problem 8 · Undersampling a V-shaped spectrum (15 pts)

*Topic: sampling and aliasing — Lectures 17+ (not yet in these notes).*

> [!question] Problem 8
> The continuous-time signal $x_c(t)$ has the real-valued Fourier transform shown below. The signal $x_c(t)$ is sampled with a sampling period of $T$ to produce the discrete-time signal $x[n] = x_c(nT)$.
>
> (a) What is the Nyquist rate for the signal $x_c(t)$?
>
> (b) Sketch the DTFT $X_d(\omega)$ of $x[n]$ for $-\pi \lt \omega \lt \pi$ for the sampling frequency $F_s = 1/T = 5$ kHz.
>
> (c) Is the signal $x[n]$ real-valued? Justify your answer.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 190" width="640" height="190" role="img" aria-label="V-shaped spectrum rising from 0 at Omega=0 to 1 at plus/minus 10000 pi" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="70.0" y1="50.0" x2="570.0" y2="50.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="70.0" y1="150.0" x2="570.0" y2="150.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="320.0" y1="25.0" x2="320.0" y2="150.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="147.6" y1="147.0" x2="147.6" y2="153.0" stroke="currentColor" stroke-width="1"/><text x="147.6" y="164.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−10000π</text><line x1="320.0" y1="147.0" x2="320.0" y2="153.0" stroke="currentColor" stroke-width="1"/><text x="320.0" y="164.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="492.4" y1="147.0" x2="492.4" y2="153.0" stroke="currentColor" stroke-width="1"/><text x="492.4" y="164.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">10000π</text><line x1="317.0" y1="50.0" x2="323.0" y2="50.0" stroke="currentColor" stroke-width="1"/><text x="66.0" y="54.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="570.0" y="144.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">Ω (rad/s)</text><polyline points="70.0,150.0 147.6,150.0 147.6,50.0 320.0,150.0 492.4,50.0 492.4,150.0 570.0,150.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><line x1="147.6" y1="25.0" x2="147.6" y2="150.0" stroke="var(--muted)" stroke-width="1.0" stroke-dasharray="4 3"/><line x1="492.4" y1="25.0" x2="492.4" y2="150.0" stroke="var(--muted)" stroke-width="1.0" stroke-dasharray="4 3"/><text x="320.0" y="18.0" text-anchor="middle" fill="currentColor" style="font-size:13px">X<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(Ω)</text></svg><figcaption><strong>SP2021 #8: the given CTFT.</strong> X<sub>c</sub>(Ω) = |Ω|/(10000π) for |Ω| ≤ 10000π and 0 beyond: real, even, and largest at the band edges.</figcaption></figure>

> [!success]- Solution 8
> **(a)** The band edge is $10000\pi$ rad/s = 5 kHz, so the Nyquist rate is $\boldsymbol{10\ \text{kHz}}$.
>
> **(b)** $X_d(\omega) = \frac1T\sum_k X_c\!\left(\frac{\omega - 2\pi k}{T}\right)$, and the band edge lands at $10000\pi \cdot \frac{1}{5000} = 2\pi$: each copy is a V of width $4\pi$, so neighbours overlap. On $0 \le \omega \lt \pi$ only the copies $k = 0$ and $k = 1$ reach in:
> $$
> T X_d(\omega) = \frac{\omega}{2\pi} + \frac{2\pi - \omega}{2\pi} = 1,
> $$
> and the same on $-\pi \lt \omega \le 0$ with $k = -1$. So
> $$
> \boldsymbol{X_d(\omega) = \frac1T = 5000\quad\text{for all }\omega}
> $$
> a flat line: $x[n] = 5000\,\delta[n]$. (checked twice: the alias sum on a grid, and a numerical inverse CTFT giving $x_c(nT) = 5000\,\delta[n]$.)
>
> **(c) Yes.** $X_c$ is real and even, so $x_c(t)$ is real (and even), and so are its samples; indeed $x[n] = 5000\,\delta[n]$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="640" height="230" role="img" aria-label="V-shaped copies overlapping and summing to a constant" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="330.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">T·X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) at F<tspan baseline-shift="sub" style="font-size:75%">s</tspan> = 5 kHz</text><rect x="236.7" y="30.0" width="186.7" height="150.0" fill="var(--accent)" fill-opacity="0.08" stroke="none"/><polyline points="50.0,180.0 143.1,180.0 143.3,68.9 330.0,180.0 516.5,69.0 516.7,180.0 610.0,180.0" fill="none" stroke="var(--accent)" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="50.0,180.0 329.8,180.0 330.0,68.9 516.7,180.0 610.0,124.4" fill="none" stroke="var(--accent2)" stroke-width="1.4" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="50.0,124.4 143.3,180.0 330.0,68.9 330.2,180.0 610.0,180.0" fill="none" stroke="var(--accent2)" stroke-width="1.4" stroke-dasharray="5 3" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="50.0,68.9 610.0,68.9" fill="none" stroke="var(--hi)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><line x1="50.0" y1="68.9" x2="610.0" y2="68.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="50.0" y1="180.0" x2="610.0" y2="180.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="30.0" x2="330.0" y2="180.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="143.3" y1="177.0" x2="143.3" y2="183.0" stroke="currentColor" stroke-width="1"/><text x="143.3" y="194.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="236.7" y1="177.0" x2="236.7" y2="183.0" stroke="currentColor" stroke-width="1"/><text x="236.7" y="194.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="330.0" y1="177.0" x2="330.0" y2="183.0" stroke="currentColor" stroke-width="1"/><text x="330.0" y="194.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="423.3" y1="177.0" x2="423.3" y2="183.0" stroke="currentColor" stroke-width="1"/><text x="423.3" y="194.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="516.7" y1="177.0" x2="516.7" y2="183.0" stroke="currentColor" stroke-width="1"/><text x="516.7" y="194.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="327.0" y1="68.9" x2="333.0" y2="68.9" stroke="currentColor" stroke-width="1"/><text x="46.0" y="72.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="610.0" y="174.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><text x="54.0" y="51.1" text-anchor="start" fill="var(--hi)" style="font-size:11px">copies add to 1  ⇒  X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) = 1/T = 5000</text></svg><figcaption><strong>SP2021 #8(b): undersampling by exactly 2 makes the copies fill in.</strong> At T = 1/5000 s the band edge 10000π maps to ω = 2π, so each copy (solid: k = 0, dashed: k = ±1) is a V of width 4π. On any interval the falling side of one copy and the rising side of the next add to 1, so X<sub>d</sub>(ω) = 5000 everywhere, the DTFT of 5000 δ[n].</figcaption></figure>

> [!note] Labels in the key's figure
> The key labels the copies $X_c(\frac{\Omega}{F_s} \pm 2\pi)$, mixing the analog and digital variables; read them as $F_s X_c\big((\omega \pm 2\pi)F_s\big)$, the copies centred at $\omega = \mp 2\pi$ (the key's "$+2\pi$" copy is the one centred at $-2\pi$). The answer (5000, flat) is right.

> [!trap] Where points go
> - Forgetting the $\frac1T$: the height is 5000, not 1.
> - Aliasing does not always look like damage: here the copies fill each other in exactly. Add the overlapping copies; do not just draw them side by side.

## Problem 9 · Two inputs, one output (12 pts)

*Topic: sampling and reconstruction (aliasing) — Lectures 17+ (not yet in these notes).*

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 110" width="560" height="110" role="img" aria-label="block diagram ideal A/D followed by ideal D/A" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="20.0" y1="40.0" x2="114.4" y2="40.0" stroke="currentColor" stroke-width="1.4"/><path d="M120.0,40.0 L113.0,36.9 L113.0,43.1 Z" fill="currentColor"/><text x="70.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:13px">x<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(t)</text><rect x="120.0" y="20.0" width="110" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="175.0" y="45.0" text-anchor="middle" fill="currentColor" style="font-size:13px">ideal A/D</text><line x1="175.0" y1="82.0" x2="175.0" y2="66.6" stroke="currentColor" stroke-width="1.4"/><path d="M175.0,61.0 L171.8,68.0 L178.2,68.0 Z" fill="currentColor"/><text x="175.0" y="96.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-style:italic">T</text><line x1="230.0" y1="40.0" x2="324.4" y2="40.0" stroke="currentColor" stroke-width="1.4"/><path d="M330.0,40.0 L323.0,36.9 L323.0,43.1 Z" fill="currentColor"/><text x="280.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:13px">x[n]</text><rect x="330.0" y="20.0" width="110" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="1.4"/><text x="385.0" y="45.0" text-anchor="middle" fill="currentColor" style="font-size:13px">ideal D/A</text><line x1="385.0" y1="82.0" x2="385.0" y2="66.6" stroke="currentColor" stroke-width="1.4"/><path d="M385.0,61.0 L381.9,68.0 L388.1,68.0 Z" fill="currentColor"/><text x="385.0" y="96.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-style:italic">T</text><line x1="440.0" y1="40.0" x2="534.4" y2="40.0" stroke="currentColor" stroke-width="1.4"/><path d="M540.0,40.0 L533.0,36.9 L533.0,43.1 Z" fill="currentColor"/><text x="490.0" y="32.0" text-anchor="middle" fill="currentColor" style="font-size:13px">y<tspan baseline-shift="sub" style="font-size:75%">c</tspan>(t)</text></svg><figcaption><strong>Sampling and reconstruction</strong>: an ideal A/D and an ideal D/A with the same interval T.</figcaption></figure>

> [!question] Problem 9
> Suppose the output of the D/A in the system above is found to be $y_c(t) = 2\cos(300\pi t)$ when the sampling frequency is $F_s = 1/T = 400$ Hz.
>
> (a) Determine $x[n]$.
>
> (b) Assume $x_c(t)$ is bandlimited to 400 Hz. Determine the two different input signals $x_c(t) = x_1(t)$ and $x_c(t) = x_2(t)$ that could have produced the given output of the D/A.

> [!success]- Solution 9
> **(a)** The ideal D/A returns the unique signal band-limited to $\lvert\Omega\rvert \lt \pi/T = 400\pi$ that passes through the samples, so $x[n] = y_c(nT)$ with $\omega = \Omega T = \frac{300\pi}{400} = \frac{3\pi}{4}$:
> $$
> \boldsymbol{x[n] = 2\cos\left(\frac{3\pi}{4}n\right)}
> $$
> **(b)** An input cosine at $F$ Hz gives the same samples when $\frac{F}{F_s} \equiv \pm\frac38 \pmod 1$: $F = 150, 250, 550, 650, \dots$ Hz. Below 400 Hz only two remain:
> $$
> \boldsymbol{x_1(t) = 2\cos(300\pi t),\qquad x_2(t) = 2\cos(500\pi t)}
> $$
> Check: $2\cos\left(\frac{500\pi}{400}n\right) = 2\cos\left(2\pi n - \frac{3\pi}{4}n\right) = 2\cos\left(\frac{3\pi}{4}n\right)$. (checked: scanning 0–400 Hz in 0.5 Hz steps finds exactly 150 and 250 Hz.)

> [!trap] Where points go
> - The band limit (400 Hz) is above $F_s/2 = 200$ Hz; that is the only reason a second input exists.
> - Keep amplitude 2 and phase 0: $2\cos(500\pi t + \phi)$ with $\phi \ne 0$ samples to $2\cos(\frac{3\pi}{4}n - \phi)$, a different $x[n]$.

## Related

- [[exams/midterm-2/past-exams/index|All past exams]] · previous: [[exams/midterm-2/past-exams/fall-2021|Fall 2021]] · next: [[exams/midterm-2/past-exams/fall-2019|Fall 2019]]
- Lectures: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]] · [[3-fourier-analysis/14-dtft-properties|L14]] · [[3-fourier-analysis/16-magnitude-and-phase-response|L16]]
- [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[exams/midterm-1/past-exams/spring-2021|Spring 2021 · Midterm 1]]

### Sources for this page

- ECE 310 Midterm Exam 2, Spring 2021 (Profs. Moon, Katselis, Shomorony), typed key `old-exams/mt2/ECE310_sp2021_e02_sol.pdf`; the photographed #2 sketch and the #7–#9 figures were read from 110–220-dpi renders, and the figures above are redrawn.
- Every answer re-derived and checked in `verify/E1_sp2021.py` (21 checks: DTFTs on dense grids, the principal phase of #2 piece by piece, `np.fft` for #4–#5, a numerical inverse DTFT of the #7 staircase, the alias sum and a numerical inverse CTFT for #8, a frequency scan for #9).
