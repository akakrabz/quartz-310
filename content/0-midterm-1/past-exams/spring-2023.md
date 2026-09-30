---
title: "Spring 2023 · Midterm 1"
description: "ECE 310 Spring 2023 Midterm 1 (Liang, Moon, Snyder), every problem typed out with a folded worked solution and the traps: T/F, property table, three convolutions, h from two input–output pairs, an LCCDE with an input that cancels the unstable pole, H = Y/X with PFE, and bounded/unbounded input–output pairs. Includes one key erratum."
tags: [exam, midterm-1]
---

*Wednesday, March 1, 2023 · 7:00–9:00 pm · Profs. Liang, Moon, Snyder · 9 problems, 100 points (problems 8 and 9, 8 pts, are DTFT and not on the Fall 2026 Midterm 1) · one handwritten two-sided 8.5″ × 11″ sheet, no books, no calculator · "calculate / determine / find" means a closed form (no sums or integrals)*

| # | pts | what it asks | problem family | lectures |
|---|---|---|---|---|
| 1 | 10 | True/False: $h$ and LTI, BIBO with an unbounded input, right-sided vs causal (+ two DTFT items) | [[0-midterm-1/true-false-bank\|True/False bank]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 2 | 12 | Linear / shift-invariant / causal / stable table, 3 systems | [[problems/classifying-system-properties\|Classifying properties]] · [[0-midterm-1/system-property-bank\|bank]] | [[1-signals-and-systems/03-system-properties\|L3]], [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 3 | 15 | (a) finite convolution with $n=0$ bookkeeping; (b) two one-sided exponentials; (c) a 3-tap box against $\log(\lvert n\rvert+1)$ | [[problems/finite-length-convolution\|Finite]] (a) · [[problems/infinite-length-convolution\|Infinite]] (b, c) | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 4 | 6 | $h[n]$ from two input–output pairs | [[problems/finding-h-from-input-output-pairs\|Finding h]] | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] |
| 5 | 20 | LCCDE → $H(z)$, poles, zeros, ROC; response to an input that cancels the unstable pole; stability | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z)]] | [[2-z-transform/09-transfer-functions\|L9]]–[[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 6 | 20 | $H = Y/X$ and its ROC; PFE for $h[n]$; the difference equation | [[problems/finding-h-from-input-output-pairs\|Finding H]] · [[problems/all-possible-rocs\|PFE]] · [[problems/lccde-to-transfer-function-and-response\|LCCDE]] | [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/09-transfer-functions\|L9]] |
| 7 | 9 | Bounded/unbounded inputs and outputs for $H(z) = \frac{z-3}{z-4}$ | [[problems/unbounded-outputs-and-pole-matching\|Pole matching]] | [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]], [[2-z-transform/11-bibo-stability-and-causality\|L11]] |
| 8 | 4 | DTFT: not on the Fall 2026 Midterm 1 | — | [[3-beyond-midterm-1/index\|L13]] |
| 9 | 4 | DTFT: not on the Fall 2026 Midterm 1 | — | [[3-beyond-midterm-1/index\|L13]] |

## Problem 1 · True/False (10 pts)

> [!question] Problem 1 (10 pts)
> Answer **True** or **False** to each of the following statements: *Grading:* Correct answer = 2 pt.; Incorrect answer = −1 pt. No answer = 0 pts.
> - **(a)** If the system response $y[n]$ of a discrete-time system to any possible input signal $x[n]$ is fully described by its unit pulse response, then the system must be LTI.
> - **(b)** If a system is BIBO stable, any unbounded input will produce an unbounded output.
> - **(c)** If a system has a right-sided unit pulse response, then it must be causal.
> - **(d)** The DTFT, $X_d(\omega)$, of a sequence $x[n]$ is always related to its z-transform $X(z)$ by $X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$.
> - **(e)** If $x[n]$ is a real-valued sequence, then $\lvert X_d(\omega)\rvert$ is an even function.

> [!success]- Solution
> - **(a) True.** "Fully described by $h$ for every input" means $y = x*h$, and a convolution system is linear and time-invariant.
> - **(b) False.** BIBO says nothing about unbounded inputs. The stable first difference $y[n] = x[n]-x[n-1]$ maps the ramp $n\,u[n]$ to $u[n-1]$.
> - **(c) False.** Right-sided allows a start at a negative index: $h[n] = u[n+1]$ is right-sided, but $h[-1] = 1$ makes it non-causal.
> - **(d), (e):** DTFT, not on the Fall 2026 Midterm 1.
>
> More statements like these, grouped by topic: [[0-midterm-1/true-false-bank|True/False bank]] (Q4, Q17, Q7).

> [!trap]
> "Right-sided" is not "causal", and "stable" is a promise about **bounded** inputs only. The −1 per wrong answer still leaves a guess worth $+0.5$ on average.

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
> - Convolution with a fixed $h$ is LTI. $h[n] = (-1)^n u[n]$ is zero for $n<0$ (causal), but $\sum\lvert h\rvert = \sum_{n\ge0} 1 = \infty$ (unstable). The bounded input $x = (-1)^n u[n]$ gives $y = (n+1)(-1)^n u[n]$.
> - $x[n]/x[2]$: scaling $x$ by $a$ leaves $y$ unchanged, so it is not homogeneous. The stored sample $x[2]$ makes it time-varying, and $y[0]$ needs the future $x[2]$. The bounded input with $x[2] = 0$ divides by zero, so it is unstable.
> - $\cos^2(\tfrac\pi2 n)$ is 1 for even $n$ and 0 for odd $n$: an $n$-dependent gain. That is linear and memoryless, time-varying ($\delta[n]$ passes but $\delta[n-1]$ is blocked), and stable since the gain is at most 1.

> [!trap]
> $\lvert h[n]\rvert = 1$ is **bounded**, but the system is still unstable because $\sum\lvert h\rvert$ diverges. All three systems are in the [[0-midterm-1/system-property-bank|system-property bank]] with the fast rules.

## Problem 3 · Convolutions (15 pts)

> [!question] Problem 3 (15 pts)
> For each of the following parts, compute the convolution $x[n] * h[n]$ between the given sequences.
> - **(a)** $x[n] = \{\underset{\uparrow}{1}, -2, 2\}$, $h[n] = \{3, 1, \underset{\uparrow}{0}, 3, 1, 1\}$
> - **(b)** $x[n] = \left(-\tfrac12\right)^n u[n]$, $h[n] = \left(\tfrac23\right)^n u[n-1]$
> - **(c)** $x[n] = \log(\lvert n\rvert + 1)$, $h[n] = u[n+1] - u[n-2]$
>
> (The arrow marks $n = 0$: $x$ starts at $n = 0$, $h$ starts at $n = -2$.)

> [!success]- Solution
> **(a)** The output starts at $n = 0 + (-2) = -2$ and has $3 + 6 - 1 = 8$ samples. Slide, or use the matrix form $y = \mathbf{H}x$ with the columns of $\mathbf{H}$ being shifted copies of $h$:
> $$
> y[n] = \{3,\ -5,\ \underset{\uparrow}{4},\ 5,\ -5,\ 5,\ 0,\ 2\}\quad(n = -2,\dots,5).
> $$
> Check: $\sum y = 9 = (\sum x)(\sum h) = 1\cdot 9$.
>
> **(b)** Both signals are one-sided, so the sum has finite limits. $u[k]$ needs $k \ge 0$, and $u[n-k-1]$ needs $k \le n-1$:
> $$
> y[n] = \sum_{k=0}^{n-1}\left(-\tfrac12\right)^k\left(\tfrac23\right)^{n-k} = \left(\tfrac23\right)^n\sum_{k=0}^{n-1}\left(-\tfrac34\right)^k = \left(\tfrac23\right)^n\frac{1-(-\frac34)^n}{1+\frac34},\qquad n \ge 1,
> $$
> $$
> \boxed{y[n] = \tfrac47\left[\left(\tfrac23\right)^n - \left(-\tfrac12\right)^n\right]u[n-1]}
> $$
> The formula is 0 at $n = 0$, so $u[n]$ would be equally correct. The z-domain route gives the same result: $Y = \dfrac{\frac23 z^{-1}}{(1+\frac12 z^{-1})(1-\frac23 z^{-1})}$ with cover-up coefficients $\tfrac47$ (pole $\tfrac23$) and $-\tfrac47$ (pole $-\tfrac12$).
>
> **(c)** $h[n] = u[n+1]-u[n-2] = \delta[n+1]+\delta[n]+\delta[n-1]$ (ones at $n = -1, 0, 1$), so $y[n] = x[n+1]+x[n]+x[n-1]$:
> $$
> \boxed{y[n] = \log(\lvert n+1\rvert+1) + \log(\lvert n\rvert+1) + \log(\lvert n-1\rvert+1)}
> $$

> [!trap]
> - (a) The index of the first output sample is the **sum of the two start indices**, here $-2$. Most lost points are an arrow in the wrong place.
> - (b) The factor $(\frac23)^{n-k}$ must keep $n-k$: pull $(\frac23)^n$ out and combine $(-\frac12)^k(\frac23)^{-k} = (-\frac34)^k$. Do not drop $u[n-1]$.
> - (c) $u[n+1]-u[n-2]$ has **three** ones ($n = -1, 0, 1$); $u[n-2]$ switches on at $n = 2$. $x[n]$ is two-sided, so no step functions appear in the answer.

## Problem 4 · $h[n]$ from two input–output pairs (6 pts)

> [!question] Problem 4 (6 pts)
> An LTI system with unit pulse response $h[n]$ has the following input–output relationships:
> $$
> x_1[n] * h[n] = y_1[n],\qquad x_2[n] * h[n] = y_2[n],
> $$
> where $x_1[n] = \{\underset{\uparrow}{1}, 3, 6, -3\}$ and $x_2[n] = \{\underset{\uparrow}{1}, 2, -1, 0\}$. Determine $h[n]$ in terms of $y_1[n]$ and $y_2[n]$.

> [!success]- Solution
> Build $\delta[n]$ out of the inputs. $3x_2[n-1] = \{\underset{\uparrow}{0}, 3, 6, -3\}$ matches $x_1$ everywhere except $n = 0$:
> $$
> x_1[n] - 3x_2[n-1] = \delta[n].
> $$
> By linearity and time-invariance, $h = h*\delta = h*x_1 - 3\,(h*x_2)[n-1]$:
> $$
> \boxed{h[n] = y_1[n] - 3\,y_2[n-1]}
> $$

> [!trap]
> Delaying the input by one sample delays the output by one sample, so write $y_2[n-1]$, not $y_2[n]$. The pattern (combine shifted inputs into $\delta[n]$) is the whole [[problems/finding-h-from-input-output-pairs|finding-h family]].

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
> **(a)** Move the $y$ terms to the left, $y[n] - y[n-1] - \tfrac34 y[n-2] = x[n] - 4x[n-2]$, and transform:
> $$
> H(z) = \frac{1-4z^{-2}}{1 - z^{-1} - \frac34 z^{-2}} = \frac{1-4z^{-2}}{(1-\frac32 z^{-1})(1+\frac12 z^{-1})}.
> $$
> **Poles** $z = \tfrac32,\ -\tfrac12$ (roots of $z^2 - z - \tfrac34$). **Zeros** $z = \pm 2$. Causal, so the **ROC is $\lvert z\rvert > \tfrac32$**.
>
> **(b)** $X(z) = 2 - 3z^{-1} = 2(1-\tfrac32 z^{-1})$ cancels the pole at $\tfrac32$:
> $$
> Y(z) = \frac{2(1-4z^{-2})}{1+\frac12 z^{-1}} = 2\cdot\frac{1}{1+\frac12 z^{-1}} - 8z^{-2}\cdot\frac{1}{1+\frac12 z^{-1}},\qquad \lvert z\rvert > \tfrac12,
> $$
> $$
> \boxed{y[n] = 2\left(-\tfrac12\right)^n u[n] - 8\left(-\tfrac12\right)^{n-2}u[n-2]}
> $$
> ($y[0] = 2$, $y[1] = -1$, $y[2] = -\tfrac{15}{2}$, then decaying.)
>
> **(c)** **No.** The ROC $\lvert z\rvert > \tfrac32$ does not contain the unit circle: a causal system with a pole outside the unit circle is unstable.

> [!trap]
> - Sign flips: the $y$ terms change sign when moved left. The denominator is $1 - z^{-1} - \frac34 z^{-2}$, not $1 + z^{-1} + \frac34 z^{-2}$.
> - (b) produced a **decaying** output from an **unstable** system. That does not contradict (c): stability asks about *every* bounded input, and this particular input's zero at $\tfrac32$ cancels the bad pole. This is the [[problems/unbounded-outputs-and-pole-matching|pole-matching]] idea.
> - Keep $z^{-2}$ as a two-sample delay: $-8z^{-2}\cdot\frac{1}{1+\frac12 z^{-1}} \leftrightarrow -8(-\frac12)^{n-2}u[n-2]$, not $(-\frac12)^n$.

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
> H(z) = \frac{Y(z)}{X(z)} = \frac{(1-2z^{-1})(1-z^{-1})}{(1-\frac12 z^{-1})(1-z^{-1})(1-\frac14 z^{-1})} = \boxed{\frac{1-2z^{-1}}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})},\quad \lvert z\rvert > \tfrac12}
> $$
> The ROC is causal (outside the largest pole). It contains $\lvert z\rvert = 1$, which is consistent with "stable".
>
> **(b)** $H = \dfrac{A}{1-\frac12 z^{-1}} + \dfrac{B}{1-\frac14 z^{-1}}$ with cover-up:
> $A = \dfrac{1-2z^{-1}}{1-\frac14 z^{-1}}\Big|_{z^{-1}=2} = \dfrac{-3}{1/2} = -6$ and $B = \dfrac{1-2z^{-1}}{1-\frac12 z^{-1}}\Big|_{z^{-1}=4} = \dfrac{-7}{-1} = 7$.
> $$
> \boxed{h[n] = -6\left(\tfrac12\right)^n u[n] + 7\left(\tfrac14\right)^n u[n]}
> $$
> Check: $h[0] = 1 = H(\infty)$.
>
> **(c)** Denominator $(1-\frac12 z^{-1})(1-\frac14 z^{-1}) = 1 - \frac34 z^{-1} + \frac18 z^{-2}$, so $y[n] - \frac34 y[n-1] + \frac18 y[n-2] = x[n] - 2x[n-1]$:
> $$
> \boxed{y[n] = \tfrac34\,y[n-1] - \tfrac18\,y[n-2] + x[n] - 2x[n-1]}
> $$

> [!warning] Answer-key erratum (#6c)
> The official key writes $y[n] = \frac34 y[n-1] - \frac18 y[n-1] + x[n] - 2x[n-1]$, with $y[n-1]$ twice. The second term is $-\frac18\,y[n-2]$, as above; the typo would describe a different, first-order system. Listed on [[0-toolkit/05-errata|Errata]].

> [!trap]
> - "Causal **and** stable" fixes the ROC of $H$ even though $X$ and $Y$ come without ROCs.
> - In the cover-up, substitute $z^{-1} = 1/p$ (here 2 and 4), not $z^{-1} = p$.
> - The same $H(z)$ reappears as [[0-midterm-1/past-exams/fall-2019|FA2019 #10]].

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
> Write $H(z) = \dfrac{1-3z^{-1}}{1-4z^{-1}}$: a pole at 4 (outside the unit circle, causal ⇒ unstable) and a zero at 3. Many answers are accepted; these are the key's.
>
> **(a)** $x[n] = \delta[n]$ gives $y = h[n] = 4^n u[n] - 3\cdot4^{n-1}u[n-1] = \delta[n] + 4^{n-1}u[n-1]$, which is unbounded. (Any bounded causal input with $X(4) \ne 0$ works, e.g. $u[n]$: the pole at 4 survives in $Y$.)
>
> **(b)** Choose $X = 1/H$: $X(z) = \dfrac{z-4}{z-3} = \dfrac{1-4z^{-1}}{1-3z^{-1}}$, $\lvert z\rvert > 3$, so
> $$
> x[n] = 3^n u[n] - 4\cdot3^{n-1}u[n-1] = \delta[n] - 3^{n-1}u[n-1]\ \ (\text{unbounded}),\qquad \boxed{y[n] = \delta[n]}.
> $$
>
> **(c)** Cancel the pole with a finite input: $X(z) = 1 - 4z^{-1}$, i.e. $x[n] = \delta[n] - 4\delta[n-1]$, gives $Y = 1-3z^{-1}$:
> $$
> \boxed{y[n] = \delta[n] - 3\delta[n-1]}
> $$

> [!trap]
> "Bounded in, bounded out" for an **unstable** system needs the input to put a **zero on the unstable pole** ($z = 4$). An input like $u[n]$ does not: its own pole at 1 leaves the pole at 4 in $Y$, so the output still grows like $4^n$. See [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]].

## Problems 8 and 9 · DTFT (4 + 4 pts)

> [!note] DTFT: not on the Fall 2026 Midterm 1
> **#8** asked which sequence has DTFT $X_d(\omega) = 1 + 2\cos(2\omega) - 2j\sin(4\omega)$ (multiple choice). **#9** gave $\{x[n]\}_{n=-1}^{2} = \{1-j,\ 1,\ -1-j,\ 2j\}$ and asked for $X_d(0)$ and $X_d(\pi/2)$ without computing $X_d(\omega)$ everywhere. Both belong to Lectures 13–14; see [[3-beyond-midterm-1/index|beyond Midterm 1]].

### Sources for this page

- Official solutions, ECE 310 Midterm Exam, Spring 2023 (typed key); the problem statements are typed from the same file.
- Every answer above is checked in `verify/exams/sp23.py` (26 checks: `np.convolve` with index bookkeeping, direct sums vs closed forms, `residuez`, exact rational `lfilter`-style recursions for the pole-cancelling inputs).
- Related lectures: [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/08-inverse-z-transform|Lecture 8]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]].
