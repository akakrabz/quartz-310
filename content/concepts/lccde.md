---
title: "Linear constant-coefficient difference equation (LCCDE)"
description: "The recursion behind every practical LTI system: Lecture 5's form, feedback and input terms, initial rest, causality, the Lecture 9 sign convention and H(z), running the recursion, scipy.signal.lfilter."
tags: [concept, lccde, systems, z-transform, midterm-1]
aliases: ["difference equation", "LCCDE", "linear constant-coefficient difference equation", "recursion", "recursive system", "initial rest", "zero initial conditions", "feedback"]
---

*Lectures 5 (Wed Sep 2) §1 and 9 (Mon Sep 14) §1.1 · [[homework/hw2|HW2]] #1 · [[homework/hw4|HW4]] #6 · families: [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]] (7/7), [[problems/two-sided-systems-as-recursions|Two-sided systems as recursions]] · demo: [[demos/difference-equation-simulator|simulator]]*

> [!abstract] In one breath
> - Each output is a fixed linear combination of current/past inputs and past outputs; at rest (zero initial conditions) it is LTI.
> - No feedback ⇒ $h$ is the coefficient list (FIR); feedback ⇒ $h$ can ring forever (IIR), yet the recursion is cheap to run.
> - Lecture 5 writes feedback with $+b_i$; Lecture 9, the exams and `lfilter` move it left with $+a_k$: signs flip.

## 1. Definition (Lecture 5)

> [!key] LCCDE (Lecture 5, eq. 1)
> $$
> y[n] = \sum_{i=1}^{K} b_i\,y[n-i] + \sum_{j=0}^{M-1} c_j\,x[n-j], \qquad 0 \le K < \infty,\quad 1 \le M < \infty .
> $$
> - $K$ **feedback** (output) terms, coefficients $b_1, \dots, b_K$ at delays $1, \dots, K$.
> - $M$ **input** terms, coefficients $c_0, \dots, c_{M-1}$ at delays $0, \dots, M-1$.

- **Zero initial conditions** ("at rest"): $y[n] = 0$ before the input arrives; in hardware, clear the memory first. Assumed throughout; this is what makes the system LTI.
- All shifts non-negative ⇒ no future values ⇒ the recursion runs **causally**. Non-causal LCCDEs have terms like $x[n+2]$ or $y[n+1]$; and the equation alone does not fix causality ([[concepts/causality|causality]]).
- $K = 0$: [[concepts/fir-and-iir|FIR]], $h[n] = \{\underset{\uparrow}{c_0}, \dots, c_{M-1}\}$. $K > 0$: IIR in general ([[concepts/fir-and-iir|FIR and IIR]], with the worked recursions of Lecture 5).

## 2. Standard form (Lecture 9) and the sign convention

> [!key] Standard form (Lecture 9, same `b, a` as `lfilter`)
> $$
> \begin{gathered}
> y[n]+\sum_{k=1}^{N}a_k\,y[n-k]=\sum_{k=0}^{M-1}b_k\,x[n-k]
> \\[4pt] \Big\Downarrow \\[4pt]
> H(z)=\frac{Y(z)}{X(z)}=\frac{\sum_{k=0}^{M-1}b_k\,z^{-k}}{1+\sum_{k=1}^{N}a_k\,z^{-k}}
> \end{gathered}
> $$
> So $a_k = -\,b_k^{(\text{L5})}$ and $b_k^{(\text{L9})} = c_k^{(\text{L5})}$: in Lecture 5 "$b$" is feedback, in Lecture 9 feedforward. $y[n] = \tfrac12 y[n-1] + x[n]$: $b_1 = +\tfrac12$ in Lecture 5, $a_1 = -\tfrac12$ and `lfilter([1], [1, -0.5], x)` in Lecture 9. Transfer functions and LCCDEs in full: [[concepts/transfer-function|transfer function]].

## 3. Running it

- **Run it:** solve for $y[n]$, step forward from rest. $y[n]=\frac12y[n-1]+x[n]$ with $x = \delta$ gives $1, \tfrac12, \tfrac14, \dots$, so $h[n]=(\frac12)^nu[n]$.
- **No feedback** ⇒ $h$ is the $b_k$ list ([[concepts/fir-and-iir|FIR]]). Second-order feedback needs the z-transform and partial fractions (Lecture 9); until then, iterate by hand.
- **ROC** comes from causality or stability, not from the equation.

> [!example] FA2025 #6: $y[n]=\frac43y[n-1]+\frac43y[n-2]+x[n]-x[n-2]$
> $$
> H(z)=\frac{1-z^{-2}}{(1-2z^{-1})(1+\frac23z^{-1})},
> $$
> poles $2,-\frac23$, zeros $\pm1$; causal ROC $\lvert z\rvert>2$, not stable. Backwards ([[exams/midterm-1/past-exams/spring-2025|SP2025 #8]]): $H=\frac{2-3z^{-1}}{1+z^{-1}-\frac34z^{-2}}$ is $y[n]+y[n-1]-\frac34y[n-2]=2x[n]-3x[n-1]$.

> [!trap]
> - **Sign flip**: $y[n]-\frac12y[n-1]=x[n]$ is `a = [1, -0.5]`; a feedback gain $+\tfrac12$ in a Lecture 5 block diagram is $a_1 = -\tfrac12$ in Lecture 9. Normalize first ($y[n-2]+2y[n]$, [[homework/hw2|HW2]] #1b).
> - **The equation does not fix causality** ([[exams/midterm-1/past-exams/fall-2019|FA2019 #1a]]): the same LCCDE has a causal and an anti-causal solution.
> - **"Feedback ⇒ IIR" can fail** when a pole is cancelled: the recursive moving average is FIR ([[concepts/pole-zero-cancellation|pole-zero cancellation]]).
> - $y[n]=2y[n-3]-x[n]+x[n-3]$: $h[0]=-1$, $h[3]=-1$ (SP2021 #6 key slips; [[0-toolkit/05-errata|errata]]).
> - Finitely many poles; $y[n]=y[n-3]+x[n]$ has three, the cube roots of unity ([[exams/midterm-1/past-exams/fall-2024|FA2024 #1e]]).

> [!exam] LCCDE ↔ $H(z)$ ↔ response, 7 of 7 exams (Lecture 9 sign convention)
> Also tested: FIR ⇒ stable; an LCCDE alone does not fix causality; recursions run backwards.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #4, #6, #7(b)]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #6]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #1(a), #1(e), #10]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #1(d)(e)]] · [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]] · [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]]

**Where it appears:** [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] §1, [[2-z-transform/09-transfer-functions|Lecture 9]] §1.1, [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]; [[homework/hw2|HW2]] #1, [[homework/hw4|HW4]] #6; [[problems/lccde-to-transfer-function-and-response|LCCDE → transfer function → response]] (7/7), [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]]; [[demos/difference-equation-simulator|difference-equation simulator]], [[supplements/demo-notebooks|course demo notebooks]].

## Related
[[concepts/transfer-function|transfer function]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/block-diagram|block diagram]] · [[concepts/impulse-response|impulse response]] · [[concepts/causality|causality]] · [[concepts/lti-system|LTI system]]

### Sources for this page
Lecture 5 §1 (eqs. 1, 5–7, 12); Lecture 9 §1.1 (eqs. 4–7); Lecture 10 §1; HW2 #1, HW4 #6; FA2025 #6, SP2025 #8, SP2021 #6, FA2019 #1a, FA2024 #1d–e.
