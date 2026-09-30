---
title: "HW2 · System properties, convolution, and the impulse response"
description: "Verified walkthrough of ECE 310 Homework 2 (due Sep 11): linearity and time invariance of two recursions and a time-varying gain, why every convolution system is LSI, the output from the step response, h[n] from a single input–output pair, and five convolutions — finite, one-sided, geometric, and one that diverges."
tags: [homework, midterm-1, systems, convolution, lccde]
---

*Homework 2 · due Fri Sep 11, 2026 · covers [[1-signals-and-systems/03-system-properties|Lecture 3]] (system properties), [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] (impulse response and convolution), [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] (difference equations, "at rest") · 100 pts · official solutions v1.0, every answer re-checked in Python · prev: [[homework/hw1|HW1]] · next: [[homework/hw3|HW3]] · all sets: [[homework/index|Homework]]*

> [!abstract] What HW2 trains, in one breath
> The core of Unit 1. **Properties of real systems** (#1): a recursion is LTI only under initial rest, and a coefficient that depends on $n$ makes a system time-varying. **Why convolution** (#2–#3): a convolution system is automatically linear and shift-invariant, and $\delta[n] = u[n] - u[n-1]$ turns a step response into an impulse response. **Finding $h$** (#4): build $\delta[n]$ from shifted copies of the input, then apply the same recipe to the outputs. **Computing convolutions** (#5): index bookkeeping for finite sequences, geometric sums for one-sided ones, and recognising a sum that does not exist.

| # | Pts | Skill | Lecture | Problem family / concepts |
|---|---|---|---|---|
| 1 | 18 | Linearity and time invariance of two recursions and a time-varying gain | [[1-signals-and-systems/03-system-properties\|L3]], [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5]] | [[problems/classifying-system-properties\|classifying system properties]], [[concepts/lccde\|LCCDE]] |
| 2 | 20 | Prove that $y = h * x$ is linear and shift-invariant | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] | [[concepts/lti-system\|LTI system]], [[concepts/convolution\|convolution]] |
| 3 | 20 | The output from the step response: $y = g * (x[n] - x[n-1])$ | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] | [[concepts/step-response\|step response]], [[problems/finding-h-from-input-output-pairs\|finding h from input–output pairs]] |
| 4 | 22 | $h[n]$ from one input–output pair | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] | [[problems/finding-h-from-input-output-pairs\|finding h from input–output pairs]], [[concepts/impulse-response\|impulse response]] |
| 5 | 20 | Five convolutions: shifted copies, a table, geometric sums, divergence | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] | [[problems/finite-length-convolution\|finite-length convolution]], [[problems/infinite-length-convolution\|infinite-length convolution]] |

Every solution below is folded: read the question, answer it on paper, then open the solution.

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
> **Ground rule for (a) and (b).** A recursion defines $y[n]$ through earlier outputs, so it defines a system only once the initial conditions are fixed. The course convention ([[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]]) is **initial rest**: zero initial conditions, $y[n] = 0$ before the input starts. Everything below assumes it.
>
> **(a) Linear and time-invariant.** *Linearity:* let $y_1$, $y_2$ be the at-rest responses to $x_1$, $x_2$. Then $\alpha y_1 + \beta y_2$ is at rest and satisfies
>
> $$
> \begin{aligned}
> (\alpha y_1 + \beta y_2)[n] &- (\alpha y_1 + \beta y_2)[n-5]\\
> &= (\alpha x_1 + \beta x_2)[n] + 10\,(\alpha x_1 + \beta x_2)[n-1],
> \end{aligned}
> $$
>
> so it is the (unique) at-rest response to $\alpha x_1 + \beta x_2$. *Time invariance:* the coefficients $1, 1, 10$ do not depend on $n$, so $y[n-n_0]$ satisfies the same recursion with input $x[n-n_0]$ and is still at rest; it is therefore the response to the delayed input.
>
> **(b) Linear, time-varying.** Rewrite it as $y[n] = -\tfrac12 y[n-2] + \tfrac12\cos(\tfrac{\pi}{6}n)\,x[n]$. The superposition argument of (a) goes through unchanged, because the input enters multiplied by a *known* sequence and the outputs enter linearly. But the coefficient $\cos(\tfrac{\pi}{6}n)$ changes with $n$. Counterexample (the official one): $x[n] = \delta[n]$ puts $\cos(0)\,\delta[n] = \delta[n]$ on the right, so $y[0] = \tfrac12$ and the response is nonzero. The delayed input $\delta[n-3]$ puts $\cos(\tfrac{\pi}{2})\,\delta[n-3] = 0$ on the right, so its response is identically zero — not the delayed nonzero response.
>
> **(c) Linear, time-varying.** Multiplication by the fixed sequence $(1/2)^{\lvert n\rvert}$ is linear. Counterexample: $\delta[n] \mapsto \delta[n]$ (the gain at $n = 0$ is 1), but $\delta[n-1] \mapsto \tfrac12\delta[n-1]$, which is not the delayed output $\delta[n-1]$.
>
> **Exam-table rows** (linear · time-invariant · causal · stable), all four checked numerically:
>
> | System | L | TI | C | S | Why the last two |
> |---|---|---|---|---|---|
> | (a) $y[n] = y[n-5] + x[n] + 10x[n-1]$ | Y | Y | Y | **N** | $h = \{\underset{\uparrow}{1}, 10, 0, 0, 0, 1, 10, 0, 0, 0, \dots\}$ never decays; the poles are the 5th roots of unity |
> | (b) $y[n-2] + 2y[n] = \cos(\tfrac{\pi}{6}n)\,x[n]$ | Y | N | Y | Y | $\lvert x\rvert \le 1 \Rightarrow \lvert y[n]\rvert \le \tfrac12\lvert y[n-2]\rvert + \tfrac12 \le 1$ |
> | (c) $y[n] = (\tfrac12)^{\lvert n\rvert} x[n]$ | Y | N | Y | Y | memoryless; the gain is at most 1 |
>
> *Rubric (6 pts per system):* 3 for linearity and 3 for time invariance, each earned only with a proper justification.

> [!note] Where the official argument is incomplete
> For (a) and (b) the key checks superposition on the right-hand side only ("let $T(x[n]) = x[n] + 10x[n-1]$ be the system"). The verdicts are right, but the system is the whole recursion, and the argument needs initial rest: with $y[-5] = 1$ and $x \equiv 0$, system (a) produces $y[0] = 1$, a nonzero response to the zero input, which no linear system can do.

> [!trap] "It has an n in it, so it's time-varying"
> The $n$ inside $x[n-1]$ or $y[n-5]$ is just the time index. It is an $n$ *outside* the brackets — the $\cos(\tfrac{\pi}{6}n)$ in (b), the $(1/2)^{\lvert n\rvert}$ in (c) — that makes a system time-varying.

**On the exam:** the property table, on 7/7 past midterms ([[problems/classifying-system-properties|classifying system properties]]). Gains like (c): $\lvert n\rvert\,x[n]$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #2]], Y N Y **N**: that gain grows, so unlike (c) it is unstable), $\log(\lvert n\rvert + 1)\,x[n]$ ([[0-midterm-1/past-exams/fall-2023|FA2023 #2]], Y N Y N), $(0.8+0.8j)^n x[n]$ ([[0-midterm-1/past-exams/spring-2021|SP2021 #3]], Y N Y N). Recursions like (a) appear in T/F: [[0-midterm-1/past-exams/fall-2024|FA2024 1(e)]], $y[n] = y[n-3] + x[n]$ has three distinct poles (True). Every row: [[0-midterm-1/system-property-bank|system-property bank]].

## Problem 2 · Every convolution system is LSI

> [!question] Problem 2 (20 pts)
> The output $y[n]$ of a given system is always related to its input $x[n]$ by $y[n] = h[n] * x[n]$, where $h[n]$ is the system's unit pulse response. Show that the system must be LSI.

> [!success]- Solution
> Write the system as $T\{x\}[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]$.
>
> **Linear.** For any inputs $x_1, x_2$ and constants $\alpha, \beta$ the sum splits:
>
> $$
> \begin{aligned}
> T\{\alpha x_1 + \beta x_2\}[n] &= \sum_{k}\big(\alpha x_1[k] + \beta x_2[k]\big)\,h[n-k]\\
> &= \alpha\sum_k x_1[k]\,h[n-k] + \beta\sum_k x_2[k]\,h[n-k]\\
> &= \alpha\,y_1[n] + \beta\,y_2[n].
> \end{aligned}
> $$
>
> **Shift-invariant.** Feed $x_s[n] = x[n-n_0]$ and substitute $m = k - n_0$:
>
> $$
> T\{x_s\}[n] = \sum_{k} x[k-n_0]\,h[n-k] = \sum_{m} x[m]\,h[(n-n_0)-m] = y[n-n_0].
> $$
>
> The official solution runs the same argument with the sum written the other way round, $\sum_k h[k]\,x[n-k]$ (convolution commutes).
>
> *Rubric:* 10 points for each of the two proofs.

> [!key] Both directions
> Convolution ⇒ LTI is this problem. LTI ⇒ convolution with $h[n] = T\{\delta[n]\}$ is [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]]: write $x[n] = \sum_k x[k]\,\delta[n-k]$ and use linearity and shift invariance. So "LTI" and "a convolution with some $h$" are the same statement, and an impulse response characterizes a system **only** when the system is LTI.

**On the exam:** in the property table, any row written as a convolution is automatically **L = Y, TI = Y**; then read causality off "$h[n] = 0$ for $n < 0$" and stability off $\sum\lvert h[n]\rvert < \infty$: $x[n] * 2^n u[-n]$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #2]], Y Y N Y), $x[n] * j^n u[n]$ ([[0-midterm-1/past-exams/spring-2025|SP2025 #2]], Y Y Y N), $x[n] * u[n+1]$ ([[0-midterm-1/past-exams/fall-2023|FA2023 #2]], Y Y N N). The converse is a favorite T/F: "the output to any input is determined by $h[n]$" is **False** for a general system ([[0-midterm-1/past-exams/fall-2024|FA2024 1(a)]], [[0-midterm-1/past-exams/fall-2023|FA2023 1(d)]]), and so is "$\sum\lvert h[n]\rvert < \infty$ implies BIBO stable whether or not the system is LSI" ([[0-midterm-1/past-exams/spring-2025|SP2025 1(b)]]: $y[n] = n\,x[n]$ maps $\delta[n]$ to $0$, yet it is unstable).

## Problem 3 · The output from the step response

> [!question] Problem 3 (20 pts)
> Express the output $y[n]$ of an LSI system with unit pulse response $h[n]$ in terms of its step response $g[n] = h[n] * u[n]$ and the input $x[n]$. *Hint:* try to represent $\delta[n]$ in terms of shifted versions of $u[n]$.

> [!success]- Solution
> Start from the hint, $\delta[n] = u[n] - u[n-1]$. Convolving with $h$ and using the shift property,
>
> $$
> h[n] = h[n] * \delta[n] = h[n] * u[n] - h[n] * u[n-1] = g[n] - g[n-1].
> $$
>
> Then, by commutativity and associativity,
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
> that is, $y[n] = \sum_k g[k]\,\big(x[n-k] - x[n-k-1]\big)$: feed the step response the first difference of the input. (Checked numerically for random $h$ and $x$.)
>
> *Rubric:* 20 for the correct answer, 10 for a minor mistake with clear reasoning.

> [!key] Step response ↔ impulse response
> $g[n] = \sum_{k=-\infty}^{n} h[k]$ (running sum) and $h[n] = g[n] - g[n-1]$ (first difference).

**On the exam:** [[0-midterm-1/past-exams/fall-2023|FA2023 #4]] (5 pts): the response to $u[n]$ is $\delta[n] + \delta[n-1]$; which $h$? Take the first difference: $h[n] = g[n] - g[n-1] = \delta[n] - \delta[n-2] = \{\underset{\uparrow}{1}, 0, -1\}$, option (b). [[0-midterm-1/past-exams/fall-2019|FA2019 #3]] asks the other direction (the step response is the running sum of $h$), and [[0-midterm-1/past-exams/fall-2019|FA2019 T/F 1(j)]] rests on the hint itself: $u[n] * (\delta[n] - \delta[n-1]) = \delta[n]$ is a bounded output from an unstable system, so "any nonzero input gives an unbounded output" is False. See also [[concepts/step-response|step response]].

## Problem 4 · The impulse response from one input–output pair

> [!question] Problem 4 (22 pts)
> Assume that the zero-state response of an LSI system to the input $x[n] = 3^{-n}u[n]$ is $y[n] = \dfrac{1}{5^n}\,u[n-1]$. Use the system's properties (linearity and shift invariance) to find $h[n]$, the system's unit pulse response.

> [!success]- Solution
> **Step 1: build $\delta[n]$ from shifted copies of the input.** For $x[n] = a^n u[n]$ the combination $x[n] - a\,x[n-1]$ cancels everything except $n = 0$. With $a = \tfrac13$:
>
> $$
> \begin{aligned}
> x[n] - \tfrac13\,x[n-1] &= 3^{-n}u[n] - \tfrac13\,3^{-(n-1)}u[n-1]\\
> &= 3^{-n}\big(u[n] - u[n-1]\big) = 3^{-n}\,\delta[n] = \delta[n].
> \end{aligned}
> $$
>
> **Step 2: apply the same combination to the outputs.** By linearity and shift invariance the input $x[n] - \tfrac13 x[n-1]$ produces $y[n] - \tfrac13 y[n-1]$. That input is $\delta[n]$, so that output is $h[n]$:
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
> First samples: $h[0] = 0$, $h[1] = \tfrac15$, $h[2] = -\tfrac{2}{75}$, $h[3] = -\tfrac{2}{375}$. Convolving this $h$ with $x$ reproduces $y$ exactly.
>
> **Cross-check in the z-domain** (fair game on the midterm, [[2-z-transform/09-transfer-functions|Lecture 9]]): with $X(z) = \dfrac{1}{1 - \frac13 z^{-1}}$ and $Y(z) = \dfrac{\frac15 z^{-1}}{1 - \frac15 z^{-1}}$,
>
> $$
> H(z) = \frac{Y(z)}{X(z)} = \frac{\tfrac15 z^{-1}\big(1 - \tfrac13 z^{-1}\big)}{1 - \tfrac15 z^{-1}},\qquad \text{ROC: } \lvert z\rvert > \tfrac15,
> $$
>
> whose inverse is $(\tfrac15)^n u[n-1] - \tfrac13(\tfrac15)^{n-1}u[n-2]$, the same $h$.
>
> *Rubric (22 pts):* 16 for a minor math mistake with correct LTI reasoning; 8 for relating $\delta[n]$ and $u[n]$ correctly but failing to apply superposition.

> [!recipe] Finding h from one input–output pair
> 1. Find constants with $\sum_k c_k\,x[n-k] = \delta[n]$. For $x = a^n u[n]$: $x[n] - a\,x[n-1] = \delta[n]$. For finite sequences, solve for the $c_k$ as in [[0-midterm-1/past-exams/spring-2023|SP2023 #4]].
> 2. Then $h[n] = \sum_k c_k\,y[n-k]$.
> 3. Or in the z-domain: $H(z) = Y(z)/X(z)$, with the ROC fixed by what you are told (causal, stable, …).

> [!trap] Shift everything, including the step
> $y[n-1] = (\tfrac15)^{n-1}u[n-2]$: replace $n$ by $n-1$ inside the step too. Keeping $u[n-1]$ adds a spurious term at $n = 1$ and gives $h[1] = \tfrac15 - \tfrac13 = -\tfrac{2}{15}$ instead of $\tfrac15$.

The same computation in Python, with the z-domain answer as a cross-check:

```python
import numpy as np
from scipy.signal import lfilter
n = np.arange(8)
x = 3.0 ** -n                             # x[n] = 3^-n u[n]
y = np.where(n >= 1, 5.0 ** -n, 0)        # y[n] = 5^-n u[n-1]
h = y - np.r_[0, y[:-1]] / 3              # h[n] = y[n] - (1/3) y[n-1]
print(h[:4])                              # h[0..3]
print(np.allclose(lfilter(h, 1, x), y))   # h * x reproduces y
print(np.allclose(lfilter([0, 1/5, -1/15], [1, -1/5], n == 0), h))  # H = Y/X
```

```text
[ 0.          0.2        -0.02666667 -0.00533333]
True
True
```

**On the exam:** [[problems/finding-h-from-input-output-pairs|finding h from input–output pairs]] is on 7/7 past midterms. [[0-midterm-1/past-exams/spring-2023|SP2023 #4]] uses two pairs: $x_1[n] - 3x_2[n-1] = \delta[n]$, so $h = y_1[n] - 3y_2[n-1]$ — exactly this problem's two steps. [[0-midterm-1/past-exams/fall-2024|FA2024 #3]] peels a known $h_2$ off a cascade to get $h_1 = 2\delta[n+1]$, and FA2024 #6 gives $y = \{\underset{\uparrow}{1}, \tfrac12\}$ from $x = \{\underset{\uparrow}{1}, \tfrac13\}$, so $H = Y/X$. More: [[0-midterm-1/past-exams/spring-2025|SP2025 #3]], [[0-midterm-1/past-exams/fall-2019|FA2019 #3]].

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
> Bookkeeping first: $x$ starts at $n = -1$ and $h$ at $n = 0$, so $y$ starts at $-1 + 0 = -1$ and has length $3 + 5 - 1 = 7$. Since $x[n] = -\delta[n+1] + \delta[n-1]$, the output is two shifted copies of $h$: $y[n] = -h[n+1] + h[n-1]$.
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
> The official solution builds the same column with the convolution matrix (columns = shifted copies of $h$, times the vector $x$). Sum check: $\sum y = \big(\sum x\big)\big(\sum h\big) = 0 \cdot 15 = 0$, and indeed $-1 - 2 - 2 - 2 - 2 + 4 + 5 = 0$.

> [!success]- (b) Solution
> Read the arrow: $h[0] = 0$, so $h[n] = \delta[n-1] + 2\delta[n-2]$ and the output is two *delayed* copies of $x$:
>
> $$
> \begin{aligned}
> x[n] * h[n] &= 3^{-(n-1)}u[n-1] + 2\cdot 3^{-(n-2)}u[n-2]\\
> &= 3^{-(n-1)}\big(u[n-1] + 6\,u[n-2]\big)\\
> &= \delta[n-1] + 7\Big(\tfrac13\Big)^{n-1}u[n-2].
> \end{aligned}
> $$
>
> Values: $y[0] = 0$, $y[1] = 1$, $y[2] = \tfrac73$, $y[3] = \tfrac79$, … The middle form is the official answer; the last one shows the shape.

> [!success]- (c) Solution
> $h[n] = n(u[n] - u[n-4])$ keeps $n = 0, 1, 2, 3$ and multiplies by $n$, so $h = \{\underset{\uparrow}{0}, 1, 2, 3\} = \delta[n-1] + 2\delta[n-2] + 3\delta[n-3]$ (the $n = 0$ sample is $0 \cdot 1 = 0$). Each $\delta[n-k]$ delays the step:
>
> $$
> x[n] * h[n] = u[n-1] + 2u[n-2] + 3u[n-3] = \{\underset{\uparrow}{0},\ 1,\ 3,\ 6,\ 6,\ 6,\ \dots\}.
> $$
>
> The output is the running sum of $h$: this is the step response of problem 3.

> [!success]- (d) Solution
> For integer $k$, $(-1)^{-k} = (-1)^k$. Both signals are causal, so $y[n] = 0$ for $n < 0$, and for $n \ge 0$ the sum runs over $0 \le k \le n$ (a finite geometric sum with ratio $-e$):
>
> $$
> y[n] = \sum_{k=0}^{n} (-1)^k e^{-(n-k)} = e^{-n}\sum_{k=0}^{n}(-e)^k = e^{-n}\,\frac{1 - (-e)^{n+1}}{1+e}.
> $$
>
> $$
> \boxed{\,x[n] * h[n] = \frac{e^{-n} + e\,(-1)^n}{1+e}\,u[n]\,}
> $$
>
> The key writes the numerator as $e^{-n} - (-1)^{n+1}e$, the same thing. Check values straight from the sum: $y[0] = 1$, $y[1] = e^{-1} - 1$, $y[2] = 1 - e^{-1} + e^{-2}$.

> [!success]- (e) Solution
> Note $2^{-(n-k)} = 0.5^{\,n-k}$, and $h[n-k] \ne 0$ requires $n - k \le 0$, i.e. $k \ge n$. Every surviving term is the same number:
>
> $$
> x[k]\,h[n-k] = 0.5^{k}\cdot 0.5^{\,n-k} = 0.5^{n}\qquad\text{for every } k \ge \max(0, n).
> $$
>
> Infinitely many equal, nonzero terms, so $y[n] = \sum_{k \ge \max(0,n)} 0.5^n = \infty$ for every $n$: **the convolution does not exist (it diverges).**
>
> Why: $h[n] = 2^{\lvert n\rvert}$ for $n \le 0$ grows toward $n \to -\infty$ exactly as fast as $x$ decays toward $+\infty$. In z-domain terms, $X(z)$ needs $\lvert z\rvert > \tfrac12$ while $H(z) = \sum_{m \ge 0}(2z)^m = \dfrac{1}{1 - 2z}$ needs $\lvert z\rvert < \tfrac12$: there is no common ROC.

*Rubric (20 pts):* 4 points per part, minus 1 for each minor math mistake.

> [!trap] Summing a series whose terms don't shrink
> Before using $\sum_{k\ge0} r^k = \frac{1}{1-r}$, check that $\lvert r\rvert < 1$. In (e) the ratio is exactly 1 (every term equals $0.5^n$), so any closed form is wrong: the answer is "diverges". In (d) the sum is finite ($0 \le k \le n$), so the ratio $-e$ is harmless.

The index bookkeeping of (a) in Python: `np.convolve` only sees the values, so carry the start index by hand (start indices add).

```python
import numpy as np
x, nx = np.array([-1, 0, 1]), -1          # x starts at n = -1
h, nh = np.array([1, 2, 3, 4, 5]), 0      # h starts at n = 0
y, ny = np.convolve(x, h), nx + nh        # start indices add
print("y starts at n =", ny, ":", y)
print("sum check:", y.sum(), "=", x.sum(), "*", h.sum())
```

```text
y starts at n = -1 : [-1 -2 -2 -2 -2  4  5]
sum check: 0 = 0 * 15
```

**On the exam:** a finite convolution is on every past midterm ([[problems/finite-length-convolution|finite-length convolution]], 7/7, e.g. [[0-midterm-1/past-exams/fall-2025|FA2025 #3a]], [[0-midterm-1/past-exams/spring-2021|SP2021 #2]]) and an infinite or mixed one on 5 of 7 ([[problems/infinite-length-convolution|infinite-length convolution]], e.g. [[0-midterm-1/past-exams/fall-2025|FA2025 #3b]], [[0-midterm-1/past-exams/spring-2025|SP2025 #4b]]). Always run the sum check: the official key of [[0-midterm-1/past-exams/spring-2025|SP2025 #4(a)]] boxed an answer whose samples add to 7 instead of $(\sum x)(\sum h) = 8$ (see [[0-toolkit/05-errata|errata]]).

## What the rubric teaches

- **Proof problems** (#1–#3) are graded on the justification: in #1 each verdict earns its 3 points only "with proper justification"; #2 is 10 + 10 for the two proofs. Here a bare verdict is not enough — unlike the midterm's property table, where only the Y/N boxes are graded.
- **#4** rewards the LTI reasoning: a minor algebra slip still earns 16 of 22, while relating $\delta[n]$ and $u[n]$ without applying superposition correctly earns 8.
- **#5** is 4 points per convolution, minus 1 per minor slip: a wrong start index or a dropped sample costs a point each, so do the bookkeeping (start index, length, sum check) before the arithmetic.

## Related

- [[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]] · [[concepts/step-response|step response]] · [[concepts/convolution|convolution]] · [[concepts/lccde|LCCDE]] · [[concepts/linearity|linearity]] · [[concepts/time-invariance|time invariance]] · [[concepts/bibo-stability|BIBO stability]]
- [[demos/convolution-explorer|Convolution explorer]] · [[0-toolkit/02-geometric-series|geometric series]] · prev set: [[homework/hw1|HW1]] · next set: [[homework/hw3|HW3]]

### Sources for this page

- ECE 310 Fall 2026 Homework 2 (due Sep 11) and the official solutions v1.0 (prepared by Nick & Mia), including the grading rubrics; the PDF pages were rendered to confirm the $n = 0$ arrows.
- Lecture notes 3–5 (Snyder); the initial-rest convention is stated in Lecture 5 §1.
- Past Midterm 1 exams cited above: FA2025 #2, #3a, #3b; SP2025 1(b), #2, #3, #4; FA2024 1(a), 1(e), #3, #6; FA2023 1(d), #2, #4; SP2023 #4; SP2021 #2, #3; FA2019 1(j), #3.
- Verification: every sample, closed form and counterexample on this page was recomputed in Python (numpy/scipy; 47 checks: direct convolution sums against the closed forms, `lfilter` for the recursions and the z-domain cross-check, divergence of the partial sums in 5(e)); the property rows use the randomized tests of the system-property bank.
