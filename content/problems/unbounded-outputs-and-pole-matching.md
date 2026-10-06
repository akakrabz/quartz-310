---
title: "Unbounded outputs and pole matching"
description: "Recipe for the \"which inputs give an unbounded output?\" problems: pole bookkeeping for Y(z) = H(z)X(z), unstable versus marginally stable systems, resonance at a unit-circle pole, and inputs whose zeros cancel a pole. Three fresh practice problems."
tags: [problem-family, problem, midterm-1, stability, z-transform, roc]
family_frequency: "7 of 7 exams"
typical_points: "6–10"
lectures: [4, 9, 10, 11]
---

*Problem family · on 7 of 7 past midterms · typically 6–10 pts (a T/F list or a three-part construction) · uses [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] · concepts: [[concepts/bibo-stability]], [[concepts/marginal-stability]], [[concepts/pole-zero-cancellation]], [[concepts/eigenfunctions-of-lti-systems]]*

> [!abstract] In one breath
> For a causal system and a right-sided input, $y[n]$ is bounded exactly when every pole of $Y(z)=H(z)X(z)$ **that survives cancellation** is inside the unit circle, or on it and simple. So an **unstable** system blows up for almost any input (take $\delta[n]$), unless the input has a zero on the bad pole. A **marginally stable** system (simple poles on $\lvert z\rvert=1$) blows up only when the input has a pole at *exactly* the same point, which gives a double pole and linear growth.

## What it looks like on the exam

Two formats, both short and both easy to lose points on:

1. **A true/false list:** "mark which inputs produce an unbounded (or bounded) output" for a given $H(z)$, 5–6 inputs (FA2025 #8, SP2025 #6, Lecture 11 slide 18).
2. **A construction:** "find a bounded input that gives an unbounded output / an unbounded input that gives a bounded output / a bounded input that gives a bounded output" (SP2023 #7, HW4 #3), or "is $y$ bounded?" at the end of a response calculation (FA2024 #7d, FA2023 #7c).

| where | system | asked | answers |
|---|---|---|---|
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #8a]] | $\dfrac{1-\frac34z^{-1}}{1+3z^{-1}}$, $\lvert z\rvert>3$ (unstable) | bounded output? | i $(\frac34)^nu[n]$ F · ii $\frac13(\frac12)^nu[n]+(\frac12)^{n-1}u[n-1]$ **T** · iii $(-3)^nu[n]$ F · iv $\delta[n]-\frac34\delta[n-1]$ F · v $\delta[n]+3\delta[n-1]$ **T** |
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #8b]] | poles $\frac34,\ j,\ e^{j2/3}$, $\lvert z\rvert>1$ (marginal) | unbounded output? | i $\delta[n]-\frac34\delta[n-1]$ F · ii $(\frac23)^nu[n]$ F · iii $j^nu[n]$ **T** · iv $\sin(\frac{\pi}{2}n)u[n]$ **T** · v $\cos(\frac{2\pi}{3}n)u[n]$ F |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #6]] | $\dfrac{z}{z-e^{j\pi/4}}$, $\lvert z\rvert>1$ (marginal) | unbounded output? | $u[n]$ F · $e^{j\pi n/4}u[n]$ **T** · $e^{-j\pi n/4}u[n]$ F · $e^{-j3\pi n/4}u[n]$ F · $\cos(\frac{\pi}{4}n)u[n]$ **T** · $4^nu[n]$ **T** |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #7]] | $\dfrac{z-3}{z-4}$, $\lvert z\rvert>4$ (unstable) | three constructions | $\delta[n]$; $3^nu[n]-4(3)^{n-1}u[n-1]\to\delta[n]$; $\delta[n]-4\delta[n-1]\to\delta[n]-3\delta[n-1]$ |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #5b]] | $\dfrac{3z^{-1}}{1+z^{-2}}$, poles $\pm j$ (marginal) | bounded inputs with unbounded outputs | $j^nu[n]$, $\cos(\frac{\pi}{2}n)u[n]$, $\sin(\frac{\pi}{2}n)u[n]$ |
| [[exams/midterm-1/past-exams/fall-2023\|FA2023 #7c]] | causal, poles $\frac14,\ -1$ | not stable: give a bad input | $(-1)^nu[n]=\cos(\pi n)u[n]$ |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #7c,d]] | causal, poles $\frac12,\ 2$; $X$ has a zero at 2 | is $y$ bounded? | yes: $y=2n(\frac12)^nu[n]$ |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #10d]] | stable $H$ in series with $2^nu[n]$ | "overall unstable": T/F? | False: the zero of $H$ at 2 cancels the pole |
| [[homework/hw4\|HW4 #3, #5]] | four causal $H$; a cascade | stable? bad input? | (a) $\delta[n]$; (c) $u[n]$, not $\delta[n]$; (d) $\cos(\frac{\pi}{4}n)u[n]$; #5 cascade is stable |
| [[2-z-transform/11-bibo-stability-and-causality\|Lecture 11]] | $3^nu[n]$, $(-1)^nu[n]$; slide 18 | which inputs are bad? | answered below |

> [!example]- Lecture 11, slide 18, answered
> Causal $H(z)=\dfrac{1}{(1-jz^{-1})(1+z^{-1})(1-\frac23z^{-1})}$, ROC $\lvert z\rvert>1$: marginally stable, with unit-circle poles $j$ and $-1$. Unbounded output for: $(-1)^nu[n]$ **yes** (pole $-1$); $u[n]$ no (pole $1$ is not a pole of $H$); $e^{j\pi n/2}u[n]=j^nu[n]$ **yes**; $e^{-j\pi n/2}u[n]$ no ($-j$ is not a pole of $H$); $(\frac23)^nu[n]$ no (a double pole *inside* the circle is harmless); $\sin(-\frac{\pi}{2}n)u[n]$ **yes** and $\cos(\frac{\pi}{2}n)u[n]$ **yes** (each contains $e^{j\pi n/2}$); $\sin(\frac{2\pi}{3}n)u[n]$ no.

## The recipe

> [!recipe] Bounded or unbounded? Do the pole bookkeeping
> 1. **System poles and ROC.** Factor $H(z)$; causal → $\lvert z\rvert>\max\lvert p\rvert$. Classify: **stable** (ROC contains $\lvert z\rvert=1$: every bounded input gives a bounded output, done); **unstable** (a pole strictly outside the unit circle); **marginally stable** (largest poles simple and exactly on $\lvert z\rvert=1$).
> 2. **Input poles and zeros.** $a^nu[n]\to$ pole at $a$. $e^{j\omega_0n}u[n]\to$ one pole $e^{j\omega_0}$. $\cos(\omega_0n+\phi)u[n]$ and $\sin(\omega_0n)u[n]\to$ **both** poles $e^{\pm j\omega_0}$. A finite input has only zeros, so compute them: $\delta[n]-c\,\delta[n-1]\to$ zero at $c$. For a sum of terms, combine $X(z)$ over a common denominator and look at the numerator.
> 3. **Form $Y=HX$ and cancel:** a zero of $X$ on a pole of $H$, or a zero of $H$ on a pole of $X$.
> 4. **Read the survivors.** Bounded $\iff$ every surviving pole has $\lvert p\rvert<1$, or $\lvert p\rvert=1$ and is simple. A pole with $\lvert p\rvert>1$ gives exponential growth; a double pole on $\lvert z\rvert=1$ gives $n\,e^{j\omega_0n}$ growth (resonance, [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]).
> 5. **Constructions on demand:**
>    - *bounded → unbounded:* unstable $H$: $\delta[n]$. Marginal $H$: $e^{j\omega_0n}u[n]$ or $\cos(\omega_0n)u[n]$ at a pole angle $\omega_0$ ($\delta[n]$ fails, since $h$ is bounded).
>    - *bounded → bounded, unstable $H$:* put a zero on each bad pole, $X(z)=1-pz^{-1}$, i.e. $x[n]=\delta[n]-p\,\delta[n-1]$.
>    - *unbounded → bounded:* $X$ must also carry a bad pole that a zero of $H$ removes, so $H$ needs a zero with $\lvert q\rvert\ge1$. The cleanest choice is $X(z)=1/H(z)$, which gives $y[n]=\delta[n]$ (SP2023 #7b).
>
> **Checks.** Compare poles exactly, angle **and** magnitude, with angles reduced mod $2\pi$: $e^{j5\pi/3}=e^{-j\pi/3}$. A repeated pole *inside* the circle ($n\,a^n$, $\lvert a\rvert<1$) is bounded.

> [!trap] Where the points go
> - **$e^{j2/3}$ is not $e^{j2\pi/3}$.** FA2025 #8b-v: the pole is at angle $\tfrac23$ rad $\approx 38°$, the input $\cos(\tfrac{2\pi}{3}n)u[n]$ has poles at $\pm120°$. No match, bounded output: **False**. Read every exponent twice for a missing $\pi$.
> - **A conjugate is a different pole.** SP2025 #6: $H$ has only $e^{j\pi/4}$ (complex coefficients), so $e^{-j\pi n/4}u[n]$ is harmless, but $\cos(\tfrac{\pi}{4}n)u[n]$ contains $e^{+j\pi n/4}$ and blows up.
> - **$\delta[n]$ is not the universal answer.** For a marginally stable system $h$ is bounded (HW4 #3c: $h=u[n]+u[n-1]$), so $\delta[n]$ gives a bounded output. The resonant input is required.
> - **Disguised cancellations.** FA2025 #8a-ii: $\tfrac13(\tfrac12)^nu[n]+(\tfrac12)^{n-1}u[n-1]$ has $X=\dfrac{\frac13(1+3z^{-1})}{1-\frac12z^{-1}}$, whose zero at $-3$ kills the unstable pole: bounded, **True**. Always combine $X(z)$ and look at its zeros.
> - **A zero of $H$ can eat the input's pole.** HW4 #3d: $u[n]$ into $H=\frac{z-1}{z^2+j}$ is harmless because $H$ has a zero at 1. But eating the *input's* pole does nothing about the *system's* bad pole (Practice 2, input i).
> - **One signal, several disguises.** $(-1)^nu[n]$, $\cos(\pi n)u[n]$ and $e^{j\pi n}u[n]$ are the same input, with a single pole at $-1$ (the "two" poles $e^{\pm j\pi}$ coincide). Likewise $j^nu[n]=e^{j\pi n/2}u[n]$. Rewrite each input as $a^nu[n]$ terms before matching.
> - **Cascades:** stability of a series connection is decided by the product $H_1H_2$ **after** cancellation (FA2019 #10d is False, HW4 #5 is stable), even though a signal inside the cascade can blow up (Practice 3).

## Practice problems

> [!question] Practice 1 — marginally stable, seven inputs
> A causal LTI system has
> $$
> H(z) = \frac{1}{(1-\frac13z^{-1})(1-z^{-1}+z^{-2})} .
> $$
> Mark True/False: the input produces an **unbounded** output.
> (i) $\delta[n]$ (ii) $(\tfrac13)^nu[n]$ (iii) $\cos(\tfrac{\pi}{3}n)u[n]$ (iv) $\sin(\tfrac{2\pi}{3}n)u[n]$ (v) $e^{j5\pi n/3}u[n]$ (vi) $(-1)^nu[n]$ (vii) $\cos(\tfrac{n}{3})u[n]$

> [!success]- Solution
> $1-z^{-1}+z^{-2}$ has roots $z=\tfrac12\pm j\tfrac{\sqrt3}{2} = e^{\pm j\pi/3}$ (the same quadratic as Lecture 8, Exercise 2). Poles: $\tfrac13$, $e^{j\pi/3}$, $e^{-j\pi/3}$; causal ROC $\lvert z\rvert>1$: **marginally stable**. Only inputs with a pole at $e^{\pm j\pi/3}$ are dangerous.
>
> | input | its poles | match? | unbounded? |
> |---|---|---|---|
> | (i) $\delta[n]$ | none | – | **F** ($h$ is a bounded oscillation) |
> | (ii) $(\frac13)^nu[n]$ | $\frac13$ | double pole at $\frac13$, inside | **F** ($n(\frac13)^n\to0$) |
> | (iii) $\cos(\frac{\pi}{3}n)u[n]$ | $e^{\pm j\pi/3}$ | both | **T** |
> | (iv) $\sin(\frac{2\pi}{3}n)u[n]$ | $e^{\pm j2\pi/3}$ | no ($120°\neq60°$) | **F** |
> | (v) $e^{j5\pi n/3}u[n]$ | $e^{j5\pi/3}=e^{-j\pi/3}$ | yes | **T** |
> | (vi) $(-1)^nu[n]$ | $-1$ | no | **F** |
> | (vii) $\cos(\frac{n}{3})u[n]$ | $e^{\pm j/3}$ (angle $\frac13$ rad) | no | **F** |
>
> In (iii) and (v) $Y(z)$ has a double pole on the unit circle, and the output grows like $n$. (vii) is the FA2025 trap turned around: $\tfrac13$ rad is not $\tfrac{\pi}{3}$.

The resonance is easy to see numerically: the peak of $\lvert y\rvert$ grows in proportion to the length of the record for (iii) and stays put for (vii).

```python
import numpy as np
from scipy.signal import lfilter

a = np.convolve([1, -1/3], [1, -1, 1])       # Practice 1: poles 1/3 and e^{+-j pi/3}, causal
n = np.arange(3000)
for name, x in [("cos(pi n/3)", np.cos(np.pi * n / 3)),    # matches the unit-circle poles
                ("cos(n/3)   ", np.cos(n / 3))]:            # angle 1/3 rad: no match
    y = lfilter([1], a, x)
    print(name, [float(round(np.abs(y[:N]).max(), 1)) for N in (300, 1000, 3000)])
```

```text
cos(pi n/3) [192.8, 642.1, 1928.5]
cos(n/3)    [3.0, 3.0, 3.0]
```

> [!question] Practice 2 — an unstable system with a zero outside the unit circle
> A causal LTI system has $H(z) = \dfrac{1-2z^{-1}}{1+3z^{-1}}$.
> (a) Find a bounded input that produces an unbounded output. (b) Find an unbounded input that produces a bounded output. (c) Find a bounded input that produces a bounded output.
> (d) True/False, the output is **bounded**: (i) $2^nu[n]$ (ii) $(-3)^nu[n]$ (iii) $(\tfrac12)^nu[n]+3(\tfrac12)^{n-1}u[n-1]$ (iv) $\delta[n]-2\delta[n-1]$.

> [!success]- Solution
> Pole $-3$ (outside), zero $2$ (also outside); ROC $\lvert z\rvert>3$: unstable.
>
> **(a)** $x[n]=\delta[n]$: $y[n]=h[n] = (-3)^nu[n]-2(-3)^{n-1}u[n-1] = \{\underset{\uparrow}{1},\ -5,\ 15,\ -45,\dots\}$, unbounded.
>
> **(b)** Take $X(z) = 1/H(z) = \dfrac{1+3z^{-1}}{1-2z^{-1}}$, ROC $\lvert z\rvert>2$: $x[n] = 2^nu[n]+3(2)^{n-1}u[n-1] = \{\underset{\uparrow}{1},\ 5,\ 10,\ 20,\dots\}$, unbounded, and $Y(z)=1$, so $y[n]=\delta[n]$. The input's pole at 2 sits on the system's zero, and the input's zero at $-3$ sits on the system's pole.
>
> **(c)** $x[n] = \delta[n]+3\delta[n-1]$: $X = 1+3z^{-1}$ cancels the pole, $Y = 1-2z^{-1}$, $y[n] = \delta[n]-2\delta[n-1]$.
>
> **(d)**
> - (i) **F.** $Y = \dfrac{1-2z^{-1}}{(1-2z^{-1})(1+3z^{-1})} = \dfrac{1}{1+3z^{-1}}$: the zero ate the input's pole, but the system's pole survives, $y = (-3)^nu[n]$.
> - (ii) **F.** Double pole at $-3$.
> - (iii) **T.** $X = \dfrac{1+3z^{-1}}{1-\frac12z^{-1}}$ has a zero at $-3$; $Y = \dfrac{1-2z^{-1}}{1-\frac12z^{-1}}$, $y = (\tfrac12)^nu[n]-2(\tfrac12)^{n-1}u[n-1]$.
> - (iv) **F.** The zero at 2 does not touch the pole at $-3$: $Y = \dfrac{(1-2z^{-1})^2}{1+3z^{-1}}$.

> [!question] Practice 3 — a cascade with an unstable stage
> System 1 has $h_1[n] = 2^nu[n]$. System 2 is causal with $H_2(z) = \dfrac{1-2z^{-1}}{1-\frac13z^{-1}}$. They are connected in series.
> (a) True or False: the overall system is BIBO unstable, because system 1 is. (b) Let $x[n]=u[n]$ enter system 1 first. Find the signal $w[n]$ between the two systems and the final output $y[n]$.

> [!success]- Solution
> **(a) False.** $H(z) = H_1(z)H_2(z) = \dfrac{1}{1-2z^{-1}}\cdot\dfrac{1-2z^{-1}}{1-\frac13z^{-1}} = \dfrac{1}{1-\frac13z^{-1}}$. The pole at 2 is cancelled, the cascade is causal, so ROC $\lvert z\rvert>\tfrac13$ and $h[n] = (\tfrac13)^nu[n]$: stable. (Same logic as FA2019 #10d and HW4 #5.)
>
> **(b)** $w[n] = u[n]*2^nu[n] = \sum_{k=0}^{n}2^k = (2^{n+1}-1)\,u[n]$, unbounded. But
> $$
> y[n] = u[n]*\left(\tfrac13\right)^nu[n] = \frac{1-(\frac13)^{n+1}}{1-\frac13}\,u[n] = \tfrac32\left(1-\left(\tfrac13\right)^{n+1}\right)u[n],
> $$
> bounded by $\tfrac32$. With system 2 first, the middle signal stays bounded (it settles at $H_2(1) = -\tfrac32$) and the output is the same. BIBO stability is a property of the overall input–output map; a real implementation with system 1 first would still overflow internally, which is why the order matters in practice.

## Where to go next

- Concepts: [[concepts/bibo-stability|BIBO stability]], [[concepts/marginal-stability|marginal stability]], [[concepts/pole-zero-cancellation|pole–zero cancellation]], [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] (why $e^{j\omega_0n}$ is special), [[concepts/system-algebra|system algebra]].
- Lectures: [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]] (unstable inputs, marginal stability, pole matching), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (series connections).
- Related families: [[problems/parameters-for-stability|parameters for stability]] (choose a zero to cancel the bad pole), [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]], and the stability statements in the [[exams/midterm-1/true-false-bank|true/false bank]].
- Try it: [[demos/difference-equation-simulator|difference-equation simulator]] (drive a marginal system at its pole frequency and watch the envelope grow), [[demos/pole-zero-and-roc-explorer|pole–zero and ROC explorer]], [[demos/practice-drills|practice drills]].

### Sources for this page

Lecture 11 notes (§1.2 unstable inputs, §1.2.1 marginal stability) and slides 12–18 (pole matching); HW4 #3 and #5 with solutions; past midterms FA2025 #8, SP2025 #6, SP2023 #7, SP2021 #5, FA2023 #7c, FA2024 #7c–d, FA2019 #10d. Practice problems are new; every claim is checked in `verify/problems/unbounded_practice.py` (exact rational arithmetic where an unstable pole must cancel, long `lfilter` runs for resonance).
