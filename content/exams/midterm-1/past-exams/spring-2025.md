---
title: "Spring 2025 · Midterm 1"
description: "Spring 2025 ECE 310 Midterm 1 (Liang, Snyder) problem by problem with folded solutions, point traps and the corrected #4(a) answer (the key's boxed convolution is wrong)."
tags: [exam, midterm-1]
---

*Wed Feb 26, 2025 · 7:00–9:00 pm · Profs. Liang and Snyder · 8 problems, 100 points · T/F +2 / −1 / 0 blank · one handwritten two-sided sheet, no calculator · closed-form answers.*

> [!abstract] How to use this exam
> Second most useful (Snyder): adds parameter-for-stability (#7) and "all possible outputs" (#8b). Take it timed. The key's boxed #4(a) is wrong.

## Map of the exam

| # | pts | what it asks | problem family | lectures |
|---|---|---|---|---|
| 1 | 12 | six True/False statements (graded +2/−1/0) | [[exams/midterm-1/true-false-bank\|T/F bank]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]], [[2-z-transform/06-the-z-transform\|L6]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 2 | 12 | linear / shift-invariant / causal / stable for three systems | [[problems/classifying-system-properties\|classifying system properties]] | [[1-signals-and-systems/03-system-properties\|L3]], [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 3 | 10 | parallel connection, $h_1 = \delta[n-1]$: find $h_2$ from one input–output pair; is the whole system causal? | [[problems/finding-h-from-input-output-pairs\|finding h]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]] |
| 4 | 16 | (a) finite ∗ finite convolution; (b) $(-\tfrac13)^n u[n] * (\tfrac12)^n u[n-3]$ | [[problems/finite-length-convolution\|finite-length]] · [[problems/infinite-length-convolution\|infinite-length convolution]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]], [[2-z-transform/09-transfer-functions\|L9]] |
| 5 | 18 | three z-transforms with ROC (sum of steps, left-sided, two-sided) | [[problems/z-transform-with-roc\|z-transform with ROC]] | [[2-z-transform/06-the-z-transform\|L6]], [[2-z-transform/07-z-transform-properties\|L7]] |
| 6 | 6 | pole on the unit circle: which inputs give an unbounded output | [[problems/unbounded-outputs-and-pole-matching\|pole matching]] | [[2-z-transform/09-transfer-functions\|L9]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 7 | 6 | which values of $\alpha$ make a causal LCCDE stable | [[problems/parameters-for-stability\|parameters for stability]] | [[2-z-transform/09-transfer-functions\|L9]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 8 | 20 | $H(z)$ → LCCDE; *all* possible outputs for a pole-cancelling input; stable ROC and $h[n]$ | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z)]] · [[problems/all-possible-rocs\|inverse z / all ROCs]] | [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/09-transfer-functions\|L9]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |

## Problem 1 · True/False (12 pts)

> [!question] Problem 1
> Mark True or False. *Grading: correct = 2 pts, incorrect = −1 pt, no answer = 0 pts.*
>
> (a) If the output $y[n]$ of a system is related to its input $x[n]$ by $y[n] = \sum_{\ell=-\infty}^{\infty} h[\ell]\,x[n-\ell]$, for some well-defined function $h[n]$, the system must be a causal system.
>
> (b) If the unit pulse response $h[n]$ of a system $\mathcal{S}$ is absolutely summable, i.e. $\sum_{n=-\infty}^{\infty}\lvert h[n]\rvert < \infty$, then $\mathcal{S}$ must be BIBO-stable regardless if $\mathcal{S}$ is LSI or not.
>
> (c) The z-transform of $x[n] = e^{j\frac{\pi}{4}n}$ does not exist because the ROC is empty.
>
> (d) The parallel connection of two BIBO stable LTI systems always results in another BIBO stable LTI system.
>
> (e) A BIBO stable LTI system has a transfer function given by $H(z) = \dfrac{1}{1 - \sqrt2\,z^{-1}}$. This system must be anti-causal.
>
> (f) An LTI system with a two-sided impulse response is never BIBO stable.

> [!success]- Solution 1
> - **(a) False.** $h = \delta[n+1]$ gives $y[n] = x[n+1]$.
> - **(b) False.** Not LSI ⇒ $h$ doesn't determine the output: $y[n] = n\,x[n]$ has $h = 0$, yet $x = 1$ gives $y = n$.
> - **(c) True.** Two-sided: $n\ge0$ needs $\lvert z\rvert > 1$, $n<0$ needs $\lvert z\rvert < 1$; empty. (Key labels this scratch work "(d)".)
> - **(d) True.** $\sum\lvert h_1 + h_2\rvert \le \sum\lvert h_1\rvert + \sum\lvert h_2\rvert < \infty$.
> - **(e) True.** Stability forces ROC $\lvert z\rvert < \sqrt2$: $h = -(\sqrt2)^n u[-n-1]$, anti-causal.
> - **(f) False.** $h = (\tfrac12)^{\lvert n\rvert}$, $\sum\lvert h\rvert = 3$.

> [!trap] Where points go
> - (b): "absolutely summable $h$ ⇒ stable" holds for LTI only; "regardless if LSI" is the tell.
> - (e): stability decides the ROC; powers of $z^{-1}$ don't imply causal.

## Problem 2 · System properties (12 pts)

> [!question] Problem 2
> For each system, indicate "yes" or "no" for Linear, Shift-Invariant, Causal, Stable (no justification needed; no deduction for wrong answers).
>
> 1. $y[n] = x[n] * j^n u[n]$
> 2. $y[n] = 2x[\lvert n\rvert] + 10$
> 3. $y[n] = e^{x[n]+1}$

> [!success]- Solution 2
>
> | system | Linear | Shift-inv. | Causal | Stable |
> |---|---|---|---|---|
> | $x[n]*j^n u[n]$ | **Yes** | **Yes** | **Yes** | **No** |
> | $2x[\lvert n\rvert]+10$ | **No** | **No** | **No** | **Yes** |
> | $e^{x[n]+1}$ | **No** | **Yes** | **Yes** | **Yes** |
>
> - Row 1: LTI, $h = j^n u[n]$ causal; $\sum\lvert j^n\rvert = \sum 1 = \infty$.
> - Row 2: $x = 0$ gives $y = 10$; $\lvert n\rvert$ folds time; $y[-3] = 2x[3] + 10$; $\lvert y\rvert \le 2B + 10$.
> - Row 3: nonlinear, memoryless; $\lvert y\rvert \le e^{B+1}$.

> [!trap] Where points go
> - Row 1: bounded $\lvert j^n\rvert = 1$ is not summable. More: [[exams/midterm-1/system-property-bank|system-property bank]].

## Problem 3 · Parallel connection: find $h_2$ (10 pts)

> [!question] Problem 3
> Two LTI systems $h_1[n]$ and $h_2[n]$ are connected in parallel: $x[n]$ feeds both, and their outputs add to give $y[n]$. We are given $h_1[n] = \delta[n-1]$ and the input–output pair
> $$
> x[n] = \{\underset{\uparrow}{1},\ 2,\ 1\},\qquad y[n] = \{1,\ \underset{\uparrow}{2},\ 2,\ 2,\ 1\}.
> $$
> (a) Determine the impulse response $h_2[n]$.
>
> (b) Is the overall system $h[n]$ (such that $x[n]*h[n] = y[n]$) causal? Justify your reasoning.

> [!success]- Solution 3
> **(a)** $y = x[n-1] + x*h_2$; subtract on $n = -1,\dots,3$:
>
> | $n$ | −1 | 0 | 1 | 2 | 3 |
> |---|---|---|---|---|---|
> | $y[n]$ | 1 | 2 | 2 | 2 | 1 |
> | $x[n-1]$ | 0 | 0 | 1 | 2 | 1 |
> | $x*h_2$ | 1 | 2 | 1 | 0 | 0 |
>
> $x*h_2 = \{1,\underset{\uparrow}{2},1\} = x[n+1]$: $\boldsymbol{h_2[n] = \delta[n+1]}$. (z: $Y - z^{-1}X = z + 2 + z^{-1} = zX$, $H_2(z) = z$.)
>
> **(b)** $h = h_1 + h_2 = \{1,\ \underset{\uparrow}{0},\ 1\}$: **not causal**, $h[-1] = 1$.

> [!trap] Where points go
> - $y$'s arrow is on the second entry: $y$ starts at $n = -1$.

## Problem 4 · Convolution (16 pts)

> [!question] Problem 4
> Compute the response of an LSI system with impulse response $h[n]$ to the input $x[n]$.
>
> (a) $x[n] = \{1,\ -2,\ \underset{\uparrow}{0},\ 3,\ -1,\ 1\}$, $\quad h[n] = \{\underset{\uparrow}{2},\ -1,\ 3\}$
>
> (b) $x[n] = \left(-\tfrac13\right)^n u[n]$, $\quad h[n] = \left(\tfrac12\right)^n u[n-3]$

> [!success]- Solution 4(a)
> Start $n = -2$, length $6 + 3 - 1 = 8$; e.g. $y[0] = x[0]h[0] + x[-1]h[1] + x[-2]h[2] = 0 + 2 + 3$:
> $$
> \boldsymbol{y[n] = \{2,\ -5,\ \underset{\uparrow}{5},\ 0,\ -5,\ 12,\ -4,\ 3\}}
> $$
> Check: $\sum y = 8 = \big(\sum x\big)\big(\sum h\big) = 2\cdot 4$ ✓.

> [!warning] Answer-key erratum — #4(a)
> The key's boxed $\{2, -5, \underset{\uparrow}{6}, 0, -5, 10, -4, 3\}$ is wrong in two entries (sum 7 ≠ 8); its own matrix product gives $2, -5, 5, 0, -5, 12, -4, 3$.

> [!success]- Solution 4(b)
> $X(z) = \dfrac{1}{1+\frac13 z^{-1}}$, $h[n] = \tfrac18\left(\tfrac12\right)^{n-3}u[n-3] \Rightarrow H(z) = \dfrac{\frac18 z^{-3}}{1 - \frac12 z^{-1}}$:
> $$
> \begin{aligned}
> \frac{1}{(1+\frac13 z^{-1})(1-\frac12 z^{-1})} &= \frac{2/5}{1+\frac13 z^{-1}} + \frac{3/5}{1-\frac12 z^{-1}},\\
> Y(z) &= \tfrac18 z^{-3}\left[\frac{2/5}{1+\frac13 z^{-1}} + \frac{3/5}{1-\frac12 z^{-1}}\right]
> \end{aligned}
> $$
> $$
> \begin{gathered}
> \boldsymbol{y[n] = \tfrac{1}{20}\left(-\tfrac13\right)^{n-3}u[n-3] + \tfrac{3}{40}\left(\tfrac12\right)^{n-3}u[n-3]}\\
> = \left[-\tfrac{27}{20}\left(-\tfrac13\right)^n + \tfrac35\left(\tfrac12\right)^n\right]u[n-3].
> \end{gathered}
> $$
> (Time domain: $y[n] = \left(-\tfrac13\right)^n\sum_{k=3}^{n}\left(-\tfrac32\right)^k$, $n \ge 3$.)

> [!trap] Where points go
> - (a): start index $n_x + n_h = -2$. (b): keep the $\tfrac18$ and the $u[n-3]$.

## Problem 5 · z-transforms (18 pts)

> [!question] Problem 5
> Compute the z-transform of each signal, including its ROC.
>
> (a) $x[n] = \displaystyle\sum_{k=0}^{2}\left(\tfrac12\right)^k u[n-k]$
>
> (b) $x[n] = 3^n u[-n+2]$
>
> (c) $x[n] = \left(\tfrac14\right)^n\left(\tfrac23\right)^{n-2}u[n-1] + \left(\tfrac43\right)^n u[-n-1]$

> [!success]- Solution 5(a)
> $x[n] = u[n] + \tfrac12 u[n-1] + \tfrac14 u[n-2]$:
> $$
> \boldsymbol{X(z) = \frac{1 + \frac12 z^{-1} + \frac14 z^{-2}}{1 - z^{-1}},\qquad \lvert z\rvert > 1}
> $$
> ($= 1 + \tfrac32 z^{-1} + \dfrac{\frac74 z^{-2}}{1-z^{-1}}$.)

> [!success]- Solution 5(b)
> $m = -n$: $X(z) = \sum_{m=-2}^{\infty}\left(\tfrac{z}{3}\right)^m = \dfrac{(z/3)^{-2}}{1 - z/3}$, $\lvert z\rvert < 3$; $z^{-1}, z^{-2}$ exclude $z = 0$:
> $$
> \boldsymbol{X(z) = \frac{9z^{-2}}{1 - \frac13 z} = \frac{-27z^{-3}}{1 - 3z^{-1}},\qquad 0 < \lvert z\rvert < 3}
> $$
> ($= -\dfrac{1}{1-3z^{-1}} + 1 + 3z^{-1} + 9z^{-2}$.)

> [!success]- Solution 5(c)
> $\left(\tfrac14\right)^n\left(\tfrac23\right)^{n-2} = \tfrac94\left(\tfrac16\right)^n = \tfrac38\left(\tfrac16\right)^{n-1}$; left-sided $a^n u[-n-1] \leftrightarrow \dfrac{-1}{1-az^{-1}}$:
> $$
> \boldsymbol{X(z) = \frac{\frac38 z^{-1}}{1 - \frac16 z^{-1}} - \frac{1}{1 - \frac43 z^{-1}},\qquad \tfrac16 < \lvert z\rvert < \tfrac43}
> $$

> [!trap] Where points go
> - (b): "$0 <$" in the ROC. (c): combine bases first, track $\tfrac94$; minus on the left-sided term.

## Problem 6 · Unbounded outputs (6 pts)

> [!question] Problem 6
> A causal LSI system has
> $$
> H(z) = \frac{z}{z - \frac{1}{\sqrt2}(1+j)},\qquad \text{ROC: } \lvert z\rvert > 1 .
> $$
> Mark True or False for each input that will produce an **unbounded** output.
>
> - (a) $u[n]$
> - (b) $e^{j\frac{\pi}{4}n}u[n]$
> - (c) $e^{-j\frac{\pi}{4}n}u[n]$
> - (d) $e^{-j\frac{3\pi}{4}n}u[n]$
> - (e) $\cos\!\left(\tfrac{\pi}{4}n\right)u[n]$
> - (f) $4^n u[n]$

> [!success]- Solution 6
> $H(z) = \dfrac{1}{1 - e^{j\pi/4}z^{-1}}$: simple pole at $\frac{1+j}{\sqrt2} = e^{j\pi/4}$ **on** the unit circle.
> - (a) **False.** Pole at $1$.
> - (b) **True.** $Y = \frac{1}{(1-e^{j\pi/4}z^{-1})^2}$, $y = (n+1)e^{j\pi n/4}u[n]$.
> - (c) **False.** Conjugate pole $e^{-j\pi/4}$.
> - (d) **False.** Pole at $e^{-j3\pi/4}$.
> - (e) **True.** $\cos(\tfrac{\pi}{4}n) = \tfrac12 e^{j\pi n/4} + \tfrac12 e^{-j\pi n/4}$.
> - (f) **True.** Unbounded input, no zero at $4$.

> [!trap] Where points go
> - (c): a conjugate pole is a different pole. (f): unbounded input not cancelled ⇒ unbounded output ([[problems/unbounded-outputs-and-pole-matching|pole matching]]).

## Problem 7 · Which $\alpha$ makes it stable? (6 pts)

> [!question] Problem 7
> A causal LSI system is given by
> $$
> y[n] = -\tfrac32\,y[n-1] + y[n-2] + x[n] - \alpha^2 x[n-2],\qquad \alpha \in \mathbb{C}.
> $$
> Mark True or False for each value of $\alpha$ that will make the system BIBO stable: (a) $2$ (b) $-2$ (c) $j2$ (d) $-j2$ (e) $\tfrac{\sqrt2}{2}$ (f) $\tfrac12$.

> [!success]- Solution 7
> $$
> H(z) = \frac{1 - \alpha^2 z^{-2}}{1 + \frac32 z^{-1} - z^{-2}} = \frac{(1-\alpha z^{-1})(1+\alpha z^{-1})}{(1+2z^{-1})(1-\frac12 z^{-1})}
> $$
> Poles $-2$ (unstable), $\tfrac12$; zeros $\pm\alpha$. Stable iff a zero is on $-2$: $\alpha = \pm 2$.
>
> **(a) True, (b) True, (c) False, (d) False, (e) False, (f) False.**

> [!trap] Where points go
> - $\lvert\alpha\rvert = 2$ is not enough: zeros at $\pm j2$ miss. ([[problems/parameters-for-stability|parameters for stability]])

## Problem 8 · LCCDE, all possible outputs, stable $h$ (20 pts)

> [!question] Problem 8
> An LTI system has
> $$
> H(z) = \frac{2 - 3z^{-1}}{\left(1 - \frac12 z^{-1}\right)\left(1 + \frac32 z^{-1}\right)} .
> $$
> (a) Determine the difference equation corresponding to this system.
>
> (b) Determine all the possible outputs $y[n]$ when the input is $x[n] = \delta[n] + \tfrac32\delta[n-1]$.
>
> (c) Determine the ROC of $H(z)$ so that the system is stable, and find the corresponding impulse response $h[n]$.

> [!success]- Solution 8(a)
> $\left(1 - \frac12 z^{-1}\right)\left(1 + \frac32 z^{-1}\right) = 1 + z^{-1} - \frac34 z^{-2}$:
> $$
> \boldsymbol{y[n] + y[n-1] - \tfrac34\,y[n-2] = 2x[n] - 3x[n-1]}
> $$

> [!success]- Solution 8(b)
> $X(z) = 1 + \tfrac32 z^{-1}$ cancels $-\tfrac32$:
> $$
> Y(z) = \frac{2 - 3z^{-1}}{1 - \frac12 z^{-1}} = \frac{2}{1-\frac12 z^{-1}} - \frac{3z^{-1}}{1-\frac12 z^{-1}} .
> $$
> $H$'s ROC could be $\lvert z\rvert > \tfrac32$, $\tfrac12 < \lvert z\rvert < \tfrac32$ or $\lvert z\rvert < \tfrac12$; ROC$_Y$ is $\lvert z\rvert > \tfrac12$ (first two) or $\lvert z\rvert < \tfrac12$: **two** outputs:
> $$
> \begin{aligned}
> \#1\ (\lvert z\rvert > \tfrac12):&\quad \boldsymbol{y[n] = 2\left(\tfrac12\right)^n u[n] - 3\left(\tfrac12\right)^{n-1}u[n-1]}\\
> &\qquad\quad = 2\delta[n] - 4\left(\tfrac12\right)^n u[n-1]\\
> \#2\ (\lvert z\rvert < \tfrac12):&\quad \boldsymbol{y[n] = -2\left(\tfrac12\right)^n u[-n-1] + 3\left(\tfrac12\right)^{n-1}u[-n]}\\
> &\qquad\quad = 6\delta[n] + 4\left(\tfrac12\right)^n u[-n-1]
> \end{aligned}
> $$

> [!success]- Solution 8(c)
> **ROC $\tfrac12 < \lvert z\rvert < \tfrac32$**. Cover-up:
> $$
> A_1 = \left.\frac{2-3z^{-1}}{1+\frac32 z^{-1}}\right|_{z=1/2} = \frac{-4}{4} = -1,\qquad A_2 = \left.\frac{2-3z^{-1}}{1-\frac12 z^{-1}}\right|_{z=-3/2} = \frac{4}{4/3} = 3
> $$
> $$
> \boldsymbol{h[n] = -\left(\tfrac12\right)^n u[n] - 3\left(-\tfrac32\right)^n u[-n-1]}
> $$

> [!trap] Where points go
> - (b): give every output, not one. (c): left-sided term keeps its minus ([[problems/all-possible-rocs|all possible ROCs]]).

## Related

[[exams/midterm-1/past-exams/index|All past exams]] · previous: [[exams/midterm-1/past-exams/fall-2025|Fall 2025]] · next: [[exams/midterm-1/past-exams/fall-2024|Fall 2024]] · [[exams/midterm-1/true-false-bank|T/F bank]] · [[0-toolkit/05-errata|errata]] · [[concepts/sided-sequences|sided sequences]]

### Sources for this page

ECE 310 Midterm Exam 1, Spring 2025 (Liang, Snyder), handwritten key (ECE_310_Exam_1_Spring_2025_Solutions.pdf); arrows in #3, #4(a) read from a high-resolution render.
