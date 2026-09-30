---
title: "Complex numbers"
description: "Rectangular and polar form, Euler's formula, conjugates, magnitude and angle, roots of z^N = a, and turning sums of complex exponentials into cosines — the complex arithmetic that every ECE 310 z-transform, PFE and stability problem runs on."
tags: [toolkit, complex-numbers]
---

*Toolkit · reference page · Lecture 2 notes §1 and HW1 #4, plus every place the exams lean on it*

No calculator on the exam, so every angle has to come from a sketch and every magnitude from $\sqrt{a^2+b^2}$. What follows is the minimum that makes pole locations, $|a^n|$ and complex-conjugate PFE terms automatic.

## Two forms and how to switch

$x = a + jb = Re^{j\theta}$ with $j=\sqrt{-1}$. Euler's formula $Re^{j\theta} = R(\cos\theta + j\sin\theta)$ converts polar to rectangular; magnitude and angle go the other way.

| quantity | from $a+jb$ | from $Re^{j\theta}$ |
|---|---|---|
| real part $\mathrm{Re}\{x\}$ | $a$ | $R\cos\theta$ |
| imaginary part $\mathrm{Im}\{x\}$ | $b$ | $R\sin\theta$ |
| magnitude $\lvert x\rvert$ | $\sqrt{a^2+b^2} = \sqrt{xx^*}$ | $R$ |
| angle $\angle x$ | $\tan^{-1}(b/a)$, then fix the quadrant | $\theta$ (any $\theta + 2\pi k$) |
| conjugate $x^*$ | $a - jb$ | $Re^{-j\theta}$ |

Quadrant rule (Lecture 2, Eq. 12): $\angle x = \tan^{-1}(b/a)$ if $a \ge 0$; add $\pi$ if $a<0,\ b\ge 0$; subtract $\pi$ if $a<0,\ b<0$. This is `np.angle` (atan2).

> [!trap] Sketch the point before you write its angle
> $-1-j$: $\tan^{-1}(1) = \pi/4$, but the point is in the third quadrant, so $\angle(-1-j) = \pi/4 - \pi = -3\pi/4$ and $-1-j = \sqrt2\,e^{-j3\pi/4}$. Likewise $-\sqrt3 + j = 2e^{j5\pi/6}$, not $2e^{-j\pi/6}$.

## Arithmetic

- **Add, subtract:** rectangular, part by part.
- **Multiply, divide:** polar — multiply (divide) magnitudes, add (subtract) angles: $2e^{j\pi/3}\cdot 4e^{-j\pi/6} = 8e^{j\pi/6}$ and $2e^{j\pi/3}/(4e^{-j\pi/6}) = \tfrac12 e^{j\pi/2} = j/2$.
- **Divide in rectangular:** multiply top and bottom by the conjugate of the bottom (Lecture 2): $\dfrac{1+j2}{3-j} = \dfrac{(1+j2)(3+j)}{(3-j)(3+j)} = \dfrac{1+j7}{10}$.
- **Conjugates:** $xx^* = \lvert x\rvert^2$, $\mathrm{Re}\{x\} = \tfrac12(x+x^*)$, $\mathrm{Im}\{x\} = \tfrac{1}{2j}(x-x^*)$ — note the $j$ (the Lecture 7 property table drops it, see [[0-toolkit/05-errata|errata]]).
- **Powers:** $(Re^{j\theta})^n = R^n e^{jn\theta}$, so $\lvert a^n\rvert = \lvert a\rvert^n$. That single fact decides whether $a^n u[n]$ decays ($\lvert a\rvert<1$), stays bounded ($\lvert a\rvert = 1$) or blows up ($\lvert a\rvert>1$) — the whole of [[concepts/bibo-stability|BIBO stability]] for causal systems.

> [!exam] SP2021 #3, third row: $y[n] = (0.8+0.8j)^n x[n]$
> $\lvert 0.8+0.8j\rvert = 0.8\sqrt2 \approx 1.13 > 1$, so the multiplier grows like $1.13^n$ and a bounded input can produce an unbounded output: **not stable** (it is linear, not shift-invariant, causal). See [[0-midterm-1/past-exams/spring-2021|SP2021]] and [[problems/classifying-system-properties|classifying system properties]].

## $e^{j\theta}$ lives on the unit circle

$\lvert e^{j\theta}\rvert = 1$ for every real $\theta$. Values to know cold:

| $\theta$ | $0$ | $\pi/2$ | $\pi$ | $-\pi/2$ | $\pi/4$ | $2\pi k$ |
|---|---|---|---|---|---|---|
| $e^{j\theta}$ | $1$ | $j$ | $-1$ | $-j$ | $(1+j)/\sqrt2$ | $1$ |

So $j^n = e^{j\pi n/2}$ cycles $1, j, -1, -j$ (period 4) and $(-1)^n = e^{j\pi n} = \cos(\pi n)$. Angles are only defined modulo $2\pi$: add or subtract $2\pi$ until you reach the principal range, e.g. $e^{j\pi/3} = e^{j7\pi/3}$ (Lecture 2) and $e^{-j4\pi/3} = e^{j2\pi/3}$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #5a]]).

> [!trap] $e^{j2/3}$ is not $e^{j2\pi/3}$
> [[0-midterm-1/past-exams/fall-2025|FA2025 #8(b)]] puts a pole at $e^{j2/3}$: angle $2/3$ rad $\approx 38^\circ$. The input $\cos(\tfrac{2\pi}{3}n)u[n]$ has poles at $e^{\pm j2\pi/3}$ (angle $\approx 120^\circ$), which do **not** coincide with it, so that output stays bounded (key: False). Read exponents literally — see [[problems/unbounded-outputs-and-pole-matching|pole matching]].

## Solving $z^N = a$

> [!recipe] N-th roots
> 1. Write $a$ in polar form **with the $2\pi k$**: $a = Re^{j(\theta_p + 2\pi k)}$, $k\in\mathbb Z$.
> 2. Take the $N$-th root: $z_k = R^{1/N} e^{j(\theta_p + 2\pi k)/N}$.
> 3. $k = 0,1,\dots,N-1$ gives $N$ distinct points, equally spaced by $2\pi/N$ on the circle of radius $R^{1/N}$; other $k$ repeat them. They sum to zero for $N\ge2$ — a quick check.

<figure class="ece-fig"><svg viewBox="0 0 340 260" width="340" role="img" aria-label="Roots of z^4 = 1 and z^4 = -1 on the unit circle"><line x1="15" y1="130" x2="245" y2="130" stroke="currentColor" stroke-width="1" opacity="0.6"/><line x1="130" y1="245" x2="130" y2="15" stroke="currentColor" stroke-width="1" opacity="0.6"/><text x="248" y="134" font-size="12" fill="currentColor">Re</text><text x="135" y="12" font-size="12" fill="currentColor">Im</text><circle cx="130" cy="130" r="90" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="220.0" cy="130.0" r="5.5" fill="var(--accent)"/><circle cx="130.0" cy="40.0" r="5.5" fill="var(--accent)"/><circle cx="40.0" cy="130.0" r="5.5" fill="var(--accent)"/><circle cx="130.0" cy="220.0" r="5.5" fill="var(--accent)"/><text x="228.0" y="122.0" font-size="12" fill="var(--accent)">1</text><text x="138.0" y="34.0" font-size="12" fill="var(--accent)">j</text><text x="16.0" y="122.0" font-size="12" fill="var(--accent)">−1</text><text x="138.0" y="236.0" font-size="12" fill="var(--accent)">−j</text><circle cx="193.6" cy="66.4" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2.2"/><circle cx="66.4" cy="66.4" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2.2"/><circle cx="66.4" cy="193.6" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2.2"/><circle cx="193.6" cy="193.6" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2.2"/><path d="M 160.0 130.0 A 30 30 0 0 0 151.2 108.8" fill="none" stroke="var(--accent2)" stroke-width="1.2"/><text x="164" y="121" font-size="11" fill="var(--accent2)">π/4</text><line x1="130" y1="130" x2="193.6" y2="66.4" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 2"/><text x="201.6" y="62.4" font-size="11" fill="var(--accent2)">(1+j)/√2</text><circle cx="245" cy="200" r="5" fill="var(--accent)"/><text x="255" y="204" font-size="12" fill="currentColor">z⁴ = 1</text><circle cx="245" cy="222" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="255" y="226" font-size="12" fill="currentColor">z⁴ = −1</text><text x="8" y="244" font-size="11" fill="var(--muted)">unit circle |z| = 1</text></svg><figcaption><b>The four fourth roots of 1 and of −1.</b> Both sets sit on the unit circle (|a| = 1, so the radius is 1<sup>1/4</sup> = 1), spaced 2π/4 = π/2 apart; the roots of z⁴ = −1 are the roots of z⁴ = 1 rotated by π/4 (HW1 #4).</figcaption></figure>

> [!question] HW1 #4: solve (a) $z^4 - 1 = 0$, (b) $z^4 + 1 = 0$, and plot the roots.

> [!success]- Answers
> (a) $z^4 = 1 = e^{j2\pi k}$, so $z = e^{j\pi k/2}$: $\ 1,\ j,\ -1,\ -j$.
>
> (b) $z^4 = -1 = e^{j(\pi + 2\pi k)}$, so $z = e^{j(\pi/4 + \pi k/2)}$: $\ \tfrac{1+j}{\sqrt2},\ \tfrac{-1+j}{\sqrt2},\ \tfrac{-1-j}{\sqrt2},\ \tfrac{1-j}{\sqrt2}$. The official key writes $e^{j(-\pi/4 + \pi k/2)}$ (it started from $-1 = e^{-j\pi}$): the same four points.
>
> One more for practice: $z^3 = -8j = 8e^{-j\pi/2}$ gives $z = 2e^{j(-\pi/6 + 2\pi k/3)}$, i.e. $2e^{-j\pi/6},\ 2j,\ 2e^{-j5\pi/6}$.

Where it shows up: the poles of $1/(1 - c\,z^{-N})$ are the $N$-th roots of $c$. In [[0-midterm-1/past-exams/spring-2021|SP2021 #6]], $H(z) = \dfrac{-1+z^{-3}}{1-2z^{-3}}$ has poles at $z^3 = 2$, i.e. $2^{1/3}e^{j2\pi k/3}$, all with $\lvert p\rvert = 2^{1/3}\approx 1.26 > 1$, so the causal system is unstable.

## Sums of exponentials ↔ cosines and sines

Euler's identities (Lecture 2, Eqs. 17 and 20):

$$
\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2},\qquad \sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}.
$$

- **Forward, for z-transforms:** split, then transform each exponential as a geometric series: $\cos(\omega_0 n)u[n] = \tfrac12 e^{j\omega_0 n}u[n] + \tfrac12 e^{-j\omega_0 n}u[n] \;\to\; \dfrac{1/2}{1-e^{j\omega_0}z^{-1}} + \dfrac{1/2}{1-e^{-j\omega_0}z^{-1}}$, ROC $\lvert z\rvert>1$ (combine over a common denominator to get [[supplements/transform-tables|table pair 9]]).
- **Backward, after a PFE with complex poles:** the two terms are conjugates, and

$$
A\,p^n + A^*(p^*)^n = 2\,\mathrm{Re}\{A p^n\} = 2\lvert A\rvert\,\lvert p\rvert^n\cos(\angle p\cdot n + \angle A).
$$

> [!example] SP2021 #5: $H(z) = \dfrac{3z^{-1}}{1+z^{-2}}$, ROC $\lvert z\rvert>1$
> Factor $1+z^{-2} = (1-jz^{-1})(1+jz^{-1})$. Cover-up at $p=j$: $A = \Big[\dfrac{3z^{-1}}{1+jz^{-1}}\Big]_{z=j} = \dfrac{3(-j)}{2} = -\dfrac{3j}{2}$; the residue at $p=-j$ is its conjugate $\tfrac{3j}{2}$. With $2\lvert A\rvert = 3$ and $\angle A = -\pi/2$:
> $$
> h[n] = 3\cos\!\big(\tfrac{\pi}{2}n - \tfrac{\pi}{2}\big)u[n] = 3\sin\!\big(\tfrac{\pi}{2}n\big)u[n].
> $$
> Poles on the unit circle: bounded $h$, but not absolutely summable — [[concepts/marginal-stability|marginally stable]], i.e. not BIBO stable.

## Squares and products of cosines

$$
\begin{gathered}
\cos^2\theta = \tfrac12 + \tfrac14 e^{j2\theta} + \tfrac14 e^{-j2\theta},\qquad
\sin^2\theta = \tfrac12 - \tfrac14 e^{j2\theta} - \tfrac14 e^{-j2\theta},\\[4pt]
\cos A\cos B = \tfrac12\big[\cos(A-B)+\cos(A+B)\big].
\end{gathered}
$$

> [!exam] FA2025 #5(c): z-transform of $\cos^2(\tfrac{\pi}{4}n)u[n]$
> $\cos^2(\tfrac{\pi}{4}n) = \tfrac12 + \tfrac14 e^{j\pi n/2} + \tfrac14 e^{-j\pi n/2}$ (samples $1, \tfrac12, 0, \tfrac12, 1, \dots$), so
> $$
> X(z) = \frac{1/2}{1-z^{-1}} + \frac{1/4}{1-jz^{-1}} + \frac{1/4}{1+jz^{-1}},\qquad \text{ROC: } \lvert z\rvert > 1.
> $$
> Three poles on the unit circle ($1, j, -j$). See [[0-midterm-1/past-exams/fall-2025|FA2025]] and [[problems/z-transform-with-roc|z-transform with ROC]].

## Python check

```python
import numpy as np
z = -1 - 1j
print(abs(z), np.angle(z) / np.pi)       # magnitude, angle in units of pi
r = np.roots([1, 0, 0, 0, 1])            # z^4 + 1 = 0
print(np.round(r, 4))
print(np.angle(r) / np.pi)               # angles in units of pi
print(abs(0.8 + 0.8j))                   # SP2021: |0.8+0.8j| > 1
```

```text
1.4142135623730951 -0.75
[-0.7071+0.7071j -0.7071-0.7071j  0.7071+0.7071j  0.7071-0.7071j]
[ 0.75 -0.75  0.25 -0.25]
1.131370849898476
```

## Related

[[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/partial-fraction-expansion|partial fraction expansion]] · [[concepts/marginal-stability|marginal stability]] · [[homework/hw1|HW1]] · [[0-toolkit/02-geometric-series|geometric series]] · Singer & Munson, Appendix A (PDF pp. 304–313) in the [[supplements/singer-munson-notes|reading guide]].

### Sources for this page

Lecture 2 notes §1.1–1.4 (forms, quadrant rule, Euler's identities, principal angle, the $(1+j2)/(3-j)$ example); HW1 #4 and its solution; SP2021 #3, #5, #6; FA2025 #5(a), #5(c), #8(b). Every number is checked in `verify/hub/toolkit_complex.py`.
