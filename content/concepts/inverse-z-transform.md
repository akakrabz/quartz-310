---
title: "Inverse z-transform"
description: "x[n] from X(z) and its ROC: by inspection for finite and table-shaped transforms, by partial fractions for rational ones; the ROC decides each term's side."
tags: [concept, z-transform, roc]
aliases: ["inverse z-transform", "inverse z transform"]
---

> [!key] The rule (Lecture 8)
> Methods: read coefficients of finite sequences, match [[concepts/z-transform-pairs|table rows]], or [[concepts/partial-fraction-expansion|PFE]]. The [[concepts/region-of-convergence|ROC]] picks each term:
> $$
> \frac{A}{1-pz^{-1}} \;\longrightarrow\;
> \begin{cases} A\,p^n\,u[n], & |z|>|p|,\\[2pt]
> -A\,p^n\,u[-n-1], & |z|<|p|. \end{cases}
> $$

> [!example] Lecture 8 slides, Example 1
> - $1-\frac14 z^{-1}+\frac{1}{16}z^{-2}$: $\{\underset{\uparrow}{1},\ -\tfrac14,\ \tfrac{1}{16}\}$.
> - $\dfrac{1}{1+\frac13 z^{-1}}$, $|z|<\frac13$: $-\left(-\frac13\right)^n u[-n-1]$.
> - $\dfrac{1}{1-\frac12 z^{-1}} - \dfrac{3z^{-1}}{1+\frac15 z^{-1}}$, $|z|>\frac12$: $\left(\frac12\right)^n u[n] - 3\left(-\frac15\right)^{n-1}u[n-1]$.

> [!recipe] Rational $X(z)$
> 1. Powers of $z^{-1}$; cancel common factors. 2. Improper: long division ($C_k\delta[n-k]$) or pull out $z^{-k}$.
> 3. PFE. 4. Each pole's side from the ROC. 5. Re-apply delays; state $u[\cdot]$ factors.

> [!example] Lecture 8 slides, Example 3: $X(z) = \dfrac{1}{\left(1-\frac43 z^{-1}\right)\left(1-\frac23 z^{-1}\right)} = \dfrac{2}{1-\frac43 z^{-1}} - \dfrac{1}{1-\frac23 z^{-1}}$
> List every ROC.

> [!success]- Answer
> - $|z|>\frac43$: $x[n] = 2\left(\frac43\right)^n u[n] - \left(\frac23\right)^n u[n]$.
> - $\frac23<|z|<\frac43$ (stable): $x[n] = -2\left(\frac43\right)^n u[-n-1] - \left(\frac23\right)^n u[n]$.
> - $|z|<\frac23$: $x[n] = -2\left(\frac43\right)^n u[-n-1] + \left(\frac23\right)^n u[-n-1]$.
> - $\frac43$ right-sided with $\frac23$ left-sided: empty ROC, no z-transform.

> [!trap]
> - Left-sided term: $-A\,p^n u[-n-1]$, both the minus and the $-n-1$.
> - Side chosen per pole, from the ROC.
> - Delay shifts the exponent: $\frac{z^{-1}}{1-az^{-1}} \to a^{n-1}u[n-1]$.
> - Causal check: $h[0] = H(\infty)$.

**Where it appears:** [[2-z-transform/08-inverse-z-transform|L8]]–[[2-z-transform/11-bibo-stability-and-causality|L11]]; [[problems/all-possible-rocs]], [[problems/two-sided-systems-as-recursions]]; [[homework/hw3|HW3]] #3, [[homework/hw4|HW4]].

## Related
[[concepts/partial-fraction-expansion]] · [[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/sided-sequences]] · [[concepts/z-transform]]

### Sources for this page
Lecture 8 notes §1–2 and slides (Examples 1–3); HW3 #3 solutions; FA2019 #6, FA2025 #7 keys.
