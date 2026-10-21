---
title: "HW2 · System properties, convolution, and the impulse response"
description: "ECE 310 Homework 2 (due Sep 11) with folded solutions: properties of two recursions and a time-varying gain, convolution ⇒ LSI, output from the step response, h[n] from one input–output pair, five convolutions."
tags: [homework, midterm-1, systems, convolution, lccde]
---

*Homework 2 · due Fri Sep 11, 2026 · covers [[1-signals-and-systems/03-system-properties|Lecture 3]] (system properties), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (impulse response and convolution), [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] (difference equations, "at rest") · 100 pts · official solutions v1.0 · prev: [[homework/hw1|HW1]] · next: [[homework/hw3|HW3]] · all sets: [[homework/index|Homework]]*

> [!abstract] In one breath
> - A recursion is LTI only at initial rest; an $n$-dependent coefficient makes a system time-varying.
> - Convolution ⇔ LTI; $h[n] = g[n] - g[n-1]$.
> - Find $h$ by building $\delta[n]$ from shifted inputs; convolve with bookkeeping, geometric sums, or "diverges".

| # | Pts | Skill | Links |
|---|---|---|---|
| 1 | 18 | Linearity, time invariance of recursions and a gain | [[problems/classifying-system-properties\|classifying system properties]] |
| 2 | 20 | Prove $y = h * x$ is LSI | [[concepts/lti-system\|LTI system]] |
| 3 | 20 | Output from the step response | [[concepts/step-response\|step response]] |
| 4 | 22 | $h[n]$ from one input–output pair | [[problems/finding-h-from-input-output-pairs\|finding h from input–output pairs]] |
| 5 | 20 | Five convolutions | [[problems/finite-length-convolution\|finite-length]], [[problems/infinite-length-convolution\|infinite-length convolution]] |

## Problem 1 · Linearity and time invariance of three systems

> [!question] Problem 1 (18 pts)
> The following systems are specified by input–output relations, where $x[n]$ is the input and $y[n]$ the output (the assignment says "two systems" but lists three):
>
> - (a) $y[n] = y[n-5] + x[n] + 10x[n-1]$
> - (b) $y[n-2] + 2y[n] = \cos\!\left(\tfrac{\pi}{6}n\right)x[n]$
> - (c) $y[n] = \left(\tfrac12\right)^{\lvert n\rvert} x[n]$
>
> For each system, determine if it is (a) linear or non-linear, (b) time-invariant or time-varying. Justify your answers with proofs or counterexamples.

> [!success]- Solution
> Recursions (a), (b) assume **initial rest** ([[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]]).
>
> **(a) Linear, time-invariant.** If $y_1$, $y_2$ are the at-rest responses to $x_1$, $x_2$, then $\alpha y_1 + \beta y_2$ is at rest and satisfies
>
> $$
> \begin{aligned}
> (\alpha y_1 + \beta y_2)[n] &- (\alpha y_1 + \beta y_2)[n-5]\\
> &= (\alpha x_1 + \beta x_2)[n] + 10\,(\alpha x_1 + \beta x_2)[n-1].
> \end{aligned}
> $$
>
> Coefficients $1, 1, 10$ are constant, so $y[n-n_0]$ is the at-rest response to $x[n-n_0]$.
>
> **(b) Linear, time-varying.** $y[n] = -\tfrac12 y[n-2] + \tfrac12\cos(\tfrac{\pi}{6}n)\,x[n]$; superposition as in (a). $\delta[n]$ gives $y[0] = \tfrac12$ (nonzero response); $\delta[n-3]$ meets $\cos(\tfrac{\pi}{2}) = 0$, so its response is zero.
>
> **(c) Linear, time-varying.** Fixed gain $(1/2)^{\lvert n\rvert}$ is linear. $\delta[n] \mapsto \delta[n]$, but $\delta[n-1] \mapsto \tfrac12\delta[n-1] \ne \delta[n-1]$.
>
> | System | L | TI | C | S | Why the last two |
> |---|---|---|---|---|---|
> | (a) $y[n] = y[n-5] + x[n] + 10x[n-1]$ | Y | Y | Y | **N** | $h = \{\underset{\uparrow}{1}, 10, 0, 0, 0, 1, 10, 0, 0, 0, \dots\}$ never decays; poles = 5th roots of unity |
> | (b) $y[n-2] + 2y[n] = \cos(\tfrac{\pi}{6}n)\,x[n]$ | Y | N | Y | Y | $\lvert x\rvert \le 1 \Rightarrow \lvert y[n]\rvert \le \tfrac12\lvert y[n-2]\rvert + \tfrac12 \le 1$ |
> | (c) $y[n] = (\tfrac12)^{\lvert n\rvert} x[n]$ | Y | N | Y | Y | memoryless; gain at most 1 |

> [!note] Official argument incomplete
> The key checks superposition on the right-hand side only. Without initial rest, (a) with $y[-5] = 1$ and $x \equiv 0$ gives $y[0] = 1$: not linear.

**On the exam:** $\lvert n\rvert\,x[n]$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #2]], Y N Y N); every row in the [[exams/midterm-1/system-property-bank|system-property bank]].

## Problem 2 · Every convolution system is LSI

> [!question] Problem 2 (20 pts)
> The output $y[n]$ of a given system is always related to its input $x[n]$ by $y[n] = h[n] * x[n]$, where $h[n]$ is the system's unit pulse response. Show that the system must be LSI.

> [!success]- Solution
> $T\{x\}[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]$.
>
> **Linear:**
>
> $$
> \begin{aligned}
> T\{\alpha x_1 + \beta x_2\}[n] &= \sum_{k}\big(\alpha x_1[k] + \beta x_2[k]\big)\,h[n-k]\\
> &= \alpha\sum_k x_1[k]\,h[n-k] + \beta\sum_k x_2[k]\,h[n-k]\\
> &= \alpha\,y_1[n] + \beta\,y_2[n].
> \end{aligned}
> $$
>
> **Shift-invariant:** $x_s[n] = x[n-n_0]$, $m = k - n_0$:
>
> $$
> T\{x_s\}[n] = \sum_{k} x[k-n_0]\,h[n-k] = \sum_{m} x[m]\,h[(n-n_0)-m] = y[n-n_0].
> $$
>
> Converse ([[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]): LTI ⇒ $y = h * x$ with $h = T\{\delta\}$. $h$ characterizes a system only if it is LTI.

**On the exam:** any convolution row is L = Y, TI = Y, e.g. $x[n] * 2^n u[-n]$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #2]], Y Y N Y).

## Problem 3 · The output from the step response

> [!question] Problem 3 (20 pts)
> Express the output $y[n]$ of an LSI system with unit pulse response $h[n]$ in terms of its step response $g[n] = h[n] * u[n]$ and the input $x[n]$. *Hint:* try to represent $\delta[n]$ in terms of shifted versions of $u[n]$.

> [!success]- Solution
> $\delta[n] = u[n] - u[n-1]$, so
>
> $$
> h[n] = h[n] * \delta[n] = h[n] * u[n] - h[n] * u[n-1] = g[n] - g[n-1].
> $$
>
> $$
> \begin{aligned}
> y[n] = h[n] * x[n] &= \big(g[n] - g[n-1]\big) * x[n]\\
> &= g[n] * x[n] - g[n] * x[n-1],
> \end{aligned}
> $$
>
> $$
> \boxed{\,y[n] = g[n] * \big(x[n] - x[n-1]\big)\,}
> $$
>
> Also $g[n] = \sum_{k=-\infty}^{n} h[k]$.

**On the exam:** [[exams/midterm-1/past-exams/fall-2023|FA2023 #4]]: $g = \delta[n] + \delta[n-1] \Rightarrow h[n] = \delta[n] - \delta[n-2] = \{\underset{\uparrow}{1}, 0, -1\}$.

## Problem 4 · The impulse response from one input–output pair

> [!question] Problem 4 (22 pts)
> Assume that the zero-state response of an LSI system to the input $x[n] = 3^{-n}u[n]$ is $y[n] = \dfrac{1}{5^n}\,u[n-1]$. Use the system's properties (linearity and shift invariance) to find $h[n]$, the system's unit pulse response.

> [!success]- Solution
> **Step 1: $\delta[n]$ from shifted inputs** ($x[n] - a\,x[n-1] = \delta[n]$ for $x = a^n u[n]$, $a = \tfrac13$):
>
> $$
> \begin{aligned}
> x[n] - \tfrac13\,x[n-1] &= 3^{-n}u[n] - \tfrac13\,3^{-(n-1)}u[n-1]\\
> &= 3^{-n}\big(u[n] - u[n-1]\big) = 3^{-n}\,\delta[n] = \delta[n].
> \end{aligned}
> $$
>
> **Step 2: same combination of outputs:**
>
> $$
> \begin{aligned}
> h[n] = y[n] - \tfrac13\,y[n-1] &= \frac{1}{5^n}\,u[n-1] - \frac13\cdot\frac{1}{5^{n-1}}\,u[n-2]\\
> &= \frac{1}{5^n}\Big(u[n-1] - \frac53\,u[n-2]\Big).
> \end{aligned}
> $$
>
> $$
> \boxed{\,h[n] = \Big(\tfrac15\Big)^{n}\Big(u[n-1] - \tfrac53\,u[n-2]\Big) = \tfrac15\,\delta[n-1] - \tfrac23\Big(\tfrac15\Big)^{n}u[n-2]\,}
> $$
>
> $h[0] = 0$, $h[1] = \tfrac15$, $h[2] = -\tfrac{2}{75}$, $h[3] = -\tfrac{2}{375}$.
>
> **z-domain check** ([[2-z-transform/09-transfer-functions|Lecture 9]]): $X(z) = \dfrac{1}{1 - \frac13 z^{-1}}$, $Y(z) = \dfrac{\frac15 z^{-1}}{1 - \frac15 z^{-1}}$,
>
> $$
> H(z) = \frac{Y(z)}{X(z)} = \frac{\tfrac15 z^{-1}\big(1 - \tfrac13 z^{-1}\big)}{1 - \tfrac15 z^{-1}},\qquad \text{ROC: } \lvert z\rvert > \tfrac15.
> $$

**On the exam:** [[exams/midterm-1/past-exams/spring-2023|SP2023 #4]]: $x_1[n] - 3x_2[n-1] = \delta[n]$, so $h = y_1[n] - 3y_2[n-1]$.

## Problem 5 · Five convolutions

> [!question] Problem 5 (20 pts)
> Compute the convolution $x[n] * h[n]$ for the $x[n]$ and $h[n]$ given below (the arrow marks $n = 0$).
>
> - (a) $x[n] = \{-1,\ \underset{\uparrow}{0},\ 1\}$, $\ h[n] = \{\underset{\uparrow}{1},\ 2,\ 3,\ 4,\ 5\}$
> - (b) $x[n] = 3^{-n}u[n]$, $\ h[n] = \{\underset{\uparrow}{0},\ 1,\ 2\}$
> - (c) $x[n] = u[n]$, $\ h[n] = n\big(u[n] - u[n-4]\big)$
> - (d) $x[n] = (-1)^{-n}u[n]$, $\ h[n] = e^{-n}u[n]$
> - (e) $x[n] = 0.5^n u[n]$, $\ h[n] = 2^{-n}u[-n]$

> [!success]- (a) Solution
> Start $-1 + 0 = -1$, length $3 + 5 - 1 = 7$; $y[n] = -h[n+1] + h[n-1]$.
>
> | $n$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
> |---|---|---|---|---|---|---|---|
> | $-h[n+1]$ | $-1$ | $-2$ | $-3$ | $-4$ | $-5$ | $0$ | $0$ |
> | $h[n-1]$ | $0$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
> | $y[n]$ | $-1$ | $-2$ | $-2$ | $-2$ | $-2$ | $4$ | $5$ |
>
> $$
> x[n] * h[n] = \{-1,\ \underset{\uparrow}{-2},\ -2,\ -2,\ -2,\ 4,\ 5\}
> $$
>
> Sum check: $\sum y = \big(\sum x\big)\big(\sum h\big) = 0 \cdot 15 = 0$.

> [!success]- (b) Solution
> $h[n] = \delta[n-1] + 2\delta[n-2]$:
>
> $$
> \begin{aligned}
> x[n] * h[n] &= 3^{-(n-1)}u[n-1] + 2\cdot 3^{-(n-2)}u[n-2]\\
> &= 3^{-(n-1)}\big(u[n-1] + 6\,u[n-2]\big)\\
> &= \delta[n-1] + 7\Big(\tfrac13\Big)^{n-1}u[n-2].
> \end{aligned}
> $$
>
> $y[0] = 0$, $y[1] = 1$, $y[2] = \tfrac73$, $y[3] = \tfrac79$, …

> [!success]- (c) Solution
> $h = \{\underset{\uparrow}{0}, 1, 2, 3\} = \delta[n-1] + 2\delta[n-2] + 3\delta[n-3]$:
>
> $$
> x[n] * h[n] = u[n-1] + 2u[n-2] + 3u[n-3] = \{\underset{\uparrow}{0},\ 1,\ 3,\ 6,\ 6,\ 6,\ \dots\}.
> $$

> [!success]- (d) Solution
> $(-1)^{-k} = (-1)^k$; both causal, so for $n \ge 0$:
>
> $$
> y[n] = \sum_{k=0}^{n} (-1)^k e^{-(n-k)} = e^{-n}\sum_{k=0}^{n}(-e)^k = e^{-n}\,\frac{1 - (-e)^{n+1}}{1+e}.
> $$
>
> $$
> \boxed{\,x[n] * h[n] = \frac{e^{-n} + e\,(-1)^n}{1+e}\,u[n]\,}
> $$
>
> $y[0] = 1$, $y[1] = e^{-1} - 1$, $y[2] = 1 - e^{-1} + e^{-2}$.

> [!success]- (e) Solution
> $h[n-k] \ne 0$ needs $k \ge n$; each term:
>
> $$
> x[k]\,h[n-k] = 0.5^{k}\cdot 0.5^{\,n-k} = 0.5^{n}\qquad\text{for every } k \ge \max(0, n).
> $$
>
> Infinitely many equal terms: **the convolution diverges** for every $n$. No common ROC: $\lvert z\rvert > \tfrac12$ vs. $H(z) = \dfrac{1}{1 - 2z}$, $\lvert z\rvert < \tfrac12$.

> [!trap] Traps
> - An $n$ outside the brackets ($\cos(\tfrac{\pi}{6}n)$, $(1/2)^{\lvert n\rvert}$) makes a system time-varying; $x[n-1]$ does not.
> - Shift the step too: $y[n-1] = (\tfrac15)^{n-1}u[n-2]$; keeping $u[n-1]$ gives $h[1] = \tfrac15 - \tfrac13 = -\tfrac{2}{15}$.
> - $\sum r^k = \frac{1}{1-r}$ needs $\lvert r\rvert < 1$; in (e) the ratio is 1.

**On the exam:** finite convolution on 7/7 past midterms, infinite on 5/7; always run the sum check ([[0-toolkit/05-errata|errata]]: SP2025 #4(a) key sums to 7, not 8).

## Related

[[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]] · [[concepts/convolution|convolution]] · [[concepts/lccde|LCCDE]] · [[demos/convolution-explorer|convolution explorer]] · [[0-toolkit/02-geometric-series|geometric series]] · [[homework/hw3|HW3]]

### Sources for this page

ECE 310 Fall 2026 HW2 and official solutions v1.0; Lecture notes 3–5 (Snyder); past Midterm 1 exams cited above.
