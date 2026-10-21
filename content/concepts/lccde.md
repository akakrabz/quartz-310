---
title: "Linear constant-coefficient difference equation (LCCDE)"
description: "The recursion behind every practical LTI system: the sign conventions of Lectures 5 and 9, initial rest, running the recursion, reading off H(z), scipy.signal.lfilter."
tags: [concept, lccde, systems, z-transform, midterm-1]
aliases: ["difference equation", "LCCDE", "linear constant-coefficient difference equation", "recursion", "recursive system"]
---

> [!key] Standard form (Lecture 9, same `b, a` as `lfilter`)
> $$
> \begin{gathered}
> y[n]+\sum_{k=1}^{N}a_k\,y[n-k]=\sum_{k=0}^{M-1}b_k\,x[n-k]
> \\[4pt] \Big\Downarrow \\[4pt]
> H(z)=\frac{Y(z)}{X(z)}=\frac{\sum_{k=0}^{M-1}b_k\,z^{-k}}{1+\sum_{k=1}^{N}a_k\,z^{-k}}
> \end{gathered}
> $$
> Lecture 5 writes $y[n]=\sum_{i=1}^{K}b_i\,y[n-i]+\sum_{j=0}^{M-1}c_j\,x[n-j]$: feedback signs flipped ($a_i=-b_i$). **Initial rest** makes it LTI.

- **Run it:** solve for $y[n]$, step forward from rest. $y[n]=\frac12y[n-1]+x[n]$ gives $h[n]=(\frac12)^nu[n]$.
- **No feedback** ⇒ $h$ is the $b_k$ list ([[concepts/fir-and-iir|FIR]]).
- **ROC** comes from causality or stability, not from the equation.

> [!example] FA2025 #6: $y[n]=\frac43y[n-1]+\frac43y[n-2]+x[n]-x[n-2]$
> $$
> H(z)=\frac{1-z^{-2}}{(1-2z^{-1})(1+\frac23z^{-1})},
> $$
> poles $2,-\frac23$, zeros $\pm1$; causal ROC $\lvert z\rvert>2$, not stable. Backwards ([[exams/midterm-1/past-exams/spring-2025|SP2025 #8]]): $H=\frac{2-3z^{-1}}{1+z^{-1}-\frac34z^{-2}}$ is $y[n]+y[n-1]-\frac34y[n-2]=2x[n]-3x[n-1]$.

> [!trap]
> - Sign flip: $y[n]-\frac12y[n-1]=x[n]$ is `a = [1, -0.5]`. Normalize first ($y[n-2]+2y[n]$, [[homework/hw2|HW2]] #1b).
> - The equation does not fix causality ([[exams/midterm-1/past-exams/fall-2019|FA2019 #1a]]).
> - $y[n]=2y[n-3]-x[n]+x[n-3]$: $h[0]=-1$, $h[3]=-1$ (SP2021 #6 key slips; [[0-toolkit/05-errata|errata]]).
> - Finitely many poles; $y[n]=y[n-3]+x[n]$ has three, the cube roots of unity ([[exams/midterm-1/past-exams/fall-2024|FA2024 #1e]]).

**Where it appears:** [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]; [[homework/hw2|HW2]] #1, [[homework/hw4|HW4]] #6; [[problems/lccde-to-transfer-function-and-response]] (7/7), [[problems/two-sided-systems-as-recursions]]; [[demos/difference-equation-simulator]].

## Related
[[concepts/transfer-function|transfer function]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/block-diagram|block diagram]] · [[concepts/impulse-response|impulse response]] · [[concepts/causality|causality]]

### Sources for this page
Lecture 5 §1 (Eqs. 1, 5–7, 12); Lecture 9 §1.1 (Eqs. 4–7); Lecture 10 §1; HW2 #1, HW4 #6; FA2025 #6, SP2025 #8, SP2021 #6, FA2019 #1a, FA2024 #1d–e.
