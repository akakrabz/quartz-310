---
title: "Spring 2025 · Midterm 1"
description: "The Spring 2025 ECE 310 Midterm 1 (Liang, Snyder) typed out problem by problem, with folded worked solutions, the traps that cost points, and the corrected #4(a) answer (the key's boxed convolution is wrong)."
tags: [exam, midterm-1]
---

*Wed Feb 26, 2025 · 7:00–9:00 pm · Profs. Liang and Snyder · 8 problems, 100 points · T/F graded +2 correct / −1 wrong / 0 blank · one handwritten two-sided 8.5″ × 11″ sheet, no books, no calculator · answers in closed form (no $\Sigma$ or $\int$ signs)*

> [!abstract] How to use this exam
> The second most useful past exam: Snyder co-taught it, and it has the two ideas Fall 2025 does not — a **parameter-for-stability** problem (#7) and an **"all possible outputs"** problem (#8b). Take it **timed (2 h, only your sheet)**, then check. Heads-up: the handwritten key's boxed answer to #4(a) is wrong (its own matrix work is right) — see the erratum there.

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
> - **(a) False.** Nothing forces $h[\ell] = 0$ for $\ell < 0$: $h = \delta[n+1]$ gives $y[n] = x[n+1]$, which uses the future.
> - **(b) False.** For a system that is not LSI, $h$ does not determine the output. $y[n] = n\,x[n]$ answers $\delta[n]$ with $n\delta[n] = 0$ (absolutely summable), yet $x = 1$ gives $y = n$.
> - **(c) True.** $x$ is two-sided: $\sum_{n\ge0}(e^{j\pi/4}z^{-1})^n$ needs $\lvert z\rvert > 1$, $\sum_{n<0}$ needs $\lvert z\rvert < 1$; the intersection is empty. (The key's scratch work for this item is labelled "(d)".)
> - **(d) True.** $h = h_1 + h_2$ and $\sum\lvert h_1 + h_2\rvert \le \sum\lvert h_1\rvert + \sum\lvert h_2\rvert < \infty$.
> - **(e) True.** The pole $\sqrt2$ is outside the unit circle; stability forces the ROC $\lvert z\rvert < \sqrt2$ (it must contain $\lvert z\rvert = 1$), so $h = -(\sqrt2)^n u[-n-1]$, anti-causal.
> - **(f) False.** $h = (\tfrac12)^{\lvert n\rvert}$ is two-sided with $\sum\lvert h\rvert = 3$.

> [!trap] Where points go
> - **(b)** "Absolutely summable $h$ ⇒ stable" is a theorem **about LTI systems only**. The phrase "regardless if $\mathcal{S}$ is LSI or not" is the tell.
> - **(e)** Stability + a pole outside the unit circle *decides* the ROC; don't assume causal because the formula is in powers of $z^{-1}$.
> - With +2/−1 scoring an educated guess still pays (expected $+0.5$ at 50/50); a blank scores 0.

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
> - Row 1: convolution ⇒ LTI with $h = j^n u[n]$; $h[n] = 0$ for $n<0$ ⇒ causal; $\sum\lvert j^n\rvert = \sum 1 = \infty$ ⇒ unstable.
> - Row 2: $x = 0$ gives $y = 10 \ne 0$ ⇒ nonlinear; the index $\lvert n\rvert$ folds time ⇒ shift-varying; $y[-3] = 2x[3] + 10$ uses the future ⇒ non-causal; $\lvert y\rvert \le 2B + 10$ ⇒ stable.
> - Row 3: $e^{(\cdot)}$ is nonlinear; no explicit $n$ ⇒ SI; memoryless ⇒ causal; $\lvert y\rvert \le e^{B+1}$ ⇒ stable.

> [!trap] Where points go
> - Row 1: $\lvert j^n\rvert = 1$ is **bounded**, but stability needs $\sum\lvert h\rvert < \infty$ — it isn't.
> - Row 2: the $+10$ kills linearity by itself; the $\lvert n\rvert$ kills both shift-invariance and causality. More rows: [[exams/midterm-1/system-property-bank|system-property bank]].

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
> **(a)** $y = x*h_1 + x*h_2$ and $x*h_1 = x[n-1]$. Subtract, aligned on $n = -1,\dots,3$:
>
> | $n$ | −1 | 0 | 1 | 2 | 3 |
> |---|---|---|---|---|---|
> | $y[n]$ | 1 | 2 | 2 | 2 | 1 |
> | $x[n-1]$ | 0 | 0 | 1 | 2 | 1 |
> | $x*h_2$ | 1 | 2 | 1 | 0 | 0 |
>
> $x*h_2 = \{1,\underset{\uparrow}{2},1\} = x[n+1]$, so $\boldsymbol{h_2[n] = \delta[n+1]}$. (z-domain: $Y - z^{-1}X = z + 2 + z^{-1} = zX$, so $H_2(z) = z$.)
>
> **(b)** $h = h_1 + h_2 = \{1,\ \underset{\uparrow}{0},\ 1\}$. **Not causal**: $h[-1] = 1 \ne 0$. (The key writes "$h[n] \ne 0$ for all $n<0$"; one nonzero sample at negative time is enough.)

> [!trap] Where points go
> - Misaligning $y$: its arrow is on the **second** entry, so $y$ starts at $n = -1$, one sample *before* $x$ — that early sample is exactly what forces a non-causal $h_2$.
> - Answering (b) about $h_2$ alone instead of the overall $h = h_1 + h_2$.

## Problem 4 · Convolution (16 pts)

> [!question] Problem 4
> Compute the response of an LSI system with impulse response $h[n]$ to the input $x[n]$.
>
> (a) $x[n] = \{1,\ -2,\ \underset{\uparrow}{0},\ 3,\ -1,\ 1\}$, $\quad h[n] = \{\underset{\uparrow}{2},\ -1,\ 3\}$
>
> (b) $x[n] = \left(-\tfrac13\right)^n u[n]$, $\quad h[n] = \left(\tfrac12\right)^n u[n-3]$

> [!success]- Solution 4(a)
> $x$ starts at $n = -2$, $h$ at $n = 0$ ⇒ $y$ starts at $n = -2$, length $6 + 3 - 1 = 8$. Sliding sums (e.g. $y[0] = x[0]h[0] + x[-1]h[1] + x[-2]h[2] = 0 + 2 + 3$):
> $$
> \boldsymbol{y[n] = \{2,\ -5,\ \underset{\uparrow}{5},\ 0,\ -5,\ 12,\ -4,\ 3\}}
> $$
> Sum check: $\sum y = 8 = \big(\sum x\big)\big(\sum h\big) = 2\cdot 4$ ✓.

> [!warning] Answer-key erratum — #4(a)
> The key's **boxed** answer $\{2, -5, \underset{\uparrow}{6}, 0, -5, 10, -4, 3\}$ is wrong in two entries; the matrix product written right above it gives the correct column $2, -5, 5, 0, -5, 12, -4, 3$. The box fails the sum check ($\sum = 7 \ne 8$).

> [!success]- Solution 4(b)
> z-domain route: $X(z) = \dfrac{1}{1+\frac13 z^{-1}}$, $h[n] = \tfrac18\left(\tfrac12\right)^{n-3}u[n-3] \Rightarrow H(z) = \dfrac{\frac18 z^{-3}}{1 - \frac12 z^{-1}}$. Partial fractions of the rational part:
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
> (Time-domain route: $y[n] = \left(-\tfrac13\right)^n\sum_{k=3}^{n}\left(-\tfrac32\right)^k$ for $n \ge 3$, a finite geometric sum — same answer.)

> [!trap] Where points go
> - **(a)** Starting the output at $n = 0$ because $h$ does: the start index is $n_x + n_h = -2$.
> - **(b)** $h$ is $\left(\tfrac12\right)^n u[n-3]$, **not** $\left(\tfrac12\right)^{n-3}u[n-3]$ — the factor $\tfrac18$ is easy to lose. And the sum is empty for $n < 3$, so the answer needs $u[n-3]$.

```python
import numpy as np
x, nx0 = [1, -2, 0, 3, -1, 1], -2    # arrow on the 0
h, nh0 = [2, -1, 3], 0               # arrow on the 2
y = np.convolve(x, h)
ny0 = nx0 + nh0
print("n =", list(range(ny0, ny0 + len(y))))
print("y =", y.tolist())
print("sum check:", y.sum(), "=", sum(x), "*", sum(h))
```

```text
n = [-2, -1, 0, 1, 2, 3, 4, 5]
y = [2, -5, 5, 0, -5, 12, -4, 3]
sum check: 8 = 2 * 4
```

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
> $x[n] = u[n] + \tfrac12 u[n-1] + \tfrac14 u[n-2]$, each step $\leftrightarrow \frac{z^{-k}}{1-z^{-1}}$:
> $$
> \boldsymbol{X(z) = \frac{1 + \frac12 z^{-1} + \frac14 z^{-2}}{1 - z^{-1}},\qquad \lvert z\rvert > 1}
> $$
> (Equivalent: $1 + \tfrac32 z^{-1} + \dfrac{\frac74 z^{-2}}{1-z^{-1}}$.)

> [!success]- Solution 5(b)
> $x[n] = 3^n$ for $n \le 2$ (left-sided, but with samples at $n = 1, 2$). Substitute $m = -n$: $X(z) = \sum_{m=-2}^{\infty}\left(\tfrac{z}{3}\right)^m = \dfrac{(z/3)^{-2}}{1 - z/3}$, which needs $\lvert z\rvert < 3$; the $z^{-1}, z^{-2}$ terms exclude $z = 0$:
> $$
> \boldsymbol{X(z) = \frac{9z^{-2}}{1 - \frac13 z} = \frac{-27z^{-3}}{1 - 3z^{-1}},\qquad 0 < \lvert z\rvert < 3}
> $$
> (Also $= -\dfrac{1}{1-3z^{-1}} + 1 + 3z^{-1} + 9z^{-2}$: the pair $-3^n u[-n-1]$ plus the three samples at $n = 0, 1, 2$.)

> [!success]- Solution 5(c)
> First term: $\left(\tfrac14\right)^n\left(\tfrac23\right)^{n-2} = \tfrac94\left(\tfrac16\right)^n = \tfrac38\left(\tfrac16\right)^{n-1}$, a delayed right-sided exponential. Second term: the left-sided pair $a^n u[-n-1] \leftrightarrow \dfrac{-1}{1-az^{-1}}$, $\lvert z\rvert < \lvert a\rvert$.
> $$
> \boldsymbol{X(z) = \frac{\frac38 z^{-1}}{1 - \frac16 z^{-1}} - \frac{1}{1 - \frac43 z^{-1}},\qquad \tfrac16 < \lvert z\rvert < \tfrac43}
> $$

> [!trap] Where points go
> - **(b)** ROC $\lvert z\rvert < 3$ without "$0 <$": the samples at $n = 1, 2$ put $z^{-1}, z^{-2}$ in $X(z)$, which blow up at $z = 0$.
> - **(c)** Mixing the bases: combine $\left(\tfrac14\right)^n\left(\tfrac23\right)^{n}$ into $\left(\tfrac16\right)^n$ *before* transforming, and track the constant $\left(\tfrac23\right)^{-2} = \tfrac94$. The left-sided term carries a **minus** sign.

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
> $H(z) = \dfrac{1}{1 - e^{j\pi/4}z^{-1}}$: one simple pole at $\frac{1+j}{\sqrt2} = e^{j\pi/4}$, **on** the unit circle. A bounded input gives an unbounded output only if it puts a second pole at $e^{j\pi/4}$.
> - (a) **False.** Pole at $1$ — a different point.
> - (b) **True.** Double pole: $Y = \frac{1}{(1-e^{j\pi/4}z^{-1})^2}$, $y = (n+1)e^{j\pi n/4}u[n]$.
> - (c) **False.** Pole at $e^{-j\pi/4}$, the conjugate — not the same point.
> - (d) **False.** Pole at $e^{-j3\pi/4}$.
> - (e) **True.** $\cos(\tfrac{\pi}{4}n) = \tfrac12 e^{j\pi n/4} + \tfrac12 e^{-j\pi n/4}$ contains the resonant term.
> - (f) **True.** The input is itself unbounded and $H$ has no zero at $4$ to cancel it; $y$ contains a $4^n$ term.

> [!trap] Where points go
> - **(c)** A conjugate pole is a different pole. Only $e^{+j\pi/4}$ resonates — the real $\cos$ in (e) works because it *contains* $e^{+j\pi n/4}$.
> - **(f)** The question asks about the output, not about "resonance": an unbounded input that nothing cancels gives an unbounded output. See [[problems/unbounded-outputs-and-pole-matching|pole matching]].

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
> Causal, poles $-2$ (unstable) and $\tfrac12$; zeros $\pm\alpha$. Stable **iff a zero lands exactly on $-2$**, i.e. $\alpha = \pm 2$.
>
> **(a) True, (b) True, (c) False, (d) False, (e) False, (f) False.** ($\alpha = \pm j2$ puts the zeros at $\pm j2$ — right magnitude, wrong place; $\alpha = \tfrac12$ cancels the harmless pole at $\tfrac12$.)

> [!trap] Where points go
> - Sign of the feedback terms: moving $-\tfrac32 y[n-1] + y[n-2]$ to the left gives $1 + \tfrac32 z^{-1} - z^{-2}$.
> - $\lvert\alpha\rvert = 2$ is not enough — cancellation needs the zero *on* the pole. Only $\alpha^2$ enters, so $\alpha$ and $-\alpha$ always give the same answer. Recipe: [[problems/parameters-for-stability|parameters for stability]].

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
> $\left(1 - \frac12 z^{-1}\right)\left(1 + \frac32 z^{-1}\right) = 1 + z^{-1} - \frac34 z^{-2}$, so $Y(z)\left(1 + z^{-1} - \tfrac34 z^{-2}\right) = X(z)\left(2 - 3z^{-1}\right)$:
> $$
> \boldsymbol{y[n] + y[n-1] - \tfrac34\,y[n-2] = 2x[n] - 3x[n-1]}
> $$

> [!success]- Solution 8(b)
> $X(z) = 1 + \tfrac32 z^{-1}$ cancels the pole at $-\tfrac32$:
> $$
> Y(z) = \frac{2 - 3z^{-1}}{1 - \frac12 z^{-1}} = \frac{2}{1-\frac12 z^{-1}} - \frac{3z^{-1}}{1-\frac12 z^{-1}} .
> $$
> No ROC was given for $H$ ($\lvert z\rvert > \tfrac32$, $\tfrac12 < \lvert z\rvert < \tfrac32$ or $\lvert z\rvert < \tfrac12$). $Y$ has a single pole at $\tfrac12$, so the first two choices give ROC$_Y$ $\lvert z\rvert > \tfrac12$ and the third gives $\lvert z\rvert < \tfrac12$ — **two** possible outputs:
> $$
> \begin{aligned}
> \#1\ (\lvert z\rvert > \tfrac12):&\quad \boldsymbol{y[n] = 2\left(\tfrac12\right)^n u[n] - 3\left(\tfrac12\right)^{n-1}u[n-1]}\\
> &\qquad\quad = 2\delta[n] - 4\left(\tfrac12\right)^n u[n-1]\\
> \#2\ (\lvert z\rvert < \tfrac12):&\quad \boldsymbol{y[n] = -2\left(\tfrac12\right)^n u[-n-1] + 3\left(\tfrac12\right)^{n-1}u[-n]}\\
> &\qquad\quad = 6\delta[n] + 4\left(\tfrac12\right)^n u[-n-1]
> \end{aligned}
> $$

> [!success]- Solution 8(c)
> Stable ⇒ ROC contains the unit circle: **$\tfrac12 < \lvert z\rvert < \tfrac32$**. Cover-up:
> $$
> A_1 = \left.\frac{2-3z^{-1}}{1+\frac32 z^{-1}}\right|_{z=1/2} = \frac{-4}{4} = -1,\qquad A_2 = \left.\frac{2-3z^{-1}}{1-\frac12 z^{-1}}\right|_{z=-3/2} = \frac{4}{4/3} = 3
> $$
> Pole $\tfrac12$ inside the ROC's inner edge ⇒ right-sided; pole $-\tfrac32$ outside ⇒ left-sided:
> $$
> \boldsymbol{h[n] = -\left(\tfrac12\right)^n u[n] - 3\left(-\tfrac32\right)^n u[-n-1]}
> $$

> [!trap] Where points go
> - **(b)** Giving one output. "All possible" means: list the ROCs $H$ could have, cancel, and see which distinct ROCs $Y$ can end up with. Cancelling $-\tfrac32$ first is what collapses three cases into two.
> - **(c)** The left-sided term keeps its **minus**: $\frac{3}{1+\frac32 z^{-1}}$ with $\lvert z\rvert < \tfrac32$ ↔ $-3\left(-\tfrac32\right)^n u[-n-1]$. See [[problems/all-possible-rocs|all possible ROCs]].

## Related

- [[exams/midterm-1/past-exams/index|All past exams]] · previous: [[exams/midterm-1/past-exams/fall-2025|Fall 2025]] · next: [[exams/midterm-1/past-exams/fall-2024|Fall 2024]]
- [[exams/midterm-1/true-false-bank|T/F bank]] · [[exams/midterm-1/system-property-bank|system-property bank]] · [[0-toolkit/05-errata|errata]]
- [[concepts/region-of-convergence|ROC]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/pole-zero-cancellation|pole–zero cancellation]]

### Sources for this page

- ECE 310 Midterm Exam 1, Spring 2025 (Profs. Liang and Snyder), with the handwritten solution key (`old-exams/ECE_310_Exam_1_Spring_2025_Solutions.pdf`); arrow positions in #3 and #4(a) read from a high-resolution render.
- Every answer re-derived and checked numerically (`np.convolve` with index bookkeeping, direct convolution of the infinite sequences, truncated z-transform sums at test points in each ROC, `residuez`, exact-arithmetic LCCDE runs for the $\alpha$ values, growth tests for the unit-circle pole).
