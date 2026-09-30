---
title: "Unit 2 · The z-transform and LTI systems"
description: "Lectures 6–11: the z-transform and its region of convergence, its properties, the inverse transform by partial fractions, transfer functions of difference equations, improper transfer functions and system algebra, and BIBO stability and causality read off the ROC — the second half of Midterm 1."
tags: [z-transform, roc, stability, midterm-1]
---

Unit 1 described an LTI system by its impulse response and computed outputs by convolution. Unit 2 moves to the z-domain, where convolution becomes multiplication and a system becomes a rational function $H(z)$ you can read at a glance. The unit builds one idea at a time: the transform and its region of convergence (L6); properties that transform almost anything from a few pairs (L7); the way back to time by partial fractions, with the ROC choosing each term's side (L8); transfer functions of LCCDEs and the response $Y=HX$ (L9); improper $H(z)$ and connected systems (L10); and stability and causality as statements about the ROC (L11). **All six lectures are on Midterm 1** (Lecture 12 is not).

| # | page | one line |
|---|---|---|
| 6 | [[2-z-transform/06-the-z-transform\|The z-transform and the region of convergence]] | $z_0^n$ is an eigenfunction, $H(z_0)=\sum h[k]z_0^{-k}$; $X(z)=\sum x[n]z^{-n}$; same $X(z)$ + different ROC = different signal; finite, right-, left-, two-sided ROC shapes; table of pairs |
| 7 | [[2-z-transform/07-z-transform-properties\|Properties of the z-transform]] | $X$ undefined outside the ROC; shift ($z^{-k}$, watch $0$ and $\infty$), linearity and convolution (ROC at least the intersection), $n\,x[n]\leftrightarrow-z\frac{dX}{dz}$, $a^nx[n]\leftrightarrow X(z/a)$, $x[-n]\leftrightarrow X(z^{-1})$ |
| 8 | [[2-z-transform/08-inverse-z-transform\|The inverse z-transform]] | inspection; partial fractions with cover-up in $z^{-1}$ form; conjugate poles → cosines; poles inside the ROC → right-sided, outside → left-sided; $M+1$ possible ROCs; `residuez` |
| 9 | [[2-z-transform/09-transfer-functions\|Transfer functions and LTI system response]] | $Y(z)=H(z)X(z)$; LCCDE ↔ $H(z)=\frac{\sum b_kz^{-k}}{1+\sum a_kz^{-k}}$; poles, zeros, order; FIR vs IIR |
| 10 | [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|Improper transfer functions and system algebra]] | long division before partial fractions (or expand $1/A(z)$ and shift); parallel $H_1+H_2$, series $H_1H_2$ |
| 11 | [[2-z-transform/11-bibo-stability-and-causality\|BIBO stability and causality]] | stable ⇔ $\sum\lvert h[n]\rvert<\infty$ ⇔ ROC contains $\lvert z\rvert=1$; causal ⇔ ROC outside the outermost pole, including $z=\infty$; bounded inputs with unbounded outputs; marginal stability |

> [!key] The unit on one card
> - **Transform and ROC:** $X(z)=\sum_n x[n]z^{-n}$, defined only on its ROC — always state it. $a^nu[n]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|>|a|$), $-a^nu[-n-1]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|<|a|$), $\delta[n-k]\leftrightarrow z^{-k}$.
> - **ROC shapes:** no poles inside; right-sided → outside the outermost pole; left-sided → inside the innermost pole; two-sided → a ring (or nothing); finite → all $z$ except maybe $0$ or $\infty$.
> - **Properties:** $x[n-k]\leftrightarrow z^{-k}X$; $x_1*x_2\leftrightarrow X_1X_2$ (ROC $\supseteq R_1\cap R_2$, larger after a pole-zero cancellation); $n\,x[n]\leftrightarrow-z\,X'(z)$; $a^nx[n]\leftrightarrow X(z/a)$; $x[-n]\leftrightarrow X(1/z)$.
> - **Inverse:** partial fractions $X=\sum_k\frac{A_k}{1-p_kz^{-1}}$, $A_k=\big[(1-p_kz^{-1})X(z)\big]_{z=p_k}$ (divide first if improper); each term right-sided if $p_k$ is inside the ROC, left-sided if outside; conjugate poles $re^{\pm j\omega_0}$ give $2|A|r^n\cos(\omega_0n+\angle A)$.
> - **Systems:** $y[n]+\sum_{k=1}^{N}a_ky[n-k]=\sum_{k}b_kx[n-k]\ \Rightarrow\ H(z)=\frac{\sum b_kz^{-k}}{1+\sum a_kz^{-k}}$, and $Y=HX$. Parallel adds, series multiplies.
> - **Stability and causality:** causal ⇔ ROC is $|z|>r_{\max}$ including $z=\infty$; BIBO stable ⇔ ROC contains the unit circle; causal **and** stable ⇔ every pole strictly inside $|z|=1$. An input zero can cancel an unstable pole in $Y(z)$.

> [!exam] Which exam problems this unit feeds
> On a recent Fall exam roughly half to two-thirds of the 100 points come from this unit (z-transforms 9–15, LCCDE/transfer function 15–20, PFE/ROC/stability 15–20, pole matching or a parameter problem 10, plus True/False items).
>
> | problem family | past exams | lectures |
> |---|---|---|
> | [[problems/z-transform-with-roc\|z-transform with ROC]] | 6/7 | L6, L7 |
> | [[problems/all-possible-rocs\|inverse z / PFE / all possible ROCs]] | 7/7 | L8, L11 |
> | [[problems/lccde-to-transfer-function-and-response\|LCCDE ⇄ transfer function ⇄ response]] | 7/7 | L9, L10 |
> | [[problems/unbounded-outputs-and-pole-matching\|unbounded outputs and pole matching]] | 7/7 | L9, L11 |
> | [[problems/finding-h-from-input-output-pairs\|finding h (or H) from input–output pairs]] | 7/7 | L4, L9 ($H=Y/X$) |
> | [[problems/parameters-for-stability\|parameters for stability]] | 3/7 | L11 |
> | [[problems/two-sided-systems-as-recursions\|two-sided systems as recursions]] | 2/7 | L5, L11 |
>
> Stability, causality and ROC statements are also regulars in the [[0-midterm-1/true-false-bank|True/False bank]]. Problem-by-problem maps: [[0-midterm-1/past-exams/index|past exams]].

**Homework for this unit:** [[homework/hw3|HW3]] (z-transforms, properties, inverse transforms, a right-sided system — L6–L9) · [[homework/hw4|HW4]] (all possible ROCs, BIBO stability, finding $h$, systems in series — L8–L11)

**Demos:** [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[demos/difference-equation-simulator|difference-equation simulator]] · [[demos/python-demos|Python demos]] (`residuez`, `lfilter`, `tf2zpk`)

**Concepts:** [[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|pairs]] · [[concepts/z-transform-properties|properties]] · [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/partial-fraction-expansion|partial fractions]] · [[concepts/transfer-function|transfer function]] · [[concepts/system-algebra|system algebra]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/causality|causality]]

**Before and after:** [[1-signals-and-systems/index|Unit 1 · Signals and systems]] (L1–L5) · [[3-beyond-midterm-1/index|beyond Midterm 1]] (L12–L14, not tested)
