---
title: "HW5 · The DTFT from the definition, and four numbers you can read without it"
description: "Worked solutions to ECE 310 Homework 5 (Fall 2026): DTFTs from the definition of two opposite impulses, a four-sample pulse (all four accepted forms), a phase-shifted cosine (two impulses with complex weights, repeated every 2π) and a modulated decaying exponential (geometric series plus frequency shift), then X_d(0), X_d(π), the area under X_d and the energy integral of a plotted signal from the definition, the inverse DTFT at n = 0 and Parseval's relation, with the rubric, the traps and the Midterm 2 problems that reuse each idea."
tags: [homework, midterm-2, dtft]
---

*Homework 5 · due Sun Oct 4, 2026 (Gradescope; the PDF header prints "2025", a typo) · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (the DTFT) and [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (DTFT pairs and properties) · 100 points (60 + 40) · official solutions v1.0 · prev: [[homework/hw4|HW4]] · next: [[homework/hw6|HW6]] · [[homework/index|all homework]]*

> [!abstract] What HW5 trains
> Two skills every Midterm 2 uses. **Computing a DTFT from the definition** (#1): each sample $x[k]$ contributes $x[k]e^{-j\omega k}$; samples placed symmetrically about a centre combine into cosines or sines once you factor out the centre's linear phase; a sinusoid becomes impulses at $\pm\omega_0$ (and every $2\pi$ after that); multiplying by $e^{j\omega_0 n}$ slides the whole spectrum by $\omega_0$. **Reading a spectrum without computing it** (#2): $X_d(0)$, $X_d(\pi)$, $\int X_d\,d\omega$ and $\int\lvert X_d\rvert^2 d\omega$ are a sum, an alternating sum, $2\pi x[0]$ and $2\pi$ times the energy: four numbers in four lines.

| # | skill | concept · lecture |
|---|---|---|
| 1(a) | two impulses → Euler → $2j\sin 2\omega$ | [[concepts/dtft\|DTFT]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] |
| 1(b) | a finite pulse: factor out the linear phase, or sum the geometric series | [[concepts/dtft\|DTFT]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]] (Exercise 2) |
| 1(c) | a cosine with a phase → two impulses with complex weights, $2\pi$-periodic | [[concepts/dtft-pairs\|DTFT pairs]] · [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 1(d) | geometric series, then frequency shift (or the windowing property) | [[concepts/dtft-properties\|DTFT properties]] · [[3-fourier-analysis/14-dtft-properties\|L14]] |
| 2 | $X_d(0)$, $X_d(\pi)$, inverse DTFT at $n=0$, Parseval | [[concepts/dtft-properties\|DTFT properties]] · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|L13]], [[3-fourier-analysis/14-dtft-properties\|L14]] |

> [!tip] What the rubric rewarded (the exam grades the same way)
> - **#1 (15 per part): the work is the answer.** A correct result without work, or one read off a DTFT table pair the problem did not give you, earned 6/15. With the right approach, each minor math slip cost 3 points. Every form the key marks (∗) is accepted; they are listed under each solution below.
> - **#2 (10 per part): the closed form is off limits.** A correct number obtained by first finding $X_d(\omega)$ earned 4/10. The problem tests whether you know the four shortcuts.

Every solution below is folded: read the statement, solve it on paper, then open the solution.

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

**What it practises:** the analysis equation $X_d(\omega) = \sum_n x[n]e^{-j\omega n}$ of [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] on finite sequences (a, b); the impulse pair and linearity for a periodic signal (c); and a property of [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (frequency shift, or windowing) on top of a geometric series (d). Concepts: [[concepts/dtft|DTFT]], [[concepts/dtft-pairs|DTFT pairs]], [[concepts/dtft-properties|DTFT properties]], [[0-toolkit/02-geometric-series|geometric series]].

> [!key] The DTFT of a finite sequence, by hand
> 1. Find $n=0$ (the arrow) and write $x[n] = \sum_k x[k]\,\delta[n-k]$.
> 2. Each $\delta[n-k]$ contributes $e^{-j\omega k}$, so $X_d(\omega) = \sum_k x[k]\,e^{-j\omega k}$. **That sum is already a correct answer.**
> 3. For a real amplitude times a linear phase, factor out $e^{-j\omega c}$, where $c$ is the centre of the support, and pair the terms: $e^{j\theta}+e^{-j\theta} = 2\cos\theta$, $e^{j\theta}-e^{-j\theta} = 2j\sin\theta$.
> 4. Check two values for free: $X_d(0) = \sum_n x[n]$ and $X_d(\pi) = \sum_n (-1)^n x[n]$.

> [!tip]- Hints (open one part at a time)
> - (a) Only two samples are nonzero. Which indices do they sit at?
> - (b) Four terms of a geometric series with ratio $e^{-j\omega}$. The centre of $n = 0,\dots,3$ is $n = \tfrac32$.
> - (c) Write the cosine as two complex exponentials. The phase $\tfrac{\pi}{4}$ becomes a constant complex factor in front of each.
> - (d) First find the DTFT of $\alpha^n u[n]$ from the definition (an infinite geometric series), then decide what multiplying by $e^{j\omega_0 n}$ does to a spectrum.

> [!success]- Solution (a) — two impulses, one Euler identity
> The arrow sits under the middle $0$, so the $1$ is at $n=-2$ and the $-1$ at $n=2$: $x[n] = \delta[n+2] - \delta[n-2]$. Then
> $$
> X_d(\omega) = \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n} = e^{-j\omega(-2)} - e^{-j\omega(2)} = e^{j2\omega} - e^{-j2\omega} = 2j\sin(2\omega).
> $$
> **Answer.** $X_d(\omega) = 2j\sin(2\omega)$. The key also accepts the unsimplified $e^{j2\omega} - e^{-j2\omega}$ (∗).
>
> **Checks.** $X_d(0) = 1 - 1 = 0 = 2j\sin 0$ ✓. The signal is real and odd ($x[-n] = -x[n]$), so its DTFT must be purely imaginary and odd ✓.

> [!success]- Solution (b) — a four-sample pulse, four accepted forms
> $u[n]-u[n-4]$ is $1$ for $n = 0, 1, 2, 3$ and $0$ otherwise (four samples): $x[n] = \delta[n]+\delta[n-1]+\delta[n-2]+\delta[n-3]$, so
> $$
> X_d(\omega) = 1 + e^{-j\omega} + e^{-j2\omega} + e^{-j3\omega}. \qquad (\ast)
> $$
> **Real amplitude × linear phase.** The support is centred at $n = \tfrac32$. Pair the outer and the inner terms and factor out $e^{-j\frac32\omega}$:
> $$
> \begin{aligned}
> X_d(\omega) &= \left(1 + e^{-j3\omega}\right) + \left(e^{-j\omega} + e^{-j2\omega}\right)
> = e^{-j\frac32\omega}\left(e^{j\frac32\omega} + e^{-j\frac32\omega}\right) + e^{-j\frac32\omega}\left(e^{j\frac12\omega} + e^{-j\frac12\omega}\right) \qquad (\ast)\\
> &= 2e^{-j\frac32\omega}\left(\cos\tfrac{\omega}{2} + \cos\tfrac{3\omega}{2}\right).
> \end{aligned}
> $$
> **Geometric series** (the route of [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], Exercise 2, with $L=4$):
> $$
> X_d(\omega) = \sum_{n=0}^{3}\left(e^{-j\omega}\right)^n = \frac{1-e^{-j4\omega}}{1-e^{-j\omega}}
> = \frac{e^{-j2\omega}\left(e^{j2\omega}-e^{-j2\omega}\right)}{e^{-j\frac12\omega}\left(e^{j\frac12\omega}-e^{-j\frac12\omega}\right)}
> = e^{-j\frac32\omega}\,\frac{\sin(2\omega)}{\sin(\omega/2)} \qquad (\ast)
> $$
> (the ratio forms need $\omega \neq 0$; their limit there is $4$).
>
> **Answer.** $X_d(\omega) = 2e^{-j\frac32\omega}\left(\cos\tfrac{\omega}{2} + \cos\tfrac{3\omega}{2}\right)$, or any of the (∗) forms.
>
> **Checks.** $X_d(0) = 2(1+1) = 4 = \sum_n x[n]$ ✓. $X_d(\pi) = 1-1+1-1 = 0$, and the cosine form gives $2e^{-j\frac32\pi}\left(\cos\tfrac{\pi}{2}+\cos\tfrac{3\pi}{2}\right) = 0$ ✓. The magnitude is zero at $\omega = \pm\tfrac{\pi}{2}$ and $\pi$ (where $\sin 2\omega = 0$ but $\sin\tfrac{\omega}{2} \neq 0$). The linear phase $-\tfrac32\omega$ says the pulse is centred $1.5$ samples to the right of $n=0$. All four forms agree on a 2001-point grid (Python at the end of the page).

> [!success]- Solution (c) — two impulses with complex weights
> Euler's identity splits the cosine into two complex exponentials; the phase becomes a constant factor:
> $$
> \cos\!\left(\tfrac{\pi}{3}n + \tfrac{\pi}{4}\right) = \tfrac12 e^{j\left(\frac{\pi}{3}n+\frac{\pi}{4}\right)} + \tfrac12 e^{-j\left(\frac{\pi}{3}n+\frac{\pi}{4}\right)}
> = \tfrac12 e^{j\frac{\pi}{4}}\,e^{j\frac{\pi}{3}n} + \tfrac12 e^{-j\frac{\pi}{4}}\,e^{-j\frac{\pi}{3}n}.
> $$
> The given pair with $\omega_0 = \pm\tfrac{\pi}{3}$, and linearity:
> $$
> X_d(\omega) = \tfrac12 e^{j\frac{\pi}{4}}\cdot 2\pi\delta\!\left(\omega-\tfrac{\pi}{3}\right) + \tfrac12 e^{-j\frac{\pi}{4}}\cdot 2\pi\delta\!\left(\omega+\tfrac{\pi}{3}\right) \qquad (\ast)
> $$
> $$
> X_d(\omega) = \pi e^{j\frac{\pi}{4}}\,\delta\!\left(\omega-\tfrac{\pi}{3}\right) + \pi e^{-j\frac{\pi}{4}}\,\delta\!\left(\omega+\tfrac{\pi}{3}\right),\qquad -\pi \le \omega \lt \pi,
> $$
> and the pattern repeats every $2\pi$. Written for all $\omega$ at once:
> $$
> X_d(\omega) = \pi\sum_{k=-\infty}^{\infty}\left[e^{j\frac{\pi}{4}}\,\delta\!\left(\omega-\tfrac{\pi}{3}-2\pi k\right) + e^{-j\frac{\pi}{4}}\,\delta\!\left(\omega+\tfrac{\pi}{3}-2\pi k\right)\right].
> $$
> **Answer.** $X_d(\omega) = \pi e^{j\frac{\pi}{4}}\,\delta\!\left(\omega-\tfrac{\pi}{3}\right) + \pi e^{-j\frac{\pi}{4}}\,\delta\!\left(\omega+\tfrac{\pi}{3}\right)$ on $[-\pi,\pi)$, repeated every $2\pi$ (the key's boxed answer); the (∗) form is accepted too.
>
> **Checks.** The inverse DTFT sifts each impulse: $\frac{1}{2\pi}\left(\pi e^{j\frac{\pi}{4}}e^{j\frac{\pi}{3}n} + \pi e^{-j\frac{\pi}{4}}e^{-j\frac{\pi}{3}n}\right) = \cos\!\left(\tfrac{\pi}{3}n+\tfrac{\pi}{4}\right)$ ✓. The two weights are complex conjugates, as Hermitian symmetry requires for a real signal ✓. Numerically, the average of $x[n]e^{-j\pi n/3}$ over 600,000 samples is $\tfrac12 e^{j\pi/4}$ to four decimals, and $2\pi$ times that average is the impulse weight $\pi e^{j\pi/4}$ (checked).

> [!success]- Solution (d) — a geometric series, then slide it by ω₀
> **The key's route.** Let $g[n] = e^{j\omega_0 n}$ and $h[n] = \alpha^n u[n]$, so $x[n] = g[n]h[n]$. The given pair: $G_d(\omega) = 2\pi\delta(\omega-\omega_0)$. From the definition,
> $$
> H_d(\omega) = \sum_{n=-\infty}^{\infty}\alpha^n u[n]e^{-j\omega n} = \sum_{n=0}^{\infty}\left(\alpha e^{-j\omega}\right)^n = \frac{1}{1-\alpha e^{-j\omega}},
> $$
> which converges because $\lvert\alpha e^{-j\omega}\rvert = \lvert\alpha\rvert \lt 1$ for every $\omega$. Multiplication in time is periodic convolution in frequency (windowing property):
> $$
> \begin{aligned}
> X_d(\omega) &= \frac{1}{2\pi}\int_{-\pi}^{\pi} G_d(\theta)\,H_d(\omega-\theta)\,d\theta
> = \frac{1}{2\pi}\int_{-\pi}^{\pi} 2\pi\delta(\theta-\omega_0)\,\frac{1}{1-\alpha e^{-j(\omega-\theta)}}\,d\theta\\
> &= \frac{1}{1-\alpha e^{-j(\omega-\omega_0)}} .
> \end{aligned}
> $$
> Take $\omega_0 \in [-\pi,\pi)$ so that exactly one impulse of the $2\pi$-periodic $G_d$ lies inside the integration interval; since $G_d$ and $H_d$ are both $2\pi$-periodic, the result holds for any real $\omega_0$.
>
> **Two faster routes to the same answer.** Sum the definition directly, $X_d(\omega) = \sum_{n\ge0}\left(\alpha e^{-j(\omega-\omega_0)}\right)^n$; or use the frequency-shift property $e^{j\omega_0 n}h[n] \leftrightarrow H_d(\omega-\omega_0)$. Both are allowed: only table *pairs* are off limits.
>
> **Answer.** $X_d(\omega) = \dfrac{1}{1-\alpha e^{-j(\omega-\omega_0)}}$.
>
> **Checks.** At $\omega = \omega_0$ the modulation is undone: $X_d(\omega_0) = \frac{1}{1-\alpha} = \sum_{n\ge0}\alpha^n$ ✓. For real $0\lt\alpha\lt1$ the magnitude peaks at $\omega=\omega_0$: the low-pass bump of $\alpha^n u[n]$, moved from $0$ to $\omega_0$. A 400-term truncated sum matches the closed form to $10^{-10}$ for $(\alpha,\omega_0) = (0.6,\,1.1)$, $(-0.8,\,-2.5)$ and the complex $\alpha = 0.5e^{j0.3}$, $\omega_0 = 0.7$ (checked).

> [!trap] Five ways to lose points on Problem 1
> - **(a) Where is $n=0$?** Reading $\{1,0,0,0,-1\}$ as starting at $n=0$ gives $1-e^{-j4\omega} = 2je^{-j2\omega}\sin 2\omega$: the right magnitude, but an extra linear phase $e^{-j2\omega}$, i.e. the same signal delayed by 2.
> - **(b) Four samples, not five.** $u[n]-u[n-4]$ stops at $n=3$.
> - **(c) The phase goes into the weight, not the location.** $\delta\!\left(\omega-\tfrac{\pi}{3}-\tfrac{\pi}{4}\right)$ is wrong. So is a weight of $\tfrac12$ instead of $\pi$ (the pair carries $2\pi$), and $e^{+j\pi/4}$ on the impulse at $-\tfrac{\pi}{3}$ (it is the conjugate).
> - **(d) Multiplying in time is not multiplying spectra.** $X_d \neq G_d(\omega)H_d(\omega)$; it is the periodic convolution with the factor $\tfrac{1}{2\pi}$ (or simply the frequency shift).
> - **Table pairs.** The rectangular-pulse and $a^n u[n]$ pairs of [[3-fourier-analysis/14-dtft-properties|Lecture 14]] give (b) and (d) in one line, but the problem forbids them: 6/15.

**On the exam:** [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #3 asks for the DTFT of $3\delta[n+1]-3\delta[n-7]$ in the form $Ae^{-jB\omega}\sin(C\omega)$: factor out the centre $e^{-j3\omega}$, exactly as in (a) and (b), to get $A = 6j$, $B = 3$, $C = 4$; #2 of the same exam sketches the magnitude and phase of $e^{-j4\omega}\sin(2\omega)$, the next step ([[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]). The impulse pairs of (c) return in every sinusoidal-input problem ([[problems/lti-response-to-sinusoids|LTI response to sinusoids]]). Practice family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].

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

**What it practises:** evaluating the analysis equation at the two special frequencies $\omega = 0$ and $\omega = \pi$, the synthesis equation $x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)e^{j\omega n}d\omega$ at $n=0$ ([[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]]), and Parseval's relation ([[3-fourier-analysis/14-dtft-properties|Lecture 14]]). Concepts: [[concepts/dtft|DTFT]], [[concepts/dtft-properties|DTFT properties]].

> [!key] Four numbers you can read straight off $x[n]$
> | quantity | where it comes from | value |
> |---|---|---|
> | $X_d(0)$ | definition at $\omega = 0$: every $e^{-j0n} = 1$ | $\sum_n x[n]$ |
> | $X_d(\pi)$ | definition at $\omega=\pi$: $e^{-j\pi n} = (-1)^n$ | $\sum_n (-1)^n x[n]$ |
> | $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$ | inverse DTFT at $n = 0$ | $2\pi\,x[0]$ |
> | $\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega$ | Parseval | $2\pi\sum_n\lvert x[n]\rvert^2$ |

> [!intuition] Why these four work
> At $\omega = 0$ the DTFT compares $x$ with the constant $1$ (its DC content); at $\omega = \pi$ with the fastest possible oscillation $+1,-1,+1,\dots$, so $X_d(\pi)$ is large when $x$ alternates in sign. The inverse DTFT at $n=0$ is $\frac{1}{2\pi}\int X_d\,d\omega$, the **average** of $X_d$ over one period: that average is the sample at the origin. Parseval says the DTFT keeps energy, up to the $2\pi$ of the frequency axis.

> [!tip]- Hint
> Do not look for $X_d(\omega)$. Read the samples off the plot ($x[n]$ is nonzero only for $-2\le n\le 2$), then use one row of the table above per part. Mind the signs of $(-1)^n$ at negative $n$.

> [!success]- Solution (a) — the sum of the samples
> From the figure, $x[n] = \{2,\ -1,\ \underset{\uparrow}{1},\ -1,\ 2\}$: $x[-2] = 2$, $x[-1] = -1$, $x[0] = 1$, $x[1] = -1$, $x[2] = 2$. Setting $\omega = 0$ in the definition,
> $$
> X_d(0) = \sum_{n=-\infty}^{\infty}x[n]e^{-j(0)n} = \sum_{n=-2}^{2}x[n] = 2 + (-1) + 1 + (-1) + 2 = 3 .
> $$
> **Answer.** $X_d(0) = 3$.

> [!success]- Solution (b) — the alternating sum
> With $e^{-j\pi n} = (-1)^n$, the odd-indexed samples flip sign and the even-indexed ones stay:
> $$
> X_d(\pi) = \sum_{n=-2}^{2}(-1)^n x[n] = x[-2] - x[-1] + x[0] - x[1] + x[2] = 2 - (-1) + 1 - (-1) + 2 = 7 .
> $$
> **Answer.** $X_d(\pi) = 7$.

> [!success]- Solution (c) — the inverse DTFT at n = 0
> $$
> x[0] = \frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)e^{j\omega\cdot 0}\,d\omega \quad\Longrightarrow\quad \int_{-\pi}^{\pi}X_d(\omega)\,d\omega = 2\pi\,x[0] = 2\pi(1).
> $$
> **Answer.** $\displaystyle\int_{-\pi}^{\pi}X_d(\omega)\,d\omega = 2\pi$.

> [!success]- Solution (d) — Parseval
> $$
> \sum_{n=-\infty}^{\infty}\lvert x[n]\rvert^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega
> \quad\Longrightarrow\quad
> \int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega = 2\pi\left(2^2 + (-1)^2 + 1^2 + (-1)^2 + 2^2\right) = 2\pi(11).
> $$
> **Answer.** $\displaystyle\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2 d\omega = 22\pi$.

**Checking all four afterwards (with the closed form you were not allowed to use).** The signal is real and even, so the pairs $\pm n$ combine into cosines: $X_d(\omega) = x[0] + 2x[1]\cos\omega + 2x[2]\cos 2\omega = 1 - 2\cos\omega + 4\cos 2\omega$. Then $X_d(0) = 1-2+4 = 3$ ✓, $X_d(\pi) = 1+2+4 = 7$ ✓, the cosines integrate to zero over a period so $\int X_d = 2\pi\cdot 1$ ✓, and $\int\lvert X_d\rvert^2 = 2\pi\cdot1 + 4\pi + 16\pi = 22\pi$ ✓ (each $\cos^2$ integrates to $\pi$, the cross terms to $0$).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 250" width="640" height="250" role="img" aria-label="The DTFT 1 - 2cos w + 4cos 2w on [-pi, pi] with X(0)=3, X(pi)=7 and mean value 1" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="150.0" y1="202.4" x2="510.0" y2="202.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="138.6" x2="510.0" y2="138.6" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="106.6" x2="510.0" y2="106.6" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="42.8" x2="510.0" y2="42.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="150.0" y1="154.5" x2="510.0" y2="154.5" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="330.0" y1="30.0" x2="330.0" y2="212.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="150.0" y1="151.5" x2="150.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="150.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="240.0" y1="151.5" x2="240.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="240.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="330.0" y1="151.5" x2="330.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="330.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="420.0" y1="151.5" x2="420.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="420.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="510.0" y1="151.5" x2="510.0" y2="157.5" stroke="currentColor" stroke-width="1"/><text x="510.0" y="226.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="327.0" y1="202.4" x2="333.0" y2="202.4" stroke="currentColor" stroke-width="1"/><text x="146.0" y="206.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">−3</text><line x1="327.0" y1="138.6" x2="333.0" y2="138.6" stroke="currentColor" stroke-width="1"/><text x="146.0" y="142.6" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="327.0" y1="106.6" x2="333.0" y2="106.6" stroke="currentColor" stroke-width="1"/><text x="146.0" y="110.6" text-anchor="end" fill="var(--muted)" style="font-size:11px">3</text><line x1="327.0" y1="42.8" x2="333.0" y2="42.8" stroke="currentColor" stroke-width="1"/><text x="146.0" y="46.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">7</text><text x="510.0" y="148.5" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><text x="336.0" y="41.0" text-anchor="start" fill="var(--muted)" style="font-size:12px">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="150.0" y1="138.6" x2="510.0" y2="138.6" stroke="var(--accent2)" stroke-width="1.3" stroke-dasharray="5 4"/><polyline points="150.0,42.8 152.5,43.0 155.2,43.9 159.7,46.8 165.1,52.5 171.2,61.5 176.8,72.1 184.7,89.7 208.9,152.0 215.2,166.7 220.4,177.4 226.7,188.4 233.0,196.7 236.6,200.1 239.6,202.2 242.2,203.5 246.1,204.4 251.0,203.9 255.3,202.0 259.4,199.0 263.9,194.5 268.4,188.8 275.6,177.8 297.1,139.1 306.8,123.8 313.1,116.0 318.5,111.0 321.9,108.8 324.8,107.5 329.3,106.6 332.5,106.8 335.2,107.5 339.5,109.6 345.8,114.8 350.5,120.2 354.8,126.1 361.1,136.0 378.1,166.9 386.0,180.4 391.4,188.5 397.7,196.2 401.3,199.6 404.2,201.7 409.0,203.9 411.7,204.4 414.8,204.3 417.8,203.5 420.5,202.2 425.0,198.7 430.4,192.6 436.7,182.8 443.0,170.6 453.8,145.3 474.2,92.4 480.5,77.8 486.8,65.1 493.1,54.9 499.4,47.6 504.8,43.9 507.5,43.0 510.0,42.8" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="330.0" cy="106.6" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="510.0" cy="42.8" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="150.0" cy="42.8" r="3.5" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="233.7" y="132.6" text-anchor="middle" fill="var(--accent2)" style="font-size:11px">mean = x[0]</text></svg><figcaption><strong>The check you were not allowed to use: X<sub>d</sub>(ω) = 1 − 2cos ω + 4cos 2ω.</strong> It is real and even because x[n] is real and even. The dots are X<sub>d</sub>(0) = 3 and X<sub>d</sub>(±π) = 7; the dashed line at height x[0] = 1 is the average of X<sub>d</sub> over one period, which is exactly why ∫X<sub>d</sub>(ω)dω = 2π·x[0]. X<sub>d</sub> dips to −25/8 where cos ω = 1/8: a spectrum can be negative, its magnitude cannot.</figcaption></figure>

> [!trap] Where the 40 points leak
> - **(b) Signs at negative $n$.** $(-1)^{-1} = -1$ and $(-1)^{-2} = +1$: the same as for $+1$ and $+2$.
> - **(c) It is $2\pi x[0]$, and $x[0]$ is the sample at the arrow** (here $1$, not the first sample $2$). Writing just $x[0] = 1$ forgets the $2\pi$.
> - **(d) Parseval's $2\pi$ sits on the frequency side**: the answer is $22\pi$, not $11$. And the negative samples count positively, because they are squared.
> - **Using the closed form** (as in the check above) earns 4/10 per part: the problem asks you to know the shortcuts.

**On the exam:** this is a Midterm 2 regular. [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #2 asks for $X_d(0)$ and $X_d(\pi)$ of $u[n+2]-u[n-3]$ (five ones centred at $0$: $5$ and $1$); [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #3 asks for $X_d(0)$, $X_d(\pi)$ and $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$ of $\{1,-3,5,\underset{\uparrow}{-7},5,-3,1\}$ ($-1$, $-25$ and $2\pi(-7) = -14\pi$). Practice family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].

## Checking it in Python

The four forms of 1(b) agree on a grid, and the four numbers of Problem 2 come out of the shortcuts and, as a check, out of numerical integration of $X_d$ (a rectangle rule over one period is exact here, because $X_d$ is a trigonometric polynomial).

```python
import numpy as np

def dtft(x, n0, w):
    """DTFT of a finite sequence whose first sample is at index n0."""
    n = np.arange(n0, n0 + len(x))
    return np.exp(-1j * np.outer(w, n)) @ np.asarray(x, dtype=complex)

w = np.linspace(-np.pi, np.pi, 2001)
w = w[np.abs(w) > 1e-6]                          # the ratio forms are 0/0 at w = 0

# HW5 #1(b): the four accepted forms of the DTFT of u[n] - u[n-4]
X = dtft([1, 1, 1, 1], 0, w)
forms = [2 * np.exp(-1.5j * w) * (np.cos(w / 2) + np.cos(1.5 * w)),
         (1 - np.exp(-4j * w)) / (1 - np.exp(-1j * w)),
         np.exp(-1.5j * w) * np.sin(2 * w) / np.sin(w / 2)]
print([np.allclose(X, f) for f in forms])

# HW5 #2 without a closed form, then the integrals on a fine grid as a check
x, n = np.array([2, -1, 1, -1, 2]), np.arange(-2, 3)
print("X(0) =", x.sum(), "  X(pi) =", np.sum((-1.0) ** n * x))
M = 4096
wg = -np.pi + 2 * np.pi * np.arange(M) / M
Xg = dtft(x, -2, wg)
print("int X / pi =", round((Xg.sum() * 2 * np.pi / M).real / np.pi, 6),
      "  int |X|^2 / pi =", round(np.sum(abs(Xg) ** 2) * 2 * np.pi / M / np.pi, 6))
```

```text
[True, True, True]
X(0) = 3   X(pi) = 7.0
int X / pi = 2.0   int |X|^2 / pi = 22.0
```

## Related

[[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/complex-exponential|complex exponentials]] · [[0-toolkit/01-complex-numbers|complex numbers]] · [[0-toolkit/02-geometric-series|geometric series]] · [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[supplements/transform-tables|transform tables]] (the DTFT tables) · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] · [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · prev: [[homework/hw4|HW4]] · next: [[homework/hw6|HW6]]

### Sources for this page

- ECE 310 Fall 2026 Homework 5 (due Sun Oct 4; the PDF header prints "2025") and the official HW5 solutions, version 1.0 (Hao and Jung Ki), including the grading rubric and the list of accepted (∗) forms quoted above. The signal of Problem 2 was read off the assignment's figure ($x[-2..2] = 2, -1, 1, -1, 2$, zero at $n = \pm3$) and agrees with the key.
- Lecture 13 notes (DTFT analysis and synthesis equations, Exercise 2: the rectangular pulse) and Lecture 14 notes (the impulse pairs, frequency shifting, windowing, Parseval).
- Past Midterm 2 exams cited in the "On the exam" lines (SP2021, FA2023, FA2019 keys).
- Every answer on this page was re-derived and checked numerically (`verify/HW_hw5.py`: DTFT sums on dense grids against every closed form, the impulse weights of (c) from long time averages, truncated geometric sums for (d), and rectangle-rule integration over one period for Problem 2).
