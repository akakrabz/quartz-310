---
title: "Computing DTFTs and inverse DTFTs"
description: "Recipe for the DTFT problems of Midterm 2: a DTFT from the definition (factor out the linear phase), values such as X_d(0), X_d(π), ∫X_d and ∫|X_d|² without the transform, inverse DTFTs of trigonometric polynomials, impulses and sketched rectangles (with a real answer), symmetry versus periodicity, modulation copies that wrap around ±π, and when X_d(ω) = X(e^{jω}). On all seven past Midterm 2 exams; four fresh practice problems."
tags: [problem-family, problem, dtft, inverse-dtft, midterm-2]
family_frequency: "7 of 7 Midterm 2 exams"
typical_points: "6–23"
lectures: [13, 14]
---

*Problem family · on all seven past Midterm 2 exams, one to three short problems per exam · 6–23 points of problems, plus 2–9 points of True/False · uses [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] and [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · concepts: [[concepts/dtft]], [[concepts/dtft-pairs]], [[concepts/dtft-properties]], [[concepts/fourier-series]] · drill: [DTFT values](/static/demos/drills/#dtftv) · homework: [[homework/hw5|HW5]], %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #2–#4*

> [!abstract] In one breath
> Every Midterm 2 opens Unit 3 with a few short DTFT problems, and they come in five shapes: **compute** $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$ for a short sequence and put it in a requested form; **read numbers off the definition** without the closed form ($X_d(0)=\sum x$, $X_d(\pi)=\sum(-1)^nx$, $\int X_d=2\pi x[0]$, $\int\lvert X_d\rvert^2=2\pi\sum\lvert x\rvert^2$); **invert** a trigonometric polynomial, an impulse or a sketched rectangle, giving a real-valued answer; use **symmetry and periodicity** (real $x$ $\iff$ $X_d(-\omega)=X_d^*(\omega)$; every $X_d$ repeats every $2\pi$); and **modulate** (multiplying by $\cos\omega_0n$ makes half-height copies at $\pm\omega_0$, which may wrap around $\pm\pi$). Under all of it sits one existence check: $X_d(\omega)=X(e^{j\omega})$ only when the ROC contains the unit circle.

## What it looks like on the exam

Short problems of 3–15 points, each testing one move. The two "big" ones are SP2021 #7 (14 pts, reading a stacked spectrum) and FA2021 #2 (15 pts, a frequency response that needs impulses). The same moves fill the True/False problem: 14 of its 43 past statements are DTFT facts ([[exams/midterm-2/true-false-bank|Midterm 2 T/F bank]], §1 and §3).

| instance | what was asked |
|---|---|
| [[exams/midterm-2/past-exams/fall-2019\|FA2019 #3]] (9) | $X_d(0)$, $X_d(\pi)$ and $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$ for $x=\{1,\ -3,\ 5,\ \underset{\uparrow}{-7},\ 5,\ -3,\ 1\}$ |
| [[exams/midterm-2/past-exams/fall-2019\|FA2019 #5]] (8) | inverse DTFT of $e^{-j\omega/3}$, $\lvert\omega\rvert\le\pi$, "without complex numbers" (a fractional delay) |
| [[exams/midterm-2/past-exams/fall-2019\|FA2019 #6]] (5) | $X_d(\omega)=e^{-j\omega^2/3}$ into $h=(\frac13)^nu[n]$: can the output be real? |
| [[exams/midterm-2/past-exams/spring-2021\|SP2021 #3]] (9) | DTFT of $3\delta[n+1]-3\delta[n-7]$ written as $Ae^{-jB\omega}\sin(C\omega)$ |
| [[exams/midterm-2/past-exams/spring-2021\|SP2021 #7]] (14) | $A_1$, $A_2$, $\omega_0$ in $A_1\frac{\sin(\omega_0n)}{\omega_0n}+A_2\frac{\sin(2\omega_0n)}{2\omega_0n}$ from its two-step spectrum (2 on $\lvert\omega\rvert\lt\frac{\pi}{3}$, 1 out to $\frac{2\pi}{3}$) |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021 #2]] (15) | causal $y[n]=y[n-2]+x[n]-x[n-1]$: $H(z)$, $h[n]$, $H_d(\omega)$, and is $H_d(\omega)=H(e^{j\omega})$? |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #2, #3]] (3 + 3) | $X_d=j\omega$ on $[0,\pi]$: the formula on $[-\pi,0]$ if $x$ is real; on $[2\pi,3\pi]$ if $x$ is arbitrary (multiple choice) |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #4]] (5) | inverse DTFT of $5e^{j\pi\omega}\delta(\omega-\omega_0)$ |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023 #2]] (6) | $X_d(0)$ and $X_d(\pi)$ for $x[n]=u[n+2]-u[n-3]$ |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024 #2]] (8) | real-valued $x[n]$ from a plotted ideal high-pass ($X_d=1$ for $\frac{\pi}{2}\lt\lvert\omega\rvert\le\pi$) |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025 #2]] (10) | sketch the DTFTs of $x[n]\cos(\frac{2\pi}{5}n)$ and $x[n]\cos^2(\frac{2\pi}{5}n)$ for an ideal low-pass $X_d$ of cutoff $\frac{\pi}{3}$ |
| True/False parts | FA2019 #1(a, b, c, e) · SP2023 #1(c) · FA2023 #1(a, b, c, f) · FA2024 #1(a, b, d) · SP2025 #1(a, d) → [[exams/midterm-2/true-false-bank\|T/F bank]] Q1–Q9, Q12–Q16 |
| old Midterm 1s | [[exams/midterm-1/past-exams/spring-2023\|SP2023 MT1]] #8 (which $x$ has $X_d=1+2\cos2\omega-2j\sin4\omega$), #9 ($X_d(0)$, $X_d(\frac{\pi}{2})$ of $\{1-j,\ \underset{\uparrow}{1},\ -1-j,\ 2j\}$); [[exams/midterm-1/past-exams/fall-2019\|FA2019 MT1]] #8 (DTFT of $\{1,\ \underset{\uparrow}{0},\ 0,\ 2\}$), #9 (the DTFT of $\frac{z}{z-3}$, $\lvert z\rvert\gt3$) |
| [[homework/hw5\|HW5]] | #1: DTFTs from the definition of $\{1,0,\underset{\uparrow}{0},0,-1\}$, $u[n]-u[n-4]$, $\cos(\frac{\pi}{3}n+\frac{\pi}{4})$, $\alpha^ne^{j\omega_0n}u[n]$; #2: $X_d(0)$, $X_d(\pi)$, $\int X_d$, $\int\lvert X_d\rvert^2$ of a plotted signal |
| %%hw6:W1tob21ld29yay9odzZcfEhXNl1d%%HW6%%/hw6%% | #2: DTFTs of $x^*[n]$, $x^*[-n]$; #3: inverse DTFTs of $e^{-j3\omega}+2e^{-j10\omega}$, $e^{-j3.5\omega}$, $\cos^2\omega$; #4: DTFT vs z-transform of $3^{-n}u[n]$ and $e^{j\frac{\pi}{4}n}u[n]$ |

> [!success]- Answers to the exam instances
> | instance | answer |
> |---|---|
> | FA2019 #3 | $X_d(0)=-1$, $X_d(\pi)=-25$, $\int_{-\pi}^{\pi}X_d\,d\omega=2\pi x[0]=-14\pi$ |
> | FA2019 #5 | $x[n]=\dfrac{\sin\big(\pi(n-\frac13)\big)}{\pi(n-\frac13)}$ |
> | FA2019 #6 | No: $X_d(-\omega)\ne X_d^*(\omega)$, so $x$ is complex, and $\lvert H_d\rvert\ge\frac34$ never vanishes, so $y$ stays complex |
> | SP2021 #3 | $A=6j$, $B=3$, $C=4$ (or $A=-6j$, $C=-4$) |
> | SP2021 #7 | $\omega_0=\frac{\pi}{3}$, $A_2=\frac23$, $A_1=\frac13$ |
> | FA2021 #2 | $H(z)=\dfrac{1}{1+z^{-1}}$, $\lvert z\rvert\gt1$; $h=(-1)^nu[n]$; $H_d=\dfrac{1}{1+e^{-j\omega}}+\pi\sum_k\delta(\omega-\pi-2\pi k)\ne H(e^{j\omega})$ |
> | SP2023 #2 / #3 | (c) $j\omega$ / (e) none: $X_d=j(\omega-2\pi)$ there |
> | SP2023 #4 | $x[n]=\frac{5}{2\pi}e^{j\omega_0(\pi+n)}$ |
> | FA2023 #2 | $X_d(0)=5$, $X_d(\pi)=1$ |
> | FA2024 #2 | $\delta[n]-\dfrac{\sin(\frac{\pi}{2}n)}{\pi n}=(-1)^n\dfrac{\sin(\frac{\pi}{2}n)}{\pi n}$, $x[0]=\frac12$ |
> | SP2025 #2 | (a) $\frac12$ on $\frac{\pi}{15}\lt\lvert\omega\rvert\lt\frac{11\pi}{15}$; (b) $\frac12$ on $\lvert\omega\rvert\le\frac{\pi}{3}$, $\frac14$ on $\frac{7\pi}{15}\lt\lvert\omega\rvert\lt\frac{13\pi}{15}$, $\frac12$ on $\frac{13\pi}{15}\lt\lvert\omega\rvert\le\pi$ |
> | SP2023 MT1 #8, #9 | $\{-1,\ 0,\ 1,\ 0,\ \underset{\uparrow}{1},\ 0,\ 1,\ 0,\ 1\}$; $X_d(0)=1$, $X_d(\frac{\pi}{2})=1$ |
> | FA2019 MT1 #8, #9 | $X_d=e^{j\omega}+2e^{-j2\omega}$; no DTFT (the ROC $\lvert z\rvert\gt3$ misses the unit circle) |
>
> Full worked solutions are on the exam pages; every row is re-checked in `verify/FAM_instances.py`.

## The recipe

The pairs you need (from [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]]–[[3-fourier-analysis/14-dtft-properties|14]] and the [[supplements/transform-tables|transform tables]]):

| $x[n]$ | $X_d(\omega)$ on $[-\pi,\pi]$ |
|---|---|
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ |
| $a^nu[n]$, $\lvert a\rvert\lt1$ | $\dfrac{1}{1-ae^{-j\omega}}$ |
| $\dfrac{\sin(Wn)}{\pi n}$, $0\lt W\lt\pi$ | $1$ for $\lvert\omega\rvert\le W$, $0$ for $W\lt\lvert\omega\rvert\le\pi$ |
| $e^{j\omega_0n}$ | $2\pi\delta(\omega-\omega_0)$ (and copies every $2\pi$) |
| $x[n-n_0]$ / $e^{j\omega_0n}x[n]$ | $e^{-j\omega n_0}X_d(\omega)$ / $X_d(\omega-\omega_0)$ |
| $x^*[n]$ / $x[-n]$ | $X_d^*(-\omega)$ / $X_d(-\omega)$ |
| $n\,x[n]$ | $+j\,\dfrac{dX_d}{d\omega}$ (the Lecture 14 table prints $-j$: an erratum) |

> [!recipe] DTFTs and inverse DTFTs, move by move
> 1. **Does it exist, and is it $X(e^{j\omega})$?** Absolutely summable $\iff$ the ROC contains $\lvert z\rvert=1$; then $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$. Bounded but not summable ($u[n]$, sinusoids, a pole *on* the unit circle): impulses appear in $X_d$, and the substitution misses them (FA2021 #2). Growing ($2^nu[n]$): no DTFT.
> 2. **Short sequence → factor out the centre.** Write $\sum_nx[n]e^{-j\omega n}$ term by term. If the samples are symmetric about $M=\frac{\text{first}+\text{last}}{2}$, pull out $e^{-jM\omega}$: equal pairs give $2\cos(m\omega)$, opposite pairs give $2j\sin(m\omega)$. This puts $X_d$ in the form $Ae^{-jB\omega}\sin(C\omega)$ or $e^{-jM\omega}\times$(real) that the exam asks for.
> 3. **Numbers without the transform.** $X_d(0)=\sum_nx[n]$; $X_d(\pi)=\sum_n(-1)^nx[n]$ with the sign anchored at $n=0$; $\int_{-\pi}^{\pi}X_d\,d\omega=2\pi x[0]$; $\int_{-\pi}^{\pi}\lvert X_d\rvert^2d\omega=2\pi\sum_n\lvert x[n]\rvert^2$; any other point, e.g. $X_d(\frac{\pi}{2})=\sum_nx[n]\,(-j)^n$.
> 4. **Inverse of a trigonometric polynomial:** expand into $e^{\pm j\omega m}$ and read the coefficients (the DTFT is unique): $e^{-j\omega n_0}\leftrightarrow\delta[n-n_0]$, $\cos m\omega\leftrightarrow\frac12(\delta[n+m]+\delta[n-m])$. A **non-integer** delay $e^{-j\omega d}$ is not a shifted impulse: integrate, $x[n]=\frac{\sin(\pi(n-d))}{\pi(n-d)}$.
> 5. **Inverse of a sketched spectrum:** split it into rectangles. A rectangle of height $A$ on $\lvert\omega\rvert\le W$ is $A\frac{\sin Wn}{\pi n}$ (and $\frac{\sin Wn}{Wn}$ has height $\frac{\pi}{W}$); a band $W_1\lt\lvert\omega\rvert\lt W_2$ is the difference of two low-passes, or a low-pass of half-width $\frac{W_2-W_1}{2}$ times $2\cos\big(\frac{W_1+W_2}{2}n\big)$; a band centred at $\pi$ is a low-pass times $(-1)^n$. Impulses: $\delta(\omega-\omega_0)\leftrightarrow\frac{1}{2\pi}e^{j\omega_0n}$. Write the answer with sines and cosines only, and give $x[0]$ separately (the average of $X_d$ over a period).
> 6. **Symmetry, periodicity, modulation.** Real $x$: $X_d(-\omega)=X_d^*(\omega)$ fills in $[-\pi,0]$. Arbitrary $x$: only $X_d(\omega+2\pi)=X_d(\omega)$ is known. $x[n]\cos\omega_0n\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$ with the **periodic** $X_d$: a copy that leaves at $+\pi$ re-enters at $-\pi$; $\cos^2$ gives $\frac12X_d+\frac14$ copies at $\pm2\omega_0$.
>
> **Checks:** $X_d(0)=\sum x$ against your closed form; real $x$ $\Rightarrow$ even magnitude; your $x[0]$ equals the average height of the sketch; heights of stacked rectangles add.

> [!example] Python: invert a sketch numerically before you trust the formula
> ```python
> import numpy as np
>
> # FA2024 MT2 #2: X_d = 1 on pi/2 < |w| <= pi.  Invert numerically, compare with the closed form.
> w = np.linspace(-np.pi, np.pi, 400001)
> Xd = (np.abs(w) > np.pi / 2).astype(float)
> n = np.arange(-4, 5)
> x_num = np.array([np.trapezoid(Xd * np.exp(1j * w * k), w) / (2 * np.pi) for k in n])
> with np.errstate(invalid="ignore", divide="ignore"):
>     x_formula = np.where(n == 0, 0.5, (-1.0) ** n * np.sin(np.pi * n / 2) / (np.pi * n))
> print("n          :", n)
> print("numerical  :", np.round(x_num.real, 4) + 0.0, " max |imag| =", f"{np.abs(x_num.imag).max():.0e}")
> print("(-1)^n sin(pi n/2)/(pi n):", np.round(x_formula, 4) + 0.0)
> ```
> ```text
> n          : [-4 -3 -2 -1  0  1  2  3  4]
> numerical  : [ 0.      0.1061  0.     -0.3183  0.5    -0.3183  0.      0.1061  0.    ]  max |imag| = 2e-06
> (-1)^n sin(pi n/2)/(pi n): [ 0.      0.1061  0.     -0.3183  0.5    -0.3183  0.      0.1061  0.    ]
> ```
> The imaginary part is numerical noise: the spectrum is real and even, so $x[n]$ is real and even. $x[0]=\frac12$ is the fraction of the period the band covers.

> [!trap] Where the points go
> - **The $2\pi$ in $\int X_d\,d\omega=2\pi x[0]$** (FA2019 #3c: $-14\pi$, not $-7$), and the $\frac{1}{2\pi}$ when an impulse is inverted (SP2023 #4).
> - **The sign pattern of $X_d(\pi)$ follows $n$, not the list:** the sample under the arrow gets $+$, and so does every even $n$, negative ones included (FA2023 #2: the end samples at $n=\pm2$ count $+1$).
> - **$\delta[n-\frac13]$ is not a signal.** A fractional delay inverts to a shifted sinc (FA2019 #5, FA2023 #1(b), HW6 #3(b) with $3.5$).
> - **Substituting $z=e^{j\omega}$ when the ROC misses the unit circle:** $2^nu[n]$ has no DTFT (FA2023 #1(a), FA2024 #1(a)); a pole on the circle leaves impulses that $H(e^{j\omega})$ does not show. In FA2021 #2 cancel first: the pole at $z=1$ goes, the one at $-1$ stays, so the impulse sits at $\omega=\pi$.
> - **The height of $\frac{\sin(Wn)}{Wn}$ is $\frac{\pi}{W}$, not 1** (SP2021 #7), and stacked rectangles add.
> - **"Real-valued" is part of the grade** (FA2024 #2): pair the exponentials into $\sin$ and $\cos$; a leftover $j$ loses points.
> - **Symmetry is not periodicity.** Real $x$: conjugate *and* flip, so $j\omega$ on $[0,\pi]$ stays $j\omega$ on $[-\pi,0]$ (SP2023 #2, not $-j\omega$). Arbitrary $x$: shift the argument, $j(\omega-2\pi)$ on $[2\pi,3\pi]$ (SP2023 #3).
> - **Modulated copies wrap around $\pm\pi$**, and $\cos^2$ copies have height $\frac14$ (SP2025 #2b).

## Practice problems

> [!question] Practice 1 — six numbers, no closed form
> $x[n]=\{1,\ 2,\ \underset{\uparrow}{-1},\ 3,\ 0,\ -2\}$ (so $n=-2,\dots,3$). Without finding $X_d(\omega)$, compute $X_d(0)$, $X_d(\pi)$, $X_d(\frac{\pi}{2})$, $X_d(-\frac{\pi}{2})$, $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$ and $\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$.

> [!success]- Solution
> | $n$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
> |---|---|---|---|---|---|---|
> | $x[n]$ | $1$ | $2$ | $-1$ | $3$ | $0$ | $-2$ |
> | $(-1)^n$ | $+$ | $-$ | $+$ | $-$ | $+$ | $-$ |
> | $(-j)^n=e^{-j\frac{\pi}{2}n}$ | $-1$ | $j$ | $1$ | $-j$ | $-1$ | $j$ |
>
> - $X_d(0)=1+2-1+3+0-2=\mathbf{3}$.
> - $X_d(\pi)=1-2-1-3+0+2=\mathbf{-3}$.
> - $X_d(\frac{\pi}{2})=1\cdot(-1)+2j+(-1)\cdot1+3\cdot(-j)+0+(-2)\cdot j=\mathbf{-2-3j}$.
> - $x$ is real, so $X_d(-\frac{\pi}{2})=X_d^*(\frac{\pi}{2})=\mathbf{-2+3j}$.
> - $\int X_d\,d\omega=2\pi x[0]=\mathbf{-2\pi}$.
> - Parseval: $2\pi(1+4+1+9+0+4)=\mathbf{38\pi}$.
>
> (checked: direct sums and a numerical integral of $X_d$ on a dense grid, `verify/FAM_practice.py`.)

> [!question] Practice 2 — forward and back
> (a) Write the DTFT of $x[n]=2\delta[n+2]-2\delta[n-4]$ in the form $Ae^{-jB\omega}\sin(C\omega)$.
> (b) Find the DTFT of $x[n]=\left(\tfrac12\right)^nu[n-2]$, and check it at $\omega=0$ and $\omega=\pi$.
> (c) Find $x[n]$ if $X_d(\omega)=e^{-j2\omega}\left(1+\cos2\omega\right)$.

> [!success]- Solution
> **(a)** Samples at $n=-2$ and $n=4$: centre $B=1$, half-distance $C=3$.
> $$
> X_d(\omega)=2e^{j2\omega}-2e^{-j4\omega}=2e^{-j\omega}\left(e^{j3\omega}-e^{-j3\omega}\right)=4j\,e^{-j\omega}\sin(3\omega),
> $$
> so $A=4j$, $B=1$, $C=3$.
>
> **(b)** Shift factor, as for the z-transform: $\left(\tfrac12\right)^nu[n-2]=\tfrac14\left(\tfrac12\right)^{n-2}u[n-2]$, absolutely summable, so
> $$
> X_d(\omega)=\frac{\frac14e^{-j2\omega}}{1-\frac12e^{-j\omega}} .
> $$
> Check: $X_d(0)=\frac{1/4}{1/2}=\frac12=\sum_{n\ge2}2^{-n}$ ✓; $X_d(\pi)=\frac{1/4}{3/2}=\frac16=\sum_{n\ge2}(-\frac12)^n$ ✓.
>
> **(c)** $1+\cos2\omega=1+\frac12e^{j2\omega}+\frac12e^{-j2\omega}$, so $X_d=\frac12+e^{-j2\omega}+\frac12e^{-j4\omega}$ and, by uniqueness,
> $$
> x[n]=\tfrac12\delta[n]+\delta[n-2]+\tfrac12\delta[n-4]=\{\underset{\uparrow}{\tfrac12},\ 0,\ 1,\ 0,\ \tfrac12\}.
> $$
> (checked: all three against direct DTFT sums on a grid.)

> [!question] Practice 3 — a band-pass sketch, real answer
> $X_d(\omega)=2$ for $\frac{\pi}{4}\le\lvert\omega\rvert\le\frac{\pi}{2}$ and $0$ elsewhere in $[-\pi,\pi]$. Find a real-valued closed form for $x[n]$, and give $x[0]$, $x[1]$, $x[2]$ and $x[4]$.

> [!success]- Solution
> **Difference of two low-passes:** a height-2 rectangle out to $\frac{\pi}{2}$ minus one out to $\frac{\pi}{4}$:
> $$
> x[n]=\frac{2\sin(\frac{\pi}{2}n)}{\pi n}-\frac{2\sin(\frac{\pi}{4}n)}{\pi n}.
> $$
> **Or one shifted low-pass:** the band is centred at $\pm\frac{3\pi}{8}$ with half-width $\frac{\pi}{8}$, so $x[n]=2\cos(\frac{3\pi}{8}n)\cdot\frac{2\sin(\frac{\pi}{8}n)}{\pi n}=\frac{4\cos(\frac{3\pi}{8}n)\sin(\frac{\pi}{8}n)}{\pi n}$, the same sequence.
>
> Values: $x[0]=\frac{1}{2\pi}\int X_d=\frac{1}{2\pi}\cdot2\cdot2\cdot\frac{\pi}{4}=\frac12$; $x[1]=\frac{2(1-\frac{\sqrt2}{2})}{\pi}=\frac{2-\sqrt2}{\pi}\approx0.186$; $x[2]=\frac{2(0-1)}{2\pi}=-\frac{1}{\pi}$; $x[4]=\frac{2(\sin2\pi-\sin\pi)}{4\pi}=0$.
>
> (checked: both forms against a numerical inverse DTFT for $\lvert n\rvert\le6$.)

> [!question] Practice 4 — modulation that wraps around
> $x[n]=\dfrac{\sin(\frac{\pi}{4}n)}{\pi n}$, so $X_d(\omega)=1$ for $\lvert\omega\rvert\le\frac{\pi}{4}$.
> (a) Sketch the DTFT of $y[n]=x[n]\cos(\frac{5\pi}{6}n)$ on $[-\pi,\pi]$.
> (b) Sketch the DTFT of $v[n]=x[n]\,e^{j\frac{\pi}{2}n}$. Is $v[n]$ real?

> [!success]- Solution
> **(a)** $Y_d(\omega)=\frac12X_d(\omega-\frac{5\pi}{6})+\frac12X_d(\omega+\frac{5\pi}{6})$. The copy centred at $\frac{5\pi}{6}$ covers $[\frac{7\pi}{12},\frac{13\pi}{12}]$; its part beyond $\pi$ re-enters at $[-\pi,-\frac{11\pi}{12}]$. The copy at $-\frac{5\pi}{6}$ does the mirror image, so near $\pm\pi$ two halves overlap:
> $$
> Y_d(\omega)=\begin{cases}0, & \lvert\omega\rvert\lt\frac{7\pi}{12}\\ \frac12, & \frac{7\pi}{12}\lt\lvert\omega\rvert\lt\frac{11\pi}{12}\\ 1, & \frac{11\pi}{12}\lt\lvert\omega\rvert\le\pi .\end{cases}
> $$
> (The same wrap-around as SP2025 #2b.)
>
> **(b)** $V_d(\omega)=X_d(\omega-\frac{\pi}{2})$: height 1 on $\frac{\pi}{4}\lt\omega\lt\frac{3\pi}{4}$ and **zero** on $-\frac{3\pi}{4}\lt\omega\lt-\frac{\pi}{4}$. A real sequence needs $\lvert V_d\rvert$ even, so $v$ is **complex**, as it must be: $v[n]=x[n]\cos\frac{\pi n}{2}+j\,x[n]\sin\frac{\pi n}{2}$.
>
> (checked: long truncated DTFT sums of $y$ and $v$ at test frequencies, $\lvert n\rvert\le2\times10^5$.)

All four are verified in `verify/FAM_practice.py`.

## Related

- Lectures: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (definition, inverse, periodicity, existence, impulses, rectangles and sincs), [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (the DTFT as $X(z)$ on the unit circle, pairs, symmetry, the properties table and its sign erratum).
- Concepts: [[concepts/dtft|DTFT]], [[concepts/dtft-pairs|DTFT pairs]], [[concepts/dtft-properties|DTFT properties]], [[concepts/fourier-series|Fourier series and the CTFT]], [[concepts/region-of-convergence|ROC]]; tables: [[supplements/transform-tables|transform tables]].
- Practice: the [DTFT values drill](/static/demos/drills/#dtftv) (randomized versions of Practice 1), [[demos/practice-drills|all drills]], [[homework/hw5|HW5]], %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%%.
- Next families: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] (evaluate $H_d$ at the input frequencies) and [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]] (the same factoring, read as a plot). Exams: [[exams/midterm-2/index|Midterm 2 overview]], [[exams/midterm-2/true-false-bank|T/F bank]], [[problems/index|all families]].

### Sources for this page

Lecture 13 notes and slides (DTFT definition, inverse, periodicity, the ideal low-pass pair) and Lecture 14 notes and slides (DTFT and z-transform, pairs, properties; the $n\,x[n]$ sign erratum); HW5 #1–2 with official solutions; HW6 #2–4; past Midterm 2 exams FA2019 #3, #5, #6, SP2021 #3, #7, FA2021 #2, SP2023 #2–4, FA2023 #2, FA2024 #2, SP2025 #2 and the DTFT True/False items, with keys; SP2023 and FA2019 Midterm 1 DTFT items. Practice problems are new. Verification: `verify/FAM_practice.py` (practice), `verify/FAM_instances.py` (the answer table), `verify/FAM_counts.py` (frequencies and points).
