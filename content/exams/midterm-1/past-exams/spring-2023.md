---
title: "Spring 2023 · Midterm 1"
description: "ECE 310 Spring 2023 Midterm 1 (Liang, Moon, Snyder) with folded solutions and traps: T/F, properties, three convolutions, h from two pairs, a pole-cancelling input, H = Y/X with PFE, bounded/unbounded pairs; one key erratum."
tags: [exam, midterm-1]
---

*Wed Mar 1, 2023 · 7:00–9:00 pm · Profs. Liang, Moon, Snyder · 9 problems, 100 points (#8–#9, 8 pts, are DTFT, not on this term's Midterm 1) · one handwritten two-sided sheet, no calculator · closed forms.*

## Map of the exam

| # | pts | what it asks | problem family | lectures |
|---|---|---|---|---|
| 1 | 10 | True/False: $h$ and LTI, BIBO with an unbounded input, right-sided vs causal (+ two DTFT items) | [[exams/midterm-1/true-false-bank\|True/False bank]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 2 | 12 | Linear / shift-invariant / causal / stable table, 3 systems | [[problems/classifying-system-properties\|Classifying properties]] · [[exams/midterm-1/system-property-bank\|bank]] | [[1-signals-and-systems/03-system-properties\|L3]], [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 3 | 15 | (a) finite convolution with $n=0$ bookkeeping; (b) two one-sided exponentials; (c) a 3-tap box against $\log(\lvert n\rvert+1)$ | [[problems/finite-length-convolution\|Finite]] (a) · [[problems/infinite-length-convolution\|Infinite]] (b, c) | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 4 | 6 | $h[n]$ from two input–output pairs | [[problems/finding-h-from-input-output-pairs\|Finding h]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 5 | 20 | LCCDE → $H(z)$, poles, zeros, ROC; response to an input that cancels the unstable pole; stability | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z)]] | [[2-z-transform/09-transfer-functions\|L9]]–[[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 6 | 20 | $H = Y/X$ and its ROC; PFE for $h[n]$; the difference equation | [[problems/finding-h-from-input-output-pairs\|Finding H]] · [[problems/all-possible-rocs\|PFE]] · [[problems/lccde-to-transfer-function-and-response\|LCCDE]] | [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/09-transfer-functions\|L9]] |
| 7 | 9 | Bounded/unbounded inputs and outputs for $H(z) = \frac{z-3}{z-4}$ | [[problems/unbounded-outputs-and-pole-matching\|Pole matching]] | [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 8 | 4 | DTFT: not on the Fall 2026 Midterm 1 | — | [[3-fourier-analysis/index\|L13]] |
| 9 | 4 | DTFT: not on the Fall 2026 Midterm 1 | — | [[3-fourier-analysis/index\|L13]] |

## Problem 1 · True/False (10 pts)

> [!question] Problem 1 (10 pts)
> Answer **True** or **False** to each of the following statements: *Grading:* Correct answer = 2 pt.; Incorrect answer = −1 pt. No answer = 0 pts.
> - **(a)** If the system response $y[n]$ of a discrete-time system to any possible input signal $x[n]$ is fully described by its unit pulse response, then the system must be LTI.
> - **(b)** If a system is BIBO stable, any unbounded input will produce an unbounded output.
> - **(c)** If a system has a right-sided unit pulse response, then it must be causal.
> - **(d)** The DTFT, $X_d(\omega)$, of a sequence $x[n]$ is always related to its z-transform $X(z)$ by $X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$.
> - **(e)** If $x[n]$ is a real-valued sequence, then $\lvert X_d(\omega)\rvert$ is an even function.

> [!success]- Solution
> - **(a) True.** $y = x*h$ for every input ⇒ LTI.
> - **(b) False.** Stable $y[n] = x[n]-x[n-1]$ maps the ramp $n\,u[n]$ to $u[n-1]$.
> - **(c) False.** $h[n] = u[n+1]$ is right-sided, $h[-1] = 1$.
> - **(d), (e):** DTFT, not on this term's Midterm 1.
>
> [[exams/midterm-1/true-false-bank|T/F bank]] Q4, Q17, Q7.

> [!trap]
> Right-sided ≠ causal; stability promises nothing for unbounded inputs. A guess is worth $+0.5$ on average.

## Problem 2 · System properties (12 pts)

> [!question] Problem 2 (12 pts)
> For each of the systems with input $x[n]$ and output $y[n]$ shown in the table, indicate by "yes" or "no" whether the properties indicated apply to the system. Note: you do not need to provide proofs/justification.
> - $y[n] = x[n] * (-1)^n u[n]$
> - $y[n] = \dfrac{x[n]}{x[2]}$
> - $y[n] = \cos^2\!\left(\tfrac{\pi}{2}n\right)x[n]$

> [!success]- Solution
> | system | Linear | Shift-invariant | Causal | Stable |
> |---|---|---|---|---|
> | $x[n] * (-1)^n u[n]$ | **Yes** | **Yes** | **Yes** | **No** |
> | $x[n]/x[2]$ | **No** | **No** | **No** | **No** |
> | $\cos^2(\tfrac\pi2 n)\,x[n]$ | **Yes** | **No** | **Yes** | **Yes** |
>
> - Row 1: LTI, $h = (-1)^n u[n]$ causal; $\sum\lvert h\rvert = \sum_{n\ge0} 1 = \infty$; $x = (-1)^n u[n]$ gives $y = (n+1)(-1)^n u[n]$.
> - Row 2: scaling $x$ leaves $y$ unchanged; stored $x[2]$ ⇒ time-varying; $y[0]$ needs $x[2]$; $x[2] = 0$ divides by zero.
> - Row 3: gain 1 (even $n$) or 0 (odd $n$): linear, memoryless, time-varying, gain ≤ 1.

> [!trap]
> $\lvert h[n]\rvert = 1$ bounded, $\sum\lvert h\rvert$ divergent. See [[exams/midterm-1/system-property-bank|system-property bank]].

## Problem 3 · Convolutions (15 pts)

> [!question] Problem 3 (15 pts)
> For each of the following parts, compute the convolution $x[n] * h[n]$ between the given sequences.
> - **(a)** $x[n] = \{\underset{\uparrow}{1}, -2, 2\}$, $h[n] = \{3, 1, \underset{\uparrow}{0}, 3, 1, 1\}$
> - **(b)** $x[n] = \left(-\tfrac12\right)^n u[n]$, $h[n] = \left(\tfrac23\right)^n u[n-1]$
> - **(c)** $x[n] = \log(\lvert n\rvert + 1)$, $h[n] = u[n+1] - u[n-2]$
>
> (The arrow marks $n = 0$: $x$ starts at $n = 0$, $h$ starts at $n = -2$.)

> [!success]- Solution
> **(a)** Start $0 + (-2) = -2$, $3 + 6 - 1 = 8$ samples:
> $$
> y[n] = \{3,\ -5,\ \underset{\uparrow}{4},\ 5,\ -5,\ 5,\ 0,\ 2\}\quad(n = -2,\dots,5).
> $$
> Check: $\sum y = 9 = (\sum x)(\sum h) = 1\cdot 9$.
>
> **(b)** $0 \le k \le n-1$:
> $$
> y[n] = \sum_{k=0}^{n-1}\left(-\tfrac12\right)^k\left(\tfrac23\right)^{n-k} = \left(\tfrac23\right)^n\sum_{k=0}^{n-1}\left(-\tfrac34\right)^k = \left(\tfrac23\right)^n\frac{1-(-\frac34)^n}{1+\frac34},\qquad n \ge 1,
> $$
> $$
> \boxed{y[n] = \tfrac47\left[\left(\tfrac23\right)^n - \left(-\tfrac12\right)^n\right]u[n-1]}
> $$
> (0 at $n = 0$, so $u[n]$ also correct. z-domain: $Y = \dfrac{\frac23 z^{-1}}{(1+\frac12 z^{-1})(1-\frac23 z^{-1})}$, coefficients $\tfrac47$, $-\tfrac47$.)
>
> **(c)** $h = \delta[n+1]+\delta[n]+\delta[n-1]$:
> $$
> \boxed{y[n] = \log(\lvert n+1\rvert+1) + \log(\lvert n\rvert+1) + \log(\lvert n-1\rvert+1)}
> $$

> [!trap]
> - (a): first index = sum of start indices. (b): keep $u[n-1]$. (c): three ones; $x$ is two-sided, no steps in the answer.

## Problem 4 · $h[n]$ from two input–output pairs (6 pts)

> [!question] Problem 4 (6 pts)
> An LTI system with unit pulse response $h[n]$ has the following input–output relationships:
> $$
> x_1[n] * h[n] = y_1[n],\qquad x_2[n] * h[n] = y_2[n],
> $$
> where $x_1[n] = \{\underset{\uparrow}{1}, 3, 6, -3\}$ and $x_2[n] = \{\underset{\uparrow}{1}, 2, -1, 0\}$. Determine $h[n]$ in terms of $y_1[n]$ and $y_2[n]$.

> [!success]- Solution
> $3x_2[n-1] = \{\underset{\uparrow}{0}, 3, 6, -3\}$:
> $$
> x_1[n] - 3x_2[n-1] = \delta[n].
> $$
> $$
> \boxed{h[n] = y_1[n] - 3\,y_2[n-1]}
> $$

> [!trap]
> Delayed input ⇒ $y_2[n-1]$ ([[problems/finding-h-from-input-output-pairs|finding h]]).

## Problem 5 · LCCDE, a cancelling input, stability (20 pts)

> [!question] Problem 5 (20 pts)
> Consider a causal LTI system described by the following LCCDE:
> $$
> y[n] = y[n-1] + \tfrac34\,y[n-2] + x[n] - 4x[n-2].
> $$
> - **(a)** Determine the transfer function $H(z)$ and state the poles, zeros, and the ROC of this system.
> - **(b)** Calculate the system's response $y[n]$ to input $x[n] = 2\delta[n] - 3\delta[n-1]$.
> - **(c)** Is the system given by $H(z)$ BIBO stable? Justify your reasoning.

> [!success]- Solution
> **(a)** $y[n] - y[n-1] - \tfrac34 y[n-2] = x[n] - 4x[n-2]$:
> $$
> H(z) = \frac{1-4z^{-2}}{1 - z^{-1} - \frac34 z^{-2}} = \frac{1-4z^{-2}}{(1-\frac32 z^{-1})(1+\frac12 z^{-1})}.
> $$
> **Poles** $z = \tfrac32,\ -\tfrac12$. **Zeros** $z = \pm 2$. **ROC $\lvert z\rvert > \tfrac32$**.
>
> **(b)** $X(z) = 2 - 3z^{-1} = 2(1-\tfrac32 z^{-1})$ cancels $\tfrac32$:
> $$
> Y(z) = \frac{2(1-4z^{-2})}{1+\frac12 z^{-1}} = 2\cdot\frac{1}{1+\frac12 z^{-1}} - 8z^{-2}\cdot\frac{1}{1+\frac12 z^{-1}},\qquad \lvert z\rvert > \tfrac12,
> $$
> $$
> \boxed{y[n] = 2\left(-\tfrac12\right)^n u[n] - 8\left(-\tfrac12\right)^{n-2}u[n-2]}
> $$
> ($y[0] = 2$, $y[1] = -1$, $y[2] = -\tfrac{15}{2}$, then decaying.)
>
> **(c)** **No.** ROC $\lvert z\rvert > \tfrac32$ misses the unit circle.

> [!trap]
> - Sign flips moving $y$ terms left. A decaying output from (b) doesn't contradict (c) ([[problems/unbounded-outputs-and-pole-matching|pole matching]]).

## Problem 6 · $H = Y/X$, PFE, difference equation (20 pts)

> [!question] Problem 6 (20 pts)
> Suppose that the input $x[n]$ to **a causal and stable LTI system** produces the output $y[n]$. The z-transform of $x[n]$ and $y[n]$ is given below:
> $$
> X(z) = \frac{1}{(1-2z^{-1})(1-z^{-1})},\qquad Y(z) = \frac{1}{(1-\frac12 z^{-1})(1-z^{-1})(1-\frac14 z^{-1})}.
> $$
> - **(a)** Find the transfer function $H(z)$ and its ROC.
> - **(b)** Find the unit pulse response $h[n]$.
> - **(c)** Determine the difference equation of the system.

> [!success]- Solution
> **(a)** $(1-z^{-1})$ cancels:
> $$
> \begin{aligned}
> H(z) &= \frac{Y(z)}{X(z)} = \frac{(1-2z^{-1})(1-z^{-1})}{(1-\frac12 z^{-1})(1-z^{-1})(1-\frac14 z^{-1})}\\
> &= \boxed{\frac{1-2z^{-1}}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})},\quad \lvert z\rvert > \tfrac12}
> \end{aligned}
> $$
> Causal; contains $\lvert z\rvert = 1$ (stable).
>
> **(b)** $A = \dfrac{1-2z^{-1}}{1-\frac14 z^{-1}}\Big|_{z^{-1}=2} = \dfrac{-3}{1/2} = -6$, $B = \dfrac{1-2z^{-1}}{1-\frac12 z^{-1}}\Big|_{z^{-1}=4} = \dfrac{-7}{-1} = 7$:
> $$
> \boxed{h[n] = -6\left(\tfrac12\right)^n u[n] + 7\left(\tfrac14\right)^n u[n]}
> $$
> Check: $h[0] = 1 = H(\infty)$.
>
> **(c)** $1 - \frac34 z^{-1} + \frac18 z^{-2}$:
> $$
> \boxed{y[n] = \tfrac34\,y[n-1] - \tfrac18\,y[n-2] + x[n] - 2x[n-1]}
> $$

> [!warning] Answer-key erratum (#6c)
> The key writes $-\frac18 y[n-1]$; it must be $-\frac18\,y[n-2]$. See [[0-toolkit/05-errata|Errata]].

> [!trap]
> - Cover-up: $z^{-1} = 1/p$. Same $H(z)$ as [[exams/midterm-1/past-exams/fall-2019|FA2019 #10]].

## Problem 7 · Bounded and unbounded inputs and outputs (9 pts)

> [!question] Problem 7 (9 pts)
> The transfer function of a causal LTI system is given below:
> $$
> H(z) = \frac{z-3}{z-4},\qquad \text{ROC: } \lvert z\rvert > 4.
> $$
> - **(a)** Find a **bounded** input $x[n]$ that will produce an **unbounded** output $y[n]$.
> - **(b)** Find an **unbounded** input $x[n]$ that will produce a **bounded** output $y[n]$.
> - **(c)** Find a **bounded** input $x[n]$ that will produce a **bounded** output $y[n]$.

> [!success]- Solution
> $H(z) = \dfrac{1-3z^{-1}}{1-4z^{-1}}$: pole 4 (unstable), zero 3. Key's answers (many accepted):
>
> **(a)** $x[n] = \delta[n]$: $y = h[n] = 4^n u[n] - 3\cdot4^{n-1}u[n-1] = \delta[n] + 4^{n-1}u[n-1]$, unbounded. (Also e.g. $u[n]$.)
>
> **(b)** $X = 1/H = \dfrac{z-4}{z-3} = \dfrac{1-4z^{-1}}{1-3z^{-1}}$, $\lvert z\rvert > 3$:
> $$
> \begin{gathered}
> x[n] = 3^n u[n] - 4\cdot3^{n-1}u[n-1] = \delta[n] - 3^{n-1}u[n-1]\ \ (\text{unbounded}),\\
> \boxed{y[n] = \delta[n]}.
> \end{gathered}
> $$
>
> **(c)** $x[n] = \delta[n] - 4\delta[n-1]$, $Y = 1-3z^{-1}$:
> $$
> \boxed{y[n] = \delta[n] - 3\delta[n-1]}
> $$

> [!trap]
> Bounded out from an unstable system needs a zero on $z = 4$; $u[n]$ doesn't do it.

## Problems 8 and 9 · DTFT (4 + 4 pts)

> [!note] DTFT: not on this term's Midterm 1
> #8: which sequence has $X_d(\omega) = 1 + 2\cos(2\omega) - 2j\sin(4\omega)$. #9: $\{x[n]\}_{n=-1}^{2} = \{1-j,\ 1,\ -1-j,\ 2j\}$, find $X_d(0)$, $X_d(\pi/2)$. See [[3-fourier-analysis/index|beyond Midterm 1]].

### Sources for this page

Official typed key, ECE 310 Midterm Exam, Spring 2023; lectures [[1-signals-and-systems/04-impulse-response-and-convolution|4]], [[2-z-transform/09-transfer-functions|9]], [[2-z-transform/11-bibo-stability-and-causality|11]].
