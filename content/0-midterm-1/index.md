---
title: "Midterm 1 survival guide"
description: "Everything for ECE 310 Midterm 1 (Wed Sep 30, 2026, 7–9 pm): scope, format, how often each problem type has appeared, a plan for the remaining hours, the fifteen traps that cost the most points, and the review lecture's six problems with folded, verified solutions."
tags: [midterm-1, exam]
---

*Midterm 1 · Wednesday, September 30, 2026 · 7:00–9:00 pm · Lectures 1–11 · HW1–HW4 · review lecture Monday Sep 28*

> [!abstract] In one breath
> Two hours, about eight problems, 100 points, one handwritten two-sided sheet, no calculator, answers in closed form. Every past exam has the same skeleton: **True/False → the linear / time-invariant / causal / stable table → convolution → z-transforms with ROC → an LCCDE / transfer-function problem → PFE with the right ROC → a stability or unbounded-output problem.** The review lecture walked through exactly that sequence. Today: write your sheet, take FA2025 and SP2025 under exam conditions, repair every miss with the matching problem-family page, and stop learning new material an hour before the exam.

## 1. Scope

**On the exam: Lectures 1–11 and HW1–HW4.**

| unit | lectures | what you must be able to do |
|---|---|---|
| [[1-signals-and-systems/index\|Unit 1 · Signals and systems]] | [[1-signals-and-systems/01-digital-signals\|L1 digital signals]] (Aug 24) · [[1-signals-and-systems/02-complex-numbers-and-elementary-signals\|L2 complex numbers and elementary signals]] (Aug 26) · [[1-signals-and-systems/03-system-properties\|L3 system properties]] (Aug 28) · [[1-signals-and-systems/04-impulse-response-and-convolution\|L4 impulse response and convolution]] (Aug 31) · [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5 difference equations and block diagrams]] (Sep 2) | shift and flip signals; complex arithmetic and Euler; decide linear / time-invariant / causal / stable; convolve finite and infinite signals; LCCDE ⇄ block diagram |
| [[2-z-transform/index\|Unit 2 · The z-transform and LTI systems]] | [[2-z-transform/06-the-z-transform\|L6 z-transform]] (Sep 4) · [[2-z-transform/07-z-transform-properties\|L7 properties]] (Sep 9) · [[2-z-transform/08-inverse-z-transform\|L8 inverse z]] (Sep 11) · [[2-z-transform/09-transfer-functions\|L9 transfer functions]] (Sep 14) · [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10 improper H, system algebra]] (Sep 16) · [[2-z-transform/11-bibo-stability-and-causality\|L11 BIBO stability and causality]] (Sep 18) | z-transform with ROC; properties; inverse z by PFE (with long division when improper); $H(z)$ ⇄ LCCDE ⇄ $h[n]$; causality and stability from the ROC; which inputs give unbounded outputs |

Homework: [[homework/hw1|HW1]] · [[homework/hw2|HW2]] · [[homework/hw3|HW3]] · [[homework/hw4|HW4]].

**Not on the exam:** the DTFT (Lectures 13–14, HW5) and Lecture 12 (convolution as template matching — "will not be tested on homeworks or exams"); see [[3-beyond-midterm-1/index|Beyond Midterm 1]]. Old exams contain DTFT problems — skip them: SP2023 #1(d)–(e), #8, #9 and FA2019 #8, #9.

## 2. Format

| | Midterm 1 |
|---|---|
| when | Wednesday Sep 30, 2026, 7:00–9:00 pm — **2 hours** |
| size | about **8 problems, 100 points** (FA2025: 12 + 12 + 10 + 10 + 15 + 16 + 15 + 10) |
| allowed | **one handwritten two-sided 8.5″ × 11″ sheet** — no books, **no calculators**, no other notes |
| answers | "calculate", "determine", "find" mean **closed form** — no $\sum$ or $\int$ left in the answer |
| grading | "Show all your work to receive full credit"; "Neatness counts" |
| True/False scoring | **read the instructions on the day**: SP2023 and SP2025 scored T/F as +2 right / −1 wrong / 0 blank (FA2019 did the same on its property questions); FA2023–FA2025 printed no penalty. With a penalty, leave a pure coin-flip blank; without one, answer everything |

These are the instructions printed on the cover of every past Midterm 1 since FA2019 (FA2025 quoted; SP2021 was online). The review slides (Sep 28) contain no format slide — they are six worked problems (§6). Typical point split on recent Fall exams: T/F 12 · property table 12 · convolution 8–10 · short LTI problem 5–10 · z-transforms 9–15 · LCCDE / transfer function 15–20 · PFE / ROC / stability 15–20 · pole matching or parameter problem 10.

## 3. What gets asked — problem types × past exams

Each row is an exam recipe. Seven of the eleven families appeared on **all seven** past exams.

| problem family | FA25 | SP25 | FA24 | FA23 | SP23 | SP21 | FA19 | count |
|---|---|---|---|---|---|---|---|---|
| True/False → [[0-midterm-1/true-false-bank\|T/F bank]] | #1 | #1 | #1 | #1 | #1 | #1 | #1 | 7/7 |
| [[problems/classifying-system-properties\|System-property table]] → [[0-midterm-1/system-property-bank\|property bank]] | #2 | #2 | #2 | #2 | #2 | #3 | #2 | 7/7 |
| [[problems/finite-length-convolution\|Finite-length convolution]] | #3a | #4a | #4a | #3a | #3a | #2 | #4 | 7/7 |
| [[problems/infinite-length-convolution\|Infinite / mixed convolution]] | #3b | #4b | #4b | #3b | #3b,#3c | — | — | 5/7 |
| [[problems/finding-h-from-input-output-pairs\|Finding h (or H) from input–output data]] | #4 | #3 | #3,#6 | #4 | #4,#6 | #7 | #3 | 7/7 |
| [[problems/z-transform-with-roc\|z-transform with ROC]] | #5 | #5 | #5 | #5 | — | #4 | #5 | 6/7 |
| [[problems/all-possible-rocs\|Inverse z / PFE / all possible ROCs]] | #7 | #8 | #7 | #6 | #6 | #5,#7 | #6,#7 | 7/7 |
| [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z) ↔ response]] | #6 | #8 | #6 | #6,#7 | #5,#6 | #6 | #10 | 7/7 |
| [[problems/unbounded-outputs-and-pole-matching\|Unbounded outputs, pole matching, cancellation]] | #8 | #6 | #7 | #7 | #7 | #5 | #10 | 7/7 |
| [[problems/parameters-for-stability\|Parameters for stability]] | — | #7 | #8 | #8 | — | — | — | 3/7 |
| [[problems/two-sided-systems-as-recursions\|Two-sided systems as recursions]] | #7b | — | #8a | — | — | — | — | 2/7 |

Every problem of every past exam, mapped to its family and lectures: [[0-midterm-1/past-exams/index|past exams]] (each exam page has the problems with folded solutions).

> [!exam] Read the table as a to-do list
> The seven 7/7 families are worth well over half the points on every exam. If you can do those cold — with ROCs stated and $n = 0$ marked — you have passed. The three problem slots that change between exams (infinite convolution, parameters for stability, two-sided recursions) are variations on the same PFE-and-ROC skills.

## 4. Plan for the remaining hours

Adapt the blocks to the time you have; keep the order.

| block | time | what | where |
|---|---|---|---|
| 1 | 60 min | **Write your handwritten sheet.** The act of writing it is the first review. | [[0-midterm-1/cheat-sheet\|cheat sheet]] |
| 2 | 120 min | **FA2025 under exam conditions** — timer, your sheet only, no calculator. It is the most recent exam by the same instructor. | [[0-midterm-1/past-exams/fall-2025\|Fall 2025]] |
| 3 | 45 min | Grade it with the folded solutions. For every lost point: read the family page's recipe and trap, then redo the problem without looking. | [[problems/index\|problem families]] |
| — | 30 min | Break and a real meal. | |
| 4 | 120 min | **SP2025 under exam conditions.** | [[0-midterm-1/past-exams/spring-2025\|Spring 2025]] |
| 5 | 30 min | Grade and repair, as in block 3; add anything you had to look up to your sheet. | |
| 6 | 30–45 min | Randomized drills on your weakest skill, then the T/F and property banks. | [[0-midterm-1/practice-drills\|practice drills]] · [[0-midterm-1/true-false-bank\|T/F bank]] · [[0-midterm-1/system-property-bank\|property bank]] |
| 7 | last hour before 7 pm | **Light review only**: re-read §5 below and your sheet. No new problems. Eat, pack your sheet and pencils, arrive early. | |

> [!tip] Short on time (about 4 hours)?
> Sheet (45 min) → FA2025 problems #1, #2, #3, #6, #7, #8 timed (75 min) → repair the misses with the family pages (45 min) → T/F bank and the trap list (30 min) → light review. If you only have an hour: read the trap list, then the [[0-midterm-1/cheat-sheet|cheat sheet]] §6, §8 and §10.

## 5. The fifteen traps that cost the most points

1. **$e^{j2/3}$ is not $e^{j2\pi/3}$** — FA25 #8b's pole sits at angle $\tfrac23$ rad, so $\cos(\tfrac{2\pi}{3}n)u[n]$ does not match it: bounded output (key: False). → [[problems/unbounded-outputs-and-pole-matching|pole matching]]
2. **A transform without its ROC is half an answer** — HW3 rubric: 3 of 6 points for a correct $X(z)$ with a missing or wrong ROC. → [[problems/z-transform-with-roc|z-transform with ROC]]
3. **Left-sided pair sign:** $-a^nu[-n-1] \leftrightarrow \dfrac{1}{1-az^{-1}}$, ROC $\lvert z\rvert<\lvert a\rvert$ — the minus sign and the $-n-1$ both matter. → [[concepts/z-transform-pairs|z-transform pairs]]
4. **Shift factor:** $a^nu[n-k] = a^k\,a^{n-k}u[n-k] \leftrightarrow \dfrac{a^kz^{-k}}{1-az^{-1}}$ — don't drop the $a^k$. → [[concepts/z-transform-properties|z-transform properties]]
5. **Improper $H(z)$ needs long division** before PFE (numerator degree in $z^{-1}$ ≥ denominator degree), which adds $\delta$ terms. → [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]
6. **Pole-zero cancellation changes the ROC** — cancel common factors first, then read the ROC (FA25 #6, SP25 #8, SP21 #7). → [[concepts/pole-zero-cancellation|pole-zero cancellation]]
7. **"Bounded $h$ ⇒ stable" is false** — $h = u[n]$ is bounded but $\sum\lvert h\rvert = \infty$ (FA25 #1a, FA19 #1c). → [[concepts/bibo-stability|BIBO stability]]
8. **Causal ⇔ ROC outside the outermost pole *and* $H$ proper** (no pole at $z = \infty$); causal *and* stable ⇔ every pole inside the unit circle. → [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]
9. **Causality of $x[f(n)]$: test negative $n$** — $x[\lvert n\rvert]$ at $n = -3$ needs $x[3]$ (non-causal) even though it is fine for $n \ge 0$. → [[problems/classifying-system-properties|classifying system properties]]
10. **An additive constant makes a system nonlinear** — $x[n]+3$, $2x[\lvert n\rvert]+10$ ($T\{0\}\neq0$). → [[concepts/linearity|linearity]]
11. **$n$ outside the brackets makes it time-varying** — $n\,x[n]$, $\cos^2(\tfrac{\pi}{2}n)\,x[n]$ (a convolution $x*h$ is always time-invariant, whatever $h$ looks like). → [[concepts/time-invariance|time invariance]]
12. **Convolution start index = sum of the start indices**, length $L_x+L_h-1$ — and mark $n = 0$ in the answer. → [[problems/finite-length-convolution|finite-length convolution]]
13. **Lecture 5 vs Lecture 9 sign convention:** L5 writes $y[n] = \sum b_i\,y[n-i]+\dots$, L9 writes $y[n]+\sum a_k\,y[n-k] = \dots$ — the feedback coefficients flip sign between them. → [[2-z-transform/09-transfer-functions|Lecture 9]]
14. **Complex-conjugate poles → a cosine:** $\dfrac{A}{1-pz^{-1}}+\dfrac{A^*}{1-p^*z^{-1}} \leftrightarrow 2\lvert A\rvert\,r^n\cos(\omega_0n+\angle A)\,u[n]$ (SP21 #5: $3\sin(\tfrac{\pi}{2}n)u[n]$). → [[concepts/partial-fraction-expansion|PFE]]
15. **Finite sequences: the ROC excludes $0$ and/or $\infty$** — $z^{-k}$ terms exclude $z = 0$, $z^{+k}$ terms exclude $z = \infty$ (FA24 #5b: $z\neq0$; FA25 #5a: $1<\lvert z\rvert<\infty$). → [[concepts/region-of-convergence|ROC]]

Known mistakes in the official keys (so a mismatch with a key is not always your error): [[0-toolkit/05-errata|errata]].

## 6. What the instructor emphasised in the review lecture

The Midterm 1 Review (Monday Sep 28) worked **one past-exam problem per exam section, in exam order**: True/False (FA2019 #1) → the LTIC table (SP2023 #2) → convolution (FA2023 #3) → z-transforms with ROC (FA2024 #5) → LTI system response through $H(z)$ (SP2023 #6) → stability and unbounded outputs (SP2023 #7). The recurring messages in the handwritten annotations: **pole-zero cancellation** (three T/F answers hinge on it), **$h = u[n]$ as the counterexample** for "bounded but unstable", **rewrite a signal into table pairs plus shifts** before transforming, and **every inverse transform starts from the ROC**. Try each problem before opening its solution. All answers below were re-checked numerically.

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
> - (a) **True** — one LCCDE, two ROCs: $\lvert z\rvert>\tfrac12$ gives the causal $h = (\tfrac12)^nu[n]$, $\lvert z\rvert<\tfrac12$ the anti-causal $h = -(\tfrac12)^nu[-n-1]$.
> - (b) **False** — only an LTI (= LSI) system is determined by its impulse response.
> - (c) **False** — the annotation: consider $h[n] = u[n]$, bounded yet $\sum\lvert h\rvert = \infty$.
> - (d) **False** — the cascade "may have pole-zero cancellation": $\dfrac{1}{1-2z^{-1}}\cdot(1-2z^{-1}) = 1$, i.e. $h = \delta[n]$.
> - (e) **False** — a finite $\sum\lvert h\rvert$ is always finite: FIR systems are always stable.
> - (f) **False** — $y[n] = n\,x[n]$ is time-varying and causal.
> - (g) **False** — the impulse fires only where $2^nu[n] = 8$, i.e. at $n = 3$, so the sum is $x[3]$ and $x[3] = 4$.
> - (h) **True** — the annotation: $G(z) = H(z)\,\dfrac{1}{1-z^{-1}}$; the step contributes only a pole at $z = 1$, so a pole at $\tfrac12$ must be a pole of $H$.
> - (i) **False** — the input is itself unbounded; even the stable system $y[n] = x[n]$ passes it through.
> - (j) **False** — "we may have pole-zero cancellation": an input with a zero on the unstable pole gives a bounded output.
>
> More statements like these, from all seven exams: [[0-midterm-1/true-false-bank|T/F bank]].

### 6.2 The property table — SP2023 #2

> [!question] SP2023 #2 — Linear? Shift-invariant? Causal? Stable?
> (1) $y[n] = x[n]*(-1)^nu[n]$ (2) $y[n] = \dfrac{x[n]}{x[2]}$ (3) $y[n] = \cos^2(\tfrac{\pi}{2}n)\,x[n]$

> [!success]- Answers
> | system | linear | shift-invariant | causal | stable |
> |---|---|---|---|---|
> | $x[n]*(-1)^nu[n]$ | Yes | Yes | Yes | No |
> | $x[n]/x[2]$ | No | No | No | No |
> | $\cos^2(\tfrac{\pi}{2}n)\,x[n]$ | Yes | No | Yes | Yes |
>
> (1) A convolution is LTI; $h = (-1)^nu[n]$ vanishes for $n<0$ (causal) but $\sum\lvert h\rvert = \infty$ (unstable). (2) Doubling $x$ leaves $y$ unchanged, so it is not linear; the fixed sample $x[2]$ makes it shift-varying, and non-causal (at $n = 0$ it needs $x[2]$); a bounded input with $x[2] = 0$, such as $\delta[n]$, divides by zero — not stable. (3) The coefficient depends on $n$: linear but shift-varying; memoryless, so causal; $\lvert\cos^2\rvert\le1$, so stable. Every system from the past tables and the lectures: [[0-midterm-1/system-property-bank|property bank]].

### 6.3 Convolution — FA2023 #3

> [!question] FA2023 #3 — compute $y[n] = x[n]*h[n]$
> (a) $x[n] = \{\underset{\uparrow}{1},\ 2,\ 3,\ 2,\ 1\}$, $h[n] = \{\underset{\uparrow}{-1},\ 1\}$
> (b) $x[n] = (\tfrac34)^nu[n]$, $h[n] = 2u[n]-u[n-1]-u[n-2]$

> [!success]- Solution
> (a) Both start at $n = 0$, so $y$ starts at $n = 0$ and has length $5+2-1 = 6$. The instructor wrote it as $y = Hx$ with a $6\times5$ matrix whose columns are shifted copies of $h$:
> $$
> y[n] = \{\underset{\uparrow}{-1},\ -1,\ -1,\ 1,\ 1,\ 1\}\qquad(n = 0,\dots,5)
> $$
> Check: $\sum y = 0 = (\sum x)(\sum h) = 9\cdot0$ ✓.
>
> (b) First simplify $h$: at $n = 0$ it is $2$, at $n = 1$ it is $2-1 = 1$, for $n\ge2$ it is $2-1-1 = 0$. So $h[n] = \{\underset{\uparrow}{2},\ 1\} = 2\delta[n]+\delta[n-1]$ and
> $$
> y[n] = 2x[n]+x[n-1] = 2\left(\tfrac34\right)^nu[n]+\left(\tfrac34\right)^{n-1}u[n-1].
> $$
> Lesson: **simplify a sum of steps into impulses before convolving.** → [[problems/finite-length-convolution|finite-length]], [[problems/infinite-length-convolution|infinite-length convolution]]

### 6.4 z-transforms with ROC — FA2024 #5

> [!question] FA2024 #5 — z-transform with ROC
> (a) $x[n] = (n+1)\,u[n-1]$ (b) $x[n] = u[n-1]\,u[3-n]$ (c) $x[n] = 3^{-n}u[n]+3^nu[-n]$

> [!success]- Solution
> (a) Rewrite so that the factor multiplying the step matches its shift: $(n+1)u[n-1] = (n-1)u[n-1]+2u[n-1]$. The first term is $g[n-1]$ with $g[n] = n\,u[n]$, and $G(z) = -z\,\dfrac{d}{dz}\dfrac{1}{1-z^{-1}} = \dfrac{z^{-1}}{(1-z^{-1})^2}$. Hence
> $$
> X(z) = \frac{z^{-2}}{(1-z^{-1})^2}+\frac{2z^{-1}}{1-z^{-1}},\qquad \text{ROC: } \lvert z\rvert>1.
> $$
> (b) $x[n] = \{\underset{\uparrow}{0},\ 1,\ 1,\ 1\} = \delta[n-1]+\delta[n-2]+\delta[n-3]$, so $X(z) = z^{-1}+z^{-2}+z^{-3}$, ROC: $z\neq0$.
>
> (c) The first term is right-sided, $(\tfrac13)^nu[n] \leftrightarrow \dfrac{1}{1-\frac13z^{-1}}$, $\lvert z\rvert>\tfrac13$. The second is left-sided: $3^nu[-n] = 3\cdot3^{n-1}u[-(n-1)-1]$, a shifted copy of $3^nu[-n-1] \leftrightarrow \dfrac{-1}{1-3z^{-1}}$ ($\lvert z\rvert<3$). So
> $$
> X(z) = \frac{1}{1-\frac13z^{-1}}-\frac{3z^{-1}}{1-3z^{-1}},\qquad \text{ROC: } \tfrac13<\lvert z\rvert<3.
> $$
> (Equivalently the second term is $\dfrac{1}{1-z/3}$.) → [[problems/z-transform-with-roc|z-transform with ROC]]

### 6.5 System response through H(z) — SP2023 #6

> [!question] SP2023 #6 — a causal and stable LTI system maps $x$ to $y$ with
> $$
> X(z) = \frac{1}{(1-2z^{-1})(1-z^{-1})},\qquad Y(z) = \frac{1}{(1-\frac12z^{-1})(1-z^{-1})(1-\frac14z^{-1})}.
> $$
> (a) Find $H(z)$ and its ROC. (b) Find $h[n]$. (c) Find the difference equation.

> [!success]- Solution
> (a) $H = Y/X$; the $(1-z^{-1})$ factors cancel:
> $$
> H(z) = \frac{1-2z^{-1}}{(1-\frac12z^{-1})(1-\frac14z^{-1})},\qquad \text{ROC: } \lvert z\rvert>\tfrac12
> $$
> (causal ⇒ outside the outermost pole; it contains the unit circle, consistent with "stable").
>
> (b) PFE: $H(z) = \dfrac{A_1}{1-\frac12z^{-1}}+\dfrac{A_2}{1-\frac14z^{-1}}$ with $A_1 = \dfrac{1-2\cdot2}{1-\frac14\cdot2} = -6$ (set $z = \tfrac12$) and $A_2 = \dfrac{1-2\cdot4}{1-\frac12\cdot4} = 7$ (set $z = \tfrac14$):
> $$
> h[n] = -6\left(\tfrac12\right)^nu[n]+7\left(\tfrac14\right)^nu[n].
> $$
> Check: $h[0] = -6+7 = 1 = \lim_{z\to\infty}H(z)$ ✓.
>
> (c) Cross-multiply: $Y(z)\,(1-\tfrac34z^{-1}+\tfrac18z^{-2}) = X(z)\,(1-2z^{-1})$, so $y[n]-\tfrac34y[n-1]+\tfrac18y[n-2] = x[n]-2x[n-1]$, i.e. for the causal system
> $$
> y[n] = \tfrac34\,y[n-1]-\tfrac18\,y[n-2]+x[n]-2x[n-1].
> $$
> (The official SP2023 key misprints this equation — see [[0-toolkit/05-errata|errata]]; the review slide has it right.) → [[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z) ↔ response]]

### 6.6 Stability and unbounded outputs — SP2023 #7

> [!question] SP2023 #7 — a causal LTI system has $H(z) = \dfrac{z-3}{z-4}$, ROC: $\lvert z\rvert>4$.
> (a) Find a bounded input that produces an unbounded output. (b) Find an unbounded input that produces a bounded output. (c) Find a bounded input that produces a bounded output.

> [!success]- Solution
> In powers of $z^{-1}$: $H(z) = \dfrac{1-3z^{-1}}{1-4z^{-1}}$ — pole at $4$ (outside the unit circle, so unstable), zero at $3$.
>
> (a) $x[n] = \delta[n]$ gives $y[n] = h[n] = 4^nu[n]-3\cdot4^{n-1}u[n-1]$ — unbounded.
>
> (b) Cancel the pole *and* put the input's pole on $H$'s zero: $X(z) = \dfrac{1-4z^{-1}}{1-3z^{-1}}$, i.e. $x[n] = 3^nu[n]-4\cdot3^{n-1}u[n-1]$ (unbounded). Then $Y(z) = X(z)H(z) = 1$ and $y[n] = \delta[n]$.
>
> (c) Cancel only the pole: $X(z) = 1-4z^{-1}$, $x[n] = \delta[n]-4\delta[n-1]$; then $Y(z) = 1-3z^{-1}$ and $y[n] = \delta[n]-3\delta[n-1]$.
>
> → [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]]

## 7. See how it fits together

The [[0-midterm-1/concept-map.canvas|concept map]] is a pannable canvas of the ~25 ideas that carry Midterm 1 — from $\delta[n]$ through convolution and the transfer function to ROCs, causality, stability and the exam's problem families — with labelled arrows showing what depends on what. Click a box to open its page.

> [!tip] In the exam room
> Skim all problems first (two minutes). Bank the T/F and the property table quickly — 24 points, don't overthink. Write the ROC next to **every** transform the moment you write the transform, and mark $n = 0$ on every sequence. Check convolutions with $\sum y = \sum x\cdot\sum h$ and PFEs by $h[0] = \lim_{z\to\infty}H(z)$. Leave ten minutes to re-read what the question actually asks (causal? stable? *all* possible ROCs?).

## Related

[[0-midterm-1/cheat-sheet|cheat sheet]] · [[0-midterm-1/practice-drills|practice drills]] · [[0-midterm-1/true-false-bank|T/F bank]] · [[0-midterm-1/system-property-bank|property bank]] · [[0-midterm-1/past-exams/index|past exams]] · [[problems/index|problem families]] · [[0-toolkit/05-errata|errata]] · [[index|home]]

### Sources for this page

Midterm 1 Review slides and annotated slides (Prof. Snyder, Sep 28, 2026: FA2019 #1, SP2023 #2, FA2023 #3, FA2024 #5, SP2023 #6–#7); cover pages of the past Midterm 1 exams (FA2019–FA2025) for the format; the problem-family × exam map shared across this site; HW3 solutions (ROC grading rubric); lecture notes L1–L11 and the course calendar dates on the slides. Solutions re-verified numerically (`verify/hub/verify_hub.py`, plus the per-exam checks in `verify/exams/`).
