---
title: "Lecture 6 — The z-transform and the region of convergence"
description: "zⁿ as eigenfunction of LTI systems with eigenvalue H(z); the z-transform sum and its ROC; u[n] vs −u[−n−1]: same X(z), different ROC; aⁿu[n]; pole-zero plots; the table of pairs."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 6
---

*Lecture 6 · Fri Sep 4, 2026 · notes + slides "z-transform" · prev: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] · next: [[2-z-transform/07-z-transform-properties|Lecture 7]]*

> [!abstract] In one breath
> - $z_0^{\,n}$ (all $n$) through any LTI system → $H(z_0)\,z_0^{\,n}$, $H(z) = \sum_k h[k]z^{-k}$.
> - z-transform $X(z) = \sum_n x[n]z^{-n}$; it converges only on the ROC.
> - $u[n]$ and $-u[-n-1]$ share $\frac{1}{1-z^{-1}}$; only the ROC tells them apart.

## 1. Motivation for the z-transform

- Convolution gives any output; LCCDEs give $h[n]$. Neither says *what a system does* (slide 3: $h[n] = (\tfrac12)^n u[n]$).
- Wanted: inputs whose **shape** no LTI system changes, only scales: $y[n] = x[n] * h[n] = A(x[n])\,x[n]$ (eqs. 1–2).
- Needs $x[n-k]$ to split into an $n$-part and a $k$-part: $z^{n-k} = z^n z^{-k}$. Slide example: $z_0 = 1 + j2$.

Eqs. 5–7:
$$
y[n] = \sum_{k=-\infty}^{\infty}h[k]\,z^{\,n-k} = \Bigl(\sum_{k=-\infty}^{\infty}h[k]\,z^{-k}\Bigr)z^{\,n} = H(z)\,z^{\,n}, \qquad \forall n.
$$

> [!key] Complex exponentials are eigenfunctions of LTI systems
> $$
> z_0^{\,n}\ \longrightarrow\ \boxed{\text{LTI } h[n]}\ \longrightarrow\ H(z_0)\,z_0^{\,n},\qquad H(z_0)=\sum_{k=-\infty}^{\infty}h[k]\,z_0^{-k}
> $$
> - $H(z_0)$ depends on $h$ and $z_0$ only, not on $n$: the eigenvalue. $H(z)$ is the **transfer function** (z-transform of $h$).
> - Holds only for inputs defined for **all** $n$, and only if the sum converges.

Sums of exponentials (eqs. 8–9):
$$
x[n]=\sum_{k=1}^{K}b_k\,z_k^{\,n}\quad\Longrightarrow\quad y[n]=\sum_{k=1}^{K}H(z_k)\,b_k\,z_k^{\,n}.
$$
Slide 6: $\lvert H(z_k)\rvert > 1$ amplifies, $0 < \lvert H(z_k)\rvert < 1$ attenuates, $H(z_k) = 0$ removes the $z_k$ component (filtering).

## 2. The z-transform

> [!key] Definition (eqs. 10–11)
> $$
> X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n},\qquad x[n]\ \overset{\mathcal{Z}}{\longleftrightarrow}\ X(z),\qquad z\in\mathbb{C}.
> $$
> - **ROC**: the $z$ where the sum converges. Always state it.
> - **Pole**: $X(z)\to\infty$. **Zero**: $X(z)=0$.

Course form: powers of $z^{-1}$, "ROC: $|z|>a$". Geometric series: $\sum_{n\ge0} b^n = \frac{1}{1-b}$ iff $|b|<1$ ([[0-toolkit/02-geometric-series|toolkit]]).

> [!question] Exercise 1 (notes; slide 8): $X(z)$ and ROC of $u[n]$ and of $-u[-(n+1)]$.

> [!success]- Answer
> $$
> \sum_{n=0}^{\infty}z^{-n}=\frac{1}{1-z^{-1}},\qquad |z^{-1}|<1\iff \text{ROC: } |z|>1;\ \text{pole at } z = 1 .
> $$
> With $m=-n-1$ (eqs. 15–20):
> $$
> \begin{aligned}
> X(z)&=-\sum_{n=-\infty}^{-1}z^{-n}=-\sum_{m=0}^{\infty}z^{m+1}=-z\sum_{m=0}^{\infty}z^{m}\\
> &=\frac{-z}{1-z}\cdot\frac{-z^{-1}}{-z^{-1}}=\frac{1}{1-z^{-1}},\qquad \text{ROC: } |z|<1 .
> \end{aligned}
> $$

> [!key] Unique only with the ROC
> $$
> u[n]\ \longleftrightarrow\ \frac{1}{1-z^{-1}},\ |z|>1 \qquad\qquad -u[-n-1]\ \longleftrightarrow\ \frac{1}{1-z^{-1}},\ |z|<1
> $$

> [!question] Exercise 2 (notes; slide 9 with $a\in\mathbb{C}$): $x[n] = a^n u[n]$.

> [!success]- Answer
> $$
> X(z)=\sum_{n=0}^{\infty}\left(\frac{a}{z}\right)^n=\frac{1}{1-az^{-1}},\qquad \left|\frac{a}{z}\right|<1\iff \text{ROC: } |z|>|a| .
> $$
> $\frac{1}{1-az^{-1}} = \frac{z}{z-a}$: pole at $z = a$, zero at $z = 0$.

**Pole-zero plot**: zeros ○, poles ×, ROC shaded, unit circle dashed. Notes Fig. 1:

| signal | $X(z)$ | poles | zeros | ROC |
|---|---|---|---|---|
| $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $1$ | $0$ | $\lvert z\rvert>1$ |
| $(-\tfrac13)^n u[n]$ | $\dfrac{1}{1+\frac13 z^{-1}}$ | $-\tfrac13$ | $0$ | $\lvert z\rvert>\tfrac13$ |
| $\cos(\tfrac{2\pi}{3}n)\,u[n]$ | $\dfrac{1+\frac12 z^{-1}}{1+z^{-1}+z^{-2}}$ | $e^{\pm j2\pi/3}$ | $0,\ -\tfrac12$ | $\lvert z\rvert>1$ |

Cosine: $X(z)=\dfrac{z(z+\frac12)}{z^2+z+1}$; poles on the unit circle.

> [!key] Common z-transform pairs (Table 1)
> | $x[n]$ | $X(z)$ | ROC |
> |---|---|---|
> | $\delta[n]$ | $1$ | all $z$ |
> | $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
> | $a^n u[n]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ |
> | $-a^n u[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert<\lvert a\rvert$ |
> | $n\,a^n u[n]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert>\lvert a\rvert$ |
> | $-n\,a^n u[-n-1]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert<\lvert a\rvert$ |
> | $\cos(\omega_0 n)\,u[n]$ | $\dfrac{1-\cos(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ |
> | $\sin(\omega_0 n)\,u[n]$ | $\dfrac{\sin(\omega_0)z^{-1}}{1-2\cos(\omega_0)z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ |
> | $a^n\cos(\omega_0 n)\,u[n]$ | $\dfrac{1-a\cos(\omega_0)z^{-1}}{1-2a\cos(\omega_0)z^{-1}+a^2z^{-2}}$ | $\lvert z\rvert>\lvert a\rvert$ |
> | $a^n\sin(\omega_0 n)\,u[n]$ | $\dfrac{a\sin(\omega_0)z^{-1}}{1-2a\cos(\omega_0)z^{-1}+a^2z^{-2}}$ | $\lvert z\rvert>\lvert a\rvert$ |
>
> $n\,a^n$ rows: differentiation property; cosine/sine rows: Euler + $a^n u[n]$ ([[2-z-transform/07-z-transform-properties|Lecture 7]]).

ROC shapes (right-sided: outside a circle; left-sided: inside; two-sided: a ring; finite: whole plane except maybe $0$, $\infty$) are Lecture 7's rules: [[2-z-transform/07-z-transform-properties|Lecture 7]].

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 256" width="640" height="256" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M9.0,50.0 h196.0 v176.0 h-196.0 Z M119.0,138.0 A12.0,12.0 0 1,0 95.0,138.0 A12.0,12.0 0 1,0 119.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="107.0" cy="138.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="9.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="9.0" y1="138.0" x2="205.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="107.0" y1="50.0" x2="107.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="107.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="201.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="112.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="126.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="107.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M114.0,133.0 L124.0,143.0 M114.0,143.0 L124.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="119.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><text x="107.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(a) right-sided</text><text x="107.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">(½)ⁿ u[n]</text><text x="107.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > ½</text><circle cx="320.0" cy="138.0" r="72.0" fill="var(--accent)" fill-opacity="0.20" stroke="var(--accent)" stroke-width="1.6"/><rect x="222.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="222.0" y1="138.0" x2="418.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="320.0" y1="50.0" x2="320.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="320.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="414.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="325.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="339.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="320.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M387.0,133.0 L397.0,143.0 M387.0,143.0 L397.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="392.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">3</text><text x="320.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(b) left-sided</text><text x="320.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−3ⁿ u[−n−1]</text><text x="320.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| < 3</text><path d="M605.0,138.0 A72.0,72.0 0 1,0 461.0,138.0 A72.0,72.0 0 1,0 605.0,138.0 Z M545.0,138.0 A12.0,12.0 0 1,0 521.0,138.0 A12.0,12.0 0 1,0 545.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="533.0" cy="138.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="533.0" cy="138.0" r="72.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="435.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="435.0" y1="138.0" x2="631.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="533.0" y1="50.0" x2="533.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="533.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="627.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="538.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="552.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="533.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M540.0,133.0 L550.0,143.0 M540.0,143.0 L550.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="545.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><path d="M600.0,133.0 L610.0,143.0 M600.0,143.0 L610.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="605.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">3</text><text x="533.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(c) two-sided</text><text x="533.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">(½)ⁿ u[n] + 3ⁿ u[−n−1]</text><text x="533.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: ½ < |z| < 3</text></svg><figcaption><strong>ROC shape follows the signal's extent: (a) right-sided, outside the outermost pole; (b) left-sided, inside the innermost pole; (c) two-sided, the ring where both parts converge.</strong> Poles ×, zeros ○, dashed |z| = 1, ROC shaded; an ROC never contains a pole.</figcaption></figure>

### 2.1 Linear algebra intuition (optional)

- Dot product $v^H u = \sum_n u_n v_n^*$ measures alignment (eqs. 23–25).
- $X(z)$ is the dot product of $x[n]$ with the exponential $z^{-n}$: large $\lvert X(z)\rvert$ means $x$ resembles that exponential; near $0$, nearly orthogonal.

> [!trap] z-transform traps
> - Left-sided entry: $a^n u[-n-1]$ (no minus) $\leftrightarrow -\frac{1}{1-az^{-1}}$, $|z|<|a|$.
> - Zeros at $z = 0$ hide in the $z^{-1}$ form: rewrite in positive powers before listing.
> - A finite pulse has no pole at $z=1$: $\sum_{k=0}^{7}z^{-k}=\frac{1-z^{-8}}{1-z^{-1}}$ is $8$ at $z=1$; ROC $z\neq0$.
> - $z_0^{\,n}u[n]$ is not an eigenfunction: switching on at $n=0$ adds a transient.
> - Everlasting $e^{j\omega_0 n}$ or $1$: empty ROC, no z-transform.

> [!exam] How Lecture 6 is tested
> "z-transform **and ROC**": 6 of 7 exams, 9–15 points. Points lost on a missing ROC, a missing $z\neq0$, the left-sided sign, unintersected ROCs. Same $X(z)$, different ROC returns in every all-possible-ROCs problem.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #5]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1(c), #5]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #5]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]] · recipes: [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/all-possible-rocs|all possible ROCs]]

## Related

[[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|ROC]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions]] · [[concepts/transfer-function|transfer function]] · [[demos/pole-zero-and-roc-explorer|ROC explorer]] · [[homework/hw3|HW3]] · unit: [[2-z-transform/index|Unit 2]]

### Sources for this page

Snyder, Lecture 6 notes (§1, §2 with Exercises 1–2, Fig. 1, Table 1, §2.1) and annotated slides (Sep 4, 2026); Lecture 7 notes §1 (ROC rules); past exams above.
