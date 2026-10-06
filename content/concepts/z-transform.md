---
title: "z-transform"
description: "X(z) = Σ x[n] z⁻ⁿ together with its region of convergence: the tool that turns convolution into multiplication and LCCDEs into algebra, and whose poles decide causality and stability."
tags: [concept, z-transform, roc]
aliases: ["z transform", "X(z)"]
---

> [!key] Definition (Lecture 6)
> $$
> X(z) = \sum_{n=-\infty}^{\infty} x[n]\,z^{-n}, \qquad z \in \mathbb{C}, \qquad x[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; X(z)
> $$
> valid on the [[concepts/region-of-convergence|region of convergence]] (ROC), the set of $z$ where the sum converges. **The ROC is part of the transform**: the same formula can belong to different signals.

**Why this sum.** Feed an everlasting exponential $x[n] = z^n$ into an [[concepts/lti-system|LTI system]]:
$$
y[n] = \sum_k h[k]\,z^{n-k} = \Big(\sum_k h[k] z^{-k}\Big) z^n = H(z)\,z^n .
$$
Exponentials pass through unchanged in shape, scaled by $H(z)$, the z-transform of $h[n]$ ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]). Writing signals in terms of exponentials therefore makes every LTI system a multiplication: [[concepts/convolution|convolution]] becomes $Y(z) = H(z)X(z)$ ([[concepts/transfer-function|transfer function]]).

**Why the ROC is a ring.** With $z = re^{j\omega}$, $x[n]z^{-n} = \left(x[n]r^{-n}\right)e^{-j\omega n}$: only $r = |z|$ affects convergence. Large $|z|$ tames the right-hand tail ($n\to+\infty$), small $|z|$ tames the left-hand tail ($n\to-\infty$). On the unit circle $|z|=1$ it becomes the [[concepts/dtft|DTFT]] (see *In Unit 3* below).

**Poles and zeros.** Values of $z$ where $X(z)=0$ are zeros, where $X(z)\to\infty$ poles ([[concepts/poles-and-zeros|poles and zeros]]). The ROC never contains a pole, so pole radii are its edges.

## Computing it

> [!example] Lecture 6, Exercise 1: $u[n]$ versus $-u[-n-1]$
> $$
> \begin{aligned}
> u[n]: &\quad X(z) = \sum_{n=0}^{\infty} z^{-n} = \frac{1}{1-z^{-1}}, & |z^{-1}|<1 \iff |z|>1,\\
> -u[-n-1]: &\quad X(z) = -\sum_{n=-\infty}^{-1} z^{-n} = -\sum_{m=0}^{\infty} z^{m+1}\\
> &\quad\phantom{X(z)} = \frac{-z}{1-z} = \frac{1}{1-z^{-1}}, & |z|<1 .
> \end{aligned}
> $$
> Identical formulas, disjoint ROCs: a z-transform is unique **only with its ROC**.

> [!example] Lecture 6, Exercise 2: $a^n u[n]$
> $X(z) = \sum_{n\ge0}(az^{-1})^n = \dfrac{1}{1-az^{-1}}$, converging for $|a/z|<1$, i.e. ROC $|z|>|a|$, with one pole at $z=a$ (and a zero at $z=0$). Both exercises are [[0-toolkit/02-geometric-series|geometric series]] $\sum_{n\ge0} r^n = \frac{1}{1-r}$, $|r|<1$.

**Finite-length signals** transform by reading off coefficients: $x[n] = \{\underset{\uparrow}{1},\ -\tfrac14,\ \tfrac{1}{16}\}$ gives $X(z) = 1 - \tfrac14 z^{-1} + \tfrac{1}{16}z^{-2}$, ROC $z\neq0$. The sample at $n=k$ multiplies $z^{-k}$.

> [!recipe] "Find $X(z)$ and its ROC" (the exam version)
> 1. **Split** $x[n]$ into pieces that match [[concepts/z-transform-pairs|table rows]]: Euler for $\cos$, $\sin$ and complex exponentials; $a^n u[n-k] = a^k\,a^{n-k}u[n-k]$ for shifts; a two-sided signal into a right-sided part plus a left-sided part.
> 2. **Transform each piece** with its own ROC, using [[concepts/z-transform-properties|properties]] (shift, scaling $a^n x[n]$, differentiation $n\,x[n]$, time reversal) where a row doesn't fit directly.
> 3. **Add** them; the ROC is the **intersection** of the pieces' ROCs. If it is empty, the z-transform does not exist.
> 4. State the ROC explicitly, including whether $z=0$ or $z=\infty$ are excluded.

> [!trap]
> - An answer without "ROC: …" is incomplete — the grading rubrics deduct for missing ROCs and even for a missing $|\cdot|$ in "$|z|>a$".
> - It is $z^{-n}$, not $z^{n}$: the sample at $n=2$ multiplies $z^{-2}$, the one at $n=-3$ multiplies $z^{3}$.
> - The left-sided pair has a **minus**: $-a^nu[-n-1] \leftrightarrow \frac{1}{1-az^{-1}}$.
> - Outside the ROC the formula is meaningless: $\frac{1}{1-\frac12 z^{-1}}$ gives $-1$ at $z=\frac14$, but $\sum (\frac12)^n 4^n$ diverges ([[2-z-transform/07-z-transform-properties|Lecture 7]]).
> - A sinusoid for **all** $n$ (e.g. $e^{j\pi n/4}$) has an empty ROC — no z-transform (SP2025 T/F (c), True).

**In Unit 3.** Setting $z=e^{j\omega}$ (radius 1, angle $\omega$) turns $X(z)=\sum_n x[n]z^{-n}$ into the [[concepts/dtft|DTFT]] $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$, provided the ROC contains the unit circle ([[3-fourier-analysis/14-dtft-properties|Lecture 14]]). The z-transform still covers more signals — $2^nu[n]$ has $X(z)=\frac{1}{1-2z^{-1}}$, ROC $\lvert z\rvert>2$, but no DTFT — while the DTFT shows the frequency content. Many DTFT pairs and properties are the z-transform ones read at $z=e^{j\omega}$ ([[concepts/dtft-pairs|DTFT pairs]], [[concepts/dtft-properties|DTFT properties]]); for $n\,x[n]$ that turns $-z\frac{dX}{dz}$ into $+j\frac{dX_d}{d\omega}$, not the $-j$ printed in Lecture 14's table.

**Where it appears.**
- Lectures: [[2-z-transform/06-the-z-transform|L6]] (definition, motivation, table), [[2-z-transform/07-z-transform-properties|L7]] (ROC rules, properties), [[2-z-transform/08-inverse-z-transform|L8]] (going back), [[2-z-transform/09-transfer-functions|L9]]–[[2-z-transform/11-bibo-stability-and-causality|L11]] (systems).
- Problem families: [[problems/z-transform-with-roc]] (6/7 exams), and through $H(z)$ in [[problems/lccde-to-transfer-function-and-response]], [[problems/all-possible-rocs]], [[problems/unbounded-outputs-and-pole-matching]].
- Homework: [[homework/hw3|HW3]] (all problems), [[homework/hw4|HW4]].
- Past exams: [[exams/midterm-1/past-exams/fall-2025|FA2025 #5]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #5]], [[exams/midterm-1/past-exams/fall-2024|FA2024 #5]], [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]].

Related: [[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/z-transform-properties]] · [[concepts/inverse-z-transform]] · [[concepts/poles-and-zeros]] · [[concepts/transfer-function]] · [[concepts/sided-sequences]] · [[demos/pole-zero-and-roc-explorer]]

### Sources for this page
Lecture 6 notes §1–2 (motivation, definition, Exercises 1–2, Table 1) and slides; Lecture 7 notes §1 (the $X(\frac14)=-1$ remark); Lecture 8 slides, Example 1(a) (finite sequence); HW3 grading rubric (ROC deductions). Verification: `verify/concepts/verify_pairs.py`. The *In Unit 3* paragraph: Lecture 14 §1 (Eqs. 1–6) and Table 2; checked in `verify/CLEAN_unit3.py`.
