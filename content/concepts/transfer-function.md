---
title: "Transfer function H(z)"
description: "H(z) = Z{h[n]} = Y(z)/X(z): read it straight off an LCCDE, factor it for poles and zeros, attach the ROC that causality or stability demands, and invert it (or multiply by X(z)) to get h[n] and y[n]."
tags: [concept, z-transform, lccde, systems, stability]
aliases: ["system function", "H(z)"]
---

> [!key] Definition and the LCCDE form (Lecture 9)
> For an [[concepts/lti-system|LTI system]] with [[concepts/impulse-response|impulse response]] $h[n]$, the transfer function is $H(z) = \mathcal{Z}\{h[n]\}$, and by the convolution property
> $$
> Y(z) = H(z)\,X(z), \quad \text{ROC} \supseteq R_x\cap R_h, \qquad H(z) = \frac{Y(z)}{X(z)} .
> $$
> For the [[concepts/lccde|LCCDE]] $\;y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k]$ (zero initial conditions):
> $$
> H(z) = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{1+\sum_{k=1}^{N} a_k z^{-k}} .
> $$
> Numerator ← input taps, denominator ← feedback taps (with the signs of this standard form). This matches `scipy.signal.lfilter(b, a, x)` with `a[0] = 1`.

**What $H(z)$ tells you at a glance.**
- **Poles and zeros** ([[concepts/poles-and-zeros|poles and zeros]]): roots of the denominator and numerator; $N$ poles, so $N$ is the system's order. A pole and zero at the same place cancel ([[concepts/pole-zero-cancellation|cancellation]]).
- **FIR or IIR** ([[concepts/fir-and-iir|FIR and IIR]]): any finite, nonzero pole left after cancellation ⇒ IIR; a denominator that is a single term (poles only at $z=0$ or $\infty$) ⇒ FIR.
- **Causality and stability** from the ROC ([[concepts/region-of-convergence|ROC]], Lecture 11): causal ⇔ $|z|>|p_{\max}|$ including $\infty$; stable ⇔ ROC contains $|z|=1$; causal **and** stable ⇔ all poles inside the unit circle.
- **Response to exponentials**: an everlasting $x[n] = z_0^n$ with $z_0$ in the ROC comes out as $H(z_0)\,z_0^n$ ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]).

> [!recipe] LCCDE → $H(z)$ → $h[n]$ → $y[n]$
> 1. Move every $y$ term to the left: $y[n] + \sum a_k y[n-k] = \dots$ (watch the signs).
> 2. Transform term by term with the shift property ($y[n-k] \to z^{-k}Y(z)$) and solve for $Y/X$.
> 3. Factor; list poles and zeros; cancel common factors.
> 4. Attach the ROC the problem specifies (causal → outside the largest pole; stable → the ring containing $|z|=1$).
> 5. [[concepts/partial-fraction-expansion|PFE]] (long division first if improper) and invert → $h[n]$.
> 6. For an output: $Y = HX$, cancel, PFE, invert with $\text{ROC}_Y \supseteq R_x\cap R_h$.

> [!example] Lecture 9 slides, Exercise 3: $y[n] = \tfrac12 y[n-1] + \tfrac{3}{16}y[n-2] + x[n] - 3x[n-1]$, causal
> Standard form: $y[n] - \frac12 y[n-1] - \frac{3}{16}y[n-2] = x[n]-3x[n-1]$, so
> $$
> H(z) = \frac{1-3z^{-1}}{1-\frac12 z^{-1}-\frac{3}{16}z^{-2}} = \frac{1-3z^{-1}}{\left(1-\frac34 z^{-1}\right)\left(1+\frac14 z^{-1}\right)} .
> $$
> Poles $\frac34$, $-\frac14$; zeros $3$ (and $0$). Causal ⇒ ROC $|z|>\frac34$, which contains the unit circle: **stable**. Cover-up gives $-\frac94$ (pole $\frac34$) and $\frac{13}{4}$ (pole $-\frac14$):
> $$
> h[n] = -\tfrac94\left(\tfrac34\right)^n u[n] + \tfrac{13}{4}\left(-\tfrac14\right)^n u[n] .
> $$
> Check: $h[0] = -\frac94+\frac{13}{4} = 1 = H(\infty)$ ✓.

```python
import numpy as np
from scipy.signal import lfilter
b, a = [1, -3], [1, -1/2, -3/16]   # y[n] - 1/2 y[n-1] - 3/16 y[n-2] = x[n] - 3x[n-1]
n = np.arange(6)
h = lfilter(b, a, (n == 0).astype(float))      # delta in -> h[n] out (causal)
closed = -9/4 * (3/4)**n + 13/4 * (-1/4)**n     # from the PFE
print(np.round(h, 4), np.allclose(h, closed))
```

```text
[ 1.     -2.5    -1.0625 -1.     -0.6992 -0.5371] True
```

**Going backwards, $H(z) \to$ LCCDE.** Multiply out the denominator and read the coefficients back. SP2025 #8: $H = \frac{2-3z^{-1}}{(1-\frac12 z^{-1})(1+\frac32 z^{-1})} = \frac{2-3z^{-1}}{1+z^{-1}-\frac34 z^{-2}}$ gives $y[n] + y[n-1] - \frac34 y[n-2] = 2x[n] - 3x[n-1]$.

> [!trap]
> - **Sign bookkeeping.** In the standard form the feedback coefficients sit on the left with $+a_k$; if the problem writes $y[n] = \frac12 y[n-1] + \dots$, the denominator gets $-\frac12 z^{-1}$. Lecture 5 writes $y[n] = \sum b_i y[n-i] + \dots$ (opposite sign convention). Even exam keys slip here: SP2021 #6 ($y[n] = 2y[n-3] - x[n] + x[n-3]$ has $H = \frac{-1+z^{-3}}{1-2z^{-3}}$, $h[0]=-1$, $h[3]=-1$; the key's $h[0]=1$, $h[3]=3$ is wrong) and SP2023 #6(c) (key repeats $y[n-1]$) — see [[0-toolkit/05-errata|errata]].
> - **An LCCDE does not fix the ROC.** $y[n]-\frac12 y[n-1] = x[n]$ is satisfied by the causal $\left(\frac12\right)^nu[n]$ and by the anti-causal $-\left(\frac12\right)^nu[-n-1]$ (FA2019 T/F (a), True). Use "causal"/"stable" from the problem statement.
> - **Improper $H$** (an input delay at least as long as the longest feedback delay) produces $\delta$ terms in $h[n]$: divide first.
> - Cancel common factors before calling a system IIR or unstable (HW4 #6: $\frac{1+\frac12 z^{-1}}{(1+\frac12 z^{-1})^2}$ is first order).
> - $H(z) = Y/X$ assumes an LTI system at rest; it is also how you **find** $H$ from an input-output pair (HW4 #4, SP2023 #6a, FA2024 #6).

**In Unit 3.** For a stable system, $H(z)$ on the unit circle is the [[concepts/frequency-response|frequency response]] $H_d(\omega)=H(e^{j\omega})$ ([[3-fourier-analysis/15-frequency-response|Lecture 15]]); from an LCCDE, $H_d(\omega)=\frac{\sum_k b_ke^{-j\omega k}}{1+\sum_k a_ke^{-j\omega k}}$. Its magnitude and phase say how the system scales and shifts each sinusoid ([[concepts/magnitude-and-phase-response|magnitude and phase response]]), and $Y_d(\omega)=H_d(\omega)X_d(\omega)$ replaces $Y(z)=H(z)X(z)$ for inputs that have a DTFT. For an unstable system $H(e^{j\omega})$ is not the frequency response: the accumulator $\frac{1}{1-z^{-1}}$ (ROC $\lvert z\rvert>1$) has $H_d(\omega)=\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$ (HW6 #5).

**Where it appears.**
- Lectures: [[2-z-transform/09-transfer-functions|L9]] (definition, LCCDE form, FIR/IIR), [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]] (improper $H$, system algebra), [[2-z-transform/11-bibo-stability-and-causality|L11]] (ROC → causality and stability); [[1-signals-and-systems/05-difference-equations-and-block-diagrams|L5]] (the LCCDEs themselves).
- Problem families: [[problems/lccde-to-transfer-function-and-response]] (7/7 exams), [[problems/finding-h-from-input-output-pairs]], [[problems/unbounded-outputs-and-pole-matching]], [[problems/parameters-for-stability]].
- Homework: [[homework/hw3|HW3]] #4; [[homework/hw4|HW4]] #3, #4, #6.
- Past exams: [[exams/midterm-1/past-exams/fall-2025|FA2025 #6]], [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]], [[exams/midterm-1/past-exams/fall-2024|FA2024 #6]], [[exams/midterm-1/past-exams/fall-2023|FA2023]] #6, #7, [[exams/midterm-1/past-exams/spring-2023|SP2023]] #5, #6, [[exams/midterm-1/past-exams/spring-2021|SP2021 #6]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #10]]. Try it in the [[demos/difference-equation-simulator|difference-equation simulator]].

Related: [[concepts/lccde]] · [[concepts/poles-and-zeros]] · [[concepts/region-of-convergence]] · [[concepts/fir-and-iir]] · [[concepts/system-algebra]] · [[concepts/partial-fraction-expansion]] · [[concepts/bibo-stability]]

### Sources for this page
Lecture 9 notes §1–1.2 (Eqs. 2–7, Exercise 1, Fig. 1 FIR/IIR flow) and slides (Exercises 1–3); Lecture 10 notes §1; Lecture 11 Table 1; exam keys SP2025 #8, SP2021 #6 (corrected), SP2023 #6(c) (corrected), FA2019 T/F (a). Verification: `verify/concepts/verify_zdomain_extra.py` (L9 Exercises 2–3), `verify_systems.py` (SP2021 #6, HW4 #6); output above pasted from a real run. The *In Unit 3* paragraph: Lecture 15 §1 (Eqs. 1–2, 16); Lecture 14 Table 1; HW6 #5; checked in `verify/CLEAN_unit3.py`.
