---
title: "Transfer function H(z)"
description: "H(z) = Z{h[n]} = Y(z)/X(z): read it off an LCCDE, factor for poles and zeros, attach the ROC causality or stability demands, invert for h[n] and y[n]."
tags: [concept, z-transform, lccde, systems, stability]
aliases: ["system function", "H(z)"]
---

> [!key] Definition and LCCDE form (Lecture 9)
> $$
> Y(z) = H(z)\,X(z), \quad \text{ROC} \supseteq R_x\cap R_h, \qquad H(z) = \frac{Y(z)}{X(z)} .
> $$
> For $y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k]$:
> $$
> H(z) = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{1+\sum_{k=1}^{N} a_k z^{-k}} .
> $$
> Same `b, a` as `scipy.signal.lfilter`.

- **Poles/zeros** give order, FIR vs IIR (after cancellation).
- **ROC:** causal ⇔ $|z|>|p_{\max}|$ incl. $\infty$; stable ⇔ contains $|z|=1$.
- **Stable:** $H_d(\omega)=H(e^{j\omega})$ ([[concepts/frequency-response|frequency response]]). Not for unstable $H$: the accumulator $\frac{1}{1-z^{-1}}$ has $H_d(\omega)=\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$ (HW6 #5).

> [!recipe] LCCDE → $H(z)$ → $h[n]$ → $y[n]$
> 1. Move every $y$ term left (watch signs). 2. Transform with $y[n-k]\to z^{-k}Y(z)$; solve for $Y/X$.
> 3. Factor; cancel common factors. 4. Attach the ROC (causal → outside largest pole; stable → ring with $|z|=1$).
> 5. Long division if improper; [[concepts/partial-fraction-expansion|PFE]]; invert. 6. Output: $Y=HX$, PFE, invert.

> [!example] Lecture 9, Exercise 3: $y[n] = \tfrac12 y[n-1] + \tfrac{3}{16}y[n-2] + x[n] - 3x[n-1]$, causal
> $$
> H(z) = \frac{1-3z^{-1}}{\left(1-\frac34 z^{-1}\right)\left(1+\frac14 z^{-1}\right)},\qquad h[n] = -\tfrac94\left(\tfrac34\right)^n u[n] + \tfrac{13}{4}\left(-\tfrac14\right)^n u[n] .
> $$
> ROC $|z|>\frac34$: stable. Check $h[0]=1=H(\infty)$.

> [!trap]
> - Sign bookkeeping: $y[n]=\frac12y[n-1]+\dots$ gives $-\frac12z^{-1}$ in the denominator. SP2021 #6 key slips ($h[0]=-1$, $h[3]=-1$ is correct); see [[0-toolkit/05-errata|errata]].
> - An LCCDE does not fix the ROC: $(\frac12)^nu[n]$ and $-(\frac12)^nu[-n-1]$ both solve $y[n]-\frac12y[n-1]=x[n]$.
> - Improper $H$ gives $\delta$ terms: divide first. Cancel before calling a system IIR or unstable (HW4 #6).

**Where it appears:** [[2-z-transform/09-transfer-functions|L9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]], [[2-z-transform/11-bibo-stability-and-causality|L11]], [[3-fourier-analysis/15-frequency-response|L15]]; [[problems/lccde-to-transfer-function-and-response]], [[problems/finding-h-from-input-output-pairs]]; [[homework/hw3|HW3]] #4, [[homework/hw4|HW4]] #3–#6; [[demos/difference-equation-simulator|difference-equation simulator]].

## Related
[[concepts/lccde]] · [[concepts/poles-and-zeros]] · [[concepts/region-of-convergence]] · [[concepts/fir-and-iir]] · [[concepts/system-algebra]] · [[concepts/bibo-stability]]

### Sources for this page
Lecture 9 notes §1–1.2 and slides (Exercises 1–3); Lecture 10 §1; Lecture 11 Table 1; Lecture 15 §1; SP2021 #6, FA2019 T/F (a) keys.
