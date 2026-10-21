---
title: "Unbounded outputs and pole matching"
description: "\"Which inputs give an unbounded output?\": pole bookkeeping for Y(z) = H(z)X(z), unstable versus marginally stable systems, resonance at a unit-circle pole, inputs whose zeros cancel a pole."
tags: [problem-family, problem, midterm-1, stability, z-transform, roc]
family_frequency: "7 of 7 exams"
typical_points: "6–10"
lectures: [4, 9, 10, 11]
---

*Problem family · 7 of 7 past midterms · 6–10 points, a T/F list or a three-part construction · [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]*

## What it looks like on the exam

1. **T/F list:** which of 5–6 inputs give an unbounded (or bounded) output (FA2025 #8, SP2025 #6, Lecture 11 slide 18).
2. **Construction:** a bounded input with unbounded output, an unbounded input with bounded output, a bounded one with bounded output (SP2023 #7, HW4 #3); or "is $y$ bounded?" after a response (FA2024 #7d, FA2023 #7c).

| where | system | asked | answers |
|---|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #8a]] | $\dfrac{1-\frac34z^{-1}}{1+3z^{-1}}$, $\lvert z\rvert>3$ (unstable) | bounded output? | i $(\frac34)^nu[n]$ F · ii $\frac13(\frac12)^nu[n]+(\frac12)^{n-1}u[n-1]$ **T** · iii $(-3)^nu[n]$ F · iv $\delta[n]-\frac34\delta[n-1]$ F · v $\delta[n]+3\delta[n-1]$ **T** |
| FA2025 #8b | poles $\frac34,\ j,\ e^{j2/3}$, $\lvert z\rvert>1$ (marginal) | unbounded output? | i $\delta[n]-\frac34\delta[n-1]$ F · ii $(\frac23)^nu[n]$ F · iii $j^nu[n]$ **T** · iv $\sin(\frac{\pi}{2}n)u[n]$ **T** · v $\cos(\frac{2\pi}{3}n)u[n]$ F |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #6]] | $\dfrac{z}{z-e^{j\pi/4}}$, $\lvert z\rvert>1$ (marginal) | unbounded output? | $u[n]$ F · $e^{j\pi n/4}u[n]$ **T** · $e^{-j\pi n/4}u[n]$ F · $e^{-j3\pi n/4}u[n]$ F · $\cos(\frac{\pi}{4}n)u[n]$ **T** · $4^nu[n]$ **T** |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #7]] | $\dfrac{z-3}{z-4}$, $\lvert z\rvert>4$ (unstable) | three constructions | $\delta[n]$; $3^nu[n]-4(3)^{n-1}u[n-1]\to\delta[n]$; $\delta[n]-4\delta[n-1]\to\delta[n]-3\delta[n-1]$ |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #5b]] | $\dfrac{3z^{-1}}{1+z^{-2}}$, poles $\pm j$ | bounded inputs, unbounded outputs | $j^nu[n]$, $\cos(\frac{\pi}{2}n)u[n]$, $\sin(\frac{\pi}{2}n)u[n]$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #7c]] | causal, poles $\frac14,\ -1$ | a bad input | $(-1)^nu[n]=\cos(\pi n)u[n]$ |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #7c,d]] | poles $\frac12,\ 2$; $X$ has a zero at 2 | $y$ bounded? | yes: $y=2n(\frac12)^nu[n]$ |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #10d]] | stable $H$ in series with $2^nu[n]$ | "overall unstable"? | False: zero of $H$ at 2 cancels the pole |
| [[homework/hw4\|HW4 #3, #5]] | four causal $H$; a cascade | stable? bad input? | (a) $\delta[n]$; (c) $u[n]$, not $\delta[n]$; (d) $\cos(\frac{\pi}{4}n)u[n]$; #5 stable |
| Lecture 11 slide 18 | $\dfrac{1}{(1-jz^{-1})(1+z^{-1})(1-\frac23z^{-1})}$, $\lvert z\rvert>1$ | which inputs are bad? | $(-1)^nu[n]$, $j^nu[n]$, $\sin(-\frac{\pi}{2}n)u[n]$, $\cos(\frac{\pi}{2}n)u[n]$ yes; $u[n]$, $e^{-j\pi n/2}u[n]$, $(\frac23)^nu[n]$, $\sin(\frac{2\pi}{3}n)u[n]$ no |

## The recipe

> [!recipe] Pole bookkeeping
> 1. **Classify $H$:** stable (ROC contains $\lvert z\rvert=1$: done); unstable (pole outside); marginal (largest poles simple on $\lvert z\rvert=1$).
> 2. **Input poles and zeros.** $a^nu[n]$: pole $a$. $e^{j\omega_0n}u[n]$: one pole $e^{j\omega_0}$. $\cos$, $\sin$: both $e^{\pm j\omega_0}$. Finite input: zeros only. Sums: combine $X(z)$, read the numerator.
> 3. **$Y=HX$, cancel** zeros of $X$ on poles of $H$ and vice versa.
> 4. **Survivors:** bounded iff every pole has $\lvert p\rvert<1$, or $\lvert p\rvert=1$ and simple. Double unit-circle pole: $n\,e^{j\omega_0n}$ growth.
> 5. **Constructions.** Bounded → unbounded: $\delta[n]$ (unstable), resonant $e^{j\omega_0n}u[n]$ (marginal). Bounded → bounded: $x=\delta[n]-p\,\delta[n-1]$. Unbounded → bounded: $X=1/H$, $y=\delta[n]$.
> 6. **Check** angle and magnitude, angles mod $2\pi$: $e^{j5\pi/3}=e^{-j\pi/3}$.

> [!trap] Where the points go
> - **$e^{j2/3}$ is not $e^{j2\pi/3}$** (FA2025 #8b-v: $\frac23$ rad vs $120°$, False).
> - **A conjugate is a different pole** (SP2025 #6: $e^{-j\pi n/4}u[n]$ harmless, $\cos(\tfrac{\pi}{4}n)u[n]$ not).
> - **$\delta[n]$ fails for a marginal system:** $h$ is bounded (HW4 #3c).
> - **Disguised cancellations:** combine $X(z)$ (FA2025 #8a-ii: zero at $-3$, True).
> - **Cascades:** decide on $H_1H_2$ after cancellation (FA2019 #10d False, HW4 #5 stable).

## Practice problems

> [!question] Practice 1 — marginally stable, seven inputs
> $$
> H(z) = \frac{1}{(1-\frac13z^{-1})(1-z^{-1}+z^{-2})},\quad\text{causal.}
> $$
> Unbounded output? (i) $\delta[n]$ (ii) $(\tfrac13)^nu[n]$ (iii) $\cos(\tfrac{\pi}{3}n)u[n]$ (iv) $\sin(\tfrac{2\pi}{3}n)u[n]$ (v) $e^{j5\pi n/3}u[n]$ (vi) $(-1)^nu[n]$ (vii) $\cos(\tfrac{n}{3})u[n]$

> [!success]- Solution
> Poles $\tfrac13$, $e^{\pm j\pi/3}$: marginal.
> (i) F; (ii) F (double pole inside); (iii) **T**; (iv) F ($120°\neq60°$); (v) **T** ($e^{j5\pi/3}=e^{-j\pi/3}$); (vi) F; (vii) F ($\tfrac13$ rad).

> [!question] Practice 2 — an unstable system with a zero outside the unit circle
> Causal $H(z) = \dfrac{1-2z^{-1}}{1+3z^{-1}}$. (a) Bounded input, unbounded output. (b) Unbounded input, bounded output. (c) Bounded → bounded. (d) Bounded output? (i) $2^nu[n]$ (ii) $(-3)^nu[n]$ (iii) $(\tfrac12)^nu[n]+3(\tfrac12)^{n-1}u[n-1]$ (iv) $\delta[n]-2\delta[n-1]$.

> [!success]- Solution
> **(a)** $\delta[n]$: $h=\{\underset{\uparrow}{1},\ -5,\ 15,\ -45,\dots\}$.
> **(b)** $X=1/H$: $x[n] = 2^nu[n]+3(2)^{n-1}u[n-1]$, $y=\delta[n]$.
> **(c)** $x=\delta[n]+3\delta[n-1]$: $y=\delta[n]-2\delta[n-1]$.
> **(d)** (i) F: the zero eats the input's pole, $-3$ survives. (ii) F. (iii) **T**: zero at $-3$. (iv) F.

> [!question] Practice 3 — a cascade with an unstable stage
> $h_1=2^nu[n]$ in series with causal $H_2(z) = \dfrac{1-2z^{-1}}{1-\frac13z^{-1}}$. (a) T/F: the cascade is unstable. (b) $x=u[n]$ into system 1: the middle signal $w$ and $y$?

> [!success]- Solution
> **(a) False:** $H=\dfrac{1}{1-\frac13z^{-1}}$, $h=(\tfrac13)^nu[n]$.
> **(b)** $w[n] = (2^{n+1}-1)\,u[n]$, unbounded;
> $$
> y[n] = \tfrac32\left(1-\left(\tfrac13\right)^{n+1}\right)u[n],
> $$
> bounded. A real implementation with system 1 first would still overflow.

## Related

[[concepts/marginal-stability|Marginal stability]] · [[concepts/pole-zero-cancellation|pole–zero cancellation]] · [[problems/parameters-for-stability|parameters for stability]] · [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z)]] · [[exams/midterm-1/true-false-bank|T/F bank]]

### Sources for this page

Lecture 11 notes and slides 12–18; HW4 #3, #5 with solutions; past Midterm 1 exams FA2019–FA2025 with keys. Practice problems are new.
