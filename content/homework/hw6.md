---
title: "HW6 · CTFT pairs, inverse DTFTs, and frequency response (site solutions)"
description: "This site's own verified solutions to ECE 310 Homework 6 (Fall 2026; no official key yet): continuous-time Fourier transforms of a scaled and shifted Dirac impulse, a cosine with a phase and a rectangular pulse; the DTFTs of x*[n] and x*[−n]; three inverse DTFTs (integer delays, a delay of 3.5 samples, cos²ω); when the DTFT is the z-transform on the unit circle; the accumulator, whose frequency response needs an impulse; the comb filter y[n] = x[n] + x[n−10] with its magnitude, phase and sinusoidal outputs; and the complex-valued system ωe^{j sin ω}, where the real-system cosine formula fails."
tags: [homework, midterm-2, dtft, frequency-response]
draft: true
---

*Homework 6 · due Fri Oct 9, 2026, 11:59 pm (Gradescope) · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (the CTFT and the DTFT), [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (pairs and properties), [[3-fourier-analysis/15-frequency-response|Lecture 15]] (frequency response), [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] (magnitude and phase) · 7 problems · **no official solutions yet: these are this site's solutions** · prev: [[homework/hw5|HW5]] · [[homework/index|all homework]]*

> [!warning] A draft until the deadline, and not the official key
> This page has `draft: true` in its frontmatter, so the site's remove-draft plugin keeps it out of the published site while HW6 is open. **After Fri Oct 9, 11:59 pm, delete that line to publish it.** The solutions are this site's own, worked from the lecture notes and checked numerically in Python (`verify/HW_hw6.py`); they are not the official answer key. When the official solutions come out, compare them with this page.

> [!abstract] What HW6 trains
> The step from computing a transform to using one. **Transforms** (#1–#4): the continuous-time Fourier transform of Lecture 13 (frequency $\Omega$ in rad/s, no periodicity), conjugation and time reversal, inverse DTFTs by recognising exponentials (including a delay of 3.5 samples, which no single sample can carry), and the rule that the DTFT is the z-transform on the unit circle **only when the ROC contains it**. **Systems** (#5–#7): an accumulator whose frequency response needs an impulse; a comb filter whose magnitude, phase and sinusoidal outputs all come from one factorisation; and a complex-valued system where the real-system cosine formula gives a wrong answer.

| # | skill | concept · lecture |
|---|---|---|
| 1 | CTFT from the definition: sifting with a scaled argument, impulses for a cosine, a pulse | [[concepts/fourier-series\|Fourier series and the CTFT]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] |
| 2 | conjugation and time reversal | [[concepts/dtft-properties\|DTFT properties]] · [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 3 | inverse DTFT: integer delays, a non-integer delay, $\cos^2\omega$ | [[concepts/dtft\|DTFT]], [[concepts/dtft-pairs\|DTFT pairs]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]], [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 4 | DTFT versus z-transform: the ROC decides | [[concepts/dtft\|DTFT]], [[concepts/region-of-convergence\|ROC]] · [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 5 | LCCDE → $H(z)$ → $h[n]$ → $H_d(\omega)$, and why $H_d \neq H(e^{j\omega})$ here | [[concepts/frequency-response\|frequency response]], [[concepts/marginal-stability\|marginal stability]] · [[3-fourier-analysis/15-frequency-response\|L15]] |
| 6 | comb filter: magnitude and phase plots, outputs for sinusoids | [[concepts/magnitude-and-phase-response\|magnitude and phase response]], [[concepts/group-delay\|group delay]] · [[3-fourier-analysis/15-frequency-response\|L15]], [[3-fourier-analysis/16-magnitude-and-phase-response\|L16]] |
| 7 | eigenfunction outputs of a complex-valued system | [[concepts/eigenfunctions-of-lti-systems\|eigenfunctions]], [[concepts/frequency-response\|frequency response]] · [[3-fourier-analysis/15-frequency-response\|L15]] |

Every solution below is folded: read the statement, solve it on paper, then open the solution.

## Problem 1 — three continuous-time Fourier transforms

> [!question] Problem 1
> Determine the Fourier transform of the following functions:
>
> (a) $\delta(5t-2)$
>
> (b) $\cos(\Omega_0 t + \phi_0)$, where $\Omega_0$ and $\phi_0$ are known real numbers.
>
> (c) $u(t) - u(t-T)$, where $T$ is a constant.

**What it practises:** the continuous-time Fourier transform (CTFT) that [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] derives from the Fourier series, and the Dirac delta with its sifting property ([[3-fourier-analysis/14-dtft-properties|Lecture 14]], §2). Concept: [[concepts/fourier-series|Fourier series and the CTFT]]. The CTFT comes back with sampling later in the course, where the exams write it $X_c(\Omega)$.

> [!key] The CTFT conventions used here (Lecture 13, Eqs. 26–27)
> $$
> X_c(\Omega) = \int_{-\infty}^{\infty} x_c(t)\,e^{-j\Omega t}\,dt, \qquad x_c(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X_c(\Omega)\,e^{j\Omega t}\,d\Omega .
> $$
> $\Omega$ is in rad/s and runs over all real numbers: **a CTFT is not periodic**, unlike $X_d(\omega)$. Two Dirac facts: sifting, $\int f(t)\,\delta(t-a)\,dt = f(a)$; and scaling, $\delta(at-b) = \frac{1}{\lvert a\rvert}\,\delta\!\left(t-\frac{b}{a}\right)$.

> [!tip]- Hints (open one part at a time)
> - (a) Substitute $\tau = 5t$ inside the integral, or rewrite $\delta(5t-2)$ as a delta at $t = \tfrac25$ first. What is its area?
> - (b) Find the CTFT of $e^{j\Omega_0 t}$ the way Lecture 14 finds the DTFT of $e^{j\omega_0 n}$: guess $c\,\delta(\Omega-\Omega_0)$ and fix $c$ with the inverse transform. Then use Euler.
> - (c) For $T \gt 0$ the signal is $1$ on $[0, T)$. Integrate $e^{-j\Omega t}$ over that interval, then factor out the midpoint $e^{-j\Omega T/2}$.

> [!success]- Solution (a) — a delta with a scaled argument
> With $\tau = 5t$ ($dt = d\tau/5$; the limits stay $\mp\infty$ because $5 \gt 0$):
> $$
> X_c(\Omega) = \int_{-\infty}^{\infty}\delta(5t-2)\,e^{-j\Omega t}\,dt = \frac15\int_{-\infty}^{\infty}\delta(\tau-2)\,e^{-j\Omega\tau/5}\,d\tau = \frac15\,e^{-j2\Omega/5}.
> $$
> Equivalently, $\delta(5t-2) = \tfrac15\,\delta\!\left(t-\tfrac25\right)$: an impulse of area $\tfrac15$ at $t = \tfrac25$, and a delay by $t_0$ multiplies the transform by $e^{-j\Omega t_0}$.
>
> **Answer.** $X_c(\Omega) = \dfrac15\,e^{-j2\Omega/5}$: magnitude $\tfrac15$ at every frequency, linear phase $-\tfrac25\Omega$.
>
> **Checks.** $X_c(0) = \int x_c(t)\,dt$ is the area of $\delta(5t-2)$, which is $\tfrac15$, not $1$ ✓. Replacing the delta by a unit-area Gaussian of width $10^{-3}$ and integrating numerically reproduces $\tfrac15 e^{-j2\Omega/5}$ at $\Omega = 0,\ 1,\ 7.3,\ -12$ to $10^{-6}$ (checked).

> [!success]- Solution (b) — two impulses, and no copies
> **The pair.** Guess $e^{j\Omega_0 t} \leftrightarrow c\,\delta(\Omega-\Omega_0)$; the inverse transform sifts: $\frac{1}{2\pi}\int c\,\delta(\Omega-\Omega_0)\,e^{j\Omega t}\,d\Omega = \frac{c}{2\pi}e^{j\Omega_0 t}$, so $c = 2\pi$:
> $$
> e^{j\Omega_0 t} \overset{\mathcal F}{\longleftrightarrow} 2\pi\,\delta(\Omega-\Omega_0).
> $$
> **Euler**, with the phase as a constant weight: $\cos(\Omega_0 t+\phi_0) = \tfrac12 e^{j\phi_0}e^{j\Omega_0 t} + \tfrac12 e^{-j\phi_0}e^{-j\Omega_0 t}$, so by linearity
> $$
> X_c(\Omega) = \pi e^{j\phi_0}\,\delta(\Omega-\Omega_0) + \pi e^{-j\phi_0}\,\delta(\Omega+\Omega_0), \qquad \text{for all real } \Omega .
> $$
> **Answer.** The two impulses above, and nothing else: no repetition every $2\pi$.
>
> **Checks.** The inverse transform sifts both impulses back to $\cos(\Omega_0 t+\phi_0)$ ✓. Special case $\Omega_0 = 0$: the signal is the constant $\cos\phi_0$ and the impulses merge into $2\pi\cos\phi_0\,\delta(\Omega)$ ✓. Numerically, for $\Omega_0 = 3.7$, $\phi_0 = 0.9$, the time average of $x_c(t)e^{-j\Omega_0 t}$ over $[-4000, 4000]$ is $\tfrac12 e^{j\phi_0}$ to $10^{-3}$, and $2\pi$ times that is the weight $\pi e^{j\phi_0}$ (checked).
>
> Compare [[homework/hw5|HW5]] #1(c): the same two impulses with the same weights, but there they repeat every $2\pi$ because a DTFT is periodic.

> [!success]- Solution (c) — a pulse of width T
> For $T \gt 0$, $u(t)-u(t-T)$ is $1$ on $[0, T)$ and $0$ elsewhere:
> $$
> \begin{aligned}
> X_c(\Omega) &= \int_0^T e^{-j\Omega t}\,dt = \left[\frac{e^{-j\Omega t}}{-j\Omega}\right]_0^T = \frac{1-e^{-j\Omega T}}{j\Omega}
> = e^{-j\Omega T/2}\,\frac{e^{j\Omega T/2}-e^{-j\Omega T/2}}{j\Omega}\\
> &= \frac{2\sin(\Omega T/2)}{\Omega}\,e^{-j\Omega T/2} = T\,\frac{\sin(\Omega T/2)}{\Omega T/2}\,e^{-j\Omega T/2}, \qquad X_c(0) = T .
> \end{aligned}
> $$
> **Answer.** $X_c(\Omega) = \dfrac{1-e^{-j\Omega T}}{j\Omega} = \dfrac{2\sin(\Omega T/2)}{\Omega}\,e^{-j\Omega T/2}$, with $X_c(0) = T$.
>
> **Checks.** $X_c(0) = T$ is the area of the pulse ✓. Zeros at $\Omega = 2\pi k/T$, $k \neq 0$. The linear phase $-\Omega T/2$ says the pulse is centred at $t = T/2$: the continuous-time version of the $e^{-j\frac32\omega}$ in [[homework/hw5|HW5]] #1(b). "$T$ is a constant" allows $T \lt 0$: the signal is then $-1$ on $[T, 0)$, and the same formula comes out (with $X_c(0) = T \lt 0$). Numerical integration matches both forms for $T = 3,\ 0.5,\ -2$ at $\Omega = 0,\ 0.8,\ 2,\ -5.5$ (checked).

> [!trap] Three continuous-time slips
> - **$\delta(5t-2) \neq \delta(t-2)$, and $\neq \delta\!\left(t-\tfrac25\right)$ either.** The impulse sits at $t = \tfrac25$ and has area $\tfrac15$; both the location and the factor $\tfrac15$ come from the scaling rule.
> - **No $2\pi$ copies in continuous time.** $X_c(\Omega)$ has exactly two impulses. The phase $\phi_0$ lives in the weights, never in the locations.
> - **$\Omega$ is not $\omega$.** $\Omega$ is in rad/s and unbounded; $\omega$ is in rad/sample and lives on $[-\pi,\pi]$. The two meet only through sampling, later in the course.

**On the exam:** CTFT sketches return in the sampling problems of Midterm 2 (for example [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5 and [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8 start from a plotted $X_c(\Omega)$). [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #6 asks which transform a sentence describes; "defined for infinitely many frequencies and typically not periodic" is the CTFT.

## Problem 2 — conjugation and time reversal

> [!question] Problem 2
> Let $x[n]$ be an arbitrary sequence, not necessarily real-valued, with DTFT $X_d(\omega)$. Express the DTFT of the following sequences in terms of $X_d(\omega)$:
>
> (a) $x^*[n]$
>
> (b) $x^*[-n]$

**What it practises:** proving two lines of the [[3-fourier-analysis/14-dtft-properties|Lecture 14]] property table from the definition. Concept: [[concepts/dtft-properties|DTFT properties]].

> [!tip]- Hint
> Conjugate the whole sum: $\left(\sum_n a_n\right)^* = \sum_n a_n^*$ and $\left(e^{-j\omega n}\right)^* = e^{j\omega n}$. Then ask which frequency the conjugated sum is evaluated at. For (b), substitute $m = -n$.

> [!success]- Solution (a) — conjugation flips the frequency
> $$
> \sum_{n=-\infty}^{\infty}x^*[n]\,e^{-j\omega n} = \left(\sum_{n=-\infty}^{\infty}x[n]\,e^{j\omega n}\right)^{\!*} = \left(\sum_{n=-\infty}^{\infty}x[n]\,e^{-j(-\omega)n}\right)^{\!*} = X_d^*(-\omega).
> $$
> **Answer.** $x^*[n] \overset{\mathcal F}{\longleftrightarrow} X_d^*(-\omega)$.

> [!success]- Solution (b) — conjugation and reversal together
> With $m = -n$:
> $$
> \sum_{n=-\infty}^{\infty}x^*[-n]\,e^{-j\omega n} = \sum_{m=-\infty}^{\infty}x^*[m]\,e^{j\omega m} = \left(\sum_{m=-\infty}^{\infty}x[m]\,e^{-j\omega m}\right)^{\!*} = X_d^*(\omega).
> $$
> Or chain the table: $y[n] = x^*[n]$ has $Y_d(\omega) = X_d^*(-\omega)$ by (a), and time reversal gives $y[-n] \leftrightarrow Y_d(-\omega) = X_d^*(\omega)$.
>
> **Answer.** $x^*[-n] \overset{\mathcal F}{\longleftrightarrow} X_d^*(\omega)$.
>
> **Checks.** For a real $x$, $x^*[n] = x[n]$ and (a) becomes $X_d(\omega) = X_d^*(-\omega)$: Hermitian symmetry ✓. Both identities hold to $10^{-10}$ on a 4001-point grid for a random complex 9-sample sequence (checked).

> [!intuition] What (b) means
> $x^*[-n]$ has the same magnitude spectrum as $x[n]$ and the opposite phase. It is the complex-valued form of the matched filter of [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] ($\tilde h[n] = h[-n]$ for a real pattern): filtering $x$ with it gives the spectrum $X_d(\omega)X_d^*(\omega) = \lvert X_d(\omega)\rvert^2$, all phases aligned.

> [!trap] Each operation negates ω once
> Conjugation alone gives $X_d^*(-\omega)$, not $X_d^*(\omega)$; time reversal alone gives $X_d(-\omega)$. Applied together, the two sign flips cancel. The shortcut "conjugate in time ⇒ conjugate in frequency" is only half right.

**On the exam:** [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #7 proves the DFT version of the conjugation property and uses it to compute two real DFTs with one; the real-signal special case (Hermitian symmetry) is a True/False regular ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(c): "the DTFT of a real-valued signal is always Hermitian symmetric", true).

## Problem 3 — three inverse DTFTs

> [!question] Problem 3
> Find $x[n]$ for each DTFT given below:
>
> (a) $X_d(\omega) = e^{-j3\omega} + 2e^{-j10\omega}$
>
> (b) $X_d(\omega) = e^{-j3.5\omega}$
>
> (c) $X_d(\omega) = \cos^2(\omega)$

**What it practises:** reading a DTFT as a sum of exponentials, each one a delayed impulse (time-shift property, [[3-fourier-analysis/14-dtft-properties|Lecture 14]]), and falling back on the synthesis integral of [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] when that fails. Concepts: [[concepts/dtft|DTFT]], [[concepts/dtft-pairs|DTFT pairs]]; family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].

> [!tip]- Hints (open one part at a time)
> - (a) $e^{-j\omega k} \leftrightarrow \delta[n-k]$.
> - (b) $3.5$ is not an integer, so no single delayed sample has this DTFT. Evaluate $x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)e^{j\omega n}d\omega$.
> - (c) $\cos^2\omega = \tfrac12 + \tfrac12\cos 2\omega$, then Euler.

> [!success]- Solution (a) — two delayed impulses
> $e^{-j3\omega} \leftrightarrow \delta[n-3]$ and $e^{-j10\omega} \leftrightarrow \delta[n-10]$.
>
> **Answer.** $x[n] = \delta[n-3] + 2\delta[n-10]$.
>
> **Check.** $X_d(0) = 1 + 2 = 3 = \sum_n x[n]$ ✓.

> [!success]- Solution (b) — a delay of 3.5 samples is a sampled sinc
> **First, what the formula means.** A DTFT is $2\pi$-periodic, but $e^{-j3.5(\omega+2\pi)} = e^{-j7\pi}e^{-j3.5\omega} = -e^{-j3.5\omega}$. So $e^{-j3.5\omega}$ is read on one period, $-\pi \lt \omega \lt \pi$, and repeated from there (the convention [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #5 states explicitly with "for $\lvert\omega\rvert \le \pi$"). Then
> $$
> x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi}e^{-j3.5\omega}e^{j\omega n}\,d\omega = \frac{1}{2\pi}\left[\frac{e^{j\omega(n-3.5)}}{j(n-3.5)}\right]_{-\pi}^{\pi}
> = \frac{1}{2\pi}\cdot\frac{2j\sin\big(\pi(n-3.5)\big)}{j(n-3.5)} = \frac{\sin\big(\pi(n-3.5)\big)}{\pi(n-3.5)} .
> $$
> For integer $n$, $\sin(\pi n - 3.5\pi) = \sin\!\left(\pi n + \tfrac{\pi}{2} - 4\pi\right) = \cos(\pi n) = (-1)^n$, so
> $$
> x[n] = \frac{(-1)^n}{\pi(n-3.5)}:\qquad x[3] = x[4] = \frac{2}{\pi} \approx 0.637,\quad x[2] = x[5] = -\frac{2}{3\pi} \approx -0.212,\quad x[0] = -\frac{2}{7\pi} \approx -0.091 .
> $$
> **Answer.** $x[n] = \dfrac{\sin\big(\pi(n-3.5)\big)}{\pi(n-3.5)} = \dfrac{(-1)^n}{\pi(n-3.5)}$ for all $n$.
>
> **Checks.** With an integer delay $k$ in place of $3.5$ the same integral gives $\frac{\sin(\pi(n-k))}{\pi(n-k)} = \delta[n-k]$, which is part (a) ✓. The result is real and symmetric about $n = 3.5$, as a real signal with phase $-3.5\omega$ must be ✓. Its energy is $\sum_n\lvert x[n]\rvert^2 = 1 = \frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d\rvert^2 d\omega$ (Parseval) ✓, yet $\sum_n\lvert x[n]\rvert = \infty$, since $x$ decays only like $1/n$: this DTFT converges in energy, not absolutely, which is why its periodic extension can jump at $\omega = \pm\pi$. The synthesis integral computed numerically matches $(-1)^n/(\pi(n-3.5))$ for $n = -6,\dots,13$ to $10^{-12}$, and the DTFT sum over $\lvert n\rvert \le 2\cdot10^5$ gives back $e^{-j3.5\omega}$ at $\omega = 0.3,\ -1.2,\ 2.5$ to $10^{-4}$ (checked).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="640" height="230" role="img" aria-label="Stem plot of (-1)^n/(pi(n-3.5)) for n=-4..11, symmetric about n=3.5" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="330.0" y="20.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">x[n] = (−1)ⁿ / (π(n − 3.5))</text><line x1="40.0" y1="168.1" x2="620.0" y2="168.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="108.2" x2="620.0" y2="108.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="78.3" x2="620.0" y2="78.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="48.4" x2="620.0" y2="48.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="138.1" x2="620.0" y2="138.1" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="204.7" y1="26.0" x2="204.7" y2="186.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="61.5" y1="135.1" x2="61.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="61.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−4</text><line x1="97.3" y1="135.1" x2="97.3" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="97.3" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3</text><line x1="133.1" y1="135.1" x2="133.1" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="133.1" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2</text><line x1="168.9" y1="135.1" x2="168.9" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="168.9" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="204.7" y1="135.1" x2="204.7" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="204.7" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="240.5" y1="135.1" x2="240.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="240.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="276.3" y1="135.1" x2="276.3" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="276.3" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2</text><line x1="312.1" y1="135.1" x2="312.1" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="312.1" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3</text><line x1="347.9" y1="135.1" x2="347.9" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="347.9" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">4</text><line x1="383.7" y1="135.1" x2="383.7" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="383.7" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">5</text><line x1="419.5" y1="135.1" x2="419.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="419.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">6</text><line x1="455.3" y1="135.1" x2="455.3" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="455.3" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">7</text><line x1="491.1" y1="135.1" x2="491.1" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="491.1" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">8</text><line x1="526.9" y1="135.1" x2="526.9" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="526.9" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">9</text><line x1="562.7" y1="135.1" x2="562.7" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="562.7" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">10</text><line x1="598.5" y1="135.1" x2="598.5" y2="141.1" stroke="currentColor" stroke-width="1"/><text x="598.5" y="200.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">11</text><line x1="201.7" y1="168.1" x2="207.7" y2="168.1" stroke="currentColor" stroke-width="1"/><text x="36.0" y="172.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">−0.2</text><line x1="201.7" y1="108.2" x2="207.7" y2="108.2" stroke="currentColor" stroke-width="1"/><text x="36.0" y="112.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">0.2</text><line x1="201.7" y1="78.3" x2="207.7" y2="78.3" stroke="currentColor" stroke-width="1"/><text x="36.0" y="82.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">0.4</text><line x1="201.7" y1="48.4" x2="207.7" y2="48.4" stroke="currentColor" stroke-width="1"/><text x="36.0" y="52.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">0.6</text><text x="620.0" y="132.1" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><line x1="330.0" y1="26.0" x2="330.0" y2="186.0" stroke="var(--accent2)" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="61.5" y1="138.1" x2="61.5" y2="144.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="61.5" cy="144.5" r="3.2" fill="var(--accent)"/><line x1="97.3" y1="138.1" x2="97.3" y2="130.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="97.3" cy="130.8" r="3.2" fill="var(--accent)"/><line x1="133.1" y1="138.1" x2="133.1" y2="146.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="133.1" cy="146.8" r="3.2" fill="var(--accent)"/><line x1="168.9" y1="138.1" x2="168.9" y2="127.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="168.9" cy="127.6" r="3.2" fill="var(--accent)"/><line x1="204.7" y1="138.1" x2="204.7" y2="151.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="204.7" cy="151.7" r="3.2" fill="var(--accent)"/><line x1="240.5" y1="138.1" x2="240.5" y2="119.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="240.5" cy="119.1" r="3.2" fill="var(--accent)"/><line x1="276.3" y1="138.1" x2="276.3" y2="169.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="276.3" cy="169.9" r="3.2" fill="var(--accent)"/><line x1="312.1" y1="138.1" x2="312.1" y2="43.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="312.1" cy="43.0" r="3.2" fill="var(--accent)"/><line x1="347.9" y1="138.1" x2="347.9" y2="43.0" stroke="var(--accent)" stroke-width="1.6"/><circle cx="347.9" cy="43.0" r="3.2" fill="var(--accent)"/><line x1="383.7" y1="138.1" x2="383.7" y2="169.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="383.7" cy="169.9" r="3.2" fill="var(--accent)"/><line x1="419.5" y1="138.1" x2="419.5" y2="119.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="419.5" cy="119.1" r="3.2" fill="var(--accent)"/><line x1="455.3" y1="138.1" x2="455.3" y2="151.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="455.3" cy="151.7" r="3.2" fill="var(--accent)"/><line x1="491.1" y1="138.1" x2="491.1" y2="127.6" stroke="var(--accent)" stroke-width="1.6"/><circle cx="491.1" cy="127.6" r="3.2" fill="var(--accent)"/><line x1="526.9" y1="138.1" x2="526.9" y2="146.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="526.9" cy="146.8" r="3.2" fill="var(--accent)"/><line x1="562.7" y1="138.1" x2="562.7" y2="130.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="562.7" cy="130.8" r="3.2" fill="var(--accent)"/><line x1="598.5" y1="138.1" x2="598.5" y2="144.5" stroke="var(--accent)" stroke-width="1.6"/><circle cx="598.5" cy="144.5" r="3.2" fill="var(--accent)"/><text x="336.0" y="177.0" text-anchor="start" fill="var(--accent2)" style="font-size:11px">n = 3.5</text><text x="302.1" y="41.0" text-anchor="end" fill="var(--accent)" style="font-size:11px">2/π</text></svg><figcaption><strong>HW6 #3(b): the inverse DTFT of e<sup>−j3.5ω</sup> is a sampled sinc centred between samples.</strong> x[3] = x[4] = 2/π ≈ 0.637, symmetric about n = 3.5, decaying only like 1/n (so x is not absolutely summable, though its energy is exactly 1). A delay by a non-integer number of samples cannot just move one sample.</figcaption></figure>

> [!success]- Solution (c) — three exponentials
> $$
> \cos^2\omega = \frac{1+\cos 2\omega}{2} = \frac12 + \frac14 e^{j2\omega} + \frac14 e^{-j2\omega} .
> $$
> $e^{j2\omega} \leftrightarrow \delta[n+2]$ (an advance) and $e^{-j2\omega} \leftrightarrow \delta[n-2]$.
>
> **Answer.** $x[n] = \tfrac14\delta[n+2] + \tfrac12\delta[n] + \tfrac14\delta[n-2] = \{\tfrac14,\ 0,\ \underset{\uparrow}{\tfrac12},\ 0,\ \tfrac14\}$.
>
> **Another route.** $\cos\omega \leftrightarrow \tfrac12\delta[n+1] + \tfrac12\delta[n-1]$, and a product of spectra is a convolution in time: $\left(\tfrac12\delta[n+1]+\tfrac12\delta[n-1]\right)*\left(\tfrac12\delta[n+1]+\tfrac12\delta[n-1]\right)$ gives the same three samples.
>
> **Checks.** $X_d(0) = \cos^2 0 = 1 = \tfrac14+\tfrac12+\tfrac14$ ✓; $X_d(\pi) = 1$ as well, because all samples sit at even $n$ ✓; $x[0] = \frac{1}{2\pi}\int_{-\pi}^{\pi}\cos^2\omega\,d\omega = \tfrac12$ ✓.

> [!trap] Three inverse-DTFT slips
> - **"$\delta[n-3.5]$" does not exist.** A sequence has samples only at integers. Rounding to $\delta[n-3]$ or $\delta[n-4]$ is wrong too: a fractional delay spreads over every sample.
> - **Forgetting the sign of the exponent.** $e^{+j2\omega}$ is an advance, $\delta[n+2]$.
> - **Squaring the samples instead of the spectrum.** $\cos^2\omega$ is the spectrum squared, which is a convolution in time; squaring the samples of $\tfrac12\delta[n+1]+\tfrac12\delta[n-1]$ gives the wrong $\tfrac14\delta[n+1]+\tfrac14\delta[n-1]$.

**On the exam:** [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(b), True/False: "$X_d(\omega) = e^{-j\omega/2}$ on $[-\pi,\pi]$ gives $x[n] = \delta\!\left[n-\tfrac12\right]$" is false (the first trap above). [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #5 is 3(b) with a delay of $\tfrac13$: $X_d(\omega) = e^{-j\omega/3}$ for $\lvert\omega\rvert \le \pi$ gives $x[n] = \frac{\sin(\pi(n-1/3))}{\pi(n-1/3)}$. [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #2 reads $x[n]$ off a plotted $X_d(\omega)$ with the same synthesis integral and asks for a real-valued expression.

## Problem 4 — when is the DTFT the z-transform on the unit circle?

> [!question] Problem 4
> Compare the DTFT and z-transform of the following sequences:
>
> (a) $x[n] = 3^{-n}u[n]$
>
> (b) $x[n] = e^{jn\frac{\pi}{4}}u[n]$

**What it practises:** the link of [[3-fourier-analysis/14-dtft-properties|Lecture 14]] §1 between the two transforms, and the DTFTs "with impulses" of §2 for signals that are not absolutely summable. Concepts: [[concepts/dtft|DTFT]], [[concepts/region-of-convergence|ROC]], [[concepts/dtft-pairs|DTFT pairs]].

> [!key] The rule
> If the ROC of $X(z)$ contains the unit circle (equivalently $\sum_n\lvert x[n]\rvert \lt \infty$), the DTFT sum converges and $X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$. If a pole sits **on** the unit circle, the DTFT exists only as a generalised function, with an impulse at the pole's angle, and $X(e^{j\omega})$ is not the DTFT. If the ROC stays away from the unit circle altogether (e.g. $2^n u[n]$), there is no DTFT at all.

> [!tip]- Hint
> Find $X(z)$ and its ROC first. Then ask whether $z = e^{j\omega}$ lies inside the ROC for every $\omega$.

> [!success]- Solution (a) — ROC contains the unit circle
> $x[n] = \left(\tfrac13\right)^n u[n]$, so
> $$
> X(z) = \frac{1}{1-\frac13 z^{-1}},\quad \lvert z\rvert \gt \tfrac13; \qquad X_d(\omega) = \sum_{n=0}^{\infty}\left(\tfrac13 e^{-j\omega}\right)^n = \frac{1}{1-\frac13 e^{-j\omega}} = X(z)\Big|_{z=e^{j\omega}} .
> $$
> **Answer.** Both exist, and the DTFT is the z-transform evaluated on the unit circle, because $\lvert z\rvert = 1$ lies inside the ROC $\lvert z\rvert \gt \tfrac13$ (and $\sum_n\lvert x[n]\rvert = \tfrac32 \lt \infty$).
>
> **Checks.** $X_d(0) = \tfrac32 = \sum_n\left(\tfrac13\right)^n$ ✓ and $X_d(\pi) = \tfrac34 = \sum_n\left(-\tfrac13\right)^n$ ✓.

> [!success]- Solution (b) — a pole on the unit circle
> $$
> X(z) = \sum_{n=0}^{\infty}\left(e^{j\pi/4}z^{-1}\right)^n = \frac{1}{1-e^{j\pi/4}z^{-1}}, \qquad \lvert z\rvert \gt 1 .
> $$
> The pole $e^{j\pi/4}$ lies on the unit circle and the ROC $\lvert z\rvert \gt 1$ excludes it, so the DTFT sum does not converge: $\lvert x[n]\rvert = 1$ for all $n \ge 0$, $\sum_n\lvert x[n]\rvert = \infty$, and at $\omega = \tfrac{\pi}{4}$ the partial sums equal $N+1$. A DTFT exists only in the generalised sense: apply the frequency-shift property to the [[3-fourier-analysis/14-dtft-properties|Lecture 14]] pair $u[n] \leftrightarrow \frac{1}{1-e^{-j\omega}} + \pi\delta(\omega)$:
> $$
> X_d(\omega) = \frac{1}{1-e^{-j(\omega-\pi/4)}} + \pi\sum_{k=-\infty}^{\infty}\delta\!\left(\omega-\tfrac{\pi}{4}-2\pi k\right).
> $$
> **Answer.** The z-transform exists for $\lvert z\rvert \gt 1$; the DTFT exists only with the impulse at $\omega = \tfrac{\pi}{4}$, and $X_d(\omega) \neq X(z)\big|_{z=e^{j\omega}}$: substituting gives $\frac{1}{1-e^{-j(\omega-\pi/4)}}$, which is undefined at $\omega = \tfrac{\pi}{4}$ and misses the impulse.
>
> **Check.** Inverse DTFT, computed numerically as a principal value: the first term alone returns $+\tfrac12 e^{j\pi n/4}$ for $n \ge 0$ and $-\tfrac12 e^{j\pi n/4}$ for $n \lt 0$; the impulse adds $\frac{\pi}{2\pi}e^{j\pi n/4} = \tfrac12 e^{j\pi n/4}$ for every $n$. Together: $e^{j\pi n/4}u[n]$ ✓ (checked for $n = -4,\dots,5$).

> [!trap] Bounded is not summable
> $e^{j\pi n/4}u[n]$ never exceeds $1$ in magnitude, yet it has no ordinary DTFT, exactly as a bounded $h[n]$ need not be BIBO stable ([[homework/hw4|HW4]] #2). Writing $X(e^{j\omega})$ as "the DTFT" in (b) loses the impulse at $\omega = \tfrac{\pi}{4}$, which carries the oscillation at that frequency that never dies out.

**On the exam:** [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(a), True/False: "a signal with z-transform $X(z)$ always has a finite DTFT given by $X(z)$ at $z = e^{j\omega}$" is false, for exactly the reason of (b). [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #6(a): "if $x$ is absolutely summable, this transform is easily computed from the z-transform" describes the DTFT. Problem 5 below and [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2(c) are the system version of (b).

## Problem 5 — the accumulator's frequency response

> [!question] Problem 5
> A causal LSI system is described by the difference equation $y[n] - y[n-1] = x[n]$.
>
> (a) Determine the system's transfer function $H(z)$.
>
> (b) Determine the system's unit pulse response $h[n]$.
>
> (c) Determine the system's frequency response $H_d(\omega)$; is $H_d(\omega) = H(z)\big|_{z=e^{j\omega}}$? If not, explain why.

**What it practises:** LCCDE → $H(z)$ → $h[n]$ ([[2-z-transform/09-transfer-functions|Lecture 9]]), a pole on the unit circle ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]), and the frequency response as the DTFT of $h[n]$ ([[3-fourier-analysis/15-frequency-response|Lecture 15]]). Concepts: [[concepts/frequency-response|frequency response]], [[concepts/transfer-function|transfer function]], [[concepts/marginal-stability|marginal stability]].

> [!tip]- Hint
> The impulse response is a sequence you know by name. For (c), is the unit circle inside the ROC? Lecture 14's table has the DTFT of that sequence.

> [!success]- Solution (a)
> Taking z-transforms, $Y(z) - z^{-1}Y(z) = X(z)$.
>
> **Answer.** $H(z) = \dfrac{1}{1-z^{-1}}$, ROC $\lvert z\rvert \gt 1$ (causal: outside the pole at $z = 1$).

> [!success]- Solution (b)
> **Answer.** $h[n] = u[n]$. The system is the accumulator, $y[n] = \sum_{k=-\infty}^{n}x[k]$. (`lfilter([1], [1, -1], δ)` returns all ones, checked.)

> [!success]- Solution (c) — the DTFT of u[n] needs an impulse
> $H_d(\omega)$ is the DTFT of $h[n] = u[n]$, which Lecture 14 tabulates (on $[-\pi,\pi]$: $\frac{1}{1-e^{-j\omega}} + \pi\delta(\omega)$):
> $$
> H_d(\omega) = \frac{1}{1-e^{-j\omega}} + \pi\sum_{k=-\infty}^{\infty}\delta(\omega-2\pi k).
> $$
> **Is $H_d(\omega) = H(z)\big|_{z=e^{j\omega}}$? No.** The ROC $\lvert z\rvert \gt 1$ does not contain the unit circle (the pole $z = 1$ is on it), so the system is not BIBO stable (it is marginally stable), $\sum_n\lvert h[n]\rvert = \infty$, and the DTFT sum does not converge in the ordinary sense. Substituting $z = e^{j\omega}$ gives only $\frac{1}{1-e^{-j\omega}}$, which is undefined at $\omega = 0$ and misses the impulse $\pi\delta(\omega)$ that carries the DC content of $u[n]$. Away from $\omega = 0$ (mod $2\pi$) the two expressions agree.
>
> **Checks.** $\frac{1}{1-e^{-j\omega}} = \tfrac12 - \tfrac{j}{2}\cot\tfrac{\omega}{2}$, whose magnitude $\frac{1}{2\lvert\sin(\omega/2)\rvert}$ blows up at $\omega = 0$. The principal-value inverse DTFT of the pair returns $u[n]$ for $n = -4,\dots,5$, and the averaged partial sums of $\sum_{n\ge0}e^{-j\omega n}$ converge to $\frac{1}{1-e^{-j\omega}}$ at $\omega = 0.5,\ 2,\ -1$ (checked).

> [!trap] Two incomplete answers
> - "$H_d(\omega) = \dfrac{1}{1-e^{-j\omega}}$": that is $H(e^{j\omega})$, the expression the question asks you to compare with, and it misses the impulse.
> - "Not equal, because the system is causal": causality is not the reason. The reason is the ROC: it does not contain $\lvert z\rvert = 1$. A causal system with all poles inside the unit circle has $H_d(\omega) = H(e^{j\omega})$.

**On the exam:** [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2 is this problem with $y[n] = y[n-2] + x[n] - x[n-1]$: $H(z) = \frac{1-z^{-1}}{1-z^{-2}} = \frac{1}{1+z^{-1}}$ after cancelling, $h[n] = (-1)^n u[n] = e^{j\pi n}u[n]$, and $H_d(\omega) = \frac{1}{1-e^{-j(\omega-\pi)}} + \pi\sum_k\delta(\omega-\pi-2\pi k)$: the impulse sits at the angle of the pole, $\pi$.

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

**What it practises:** the frequency response of an FIR system, magnitude and phase with $\pm\pi$ jumps and principal values ([[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]), and the sinusoidal response of a real LTI system ([[3-fourier-analysis/15-frequency-response|Lecture 15]]). Concepts: [[concepts/magnitude-and-phase-response|magnitude and phase response]], [[concepts/group-delay|group delay]], [[concepts/frequency-response|frequency response]]; families: [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]], [[problems/lti-response-to-sinusoids|LTI response to sinusoids]].

> [!recipe] Two taps: factor out half the delay
> $1 + e^{-jN\omega} = e^{-jN\omega/2}\left(e^{jN\omega/2} + e^{-jN\omega/2}\right) = 2\cos\!\left(\tfrac{N\omega}{2}\right)e^{-jN\omega/2}$. Then $\lvert H_d\rvert = 2\lvert\cos\frac{N\omega}{2}\rvert$ and $\angle H_d = -\frac{N}{2}\omega + \angle\cos\frac{N\omega}{2}$, where the last term is $0$ or $\pm\pi$ by the sign of the cosine; wrap the result into $[-\pi,\pi]$.

> [!tip]- Hint
> Use the recipe with $N = 10$. For (b), $h[n]$ is real, so each sinusoid leaves as $\lvert H_d(\omega_0)\rvert A\cos\!\big(\omega_0 n + \theta + \angle H_d(\omega_0)\big)$ (same for sine): evaluate $H_d$ at $\tfrac{\pi}{10}$, $\tfrac{\pi}{3}$, $0$ and $\tfrac{2\pi}{5}$.

> [!success]- Solution (a) — magnitude and phase
> $h[n] = \delta[n] + \delta[n-10]$, so
> $$
> H_d(\omega) = 1 + e^{-j10\omega} = 2\cos(5\omega)\,e^{-j5\omega}, \qquad \lvert H_d(\omega)\rvert = 2\lvert\cos 5\omega\rvert, \qquad \angle H_d(\omega) = -5\omega + \angle\cos(5\omega).
> $$
> **Magnitude:** peaks of $2$ at $\omega = \tfrac{k\pi}{5}$ ($0$, $\pm\tfrac{\pi}{5}$, $\pm\tfrac{2\pi}{5}$, $\pm\tfrac{3\pi}{5}$, $\pm\tfrac{4\pi}{5}$, $\pm\pi$) and notches (zeros) at $\omega = \tfrac{\pi}{10} + \tfrac{k\pi}{5}$ ($\pm\tfrac{\pi}{10}$, $\pm\tfrac{3\pi}{10}$, $\pm\tfrac{\pi}{2}$, $\pm\tfrac{7\pi}{10}$, $\pm\tfrac{9\pi}{10}$), ten in one period: a comb.
>
> **Phase:** since $\mathrm{Re}\,H_d = 1 + \cos 10\omega \ge 0$, the phase never leaves $[-\tfrac{\pi}{2}, \tfrac{\pi}{2}]$. On each lobe it falls with slope $-5$ from $\tfrac{\pi}{2}$ to $-\tfrac{\pi}{2}$, and it jumps by $+\pi$ at every notch, where $\cos 5\omega$ changes sign (at the notches themselves the phase is undefined). The group delay $-\frac{d\angle H_d}{d\omega} = 5$ samples away from the notches: every frequency that gets through is delayed by 5, the average of the two taps' delays $0$ and $10$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 268" width="640" height="268" role="img" aria-label="Magnitude 2|cos 5w| and sawtooth phase of 1 + e^{-j10w} on [-pi, pi]" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="174.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| = 2|cos 5ω|</text><line x1="40.0" y1="139.1" x2="308.0" y2="139.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="58.3" x2="308.0" y2="58.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="220.0" x2="308.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="174.0" y1="30.0" x2="174.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="40.0" y1="217.0" x2="40.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="40.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="107.0" y1="217.0" x2="107.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="107.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="174.0" y1="217.0" x2="174.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="174.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="241.0" y1="217.0" x2="241.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="241.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="308.0" y1="217.0" x2="308.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="308.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="171.0" y1="139.1" x2="177.0" y2="139.1" stroke="currentColor" stroke-width="1"/><text x="36.0" y="143.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="171.0" y1="58.3" x2="177.0" y2="58.3" stroke="currentColor" stroke-width="1"/><text x="36.0" y="62.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><text x="308.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="40.0,58.3 41.2,59.8 42.7,66.2 44.4,78.9 45.9,95.0 48.9,138.2 53.4,220.0 57.9,138.2 60.9,95.0 63.6,69.4 65.1,61.4 66.6,58.3 67.5,58.8 68.0,59.8 69.5,66.2 71.2,78.9 72.7,95.0 75.7,138.2 80.2,220.0 84.7,138.2 87.7,95.0 90.2,70.6 91.9,61.4 93.4,58.3 94.3,58.8 94.8,59.8 96.3,66.2 98.0,78.9 99.5,95.0 103.7,158.1 107.0,220.0 111.5,138.2 114.5,95.0 117.2,69.4 118.7,61.4 120.2,58.3 121.1,58.8 121.6,59.8 123.1,66.2 124.8,78.9 126.3,95.0 129.3,138.2 133.8,220.0 137.1,158.1 141.3,95.0 144.0,69.4 145.5,61.4 147.0,58.3 147.9,58.8 148.4,59.8 149.9,66.2 151.6,78.9 153.1,95.0 156.1,138.2 160.6,220.0 164.6,146.6 167.6,101.3 170.1,74.5 171.8,63.5 173.3,58.8 173.8,58.3 174.7,58.8 176.2,63.5 177.9,74.5 179.4,89.2 182.9,138.2 187.4,220.0 191.4,146.6 194.4,101.3 196.9,74.5 198.6,63.5 200.1,58.8 200.6,58.3 201.5,58.8 203.0,63.5 204.7,74.5 206.2,89.2 209.7,138.2 214.2,220.0 218.2,146.6 221.2,101.3 223.7,74.5 224.9,66.2 226.4,59.8 227.4,58.3 228.3,58.8 229.8,63.5 231.5,74.5 233.0,89.2 236.5,138.2 241.0,220.0 245.5,138.2 249.5,83.8 251.7,66.2 253.2,59.8 254.2,58.3 255.1,58.8 256.1,61.4 257.8,70.6 258.8,78.9 261.3,107.9 264.5,158.1 267.8,220.0 272.3,138.2 275.8,89.2 277.3,74.5 279.0,63.5 280.5,58.8 281.0,58.3 281.9,58.8 283.4,63.5 284.6,70.6 287.6,101.3 290.6,146.6 294.6,220.0 297.9,158.1 302.1,95.0 303.6,78.9 305.3,66.2 306.8,59.8 308.0,58.3" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="174.0" cy="58.3" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="187.4" cy="220.0" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="218.7" cy="139.1" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="227.6" cy="58.3" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="205.4" y="214.0" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/10</text><text x="235.7" y="143.1" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/3</text><text x="239.6" y="52.3" text-anchor="middle" fill="var(--hi)" style="font-size:10px">2π/5</text><text x="490.0" y="18.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠H<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="360.0" y1="220.0" x2="620.0" y2="220.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="172.5" x2="620.0" y2="172.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="77.5" x2="620.0" y2="77.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="30.0" x2="620.0" y2="30.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="360.0" y1="125.0" x2="620.0" y2="125.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="490.0" y1="30.0" x2="490.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="360.0" y1="122.0" x2="360.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="360.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="425.0" y1="122.0" x2="425.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="425.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="490.0" y1="122.0" x2="490.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="490.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="555.0" y1="122.0" x2="555.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="555.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="620.0" y1="122.0" x2="620.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="620.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="487.0" y1="220.0" x2="493.0" y2="220.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="224.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π</text><line x1="487.0" y1="172.5" x2="493.0" y2="172.5" stroke="currentColor" stroke-width="1"/><text x="356.0" y="176.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="487.0" y1="125.0" x2="493.0" y2="125.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="487.0" y1="77.5" x2="493.0" y2="77.5" stroke="currentColor" stroke-width="1"/><text x="356.0" y="81.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="487.0" y1="30.0" x2="493.0" y2="30.0" stroke="currentColor" stroke-width="1"/><text x="356.0" y="34.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π</text><text x="620.0" y="119.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="360.0,125.0 372.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="373.2,78.1 398.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="399.2,78.1 424.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="425.2,78.1 450.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="451.2,78.1 476.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="477.2,78.1 502.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="503.2,78.1 528.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="529.2,78.1 554.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="555.2,78.1 580.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="581.2,78.1 606.8,171.9" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="607.2,78.1 620.0,125.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="533.3" cy="93.3" r="3.6" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="547.3" y="89.3" text-anchor="middle" fill="var(--hi)" style="font-size:10px">π/3</text></svg><figcaption><strong>HW6 #6(a): y[n] = x[n] + x[n − 10] is a comb filter.</strong> Ten notches at ω = π/10 + kπ/5 and peaks of 2 at ω = kπ/5. The phase is −5ω folded into [−π/2, π/2]: slope −5 (a delay of 5 samples), with a jump of +π at every notch, where cos 5ω changes sign. Red dots: the input frequencies of part (b) — π/10 is blocked, π/3 passes with gain 1 and phase π/3, 0 and 2π/5 pass with gain 2.</figcaption></figure>

> [!success]- Solution (b) — evaluate H at each input frequency
> **i.** $H_d\!\left(\tfrac{\pi}{10}\right) = 2\cos\tfrac{\pi}{2}\,e^{-j\pi/2} = 0$: the cosine is blocked. $H_d\!\left(\tfrac{\pi}{3}\right) = 2\cos\tfrac{5\pi}{3}\,e^{-j5\pi/3} = 2\cdot\tfrac12\cdot e^{-j5\pi/3} = e^{j\pi/3}$: gain $1$, phase $\tfrac{\pi}{3}$ (the principal value of $-\tfrac{5\pi}{3}$). So
> $$
> y[n] = 0 + 3\sin\!\left(\tfrac{\pi}{3}n + \tfrac{\pi}{10} + \tfrac{\pi}{3}\right) = 3\sin\!\left(\tfrac{\pi}{3}n + \tfrac{13\pi}{30}\right).
> $$
> **ii.** $H_d(0) = 2$ and $H_d\!\left(\tfrac{2\pi}{5}\right) = 2\cos 2\pi\,e^{-j2\pi} = 2$, so
> $$
> y[n] = 20 + 10\cos\!\left(\tfrac{2\pi}{5}n + \tfrac{\pi}{2}\right) = 20 - 10\sin\!\left(\tfrac{2\pi}{5}n\right).
> $$
> **Answers.** i. $y[n] = 3\sin\!\left(\tfrac{\pi}{3}n + \tfrac{13\pi}{30}\right)$; ii. $y[n] = 20 + 10\cos\!\left(\tfrac{2\pi}{5}n + \tfrac{\pi}{2}\right)$.
>
> **Checks in the time domain.** i. $\cos\!\left(\tfrac{\pi}{10}(n-10)\right) = \cos\!\left(\tfrac{\pi}{10}n - \pi\right) = -\cos\!\left(\tfrac{\pi}{10}n\right)$ cancels the first term; with $\theta = \tfrac{\pi}{3}n + \tfrac{\pi}{10}$, the delayed sine is $\sin\!\left(\theta - \tfrac{10\pi}{3}\right) = \sin\!\left(\theta + \tfrac{2\pi}{3}\right)$ and $\sin\theta + \sin\!\left(\theta + \tfrac{2\pi}{3}\right) = 2\sin\!\left(\theta + \tfrac{\pi}{3}\right)\cos\tfrac{\pi}{3} = \sin\!\left(\theta + \tfrac{\pi}{3}\right)$ ✓. ii. $x$ has period $5$, which divides $10$, so $x[n-10] = x[n]$ and $y = 2x$ ✓. `lfilter` from rest agrees with i. for every $n \ge 10$ (checked).

> [!trap] Three comb-filter slips
> - **A negative "magnitude".** $2\cos 5\omega$ is negative on half the lobes; the magnitude is $2\lvert\cos 5\omega\rvert$ and the sign goes into the phase as $\pm\pi$.
> - **An unwrapped phase.** $-\tfrac{5\pi}{3}$ and $\tfrac{\pi}{3}$ give the same output, but the phase response is plotted as a principal value in $[-\pi,\pi]$ (Lecture 16), so the plot shows $\tfrac{\pi}{3}$.
> - **Keeping a blocked term.** $\tfrac{\pi}{10}$ is exactly a notch: the output contains no cosine at all.

**On the exam:** [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #5 is this filter with a 6-sample delay ($h[n] = \delta[n] + \delta[n-6]$, $H_d = 2e^{-j3\omega}\cos 3\omega$: plot magnitude and phase). [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #3 adds a middle tap: $x[n] + 2x[n-3] + x[n-6]$ gives $e^{-j3\omega}(2 + 2\cos 3\omega)$, whose amplitude is never negative, so its phase is exactly $-3\omega$ with no jumps. [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3 centres the taps, $\delta[n+2] + \delta[n] + \delta[n-2] \to 1 + 2\cos 2\omega$, a real frequency response with no linear phase at all.

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

**What it practises:** complex exponentials are eigenfunctions, $e^{j\omega_0 n} \to H_d(\omega_0)e^{j\omega_0 n}$, and the cosine formula $\lvert H_d\rvert A\cos(\omega_0 n + \theta + \angle H_d)$ holds **only for a real $h[n]$** ([[3-fourier-analysis/15-frequency-response|Lecture 15]]); Hermitian symmetry is the test ([[3-fourier-analysis/14-dtft-properties|Lecture 14]]). Concepts: [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]], [[concepts/frequency-response|frequency response]]; family: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]].

> [!key] First question, always: is h[n] real?
> $h[n]$ is real exactly when $H_d^*(\omega) = H_d(-\omega)$ for all $\omega$. If so, each sinusoid goes through with the cosine formula. If not, split every sinusoid into its two complex exponentials and send each through $H_d$ separately.

> [!tip]- Hint
> Compare $H_d^*(\omega)$ with $H_d(-\omega)$. Then list the input frequencies: $0$, $\pm\tfrac{\pi}{4}$ and $\tfrac{\pi}{2}$ (because $j^n = e^{j\pi n/2}$). Careful with units: $45^\circ = \tfrac{\pi}{4}$ rad, while the $\sin\omega$ in the exponent of $H_d$ is already a phase in radians ($\sin\tfrac{\pi}{4} = \tfrac{\sqrt2}{2} \approx 0.707$ rad).

> [!success]- Solution — is h real? Which gains are needed?
> $H_d^*(\omega) = \omega\,e^{-j\sin\omega}$, while $H_d(-\omega) = (-\omega)\,e^{j\sin(-\omega)} = -\omega\,e^{-j\sin\omega} = -H_d^*(\omega)$. Not Hermitian, so **$h[n]$ is not real-valued** and the cosine shortcut is off limits. (In fact $H_d^*(\omega) = -H_d(-\omega)$ means $h[n]$ is purely imaginary; numerically $h[0] \approx 0.893j$, $h[1] \approx 0.453j$.)
>
> The gains at the input frequencies:
> $$
> H_d(0) = 0,\qquad H_d\!\left(\tfrac{\pi}{4}\right) = \tfrac{\pi}{4}\,e^{j\frac{\sqrt2}{2}},\qquad H_d\!\left(-\tfrac{\pi}{4}\right) = -\tfrac{\pi}{4}\,e^{-j\frac{\sqrt2}{2}},\qquad H_d\!\left(\tfrac{\pi}{2}\right) = \tfrac{\pi}{2}\,e^{j} .
> $$

> [!success]- Solution (a) — three eigenfunctions
> Each term is a complex exponential, so it is simply multiplied by $H_d$ at its frequency:
> $$
> \begin{aligned}
> y[n] &= 3H_d(0) - 10H_d\!\left(\tfrac{\pi}{4}\right)e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} + H_d\!\left(\tfrac{\pi}{2}\right)e^{j\frac{\pi}{2}n}
> = 0 - \frac{10\pi}{4}\,e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)} + \frac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)} .
> \end{aligned}
> $$
> **Answer.** $y[n] = -\dfrac{5\pi}{2}\,e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)} + \dfrac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)}$, equivalently $\dfrac{5\pi}{2}\,e^{j\left(\frac{\pi}{4}n-\frac{3\pi}{4}+\frac{\sqrt2}{2}\right)} + \dfrac{\pi}{2}\,j^n e^{j}$.

> [!success]- Solution (b) — split the cosine first
> $10\cos\!\left(\tfrac{\pi}{4}n+\tfrac{\pi}{4}\right) = 5e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} + 5e^{-j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)}$, and the two halves see different gains:
> $$
> \begin{aligned}
> y[n] &= 3H_d(0) + 5H_d\!\left(\tfrac{\pi}{4}\right)e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} + 5H_d\!\left(-\tfrac{\pi}{4}\right)e^{-j\left(\frac{\pi}{4}n+\frac{\pi}{4}\right)} - H_d\!\left(\tfrac{\pi}{2}\right)e^{j\frac{\pi}{2}n}\\
> &= \frac{5\pi}{4}\left[e^{j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)} - e^{-j\left(\frac{\pi}{4}n+\frac{\pi}{4}+\frac{\sqrt2}{2}\right)}\right] - \frac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)}
> = j\,\frac{5\pi}{2}\sin\!\left(\tfrac{\pi}{4}n+\tfrac{\pi}{4}+\tfrac{\sqrt2}{2}\right) - \frac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)} .
> \end{aligned}
> $$
> **Answer.** $y[n] = j\,\dfrac{5\pi}{2}\sin\!\left(\tfrac{\pi}{4}n+\tfrac{\pi}{4}+\tfrac{\sqrt2}{2}\right) - \dfrac{\pi}{2}\,e^{j\left(\frac{\pi}{2}n+1\right)}$.
>
> **Checks.** A purely imaginary $h$ maps a real input to a purely imaginary output: the constant goes to $0$ and the cosine to $j\frac{5\pi}{2}\sin(\cdot)$, both imaginary ✓; only the complex input $j^n$ gives a complex output. The real-system formula would have predicted $\frac{5\pi}{2}\cos\!\left(\tfrac{\pi}{4}n+\tfrac{\pi}{4}+\tfrac{\sqrt2}{2}\right)$: real, and wrong. Numerically, $h[n]$ from the inverse DTFT on a $2^{21}$-point grid, truncated to $\lvert n\rvert \le 60000$ and convolved with both inputs, reproduces both answers at $n = 0, 1, 5, -3$ to $10^{-4}$ (checked).

> [!trap] Where Problem 7 goes wrong
> - **The cosine shortcut on a complex system.** It assumes $H_d(-\omega_0) = H_d^*(\omega_0)$; here $H_d(-\tfrac{\pi}{4}) = -H_d^*(\tfrac{\pi}{4})$, and the output of the cosine becomes an imaginary sine.
> - **Degrees and radians in one expression.** $45^\circ = \tfrac{\pi}{4}$, but $\sin\tfrac{\pi}{4} = 0.707$ is added to the phase as $0.707$ rad (about $40.5^\circ$), not as $0.707^\circ$.
> - **The sign of $\omega$.** At $\omega = -\tfrac{\pi}{4}$ the factor $\omega$ is negative: $\lvert H_d\rvert = \tfrac{\pi}{4}$ and the phase is $-\tfrac{\sqrt2}{2} \pm \pi$, not $-\tfrac{\sqrt2}{2}$.
> - **DC.** $H_d(0) = 0$ removes the constant $3$ from both outputs.

**On the exam:** this format is on almost every Midterm 2, and the first step is always the Hermitian test. [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #6: $H_d = \omega e^{j\pi\cos\omega}$, not real, so $\sin\!\left(\tfrac{\pi}{2}n+\tfrac{\pi}{4}\right)$ is split into exponentials. [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #4: $\lvert\omega\rvert e^{-j\pi\sin\omega}$, real by Hermitian symmetry, so the shortcut is allowed. [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #4: $j\omega e^{j\pi\sin\omega}$, where the extra $j$ makes $h$ real. [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #4: $\left(\tfrac12+\cos\omega\right)e^{j\lvert\omega\rvert}$, not real, split the sine.

## Checking it in Python

The comb filter's gains at the four input frequencies (`freqz`), its output for input i. (`lfilter`, exact once the 10-sample memory has filled), and the 3.5-sample delay of 3(b) by numerical integration of the synthesis equation.

```python
import numpy as np
from scipy import integrate, signal

# HW6 #6: the comb y[n] = x[n] + x[n-10]
b = np.zeros(11); b[0] = b[10] = 1
w0 = np.array([0, np.pi / 10, np.pi / 3, 2 * np.pi / 5])
_, H = signal.freqz(b, [1], worN=w0)
print("|H| :", np.round(abs(H), 4))
ph = np.where(abs(H) > 1e-9, np.angle(H) / np.pi, np.nan)   # no phase where |H| = 0
print("<H/pi:", np.round(ph, 4))

n = np.arange(40)
x = np.cos(np.pi * n / 10) + 3 * np.sin(np.pi * n / 3 + np.pi / 10)
y = signal.lfilter(b, [1], x)                      # from rest: exact once n >= 10
print(np.allclose(y[10:], 3 * np.sin(np.pi * n[10:] / 3 + 13 * np.pi / 30)))

# HW6 #3(b): inverse DTFT of e^{-j3.5w} over [-pi, pi], by numerical integration
for k in [0, 2, 3, 4, 5]:
    re = integrate.quad(lambda om: np.cos(om * (k - 3.5)), -np.pi, np.pi)[0] / (2 * np.pi)
    print(k, round(re, 4), round((-1) ** k / (np.pi * (k - 3.5)), 4))
```

```text
|H| : [2. 0. 1. 2.]
<H/pi: [0.        nan 0.3333 0.    ]
True
0 -0.0909 -0.0909
2 -0.2122 -0.2122
3 0.6366 0.6366
4 0.6366 0.6366
5 -0.2122 -0.2122
```

## Related

[[concepts/fourier-series|Fourier series and the CTFT]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/frequency-response|frequency response]] · [[concepts/magnitude-and-phase-response|magnitude and phase response]] · [[concepts/group-delay|group delay]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[concepts/region-of-convergence|ROC]] · [[concepts/marginal-stability|marginal stability]] · [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] · [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]] · [[demos/frequency-response-explorer|frequency response explorer]] · prev: [[homework/hw5|HW5]]

### Sources for this page

- ECE 310 Fall 2026 Homework 6 (due Fri Oct 9, 11:59 pm). No official solutions were available when this page was written: every solution here is this site's own.
- Lecture 13 notes (the CTFT, Eqs. 26–27, and the DTFT synthesis equation), Lecture 14 notes (Dirac delta and sifting, the pairs for $e^{j\omega_0 n}$ and $u[n]$, the property table: conjugation, time reversal, frequency shift, Hermitian symmetry), Lecture 15 notes (frequency response, eigenfunctions, the sinusoidal response of real systems) and Lecture 16 notes (magnitude, principal-value phase, group delay). Lecture 12 for the matched filter.
- Past Midterm 2 exams cited in the "On the exam" lines (FA2019, SP2021, FA2021, SP2023, FA2023, FA2024, SP2025 keys).
- Every answer was verified numerically (`verify/HW_hw6.py`): CTFTs by `scipy.integrate.quad` (a narrow Gaussian for the delta, long time averages for the impulse weights), the conjugation identities on a random complex sequence, inverse DTFTs by numerical integration (principal values for the $u[n]$-type pairs), `lfilter`/`freqz` for Problems 5 and 6, and Problem 7 by convolving the inputs with $h[n]$ obtained from a numerical inverse DTFT.
