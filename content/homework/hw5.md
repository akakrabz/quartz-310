---
title: "HW5 · The DTFT from the definition, and four numbers you can read without it"
description: "ECE 310 Homework 5 (due Oct 4) with folded solutions: four DTFTs from the definition, then X_d(0), X_d(π), the area under X_d and the energy integral of a plotted signal without a closed form."
tags: [homework, midterm-2, dtft]
---

*Homework 5 · due Sun Oct 4, 2026 (Gradescope; the PDF header prints "2025", a typo) · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (the DTFT) and [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (DTFT pairs and properties) · 100 points (60 + 40) · official solutions v1.0 · prev: [[homework/hw4|HW4]] · next: [[homework/hw6|HW6]] · [[homework/index|all homework]]*

> [!abstract] In one breath
> - $X_d(\omega) = \sum_k x[k]e^{-j\omega k}$; factor out the centre's linear phase to get cosines or sines.
> - A sinusoid → impulses at $\pm\omega_0$ (every $2\pi$); $e^{j\omega_0 n}$ shifts the spectrum by $\omega_0$.
> - $X_d(0)$, $X_d(\pi)$, $\int X_d$, $\int\lvert X_d\rvert^2$ come straight from $x[n]$.

| # | Skill | Links |
|---|---|---|
| 1(a), (b) | Finite sequences from the definition | [[concepts/dtft\|DTFT]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] |
| 1(c) | Phase-shifted cosine → impulses | [[concepts/dtft-pairs\|DTFT pairs]] · [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 1(d) | Geometric series + frequency shift | [[concepts/dtft-properties\|DTFT properties]] |
| 2 | Four numbers without $X_d$ | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |

## Problem 1 — four DTFTs from the definition

> [!question] Problem 1 (60 pts)
> Compute the discrete-time Fourier transform (DTFT) for each of the following discrete-time sequences. **Do not use DTFT table pairs unless noted otherwise.** You may use DTFT table properties, if necessary.
>
> (a) $x[n] = \{1,\ 0,\ \underset{\uparrow}{0},\ 0,\ -1\}$
>
> (b) $x[n] = u[n] - u[n-4]$
>
> (c) $x[n] = \cos\!\left(\tfrac{\pi}{3}n + \tfrac{\pi}{4}\right)$; you may use $e^{j\omega_0 n} \overset{\mathcal F}{\longleftrightarrow} 2\pi\delta(\omega-\omega_0)$, if necessary.
>
> (d) $x[n] = \alpha^n e^{j\omega_0 n}u[n]$, where $\lvert\alpha\rvert \lt 1$ and $\omega_0$ is a real constant. You may use $e^{j\omega_0 n} \overset{\mathcal F}{\longleftrightarrow} 2\pi\delta(\omega-\omega_0)$, if necessary.

Forms marked (∗) are accepted by the key.

> [!success]- Solution (a)
> $x[n] = \delta[n+2] - \delta[n-2]$:
> $$
> X_d(\omega) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n} = e^{-j\omega(-2)} - e^{-j\omega(2)} = e^{j2\omega} - e^{-j2\omega} = 2j\sin(2\omega).
> $$
> **Answer.** $X_d(\omega) = 2j\sin(2\omega)$ (or $e^{j2\omega} - e^{-j2\omega}$ (∗)). Real, odd $x$ → imaginary, odd $X_d$.

> [!success]- Solution (b)
> $x[n] = \delta[n]+\delta[n-1]+\delta[n-2]+\delta[n-3]$:
> $$
> X_d(\omega) = 1 + e^{-j\omega} + e^{-j2\omega} + e^{-j3\omega}. \qquad (\ast)
> $$
> Factor out the centre $e^{-j\frac32\omega}$:
> $$
> \begin{aligned}
> X_d(\omega) &= \left(1 + e^{-j3\omega}\right) + \left(e^{-j\omega} + e^{-j2\omega}\right)\\
> &= e^{-j\frac32\omega}\left(e^{j\frac32\omega} + e^{-j\frac32\omega}\right) + e^{-j\frac32\omega}\left(e^{j\frac12\omega} + e^{-j\frac12\omega}\right) \qquad (\ast)\\
> &= 2e^{-j\frac32\omega}\left(\cos\tfrac{\omega}{2} + \cos\tfrac{3\omega}{2}\right).
> \end{aligned}
> $$
> Geometric series ([[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], Exercise 2, $L=4$):
> $$
> \begin{aligned}
> X_d(\omega) &= \sum_{n=0}^{3}\left(e^{-j\omega}\right)^n = \frac{1-e^{-j4\omega}}{1-e^{-j\omega}}\\
> &= \frac{e^{-j2\omega}\left(e^{j2\omega}-e^{-j2\omega}\right)}{e^{-j\frac12\omega}\left(e^{j\frac12\omega}-e^{-j\frac12\omega}\right)}
> = e^{-j\frac32\omega}\,\frac{\sin(2\omega)}{\sin(\omega/2)} \qquad (\ast)
> \end{aligned}
> $$
> (limit $4$ at $\omega = 0$).
>
> **Answer.** $X_d(\omega) = 2e^{-j\frac32\omega}\left(\cos\tfrac{\omega}{2} + \cos\tfrac{3\omega}{2}\right)$ or any (∗) form. Checks: $X_d(0) = 4$, $X_d(\pi) = 0$.

> [!success]- Solution (c)
> $$
> \cos\!\left(\tfrac{\pi}{3}n + \tfrac{\pi}{4}\right) = \tfrac12 e^{j\left(\frac{\pi}{3}n+\frac{\pi}{4}\right)} + \tfrac12 e^{-j\left(\frac{\pi}{3}n+\frac{\pi}{4}\right)}
> = \tfrac12 e^{j\frac{\pi}{4}}\,e^{j\frac{\pi}{3}n} + \tfrac12 e^{-j\frac{\pi}{4}}\,e^{-j\frac{\pi}{3}n}.
> $$
> $$
> X_d(\omega) = \tfrac12 e^{j\frac{\pi}{4}}\cdot 2\pi\delta\!\left(\omega-\tfrac{\pi}{3}\right) + \tfrac12 e^{-j\frac{\pi}{4}}\cdot 2\pi\delta\!\left(\omega+\tfrac{\pi}{3}\right) \qquad (\ast)
> $$
> $$
> X_d(\omega) = \pi e^{j\frac{\pi}{4}}\,\delta\!\left(\omega-\tfrac{\pi}{3}\right) + \pi e^{-j\frac{\pi}{4}}\,\delta\!\left(\omega+\tfrac{\pi}{3}\right),\qquad -\pi \le \omega \lt \pi,
> $$
> repeated every $2\pi$:
> $$
> X_d(\omega) = \pi\sum_{k=-\infty}^{\infty}\left[e^{j\frac{\pi}{4}}\,\delta\!\left(\omega-\tfrac{\pi}{3}-2\pi k\right) + e^{-j\frac{\pi}{4}}\,\delta\!\left(\omega+\tfrac{\pi}{3}-2\pi k\right)\right].
> $$
> Weights are conjugates (real signal).

> [!success]- Solution (d)
> $g[n] = e^{j\omega_0 n}$, $h[n] = \alpha^n u[n]$, $G_d(\omega) = 2\pi\delta(\omega-\omega_0)$:
> $$
> H_d(\omega) = \sum_{n=-\infty}^{\infty}\alpha^n u[n]e^{-j\omega n} = \sum_{n=0}^{\infty}\left(\alpha e^{-j\omega}\right)^n = \frac{1}{1-\alpha e^{-j\omega}},
> $$
> ($\lvert\alpha e^{-j\omega}\rvert = \lvert\alpha\rvert \lt 1$). Windowing property:
> $$
> \begin{aligned}
> X_d(\omega) &= \frac{1}{2\pi}\int_{-\pi}^{\pi} G_d(\theta)\,H_d(\omega-\theta)\,d\theta
> = \frac{1}{2\pi}\int_{-\pi}^{\pi} 2\pi\delta(\theta-\omega_0)\,\frac{1}{1-\alpha e^{-j(\omega-\theta)}}\,d\theta\\
> &= \frac{1}{1-\alpha e^{-j(\omega-\omega_0)}} .
> \end{aligned}
> $$
> Or directly: frequency shift $e^{j\omega_0 n}h[n] \leftrightarrow H_d(\omega-\omega_0)$ (properties allowed, pairs not).
>
> **Answer.** $X_d(\omega) = \dfrac{1}{1-\alpha e^{-j(\omega-\omega_0)}}$. Check: $X_d(\omega_0) = \frac{1}{1-\alpha}$.

**On the exam:** [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #3: $3\delta[n+1]-3\delta[n-7]$ as $Ae^{-jB\omega}\sin(C\omega)$, $A = 6j$, $B = 3$, $C = 4$.

## Problem 2 — four numbers from a plot, no closed form

> [!question] Problem 2 (40 pts)
> A discrete-time signal $x[n]$ is depicted in the figure below. Without explicitly determining a closed-form expression for $X_d(\omega)$, find each of the following quantities.
>
> (a) $X_d(0)$
>
> (b) $X_d(\pi)$
>
> (c) $\displaystyle\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$
>
> (d) $\displaystyle\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2\,d\omega$

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 236" width="640" height="236" role="img" aria-label="Stem plot of x[n] with x[-2]=2, x[-1]=-1, x[0]=1, x[1]=-1, x[2]=2, zero elsewhere" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="150.0" y1="176.5" x2="510.0" y2="176.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="90.5" x2="510.0" y2="90.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="47.5" x2="510.0" y2="47.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="133.5" x2="510.0" y2="133.5" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="26.0" x2="330.0" y2="198.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="180.0" y1="130.5" x2="180.0" y2="136.5" stroke="currentColor" stroke-width="1"/><text x="180.0" y="212.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3</text><line x1="230.0" y1="130.5" x2="230.0" y2="136.5" stroke="currentColor" stroke-width="1"/><text x="230.0" y="212.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2</text><line x1="280.0" y1="130.5" x2="280.0" y2="136.5" stroke="currentColor" stroke-width="1"/><text x="280.0" y="212.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="330.0" y1="130.5" x2="330.0" y2="136.5" stroke="currentColor" stroke-width="1"/><text x="330.0" y="212.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="380.0" y1="130.5" x2="380.0" y2="136.5" stroke="currentColor" stroke-width="1"/><text x="380.0" y="212.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="430.0" y1="130.5" x2="430.0" y2="136.5" stroke="currentColor" stroke-width="1"/><text x="430.0" y="212.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2</text><line x1="480.0" y1="130.5" x2="480.0" y2="136.5" stroke="currentColor" stroke-width="1"/><text x="480.0" y="212.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3</text><line x1="327.0" y1="176.5" x2="333.0" y2="176.5" stroke="currentColor" stroke-width="1"/><text x="146.0" y="180.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">−1</text><line x1="327.0" y1="90.5" x2="333.0" y2="90.5" stroke="currentColor" stroke-width="1"/><text x="146.0" y="94.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="327.0" y1="47.5" x2="333.0" y2="47.5" stroke="currentColor" stroke-width="1"/><text x="146.0" y="51.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><text x="510.0" y="127.5" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><text x="336.0" y="37.0" text-anchor="start" fill="var(--muted)" style="font-size:12px">x[n]</text><line x1="180.0" y1="133.5" x2="180.0" y2="133.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="180.0" cy="133.5" r="3.2" fill="var(--accent)"/><line x1="230.0" y1="133.5" x2="230.0" y2="47.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="230.0" cy="47.5" r="3.2" fill="var(--accent)"/><line x1="280.0" y1="133.5" x2="280.0" y2="176.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="280.0" cy="176.5" r="3.2" fill="var(--accent)"/><line x1="330.0" y1="133.5" x2="330.0" y2="90.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="330.0" cy="90.5" r="3.2" fill="var(--accent)"/><line x1="380.0" y1="133.5" x2="380.0" y2="176.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="380.0" cy="176.5" r="3.2" fill="var(--accent)"/><line x1="430.0" y1="133.5" x2="430.0" y2="47.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="430.0" cy="47.5" r="3.2" fill="var(--accent)"/><line x1="480.0" y1="133.5" x2="480.0" y2="133.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="480.0" cy="133.5" r="3.2" fill="var(--accent)"/><text x="230.0" y="39.5" text-anchor="middle" fill="var(--accent)" style="font-size:11px">2</text><text x="430.0" y="39.5" text-anchor="middle" fill="var(--accent)" style="font-size:11px">2</text><text x="339.0" y="86.5" text-anchor="middle" fill="var(--accent)" style="font-size:11px">1</text><text x="280.0" y="192.5" text-anchor="middle" fill="var(--accent)" style="font-size:11px">−1</text><text x="380.0" y="192.5" text-anchor="middle" fill="var(--accent)" style="font-size:11px">−1</text></svg><figcaption><strong>The signal of HW5 #2 (redrawn from the assignment's figure):</strong> x[−2] = 2, x[−1] = −1, x[0] = 1, x[1] = −1, x[2] = 2, and x[n] = 0 for every other n.</figcaption></figure>

> [!key] Four numbers from $x[n]$
> | quantity | from | value |
> |---|---|---|
> | $X_d(0)$ | definition, $e^{-j0n} = 1$ | $\sum_n x[n]$ |
> | $X_d(\pi)$ | definition, $e^{-j\pi n} = (-1)^n$ | $\sum_n (-1)^n x[n]$ |
> | $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$ | inverse DTFT at $n = 0$ | $2\pi\,x[0]$ |
> | $\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega$ | Parseval | $2\pi\sum_n\lvert x[n]\rvert^2$ |

> [!success]- Solution (a)
> $x[n] = \{2,\ -1,\ \underset{\uparrow}{1},\ -1,\ 2\}$:
> $$
> X_d(0) = \sum_{n=-\infty}^{\infty}x[n]e^{-j(0)n} = \sum_{n=-2}^{2}x[n] = 2 + (-1) + 1 + (-1) + 2 = 3 .
> $$

> [!success]- Solution (b)
> $$
> \begin{aligned}
> X_d(\pi) &= \sum_{n=-2}^{2}(-1)^n x[n] = x[-2] - x[-1] + x[0] - x[1] + x[2]\\
> &= 2 - (-1) + 1 - (-1) + 2 = 7 .
> \end{aligned}
> $$

> [!success]- Solution (c)
> $$
> x[0] = \frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)e^{j\omega\cdot 0}\,d\omega \quad\Longrightarrow\quad \int_{-\pi}^{\pi}X_d(\omega)\,d\omega = 2\pi\,x[0] = 2\pi(1).
> $$
> **Answer.** $2\pi$.

> [!success]- Solution (d)
> $$
> \begin{gathered}
> \sum_{n=-\infty}^{\infty}\lvert x[n]\rvert^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega\\
> \Longrightarrow\quad
> \int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega = 2\pi\left(2^2 + (-1)^2 + 1^2 + (-1)^2 + 2^2\right) = 2\pi(11).
> \end{gathered}
> $$
> **Answer.** $22\pi$.
>
> Cross-check with the closed form (not allowed in the answer): $X_d(\omega) = 1 - 2\cos\omega + 4\cos 2\omega$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="The DTFT 1 - 2cos w + 4cos 2w on [-pi, pi] with X(0)=3, X(pi)=7 and mean value 1" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="150.0" y1="202.4" x2="510.0" y2="202.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="138.6" x2="510.0" y2="138.6" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="106.6" x2="510.0" y2="106.6" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="42.8" x2="510.0" y2="42.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="154.5" x2="510.0" y2="154.5" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="30.0" x2="330.0" y2="212.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="150.0" y1="151.5" x2="150.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="150.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="240.0" y1="151.5" x2="240.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="240.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="330.0" y1="151.5" x2="330.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="330.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="420.0" y1="151.5" x2="420.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="420.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="510.0" y1="151.5" x2="510.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="510.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="327.0" y1="202.4" x2="333.0" y2="202.4" stroke="currentColor" stroke-width="1"/><text x="146.0" y="206.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">−3</text><line x1="327.0" y1="138.6" x2="333.0" y2="138.6" stroke="currentColor" stroke-width="1"/><text x="146.0" y="142.6" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="327.0" y1="106.6" x2="333.0" y2="106.6" stroke="currentColor" stroke-width="1"/><text x="146.0" y="110.6" text-anchor="end" fill="var(--muted)" style="font-size:11px">3</text><line x1="327.0" y1="42.8" x2="333.0" y2="42.8" stroke="currentColor" stroke-width="1"/><text x="146.0" y="46.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">7</text><text x="510.0" y="148.5" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><text x="336.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:12px">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="150.0" y1="138.6" x2="510.0" y2="138.6" stroke="var(--accent2)" stroke-width="1.3" stroke-dasharray="5 4"/><polyline points="150.0,42.8 152.5,43.0 155.2,43.9 159.7,46.8 165.1,52.5 171.2,61.5 176.8,72.1 184.7,89.7 208.9,152.0 215.2,166.7 220.4,177.4 226.7,188.4 233.0,196.7 236.6,200.1 239.6,202.2 242.2,203.5 246.1,204.4 251.0,203.9 255.3,202.0 259.4,199.0 263.9,194.5 268.4,188.8 275.6,177.8 297.1,139.1 306.8,123.8 313.1,116.0 318.5,111.0 321.9,108.8 324.8,107.5 329.3,106.6 332.5,106.8 335.2,107.5 339.5,109.6 345.8,114.8 350.5,120.2 354.8,126.1 361.1,136.0 378.1,166.9 386.0,180.4 391.4,188.5 397.7,196.2 401.3,199.6 404.2,201.7 409.0,203.9 411.7,204.4 414.8,204.3 417.8,203.5 420.5,202.2 425.0,198.7 430.4,192.6 436.7,182.8 443.0,170.6 453.8,145.3 474.2,92.4 480.5,77.8 486.8,65.1 493.1,54.9 499.4,47.6 504.8,43.9 507.5,43.0 510.0,42.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="330.0" cy="106.6" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="510.0" cy="42.8" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="150.0" cy="42.8" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="233.7" y="132.6" text-anchor="middle" fill="var(--accent2)" style="font-size:11px">mean = x[0]</text></svg><figcaption><strong>The check you were not allowed to use: X<sub>d</sub>(ω) = 1 − 2cos ω + 4cos 2ω.</strong> Dots: X<sub>d</sub>(0) = 3, X<sub>d</sub>(±π) = 7; dashed: the average x[0] = 1.</figcaption></figure>

> [!trap] Traps
> - 1(a): the arrow is under the middle 0; starting at $n=0$ adds a phase $e^{-j2\omega}$.
> - 1(b): four samples ($n = 0,\dots,3$), not five.
> - 1(c): the phase goes into the weight, not the location; the weight is $\pi$, not $\tfrac12$.
> - Table pairs in #1 earned 6/15; the closed form in #2 earned 4/10.
> - #2(c), (d): the $2\pi$ factors; $x[0]$ is the sample at the arrow.

**On the exam:** [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #3: $\{1,-3,5,\underset{\uparrow}{-7},5,-3,1\}$ gives $-1$, $-25$, $2\pi(-7) = -14\pi$.

## Related

[[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[0-toolkit/02-geometric-series|geometric series]] · [[supplements/transform-tables|transform tables]] · [[homework/hw6|HW6]]

### Sources for this page

ECE 310 Fall 2026 HW5 and official solutions v1.0 (rubric, accepted forms); Lecture 13–14 notes (Snyder); past Midterm 2 exams cited above.
