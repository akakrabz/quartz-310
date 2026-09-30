---
title: "Pole-zero cancellation"
description: "When the same factor (1 − p z⁻¹) sits in a numerator and a denominator, the pole at p disappears: its mode leaves the signal, the ROC can grow, and an unstable system or input can produce a bounded output."
tags: [concept, z-transform, roc, stability]
aliases: ["pole-zero cancellation", "cancellation"]
---

> [!key] The rule
> If a zero and a pole sit at the **same** location $p$, the common factor $(1-pz^{-1})$ cancels: $p$ is not a pole of the result, the term $p^n$ never appears in the time signal, and the ROC is decided by the poles that **remain**. That is why the properties only promise
> $$
> \text{ROC}\{X_1X_2\} \supseteq R_1\cap R_2, \qquad \text{ROC}\{aX_1+bX_2\} \supseteq R_1\cap R_2
> $$
> ("at least the intersection"): a cancelled boundary pole lets the ROC expand to the next pole.

## Where cancellations happen

1. **Inside one $H(z)$.** An LCCDE can hide a common factor. HW4 #6: $H(z) = \frac{1+\frac12 z^{-1}}{1+z^{-1}+\frac14 z^{-2}} = \frac{1+\frac12 z^{-1}}{(1+\frac12 z^{-1})^2} = \frac{1}{1+\frac12 z^{-1}}$, so $h[n] = \left(-\frac12\right)^n u[n]$. Parameter problems exploit this: in SP2025 #7 the zeros $\pm\alpha$ cancel the unstable pole at $-2$ only when $\alpha^2 = 4$, which is the only way that causal system is stable ([[problems/parameters-for-stability]]).
2. **Series connections** $H_1(z)H_2(z)$ ([[concepts/system-algebra|system algebra]]): a zero of one block removes a pole of the other.
3. **Input against system**, $Y(z) = H(z)X(z)$: an input with a zero at an unstable system pole gives a bounded output (Lecture 11: $h = 3^nu[n]$ with $x = \delta[n]-3\delta[n-1]$ gives $y=\delta[n]$); a system zero can also remove an input pole (FA2023 #7b: $x=u[n]$ into an $H$ with a zero at $1$).
4. **Sums** $X_1+X_2$ (parallel connections, linearity): $u[n] + (\delta[n]-u[n]) = \delta[n]$, so two unstable systems in parallel can be stable (FA2025 T/F (f), False); poles of $X_1$, $X_2$ need not be poles of $X_1+X_2$ (SP2021 T/F (b), False).

> [!example] FA2025 #6: an input that cancels a system pole
> $y[n] = \frac43 y[n-1] + \frac43 y[n-2] + x[n] - x[n-2]$ gives
> $H(z) = \dfrac{1-z^{-2}}{(1-2z^{-1})(1+\frac23 z^{-1})}$, causal, ROC $|z|>2$ (poles $2$, $-\frac23$; zeros $\pm1$).
> The input $x[n] = 3\delta[n]+2\delta[n-1]$ has $X(z) = 3+2z^{-1} = 3\left(1+\frac23 z^{-1}\right)$ — a zero exactly at the pole $-\frac23$:
> $$
> Y(z) = \frac{3\left(1-z^{-2}\right)}{1-2z^{-1}}
> \quad\Longrightarrow\quad
> y[n] = 3(2)^n u[n] - 3(2)^{n-2}u[n-2].
> $$
> No $(-\frac23)^n$ term survives. (Checked with `lfilter`.)

> [!example] HW4 #5: a cascade whose ROC grows
> $h_1[n] = 2u[n]-2\left(\frac12\right)^nu[n] \leftrightarrow \dfrac{z^{-1}}{(1-z^{-1})(1-\frac12 z^{-1})}$, $|z|>1$ — unstable (pole on the unit circle).
> $h_2[n] = \delta[n]-3\left(\frac14\right)^nu[n-1] \leftrightarrow \dfrac{1-z^{-1}}{1-\frac14 z^{-1}}$, $|z|>\frac14$ — stable.
> $$
> H_1(z)H_2(z) = \frac{z^{-1}}{(1-\frac12 z^{-1})(1-\frac14 z^{-1})},\quad |z|>\tfrac12
> \quad\Longrightarrow\quad h[n] = 4\left(\tfrac12\right)^n u[n] - 4\left(\tfrac14\right)^n u[n].
> $$
> The ROC is $|z|>\frac12$, strictly larger than $R_1\cap R_2 = \{|z|>1\}$, and it contains the unit circle: **the cascade is stable** although $h_1$ is not.

> [!recipe] Using cancellation on an exam
> 1. Write every factor as $(1-pz^{-1})$ — numerator and denominator, system and input.
> 2. Cancel identical factors **before** the PFE (a cancelled pole would just get $A_k = 0$).
> 3. Recompute the ROC from the surviving poles, keeping what the problem fixed (a causal system stays causal: outside the largest surviving pole).
> 4. Judge boundedness/stability from the survivors: unbounded iff a survivor lies outside the unit circle, or a double survivor lies on it ([[concepts/marginal-stability|marginal stability]]).

> [!trap]
> - **Only exact matches cancel.** FA2025 #8a: $H = \frac{1-\frac34 z^{-1}}{1+3z^{-1}}$, $|z|>3$. The input $\delta[n]-\frac34\delta[n-1]$ has its zero at $\frac34$, not at $-3$ → output unbounded; $\delta[n]+3\delta[n-1]$ cancels $-3$ → bounded.
> - In SP2025 #7, $\alpha = \pm j2$ gives $\alpha^2=-4$: zeros at $\pm 2j$, nothing cancels, unstable. Only $\alpha = \pm2$ works.
> - After a cancellation the ROC may **grow** — SP2021 #7: $X$ has ROC $\frac13<|z|<4$, but $Y = HX$ loses the pole at $4$, so $\text{ROC}_Y = |z|>1$.
> - "Cascade of two unstable systems cannot be stable" (SP2021 T/F (c)) and "if $h_1$ or $h_2$ is unstable, $h_1*h_2$ is unstable" (FA2019 T/F (d)) are both **False**, by cancellation.
> - The reverse direction does hold: a pole of the step response $G(z) = \frac{H(z)}{1-z^{-1}}$ at $\frac12$ must be a pole of $H(z)$, because dividing by $(1-z^{-1})$ only touches $z=1$ (FA2019 T/F (h), True).
> - FA2019 #10(d): cascading a stable $H$ that has a zero at $2$ with $2^nu[n]$ cancels the pole at $2$ — the result is **still stable**, so "(d) unstable" is False.

**Where it appears.**
- Lectures: [[2-z-transform/07-z-transform-properties|L7]] (ROC "at least" the intersection; slide Example 2 with $c=-1$, where $Y = \frac{1}{1-\frac12 z^{-1}}$ and the ROC grows to $|z|>\frac12$), [[2-z-transform/09-transfer-functions|L9]] §1.2, [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]] (series connections), [[2-z-transform/11-bibo-stability-and-causality|L11]] §1.2 (inputs that cancel an unstable pole).
- Problem families: [[problems/unbounded-outputs-and-pole-matching]], [[problems/parameters-for-stability]], [[problems/lccde-to-transfer-function-and-response]].
- Homework: [[homework/hw4|HW4]] #5 (cascade), #6 (hidden common factor).
- Past exams: [[0-midterm-1/past-exams/fall-2025|FA2025]] #6, #8a, T/F (f); [[0-midterm-1/past-exams/spring-2025|SP2025]] #7, #8 ($x = \delta[n]+\frac32\delta[n-1]$ cancels $-\frac32$); [[0-midterm-1/past-exams/fall-2024|FA2024]] #7(c)–(d) (input zero at 2, output $2n(\frac12)^nu[n]$), #8b; [[0-midterm-1/past-exams/fall-2023|FA2023]] #7b, #8; [[0-midterm-1/past-exams/spring-2023|SP2023]] #5b, #7; [[0-midterm-1/past-exams/spring-2021|SP2021]] #7, T/F (b), (c); [[0-midterm-1/past-exams/fall-2019|FA2019]] #10d, T/F (d), (h).

Related: [[concepts/poles-and-zeros]] · [[concepts/region-of-convergence]] · [[concepts/system-algebra]] · [[concepts/marginal-stability]] · [[concepts/bibo-stability]] · [[concepts/transfer-function]]

### Sources for this page
Lecture 7 notes §2 (linearity/convolution ROC "at least") and slide Example 2; Lecture 9 notes §1.2; Lecture 11 notes §1.2 and slide 13; HW4 #5–#6 solutions; exam keys FA2025 #6/#8, SP2025 #7/#8, FA2024 #7, FA2023 #7, SP2023 #5/#7, SP2021 #7, FA2019 #10. Verification: `verify/concepts/verify_systems.py`, `verify_stability.py`, `verify_zdomain_extra.py` (HW4 #5 ROC growth checked by summing $h[n]z^{-n}$ at $|z| = 0.7$).
