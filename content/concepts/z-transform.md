---
title: "z-transform"
description: "X(z) = Σ x[n] z⁻ⁿ with its region of convergence: turns convolution into multiplication and LCCDEs into algebra; its poles decide causality and stability."
tags: [concept, z-transform, roc]
aliases: ["z transform", "X(z)", "the z-transform"]
---

*Lecture 6 (Fri Sep 4) §2 · [[homework/hw3|HW3]] #1 · family: [[problems/z-transform-with-roc|z-transform with ROC]]*

> [!abstract] In one breath
> - $X(z) = \sum_n x[n]z^{-n}$ converges only on its ROC; the ROC is part of the answer.
> - $u[n]$ and $-u[-n-1]$ share $\frac{1}{1-z^{-1}}$; only the ROC tells them apart.
> - $z^n$ into an LTI system gives $H(z)z^n$, so convolution becomes $Y(z)=H(z)X(z)$.

## 1. Definition

> [!key] Definition (Lecture 6, eqs. 10–11)
> $$
> X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n},\qquad x[n]\ \overset{\mathcal{Z}}{\longleftrightarrow}\ X(z),\qquad z\in\mathbb{C}.
> $$
> - **ROC**: the $z$ where the sum converges ([[concepts/region-of-convergence|region of convergence]]). Always state it; **the ROC is part of the transform.**
> - **Pole**: $X(z)\to\infty$. **Zero**: $X(z)=0$ ([[concepts/poles-and-zeros|poles and zeros]]).

- **Why:** $z^n$ into an LTI system gives $H(z)\,z^n$ ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]); convolution becomes $Y(z)=H(z)X(z)$.
- **ROC is a ring:** only $\lvert z\rvert$ affects convergence.
- **Unit circle:** $X(e^{j\omega})=X_d(\omega)$ when the ROC contains $\lvert z\rvert=1$; $2^nu[n]$ has a z-transform but no DTFT.
- Course form: powers of $z^{-1}$, "ROC: $\lvert z\rvert>a$". Geometric series: $\sum_{n\ge0} b^n = \frac{1}{1-b}$ iff $\lvert b\rvert<1$ ([[0-toolkit/02-geometric-series|toolkit]]).

## 2. The first transforms

> [!question] Exercise 1 (Lecture 6; slide 8): $X(z)$ and ROC of $u[n]$ and of $-u[-(n+1)]$.

> [!success]- Answer (eqs. 12–20)
> $$
> \sum_{n=0}^{\infty}z^{-n}=\frac{1}{1-z^{-1}},\qquad \lvert z^{-1}\rvert<1\iff \text{ROC: } \lvert z\rvert>1;\ \text{pole at } z = 1 .
> $$
> With $m=-n-1$:
> $$
> \begin{aligned}
> X(z)&=-\sum_{n=-\infty}^{-1}z^{-n}=-\sum_{m=0}^{\infty}z^{m+1}=-z\sum_{m=0}^{\infty}z^{m}\\
> &=\frac{-z}{1-z}\cdot\frac{-z^{-1}}{-z^{-1}}=\frac{1}{1-z^{-1}},\qquad \text{ROC: } \lvert z\rvert<1 .
> \end{aligned}
> $$

> [!key] Unique only with the ROC
> $$
> u[n]\ \longleftrightarrow\ \frac{1}{1-z^{-1}},\ \lvert z\rvert>1 \qquad\qquad -u[-n-1]\ \longleftrightarrow\ \frac{1}{1-z^{-1}},\ \lvert z\rvert<1
> $$

> [!question] Exercise 2 (Lecture 6; slide 9 with $a\in\mathbb{C}$): $x[n] = a^n u[n]$.

> [!success]- Answer (eqs. 21–22)
> $$
> X(z)=\sum_{n=0}^{\infty}\left(\frac{a}{z}\right)^n=\frac{1}{1-az^{-1}},\qquad \left\lvert\frac{a}{z}\right\rvert<1\iff \text{ROC: } \lvert z\rvert>\lvert a\rvert .
> $$
> $\frac{1}{1-az^{-1}} = \frac{z}{z-a}$: pole at $z = a$, zero at $z = 0$.

Finite length (Lecture 8 slides, Example 1a): $\{\underset{\uparrow}{1},\ -\tfrac14,\ \tfrac{1}{16}\}\leftrightarrow 1 - \tfrac14 z^{-1} + \tfrac{1}{16}z^{-2}$, ROC $z\neq0$.

## 3. Pole-zero plots and the ROC shapes

**Pole-zero plot**: zeros ○, poles ×, ROC shaded, unit circle dashed. Lecture 6, Fig. 1:

| signal | $X(z)$ | poles | zeros | ROC |
|---|---|---|---|---|
| $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $1$ | $0$ | $\lvert z\rvert>1$ |
| $(-\tfrac13)^n u[n]$ | $\dfrac{1}{1+\frac13 z^{-1}}$ | $-\tfrac13$ | $0$ | $\lvert z\rvert>\tfrac13$ |
| $\cos(\tfrac{2\pi}{3}n)\,u[n]$ | $\dfrac{1+\frac12 z^{-1}}{1+z^{-1}+z^{-2}}$ | $e^{\pm j2\pi/3}$ | $0,\ -\tfrac12$ | $\lvert z\rvert>1$ |

Cosine: $X(z)=\dfrac{z(z+\frac12)}{z^2+z+1}$; poles on the unit circle. The full table of pairs (Lecture 6, Table 1) is on [[concepts/z-transform-pairs|z-transform pairs]].

ROC shapes (right-sided: outside a circle; left-sided: inside; two-sided: a ring; finite: whole plane except maybe $0$, $\infty$) are Lecture 7's rules: [[concepts/region-of-convergence|region of convergence]].

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 256" width="640" height="256" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M9.0,50.0 h196.0 v176.0 h-196.0 Z M119.0,138.0 A12.0,12.0 0 1,0 95.0,138.0 A12.0,12.0 0 1,0 119.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="107.0" cy="138.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="9.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="9.0" y1="138.0" x2="205.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="107.0" y1="50.0" x2="107.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="107.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="201.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="112.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="126.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="107.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M114.0,133.0 L124.0,143.0 M114.0,143.0 L124.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="119.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><text x="107.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(a) right-sided</text><text x="107.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">(½)ⁿ u[n]</text><text x="107.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > ½</text><circle cx="320.0" cy="138.0" r="72.0" fill="var(--accent)" fill-opacity="0.20" stroke="var(--accent)" stroke-width="1.6"/><rect x="222.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="222.0" y1="138.0" x2="418.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="320.0" y1="50.0" x2="320.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="320.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="414.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="325.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="339.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="320.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M387.0,133.0 L397.0,143.0 M387.0,143.0 L397.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="392.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">3</text><text x="320.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(b) left-sided</text><text x="320.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−3ⁿ u[−n−1]</text><text x="320.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| < 3</text><path d="M605.0,138.0 A72.0,72.0 0 1,0 461.0,138.0 A72.0,72.0 0 1,0 605.0,138.0 Z M545.0,138.0 A12.0,12.0 0 1,0 521.0,138.0 A12.0,12.0 0 1,0 545.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="533.0" cy="138.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="533.0" cy="138.0" r="72.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="435.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="435.0" y1="138.0" x2="631.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="533.0" y1="50.0" x2="533.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="533.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="627.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="538.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="552.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="533.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M540.0,133.0 L550.0,143.0 M540.0,143.0 L550.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="545.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><path d="M600.0,133.0 L610.0,143.0 M600.0,143.0 L610.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="605.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">3</text><text x="533.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(c) two-sided</text><text x="533.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">(½)ⁿ u[n] + 3ⁿ u[−n−1]</text><text x="533.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: ½ < |z| < 3</text></svg><figcaption><strong>ROC shape follows the signal's extent: (a) right-sided, outside the outermost pole; (b) left-sided, inside the innermost pole; (c) two-sided, the ring where both parts converge.</strong> Poles ×, zeros ○, dashed |z| = 1, ROC shaded; an ROC never contains a pole.</figcaption></figure>

> [!recipe] Find $X(z)$ and its ROC
> 1. Split $x[n]$ into [[concepts/z-transform-pairs|table rows]] (Euler; $a^n u[n-k] = a^k\,a^{n-k}u[n-k]$; right + left parts).
> 2. Transform each with its ROC, using [[concepts/z-transform-properties|properties]].
> 3. Add; ROC = intersection (empty ⇒ no transform).
> 4. State the ROC, including $z=0$, $z=\infty$.

## 4. Linear algebra intuition (Lecture 6 §2.1, optional)

- Dot product $v^H u = \sum_n u_n v_n^*$ measures alignment (eqs. 23–25); $v^Hu=0$ iff $u\perp v$.
- $X(z)$ is the dot product of $x[n]$ with the exponential $z^{-n}$: large $\lvert X(z)\rvert$ means $x$ resembles that exponential; near $0$, nearly orthogonal.

> [!trap]
> - No ROC, incomplete answer (rubrics deduct even a missing $\lvert\cdot\rvert$); a missing $z\neq0$ too.
> - $z^{-n}$, not $z^n$: a sample at $n=-3$ multiplies $z^{3}$.
> - Left-sided entry has a minus: $a^n u[-n-1]$ (no minus) $\leftrightarrow -\frac{1}{1-az^{-1}}$, $\lvert z\rvert<\lvert a\rvert$.
> - Zeros at $z = 0$ hide in the $z^{-1}$ form: rewrite in positive powers before listing.
> - A finite pulse has no pole at $z=1$: $\sum_{k=0}^{7}z^{-k}=\frac{1-z^{-8}}{1-z^{-1}}$ is $8$ at $z=1$; ROC $z\neq0$.
> - Everlasting $e^{j\omega_0 n}$ or $1$: empty ROC, no z-transform ([[exams/midterm-1/past-exams/spring-2025|SP2025 #1c]]); $z_0^{\,n}u[n]$ is not an eigenfunction.

> [!exam] "z-transform **and ROC**": 6 of 7 exams, 9–15 points
> Points lost on a missing ROC, a missing $z\neq0$, the left-sided sign, unintersected ROCs. Same $X(z)$, different ROC returns in every all-possible-ROCs problem.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #5]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(c), #5]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #5]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]] · recipes: [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/all-possible-rocs|all possible ROCs]]

**Where it appears:** [[2-z-transform/06-the-z-transform|L6]] §2 (eqs. 10–22, Fig. 1, Table 1, §2.1), [[2-z-transform/07-z-transform-properties|L7]]–[[2-z-transform/11-bibo-stability-and-causality|L11]], [[3-fourier-analysis/14-dtft-properties|L14]]; [[problems/z-transform-with-roc|z-transform with ROC]] (6/7 exams); [[homework/hw3|HW3]] #1, [[homework/hw4|HW4]]; [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]].

## Related
[[concepts/region-of-convergence]] · [[concepts/z-transform-pairs]] · [[concepts/z-transform-properties]] · [[concepts/inverse-z-transform]] · [[concepts/poles-and-zeros]] · [[concepts/transfer-function]] · [[concepts/eigenfunctions-of-lti-systems]] · [[concepts/sided-sequences]] · [[demos/pole-zero-and-roc-explorer]]

### Sources for this page
Lecture 6 notes §2 (eqs. 10–25, Exercises 1–2, Fig. 1, Table 1, §2.1) and slides 8–9; Lecture 7 §1; Lecture 8 slides Example 1(a); Lecture 14 §1; HW3 rubric; past exams above.
