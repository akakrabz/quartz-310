---
title: "Spring 2021 · Midterm 1"
description: "ECE 310 Spring 2021 Midterm 1 (Moon, Katselis, Shomorony) with folded solutions and traps: T/F, convolution, property table, Z{(n+1)x[n]}, resonant inputs, h from a recursion (key erratum), two-sided input with H = Y/X."
tags: [exam, midterm-1]
---

*Thu Mar 11, 2021 · 7:00–8:50 pm, online (photos to Gradescope) · Profs. Moon, Katselis, Shomorony · 7 problems, 100 points, no DTFT · one handwritten two-sided sheet · closed forms. Handwritten key.*

## Map of the exam

| # | pts | what it asks | problem family | lectures |
|---|---|---|---|---|
| 1 | 15 | True/False: stability with no ROC given, poles of a sum, cascade of unstable systems, a pole on the unit circle driven by $u[n]$, $\sum x[n]\,\delta[f(n)]$ | [[exams/midterm-1/true-false-bank\|True/False bank]] | [[2-z-transform/09-transfer-functions\|L9]]–[[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 2 | 10 | Finite convolution with $n=0$ bookkeeping | [[problems/finite-length-convolution\|Finite convolution]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 3 | 24 | Linear / time-invariant / causal / stable table, 3 systems | [[problems/classifying-system-properties\|Classifying properties]] · [[exams/midterm-1/system-property-bank\|bank]] | [[1-signals-and-systems/03-system-properties\|L3]] |
| 4 | 10 | z-transform and ROC of $(n+1)x[n]$ | [[problems/z-transform-with-roc\|z-transform with ROC]] | [[2-z-transform/07-z-transform-properties\|L7]] |
| 5 | 12 | $h[n] = A\sin(\omega_0 n+\theta)u[n]$ from $H(z)$; a bounded input with an unbounded output | [[problems/all-possible-rocs\|Inverse z]] · [[problems/unbounded-outputs-and-pole-matching\|Pole matching]] | [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 6 | 8 | Impulse-response values from $y[n] = 2y[n-3] - x[n] + x[n-3]$ | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z)]] | [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5]], [[2-z-transform/09-transfer-functions\|L9]] |
| 7 | 21 | $X(z)$ of a two-sided input; $H = Y/X$; ROC of $Y$; $h$ by PFE; stability | [[problems/finding-h-from-input-output-pairs\|Finding H]] · [[problems/all-possible-rocs\|PFE and ROCs]] | [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/09-transfer-functions\|L9]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |

## Problem 1 · True/False (15 pts)

> [!question] Problem 1 (15 pts)
> Answer **True** or **False** to each of the following statements:
> - **(a)** An LTI system with transfer function $H(z) = \dfrac{1-z^{-1}}{1-2z^{-1}}$ cannot be stable.
> - **(b)** Let $X_1(z)$, $X_2(z)$ be the rational z-transforms of $x_1[n]$, $x_2[n]$. Then the poles of $X_1(z)$ and $X_2(z)$ must be poles of the z-transform of $x[n] = x_1[n] + x_2[n]$.
> - **(c)** Cascade of two BIBO *unstable* LTI systems cannot be stable.
> - **(d)** A causal LTI system with transfer function $H(z) = \dfrac{z^{-1}}{1-z^{-1}}$ produces an unbounded output for input $x[n] = u[n]$.
> - **(e)** Suppose $\sum_{n=-\infty}^{\infty} x[n]\,\delta\!\left[4\cos(2n\pi + \tfrac{\pi}{2}) - 6\sin(n\pi)\right] = 4$. Then, $\sum_{n=-\infty}^{\infty} x[n] = 3$.

> [!success]- Solution
> - **(a) False.** No ROC given: $\lvert z\rvert < 2$ (anti-causal) is stable.
> - **(b) False.** Poles can cancel (key: "possible pole–zero cancellation"): $x_1 = (\frac12)^n u[n]$, $x_2 = \delta[n] - (\frac12)^n u[n]$, $X_1 + X_2 = 1$.
> - **(c) False.** $H_1 = \frac{1-2z^{-1}}{1-3z^{-1}}$, $H_2 = \frac{1-3z^{-1}}{1-2z^{-1}}$ (causal, unstable), $H_1H_2 = 1$.
> - **(d) True.** $Y = \dfrac{z^{-1}}{(1-z^{-1})^2}$, $y[n] = n\,u[n]$.
> - **(e) False.** The delta's argument is 0 for all $n$: $\sum x[n] = 4$.
>
> [[exams/midterm-1/true-false-bank|T/F bank]] Q37, Q31, Q25, Q20, Q42.

> [!trap]
> "Cannot be stable" without an ROC is False unless a pole is on $\lvert z\rvert = 1$.

## Problem 2 · Finite convolution (10 pts)

> [!question] Problem 2 (10 pts)
> Calculate the result of the following convolution: $\{\underset{\uparrow}{-1}, -2, 3, -3, 2, 1\} * \{-1, \underset{\uparrow}{0}, 1\}$.

> [!success]- Solution
> $y$ starts at $n = -1$, 8 samples; $h = -\delta[n+1] + \delta[n-1]$, $y[n] = x[n-1] - x[n+1]$:
> $$
> y[n] = \{1,\ \underset{\uparrow}{2},\ -4,\ 1,\ 1,\ -4,\ 2,\ 1\}\quad(n = -1,\dots,6).
> $$
> (Key: matrix form, same result.) Check: $\sum y = 0 = (\sum x)(\sum h)$.

> [!trap]
> Arrow under the second entry: $y[0] = x[-1] - x[1] = 0 - (-2) = 2$.

## Problem 3 · System properties (24 pts)

> [!question] Problem 3 (24 pts)
> For each of the systems with input $x[n]$ and output $y[n]$ in the table, indicate with YES or NO whether the properties indicated apply to the system (Linear, Time-Invariant, Causal, Stable).
> - $y[n] = x[n]\cos\!\left(\tfrac{\pi}{3}(n-2)\right)$
> - $y[n] = x[3]\,x[n]$
> - $y[n] = (0.8 + 0.8j)^n\,x[n]$

> [!success]- Solution
> | system | Linear | Time-invariant | Causal | Stable |
> |---|---|---|---|---|
> | $x[n]\cos(\tfrac\pi3(n-2))$ | **Yes** | **No** | **Yes** | **Yes** |
> | $x[3]\,x[n]$ | **No** | **No** | **No** | **Yes** |
> | $(0.8+0.8j)^n\,x[n]$ | **Yes** | **No** | **Yes** | **No** |
>
> - Row 1: $n$-dependent gain, $\lvert\cos\rvert \le 1$.
> - Row 2: $2x \mapsto 4y$; stored $x[3]$; $y[0]$ needs $x[3]$; $\lvert y\rvert \le B^2$.
> - Row 3: $0.8 + 0.8j = \sqrt{1.28}\,e^{j\pi/4}$, $\sqrt{1.28} \approx 1.13 > 1$; $x = u[n]$ gives $\lvert y[n]\rvert = 1.13^n \to \infty$.

> [!trap]
> $\cos(\frac\pi3(n-2))$ is a gain, not a delay. Use $\lvert 0.8+0.8j\rvert = 0.8\sqrt2$, not 0.8. More: [[exams/midterm-1/system-property-bank|system-property bank]].

## Problem 4 · z-transform of $(n+1)x[n]$ (10 pts)

> [!question] Problem 4 (10 pts)
> Given the z-transform pair $x[n] \leftrightarrow X(z) = 1/(1 - 0.5z^{-1})$ with ROC: $\lvert z\rvert > 0.5$, determine the z-transform of $(n+1)x[n]$ and its ROC.

> [!success]- Solution
> $n\,x[n] \leftrightarrow -z\,\dfrac{dX}{dz}$, $\dfrac{dX}{dz} = -(1-\tfrac12 z^{-1})^{-2}\cdot\tfrac12 z^{-2}$:
> $$
> Y(z) = \frac{\frac12 z^{-1}}{(1-\frac12 z^{-1})^2} + \frac{1}{1-\frac12 z^{-1}} = \boxed{\frac{1}{(1-\frac12 z^{-1})^2},\qquad \lvert z\rvert > \tfrac12}
> $$
> Check: $(n+1)(\frac12)^n u[n] = x*x$, transform $X^2$. (Key leaves the sum; both full credit.)

> [!trap]
> The two minus signs in $-z\,dX/dz$ cancel; the ROC is unchanged.

## Problem 5 · A sinusoidal impulse response and resonance (12 pts)

> [!question] Problem 5 (12 pts)
> Suppose an LTI system has transfer function $H(z) = \dfrac{3z^{-1}}{1+z^{-2}}$ with ROC: $\lvert z\rvert > 1$.
> - **(a)** (8 pts) The impulse response $h[n]$ of this system can be expressed as $h[n] = A\sin(\omega_0 n + \theta)\,u[n]$. Find the constants $A$, $\omega_0$ and $\theta$. **Hint:** One approach is to use the z-transform pair
> $$
> \sin(\omega_0 n)u[n] \longleftrightarrow \frac{(\sin\omega_0)z^{-1}}{1 - 2(\cos\omega_0)z^{-1} + z^{-2}},\qquad \lvert z\rvert > 1.
> $$
> - **(b)** (4 pts) Find a bounded real or complex-valued input signal $x[n]$ for which the corresponding output $y[n]$ is unbounded.

> [!success]- Solution
> **(a)** $-2\cos\omega_0 = 0$ ⇒ $\omega_0 = \frac\pi2$, $\sin\omega_0 = 1$:
> $$
> h[n] = 3\sin\!\left(\tfrac{\pi}{2}n\right)u[n]:\qquad \boxed{A = 3,\ \ \omega_0 = \tfrac{\pi}{2},\ \ \theta = 0}
> $$
> ($h = \{\underset{\uparrow}{0}, 3, 0, -3, 0, 3, \dots\}$.)
>
> **(b)** Poles $\pm j$ on the unit circle. A bounded input with a pole at $\pm j$ doubles it; output grows like $n$:
> $$
> x[n] = j^n u[n],\qquad \cos\!\left(\tfrac\pi2 n\right)u[n],\qquad \sin\!\left(\tfrac\pi2 n\right)u[n]
> $$

> [!trap]
> $u[n]$ fails in (b): its pole at 1 doesn't match $\pm j$.

## Problem 6 · Impulse response from a recursion (8 pts)

> [!question] Problem 6 (8 pts)
> The output $y[n]$ and input $x[n]$ of a causal LTI system are related by the equation below. The system is initially at rest. Find the values of the impulse response $h[n]$ for the indicated values of $n$.
> $$
> y[n] = 2y[n-3] - x[n] + x[n-3]
> $$
> **(a)** $h[0] = $ **(b)** $h[1] = $ **(c)** $h[3] = $ **(d)** $h[4] = $

> [!success]- Solution
> $h[n] = 2h[n-3] - \delta[n] + \delta[n-3]$, rest:
> $$
> \begin{aligned}
> h[0] &= 2h[-3] - \delta[0] + \delta[-3] = 0 - 1 + 0 = -1\\
> h[1] &= 2h[-2] - 0 + 0 = 0,\qquad h[2] = 0\\
> h[3] &= 2h[0] - \delta[3] + \delta[0] = -2 - 0 + 1 = -1\\
> h[4] &= 2h[1] - 0 + 0 = 0
> \end{aligned}
> $$
> **(a) $-1$ (b) $0$ (c) $-1$ (d) $0$.** Check: $H(z) = \dfrac{-1+z^{-3}}{1-2z^{-3}} = -1 - \dfrac{z^{-3}}{1-2z^{-3}}$, $h[n] = -\delta[n] - \sum_{k\ge1}2^{k-1}\delta[n-3k]$ ($h[3] = -1$, $h[6] = -2$, $h[9] = -4$, …).

> [!warning] Answer-key erratum (#6)
> The key takes $h[0] = 1$ (it is $-1$) and so $h[3] = 3$ (it is $-1$); its $1, 0, 3, 0$ belong to $+x[n]$. See [[0-toolkit/05-errata|Errata]].

## Problem 7 · Two-sided input, $H = Y/X$, ROCs (21 pts)

> [!question] Problem 7 (21 pts)
> Suppose that the input to a **causal** LTI system is
> $$
> x[n] = \frac14\left(-\frac13\right)^n u[n] - 3\cdot 4^n\,u[-n-1]
> $$
> and the z-transform of the output $y[n]$ is
> $$
> Y(z) = \frac{13/4}{(1-\frac12 z^{-1})(1-z^{-1})(1+\frac13 z^{-1})}.
> $$
> - **(a)** Find the z-transform of $x[n]$ and its ROC.
> - **(b)** Find the transfer function $H(z)$ and its ROC.
> - **(c)** Determine the ROC of $Y(z)$.
> - **(d)** Find the impulse response of the system.
> - **(e)** Is the system stable?

> [!success]- Solution
> **(a)** Right part $\lvert z\rvert > \frac13$; left part ($-a^n u[-n-1] \leftrightarrow \frac{1}{1-az^{-1}}$) $\lvert z\rvert < 4$:
> $$
> X(z) = \frac{\frac14}{1+\frac13 z^{-1}} + \frac{3}{1-4z^{-1}} = \boxed{\frac{13/4}{(1+\frac13 z^{-1})(1-4z^{-1})},\qquad \tfrac13 < \lvert z\rvert < 4}
> $$
> Numerator: $\frac14(1-4z^{-1}) + 3(1+\frac13 z^{-1}) = \frac{13}{4}$.
>
> **(b)**
> $$
> H(z) = \frac{Y(z)}{X(z)} = \boxed{\frac{1-4z^{-1}}{(1-\frac12 z^{-1})(1-z^{-1})},\qquad \lvert z\rvert > 1\ \ (\text{causal})}
> $$
>
> **(c)** $\mathrm{ROC}_Y \supseteq \mathrm{ROC}_X\cap\mathrm{ROC}_H = \{1 < \lvert z\rvert < 4\}$; the pole at 4 cancels, leaving poles $\frac12$, $1$, $-\frac13$: $\boxed{\lvert z\rvert > 1}$.
>
> **(d)** $A_1 = \dfrac{1-8}{1-2} = 7$, $A_2 = \dfrac{1-4}{1-\frac12} = -6$:
> $$
> \boxed{h[n] = 7\left(\tfrac12\right)^n u[n] - 6\,u[n]}
> $$
>
> **(e)** **Not stable**: pole at $z = 1$; $h \to -6$.

> [!trap]
> - (c): after cancellation the ROC can grow to the next surviving pole. (e): a pole on the circle suffices.

### Sources for this page

Official handwritten key, ECE 310 Midterm Exam 1, Spring 2021 (pages 2–4); lectures [[1-signals-and-systems/03-system-properties|3]], [[2-z-transform/07-z-transform-properties|7]], [[2-z-transform/11-bibo-stability-and-causality|11]].
