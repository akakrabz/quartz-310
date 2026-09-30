---
title: "Lecture 2 — Complex numbers and elementary signals"
description: "Rectangular and polar form, magnitude and phase with the quadrant rule, conjugates, multiplication and division, Euler's formula and identities, principal angles; roots of unity and geometric sums for the z-transform; and the elementary sequences δ[n], u[n], sinusoids and (complex) exponentials."
tags: [lecture, midterm-1, complex-numbers, signals]
lecture: 2
---

*Lecture 2 · Wed Aug 26, 2026 · notes + slides "Math preliminaries, complex numbers" · prev: [[1-signals-and-systems/01-digital-signals|Lecture 1]] · next: [[1-signals-and-systems/03-system-properties|Lecture 3]]*

> [!abstract] In one breath
> A complex number is a point in the plane: $x = a + jb$ (rectangular) or $x = Re^{j\theta}$ (polar). Add in rectangular form, multiply and divide in polar form, and move between them with Euler's formula $e^{j\theta} = \cos\theta + j\sin\theta$. Phase needs the quadrant rule (a calculator's $\tan^{-1}(b/a)$ is wrong in the left half-plane), and angles are only defined up to multiples of $2\pi$. Euler's identities $\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}$, $\sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$ turn every sinusoid into complex exponentials, which is how the z-transform handles them. The lecture ends with the vocabulary of signals: the $n = 0$ marker, $\delta[n]$, $u[n]$, sinusoids $A\sin(\omega_0 n + \theta)$ and exponentials $Ba^n$. Roots of unity (HW1 #4) and geometric sums are added here because every later lecture uses them.

## 1. Rectangular form and the complex plane

A complex number $x \in \mathbb{C}$ in **rectangular form** is

$$
x = a + jb, \qquad a = \operatorname{Re}\{x\},\quad b = \operatorname{Im}\{x\},\quad j = \sqrt{-1}.
$$

(ECE uses $j$; math texts use $i$.) The **complex conjugate** flips the sign of the imaginary part, $x^* = a - jb$, and $x\,x^* = a^2 + b^2$ is always real. Arithmetic in rectangular form:

- add and subtract real and imaginary parts separately;
- multiply out every pair of terms and use $j^2 = -1$;
- divide by multiplying top and bottom by the conjugate of the denominator, which makes the denominator real (notes):

$$
\frac{1 + j2}{3 - j} = \frac{(1+j2)(3+j)}{(3-j)(3+j)} = \frac{1 + j7}{10}.
$$

Plot $x$ on the **complex plane** (real part horizontal, imaginary part vertical); $x^*$ is its mirror image across the real axis (figure below).

## 2. Polar form, magnitude and phase

The **polar form** writes the same point by its length and angle:

$$
x = R\,e^{j\theta}, \qquad x^* = R\,e^{-j\theta}.
$$

Multiplication and division are one line each in polar form: for $x = Re^{j\theta}$, $y = Se^{j\phi}$,

$$
xy = RS\,e^{j(\theta+\phi)}, \qquad \frac{x}{y} = \frac{R}{S}\,e^{j(\theta-\phi)} .
$$

> [!key] Magnitude and phase of $x = a + jb = Re^{j\theta}$
> $$
> \begin{gathered}
> \lvert x\rvert = \sqrt{a^2 + b^2} = \sqrt{x\,x^*} = R \ge 0, \\[4pt]
> \angle x = \theta =
> \begin{cases}
> \tan^{-1}\!\left(\frac{b}{a}\right), & a \ge 0\\[4pt]
> \tan^{-1}\!\left(\frac{b}{a}\right) + \pi, & a < 0,\ b \ge 0\\[4pt]
> \tan^{-1}\!\left(\frac{b}{a}\right) - \pi, & a < 0,\ b < 0
> \end{cases}
> \quad \in [-\pi, \pi].
> \end{gathered}
> $$
> Real numbers have phase $0$ (positive) or $\pm\pi$ (negative).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" height="300" role="img" aria-label="Complex plane: x = -4 + j3 with magnitude and phase, its conjugate, and the 8th roots of unity" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><line x1="40.0" y1="150.0" x2="338.0" y2="150.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="344.0,150.0 338.0,146.7 338.0,153.3" fill="currentColor"/><line x1="190.0" y1="270.0" x2="190.0" y2="32.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="190.0,26.0 186.7,32.0 193.3,32.0" fill="currentColor"/><text x="342.0" y="168.0" text-anchor="end" fill="currentColor" style="font-size:12px;">Re</text><text x="198.0" y="36.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Im</text><line x1="86.0" y1="147.0" x2="86.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="86.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−4</text><line x1="138.0" y1="147.0" x2="138.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="138.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">−2</text><line x1="242.0" y1="147.0" x2="242.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="242.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">2</text><line x1="294.0" y1="147.0" x2="294.0" y2="153.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="294.0" y="166.0" text-anchor="middle" fill="currentColor" style="font-size:11px;" opacity="0.8">4</text><line x1="187.0" y1="228.0" x2="193.0" y2="228.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="198.0" y="232.0" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">−3j</text><line x1="187.0" y1="72.0" x2="193.0" y2="72.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="198.0" y="76.0" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">3j</text><line x1="86.0" y1="72.0" x2="86.0" y2="150.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="86.0" y1="72.0" x2="190.0" y2="72.0" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" stroke-linecap="round"/><line x1="190.0" y1="150.0" x2="86.0" y2="72.0" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/><circle cx="86.0" cy="72.0" r="5.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="190.0" y1="150.0" x2="86.0" y2="228.0" stroke="var(--accent2)" stroke-width="1.6" stroke-dasharray="6 4" stroke-linecap="round"/><circle cx="86.0" cy="228.0" r="4.6" fill="none" stroke="var(--accent2)" stroke-width="1.8"/><text x="78.0" y="62.0" text-anchor="middle" fill="var(--accent)" style="font-size:13.5px;font-weight:600;">x = −4 + j3</text><text x="80.0" y="248.0" text-anchor="middle" fill="var(--accent2)" style="font-size:13px;font-weight:600;">x* = −4 − j3</text><text x="152.0" y="103.0" text-anchor="start" fill="var(--accent)" style="font-size:13px;">R = 5</text><path d="M220,150 A30,30 0 0 0 166.0,132.0" fill="none" stroke="currentColor" stroke-width="1.3"/><text x="220.0" y="116.0" text-anchor="start" fill="currentColor" style="font-size:12px;">θ ≈ 2.50 rad (143°)</text><text x="40.0" y="22" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600">rectangular a + jb  ↔  polar Re<tspan dy="-6" style="font-size:10px">jθ</tspan></text><line x1="382.0" y1="156.0" x2="616.0" y2="156.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="622.0,156.0 616.0,152.7 616.0,159.3" fill="currentColor"/><line x1="500.0" y1="272.0" x2="500.0" y2="42.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="500.0,36.0 496.7,42.0 503.3,42.0" fill="currentColor"/><text x="620.0" y="174.0" text-anchor="end" fill="currentColor" style="font-size:12px;">Re</text><text x="508.0" y="46.0" text-anchor="start" fill="currentColor" style="font-size:12px;">Im</text><circle cx="500.0" cy="156.0" r="86.0" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.7"/><circle cx="586.0" cy="156.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="560.8" y2="95.2" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="560.8" cy="95.2" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="500.0" cy="70.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="439.2" y2="95.2" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="439.2" cy="95.2" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="414.0" cy="156.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="439.2" y2="216.8" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="439.2" cy="216.8" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="500.0" cy="242.0" r="6.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="500.0" y1="156.0" x2="560.8" y2="216.8" stroke="var(--accent2)" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" stroke-linecap="round"/><circle cx="560.8" cy="216.8" r="5.5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="596.0" y="148.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">1</text><text x="510.0" y="66.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">j</text><text x="402.0" y="148.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">−1</text><text x="510.0" y="258.0" text-anchor="start" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;font-weight:600;">−j</text><path d="M534,156 A34,34 0 0 0 524.0,132.0" fill="none" stroke="currentColor" stroke-width="1.2"/><text x="540.0" y="146.0" text-anchor="start" fill="currentColor" style="font-size:11.5px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">π/4</text><text x="382.0" y="22" text-anchor="start" fill="currentColor" style="font-size:13px;font-weight:600">8th roots of unity e<tspan dy="-6" style="font-size:10px">j2πk/8</tspan></text><circle cx="388.0" cy="280.0" r="5.5" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="398.0" y="284.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">z⁴ = 1</text><circle cx="506.0" cy="280.0" r="5.0" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="516.0" y="284.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">z⁴ = −1  (HW1 #4)</text></svg><figcaption><strong>Left: one complex number, two descriptions.</strong> x = −4 + j3 sits 4 to the left and 3 up; in polar form it is 5e<sup>jθ</sup> with θ = tan⁻¹(3/(−4)) + π ≈ 2.50 rad, because the point is in the second quadrant. Its conjugate x* mirrors it across the real axis (same R, angle −θ). <strong>Right: roots of unity.</strong> The solutions of z⁸ = 1 are 8 equally spaced points on the unit circle. Every other one solves z⁴ = 1 (1, j, −1, −j); the ones in between, rotated by π/4, solve z⁴ = −1: (±1 ± j)/√2.</figcaption></figure>

> [!question] Slides: magnitude and phase of (a) $x = -4 + j3$, (b) $y = j2$, and the special case $x = -3.10$.

> [!success]- Answers (annotated slides)
> (a) $\lvert x\rvert = \sqrt{16 + 9} = 5$; $a < 0$, $b \ge 0$, so $\angle x = \tan^{-1}\!\big(\tfrac{3}{-4}\big) + \pi = \pi - \tan^{-1}\tfrac34 \approx 2.50$ rad $\approx 143.1°$. So $x = 5e^{j2.50}$.
> (b) $\lvert y\rvert = 2$, $\angle y = \tfrac{\pi}{2}$: $y = 2e^{j\pi/2}$.
> Special case: $-3.10 = 3.10\,e^{j\pi}$ (or $e^{-j\pi}$): magnitude $3.10$, phase $\pm\pi$. A negative real number is *not* "magnitude $-3.10$".

> [!trap] $\tan^{-1}(b/a)$ alone loses the quadrant
> $-4 + j3$ and $4 - j3$ have the same ratio $b/a = -\tfrac34$, but their phases are $2.50$ rad and $-0.64$ rad. Always sketch the point first; the case formula (or `numpy.angle`) adds the missing $\pm\pi$.

**Principal angle.** Adding a full turn does not move the point: $Re^{j\theta} = Re^{j(\theta_p + 2\pi k)}$ for every integer $k$. For example $e^{j\pi/3}$ and $e^{j7\pi/3}$ are the same number; the **principal angle** is the representative in $[-\pi, \pi]$ (or $[0, 2\pi)$, conventions vary), here $\theta_p = \pi/3$.

## 3. Euler's formula and identities

> [!key] Euler
> $$
> e^{j\theta} = \cos\theta + j\sin\theta, \qquad Re^{j\theta} = R\cos\theta + jR\sin\theta \quad(\text{polar} \to \text{rectangular}).
> $$
> $$
> e^{\pm j\pi} = -1, \qquad \cos\theta = \frac{e^{j\theta} + e^{-j\theta}}{2}, \qquad \sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2j}.
> $$

> [!derivation]- Where the identities come from
> Add and subtract Euler's formula at $\theta$ and at $-\theta$, using $\cos(-\theta) = \cos\theta$ (even) and $\sin(-\theta) = -\sin\theta$ (odd):
> $$
> e^{j\theta} + e^{-j\theta} = 2\cos\theta, \qquad e^{j\theta} - e^{-j\theta} = 2j\sin\theta .
> $$

> [!question] Slides: simplify into rectangular and polar form (a) $j2 + \sqrt2\,e^{-j\pi/4}$, (b) $\dfrac{j3}{1-j}$.

> [!success]- Answers
> (a) Euler on the second term: $\sqrt2\,e^{-j\pi/4} = \sqrt2\big(\tfrac{\sqrt2}{2} - j\tfrac{\sqrt2}{2}\big) = 1 - j$, so the sum is $1 + j = \sqrt2\,e^{j\pi/4}$. (Addition: go rectangular.)
> (b) Polar is faster for a quotient: $\lvert j3\rvert / \lvert 1-j\rvert = 3/\sqrt2$ and $\angle = \tfrac{\pi}{2} - \big(-\tfrac{\pi}{4}\big) = \tfrac{3\pi}{4}$, so $\dfrac{j3}{1-j} = \dfrac{3}{\sqrt2}\,e^{j3\pi/4} = -\dfrac32 + j\dfrac32$. Check by the conjugate trick: $\dfrac{j3(1+j)}{2} = \dfrac{-3 + j3}{2}$ ✓.

In NumPy, `abs` and `np.angle` do the quadrant bookkeeping for you:

```python
import numpy as np
x = -4 + 3j
print(abs(x), np.angle(x), np.degrees(np.angle(x)))   # quadrant-aware phase
print(np.angle(4 - 3j))                                 # same b/a, different quadrant
z = np.roots([1, 0, 0, 0, 1])                           # z^4 + 1 = 0, i.e. z^4 = -1
print(np.round(np.abs(z), 12), np.round(np.angle(z) / np.pi, 12))   # angles in units of pi
```

```text
5.0 2.498091544796509 143.13010235415598
-0.6435011087932844
[1. 1. 1. 1.] [ 0.75 -0.75  0.25 -0.25]
```

## 4. Two tools the z-transform will need

These are not on the Lecture 2 slides, but [[homework/hw1|HW1]] #4 asks for the first and [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] onward uses the second constantly. More practice: [[0-toolkit/01-complex-numbers|complex-number toolkit]] and [[0-toolkit/02-geometric-series|geometric series]].

> [!recipe] Solving $z^N = c$ (roots of unity and friends)
> 1. Write the right side in polar form **with the $2\pi k$ ambiguity**: $c = \lvert c\rvert\,e^{j(\arg c + 2\pi k)}$.
> 2. Take the $N$-th root: $z_k = \lvert c\rvert^{1/N}\,e^{j(\arg c + 2\pi k)/N}$, $k = 0, 1, \dots, N-1$.
> 3. The $N$ roots are equally spaced by $2\pi/N$ on a circle of radius $\lvert c\rvert^{1/N}$.
>
> $z^N = 1$ gives the **$N$-th roots of unity** $e^{j2\pi k/N}$. HW1 #4: $z^4 = 1$ gives $1, j, -1, -j$; $z^4 = -1 = e^{j(\pi + 2\pi k)}$ gives $e^{j(\pi/4 + \pi k/2)} = \dfrac{\pm1 \pm j}{\sqrt2}$ (figure above).

Where roots show up later: the poles of $y[n] = y[n-3] + x[n]$ are the three cube roots of unity ([[0-midterm-1/past-exams/fall-2024|FA2024 #1(e)]], "three distinct poles": True); $1 + z^{-2} = (1 - jz^{-1})(1 + jz^{-1})$ puts poles at $\pm j$ ([[0-midterm-1/past-exams/spring-2021|SP2021 #5]]).

> [!key] Geometric sums
> $$
> \begin{gathered}
> \sum_{k=0}^{N-1} a^k = \frac{1 - a^N}{1 - a}\ \ (a \ne 1;\ \text{the sum is } N \text{ if } a = 1), \\[4pt]
> \sum_{k=0}^{\infty} a^k = \frac{1}{1 - a}\ \ (\lvert a\rvert < 1).
> \end{gathered}
> $$
> $a$ may be complex. With $a = e^{j2\pi/N}$ (so $a^N = 1$) the first formula shows that the $N$-th roots of unity **sum to zero**.

## 5. Elementary discrete-time signals

**Where is $n = 0$?** A list of numbers is not a signal until you say where it starts. The slides' example $x[n] = \{1, \underset{\uparrow}{4}, -2, 0, 3, 1, 2\}$ can also be written $\{x[n]\}_{n=-1}^{5}$: $x[-1] = 1$, $x[0] = 4$, $x[5] = 2$. This site always puts an arrow under the $n = 0$ sample.

> [!key] The two building blocks
> $$
> \delta[n] = \begin{cases} 1, & n = 0\\ 0, & n \ne 0\end{cases} \qquad\qquad
> u[n] = \begin{cases} 1, & n \ge 0\\ 0, & n < 0\end{cases}
> $$
> $\delta[n]$ is the **Kronecker delta** (unit impulse, unit pulse): an ordinary sequence with one sample equal to 1. It is *not* the Dirac delta of ECE 210, which has no finite value at $0$. They are related by $\delta[n] = u[n] - u[n-1]$ and $u[n] = \sum_{k=0}^{\infty}\delta[n-k]$ (used in [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] for step responses).

Both can be scaled, shifted and flipped: $3\delta[n-10]$ is $3$ at $n = 10$ only; $4u[3-n]$ is $4$ for $n \le 3$ and $0$ for $n > 3$. The rules for shifting and flipping are on the [[1-signals-and-systems/01-digital-signals|Lecture 1 page]].

> [!question] Slides: sketch $x[n] = -2\delta[n+3]$ and $u[3-n]$; write $x[n] = \{2, 0, \underset{\uparrow}{3}, -1, -4\}$ in terms of $\delta[n]$.

> [!success]- Answers (annotated slides)
> $-2\delta[n+3]$ is $-2$ at $n = -3$ and zero elsewhere (the sample sits where the argument is zero). $u[3-n]$ is $1$ for $n \le 3$: a step that runs to the left, ending at $n = 3$. And $x[n] = 2\delta[n+2] + 0\,\delta[n+1] + 3\delta[n] - \delta[n-1] - 4\delta[n-2]$: one scaled, shifted delta per sample, which is the idea behind convolution.

**Sinusoids** $x[n] = A\sin(\omega_0 n + \theta)$ with amplitude $A$, frequency $\omega_0$ in **radians per sample**, and phase $\theta$, all real (the notes' figure uses $\cos(\frac{\pi}{10}n - \frac{\pi}{3})$).

**Exponentials** $x[n] = B\,a^n$ with $B$ and $a$ real or complex (the notes' figure: $2(-\tfrac34)^n$, which alternates in sign and decays). Writing $a = r e^{j\omega_0}$:

$$
a^n = r^n e^{j\omega_0 n} = r^n\big(\cos(\omega_0 n) + j\sin(\omega_0 n)\big).
$$

$r < 1$ decays, $r = 1$ stays on the unit circle, $r > 1$ grows; $\omega_0$ sets how fast it turns. With $r = 1$ this is the **complex exponential** $e^{j\omega_0 n}$, and Euler's identities write every real sinusoid as a pair of them, e.g. $\cos(\omega_0 n) = \tfrac12 e^{j\omega_0 n} + \tfrac12 e^{-j\omega_0 n}$.

> [!intuition] Why these signals matter for the rest of the course
> A term $p^n u[n]$ in an impulse response is exactly a **pole** at $z = p$ in the z-domain ([[2-z-transform/06-the-z-transform|Lecture 6]]); whether $\lvert p\rvert$ is below, on or above $1$ decides decay, persistence or growth, i.e. stability ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]). And because $n$ is an integer, $e^{j(\omega_0 + 2\pi)n} = e^{j\omega_0 n}$: discrete-time frequencies, like angles, only matter modulo $2\pi$.

> [!trap] Reading angles: $2/3$ is not $2\pi/3$
> [[0-midterm-1/past-exams/fall-2025|FA2025 #8(b)]] has a pole at $e^{j2/3}$: angle $2/3$ rad $\approx 38°$, not $2\pi/3 = 120°$. An input $\cos(\tfrac{2\pi}{3}n)u[n]$ therefore does **not** hit that pole, and the output stays bounded (key: False). Read exponents character by character.

## 6. On the exam

> [!exam] Where Lecture 2 shows up
> - **Sifting T/F items** need nothing but $\delta$ and the unit circle: [[0-midterm-1/past-exams/spring-2021|SP2021 #1(e)]] ($4\cos(2\pi n + \frac{\pi}{2}) - 6\sin(\pi n) = 0$ for *every* integer $n$, so $\delta[\cdot] = 1$ everywhere and the sum is $\sum_n x[n] = 4$; the statement "$=3$" is False) and [[0-midterm-1/past-exams/fall-2019|FA2019 #1(g)]] ($2^n u[n] - 8 = 0$ only at $n = 3$, so $\sum_n x[n]\,\delta[2^n u[n] - 8] = x[3] = 4$; the statement "$x[3] = 2$" is False).
> - **Euler inside z-transforms:** [[0-midterm-1/past-exams/fall-2025|FA2025 #5(c)]] rewrites $\cos^2(\frac{\pi}{4}n)u[n] = \big(\tfrac12 + \tfrac14 e^{j\pi n/2} + \tfrac14 e^{-j\pi n/2}\big)u[n]$; [[0-midterm-1/past-exams/fall-2025|FA2025 #5(a)]] needs $e^{-j4\pi/3} = e^{j2\pi/3}$ (principal angle); [[0-midterm-1/past-exams/spring-2021|SP2021 #5]] recognizes $3\sin(\frac{\pi}{2}n)u[n]$ from poles at $\pm j$. See [[problems/z-transform-with-roc]] and [[problems/unbounded-outputs-and-pole-matching]].
> - **Roots and poles on the unit circle:** [[0-midterm-1/past-exams/fall-2024|FA2024 #1(e)]], [[0-midterm-1/past-exams/spring-2025|SP2025 #6]] (pole $e^{j\pi/4}$), [[0-midterm-1/past-exams/fall-2025|FA2025 #8(b)]] (the $e^{j2/3}$ trap above). No calculator on the exam: know $e^{j\pi/4} = \frac{1+j}{\sqrt2}$, $e^{j\pi/3} = \frac12 + j\frac{\sqrt3}{2}$, $e^{j2\pi/3} = -\frac12 + j\frac{\sqrt3}{2}$.
> - **Homework:** [[homework/hw1|HW1]] #1, #3 (sketching and rewriting with $\delta$ and $u$) and #4 (roots of $z^4 = \pm1$).

## Related

- [[concepts/complex-exponential|Complex exponential]] · [[concepts/kronecker-delta|Kronecker delta]] · [[concepts/unit-step|Unit step]] · [[concepts/discrete-time-signal|Discrete-time signal]]
- Toolkit: [[0-toolkit/01-complex-numbers|complex numbers]] · [[0-toolkit/02-geometric-series|geometric series]] · [[0-toolkit/03-sketching-and-transforming-signals|sketching and transforming signals]]

### Sources for this page
Snyder, ECE 310 Lecture 2 notes (rectangular and polar form, magnitude and phase, principal angle, Euler's identities, common signal representations) and slides "Math preliminaries, complex numbers" (Aug 26, 2026) with the annotated in-class deck (magnitude/phase and Kronecker examples; the arithmetic examples were not annotated and are worked here). HW1 #1, #3–4. Past Midterm 1 items as cited. Every number on this page is checked in `verify/lectures/l2_complex.py`.
