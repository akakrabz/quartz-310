---
title: "HW3 · The z-transform, its properties, and its inverse"
description: "ECE 310 Homework 3 (due Sep 18) with folded solutions: five z-transforms with ROCs, transforms by properties, inverse transforms by inspection and partial fractions, poles, zeros, ROC and h[n] of a right-sided system."
tags: [homework, midterm-1, z-transform, roc]
---

*Homework 3 · due Fri Sep 18, 2026 (Gradescope) · Lectures 6–8, plus the transfer-function vocabulary of Lecture 9 · 100 points (30 + 30 + 24 + 16) · official solutions v1.0 · prev: [[homework/hw2|HW2]] · next: [[homework/hw4|HW4]] · [[homework/index|all homework]]*

> [!abstract] In one breath
> - $X(z)$ **and** its ROC (#1); new transforms from properties (#2).
> - Inverse by inspection and PFE; the ROC picks each term's side (#3).
> - Poles, zeros, ROC and $h[n]$ from $H(z)$ (#4). A missing ROC costs half the points.

| # | Skill | Links |
|---|---|---|
| 1 | $X(z)$ + ROC | [[problems/z-transform-with-roc\|z-transform with ROC]] · [[2-z-transform/06-the-z-transform\|L6]] |
| 2 | Shift, $a^n$, cosine, $n\,x[n]$, convolution | [[2-z-transform/07-z-transform-properties\|L7]] |
| 3 | Inverse $z$, PFE | [[problems/all-possible-rocs\|all possible ROCs]] · [[2-z-transform/08-inverse-z-transform\|L8]] |
| 4 | Poles, zeros, ROC, $h[n]$ | [[problems/lccde-to-transfer-function-and-response\|LCCDE ↔ H(z) ↔ response]] · [[2-z-transform/09-transfer-functions\|L9]] |

## Problem 1 — five z-transforms and their ROCs

> [!question] Problem 1 (30 pts)
> For each discrete-time signal, (i) determine the z-transform and (ii) state the region of convergence (ROC).
>
> (a) $x_1[n] = \delta[n+3] + 4\delta[n] - \delta[n-2]$
>
> (b) $x_2[n] = \left(\tfrac34\right)^{n+3} u[n-2]$
>
> (c) $x_3[n] = 3^n u[-n] + 2^{-n} u[n]$
>
> (d) $x_4[n] = \left(\tfrac14\right)^{\lvert n\rvert}$
>
> (e) $x_5[n] = n\left(\tfrac12\right)^n \big(u[n] - u[n-5]\big)$

> [!success]- Solution (a)
> $$
> X_1(z) = z^{3} + 4 - z^{-2}.
> $$
> $z^3$ excludes $z=\infty$, $z^{-2}$ excludes $z=0$. **ROC: $0 < \lvert z\rvert < \infty$**.

> [!success]- Solution (b)
> Match the exponent to the step:
> $$
> x_2[n] = \left(\tfrac34\right)^{5}\left(\tfrac34\right)^{n-2}u[n-2].
> $$
> $$
> X_2(z) = \left(\tfrac34\right)^{5}\frac{z^{-2}}{1-\frac34 z^{-1}} = \frac{243}{1024}\cdot\frac{z^{-2}}{1-\frac34 z^{-1}} .
> $$
> **ROC: $\lvert z\rvert > \tfrac34$**.

> [!warning] Typo in the official solution, 1(b)
> One intermediate line has $(3/4)^{3}$; it should be $(3/4)^{5}$. The final answer is right.

> [!success]- Solution (c)
> Right-sided part: $\displaystyle\sum_{n=0}^{\infty}2^{-n}z^{-n} = \frac{1}{1-\frac12 z^{-1}}$, $\lvert z\rvert > \tfrac12$.
>
> Left-sided part ($k=-n$): $\displaystyle\sum_{n=-\infty}^{0}3^{n}z^{-n} = \sum_{k=0}^{\infty}\left(\frac{z}{3}\right)^{k} = \frac{1}{1-\frac13 z}$, $\lvert z\rvert < 3$; $\dfrac{1}{1-\frac13 z} = \dfrac{-3z^{-1}}{1-3z^{-1}}$.
>
> **Answer.** $X_3(z) = \dfrac{1}{1-\frac12 z^{-1}} + \dfrac{1}{1-\frac13 z} = \dfrac{1}{1-\frac12 z^{-1}} - \dfrac{3z^{-1}}{1-3z^{-1}}$, **ROC: $\tfrac12 < \lvert z\rvert < 3$**.
>
> $3^{n}u[-n] = \delta[n] + 3^{n}u[-n-1]$ includes $n = 0$, so it is not the table's $-a^{n}u[-n-1]$.

> [!success]- Solution (d)
> $$
> x_4[n] = \left(\tfrac14\right)^{n}u[n] + 4^{n}u[-n-1] = \left(\tfrac14\right)^{n}u[n] - \Big(-4^{n}u[-n-1]\Big).
> $$
> **Answer.** $X_4(z) = \dfrac{1}{1-\frac14 z^{-1}} - \dfrac{1}{1-4z^{-1}} = \dfrac{-\frac{15}{4}z^{-1}}{\left(1-\frac14 z^{-1}\right)\left(1-4z^{-1}\right)}$, **ROC: $\tfrac14 < \lvert z\rvert < 4$**. Poles at $a$ and $1/a$.

> [!success]- Solution (e)
> $$
> x_5[n] = \{\underset{\uparrow}{0},\ \tfrac12,\ \tfrac12,\ \tfrac38,\ \tfrac14\} = \tfrac12\delta[n-1] + \tfrac12\delta[n-2] + \tfrac38\delta[n-3] + \tfrac14\delta[n-4].
> $$
> **Answer.** $X_5(z) = \tfrac12 z^{-1} + \tfrac12 z^{-2} + \tfrac38 z^{-3} + \tfrac14 z^{-4}$, **ROC: $\lvert z\rvert > 0$**.

**On the exam:** [[exams/midterm-1/past-exams/fall-2024|FA2024 #5(c)]] is 1(c) almost verbatim ($3^{-n}u[n] + 3^{n}u[-n]$, ROC $\tfrac13 < \lvert z\rvert < 3$).

## Problem 2 — properties instead of sums

> [!question] Problem 2 (30 pts)
> We are given the z-transform pair
> $$
> x[n] \overset{\mathcal{Z}}{\longleftrightarrow} X(z) = \frac{1}{1-\frac13 z^{-1}},\qquad \text{ROC: } \lvert z\rvert > \tfrac13 .
> $$
> Using properties of the z-transform, determine the z-transform of each of the following signals and state the ROC.
>
> (a) $x_1[n] = x[n+3]$
>
> (b) $x_2[n] = 2^{n}x[n]$
>
> (c) $x_3[n] = \cos\!\left(\tfrac{\pi}{4}n\right)x[n]$
>
> (d) $x_4[n] = n(n-2)\,x[n-1]$
>
> (e) $x_5[n] = \left(\tfrac15\right)^{n}u[n] * x[n]$

(Here $x[n] = \left(\tfrac13\right)^n u[n]$.)

> [!success]- Solution (a)
> $X_1(z) = \dfrac{z^{3}}{1-\frac13 z^{-1}}$, **ROC: $\tfrac13 < \lvert z\rvert < \infty$** (samples at $n<0$ exclude $z=\infty$).

> [!success]- Solution (b)
> $a^{n}x[n] \leftrightarrow X(z/a)$, ROC $\lvert a\rvert R_x$:
> $$
> X_2(z) = \frac{1}{1-\frac13\,(2z^{-1})} = \frac{1}{1-\frac23 z^{-1}} .
> $$
> **ROC: $\lvert z\rvert > \tfrac23$**.

> [!success]- Solution (c)
> $\cos\!\left(\tfrac{\pi}{4}n\right) = \tfrac12\left(e^{j\pi n/4} + e^{-j\pi n/4}\right)$:
> $$
> X_3(z) = \frac12\left[\frac{1}{1-\frac13 e^{j\pi/4}z^{-1}} + \frac{1}{1-\frac13 e^{-j\pi/4}z^{-1}}\right]
> = \frac{1-\frac{\sqrt2}{6}z^{-1}}{1-\frac{\sqrt2}{3}z^{-1}+\frac19 z^{-2}} .
> $$
> Uses $(1-az^{-1})(1-a^{*}z^{-1}) = 1-2\,\mathrm{Re}(a)\,z^{-1}+\lvert a\rvert^{2}z^{-2}$, $a = \tfrac13 e^{j\pi/4}$. **ROC: $\lvert z\rvert > \tfrac13$**; poles $\tfrac13 e^{\pm j\pi/4}$.

> [!success]- Solution (d)
> $g[n] = x[n-1]$:
> $$
> G(z) = z^{-1}X(z) = \frac{z^{-1}}{1-\frac13 z^{-1}} = \frac{1}{z-\frac13},\qquad \lvert z\rvert > \tfrac13 .
> $$
> $n\,g[n] \leftrightarrow -zG'(z)$, ${n^{2}g[n] \leftrightarrow -z\tfrac{d}{dz}\big(-zG'(z)\big)} = zG'(z) + z^{2}G''(z)$:
> $$
> X_4(z) = \underbrace{zG' + z^{2}G''}_{n^{2}g[n]} \;-\; 2\underbrace{\left(-zG'\right)}_{n\,g[n]} = 3zG'(z) + z^{2}G''(z).
> $$
> $G' = -\dfrac{1}{\left(z-\frac13\right)^{2}}$, $G'' = \dfrac{2}{\left(z-\frac13\right)^{3}}$:
> $$
> X_4(z) = -\frac{3z}{\left(z-\frac13\right)^{2}} + \frac{2z^{2}}{\left(z-\frac13\right)^{3}} = \frac{-3z\left(z-\frac13\right)+2z^{2}}{\left(z-\frac13\right)^{3}} = \frac{z-z^{2}}{\left(z-\frac13\right)^{3}} .
> $$
> **Answer.** $X_4(z) = \dfrac{z-z^{2}}{\left(z-\frac13\right)^{3}} = \dfrac{z^{-2}-z^{-1}}{\left(1-\frac13 z^{-1}\right)^{3}}$, **ROC: $\lvert z\rvert > \tfrac13$**.
>
> Check: $x_4[1] = -1$, $x_4[2] = 0$, $x_4[3] = \tfrac13$, $x_4[4] = \tfrac{8}{27}$ match the long division.

> [!success]- Solution (e)
> $X_5(z) = \dfrac{1}{\left(1-\frac15 z^{-1}\right)\left(1-\frac13 z^{-1}\right)}$, **ROC: $\lvert z\rvert > \tfrac13$**.
>
> Inverse: $x_5[n] = \left[\tfrac52\left(\tfrac13\right)^n - \tfrac32\left(\tfrac15\right)^n\right]u[n]$.

**On the exam:** [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] is 2(d) in miniature ($(n+1)x[n]$).

## Problem 3 — inverse transforms

> [!question] Problem 3 (24 pts)
> The transfer function $H(z)$ and ROC of several systems are given. Determine the corresponding impulse response $h[n]$ of each system.
>
> (a) $H_1(z) = 1 - \tfrac23 z^{-1} + \tfrac49 z^{-2} - \tfrac{8}{27}z^{-3}$, ROC: $z\neq0$
>
> (b) $H_2(z) = \dfrac{3z^{-2}}{1+2z^{-1}}$, ROC: $\lvert z\rvert > 2$
>
> (c) $H_3(z) = \dfrac{1}{1-\frac14 z^{-1}} + \dfrac{1}{1-\frac32 z^{-1}}$, ROC: $\tfrac14 < \lvert z\rvert < \tfrac32$
>
> (d) $H_4(z) = \dfrac{1}{\left(1-\frac23 z^{-1}\right)\left(1-z^{-1}\right)}$, ROC: $\lvert z\rvert > 1$

> [!success]- Solution (a)
> $h_1[n] = \delta[n] - \tfrac23\delta[n-1] + \tfrac49\delta[n-2] - \tfrac{8}{27}\delta[n-3] = \left(-\tfrac23\right)^{n}\big(u[n]-u[n-4]\big)$.

> [!success]- Solution (b)
> $(-2)^n u[n]$, scaled by 3, delayed by 2: $h_2[n] = 3(-2)^{n-2}u[n-2]$.

> [!success]- Solution (c)
> ROC outside pole $\tfrac14$ (right-sided), inside pole $\tfrac32$ (left-sided):
>
> $h_3[n] = \left(\tfrac14\right)^{n}u[n] - \left(\tfrac32\right)^{n}u[-n-1]$.

> [!success]- Solution (d)
> $$
> H_4(z) = \frac{A_1}{1-\frac23 z^{-1}} + \frac{A_2}{1-z^{-1}},
> $$
> $$
> A_1 = \left.\frac{1}{1-z^{-1}}\right|_{z^{-1}=\frac32} = \frac{1}{1-\frac32} = -2,\qquad
> A_2 = \left.\frac{1}{1-\frac23 z^{-1}}\right|_{z^{-1}=1} = \frac{1}{1-\frac23} = 3 .
> $$
> Both right-sided: $h_4[n] = \left[3 - 2\left(\tfrac23\right)^{n}\right]u[n]$. Check: $h_4[0] = 1 = H_4(\infty)$.

**On the exam:** [[exams/midterm-1/past-exams/fall-2019|FA2019 #6]] ($Y = 1 + z^{-100} + \frac{1}{1-5z^{-1}}$) is 3(a) + 3(b) by inspection.

## Problem 4 — a right-sided system

> [!question] Problem 4 (16 pts)
> Consider a right-sided LTI system with transfer function
> $$
> H(z) = \frac{1-3z^{-1}}{1+\frac16 z^{-1}-\frac13 z^{-2}} .
> $$
> (a) Determine the poles and zeros of $H(z)$. (b) Determine the ROC of $H(z)$ and sketch the pole-zero plot. (c) Determine the impulse response $h[n]$ of this system.

> [!success]- Solution (a)
> $$
> H(z) = \frac{z^{2}-3z}{z^{2}+\frac16 z-\frac13} = \frac{z\,(z-3)}{\left(z-\frac12\right)\left(z+\frac23\right)} .
> $$
> Zeros $z = 0$, $z = 3$; poles $z = \tfrac12$, $z = -\tfrac23$. (The key lists only the zero at 3; its plot shows both.)

> [!success]- Solution (b)
> **ROC: $\lvert z\rvert > \tfrac23$** (outside the outermost pole). Contains the unit circle: BIBO stable.

> [!success]- Solution (c)
> $$
> H(z) = \frac{1-3z^{-1}}{\left(1+\frac23 z^{-1}\right)\left(1-\frac12 z^{-1}\right)} = \frac{A_1}{1+\frac23 z^{-1}} + \frac{A_2}{1-\frac12 z^{-1}},
> $$
> $$
> \begin{aligned}
> A_1 &= \left.\frac{1-3z^{-1}}{1-\frac12 z^{-1}}\right|_{z^{-1}=-\frac32} = \frac{1+\frac92}{1+\frac34} = \frac{22}{7},\\
> A_2 &= \left.\frac{1-3z^{-1}}{1+\frac23 z^{-1}}\right|_{z^{-1}=2} = \frac{1-6}{1+\frac43} = -\frac{15}{7}.
> \end{aligned}
> $$
> **Answer.** $h[n] = \dfrac{22}{7}\left(-\dfrac23\right)^{n}u[n] - \dfrac{15}{7}\left(\dfrac12\right)^{n}u[n]$. Check: $h[0] = 1$, $h[1] = -\tfrac{19}{6}$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 290" width="640" height="290" role="img" aria-label="Pole-zero plot of HW3 problem 4 with the ROC shaded" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M40.0,34.0 H560.0 V266.0 H40.0 Z M202.0,150.0 A52.0,52.0 0 1 0 98.0,150.0 A52.0,52.0 0 1 0 202.0,150.0 Z" fill="var(--accent)" fill-opacity="0.16" fill-rule="evenodd" stroke="none"/><rect x="40" y="34" width="520" height="232" fill="none" stroke="currentColor" stroke-width="0.6" opacity="0.35"/><line x1="40.0" y1="150.0" x2="558.0" y2="150.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="564.0,150.0 558.0,146.7 558.0,153.3" fill="currentColor"/><line x1="150.0" y1="266.0" x2="150.0" y2="36.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><polygon points="150.0,30.0 146.7,36.0 153.3,36.0" fill="currentColor"/><text x="562.0" y="166.0" text-anchor="end" fill="currentColor" style="font-size:11px;">Re</text><text x="156.0" y="42.0" text-anchor="start" fill="currentColor" style="font-size:11px;">Im</text><circle cx="150.0" cy="150.0" r="78.0" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="5 4" opacity="0.75"/><circle cx="150.0" cy="150.0" r="52.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><line x1="228.0" y1="146.0" x2="228.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="234.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">1</text><line x1="306.0" y1="146.0" x2="306.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="306.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">2</text><line x1="384.0" y1="146.0" x2="384.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="384.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">3</text><line x1="72.0" y1="146.0" x2="72.0" y2="154.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="64.0" y="170.0" text-anchor="middle" fill="currentColor" style="font-size:11px;">−1</text><circle cx="150.0" cy="150.0" r="6.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><circle cx="384.0" cy="150.0" r="6.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><line x1="183.0" y1="144.0" x2="195.0" y2="156.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="183.0" y1="156.0" x2="195.0" y2="144.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="92.0" y1="144.0" x2="104.0" y2="156.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="92.0" y1="156.0" x2="104.0" y2="144.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="384.0" y="136.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">zero at 3</text><text x="142.0" y="170.0" text-anchor="end" fill="currentColor" style="font-size:12px;">0</text><line x1="415.0" y1="201.0" x2="425.0" y2="211.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="415.0" y1="211.0" x2="425.0" y2="201.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="434.0" y="210.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">poles: z = ½ and z = −⅔</text><circle cx="420.0" cy="230.0" r="5.0" fill="none" stroke="var(--accent)" stroke-width="2.2"/><text x="434.0" y="234.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">zeros: z = 0 and z = 3</text><text x="206.2" y="222.2" text-anchor="start" fill="currentColor" style="font-size:11px;" opacity="0.8">unit circle</text><text x="410.0" y="70.0" text-anchor="start" fill="var(--accent)" style="font-size:14px;font-weight:600;">ROC: |z| &gt; 2/3</text><text x="410.0" y="88.0" text-anchor="start" fill="currentColor" style="font-size:12px;">(right-sided: outside the</text><text x="410.0" y="104.0" text-anchor="start" fill="currentColor" style="font-size:12px;">largest pole; contains |z| = 1,</text><text x="410.0" y="120.0" text-anchor="start" fill="currentColor" style="font-size:12px;">so the system is also stable)</text></svg><figcaption><strong>Poles at ½ and −⅔ (×), zeros at 0 and 3 (○); ROC outside the largest pole.</strong> Only poles are excluded from the ROC.</figcaption></figure>

> [!trap] Traps
> - A correct $X(z)$ without its ROC earned 3 of 6 points.
> - Finite length: only $z=0$ ($n>0$ samples) and $z=\infty$ ($n<0$ samples) can be missing.
> - $e^{j\omega_0 n}x[n]$ moves the pole to angle $+\omega_0$ ([[exams/midterm-1/past-exams/fall-2025|FA2025 #5(a)]]).
> - Differentiate the transform of what $n$ multiplies ($x[n-1]$ in 2(d)).
> - Zeros may lie in the ROC ([[exams/midterm-1/past-exams/fall-2023|FA2023 #1(b)]]).

**On the exam:** poles, zeros, ROC of a causal system: [[exams/midterm-1/past-exams/fall-2023|FA2023 #7(a)]], [[exams/midterm-1/past-exams/fall-2025|FA2025 #6]].

## Related

[[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/partial-fraction-expansion|partial fraction expansion]] · [[concepts/poles-and-zeros|poles and zeros]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[homework/hw4|HW4]]

### Sources for this page

ECE 310 Fall 2026 HW3 and official solutions v1.0, including the rubric; Lecture notes 6–9 (Snyder); past Midterm 1 exams cited above.
