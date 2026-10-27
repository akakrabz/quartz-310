---
title: "Unit 2 · The z-transform and LTI systems"
description: "Topics of Lectures 6–11: the z-transform and ROC, properties, inverse by partial fractions, transfer functions, improper H(z) and system algebra, BIBO stability and causality from the ROC. Tested on Midterm 1."
tags: [z-transform, roc, stability, midterm-1]
---

*Unit 2 · Lectures 6–11 · Midterm 1 · prev: [[1-signals-and-systems/index|Unit 1]] · next: [[3-fourier-analysis/index|Unit 3]]*

- Convolution becomes multiplication; a system is a rational $H(z)$ with an ROC.
- Stability and causality are statements about the ROC; on the unit circle $H(z)$ is $H_d(\omega)$ (Unit 3).

## Topics

**z-domain**
- [[concepts/eigenfunctions-of-lti-systems|Eigenfunctions of LTI systems]] — $z^n\mapsto H(z)z^n$: why the z-transform.
- [[concepts/sided-sequences|Sided sequences]] — right-, left-, two-sided; the ROC each forces.
- [[concepts/z-transform|z-transform]] — $X(z)=\sum_n x[n]z^{-n}$, always with its ROC.
- [[concepts/region-of-convergence|Region of convergence]] — rings bounded by poles; decides the signal.
- [[concepts/poles-and-zeros|Poles and zeros]] — pole-zero plot.
- [[concepts/z-transform-pairs|z-transform pairs]] — $\delta[n-k]$, $a^nu[n]$, $-a^nu[-n-1]$, $na^nu[n]$, sinusoids.
- [[concepts/z-transform-properties|z-transform properties]] — shift, convolution, $n\,x[n]$, $a^nx[n]$, $x[-n]$; ROC changes.
- [[concepts/inverse-z-transform|Inverse z-transform]] — inspection or PFE; ROC picks each term's side.
- [[concepts/partial-fraction-expansion|Partial fraction expansion]] — cover-up; long division if improper.
- [[concepts/transfer-function|Transfer function]] — $Y=HX$; LCCDE ↔ $H(z)$.
- [[concepts/system-algebra|System algebra]] — series multiplies, parallel adds.

**Stability**
- [[concepts/bibo-stability|BIBO stability]] — $\sum\lvert h[n]\rvert<\infty$ ⇔ ROC ∋ $\lvert z\rvert=1$.
- [[concepts/causality|Causality]] — ROC outside the outermost pole, incl. $z=\infty$.
- [[concepts/pole-zero-cancellation|Pole-zero cancellation]] — an input zero cancels an unstable pole.
- [[concepts/marginal-stability|Marginal stability]] — unit-circle poles; resonant inputs blow up.

## Lectures
6. [[2-z-transform/06-the-z-transform|z-transform and ROC]] (Sep 4)
7. [[2-z-transform/07-z-transform-properties|z-transform properties]] (Sep 9)
8. [[2-z-transform/08-inverse-z-transform|Inverse z-transform]] (Sep 11)
9. [[2-z-transform/09-transfer-functions|Transfer functions]] (Sep 14)
10. [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Improper H(z), system algebra]] (Sep 16)
11. [[2-z-transform/11-bibo-stability-and-causality|BIBO stability and causality]] (Sep 18)

> [!key] The unit on one card
> - **Transform and ROC:** $a^nu[n]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|>|a|$), $-a^nu[-n-1]\leftrightarrow\frac{1}{1-az^{-1}}$ ($|z|<|a|$), $\delta[n-k]\leftrightarrow z^{-k}$.
> - **ROC shapes:** right-sided → outside the outermost pole; left-sided → inside the innermost; two-sided → a ring; finite → all $z$ but maybe $0$, $\infty$.
> - **Properties:** $x[n-k]\leftrightarrow z^{-k}X$; $x_1*x_2\leftrightarrow X_1X_2$ (ROC $\supseteq R_1\cap R_2$); $n\,x[n]\leftrightarrow-z\,X'(z)$; $a^nx[n]\leftrightarrow X(z/a)$; $x[-n]\leftrightarrow X(1/z)$.
> - **Inverse:** $X=\sum_k\frac{A_k}{1-p_kz^{-1}}$, $A_k=\big[(1-p_kz^{-1})X(z)\big]_{z=p_k}$ (divide if improper); $p_k$ inside the ROC → right-sided, outside → left-sided; $re^{\pm j\omega_0}$ → $2|A|r^n\cos(\omega_0n+\angle A)$.
> - **Systems:** $y[n]+\sum_{k=1}^{N}a_ky[n-k]=\sum_{k}b_kx[n-k]\ \Rightarrow\ H(z)=\frac{\sum b_kz^{-k}}{1+\sum a_kz^{-k}}$.
> - **Stability, causality:** causal ⇔ ROC $|z|>r_{\max}$ incl. $z=\infty$; stable ⇔ ROC contains unit circle; both ⇔ all poles strictly inside $|z|=1$.

> [!exam] Exam
> Families (count of 7 past exams): [[problems/z-transform-with-roc|z-transform with ROC]] 6 · [[problems/all-possible-rocs|inverse z / all ROCs]] 7 · [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z)]] 7 · [[problems/unbounded-outputs-and-pole-matching|unbounded outputs]] 7 · [[problems/finding-h-from-input-output-pairs|finding h]] 7 · [[problems/parameters-for-stability|parameters for stability]] 3 · [[problems/two-sided-systems-as-recursions|two-sided recursions]] 2. Map: [[exams/midterm-1/past-exams/index|past exams]].

**Homework:** [[homework/hw3|HW3]] (L6–L9) · [[homework/hw4|HW4]] (L8–L11) · **Demos:** [[demos/pole-zero-and-roc-explorer|pole-zero/ROC explorer]] · [[demos/difference-equation-simulator|LCCDE simulator]] · [[demos/python-demos|Python]]

## Related
[[1-signals-and-systems/index|Unit 1]] · [[3-fourier-analysis/index|Unit 3]] · [[concepts/index|Concepts]] · [[0-toolkit/05-errata|errata]]

### Sources for this page
Snyder, ECE 310 Lectures 6–11 notes and slides (Fall 2026); past Midterm 1 exams.
