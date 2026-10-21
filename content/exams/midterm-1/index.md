---
title: "Midterm 1 review guide"
description: "ECE 310 Midterm 1 (Wed Sep 30, 2026; Lectures 1–11, HW1–HW4): scope, format, problem types on seven past exams, top traps, and the review lecture's six problems with folded solutions."
tags: [midterm-1, exam]
---

*Midterm 1 · held Wed Sep 30, 2026, 7–9 pm · Lectures 1–11 · HW1–HW4 · review lecture Mon Sep 28 · [[exams/index|Exams]]*

> [!abstract] In one breath
> - 2 hours, ~8 problems, 100 points, one handwritten two-sided sheet, no calculator, closed-form answers.
> - Fixed skeleton: T/F → property table → convolution → z-transform with ROC → LCCDE/$H(z)$ → PFE with ROC → stability/unbounded outputs.
> - Now a review of Units 1–2: scope = checklist, traps = summary, review problems = self-test.

## 1. Scope

| unit | lectures | skills |
|---|---|---|
| [[1-signals-and-systems/index\|Unit 1]] | [[1-signals-and-systems/01-digital-signals\|L1]] · [[1-signals-and-systems/02-complex-numbers-and-elementary-signals\|L2]] · [[1-signals-and-systems/03-system-properties\|L3]] · [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] · [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5]] | shift/flip; complex arithmetic; L/TI/C/S; convolution; LCCDE ⇄ block diagram |
| [[2-z-transform/index\|Unit 2]] | [[2-z-transform/06-the-z-transform\|L6]] · [[2-z-transform/07-z-transform-properties\|L7]] · [[2-z-transform/08-inverse-z-transform\|L8]] · [[2-z-transform/09-transfer-functions\|L9]] · [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]] · [[2-z-transform/11-bibo-stability-and-causality\|L11]] | z-transform with ROC; properties; PFE (long division if improper); $H(z)$ ⇄ LCCDE ⇄ $h[n]$; causality, stability from ROC; unbounded outputs |

Homework: [[homework/hw1|HW1]] · [[homework/hw2|HW2]] · [[homework/hw3|HW3]] · [[homework/hw4|HW4]]. Not tested: the DTFT (L13–14) and [[3-fourier-analysis/12-convolution-as-template-matching|L12]]. Old DTFT items (SP2023 #1(d)–(e), #8, #9; FA2019 #8, #9) belong to [[3-fourier-analysis/index|Unit 3]].

## 2. Format

| | Midterm 1 |
|---|---|
| time | 2 hours |
| size | ~8 problems, 100 points (FA2025: 12 + 12 + 10 + 10 + 15 + 16 + 15 + 10) |
| allowed | one handwritten two-sided 8.5″ × 11″ sheet; no calculator |
| answers | closed form, no $\sum$ or $\int$; show all work |
| T/F | SP2023, SP2025: +2 / −1 / 0; FA2023–FA2025: no penalty. Guess if $p>\tfrac13$ ($2p-(1-p)>0$) |

Typical points (recent Falls): T/F 12 · property table 12 · convolution 8–10 · short LTI 5–10 · z-transforms 9–15 · LCCDE/$H(z)$ 15–20 · PFE/ROC/stability 15–20 · pole matching or parameter 10.

## 3. Problem types × past exams

| family | FA25 | SP25 | FA24 | FA23 | SP23 | SP21 | FA19 | count |
|---|---|---|---|---|---|---|---|---|
| T/F → [[exams/midterm-1/true-false-bank\|bank]] | #1 | #1 | #1 | #1 | #1 | #1 | #1 | 7/7 |
| [[problems/classifying-system-properties\|Property table]] → [[exams/midterm-1/system-property-bank\|bank]] | #2 | #2 | #2 | #2 | #2 | #3 | #2 | 7/7 |
| [[problems/finite-length-convolution\|Finite convolution]] | #3a | #4a | #4a | #3a | #3a | #2 | #4 | 7/7 |
| [[problems/infinite-length-convolution\|Infinite convolution]] | #3b | #4b | #4b | #3b | #3b,#3c | — | — | 5/7 |
| [[problems/finding-h-from-input-output-pairs\|Finding h]] | #4 | #3 | #3,#6 | #4 | #4,#6 | #7 | #3 | 7/7 |
| [[problems/z-transform-with-roc\|z-transform with ROC]] | #5 | #5 | #5 | #5 | — | #4 | #5 | 6/7 |
| [[problems/all-possible-rocs\|Inverse z / all ROCs]] | #7 | #8 | #7 | #6 | #6 | #5,#7 | #6,#7 | 7/7 |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z)]] | #6 | #8 | #6 | #6,#7 | #5,#6 | #6 | #10 | 7/7 |
| [[problems/unbounded-outputs-and-pole-matching\|Pole matching]] | #8 | #6 | #7 | #7 | #7 | #5 | #10 | 7/7 |
| [[problems/parameters-for-stability\|Parameters for stability]] | — | #7 | #8 | #8 | — | — | — | 3/7 |
| [[problems/two-sided-systems-as-recursions\|Two-sided recursions]] | #7b | — | #8a | — | — | — | — | 2/7 |

Per-exam detail: [[exams/midterm-1/past-exams/index|past exams]].

## 4. Last-day plan

> [!tip] Order
> Write the sheet (60 min) → [[exams/midterm-1/past-exams/fall-2025|FA2025]] timed (120) → grade, repair by [[problems/index|family]] (45) → break → [[exams/midterm-1/past-exams/spring-2025|SP2025]] timed → repair → [[demos/practice-drills|drills]] and both banks → last hour: re-read §5 and your sheet only.
> Four hours: sheet → FA2025 #1, #2, #3, #6, #7, #8 → repair → T/F bank and §5.

## 5. Top traps

1. $e^{j2/3}\neq e^{j2\pi/3}$ (FA25 #8b): no match → bounded. → [[problems/unbounded-outputs-and-pole-matching|pole matching]]
2. Missing ROC = half credit (HW3 rubric: 3 of 6). → [[problems/z-transform-with-roc|z-transform with ROC]]
3. $-a^nu[-n-1] \leftrightarrow \dfrac{1}{1-az^{-1}}$, $\lvert z\rvert<\lvert a\rvert$: minus sign and $-n-1$. → [[concepts/z-transform-pairs|pairs]]
4. $a^nu[n-k] \leftrightarrow \dfrac{a^kz^{-k}}{1-az^{-1}}$: keep $a^k$. → [[concepts/z-transform-properties|properties]]
5. Improper $H(z)$: long division before PFE. → [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]]
6. Cancel common factors before reading the ROC (FA25 #6, SP25 #8, SP21 #7). → [[concepts/pole-zero-cancellation|cancellation]]
7. Bounded $h$ ⇏ stable: $h = u[n]$ (FA25 #1a, FA19 #1c). → [[concepts/bibo-stability|BIBO stability]]
8. Causal ⇔ ROC outside outermost pole and no pole at $\infty$; causal and stable ⇔ all poles inside. → [[2-z-transform/11-bibo-stability-and-causality|L11]]
9. Causality of $x[f(n)]$: test negative $n$ ($x[\lvert n\rvert]$). → [[problems/classifying-system-properties|properties]]
10. Additive constant ⇒ nonlinear ($T\{0\}\neq0$). → [[concepts/linearity|linearity]]
11. $n$ outside the brackets ⇒ time-varying; any $x*h$ is TI. → [[concepts/time-invariance|time invariance]]
12. Convolution start = sum of starts; length $L_x+L_h-1$; mark $n=0$. → [[problems/finite-length-convolution|finite convolution]]
13. L5 vs L9 LCCDE: feedback signs flip. → [[2-z-transform/09-transfer-functions|L9]]
14. Conjugate poles: $2\lvert A\rvert\,r^n\cos(\omega_0n+\angle A)\,u[n]$ (SP21 #5). → [[concepts/partial-fraction-expansion|PFE]]
15. Finite sequences: $z^{-k}$ excludes $0$, $z^{+k}$ excludes $\infty$ (FA24 #5b, FA25 #5a). → [[concepts/region-of-convergence|ROC]]

Key mistakes: [[0-toolkit/05-errata|errata]].

## 6. Review lecture problems (Sep 28)

One past problem per exam section, in exam order. Emphasis: pole-zero cancellation, $h=u[n]$ as counterexample, rewrite into table pairs plus shifts, start every inverse from the ROC.

### 6.1 True/False — FA2019 #1

> [!question] FA2019 #1 — True or False?
> (a) An LSI system specified by $y[n]-\tfrac12y[n-1] = x[n]$ can be causal or anti-causal.
> (b) The input–output relationship of an arbitrary system is completely determined by the system's unit pulse response.
> (c) If an LSI system is BIBO unstable, its unit pulse response $h[n]$ must be unbounded.
> (d) Let $h[n] = h_1[n]*h_2[n]$ be the unit pulse response of two serial subsystems. If $h_1$ or $h_2$ is BIBO unstable, $h$ must be BIBO unstable.
> (e) An LSI system with a finite-length impulse response can be BIBO stable or unstable.
> (f) A time-varying system cannot be causal.
> (g) Let $\sum_{n=-\infty}^{\infty}x[n]\,\delta[2^nu[n]-8] = 4$. Then $x[3] = 2$.
> (h) Suppose that the step response $g[n]$ of an LSI system (its output for $x[n] = u[n]$) has a z-transform with a pole at $z = \tfrac12$. Then $H(z)$ also has a pole at $z = \tfrac12$.
> (i) If the response $y[n]$ of an LSI system to the input $x[n] = 3^nu[n]$ is unbounded, the system must be BIBO unstable.
> (j) The response $y[n]$ of a BIBO unstable LSI system to any non-zero input $x[n]$ is always unbounded.

> [!success]- Answers: T, F, F, F, F, F, F, T, F, F
> - (a) T: ROC $\lvert z\rvert>\tfrac12$ gives $(\tfrac12)^nu[n]$; $\lvert z\rvert<\tfrac12$ gives $-(\tfrac12)^nu[-n-1]$.
> - (b) F: only LTI systems.
> - (c) F: $h[n] = u[n]$.
> - (d) F: $\dfrac{1}{1-2z^{-1}}\cdot(1-2z^{-1}) = 1$.
> - (e) F: FIR is always stable.
> - (f) F: $y[n] = n\,x[n]$.
> - (g) F: impulse only at $n = 3$, so $x[3] = 4$.
> - (h) T: $G(z) = H(z)\,\dfrac{1}{1-z^{-1}}$; the step adds only $z = 1$.
> - (i) F: the input is unbounded; $y[n] = x[n]$ passes it.
> - (j) F: an input zero can cancel the unstable pole.
>
> More: [[exams/midterm-1/true-false-bank|T/F bank]].

### 6.2 Property table — SP2023 #2

> [!question] SP2023 #2 — Linear? Shift-invariant? Causal? Stable?
> (1) $y[n] = x[n]*(-1)^nu[n]$ (2) $y[n] = \dfrac{x[n]}{x[2]}$ (3) $y[n] = \cos^2(\tfrac{\pi}{2}n)\,x[n]$

> [!success]- Answers
> | system | linear | shift-invariant | causal | stable |
> |---|---|---|---|---|
> | $x[n]*(-1)^nu[n]$ | Yes | Yes | Yes | No |
> | $x[n]/x[2]$ | No | No | No | No |
> | $\cos^2(\tfrac{\pi}{2}n)\,x[n]$ | Yes | No | Yes | Yes |
>
> (1) Convolution ⇒ LTI; $h=0$ for $n<0$; $\sum\lvert h\rvert = \infty$. (2) Scaling $x$ leaves $y$ unchanged; fixed $x[2]$ ⇒ shift-varying, non-causal; $\delta[n]$ divides by zero. (3) $n$-dependent gain; memoryless; $\lvert\cos^2\rvert\le1$. More: [[exams/midterm-1/system-property-bank|property bank]].

### 6.3 Convolution — FA2023 #3

> [!question] FA2023 #3 — compute $y[n] = x[n]*h[n]$
> (a) $x[n] = \{\underset{\uparrow}{1},\ 2,\ 3,\ 2,\ 1\}$, $h[n] = \{\underset{\uparrow}{-1},\ 1\}$
> (b) $x[n] = (\tfrac34)^nu[n]$, $h[n] = 2u[n]-u[n-1]-u[n-2]$

> [!success]- Solution
> (a) Start $n = 0$, length $5+2-1 = 6$ ($y = Hx$, $6\times5$ matrix):
> $$
> y[n] = \{\underset{\uparrow}{-1},\ -1,\ -1,\ 1,\ 1,\ 1\}\qquad(n = 0,\dots,5)
> $$
> Check: $\sum y = 0 = (\sum x)(\sum h) = 9\cdot0$.
>
> (b) $h[n] = \{\underset{\uparrow}{2},\ 1\} = 2\delta[n]+\delta[n-1]$, so
> $$
> y[n] = 2x[n]+x[n-1] = 2\left(\tfrac34\right)^nu[n]+\left(\tfrac34\right)^{n-1}u[n-1].
> $$
> → [[problems/finite-length-convolution|finite]], [[problems/infinite-length-convolution|infinite convolution]]

### 6.4 z-transforms with ROC — FA2024 #5

> [!question] FA2024 #5 — z-transform with ROC
> (a) $x[n] = (n+1)\,u[n-1]$ (b) $x[n] = u[n-1]\,u[3-n]$ (c) $x[n] = 3^{-n}u[n]+3^nu[-n]$

> [!success]- Solution
> (a) $(n+1)u[n-1] = (n-1)u[n-1]+2u[n-1]$; $n\,u[n] \leftrightarrow -z\,\dfrac{d}{dz}\dfrac{1}{1-z^{-1}} = \dfrac{z^{-1}}{(1-z^{-1})^2}$:
> $$
> X(z) = \frac{z^{-2}}{(1-z^{-1})^2}+\frac{2z^{-1}}{1-z^{-1}},\qquad \text{ROC: } \lvert z\rvert>1.
> $$
> (b) $\delta[n-1]+\delta[n-2]+\delta[n-3]$: $X(z) = z^{-1}+z^{-2}+z^{-3}$, ROC: $z\neq0$.
>
> (c) $(\tfrac13)^nu[n] \leftrightarrow \dfrac{1}{1-\frac13z^{-1}}$, $\lvert z\rvert>\tfrac13$; $3^nu[-n] = 3\cdot3^{n-1}u[-(n-1)-1]$, with $3^nu[-n-1] \leftrightarrow \dfrac{-1}{1-3z^{-1}}$ ($\lvert z\rvert<3$):
> $$
> X(z) = \frac{1}{1-\frac13z^{-1}}-\frac{3z^{-1}}{1-3z^{-1}},\qquad \text{ROC: } \tfrac13<\lvert z\rvert<3.
> $$
> → [[problems/z-transform-with-roc|z-transform with ROC]]

### 6.5 Response through H(z) — SP2023 #6

> [!question] SP2023 #6 — a causal and stable LTI system maps $x$ to $y$ with
> $$
> X(z) = \frac{1}{(1-2z^{-1})(1-z^{-1})},\qquad Y(z) = \frac{1}{(1-\frac12z^{-1})(1-z^{-1})(1-\frac14z^{-1})}.
> $$
> (a) Find $H(z)$ and its ROC. (b) Find $h[n]$. (c) Find the difference equation.

> [!success]- Solution
> (a) $H = Y/X$:
> $$
> H(z) = \frac{1-2z^{-1}}{(1-\frac12z^{-1})(1-\frac14z^{-1})},\qquad \text{ROC: } \lvert z\rvert>\tfrac12
> $$
> (b) $A_1 = \dfrac{1-2\cdot2}{1-\frac14\cdot2} = -6$, $A_2 = \dfrac{1-2\cdot4}{1-\frac12\cdot4} = 7$:
> $$
> h[n] = -6\left(\tfrac12\right)^nu[n]+7\left(\tfrac14\right)^nu[n].
> $$
> Check: $h[0] = 1 = \lim_{z\to\infty}H(z)$.
>
> (c)
> $$
> y[n] = \tfrac34\,y[n-1]-\tfrac18\,y[n-2]+x[n]-2x[n-1].
> $$
> (Official key misprints this: [[0-toolkit/05-errata|errata]].) → [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z)]]

### 6.6 Unbounded outputs — SP2023 #7

> [!question] SP2023 #7 — a causal LTI system has $H(z) = \dfrac{z-3}{z-4}$, ROC: $\lvert z\rvert>4$.
> (a) Find a bounded input that produces an unbounded output. (b) Find an unbounded input that produces a bounded output. (c) Find a bounded input that produces a bounded output.

> [!success]- Solution
> $H(z) = \dfrac{1-3z^{-1}}{1-4z^{-1}}$: pole $4$ (unstable), zero $3$.
>
> (a) $x = \delta[n]$: $y = h = 4^nu[n]-3\cdot4^{n-1}u[n-1]$.
>
> (b) $X(z) = \dfrac{1-4z^{-1}}{1-3z^{-1}}$, $x[n] = 3^nu[n]-4\cdot3^{n-1}u[n-1]$: $Y = 1$, $y = \delta[n]$.
>
> (c) $X(z) = 1-4z^{-1}$, $x = \delta[n]-4\delta[n-1]$: $y = \delta[n]-3\delta[n-1]$.
>
> → [[problems/unbounded-outputs-and-pole-matching|pole matching]]

> [!tip] In the exam room
> Skim all problems. Bank T/F and the table fast (24 points). ROC beside every transform; mark $n = 0$. Check convolutions by $\sum y = \sum x\cdot\sum h$, PFEs by $h[0] = \lim_{z\to\infty}H(z)$.

## Related
[[concepts/concept-map.canvas|concept map]] · [[exams/midterm-1/cheat-sheet|cheat sheet]] · [[demos/practice-drills|drills]] · [[exams/midterm-1/past-exams/index|past exams]] · [[problems/index|problem families]] · [[exams/index|all exams]]

### Sources for this page
Midterm 1 Review slides, annotated (Snyder, Sep 28, 2026); past Midterm 1 covers FA2019–FA2025; HW3 rubric; L1–L11 dates.
