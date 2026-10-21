---
title: "LTI response to sinusoids and periodic inputs"
description: "Midterm 2 problems feeding constants, (−1)ⁿ, complex exponentials and sinusoids into a system: list the frequencies, evaluate H_d at each, test whether h is real before the cosine shortcut."
tags: [problem-family, problem, frequency-response, dtft, midterm-2]
family_frequency: "6 of 7 Midterm 2 exams"
typical_points: "8–18"
lectures: [14, 15]
---

*Problem family · a full problem on five of seven past Midterm 2 exams, a True/False part on FA2019 and FA2021 · 8–18 points · [[3-fourier-analysis/15-frequency-response|Lecture 15]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · drill: [sinusoidal response](/static/demos/drills/#sinr)*

## What it looks like on the exam

"$H_d(\omega)=\dots$; find the output for $x[n]=\dots$." Three or four kinds of term; $H_d$ chosen so one term is blocked, one tests symmetry, one needs care with a sign. Recent exams give a formula $H_d$ whose $h$ is never computed.

| instance | system | input | asked |
|---|---|---|---|
| [[exams/midterm-2/past-exams/fall-2019\|FA2019]] #7 (10) | $H(z)=1+z^{-4}$ | $3+4\cos(\frac{\pi}{4}n)+e^{j\frac{\pi}{2}n}$ | $y[n]$ |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023]] #6 (8) | $H_d=\omega e^{j\pi\cos\omega}$ | $3+e^{j\frac{\pi}{3}n}+\sin(\frac{\pi}{2}n+\frac{\pi}{4})$ | $y[n]$ |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023]] #4(b) | $H_d=(\frac12+\cos\omega)e^{j\lvert\omega\rvert}$ | $4j-2e^{j(\frac{2\pi}{3}n+\frac{\pi}{4})}+3\sin(\frac{3\pi}{4}n)$ | $y[n]$ |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024]] #4 (12) | $H_d=\lvert\omega\rvert e^{-j\pi\sin\omega}$ | $3+\cos(\frac{\pi n}{6})+j^n$ | $h$ real? $y[n]$ |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025]] #4 (10) | $H_d=j\omega e^{j\pi\sin\omega}$ | $5+2e^{j\frac{\pi}{4}n}+\sin(\frac{\pi}{2}n+\frac{\pi}{4})+(-1)^n$ | $y[n]$ |
| FA2019 #1(d) | any LSI system | $\cos(\omega_0n+\phi)$ | T/F: the cosine rule for all $\omega_0,\phi$ allows complex $h$ |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021]] #1(a) | stable LTI | $\cos(\omega_0n)$ | T/F: an eigenfunction? |
| [[homework/hw6\|HW6]] #5–7 | accumulator; comb $x[n]+x[n-10]$; $H_d=\omega e^{j\sin\omega}$ | constants, sinusoids, $j^n$ | $H_d=H(e^{j\omega})$? outputs |

> [!success]- Answers
> | instance | $y[n]$ |
> |---|---|
> | FA2019 #7 | $H_d=2\cos(2\omega)e^{-j2\omega}$: $H_d(0)=2$, $H_d(\frac{\pi}{4})=0$, $H_d(\frac{\pi}{2})=2$; $y=6+2e^{j\frac{\pi}{2}n}$ |
> | SP2023 #6 | $\frac{\pi}{3}e^{j(\frac{\pi}{3}n+\frac{\pi}{2})}-j\frac{\pi}{2}\cos(\frac{\pi}{2}n+\frac{\pi}{4})$ (DC blocked; $H_d(\pm\frac{\pi}{2})=\pm\frac{\pi}{2}$) |
> | FA2023 #4(b) | $6j+\frac{3(\sqrt2-1)}{2}\,e^{-j\pi/4}\sin(\frac{3\pi}{4}n)$ (exponential at $\frac{2\pi}{3}$ on a zero; $H_d$ even) |
> | FA2024 #4 | $h$ real; $y=\frac{\pi}{6}\sin(\frac{\pi}{6}n)-\frac{\pi}{2}\,j^n$ |
> | SP2025 #4 | key: $\frac{\pi}{2}e^{j(\frac{\pi}{4}n+\frac{\pi}{2}(1+\sqrt2))}+\frac{\pi}{2}\sin(\frac{\pi}{2}n-\frac{\pi}{4})+j\pi(-1)^n$; last term ambiguous ($H_d(\pi)=j\pi\ne H_d(-\pi)=-j\pi$); the real system returns 0 for $(-1)^n$ (exam page) |
> | FA2019 #1(d) | False: the rule for every $\omega_0,\phi$ forces real $h$ |
> | FA2021 #1(a) | False: a delay gives $\cos(\omega_0n-\omega_0)$ |

## The recipe

> [!recipe] One frequency at a time
> 1. **$H_d(\omega)$.** From $h$: $\sum_nh[n]e^{-j\omega n}$. From $H(z)$ or an LCCDE: $H(e^{j\omega})$ only if the ROC contains $\lvert z\rvert=1$ (FA2021 #2, HW6 #5).
> 2. **Is $h$ real?** $H_d(-\omega)=H_d^*(\omega)$: even magnitude, odd phase. $\lvert\omega\rvert e^{-j\pi\sin\omega}$ passes; $\omega e^{j\pi\cos\omega}$ fails.
> 3. **List frequencies in $(-\pi,\pi]$.** Constant: 0. $(-1)^n$: $\pi$. $j^n$: $\frac{\pi}{2}$ only. $e^{j\omega_0n}$: $\omega_0$ only. $\cos$, $\sin$: $\pm\omega_0$.
> 4. **Evaluate $H_d$ at each.** A zero removes the term.
> 5. **Apply.** $e^{j\omega_0n}\to H_d(\omega_0)e^{j\omega_0n}$. Real $h$: $A\cos(\omega_0n+\theta)\to A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$. Complex $h$: split $\cos$ or $\sin$ into exponentials, use $H_d(\omega_0)$ and $H_d(-\omega_0)$ separately.
> 6. **Check:** real $h$, real input term → real output term; $H_d(0)$, $H_d(\pi)$ real for real $h$.

> [!trap] Where the points go
> - **The shortcut with a complex $h$** (SP2023 #6, FA2023 #4): a real sine in, a complex signal out.
> - **$H_d(-\omega_0)$:** in SP2025 #4, $H_d(-\frac{\pi}{2})=+j\frac{\pi}{2}$, the conjugate.
> - **A lone exponential has no partner;** its coefficient stays ($2\cdot\frac{\pi}{4}=\frac{\pi}{2}$ in SP2025 #4). A constant $4j$ is $\omega=0$, not $j^n$ (FA2023 #4: $6j$).
> - **Amplitude vs magnitude:** $2\cos(2\omega)e^{-j2\omega}$ at $\frac{\pi}{2}$ is $(-2)(-1)=+2$ (FA2019 #7).
> - **$H_d(\pi)\ne H_d(-\pi)$** (SP2025 #4): say which value you take.

## Practice problems

> [!question] Practice 1 — a real FIR, four kinds of term
> $h[n]=\{\underset{\uparrow}{1},\ -1,\ 1\}$, $x[n]=4+2\cos(\frac{\pi}{3}n+\frac{\pi}{6})+3\sin(\frac{\pi}{2}n)+(-1)^n$. Find $y[n]$.

> [!success]- Solution
> $H_d=e^{-j\omega}(2\cos\omega-1)$, $h$ real. $H_d(0)=1$; $H_d(\frac{\pi}{3})=0$ (blocked); $H_d(\frac{\pi}{2})=j$; $H_d(\pi)=3$.
> $$
> y[n]=4+3\cos\left(\tfrac{\pi}{2}n\right)+3(-1)^n .
> $$

> [!question] Practice 2 — a complex $h$
> $h[n]=\{\underset{\uparrow}{-\tfrac{j}{2}},\ 1,\ \tfrac{j}{2}\}$. (a) Show $H_d(\omega)=(1+\sin\omega)\,e^{-j\omega}$. Is $h$ real? (b) $y[n]$ for $x[n]=3+2\cos(\frac{\pi}{2}n)+e^{j\frac{\pi}{3}n}$.

> [!success]- Solution
> **(a)** $e^{-j\omega}\left(1+\frac{e^{j\omega}-e^{-j\omega}}{2j}\right)=(1+\sin\omega)e^{-j\omega}$; magnitude not even: complex.
> **(b)** $H_d(0)=1$, $H_d(\frac{\pi}{2})=-2j$, $H_d(-\frac{\pi}{2})=0$, $H_d(\frac{\pi}{3})=(1+\frac{\sqrt3}{2})e^{-j\pi/3}$:
> $$
> y[n]=3+2e^{j(\frac{\pi}{2}n-\frac{\pi}{2})}+\left(1+\tfrac{\sqrt3}{2}\right)e^{j(\frac{\pi}{3}n-\frac{\pi}{3})} .
> $$
> The shortcut would give $4\sin(\frac{\pi}{2}n)$: wrong.

> [!question] Practice 3 — an IIR resonator
> Causal: $y[n]=-\tfrac14y[n-2]+x[n]-x[n-2]$. (a) Is $H_d(\omega)=H(e^{j\omega})$? (b) Output for $x[n]=5+3\sin(\frac{\pi}{2}n+\frac{\pi}{6})+2(-1)^n$, all $n$. (c) Input switched on at $n=0$?

> [!success]- Solution
> **(a)** Poles $\pm\frac{j}{2}$, ROC $\lvert z\rvert\gt\frac12$: yes, $H_d=\dfrac{1-e^{-j2\omega}}{1+\frac14e^{-j2\omega}}$, $h$ real.
> **(b)** $H_d(0)=H_d(\pi)=0$, $H_d(\frac{\pi}{2})=\frac83$:
> $$
> y[n]=8\sin\left(\tfrac{\pi}{2}n+\tfrac{\pi}{6}\right).
> $$
> **(c)** (b) becomes the steady state; a transient decaying like $(\frac12)^n$ adds 4.5 at $n=0$.

## Related

[[concepts/eigenfunctions-of-lti-systems|Eigenfunctions]] · [[concepts/frequency-response|frequency response]] · [[demos/frequency-response-explorer|frequency-response explorer]] · [[problems/dtft-and-inverse-dtft|DTFT family]] · [[problems/magnitude-phase-and-group-delay|magnitude and phase]] · [[exams/midterm-2/index|Midterm 2]]

### Sources for this page

Lectures 14–15 notes and slides; HW6 #5–7; past Midterm 2 exams FA2019–SP2025 with keys. Practice problems are new.
