---
title: "LTI system"
description: "Discrete-time systems and their four properties; linear + time-invariant: the only systems completely described by one sequence h[n]. Output = convolution, Y(z) = H(z)X(z); the equivalent descriptions and the traps about non-LTI systems."
tags: [concept, systems, convolution, midterm-1]
aliases: ["LTI system", "LSI system", "linear shift-invariant", "linear time-invariant", "LTI", "LSI", "discrete-time system", "system", "system properties"]
---

*Lectures 3 (Fri Aug 28) §1–2 and 4 (Mon Aug 31) §1.2 · [[homework/hw1|HW1]] #5–#6 · [[homework/hw2|HW2]] #1–#4 · families: [[problems/classifying-system-properties|Classifying system properties]], [[problems/finding-h-from-input-output-pairs|Finding h from input–output pairs]]*

> [!abstract] In one breath
> - A system is any rule $T$ with $y[n] = T(x[n])$; four yes/no properties: linear, time-invariant, causal, BIBO stable.
> - LTI ⇔ output is a convolution $y = x * h$ ⇔ fully described by $h$. Prove for *every* input; disprove with *one* counterexample.
> - Non-LTI systems also have an $h$, but it says nothing about other inputs.

## 1. Discrete-time systems

> [!key] Discrete-time system (Lecture 3, eqs. 1–2)
> Any computational process mapping a discrete-time input $x[n]$ to a discrete-time output $y[n]$. With operator $T$:
> $$
> x[n] \overset{T}{\longmapsto} y[n], \qquad y[n] = T(x[n]).
> $$
> "$x[n]$ maps to $y[n]$ by $T$"; "$y[n]$ is a function of $x[n]$ described by $T$".

Examples (notes eqs. 3–4, slide 3):
- $y[n] = x[n] - x[n-1]$: present minus previous sample; detects fast changes.
- $y[n] = \operatorname{median}\{x[n], x[n-1], x[n-2]\}$: running median.
- $y[n] = \text{HalfCenterCrop}(x[n])$, $\text{SnapchatFilter}(x[n])$: image operations.

**Systems are not just filters**: photo editing, speech recognition, trading algorithms, recommendation systems, de-noising filters all qualify.

## 2. The four properties

Four yes/no properties (Lecture 3 §2): [[concepts/linearity|linear]] (superposition), [[concepts/time-invariance|time-invariant]] (shift in ⇒ same shift out), [[concepts/causality|causal]] (no future inputs), [[concepts/bibo-stability|BIBO stable]] (bounded in ⇒ bounded out). LTI (linear, time-invariant) systems are the course's focus; non-linear, time-varying and non-causal systems still appear in practice (ECE 311). Prove for *every* input; disprove with *one* counterexample.

## 3. Reading the four properties off a formula

> [!recipe] A property-table row in 30 seconds
> | property | it **fails** when you see… | it **holds** for… |
> |---|---|---|
> | linear | a function of the input's value ($\lvert x\rvert$, $x^2$, $e^{x}$, $\log x$, $\sin x$, clip, max, median); a product of input samples ($x[n]\,x[n+1]$, $x[3]\,x[n]$); division by an input sample; an added constant ($x[n]+3$) | sums of input samples times fixed coefficients, even coefficients that depend on $n$; pure index maps $x[f(n)]$ |
> | time-invariant | $n$ outside the brackets ($n\,x[n]$, $\cos(\pi n/2)\,x[n]$, a window); an index map other than $n-k$ ($x[2n]$, $x[-n]$, $x[\lvert n\rvert]$); a fixed sample ($x[0]$, $x[2]$) | constant-coefficient sums of $x[n-k]$; any function of $x[n]$ alone; convolution with a fixed $h$ |
> | causal | some $n$ (try negative ones!) whose input index exceeds $n$: $x[n+1]$, $x[\lvert n\rvert]$, $x[2n]$, $x[0]$; convolution with $h[n] \ne 0$ for some $n < 0$ | only $x[n-k]$ with $k \ge 0$ |
> | BIBO stable | a multiplier that grows ($n$, $\lvert n\rvert$, $\log(\lvert n\rvert+1)$, $2^n$, $(0.8+0.8j)^n$ with $\lvert 0.8+0.8j\rvert \approx 1.13$); $\log x$ or $1/x$ (a bounded input may be $0$); convolution with an $h$ that is not absolutely summable | bounded multipliers times bounded functions of finitely many input samples ($e^{x[n]}$ is stable); convolution with $\sum_n \lvert h[n]\rvert < \infty$ |

Every past row with proofs: [[exams/midterm-1/system-property-bank|system-property bank]]; recipe and practice: [[problems/classifying-system-properties|classifying system properties]], [[demos/practice-drills|drills]].

## 4. Why LTI systems are special

Write any input as shifted impulses, $x[n]=\sum_k x[k]\,\delta[n-k]$ ([[concepts/kronecker-delta|Kronecker delta]]). With $h[n] = T(\delta[n])$ the [[concepts/impulse-response|impulse response]]:

| input | output | property |
|---|---|---|
| $\delta[n]$ | $h[n]$ | definition |
| $a\,\delta[n]$ | $a\,h[n]$ | homogeneity |
| $\delta[n-k]$ | $h[n-k]$ | time-invariance |
| $\delta[n] + \delta[n-k]$ | $h[n] + h[n-k]$ | additivity |
| $\sum_k x[k]\,\delta[n-k]$ | $\sum_k x[k]\,h[n-k]$ | all three |

> [!key] LTI response (Lecture 4, eq. 7) and the "if and only if" triangle (Fig. 1)
> $$
> y[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]=(x*h)[n],\qquad Y(z)=H(z)\,X(z).
> $$
> **LTI** ⇔ output is a **[[concepts/convolution|convolution]]** with some $h$ ⇔ **fully described by $h$** (output known for every input). **LSI** (linear shift-invariant, older exams) is the same thing; the **unit pulse response** is the impulse response.

**Worked example (Lecture 4).** The difference system $y[n]=x[n]-x[n-1]$ is LTI (Lecture 3, Exercises 1 and 4) with $h[n]=\delta[n]-\delta[n-1]$, and $x*h$ reproduces it for every input. The three-point median filter has $h[n]=0$ (every window of $\delta$ holds one $1$, two $0$s), yet it maps $u[n]$ to $u[n-1]$: it is nonlinear, so its $h$ says nothing.

## 5. One system, five descriptions

The first-order system of Lectures 5 and 9:

| description | what it is | example |
|---|---|---|
| [[concepts/impulse-response\|impulse response]] | output for the input $\delta[n]$ | $h[n]=(\frac12)^nu[n]$ |
| [[concepts/transfer-function\|transfer function]] + ROC | $Y(z)/X(z)=\mathcal{Z}\{h\}$ | $H(z)=\frac{1}{1-\frac12z^{-1}}$, $\lvert z\rvert>\frac12$ |
| [[concepts/lccde\|LCCDE]] + causality (initial rest) | the recursion you run | $y[n]=\frac12y[n-1]+x[n]$ |
| [[concepts/block-diagram\|block diagram]] | delays, gains, adders | one delay, feedback gain $\frac12$ |
| [[concepts/eigenfunctions-of-lti-systems\|eigenvalues]] | response to $z_0^n$ (all $n$) | $H(z_0)\,z_0^n$ |

**Properties read off $h$:** [[concepts/causality|causal]] $\iff h[n]=0$ for $n<0$; [[concepts/bibo-stability|BIBO stable]] $\iff\sum\lvert h[n]\rvert<\infty\iff$ ROC $\ni$ unit circle; [[concepts/fir-and-iir|FIR]] $\iff$ finitely many nonzero samples. **Interconnections** ([[concepts/system-algebra|system algebra]]): series $h_1*h_2$ ($H_1H_2$, order irrelevant), parallel $h_1+h_2$ ($H_1+H_2$).

> [!trap]
> - **"The output is always determined by $h$" is False unless the system is LTI**: [[exams/midterm-1/past-exams/fall-2024|FA2024 #1a]], [[exams/midterm-1/past-exams/fall-2023|FA2023 #1d]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #1b]] (all F). The converse is True: a system whose every response is fully described by $h$ must be LTI ([[exams/midterm-1/past-exams/spring-2023|SP2023 #1a]]).
> - **$h=0$ does not mean "zero system"** for non-LTI systems: the median filter above; $y=n\,x[n]$ answers $\delta[n]$ with $n\,\delta[n]=0$.
> - **Swapping blocks in a cascade is safe only for LTI blocks** ([[exams/midterm-1/past-exams/fall-2023|FA2023 #1e]] T). A time-varying block does not commute: "$n\,x[n]$, then delay" gives $(n-1)x[n-1]$, "delay, then $n\,x[n]$" gives $n\,x[n-1]$.
> - An LCCDE describes an LTI system only **at initial rest** (zero initial conditions); to **prove** a convolution system is LTI, show superposition and shift-invariance of the sum ([[homework/hw2|HW2]] #2).
> - **The four properties are independent**: $n\,x[n]$ is linear, causal, time-varying, unstable; $e^{x[n]}$ is nonlinear, TI, causal, stable.
> - **BIBO says nothing about unbounded inputs**: "stable ⇒ unbounded in gives unbounded out" is False.

> [!exam] The property table: 7 of 7 past exams, 12 points
> Three systems × four yes/no boxes, graded on the boxes; plus True/False on the properties' independence and on "described by $h$".
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #1(e), #2, #4]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(b), #2]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(a), #2]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1(a)(d)(e), #2]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #1(a)(b), #2]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #3]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(b)(f), #2]] · [[exams/midterm-1/system-property-bank|system-property bank]] · [[exams/midterm-1/true-false-bank|T/F bank]]

**Where it appears:** [[1-signals-and-systems/03-system-properties|Lecture 3]] §1–2, [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]] §1.2, [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/06-the-z-transform|Lecture 6]] §1, [[2-z-transform/09-transfer-functions|Lecture 9]] §1, [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]] (series/parallel); [[homework/hw1|HW1]] #5–#6, [[homework/hw2|HW2]] #1–#4; [[problems/classifying-system-properties|classifying system properties]] (7/7), [[problems/finding-h-from-input-output-pairs|finding h]] (7/7, e.g. [[exams/midterm-1/past-exams/fall-2024|FA2024 #3]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #3]]); [[demos/practice-drills|practice drills]].

## Related
[[concepts/linearity|linearity]] · [[concepts/time-invariance|time-invariance]] · [[concepts/causality|causality]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/convolution|convolution]] · [[concepts/impulse-response|impulse response]] · [[concepts/transfer-function|transfer function]] · [[concepts/system-algebra|system algebra]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]

### Sources for this page
Lecture 3 §1 (eqs. 1–4), §2 and slide 3; Lecture 4 §1.2 (eq. 7) and Fig. 1; Lecture 5 eq. 6; Lecture 9 eqs. 2 and 8–12; Lecture 10 Table 1; HW2 #2 solution; T/F items FA2024 #1a, FA2023 #1d–e, SP2023 #1a, FA2019 #1b; the seven property tables.
