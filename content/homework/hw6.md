---
title: "HW6 · CTFT pairs, inverse DTFTs, and frequency response (site solutions)"
description: "ECE 310 Homework 6 (due Oct 9) with folded solutions, matching the official key: three CTFTs, conjugation and reversal, three inverse DTFTs, DTFT vs. z-transform, the accumulator, a comb filter, a complex-valued system."
tags: [homework, midterm-2, dtft, frequency-response]
---

*Homework 6 · due Fri Oct 9, 2026, 11:59 pm (Gradescope) · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (the CTFT and the DTFT), [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (pairs and properties), [[3-fourier-analysis/15-frequency-response|Lecture 15]] (frequency response), [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] (magnitude and phase) · 7 problems · official solutions v1.0 (posted Oct 16) agree with every answer here · prev: [[homework/hw5|HW5]] · [[homework/index|all homework]]*

> [!abstract] In one breath
> - CTFT: $\Omega$ in rad/s, not periodic. Inverse DTFT by reading exponentials; a 3.5-sample delay is a sampled sinc.
> - DTFT = $X(e^{j\omega})$ only if the ROC contains the unit circle.
> - Sinusoid in → $H_d(\omega_0)$ out; the cosine formula needs a real $h[n]$.

| # | Skill | Links |
|---|---|---|
| 1 | CTFT from the definition | [[concepts/fourier-series\|Fourier series and the CTFT]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] |
| 2 | Conjugation, time reversal | [[concepts/dtft-properties\|DTFT properties]] · [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 3 | Inverse DTFT | [[problems/dtft-and-inverse-dtft\|DTFT and inverse DTFT]] |
| 4 | DTFT vs. z-transform | [[concepts/region-of-convergence\|ROC]] |
| 5 | Accumulator: $H_d \neq H(e^{j\omega})$ | [[concepts/marginal-stability\|marginal stability]] · [[3-fourier-analysis/15-frequency-response\|L15]] |
| 6 | Comb filter | [[problems/magnitude-phase-and-group-delay\|magnitude, phase and group delay]] · [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] |
| 7 | Complex-valued system | [[problems/lti-response-to-sinusoids\|LTI response to sinusoids]] |

## Problem 1 — three continuous-time Fourier transforms

> [!question] Problem 1
> Determine the Fourier transform of the following functions:
>
> (a) $\delta(5t-2)$
>
> (b) $\cos(\Omega_0 t + \phi_0)$, where $\Omega_0$ and $\phi_0$ are known real numbers.
>
> (c) $u(t) - u(t-T)$, where $T$ is a constant.

> [!key] CTFT (Lecture 13)
> $$
> X_c(\Omega) = \int_{-\infty}^{\infty} x_c(t)\,e^{-j\Omega t}\,dt, \qquad x_c(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X_c(\Omega)\,e^{j\Omega t}\,d\Omega .
> $$
> Not periodic. Sifting: $\int f(t)\,\delta(t-a)\,dt = f(a)$; scaling: $\delta(at-b) = \frac{1}{\lvert a\rvert}\,\delta\!\left(t-\frac{b}{a}\right)$.

> [!success]- Solution (a)
> $\tau = 5t$:
> $$
> X_c(\Omega) = \int_{-\infty}^{\infty}\delta(5t-2)\,e^{-j\Omega t}\,dt = \frac15\int_{-\infty}^{\infty}\delta(\tau-2)\,e^{-j\Omega\tau/5}\,d\tau = \frac15\,e^{-j2\Omega/5}.
> $$
> Equivalently $\delta(5t-2) = \tfrac15\,\delta\!\left(t-\tfrac25\right)$. **Answer.** $X_c(\Omega) = \dfrac15\,e^{-j2\Omega/5}$.

> [!success]- Solution (b)
> $e^{j\Omega_0 t} \leftrightarrow c\,\delta(\Omega-\Omega_0)$; inverse transform gives $\frac{c}{2\pi}e^{j\Omega_0 t}$, so $c = 2\pi$:
> $$
> e^{j\Omega_0 t} \overset{\mathcal F}{\longleftrightarrow} 2\pi\,\delta(\Omega-\Omega_0).
> $$
> $\cos(\Omega_0 t+\phi_0) = \tfrac12 e^{j\phi_0}e^{j\Omega_0 t} + \tfrac12 e^{-j\phi_0}e^{-j\Omega_0 t}$:
> $$
> X_c(\Omega) = \pi e^{j\phi_0}\,\delta(\Omega-\Omega_0) + \pi e^{-j\phi_0}\,\delta(\Omega+\Omega_0), \qquad \text{for all real } \Omega .
> $$
> No $2\pi$ repetition (compare [[homework/hw5|HW5]] #1(c)).

> [!success]- Solution (c)
> For $T \gt 0$ the pulse is $1$ on $[0, T)$:
> $$
> \begin{aligned}
> X_c(\Omega) &= \int_0^T e^{-j\Omega t}\,dt = \left[\frac{e^{-j\Omega t}}{-j\Omega}\right]_0^T = \frac{1-e^{-j\Omega T}}{j\Omega}
> = e^{-j\Omega T/2}\,\frac{e^{j\Omega T/2}-e^{-j\Omega T/2}}{j\Omega}\\
> &= \frac{2\sin(\Omega T/2)}{\Omega}\,e^{-j\Omega T/2} = T\,\frac{\sin(\Omega T/2)}{\Omega T/2}\,e^{-j\Omega T/2}, \qquad X_c(0) = T .
> \end{aligned}
> $$
> Zeros at $\Omega = 2\pi k/T$, $k \neq 0$. Same formula for $T \lt 0$.

**On the exam:** CTFT sketches start the sampling problems, e.g. [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5.

## Problem 2 — conjugation and time reversal

> [!question] Problem 2
> Let $x[n]$ be an arbitrary sequence, not necessarily real-valued, with DTFT $X_d(\omega)$. Express the DTFT of the following sequences in terms of $X_d(\omega)$:
>
> (a) $x^*[n]$
>
> (b) $x^*[-n]$

> [!success]- Solution (a)
> $$
> \sum_{n=-\infty}^{\infty}x^*[n]\,e^{-j\omega n} = \left(\sum_{n=-\infty}^{\infty}x[n]\,e^{j\omega n}\right)^{\!*} = \left(\sum_{n=-\infty}^{\infty}x[n]\,e^{-j(-\omega)n}\right)^{\!*} = X_d^*(-\omega).
> $$
> **Answer.** $x^*[n] \overset{\mathcal F}{\longleftrightarrow} X_d^*(-\omega)$.

> [!success]- Solution (b)
> $m = -n$:
> $$
> \sum_{n=-\infty}^{\infty}x^*[-n]\,e^{-j\omega n} = \sum_{m=-\infty}^{\infty}x^*[m]\,e^{j\omega m} = \left(\sum_{m=-\infty}^{\infty}x[m]\,e^{-j\omega m}\right)^{\!*} = X_d^*(\omega).
> $$
> **Answer.** $x^*[-n] \overset{\mathcal F}{\longleftrightarrow} X_d^*(\omega)$. Real $x$: (a) gives Hermitian symmetry.

**On the exam:** [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(c): "the DTFT of a real-valued signal is always Hermitian symmetric" (true).

## Problem 3 — three inverse DTFTs

> [!question] Problem 3
> Find $x[n]$ for each DTFT given below:
>
> (a) $X_d(\omega) = e^{-j3\omega} + 2e^{-j10\omega}$
>
> (b) $X_d(\omega) = e^{-j3.5\omega}$
>
> (c) $X_d(\omega) = \cos^2(\omega)$

> [!success]- Solution (a)
> $x[n] = \delta[n-3] + 2\delta[n-10]$.

> [!success]- Solution (b)
> Read $e^{-j3.5\omega}$ on $-\pi \lt \omega \lt \pi$ and repeat:
> $$
> \begin{aligned}
> x[n] &= \frac{1}{2\pi}\int_{-\pi}^{\pi}e^{-j3.5\omega}e^{j\omega n}\,d\omega = \frac{1}{2\pi}\left[\frac{e^{j\omega(n-3.5)}}{j(n-3.5)}\right]_{-\pi}^{\pi}\\
> &= \frac{1}{2\pi}\cdot\frac{2j\sin\big(\pi(n-3.5)\big)}{j(n-3.5)} = \frac{\sin\big(\pi(n-3.5)\big)}{\pi(n-3.5)} .
> \end{aligned}
> $$
> $\sin(\pi n - 3.5\pi) = \sin\!\left(\pi n + \tfrac{\pi}{2} - 4\pi\right) = \cos(\pi n) = (-1)^n$:
> $$
> \begin{gathered}
> x[n] = \frac{(-1)^n}{\pi(n-3.5)}:\qquad x[3] = x[4] = \frac{2}{\pi} \approx 0.637,\\
> x[2] = x[5] = -\frac{2}{3\pi} \approx -0.212,\quad x[0] = -\frac{2}{7\pi} \approx -0.091 .
> \end{gathered}
> $$
> Energy $1$, but not absolutely summable (decays like $1/n$).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="640" height="230" role="img" aria-label="Stem plot of (-1)^n/(pi(n-3.5)) for n=-4..11, symmetric about n=3.5" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="330.0" y="20.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">x[n] = (−1)ⁿ / (π(n − 3.5))</text><line x1="40.0" y1="168.1" x2="620.0" y2="168.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="108.2" x2="620.0" y2="108.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="78.3" x2="620.0" y2="78.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="48.4" x2="620.0" y2="48.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="138.1" x2="620.0" y2="138.1" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="204.7" y1="26.0" x2="204.7" y2="186.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="61.5" y1="135.1" x2="61.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="61.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−4</text><line x1="97.3" y1="135.1" x2="97.3" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="97.3" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3</text><line x1="133.1" y1="135.1" x2="133.1" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="133.1" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2</text><line x1="168.9" y1="135.1" x2="168.9" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="168.9" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="204.7" y1="135.1" x2="204.7" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="204.7" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="240.5" y1="135.1" x2="240.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="240.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="276.3" y1="135.1" x2="276.3" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="276.3" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2</text><line x1="312.1" y1="135.1" x2="312.1" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="312.1" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3</text><line x1="347.9" y1="135.1" x2="347.9" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="347.9" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">4</text><line x1="383.7" y1="135.1" x2="383.7" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="383.7" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">5</text><line x1="419.5" y1="135.1" x2="419.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="419.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">6</text><line x1="455.3" y1="135.1" x2="455.3" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="455.3" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">7</text><line x1="491.1" y1="135.1" x2="491.1" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="491.1" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">8</text><line x1="526.9" y1="135.1" x2="526.9" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="526.9" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">9</text><line x1="562.7" y1="135.1" x2="562.7" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="562.7" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">10</text><line x1="598.5" y1="135.1" x2="598.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="598.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">11</text><line x1="201.7" y1="168.1" x2="207.7" y2="168.1" stroke="currentColor" stroke-width="1"/><text x="36.0" y="172.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">−0.2</text><line x1="201.7" y1="108.2" x2="207.7" y2="108.2" stroke="currentColor" stroke-width="1"/><text x="36.0" y="112.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">0.2</text><line x1="201.7" y1="78.3" x2="207.7" y2="78.3" stroke="currentColor" stroke-width="1"/><text x="36.0" y="82.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">0.4</text><line x1="201.7" y1="48.4" x2="207.7" y2="48.4" stroke="currentColor" stroke-width="1"/><text x="36.0" y="52.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">0.6</text><text x="620.0" y="132.1" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><line x1="330.0" y1="26.0" x2="330.0" y2="186.0" stroke="var(--accent2)" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="61.5" y1="138.1" x2="61.5" y2="144.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="61.5" cy="144.5" r="3.2" fill="var(--accent)"/><line x1="97.3" y1="138.1" x2="97.3" y2="130.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="97.3" cy="130.8" r="3.2" fill="var(--accent)"/><line x1="133.1" y1="138.1" x2="133.1" y2="146.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="133.1" cy="146.8" r="3.2" fill="var(--accent)"/><line x1="168.9" y1="138.1" x2="168.9" y2="127.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="168.9" cy="127.6" r="3.2" fill="var(--accent)"/><line x1="204.7" y1="138.1" x2="204.7" y2="151.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="204.7" cy="151.7" r="3.2" fill="var(--accent)"/><line x1="240.5" y1="138.1" x2="240.5" y2="119.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="240.5" cy="119.1" r="3.2" fill="var(--accent)"/><line x1="276.3" y1="138.1" x2="276.3" y2="169.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="276.3" cy="169.9" r="3.2" fill="var(--accent)"/><line x1="312.1" y1="138.1" x2="312.1" y2="43.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="312.1" cy="43.0" r="3.2" fill="var(--accent)"/><line x1="347.9" y1="138.1" x2="347.9" y2="43.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="347.9" cy="43.0" r="3.2" fill="var(--accent)"/><line x1="383.7" y1="138.1" x2="383.7" y2="169.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="383.7" cy="169.9" r="3.2" fill="var(--accent)"/><line x1="419.5" y1="138.1" x2="419.5" y2="119.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="419.5" cy="119.1" r="3.2" fill="var(--accent)"/><line x1="455.3" y1="138.1" x2="455.3" y2="151.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="455.3" cy="151.7" r="3.2" fill="var(--accent)"/><line x1="491.1" y1="138.1" x2="491.1" y2="127.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="491.1" cy="127.6" r="3.2" fill="var(--accent)"/><line x1="526.9" y1="138.1" x2="526.9" y2="146.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="526.9" cy="146.8" r="3.2" fill="var(--accent)"/><line x1="562.7" y1="138.1" x2="562.7" y2="130.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="562.7" cy="130.8" r="3.2" fill="var(--accent)"/><line x1="598.5" y1="138.1" x2="598.5" y2="144.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="598.5" cy="144.5" r="3.2" fill="var(--accent)"/><text x="336.0" y="177.0" text-anchor="start" fill="var(--accent2)" style="font-size:11px">n = 3.5</text><text x="302.1" y="41.0" text-anchor="end" fill="var(--accent)" style="font-size:11px">2/π</text></svg><figcaption><strong>HW6 #3(b): the inverse DTFT of e<sup>−j3.5ω</sup> is a sampled sinc centred between samples.</strong> x[3] = x[4] = 2/π ≈ 0.637, symmetric about n = 3.5.</figcaption></figure>

> [!success]- Solution (c)
> $$
> \cos^2\omega = \frac{1+\cos 2\omega}{2} = \frac12 + \frac14 e^{j2\omega} + \frac14 e^{-j2\omega} .
> $$
> $x[n] = \tfrac14\delta[n+2] + \tfrac12\delta[n] + \tfrac14\delta[n-2] = \{\tfrac14,\ 0,\ \underset{\uparrow}{\tfrac12},\ 0,\ \tfrac14\}$.

**On the exam:** [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #5: $e^{-j\omega/3}$ on $\lvert\omega\rvert \le \pi$ gives $x[n] = \frac{\sin(\pi(n-1/3))}{\pi(n-1/3)}$.

## Problem 4 — when is the DTFT the z-transform on the unit circle?

> [!question] Problem 4
> Compare the DTFT and z-transform of the following sequences:
>
> (a) $x[n] = 3^{-n}u[n]$
>
> (b) $x[n] = e^{jn\frac{\pi}{4}}u[n]$

> [!key] Rule
> ROC contains the unit circle ⇒ $X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$. Pole on the unit circle ⇒ DTFT only with an impulse at the pole's angle. ROC away from the circle ⇒ no DTFT.

> [!success]- Solution (a)
> $$
> \begin{gathered}
> X(z) = \frac{1}{1-\frac13 z^{-1}},\quad \lvert z\rvert \gt \tfrac13;\\
> X_d(\omega) = \sum_{n=0}^{\infty}\left(\tfrac13 e^{-j\omega}\right)^n = \frac{1}{1-\frac13 e^{-j\omega}} = X(z)\Big|_{z=e^{j\omega}} .
> \end{gathered}
> $$
> Equal: the ROC contains $\lvert z\rvert = 1$.

> [!success]- Solution (b)
> $$
> X(z) = \sum_{n=0}^{\infty}\left(e^{j\pi/4}z^{-1}\right)^n = \frac{1}{1-e^{j\pi/4}z^{-1}}, \qquad \lvert z\rvert \gt 1 .
> $$
> Pole on the unit circle; $\sum_n\lvert x[n]\rvert = \infty$. Frequency shift of $u[n] \leftrightarrow \frac{1}{1-e^{-j\omega}} + \pi\delta(\omega)$:
> $$
> X_d(\omega) = \frac{1}{1-e^{-j(\omega-\pi/4)}} + \pi\sum_{k=-\infty}^{\infty}\delta\!\left(\omega-\tfrac{\pi}{4}-2\pi k\right).
> $$
> $X_d(\omega) \neq X(z)\big|_{z=e^{j\omega}}$: the substitution misses the impulse.

**On the exam:** [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(a): "$X(z)$ at $z = e^{j\omega}$ is always the DTFT" (false).

## Problem 5 — the accumulator's frequency response

> [!question] Problem 5
> A causal LSI system is described by the difference equation $y[n] - y[n-1] = x[n]$.
>
> (a) Determine the system's transfer function $H(z)$.
>
> (b) Determine the system's unit pulse response $h[n]$.
>
> (c) Determine the system's frequency response $H_d(\omega)$; is $H_d(\omega) = H(z)\big|_{z=e^{j\omega}}$? If not, explain why.

> [!success]- Solution
> **(a)** $Y(z) - z^{-1}Y(z) = X(z)$: $H(z) = \dfrac{1}{1-z^{-1}}$, ROC $\lvert z\rvert \gt 1$.
>
> **(b)** $h[n] = u[n]$ (accumulator).
>
> **(c)**
> $$
> H_d(\omega) = \frac{1}{1-e^{-j\omega}} + \pi\sum_{k=-\infty}^{\infty}\delta(\omega-2\pi k).
> $$
> **No.** The ROC $\lvert z\rvert \gt 1$ excludes the unit circle (pole at $z = 1$): marginally stable, $\sum_n\lvert h[n]\rvert = \infty$. $H(e^{j\omega})$ misses $\pi\delta(\omega)$; the two agree away from $\omega = 0$. The reason is the ROC, not causality.

**On the exam:** [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2: $H(z) = \frac{1-z^{-1}}{1-z^{-2}} = \frac{1}{1+z^{-1}}$, $H_d(\omega) = \frac{1}{1-e^{-j(\omega-\pi)}} + \pi\sum_k\delta(\omega-\pi-2\pi k)$.

## Problem 6 — a comb filter

> [!question] Problem 6
> An LSI system is described by the difference equation $y[n] = x[n] + x[n-10]$.
>
> (a) Compute and sketch its magnitude and phase response.
>
> (b) Determine its output to the inputs
>
> i. $x[n] = \cos\!\left(\tfrac{\pi}{10}n\right) + 3\sin\!\left(\tfrac{\pi}{3}n + \tfrac{\pi}{10}\right)$
>
> ii. $x[n] = 10 + 5\cos\!\left(\tfrac{2\pi}{5}n + \tfrac{\pi}{2}\right)$

> [!success]- Solution (a)
> $1 + e^{-jN\omega} = 2\cos\!\left(\tfrac{N\omega}{2}\right)e^{-jN\omega/2}$, $N = 10$:
> $$
> \begin{gathered}
> H_d(\omega) = 1 + e^{-j10\omega} = 2\cos(5\omega)\,e^{-j5\omega},\\
> \lvert H_d(\omega)\rvert = 2\lvert\cos 5\omega\rvert, \qquad \angle H_d(\omega) = -5\omega + \angle\cos(5\omega).
> \end{gathered}
> $$
> - Peaks of $2$ at $\omega = \tfrac{k\pi}{5}$; ten notches at $\omega = \tfrac{\pi}{10} + \tfrac{k\pi}{5}$.
> - Phase: slope $-5$ from $\tfrac{\pi}{2}$ to $-\tfrac{\pi}{2}$ on each lobe, jump $+\pi$ at each notch. Group delay 5.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 268" width="640" height="268" role="img" aria-label="Magnitude 2|cos 5w| and sawtooth phase of 1 + e^{-j10w} on [-pi, pi]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="174.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| = 2|cos 5ω|</text><line x1="40.0" y1="139.1" x2="308.0" y2="139.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="58.3" x2="308.0" y2="58.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="220.0" x2="308.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="174.0" y1="30.0" x2="174.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="40.0" y1="217.0" x2="40.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="40.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="107.0" y1="217.0" x2="107.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="107.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="174.0" y1="217.0" x2="174.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="174.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="241.0" y1="217.0" x2="241.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="241.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="308.0" y1="217.0" x2="308.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="308.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="171.0" y1="139.1" x2="177.0" y2="139.1" stroke="currentColor" stroke-width="1"/><text x="36.0" y="143.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="171.0" y1="58.3" x2="177.0" y2="58.3" stroke="currentColor" stroke-width="1"/><text x="36.0" y="62.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><text x="308.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="40.0,58.3 41.2,59.8 42.7,66.2 44.4,78.9 45.9,95.0 48.9,138.2 53.4,220.0 57.9,138.2 60.9,95.0 63.6,69.4 65.1,61.4 66.6,58.3 67.5,58.8 68.0,59.8 69.5,66.2 71.2,78.9 72.7,95.0 75.7,138.2 80.2,220.0 84.7,138.2 87.7,95.0 90.2,70.6 91.9,61.4 93.4,58.3 94.3,58.8 94.8,59.8 96.3,66.2 98.0,78.9 99.5,95.0 103.7,158.1 107.0,220.0 111.5,138.2 114.5,95.0 117.2,69.4 118.7,61.4 120.2,58.3 121.1,58.8 121.6,59.8 123.1,66.2 124.8,78.9 126.3,95.0 129.3,138.2 133.8,220.0 137.1,158.1 141.3,95.0 144.0,69.4 145.5,61.4 147.0,58.3 147.9,58.8 148.4,59.8 149.9,66.2 151.6,78.9 153.1,95.0 156.1,138.2 160.6,220.0 164.6,146.6 167.6,101.3 170.1,74.5 171.8,63.5 173.3,58.8 173.8,58.3 174.7,58.8 176.2,63.5 177.9,74.5 179.4,89.2 182.9,138.2 187.4,220.0 191.4,146.6 194.4,101.3 196.9,74.5 198.6,63.5 200.1,58.8 200.6,58.3 201.5,58.8 203.0,63.5 204.7,74.5 206.2,89.2 209.7,138.2 214.2,220.0 218.2,146.6 221.2,101.3 223.7,74.5 224.9,66.2 226.4,59.8 227.4,58.3 228.3,58.8 229.8,63.5 231.5,74.5 233.0,89.2 236.5,138.2 241.0,220.0 245.5,138.2 249.5,83.8 251.7,66.2 253.2,59.8 254.2,58.3 255.1,58.8 256.1,61.4 257.8,70.6 258.8,78.9 261.3,107.9 264.5,158.1 267.8,220.0 272.3,138.2 275.8,89.2 277.3,74.5 279.0,63.5 280.5,58.8 281.0,58.3 281.9,58.8 283.4,63.5 284.6,70.6 287.6,101.3 290.6,146.6 294.6,220.0 297.9,158.1 302.1,95.0 303.6,78.9 305.3,66.2 306.8,59.8 308.0,58.3" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="174.0" cy="58.3" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="187.4" cy="220.0" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="218.7" cy="139.1" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="227.6" cy="58.3" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="205.4" y="214.0" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/10</text><text x="235.7" y="143.1" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/3</text><text x="239.6" y="52.3" text-anchor="middle" fill="var(--hi)" style="font-size:10px">2π/5</text><text x="490.0" y="18.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="360.0" y1="220.0" x2="620.0" y2="220.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="172.5" x2="620.0" y2="172.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="77.5" x2="620.0" y2="77.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="30.0" x2="620.0" y2="30.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="125.0" x2="620.0" y2="125.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="490.0" y1="30.0" x2="490.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="360.0" y1="122.0" x2="360.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="360.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="425.0" y1="122.0" x2="425.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="425.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="490.0" y1="122.0" x2="490.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="490.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="555.0" y1="122.0" x2="555.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="555.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="620.0" y1="122.0" x2="620.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="620.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="487.0" y1="220.0" x2="493.0" y2="220.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="224.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π</text><line x1="487.0" y1="172.5" x2="493.0" y2="172.5" stroke="currentColor" stroke-width="1"/><text x="356.0" y="176.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="487.0" y1="125.0" x2="493.0" y2="125.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="487.0" y1="77.5" x2="493.0" y2="77.5" stroke="currentColor" stroke-width="1"/><text x="356.0" y="81.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="487.0" y1="30.0" x2="493.0" y2="30.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="34.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π</text><text x="620.0" y="119.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="360.0,125.0 372.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="373.2,78.1 398.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="399.2,78.1 424.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="425.2,78.1 450.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="451.2,78.1 476.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="477.2,78.1 502.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="503.2,78.1 528.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="529.2,78.1 554.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="555.2,78.1 580.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="581.2,78.1 606.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="607.2,78.1 620.0,125.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="533.3" cy="93.3" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="547.3" y="89.3" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/3</text></svg><figcaption><strong>HW6 #6(a): y[n] = x[n] + x[n − 10] is a comb filter.</strong> Red dots: the input frequencies of part (b).</figcaption></figure>

> [!success]- Solution (b)
> **i.** $H_d\!\left(\tfrac{\pi}{10}\right) = 2\cos\tfrac{\pi}{2}\,e^{-j\pi/2} = 0$; $H_d\!\left(\tfrac{\pi}{3}\right) = 2\cos\tfrac{5\pi}{3}\,e^{-j5\pi/3} = 2\cdot\tfrac12\cdot e^{-j5\pi/3} = e^{j\pi/3}$:
> $$
> y[n] = 0 + 3\sin\!\left(\tfrac{\pi}{3}n + \tfrac{\pi}{10} + \tfrac{\pi}{3}\right) = 3\sin\!\left(\tfrac{\pi}{3}n + \tfrac{13\pi}{30}\right).
> $$
> **ii.** $H_d(0) = 2$, $H_d\!\left(\tfrac{2\pi}{5}\right) = 2\cos 2\pi\,e^{-j2\pi} = 2$:
> $$
> y[n] = 20 + 10\cos\!\left(\tfrac{2\pi}{5}n + \tfrac{\pi}{2}\right) = 20 - 10\sin\!\left(\tfrac{2\pi}{5}n\right).
> $$
> Check ii: period 5 divides 10, so $x[n-10] = x[n]$ and $y = 2x$.

**On the exam:** [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #5: $h[n] = \delta[n] + \delta[n-6]$, $H_d = 2e^{-j3\omega}\cos 3\omega$.

## Problem 7 — a complex-valued system

> [!question] Problem 7
> The frequency response of an LSI system is
> $$
> H_d(\omega) = \omega\,e^{j\sin\omega}, \qquad \lvert\omega\rvert \le \pi .
> $$
> Determine the system output $y[n]$ for the following inputs:
>
> (a) $x[n] = 3 - 10e^{j\left(\frac{\pi}{4}n + 45^\circ\right)} + j^n$
>
> (b) $x[n] = 3 + 10\cos\!\left(\tfrac{\pi}{4}n + 45^\circ\right) - j^n$

> [!key] First: is h[n] real?
> Real ⇔ $H_d^*(\omega) = H_d(-\omega)$. If not, split each sinusoid into exponentials.

> [!success]- Solution — gains
> $H_d(-\omega) = (-\omega)\,e^{j\sin(-\omega)} = -\omega\,e^{-j\sin\omega} = -H_d^*(\omega)$: $h[n]$ is not real (purely imaginary).
> $$
> H_d(0) = 0,\qquad H_d\!\left(\tfrac{\pi}{4}\right) = \tfrac{\pi}{4}\,e^{j\frac{\sqrt2}{2}},\qquad H_d\!\left(-\tfrac{\pi}{4}\right) = -\tfrac{\pi}{4}\,e^{-j\frac{\sqrt2}{2}},\qquad H_d\!\left(\tfrac{\pi}{2}\right) = \tfrac{\pi}{2}\,e^{j} .
> $$
> $45^\circ = \tfrac{\pi}{4}$; $\sin\tfrac{\pi}{4} = \tfrac{\sqrt2}{2}$ rad.

> [!success]- Solution (a)
> $$
> \begin{aligned}
> y[n] &= 3H_d(0) - 10H_d\!\left(\tfrac{\pi}{4}\right)e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} + H_d\!\left(\tfrac{\pi}{2}\right)e^{j\frac{\pi}{2}n}\\
> &= 0 - \frac{10\pi}{4}\,e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)} + \frac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)} .
> \end{aligned}
> $$
> **Answer.** $y[n] = -\dfrac{5\pi}{2}\,e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)} + \dfrac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)}$.

> [!success]- Solution (b)
> $10\cos\!\left(\tfrac{\pi}{4}n+\tfrac{\pi}{4}\right) = 5e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} + 5e^{-j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)}$:
> $$
> \begin{aligned}
> y[n] &= 3H_d(0) + 5H_d\!\left(\tfrac{\pi}{4}\right)e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} + 5H_d\!\left(-\tfrac{\pi}{4}\right)e^{-j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} - H_d\!\left(\tfrac{\pi}{2}\right)e^{j\frac{\pi}{2}n}\\
> &= \frac{5\pi}{4}\left[e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)} - e^{-j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)}\right] - \frac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)}\\
> &= j\,\frac{5\pi}{2}\sin\!\left(\tfrac{\pi}{4}n+\tfrac{\pi}{4}+\tfrac{\sqrt2}{2}\right) - \frac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)} .
> \end{aligned}
> $$
> The real-system formula would give the wrong $\frac{5\pi}{2}\cos\!\left(\tfrac{\pi}{4}n+\tfrac{\pi}{4}+\tfrac{\sqrt2}{2}\right)$.

> [!trap] Traps
> - $\delta(5t-2)$: impulse at $t = \tfrac25$ with area $\tfrac15$. No $2\pi$ copies in a CTFT.
> - Conjugation alone gives $X_d^*(-\omega)$; reversal flips $\omega$ again.
> - "$\delta[n-3.5]$" does not exist. $\cos^2\omega$ squares the spectrum, so convolve in time; squaring the samples of $\tfrac12\delta[n+1]+\tfrac12\delta[n-1]$ is wrong.
> - Magnitude is $2\lvert\cos 5\omega\rvert$; plot the phase as a principal value ($\tfrac{\pi}{3}$, not $-\tfrac{5\pi}{3}$).
> - Cosine shortcut needs $H_d(-\omega_0) = H_d^*(\omega_0)$.

**On the exam:** Hermitian test first: [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #6 ($\omega e^{j\pi\cos\omega}$, not real), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #4 ($\lvert\omega\rvert e^{-j\pi\sin\omega}$, real).

## Related

[[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/group-delay|group delay]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[demos/frequency-response-explorer|frequency response explorer]] · [[homework/hw5|HW5]]

### Sources for this page

ECE 310 Fall 2026 HW6 and official solutions v1.0 (Oct 16); Lecture 13–16 notes (Snyder); past Midterm 2 exams cited above.
