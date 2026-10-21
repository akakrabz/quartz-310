---
title: "Magnitude, phase and group delay"
description: "Midterm 2 \"find H_d(ω), sketch |H_d| and ∠H_d on [−π, π]\" problems: pull out the linear phase, read the magnitude, place π jumps and 2π wraps, compute the group delay."
tags: [problem-family, problem, frequency-response, group-delay, midterm-2]
family_frequency: "5 of 7 Midterm 2 exams"
typical_points: "10–18"
lectures: [15, 16]
---

*Problem family · five of seven past Midterm 2 exams, one problem each · 10–18 points · [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]], [[3-fourier-analysis/15-frequency-response|Lecture 15]] · drill: [magnitude & phase](/static/demos/drills/#magph)*

## What it looks like on the exam

"Determine $H_d(\omega)$; plot $\lvert H_d\rvert$ and $\angle H_d$ for $-\pi\le\omega\le\pi$." A two- or three-tap FIR, or a closed-form $H_d$ whose real factor changes sign. No past exam asked for a group delay; Lecture 16 does.

| instance | system | asked |
|---|---|---|
| [[exams/midterm-2/past-exams/spring-2021\|SP2021]] #2 (10) | $X_d(\omega)=e^{-j4\omega}\sin2\omega$ | magnitude, phase (imaginary sequence) |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023]] #5 (14) | $h[n]=\delta[n]+\delta[n-6]$ | $H_d$; magnitude, phase |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023]] #4(a) | $H_d=(\frac12+\cos\omega)e^{j\lvert\omega\rvert}$ | magnitude, phase (even phase: $h$ complex) |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024]] #3 (12) | $h[n]=\delta[n+2]+\delta[n]+\delta[n-2]$ | $H_d(0)$, $H_d(\frac{\pi}{2})$, $H_d(\pi)$; $\lvert H_d\rvert$ |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025]] #3 (12) | $y[n]=x[n]+2x[n-3]+x[n-6]$ | $H_d$; magnitude, phase |
| same factoring | SP2021 #3; FA2019 #7 ($1+z^{-4}=2\cos2\omega\,e^{-j2\omega}$) | |
| [[homework/hw6\|HW6]] #6 | $y[n]=x[n]+x[n-10]$ | magnitude, phase, outputs |
| Lecture 16 | $\{1,0,1\}$, $\{1,0,-1\}$, $\{3,2,1\}$ | magnitude, phase, group delay (Example 3 non-uniform) |

> [!success]- Answers
> | instance | magnitude | phase (principal value) |
> |---|---|---|
> | SP2021 #2 | $\lvert\sin2\omega\rvert$: zeros $0,\pm\frac{\pi}{2},\pm\pi$, peaks 1 at $\pm\frac{\pi}{4},\pm\frac{3\pi}{4}$ | $-4\omega$, $+\pi$ where $\sin2\omega\lt0$: $\pi$ jumps at $0,\pm\frac{\pi}{2}$, $2\pi$ wraps only at $\frac{\pi}{4}$, $-\frac{3\pi}{4}$ (not odd) |
> | SP2023 #5 | $H_d=2e^{-j3\omega}\cos3\omega$; $2\lvert\cos3\omega\rvert$, zeros $\pm\frac{\pi}{6},\pm\frac{\pi}{2},\pm\frac{5\pi}{6}$ | slope $-3$ between jumps, $\pi$ jumps at every zero |
> | FA2023 #4(a) | $\lvert\frac12+\cos\omega\rvert$: $\frac32$ at 0, zeros $\pm\frac{2\pi}{3}$, $\frac12$ at $\pm\pi$ | $\lvert\omega\rvert$ for $\lvert\omega\rvert\lt\frac{2\pi}{3}$, $\lvert\omega\rvert-\pi$ beyond (even) |
> | FA2024 #3 | $H_d=1+2\cos2\omega$: $3$, $-1$, $3$; zeros $\pm\frac{\pi}{3},\pm\frac{2\pi}{3}$, bumps of 1 at $\pm\frac{\pi}{2}$ | (not asked) 0, or $\pm\pi$ where negative |
> | SP2025 #3 | $H_d=(2+2\cos3\omega)e^{-j3\omega}$: 4 at $0,\pm\frac{2\pi}{3}$, 0 at $\pm\frac{\pi}{3},\pm\pi$ | $-3\omega$ wrapped ($2\pi$ wraps at $\pm\frac{\pi}{3}$); group delay 3 |

## The recipe

> [!recipe] Magnitude and phase in six steps
> 1. **$H_d=\sum_nh[n]e^{-j\omega n}$** (FIR: always allowed).
> 2. **Pull out the centre** $M=\frac{\text{first}+\text{last}}{2}$: symmetric pairs give $2h\cos(m\omega)$, antisymmetric $2jh\sin(m\omega)$; $H_d=A(\omega)e^{-jM\omega}$ or $jA(\omega)e^{-jM\omega}$, $A$ real.
> 3. **Magnitude $=\lvert A\rvert$.** Mark $\lvert\sum h\rvert$ at 0, $\lvert\sum(-1)^nh\rvert$ at $\pi$, zeros, peaks.
> 4. **Phase $=-M\omega$** ($+\frac{\pi}{2}$ for the $j$), $+\pi$ where $A\lt0$, reduced to $[-\pi,\pi]$.
> 5. **Breaks:** $\pi$ jump at each simple zero of $A$, none at a double zero; $2\pi$ wrap where the line hits $\pm\pi$. Real $h$: odd phase, reflect; non-real $h$: do not.
> 6. **Group delay** $\tau_{gd}=-\frac{d\angle H_d}{d\omega}$ of the unbroken phase: $M$ for linear phase. For $1+ae^{-j\omega}$: $\frac{a^2+a\cos\omega}{1+2a\cos\omega+a^2}$.

> [!trap] Where the points go
> - **Negative "magnitude":** $H_d(\frac{\pi}{2})=-1$ in FA2024 #3; magnitude $+1$, phase $\pm\pi$.
> - **A $\pi$ that is not there:** $2+2\cos3\omega\ge0$ (SP2025 #3); breaks at $\pm\frac{\pi}{3}$ are $2\pi$ wraps on double zeros.
> - **Jumps vs wraps:** SP2023 #5 has only jumps; SP2021 #2 both.
> - **Reflecting a non-real phase:** SP2021 #2 (imaginary), FA2023 #4 (even phase).
> - **Group delay from the principal phase:** differentiate the unbroken line; negative values are allowed.

## Practice problems

> [!question] Practice 1 — the second difference
> $h[n]=\{\underset{\uparrow}{1},\ -2,\ 1\}$. $\lvert H_d\rvert$, $\angle H_d$; $\lvert H_d\rvert$ at $\frac{\pi}{3}$, $\frac{\pi}{2}$, $\pi$; group delay. Where does the phase break, and why is it not a $\pi$ jump?

> [!success]- Solution
> $H_d=-(2-2\cos\omega)e^{-j\omega}=4\sin^2\!\left(\tfrac{\omega}{2}\right)e^{j(\pi-\omega)}$.
> - $\lvert H_d\rvert=2-2\cos\omega$: 0, 1, 2, 4 at $0,\frac{\pi}{3},\frac{\pi}{2},\pi$.
> - $\angle H_d=\pi-\omega$ for $0\lt\omega\le\pi$, $-\pi-\omega$ for $-\pi\le\omega\lt0$.
> - The break at 0 is a $2\pi$ wrap: double zero, $H(z)=(1-z^{-1})^2$.
> - $\tau_{gd}=1$.

> [!question] Practice 2 — four taps, a half-sample delay
> $y[n]=x[n+1]+x[n]+x[n-1]+x[n-2]$. Show $H_d(\omega)=4\cos\omega\cos\frac{\omega}{2}\,e^{-j\omega/2}$; sketch; $\lvert H_d\rvert$ at $0$, $\frac{\pi}{3}$, $\frac{3\pi}{4}$; phase at $\frac{3\pi}{4}$; group delay.

> [!success]- Solution
> $M=\frac12$: $e^{-j\omega/2}\left(2\cos\frac{3\omega}{2}+2\cos\frac{\omega}{2}\right)$, sum-to-product.
> - $A$: 4 at 0; zeros $\pm\frac{\pi}{2}$, $\pm\pi$; negative for $\frac{\pi}{2}\lt\lvert\omega\rvert\lt\pi$. $\lvert H_d(\frac{\pi}{3})\rvert=\sqrt3$; $\lvert H_d(\frac{3\pi}{4})\rvert=2\sqrt2\cos\frac{3\pi}{8}\approx1.08$.
> - Phase $-\frac{\omega}{2}$, $+\pi$ on $(\frac{\pi}{2},\pi)$, $-\pi$ on $(-\pi,-\frac{\pi}{2})$; at $\frac{3\pi}{4}$: $\frac{5\pi}{8}$.
> - $\tau_{gd}=\frac12$.

> [!question] Practice 3 — a phase that is not linear
> $h[n]=\{\underset{\uparrow}{1},\ \tfrac12\}$. $\lvert H_d\rvert$; show $\tau_{gd}(\omega)=\dfrac{\frac14+\frac12\cos\omega}{\frac54+\cos\omega}$ and evaluate at $0$, $\frac{\pi}{3}$, $\frac{\pi}{2}$, $\frac{2\pi}{3}$, $\pi$. Is a pulse's shape preserved?

> [!success]- Solution
> $\lvert H_d\rvert^2=\frac54+\cos\omega$: $\frac32$ at DC, $\frac12$ at $\pi$, no zeros. Step 6 with $a=\frac12$:
> $$
> \tau_{gd}(\omega)=\frac{\frac14+\frac12\cos\omega}{\frac54+\cos\omega}:\qquad \tfrac13,\ \tfrac27,\ \tfrac15,\ 0,\ -1 .
> $$
> Non-uniform: lows delayed, highs advanced; the pulse is reshaped.

## Related

[[concepts/magnitude-and-phase-response|Magnitude and phase]] · [[concepts/group-delay|group delay]] · [[demos/frequency-response-explorer|frequency-response explorer]] · [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] · [[problems/dtft-and-inverse-dtft|DTFT family]]

### Sources for this page

Lectures 15–16 notes and slides; HW6 #6; past Midterm 2 exams FA2019–SP2025 with keys. Practice problems are new.
