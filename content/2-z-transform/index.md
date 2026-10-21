---
title: "Unit 2 · The z-transform and LTI systems"
description: "Lectures 6–11: the z-transform and ROC, properties, inverse by partial fractions, transfer functions, improper H(z) and system algebra, BIBO stability and causality from the ROC. Tested on Midterm 1."
tags: [z-transform, roc, stability, midterm-1]
---

*Unit 2 · Lectures 6–11 · Midterm 1 · prev: [[1-signals-and-systems/index|Unit 1]] · next: [[3-fourier-analysis/index|Unit 3]]*

- Convolution becomes multiplication; a system becomes a rational $H(z)$ with an ROC.
- Stability and causality are statements about the ROC. On the unit circle $H(z)$ becomes $H_d(\omega)$ (Unit 3).

| # | page | one line |
|---|---|---|
| 6 | [[2-z-transform/06-the-z-transform\|The z-transform and the ROC]] | $z_0^n$ eigenfunction; $X(z)=\sum x[n]z^{-n}$; same $X(z)$, different ROC, different signal; ROC shapes |
| 7 | [[2-z-transform/07-z-transform-properties\|Properties of the z-transform]] | shift, linearity, convolution, $n\,x[n]$, $a^nx[n]$, $x[-n]$; ROC changes |
| 8 | [[2-z-transform/08-inverse-z-transform\|The inverse z-transform]] | inspection; cover-up PFE; conjugate poles → cosines; ROC picks each term's side |
| 9 | [[2-z-transform/09-transfer-functions\|Transfer functions and LTI system response]] | $Y=HX$; LCCDE ↔ $H(z)$; poles, zeros; FIR vs IIR |
| 10 | [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|Improper transfer functions and system algebra]] | long division first; parallel $H_1+H_2$, series $H_1H_2$ |
| 11 | [[2-z-transform/11-bibo-stability-and-causality\|BIBO stability and causality]] | stable ⇔ ROC contains $\lvert z\rvert=1$; causal ⇔ ROC outside outermost pole, incl. $z=\infty$; marginal stability |

> [!key] The unit on one card
> - **Transform and ROC:** $X(z)=\sum_n x[n]z^{-n}$, always with its ROC. $a^nu[n]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|>|a|$), $-a^nu[-n-1]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|<|a|$), $\delta[n-k]\leftrightarrow z^{-k}$.
> - **ROC shapes:** no poles inside; right-sided → outside outermost pole; left-sided → inside innermost pole; two-sided → a ring (or nothing); finite → all $z$ except maybe $0$ or $\infty$.
> - **Properties:** $x[n-k]\leftrightarrow z^{-k}X$; $x_1*x_2\leftrightarrow X_1X_2$ (ROC $\supseteq R_1\cap R_2$); $n\,x[n]\leftrightarrow-z\,X'(z)$; $a^nx[n]\leftrightarrow X(z/a)$; $x[-n]\leftrightarrow X(1/z)$.
> - **Inverse:** $X=\sum_k\frac{A_k}{1-p_kz^{-1}}$, $A_k=\big[(1-p_kz^{-1})X(z)\big]_{z=p_k}$ (divide first if improper); $p_k$ inside the ROC's inner circle → right-sided, outside its outer circle → left-sided; $re^{\pm j\omega_0}$ give $2|A|r^n\cos(\omega_0n+\angle A)$.
> - **Systems:** $y[n]+\sum_{k=1}^{N}a_ky[n-k]=\sum_{k}b_kx[n-k]\ \Rightarrow\ H(z)=\frac{\sum b_kz^{-k}}{1+\sum a_kz^{-k}}$; parallel adds, series multiplies.
> - **Stability, causality:** causal ⇔ ROC $|z|>r_{\max}$ incl. $z=\infty$; stable ⇔ ROC contains unit circle; both ⇔ all poles strictly inside $|z|=1$. An input zero can cancel an unstable pole in $Y(z)$.

> [!exam] Exam
> About half to two-thirds of a recent Fall Midterm 1. Families (count of 7 past exams): [[problems/z-transform-with-roc|z-transform with ROC]] 6 · [[problems/all-possible-rocs|inverse z / all ROCs]] 7 · [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z)]] 7 · [[problems/unbounded-outputs-and-pole-matching|unbounded outputs]] 7 · [[problems/finding-h-from-input-output-pairs|finding h]] 7 · [[problems/parameters-for-stability|parameters for stability]] 3 · [[problems/two-sided-systems-as-recursions|two-sided recursions]] 2. Map: [[exams/midterm-1/past-exams/index|past exams]].

**Homework:** [[homework/hw3|HW3]] (L6–L9) · [[homework/hw4|HW4]] (L8–L11) · **Demos:** [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[demos/difference-equation-simulator|difference-equation simulator]] · [[demos/python-demos|Python demos]]

**Concepts:** [[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|pairs]] · [[concepts/z-transform-properties|properties]] · [[concepts/inverse-z-transform|inverse]] · [[concepts/partial-fraction-expansion|partial fractions]] · [[concepts/transfer-function|transfer function]] · [[concepts/system-algebra|system algebra]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/marginal-stability|marginal stability]] · [[concepts/causality|causality]]

### Sources for this page
Snyder, ECE 310 Lectures 6–11 notes and slides (Fall 2026); past Midterm 1 exams FA2019–FA2025.
