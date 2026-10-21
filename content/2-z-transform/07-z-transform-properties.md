---
title: "Lecture 7 — Properties of the z-transform"
description: "X(z) is undefined outside its ROC; the ROC rules (no poles, connected, sided shapes); the properties table with ROCs: shift, linearity, convolution (at least the intersection), differentiation, scaling, reversal, conjugation."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 7
---

*Lecture 7 · Wed Sep 9, 2026 · notes + slides "z-transform properties" · prev: [[2-z-transform/06-the-z-transform|Lecture 6]] · next: [[2-z-transform/08-inverse-z-transform|Lecture 8]]*

> [!abstract] In one breath
> - The ROC is part of $X(z)$: outside it the transform is undefined, even where the formula returns a number.
> - ROC: no poles, connected; right-sided → outside the largest pole, left-sided → inside the smallest.
> - Properties (shift, convolution, $n\,x[n]$, $a^nx[n]$, $x[-n]$) build every transform from a few pairs; track the ROC at each step.

## 1. Overview of the z-transform

$X(z)=\sum_n x[n]z^{-n}$ exists only where the sum converges (the ROC). Example:

$$
x[n]=\left(\tfrac12\right)^nu[n]\ \longleftrightarrow\ X(z)=\frac{1}{1-\frac12z^{-1}},\quad |z|>\tfrac12 .
$$

At $z=\tfrac14$ the formula gives $\dfrac{1}{1-\frac12\cdot4}=-1$, but the sum is $\sum_{n\ge0}(\tfrac12)^n(\tfrac14)^{-n}=\sum_{n\ge0}2^n$: divergent, consistent with $z=\tfrac14$ outside the ROC.

> [!key] ROC rules
> 1. Zeros: $X(z)=0$. Poles: $X(z)\to\infty$.
> 2. The ROC contains **no poles**.
> 3. The ROC is **connected**.
> 4. Infinite-length: **right-sided** ($x[n]=0$ for $n<n_0$) $\Rightarrow |z|>a$; **left-sided** ($x[n]=0$ for $n>n_0$) $\Rightarrow |z|<a$; **two-sided** $\Rightarrow a<|z|<b$.
> 5. Finite-length: whole plane, except perhaps $z=0$ (causal) or $z=\infty$ (non-causal). $\delta[n]+\delta[n-1]\leftrightarrow1+z^{-1}$, $|z|>0$; $\delta[n+1]+\delta[n]\leftrightarrow z+1$, $|z|<\infty$; their sum: $0<|z|<\infty$.
>
> Rational $X(z)$: right-sided starting at $n\ge0$ → $|z|>|p_{\max}|$; left-sided ending at $n\le-1$ → $|z|<|p_{\min}|$. (Typed slide 7 writes "left-sided: $x[n]=0,\ n<n_0$"; read $n>n_0$ — [[0-toolkit/05-errata|errata]].)

> [!question] Example 1 (slides): ROC of $X(z)=\dfrac{1+3z^{-1}}{1+\frac74z^{-1}-\frac12z^{-2}}$ if $x[n]$ is right-sided? Left-sided?

> [!success]- Answer
> Roots of $z^2+\tfrac74z-\tfrac12$:
> $$
> z=\frac{-\frac74\pm\sqrt{\frac{49}{16}+\frac{32}{16}}}{2}=\frac{-\frac74\pm\frac94}{2}=\tfrac14,\ -2 .
> $$
> $X(z)=\dfrac{z(z+3)}{\left(z-\frac14\right)(z+2)}$; zeros $0$, $-3$ play no role.
> - Right-sided: $|z|>2$. Left-sided: $|z|<\tfrac14$. (Two-sided $\tfrac14<|z|<2$: [[2-z-transform/08-inverse-z-transform|Lecture 8]].)

## 2. Key properties of the z-transform

> [!key] Useful z-transform properties (Table 1 of the notes)
> | property | signal | z-transform | ROC |
> |---|---|---|---|
> | time shift | $x[n-k]$ | $z^{-k}X(z)$ | $R_x$ except possibly $z=0$ or $z=\infty$ |
> | linearity | $a\,x_1[n]+b\,x_2[n]$ | $a\,X_1(z)+b\,X_2(z)$ | at least $R_{x_1}\cap R_{x_2}$ |
> | convolution | $x_1[n]*x_2[n]$ | $X_1(z)\,X_2(z)$ | at least $R_{x_1}\cap R_{x_2}$ |
> | differentiation | $n\,x[n]$ | $-z\,\dfrac{dX(z)}{dz}$ | $R_x$ |
> | conjugation | $x^*[n]$ | $X^*(z^*)$ | $R_x$ |
> | time reversal | $x[-n]$ | $X(z^{-1})$ | $1/R_x$ |
> | scaling | $a^n\,x[n]$ | $X(z/a)$ | $\lvert a\rvert R_x$ |
> | real part | $\mathrm{Re}\{x[n]\}$ | $\tfrac12[X(z)+X^*(z^*)]$ | at least $R_x$ |
> | imaginary part | $\mathrm{Im}\{x[n]\}$ | $\tfrac{1}{2j}[X(z)-X^*(z^*)]$ | at least $R_x$ |
>
> (The notes print $\tfrac12[X(z)-X^*(z^*)]$ for the imaginary part; $\mathrm{Im}\{x\}=\frac{x-x^*}{2j}$ gives $\tfrac{1}{2j}$.)

### Time shifting

With $y[n]=x[n-k]$, substitute $n=m+k$:

$$
Y(z)=\sum_{n=-\infty}^{\infty}x[n-k]z^{-n}=\sum_{m=-\infty}^{\infty}x[m]z^{-(m+k)}=z^{-k}\sum_{m=-\infty}^{\infty}x[m]z^{-m}=z^{-k}X(z).
$$

Delay ($k>0$) adds $z^{-k}$ (blows up at $z=0$); advance ($k<0$) adds $z^{|k|}$ (blows up at $z=\infty$). Slides, with $u[n]\leftrightarrow\frac{1}{1-z^{-1}}$, $|z|>1$:

- $u[n-3]\leftrightarrow\dfrac{z^{-3}}{1-z^{-1}}$, $|z|>1$ ($z=0$ already excluded).
- $u[n+2]\leftrightarrow\dfrac{z^{2}}{1-z^{-1}}$, $1<|z|<\infty$.

> [!trap] Match the exponent to the step before shifting
> - $a^nu[n-k]$ is not $a^nu[n]$ delayed: $a^nu[n-k]=a^k\cdot a^{n-k}u[n-k]\ \longleftrightarrow\ \dfrac{a^kz^{-k}}{1-az^{-1}}$, $|z|>|a|$.
> - $2^nu[n-1]\leftrightarrow\dfrac{2z^{-1}}{1-2z^{-1}}$ but $2^{n-1}u[n-1]\leftrightarrow\dfrac{z^{-1}}{1-2z^{-1}}$ (both $|z|>2$).
> - An advance excludes $z=\infty$: state "$|z|<\infty$".

> [!question] Lecture exercise: prove the time-shift property from the convolution property

> [!success]- Answer
> $x[n-k]=x[n]*\delta[n-k]$, so $X(z)\cdot\mathcal{Z}\{\delta[n-k]\}=X(z)\,z^{-k}$; ROC at least $R_x\cap\{z\ne0\}$ ($k>0$) or $R_x\cap\{z\ne\infty\}$ ($k<0$).

### Linearity and convolution

- ROC $\supseteq R_{x_1}\cap R_{x_2}$: one divergent sum makes the whole diverge (slides: $|z|>1$ and $|z|>3$ give $|z|>3$).
- "At least": a zero of one transform can cancel a pole of the other; the ROC then **grows**. Usually it is just the intersection.

> [!derivation]- Convolution becomes multiplication (notes)
> With $y[n]=x_1[n]*x_2[n]$, split $z^{-n}=z^{-k}z^{-(n-k)}$ and substitute $n=m+k$:
> $$
> \begin{aligned}
> Y(z)&=\sum_{n}\Big(\sum_{k}x_1[k]\,x_2[n-k]\Big)z^{-n}\\
> &=\sum_{n}\sum_{k}x_1[k]z^{-k}\,x_2[n-k]z^{-(n-k)}\\
> &=\sum_{m}\sum_{k}x_1[k]z^{-k}\,x_2[m]z^{-m}\\
> &=\Big(\sum_{k}x_1[k]z^{-k}\Big)\Big(\sum_{m}x_2[m]z^{-m}\Big)=X_1(z)X_2(z).
> \end{aligned}
> $$
> With $x_2=h$: $Y(z)=H(z)X(z)$ ([[2-z-transform/09-transfer-functions|Lecture 9]]).

> [!question] Example 2 (slides): $x_1[n]=(\tfrac12)^nu[n]-c\,(\tfrac12)^{n-1}u[n-1]$, $x_2[n]=(-1)^nu[n]$, $y=x_1*x_2$, $c\in\mathbb{R}$. $Y(z)$ and ROC for (a) $c=1$, (b) $c=-1$

> [!success]- Answer
> Second term of $x_1$ = first term delayed by one, scaled by $c$:
> $$
> \begin{aligned}
> X_1(z)&=\frac{1}{1-\frac12z^{-1}}-\frac{c\,z^{-1}}{1-\frac12z^{-1}}=\frac{1-cz^{-1}}{1-\frac12z^{-1}},\ |z|>\tfrac12;\qquad \\
> X_2(z)&=\frac{1}{1+z^{-1}},\ |z|>1;
> \end{aligned}
> $$
> $$
> Y(z)=X_1(z)X_2(z)=\frac{1-cz^{-1}}{\left(1-\frac12z^{-1}\right)\left(1+z^{-1}\right)} .
> $$
> - (a) $c=1$: $Y(z)=\dfrac{1-z^{-1}}{\left(1-\frac12z^{-1}\right)\left(1+z^{-1}\right)}$, $|z|>1$ (the intersection).
> - (b) $c=-1$: zero at $-1$ cancels the pole at $-1$: $Y(z)=\dfrac{1}{1-\frac12z^{-1}}$, $|z|>\tfrac12$, **larger** than $R_{x_1}\cap R_{x_2}$; $y[n]=(\tfrac12)^nu[n]$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M25.0,50.0 h280.0 v176.0 h-280.0 Z M227.0,138.0 A62.0,62.0 0 1,0 103.0,138.0 A62.0,62.0 0 1,0 227.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="165.0" cy="138.0" r="62.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="25.0" y="50.0" width="280.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="25.0" y1="138.0" x2="305.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="165.0" y1="50.0" x2="165.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="165.0" cy="138.0" r="62.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="301.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="170.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="211.6" y="90.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="165.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="227.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M191.0,133.0 L201.0,143.0 M191.0,143.0 L201.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="196.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><path d="M98.0,133.0 L108.0,143.0 M98.0,143.0 L108.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="103.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">−1</text><text x="165.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">c = 1</text><text x="165.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">Y = (1 − z⁻¹) / ((1 − ½z⁻¹)(1 + z⁻¹))</text><text x="165.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > 1</text><path d="M335.0,50.0 h280.0 v176.0 h-280.0 Z M506.0,138.0 A31.0,31.0 0 1,0 444.0,138.0 A31.0,31.0 0 1,0 506.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="475.0" cy="138.0" r="31.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="335.0" y="50.0" width="280.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="335.0" y1="138.0" x2="615.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="475.0" y1="50.0" x2="475.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="475.0" cy="138.0" r="62.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="611.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="480.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="521.6" y="90.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="475.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M501.0,133.0 L511.0,143.0 M501.0,143.0 L511.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="506.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><text x="475.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">c = −1</text><text x="475.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">Y = (1 + z⁻¹) / ((1 − ½z⁻¹)(1 + z⁻¹)) = 1 / (1 − ½z⁻¹)</text><text x="475.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > ½  (bigger than R₁ ∩ R₂)</text><g opacity="0.45"><circle cx="413.0" cy="138.0" r="7" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M408.0,133.0 L418.0,143.0 M408.0,143.0 L418.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/></g><text x="413.0" y="160.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">cancelled</text></svg><figcaption><strong>Example 2: a cancelled pole takes its boundary with it.</strong> For c = 1 the ROC is the intersection |z| &gt; 1; for c = −1 the zero of X₁ cancels the pole of X₂ at −1 and the ROC grows to |z| &gt; ½.</figcaption></figure>

### Differentiation

$n\,x[n]\leftrightarrow-z\,\frac{dX(z)}{dz}$, ROC $R_x$; gives the $n\,a^n$ rows and double poles. With $\frac{d}{dz}(1-az^{-1})=az^{-2}$:

$$
n\,a^nu[n]\ \longleftrightarrow\ -z\cdot\Big(-(1-az^{-1})^{-2}\,a z^{-2}\Big)=\frac{az^{-1}}{\left(1-az^{-1}\right)^2},\qquad |z|>|a| .
$$

> [!question] Example 3 (slides): $y[n]=2^n\,n\,x[n]$ with $x[n]=(\tfrac13)^nu[n]$; find $Y(z)$ and ROC

> [!success]- Answer
> $X(z)=\dfrac{1}{1-\frac13z^{-1}}$, $|z|>\tfrac13$.
> - **Differentiate, then scale.** $V(z)=-z\dfrac{d}{dz}\dfrac{1}{1-\frac13z^{-1}}=\dfrac{\frac13z^{-1}}{\left(1-\frac13z^{-1}\right)^2}$; $Y(z)=V(z/2)=\dfrac{\frac13\left(\frac z2\right)^{-1}}{\left(1-\frac13\left(\frac z2\right)^{-1}\right)^2}$.
> - **Scale, then differentiate.** $G(z)=X(z/2)=\dfrac{1}{1-\frac23z^{-1}}$; $Y(z)=-z\,G'(z)$.
>
> Both:
> $$
> Y(z)=\frac{\frac23z^{-1}}{\left(1-\frac23z^{-1}\right)^2},\qquad |z|>\tfrac23 ,
> $$
> the pair $n\,a^nu[n]$ with $a=\tfrac23$.

### Scaling

$\sum_n a^nx[n]z^{-n}=\sum_n x[n]\left(\frac{z}{a}\right)^{-n}=X(z/a)$: pole $p\to a\,p$, ROC $|z|>r\to|z|>|a|\,r$. With Euler, cosines:

$$
\cos(\omega_0n)\,x[n]=\tfrac12e^{j\omega_0n}x[n]+\tfrac12e^{-j\omega_0n}x[n]\ \longleftrightarrow\ \tfrac12X\!\left(e^{-j\omega_0}z\right)+\tfrac12X\!\left(e^{j\omega_0}z\right).
$$

### Conjugation

$x^*[n]\leftrightarrow X^*(z^*)$, ROC $R_x$. Real signal: $X(z)=X^*(z^*)$, so poles and zeros come in **conjugate pairs** (used in [[2-z-transform/08-inverse-z-transform|Lecture 8]]).

### Time reversal

$x[-n]\leftrightarrow X(z^{-1})$, ROC $1/R_x$ ($|z|>r$ becomes $|z|<1/r$). E.g. $(\tfrac12)^{-n}u[-n]=2^nu[-n]\leftrightarrow\dfrac{1}{1-\frac12z}=\dfrac{-2z^{-1}}{1-2z^{-1}}$, $|z|<2$.

> [!question] Lecture exercise: prove the time-reversal property

> [!success]- Answer
> $m=-n$: $\sum_n x[-n]z^{-n}=\sum_m x[m]\left(z^{-1}\right)^{-m}=X(z^{-1})$, converging when $z^{-1}\in R_x$, i.e. $z\in1/R_x$.

> [!recipe] z-transform of a signal with properties
> 1. **Base pair**: $a^nu[n]$, $u[n]$, $\delta[n]$, a cosine.
> 2. **Rewrite** as a chain: shift, multiply by $n$, multiply by $a^n$, reverse. Match exponents to shifted steps first.
> 3. **Apply** one property at a time; **update the ROC each step** (shift: maybe drop $0$/$\infty$; scaling: radii × $|a|$; reversal: invert).
> 4. **Combine** by linearity; intersect ROCs; state "$z\ne0$" or "$|z|<\infty$" if a shift introduced them.

> [!exam] z-transform with ROC — 6 of 7 past exams, 9–15 points
> Shift with advances, $(n+1)x[n]$, Euler + scaling; ROC True/False. The convolution property drives every LCCDE and pole-cancellation problem. Family: [[problems/z-transform-with-roc|z-transform with ROC]].
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #5a, #5c]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1c, #5a]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #5a]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1b, #5]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]] · [[homework/hw3|HW3 #1–2]]

## Related

[[concepts/z-transform-properties|z-transform properties]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/convolution|convolution]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/sided-sequences|sided sequences]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[supplements/transform-tables|transform tables]]

### Sources for this page

Snyder, Lecture 7 notes (§1 ROC rules, §2 properties, derivations, exercises, Table 1) and slides (Examples 1–3, shift and intersection examples); past exams above.
