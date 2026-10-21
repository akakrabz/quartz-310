---
title: "Computing DTFTs and inverse DTFTs"
description: "Midterm 2 DTFT problems: a DTFT from the definition, values without the transform, inverse DTFTs of trigonometric polynomials, impulses and rectangles, symmetry versus periodicity, modulation that wraps around ±π, and when X_d(ω) = X(e^{jω})."
tags: [problem-family, problem, dtft, inverse-dtft, midterm-2]
family_frequency: "7 of 7 Midterm 2 exams"
typical_points: "6–23"
lectures: [13, 14]
---

*Problem family · all seven past Midterm 2 exams, one to three short problems each · 6–23 points plus 2–9 points of True/False · [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · drill: [DTFT values](/static/demos/drills/#dtftv)*

## What it looks like on the exam

Short problems of 3–15 points, one move each. 14 of the 43 past T/F statements are DTFT facts.

| instance | asked |
|---|---|
| [[exams/midterm-2/past-exams/fall-2019\|FA2019]] #3 (9) | $X_d(0)$, $X_d(\pi)$, $\int_{-\pi}^{\pi}X_d\,d\omega$ for $x=\{1,\ -3,\ 5,\ \underset{\uparrow}{-7},\ 5,\ -3,\ 1\}$ |
| FA2019 #5 (8) | inverse DTFT of $e^{-j\omega/3}$, $\lvert\omega\rvert\le\pi$, "without complex numbers" |
| FA2019 #6 (5) | $X_d(\omega)=e^{-j\omega^2/3}$ into $h=(\frac13)^nu[n]$: can the output be real? |
| [[exams/midterm-2/past-exams/spring-2021\|SP2021]] #3 (9) | DTFT of $3\delta[n+1]-3\delta[n-7]$ as $Ae^{-jB\omega}\sin(C\omega)$ |
| SP2021 #7 (14) | $A_1$, $A_2$, $\omega_0$ in $A_1\frac{\sin(\omega_0n)}{\omega_0n}+A_2\frac{\sin(2\omega_0n)}{2\omega_0n}$ from its spectrum (2 on $\lvert\omega\rvert\lt\frac{\pi}{3}$, 1 out to $\frac{2\pi}{3}$) |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021]] #2 (15) | causal $y[n]=y[n-2]+x[n]-x[n-1]$: $H(z)$, $h[n]$, $H_d(\omega)$; is $H_d(\omega)=H(e^{j\omega})$? |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023]] #2, #3 (3 + 3) | $X_d=j\omega$ on $[0,\pi]$: formula on $[-\pi,0]$ for real $x$; on $[2\pi,3\pi]$ for any $x$ |
| SP2023 #4 (5) | inverse DTFT of $5e^{j\pi\omega}\delta(\omega-\omega_0)$ |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023]] #2 (6) | $X_d(0)$, $X_d(\pi)$ for $x[n]=u[n+2]-u[n-3]$ |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024]] #2 (8) | real $x[n]$ from an ideal high-pass ($X_d=1$ for $\frac{\pi}{2}\lt\lvert\omega\rvert\le\pi$) |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025]] #2 (10) | DTFTs of $x[n]\cos(\frac{2\pi}{5}n)$, $x[n]\cos^2(\frac{2\pi}{5}n)$ for a low-pass $X_d$ of cutoff $\frac{\pi}{3}$ |
| T/F | FA2019 #1(a, b, c, e) · SP2023 #1(c) · FA2023 #1(a, b, c, f) · FA2024 #1(a, b, d) · SP2025 #1(a, d) → [[exams/midterm-2/true-false-bank\|T/F bank]] Q1–Q9, Q12–Q16 |
| old Midterm 1s | [[exams/midterm-1/past-exams/spring-2023\|SP2023 MT1]] #8 ($x$ with $X_d=1+2\cos2\omega-2j\sin4\omega$), #9 ($X_d(0)$, $X_d(\frac{\pi}{2})$ of $\{1-j,\ \underset{\uparrow}{1},\ -1-j,\ 2j\}$); [[exams/midterm-1/past-exams/fall-2019\|FA2019 MT1]] #8 (DTFT of $\{1,\ \underset{\uparrow}{0},\ 0,\ 2\}$), #9 (DTFT of $\frac{z}{z-3}$, $\lvert z\rvert\gt3$) |
| homework | [[homework/hw5\|HW5]] #1–2 (definition; values of a plotted signal); [[homework/hw6\|HW6]] #2–4 ($x^*[n]$, $x^*[-n]$; inverses of $e^{-j3\omega}+2e^{-j10\omega}$, $e^{-j3.5\omega}$, $\cos^2\omega$; DTFT vs z-transform) |

> [!success]- Answers
> | instance | answer |
> |---|---|
> | FA2019 #3 | $X_d(0)=-1$, $X_d(\pi)=-25$, $\int X_d\,d\omega=2\pi x[0]=-14\pi$ |
> | FA2019 #5 | $x[n]=\dfrac{\sin\big(\pi(n-\frac13)\big)}{\pi(n-\frac13)}$ |
> | FA2019 #6 | No: $X_d(-\omega)\ne X_d^*(\omega)$, so $x$ is complex; $\lvert H_d\rvert\ge\frac34$ never vanishes |
> | SP2021 #3 | $A=6j$, $B=3$, $C=4$ (or $A=-6j$, $C=-4$) |
> | SP2021 #7 | $\omega_0=\frac{\pi}{3}$, $A_2=\frac23$, $A_1=\frac13$ |
> | FA2021 #2 | $H(z)=\dfrac{1}{1+z^{-1}}$, $\lvert z\rvert\gt1$; $h=(-1)^nu[n]$; $H_d=\dfrac{1}{1+e^{-j\omega}}+\pi\sum_k\delta(\omega-\pi-2\pi k)\ne H(e^{j\omega})$ |
> | SP2023 #2 / #3 | (c) $j\omega$ / (e) none: $X_d=j(\omega-2\pi)$ there |
> | SP2023 #4 | $x[n]=\frac{5}{2\pi}e^{j\omega_0(\pi+n)}$ |
> | FA2023 #2 | $X_d(0)=5$, $X_d(\pi)=1$ |
> | FA2024 #2 | $\delta[n]-\dfrac{\sin(\frac{\pi}{2}n)}{\pi n}=(-1)^n\dfrac{\sin(\frac{\pi}{2}n)}{\pi n}$, $x[0]=\frac12$ |
> | SP2025 #2 | (a) $\frac12$ on $\frac{\pi}{15}\lt\lvert\omega\rvert\lt\frac{11\pi}{15}$; (b) $\frac12$ on $\lvert\omega\rvert\le\frac{\pi}{3}$, $\frac14$ on $\frac{7\pi}{15}\lt\lvert\omega\rvert\lt\frac{13\pi}{15}$, $\frac12$ on $\frac{13\pi}{15}\lt\lvert\omega\rvert\le\pi$ |
> | SP2023 MT1 #8, #9 | $\{-1,\ 0,\ 1,\ 0,\ \underset{\uparrow}{1},\ 0,\ 1,\ 0,\ 1\}$; $X_d(0)=1$, $X_d(\frac{\pi}{2})=1$ |
> | FA2019 MT1 #8, #9 | $X_d=e^{j\omega}+2e^{-j2\omega}$; no DTFT (ROC misses the unit circle) |

## The recipe

| $x[n]$ | $X_d(\omega)$ on $[-\pi,\pi]$ |
|---|---|
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ |
| $a^nu[n]$, $\lvert a\rvert\lt1$ | $\dfrac{1}{1-ae^{-j\omega}}$ |
| $\dfrac{\sin(Wn)}{\pi n}$, $0\lt W\lt\pi$ | $1$ for $\lvert\omega\rvert\le W$, $0$ for $W\lt\lvert\omega\rvert\le\pi$ |
| $e^{j\omega_0n}$ | $2\pi\delta(\omega-\omega_0)$ (copies every $2\pi$) |
| $x[n-n_0]$ / $e^{j\omega_0n}x[n]$ | $e^{-j\omega n_0}X_d(\omega)$ / $X_d(\omega-\omega_0)$ |
| $x^*[n]$ / $x[-n]$ | $X_d^*(-\omega)$ / $X_d(-\omega)$ |
| $n\,x[n]$ | $+j\,\dfrac{dX_d}{d\omega}$ (the Lecture 14 table prints $-j$: an erratum) |

> [!recipe] DTFTs and inverse DTFTs
> 1. **Exists? Equals $X(e^{j\omega})$?** Only if the ROC contains $\lvert z\rvert=1$. Bounded but not summable: impulses appear that the substitution misses (FA2021 #2). Growing: no DTFT.
> 2. **Short sequence:** pull out $e^{-jM\omega}$, $M$ the centre; equal pairs give $2\cos(m\omega)$, opposite pairs $2j\sin(m\omega)$.
> 3. **Values:** $X_d(0)=\sum x$; $X_d(\pi)=\sum(-1)^nx[n]$; $\int_{-\pi}^{\pi}X_d=2\pi x[0]$; $\int_{-\pi}^{\pi}\lvert X_d\rvert^2=2\pi\sum\lvert x\rvert^2$; $X_d(\frac{\pi}{2})=\sum x[n]\,(-j)^n$.
> 4. **Trigonometric polynomial:** expand into $e^{\pm j\omega m}$, read off coefficients. Non-integer delay $e^{-j\omega d}$: $\frac{\sin(\pi(n-d))}{\pi(n-d)}$.
> 5. **Sketched spectrum:** rectangles. Height $A$ on $\lvert\omega\rvert\le W$: $A\frac{\sin Wn}{\pi n}$. Band: difference of low-passes, or low-pass times $2\cos(\text{centre}\cdot n)$; band at $\pi$: times $(-1)^n$. $\delta(\omega-\omega_0)\leftrightarrow\frac{1}{2\pi}e^{j\omega_0n}$. Answer real-valued; $x[0]$ = average height.
> 6. **Symmetry, periodicity, modulation.** Real $x$: $X_d(-\omega)=X_d^*(\omega)$. Any $x$: period $2\pi$ only. $x[n]\cos\omega_0n\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$, copies wrapping around $\pm\pi$; $\cos^2$: $\frac12X_d$ plus $\frac14$ copies at $\pm2\omega_0$.

> [!trap] Where the points go
> - **$2\pi$ factors:** $\int X_d=2\pi x[0]$ (FA2019 #3c: $-14\pi$, not $-7$); $\frac{1}{2\pi}$ when inverting an impulse (SP2023 #4).
> - **$X_d(\pi)$ signs follow $n$:** every even $n$ gets $+$, negative ones included (FA2023 #2).
> - **Fractional delay** is a shifted sinc, not $\delta[n-\frac13]$ (FA2019 #5).
> - **Symmetry is not periodicity.** Real $x$: $j\omega$ stays $j\omega$ on $[-\pi,0]$ (SP2023 #2); any $x$: $j(\omega-2\pi)$ on $[2\pi,3\pi]$ (SP2023 #3).
> - **Heights and form.** $\frac{\sin(Wn)}{Wn}$ has height $\frac{\pi}{W}$ (SP2021 #7); $\cos^2$ copies are $\frac14$ (SP2025 #2b); a leftover $j$ loses points (FA2024 #2).

## Practice problems

> [!question] Practice 1 — six numbers, no closed form
> $x[n]=\{1,\ 2,\ \underset{\uparrow}{-1},\ 3,\ 0,\ -2\}$. Without $X_d(\omega)$: $X_d(0)$, $X_d(\pi)$, $X_d(\frac{\pi}{2})$, $X_d(-\frac{\pi}{2})$, $\int_{-\pi}^{\pi}X_d\,d\omega$, $\int_{-\pi}^{\pi}\lvert X_d\rvert^2d\omega$.

> [!success]- Solution
> - $X_d(0)=1+2-1+3+0-2=\mathbf{3}$.
> - $X_d(\pi)=1-2-1-3+0+2=\mathbf{-3}$.
> - $X_d(\frac{\pi}{2})=1\cdot(-1)+2j+(-1)\cdot1+3\cdot(-j)+0+(-2)\cdot j=\mathbf{-2-3j}$.
> - Real $x$: $X_d(-\frac{\pi}{2})=X_d^*(\frac{\pi}{2})=\mathbf{-2+3j}$.
> - $\int X_d\,d\omega=2\pi x[0]=\mathbf{-2\pi}$.
> - Parseval: $2\pi(1+4+1+9+0+4)=\mathbf{38\pi}$.

> [!question] Practice 2 — a band-pass sketch, real answer
> $X_d(\omega)=2$ for $\frac{\pi}{4}\le\lvert\omega\rvert\le\frac{\pi}{2}$, 0 elsewhere in $[-\pi,\pi]$. Real closed form for $x[n]$; $x[0]$, $x[1]$, $x[2]$, $x[4]$.

> [!success]- Solution
> $$
> x[n]=\frac{2\sin(\frac{\pi}{2}n)}{\pi n}-\frac{2\sin(\frac{\pi}{4}n)}{\pi n}=\frac{4\cos(\frac{3\pi}{8}n)\sin(\frac{\pi}{8}n)}{\pi n}.
> $$
> $x[0]=\frac{1}{2\pi}\cdot2\cdot2\cdot\frac{\pi}{4}=\frac12$; $x[1]=\frac{2-\sqrt2}{\pi}\approx0.186$; $x[2]=-\frac{1}{\pi}$; $x[4]=0$.

> [!question] Practice 3 — modulation that wraps around
> $x[n]=\dfrac{\sin(\frac{\pi}{4}n)}{\pi n}$. (a) Sketch the DTFT of $y[n]=x[n]\cos(\frac{5\pi}{6}n)$ on $[-\pi,\pi]$. (b) Sketch the DTFT of $v[n]=x[n]\,e^{j\frac{\pi}{2}n}$. Is $v$ real?

> [!success]- Solution
> **(a)** The copy at $\frac{5\pi}{6}$ covers $[\frac{7\pi}{12},\frac{13\pi}{12}]$ and re-enters at $[-\pi,-\frac{11\pi}{12}]$; its mirror does the same:
> $$
> Y_d(\omega)=\begin{cases}0, & \lvert\omega\rvert\lt\frac{7\pi}{12}\\ \frac12, & \frac{7\pi}{12}\lt\lvert\omega\rvert\lt\frac{11\pi}{12}\\ 1, & \frac{11\pi}{12}\lt\lvert\omega\rvert\le\pi .\end{cases}
> $$
> **(b)** $V_d=X_d(\omega-\frac{\pi}{2})$: 1 on $\frac{\pi}{4}\lt\omega\lt\frac{3\pi}{4}$, 0 on the mirror band. Not even, so $v$ is complex.

## Related

[[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (definition, inverse, periodicity, existence) · [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (impulses, rect/sinc pairs, values without $X_d$, $X(e^{j\omega})$, properties) · [[concepts/dtft-pairs|DTFT pairs]] · [[supplements/transform-tables|transform tables]] · [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] · [[problems/magnitude-phase-and-group-delay|magnitude and phase]]

### Sources for this page

Lectures 13–14 notes and slides; HW5 #1–2, HW6 #2–4 with solutions; past Midterm 2 exams FA2019–SP2025 and two Midterm 1 exams, with keys. Practice problems are new.
