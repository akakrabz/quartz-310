---
title: "Periodic signals and discrete-time frequency"
description: "Period and frequency in continuous and discrete time; orthogonality of harmonics; a discrete-time sinusoid is periodic only when ω₀/2π is rational, and frequencies 2π apart are the same sequence."
tags: [concept, dtft, fourier-series, fourier-analysis, unit-3]
aliases: ["periodic signal", "fundamental period", "harmonics", "discrete-time sinusoid", "equivalent frequencies"]
---

*Lecture 13 (Wed Sep 23) §1 · background in [[homework/hw6|HW6]] #7 (input $j^n=e^{j\frac{\pi}{2}n}$) and HW7 #2 ([[exams/quiz-2|Quiz 2 page]]; $\sin(-\frac{\pi}{3}n)$) · feeds [[concepts/fourier-series|Fourier series]] and the [[concepts/dtft|DTFT]]*

> [!abstract] In one breath
> - Continuous time: every $\Omega_0$ gives a different periodic $e^{j\Omega_0t}$; harmonics $e^{jk\Omega_0t}$ are orthogonal over a period.
> - Discrete time: $e^{j\omega_0n}$ repeats every $2\pi$ in $\omega_0$, so one period $[-\pi,\pi]$ holds every frequency.
> - $\cos(\omega_0n)$ is periodic only if $\omega_0/2\pi=K/L$; then $N_0=L$, not $2\pi/\omega_0$.

## 1. Continuous-time periodic signals

- $x(t+T_0)=x(t)$ for all $t$ (Lecture 13, eq. 1). Smallest such $T_0\gt0$: **fundamental period**.
- Linear frequency $F_0=1/T_0$ (Hz); radial frequency $\Omega_0=2\pi F_0$ (rad/s) (eqs. 2–3).
- Basic periodic signals: $e^{j\Omega_0t}$, $\cos(\Omega_0t)$. Periodic for every real $\Omega_0\neq0$; every $\Omega_0$ gives a different signal.
- **Harmonically related**: frequencies are integer multiples of one fundamental, $x_k(t)=e^{jk\Omega_0t}$, $k\in\mathbb{Z}$ (eq. 5).

> [!key] Orthogonality of harmonics (Lecture 13, eqs. 6–11)
> $$
> \begin{aligned}
> \int_{T_0}x_k(t)\,x_l^*(t)\,dt&=\int_{0}^{T_0}e^{j\Omega_0(k-l)t}\,dt=\left.\frac{e^{j\Omega_0(k-l)t}}{j\Omega_0(k-l)}\right|_{0}^{T_0}=\frac{e^{j2\pi(k-l)}-1}{j\Omega_0(k-l)}\\
> &=\begin{cases}0,&k\neq l\\ T_0,&k=l\end{cases}
> \end{aligned}
> $$
> For $k=l$ the integrand is $1$. Any interval of length $T_0$ works. This is what makes the Fourier-series inner products pick out one coefficient.

## 2. Discrete-time periodic signals

- $x[n+N_0]=x[n]$, $N_0$ a positive integer (samples) (eq. 12).
- $f_0=1/N_0$ (cycles/sample), $\omega_0=2\pi f_0$ (rad/sample) (eqs. 13–14). Basic signal: $e^{j\omega_0n}$ (eq. 15).

> [!key] Frequencies $2\pi$ apart are the same sequence (Lecture 13, eqs. 16–18)
> $$
> e^{j(\omega_0+2\pi k)n}=e^{j\omega_0n}\,e^{j2\pi kn}=e^{j\omega_0n},
> $$
> since $kn$ is an integer. Unique frequencies: $\omega_0\in[0,2\pi)$; the course plots $[-\pi,\pi]$. Example: $\cos(\tfrac{17\pi}{3}n)=\cos(\tfrac{5\pi}{3}n)=\cos(\tfrac{\pi}{3}n)$.

- "Low" and "high" mean distance to the nearest multiple of $2\pi$: $\omega=0$ is slowest, $\omega=\pi$ (the sequence $(-1)^n$) fastest.
- Slide 5: continuous time allows every $\Omega_0\in\mathbb{R}$; discrete time only one period's worth of $\omega_0$.

> [!key] A discrete-time sinusoid is periodic only if $\omega_0/2\pi$ is rational (slide 4)
> $\cos(\omega_0n+\phi)$ and $e^{j\omega_0n}$ are periodic $\iff\dfrac{\omega_0}{2\pi}=\dfrac{K}{L}$ for integers $K,L$. With $K/L$ in lowest terms, $N_0=L$: $K$ full cycles in $L$ samples. $N_0$ is generally **not** $2\pi/\omega_0$.

| signal | $\omega_0/2\pi$ | periodic? | $N_0$ |
|---|---|---|---|
| $\cos(\tfrac{\pi}{4}n)$ | $\tfrac18$ | yes | $8$ |
| $\cos(\tfrac{3\pi}{8}n)$ | $\tfrac{3}{16}$ | yes | $16$ (while $2\pi/\omega_0=\tfrac{16}{3}$ is not an integer) |
| $e^{j0.4\pi n}$ | $\tfrac15$ | yes | $5$ |
| $\sin(\tfrac34n)$ | $\tfrac{3}{8\pi}$, irrational | no | none |

> [!question] Slide 6: which signals equal $x[n]=\sin(\tfrac{\pi}{3}n)$? (Select all that apply.)
> (a) $\sin(-\tfrac{\pi}{3}n)$ $\quad$ (b) $\sin(-\tfrac{5\pi}{3}n)$ $\quad$ (c) $\sin(\tfrac{4\pi}{3}n)$ $\quad$ (d) $\sin(\tfrac{13\pi}{3}n)$

> [!success]- Answer
> **(b) and (d).**
>
> $\tfrac{\pi}{3}-2\pi=-\tfrac{5\pi}{3}$ gives (b); $\tfrac{\pi}{3}+4\pi=\tfrac{13\pi}{3}$ gives (d). (a) $\sin(-\tfrac{\pi}{3}n)=-\sin(\tfrac{\pi}{3}n)$. (c) $\tfrac{4\pi}{3}-2\pi=-\tfrac{2\pi}{3}$, so $\sin(\tfrac{4\pi}{3}n)=-\sin(\tfrac{2\pi}{3}n)$: a different frequency.

## 3. Why it matters downstream

- Only $N_0$ distinct harmonics $e^{j\frac{2\pi}{N_0}kn}$ exist, so the [[concepts/fourier-series|DTFS]] is a finite sum.
- Every [[concepts/dtft|DTFT]] is $2\pi$-periodic for the same reason: $e^{-j(\omega+2\pi)n}=e^{-j\omega n}$.
- A sinusoid is a sum of two $e^{\pm j\omega_0n}$ ([[concepts/complex-exponential|complex exponential]]); an LTI system sees each as an [[concepts/eigenfunctions-of-lti-systems|eigenfunction]] at frequency $\omega_0$ read modulo $2\pi$ ([[concepts/frequency-response|frequency response]]).

## 4. Midterm 2 quick check

> [!question] Q1 · Period of a sum
> Find the fundamental period of $x[n]=\cos(\frac{3\pi}{10}n)+\sin(\frac{\pi}{4}n)$.

> [!success]- Answer
> $\frac{\omega_0}{2\pi}=\frac{3}{20}$: period $20$; $\frac18$: period $8$. The sum repeats when both do: $N_0=\operatorname{lcm}(20,8)=\boldsymbol{40}$. In discrete time a sum of periodic sequences is always periodic (integer periods have a common multiple).

> [!question] Q2 · True or False
> (a) $\cos(1.8\pi n)$ oscillates faster than $\cos(0.6\pi n)$. (b) $\sin(2n)$ is periodic with period $\pi$.

> [!success]- Answer
> (a) **False.** $1.8\pi-2\pi=-0.2\pi$, so $\cos(1.8\pi n)=\cos(0.2\pi n)$: slower than $0.6\pi$. Speed is distance to the nearest multiple of $2\pi$.
> (b) **False.** A period must be an integer number of samples; $\frac{2}{2\pi}=\frac1\pi$ is irrational, so $\sin(2n)$ never repeats.

> [!trap]
> - $N_0=L$ from $\omega_0/2\pi=K/L$ in lowest terms, not $2\pi/\omega_0$.
> - $\sin(\tfrac34n)$ is not periodic at all: $\tfrac{3}{8\pi}$ is irrational.
> - $\sin(-\omega_0n)=-\sin(\omega_0n)$ is a sign flip, not the same signal; $\sin((\omega_0+2\pi)n)$ is.
> - $\omega=\pi$ is the highest discrete-time frequency; $\omega=1.9\pi$ is low (it equals $-0.1\pi$).

> [!exam] Exam
> Fall 2026 MT2 (Wed Nov 4) covers this topic. Never a problem of its own: it settles sampling and aliasing answers ($\omega$ modulo $2\pi$, the sign of a sine). Family: [[problems/sampling-and-the-nyquist-rate|sampling and the Nyquist rate]].
> - [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #3 · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(a), #9(b) · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(a) · [[exams/midterm-2/true-false-bank|MT2 T/F bank]] Q3–Q5

**Where it appears:** [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] §1 (slides 3–6); [[homework/hw6|HW6]] #7, HW7 #2; background for [[concepts/fourier-series|Fourier series]], [[concepts/dtft|DTFT]] periodicity, [[concepts/aliasing|aliasing]] (Lecture 19); [[exams/midterm-2/true-false-bank|MT2 T/F bank]] Q3–Q5.

## Related
[[concepts/fourier-series|Fourier series]] · [[concepts/dtft|DTFT]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/aliasing|aliasing]] · [[concepts/frequency-response|frequency response]]

### Sources for this page
Lecture 13 notes §1.1–1.2 (eqs. 1–18), slides 3–6 (slide 6 answer ours); HW6–HW7; Midterm 2 keys cited.
