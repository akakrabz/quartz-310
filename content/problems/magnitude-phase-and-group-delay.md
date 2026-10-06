---
title: "Magnitude, phase and group delay"
description: "Recipe for the \"find H_d(ω), then sketch |H_d(ω)| and ∠H_d(ω) on [−π, π]\" problems of Midterm 2: pull out the linear-phase factor, read the magnitude off the real amplitude, place the π jumps (sign changes) and 2π wraps (principal value), spot double zeros and non-real sequences, and compute the group delay, uniform or not. On five of seven past exams; four fresh practice problems."
tags: [problem-family, problem, frequency-response, group-delay, midterm-2]
family_frequency: "5 of 7 Midterm 2 exams"
typical_points: "10–18"
lectures: [15, 16]
---

*Problem family · on five of the seven past Midterm 2 exams (SP2021, SP2023, FA2023, FA2024, SP2025), one problem each · 10–18 points · uses [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]], with $H_d$ from [[3-fourier-analysis/15-frequency-response|Lecture 15]] · concepts: [[concepts/magnitude-and-phase-response]], [[concepts/group-delay]], [[concepts/frequency-response]] · see it: [[demos/frequency-response-explorer|frequency-response explorer]] · drill: [magnitude & phase](/static/demos/drills/#magph)*

> [!abstract] In one breath
> For a short filter, factor the centre's delay out of $H_d(\omega)$: $H_d(\omega)=A(\omega)\,e^{-jM\omega}$, or $jA(\omega)e^{-jM\omega}$ for antisymmetric taps, with $A$ **real**. Then $\lvert H_d\rvert=\lvert A\rvert$ (never negative), and $\angle H_d=-M\omega$ ($+\frac{\pi}{2}$ for the $j$), plus $\pi$ wherever $A\lt0$, reduced to $[-\pi,\pi]$. Two kinds of break appear in the phase plot: **$\pi$ jumps** where $A$ changes sign (at simple zeros of the magnitude) and **$2\pi$ wraps** where the line leaves $[-\pi,\pi]$. The slope of the unbroken phase gives the **group delay** $\tau_{gd}(\omega)=-\frac{d\angle H_d}{d\omega}$: the constant $M$ for these linear-phase filters, a function of $\omega$ otherwise.

## What it looks like on the exam

"Determine $H_d(\omega)$. Plot (or sketch) $\lvert H_d(\omega)\rvert$ and $\angle H_d(\omega)$ for $-\pi\le\omega\le\pi$; label your axes carefully." The system is a two- or three-tap FIR given by $h[n]$ or a difference equation, or a closed-form $H_d$ whose real factor changes sign. Points go to the factorisation, the zeros, the values at $0$ and $\pm\pi$, and the jumps. None of the seven past exams asked for a group delay, but Lecture 16 does (and so does the magnitude & phase drill).

| instance | system | asked |
|---|---|---|
| [[exams/midterm-2/past-exams/spring-2021\|SP2021 #2]] (10) | $X_d(\omega)=e^{-j4\omega}\sin2\omega$ | sketch magnitude and phase (the sequence is purely imaginary: the phase is not odd) |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #5]] (14) | $h[n]=\delta[n]+\delta[n-6]$ | $H_d$; plot magnitude and phase |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023 #4(a)]] (18 with the output) | $H_d=(\frac12+\cos\omega)e^{j\lvert\omega\rvert}$ | plot magnitude and phase (an even phase: $h$ complex) |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024 #3]] (12) | $h[n]=\delta[n+2]+\delta[n]+\delta[n-2]$ | $H_d(0)$, $H_d(\frac{\pi}{2})$, $H_d(\pi)$; plot $\lvert H_d\rvert$ |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025 #3]] (12) | $y[n]=x[n]+2x[n-3]+x[n-6]$ | $H_d$; sketch magnitude and phase |
| same factoring | [[exams/midterm-2/past-exams/spring-2021\|SP2021 #3]] ($Ae^{-jB\omega}\sin C\omega$ form), [[exams/midterm-2/past-exams/fall-2019\|FA2019 #7]] ($1+z^{-4}=2\cos2\omega\,e^{-j2\omega}$, then sinusoids) | |
| %%hw6:W1tob21ld29yay9odzZcfEhXNl1d%%HW6%%/hw6%% #6 | $y[n]=x[n]+x[n-10]$ | magnitude and phase, then outputs for two inputs |
| [[3-fourier-analysis/16-magnitude-and-phase-response\|Lecture 16]] | $\{1,0,1\}$, $\{1,0,-1\}$, $\{3,2,1\}$ | magnitude, phase, group delay (Example 3 is non-uniform) |

> [!success]- Answers to the exam instances
> | instance | magnitude | phase (principal value) |
> |---|---|---|
> | SP2021 #2 | $\lvert\sin2\omega\rvert$: zeros $0,\pm\frac{\pi}{2},\pm\pi$, peaks 1 at $\pm\frac{\pi}{4},\pm\frac{3\pi}{4}$ | $-4\omega$, $+\pi$ where $\sin2\omega\lt0$, wrapped: $\pi$ jumps at $0,\pm\frac{\pi}{2}$, $2\pi$ wraps only at $\frac{\pi}{4}$ and $-\frac{3\pi}{4}$ (not symmetric: the phase is not odd) |
> | SP2023 #5 | $H_d=2e^{-j3\omega}\cos3\omega$; $2\lvert\cos3\omega\rvert$, zeros $\pm\frac{\pi}{6},\pm\frac{\pi}{2},\pm\frac{5\pi}{6}$ | slope $-3$ inside $[-\frac{\pi}{2},\frac{\pi}{2}]$, $\pi$ jumps at every zero |
> | FA2023 #4(a) | $\lvert\frac12+\cos\omega\rvert$: $\frac32$ at 0, zeros $\pm\frac{2\pi}{3}$, $\frac12$ at $\pm\pi$ | $\lvert\omega\rvert$ for $\lvert\omega\rvert\lt\frac{2\pi}{3}$, $\lvert\omega\rvert-\pi$ beyond (even) |
> | FA2024 #3 | $H_d=1+2\cos2\omega$: $H_d(0)=3$, $H_d(\frac{\pi}{2})=-1$, $H_d(\pi)=3$; $\lvert H_d\rvert$ zeros $\pm\frac{\pi}{3},\pm\frac{2\pi}{3}$, bumps of 1 at $\pm\frac{\pi}{2}$ | (not asked) 0, or $\pm\pi$ where $1+2\cos2\omega\lt0$ |
> | SP2025 #3 | $H_d=(2+2\cos3\omega)e^{-j3\omega}$; $2+2\cos3\omega$: 4 at $0,\pm\frac{2\pi}{3}$, 0 at $\pm\frac{\pi}{3},\pm\pi$ | $-3\omega$ wrapped ($2\pi$ wraps at $\pm\frac{\pi}{3}$); group delay 3 |
>
> Worked solutions and plots on the exam pages; the factorisations and values re-checked in `verify/FAM_instances.py`.

## The recipe

> [!recipe] Magnitude and phase plots in six steps
> 1. **Write $H_d(\omega)=\sum_nh[n]e^{-j\omega n}$** (from a difference equation: the coefficients of the $x$ terms; $H(e^{j\omega})$ for an FIR is always allowed).
> 2. **Pull out the centre.** $M=\frac{\text{first index}+\text{last index}}{2}$ (a half-integer for an even number of taps). Symmetric taps pair into $2h\cos(m\omega)$, antisymmetric ones into $2jh\sin(m\omega)$: $H_d=A(\omega)e^{-jM\omega}$ or $jA(\omega)e^{-jM\omega}$, $A$ real. Simplify $A$ (sum-to-product) until its sign is easy to read.
> 3. **Magnitude $=\lvert A(\omega)\rvert$.** Mark $\lvert A(0)\rvert=\lvert\sum h\rvert$, $\lvert A(\pi)\rvert=\lvert\sum(-1)^nh\rvert$, the zeros and the peaks. Never draw a negative magnitude.
> 4. **Phase $=-M\omega$** ($+\frac{\pi}{2}$ for the $j$), **plus $\pi$ wherever $A\lt0$.** Choose $+\pi$ or $-\pi$ to stay in $[-\pi,\pi]$ and say which endpoint you use at $\pm\pi$.
> 5. **Mark the breaks.** A $\pi$ jump at each **simple** zero of $A$ (sign change); none at a **double** zero ($A\ge0$ touches 0, as $2+2\cos3\omega$ does). A $2\pi$ wrap wherever the line reaches $\pm\pi$. For a real $h$ the phase is odd: draw $\omega\gt0$ and reflect through the origin. For a non-real $h$ (an even phase, an imaginary sequence) do **not** reflect.
> 6. **Group delay** $\tau_{gd}(\omega)=-\frac{d\angle H_d}{d\omega}$, ignoring the jumps and wraps: $M$ for every linear-phase filter. For a non-linear phase differentiate $\angle H_d=\tan^{-1}\frac{I}{R}$: $\tau_{gd}=\frac{IR'-RI'}{R^2+I^2}$; for one tap pair $1+ae^{-j\omega}$ this is $\frac{a^2+a\cos\omega}{1+2a\cos\omega+a^2}$.
>
> **Checks:** the magnitude at $0$ and $\pi$ from the sums of taps; the magnitude has at most (length of $h$ minus one) zeros in $(-\pi,\pi]$, counted with multiplicity; the phase at $\omega=0$ is $0$ or $\pm\pi$ for a real $h$ (or $\pm\frac{\pi}{2}$ next to a zero of an antisymmetric one).

> [!example] Python: magnitude and group delay of a filter whose phase is not linear
> ```python
> import numpy as np
> from scipy.signal import freqz, group_delay
>
> h = [1, 0.5]                                           # Practice 3: H_d = 1 + (1/2) e^{-jw}
> w = np.array([0, np.pi / 3, np.pi / 2, 2 * np.pi / 3, np.pi])
> _, H = freqz(h, [1], worN=w)
> _, tau = group_delay((h, [1]), w=w)
> c = np.cos(w)
> print("w/pi        :", np.round(w / np.pi, 3))
> print("|H|         :", np.round(np.abs(H), 4))
> print("tau (scipy) :", np.round(tau, 4))
> print("tau formula :", np.round((0.25 + 0.5 * c) / (1.25 + c), 4))
> ```
> ```text
> w/pi        : [0.    0.333 0.5   0.667 1.   ]
> |H|         : [1.5    1.3229 1.118  0.866  0.5   ]
> tau (scipy) : [ 0.3333  0.2857  0.2     0.     -1.    ]
> tau formula : [ 0.3333  0.2857  0.2     0.     -1.    ]
> ```
> `scipy.signal.group_delay` agrees with the formula in step 6: a third of a sample at DC, zero at $\frac{2\pi}{3}$, and $-1$ at $\pi$.

> [!trap] Where the points go
> - **A negative "magnitude".** $H_d(\frac{\pi}{2})=-1$ in FA2024 #3 is the right value of $H_d$; its magnitude is $+1$, and the $-$ goes into the phase as $\pm\pi$.
> - **A $\pi$ that is not there.** $2+2\cos3\omega$ never goes negative (SP2025 #3: "never negative, thus its angle is zero!"), so the phase is just the wrapped line $-3\omega$; its breaks at $\pm\frac{\pi}{3}$ are $2\pi$ wraps that happen to sit on double zeros.
> - **Confusing $\pi$ jumps with $2\pi$ wraps.** Jumps sit at sign changes of $A$ (zeros of the magnitude), wraps where the line hits $\pm\pi$ (SP2023 #5 has only jumps; SP2021 #2 has both).
> - **Reflecting the phase of a non-real sequence.** SP2021 #2's sequence is purely imaginary ($\angle X_d(-\omega)=\pi-\angle X_d(\omega)$), and FA2023 #4's phase $\lvert\omega\rvert$ is even. Odd phase is a property of real $h$ only.
> - **Forgetting the $j$ of an antisymmetric pair** ($e^{j\theta}-e^{-j\theta}=2j\sin\theta$): it adds $\frac{\pi}{2}$ to the phase.
> - **Group delay from the principal phase.** Differentiate the unbroken line; the jumps contribute nothing, and a negative group delay is allowed for a non-linear phase.

## Practice problems

> [!question] Practice 1 — the second difference
> $h[n]=\{\underset{\uparrow}{1},\ -2,\ 1\}$. Find $\lvert H_d(\omega)\rvert$ and $\angle H_d(\omega)$ on $[-\pi,\pi]$, the values of $\lvert H_d\rvert$ at $\frac{\pi}{3}$, $\frac{\pi}{2}$, $\pi$, and the group delay. Where does the phase plot break, and why is that not a $\pi$ jump?

> [!success]- Solution
> $H_d=1-2e^{-j\omega}+e^{-j2\omega}=e^{-j\omega}(2\cos\omega-2)=-(2-2\cos\omega)e^{-j\omega}=4\sin^2\!\left(\tfrac{\omega}{2}\right)e^{j(\pi-\omega)}$.
>
> - $\lvert H_d\rvert=2-2\cos\omega=4\sin^2(\frac{\omega}{2})$: a high-pass, $0$ at DC, $1$ at $\frac{\pi}{3}$, $2$ at $\frac{\pi}{2}$, $4$ at $\pi$.
> - The real factor $-(2-2\cos\omega)$ is never positive, so the phase is $-\omega+\pi$ everywhere, reduced to $[-\pi,\pi]$: $\angle H_d=\pi-\omega$ for $0\lt\omega\le\pi$ and $-\pi-\omega$ for $-\pi\le\omega\lt0$.
> - The break at $\omega=0$ (from $-\pi$ to $+\pi$) is a $2\pi$ wrap of the principal value: the amplitude does not change sign, because $\omega=0$ is a **double** zero ($H(z)=(1-z^{-1})^2$).
> - $\tau_{gd}=1$ sample, the centre tap.
>
> (checked with `freqz` and `group_delay`.)

> [!question] Practice 2 — four taps, a half-sample delay
> $y[n]=x[n+1]+x[n]+x[n-1]+x[n-2]$. Show that $H_d(\omega)=4\cos\omega\cos\frac{\omega}{2}\,e^{-j\omega/2}$, sketch magnitude and phase, give $\lvert H_d\rvert$ at $0$, $\frac{\pi}{3}$, $\frac{3\pi}{4}$, the phase at $\frac{3\pi}{4}$, and the group delay.

> [!success]- Solution
> Taps at $n=-1,\dots,2$, so $M=\frac12$: $H_d=e^{-j\omega/2}\left(2\cos\frac{3\omega}{2}+2\cos\frac{\omega}{2}\right)=4\cos\omega\cos\frac{\omega}{2}\,e^{-j\omega/2}$ (sum-to-product).
>
> - $A(\omega)=4\cos\omega\cos\frac{\omega}{2}$: $4$ at $0$; zeros at $\pm\frac{\pi}{2}$ ($\cos\omega$) and $\pm\pi$ ($\cos\frac{\omega}{2}$); negative for $\frac{\pi}{2}\lt\lvert\omega\rvert\lt\pi$. $\lvert H_d(\frac{\pi}{3})\rvert=4\cdot\frac12\cdot\frac{\sqrt3}{2}=\sqrt3$; $\lvert H_d(\frac{3\pi}{4})\rvert=4\cdot\frac{\sqrt2}{2}\cos\frac{3\pi}{8}=2\sqrt2\cos\frac{3\pi}{8}\approx1.08$.
> - Phase: $-\frac{\omega}{2}$ for $\lvert\omega\rvert\lt\frac{\pi}{2}$; $-\frac{\omega}{2}+\pi$ for $\frac{\pi}{2}\lt\omega\lt\pi$ and $-\frac{\omega}{2}-\pi$ for $-\pi\lt\omega\lt-\frac{\pi}{2}$ (odd, as for any real $h$), with $\pi$ jumps at $\pm\frac{\pi}{2}$. At $\frac{3\pi}{4}$: $-\frac{3\pi}{8}+\pi=\frac{5\pi}{8}$.
> - $\tau_{gd}=\frac12$ sample: the causal version $\{1,1,1,1\}$ would have $\frac32$, and the one-sample advance subtracts 1.
>
> (checked with direct DTFT sums and `group_delay`.)

> [!question] Practice 3 — a phase that is not linear
> $h[n]=\{\underset{\uparrow}{1},\ \tfrac12\}$. Find $\lvert H_d\rvert$, show that $\tau_{gd}(\omega)=\dfrac{\frac14+\frac12\cos\omega}{\frac54+\cos\omega}$, and evaluate it at $0$, $\frac{\pi}{3}$, $\frac{\pi}{2}$, $\frac{2\pi}{3}$, $\pi$. Does this filter preserve the shape of a pulse?

> [!success]- Solution
> $\lvert H_d\rvert^2=(1+\frac12\cos\omega)^2+\frac14\sin^2\omega=\frac54+\cos\omega$, so $\lvert H_d\rvert$ is $\frac32$ at DC and $\frac12$ at $\pi$, and never zero (so no jumps). $\angle H_d=-\tan^{-1}\dfrac{\frac12\sin\omega}{1+\frac12\cos\omega}$, and differentiating (step 6 with $a=\frac12$):
> $$
> \tau_{gd}(\omega)=\frac{\frac14+\frac12\cos\omega}{\frac54+\cos\omega}:\qquad \tfrac13,\ \tfrac27,\ \tfrac15,\ 0,\ -1\quad\text{at }0,\ \tfrac{\pi}{3},\ \tfrac{\pi}{2},\ \tfrac{2\pi}{3},\ \pi .
> $$
> The group delay is **non-uniform**: low frequencies are delayed by a third of a sample (the "centre of mass" $\frac{0\cdot1+1\cdot\frac12}{1+\frac12}=\frac13$ of $h$, as in Lecture 16's Example 3), high frequencies are *advanced*. Different components move by different amounts, so a pulse is slightly reshaped. (Phase at $\frac{2\pi}{3}$, where $\tau_{gd}=0$: its most negative value, $-\frac{\pi}{6}$.)

> [!question] Practice 4 — an antisymmetric pair, three points
> $h[n]=-\delta[n+1]+\delta[n-5]$. Write $H_d$ as $Ae^{-jB\omega}\sin(C\omega)$, then give $\lvert H_d\rvert$ and $\angle H_d$ at $\omega=\frac{\pi}{6}$, $\frac{\pi}{2}$, $\frac{5\pi}{6}$, and the group delay.

> [!success]- Solution
> Centre $B=2$, half-distance $C=3$: $H_d=-e^{j\omega}+e^{-j5\omega}=e^{-j2\omega}\left(-e^{j3\omega}+e^{-j3\omega}\right)=-2j\,e^{-j2\omega}\sin3\omega$, so $A=-2j$.
>
> - $\frac{\pi}{6}$: $\sin\frac{\pi}{2}=1$, $H_d=-2je^{-j\pi/3}=2e^{-j5\pi/6}$: magnitude 2, angle $-\frac{5\pi}{6}$.
> - $\frac{\pi}{2}$: $\sin\frac{3\pi}{2}=-1$, $H_d=2je^{-j\pi}=-2j$: magnitude 2, angle $-\frac{\pi}{2}$.
> - $\frac{5\pi}{6}$: $\sin\frac{5\pi}{2}=1$, $H_d=-2je^{-j5\pi/3}=2e^{-j\pi/6}$: magnitude 2, angle $-\frac{\pi}{6}$.
>
> $\lvert H_d\rvert=2\lvert\sin3\omega\rvert$ (zeros at $0,\pm\frac{\pi}{3},\pm\frac{2\pi}{3},\pm\pi$), phase $-\frac{\pi}{2}-2\omega$ plus $\pi$ where $\sin3\omega\lt0$, and $\tau_{gd}=2$. ($h$ is real, so the angles at $-\frac{\pi}{6}$, … are the negatives.)

All four are verified in `verify/FAM_practice.py`.

## Related

- Lectures: [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] (principal angle, the pull-out trick, which phases jump by $\pi$, group delay), [[3-fourier-analysis/15-frequency-response|Lecture 15]] (getting $H_d$).
- Concepts: [[concepts/magnitude-and-phase-response|magnitude and phase response]], [[concepts/group-delay|group delay and linear phase]], [[concepts/frequency-response|frequency response]], [[0-toolkit/01-complex-numbers|complex numbers]] (the principal angle).
- Try it: [[demos/frequency-response-explorer|frequency-response explorer]] (principal vs unwrapped phase, the group delay curve), the [magnitude & phase drill](/static/demos/drills/#magph), [[demos/practice-drills|all drills]]; homework %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #6.
- Related families: [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] (the same $H_d$, evaluated at the input frequencies), [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]]. Exams: [[exams/midterm-2/index|Midterm 2 overview]], [[problems/index|all families]].

### Sources for this page

Lecture 16 notes and slides (magnitude and phase response, the linear-phase trick on $\{1,0,1\}$, $\{1,0,-1\}$, $\{3,2,1\}$, group delay; no annotated slides exist for this lecture) and Lecture 15; HW6 #6; past Midterm 2 exams SP2021 #2–3, SP2023 #5, FA2023 #4, FA2024 #3, SP2025 #3 and FA2019 #7 with keys. Practice problems are new; every value is checked in `verify/FAM_practice.py` (`freqz`, `group_delay`, finite differences of the unwrapped phase), the answer table in `verify/FAM_instances.py`.
