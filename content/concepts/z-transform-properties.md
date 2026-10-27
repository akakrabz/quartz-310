---
title: "z-transform properties"
description: "Shift, linearity, convolution, differentiation, conjugation, time reversal, scaling, Re/Im: what each does to X(z) and the ROC, with the Lecture 7 derivations and examples and HW3 #2 worked."
tags: [concept, z-transform, roc]
aliases: ["z-transform properties", "properties of the z-transform", "time-shift property", "convolution property", "differentiation property"]
---

*Lecture 7 (Wed Sep 9) §2 · [[homework/hw3|HW3]] #1–#2 · family: [[problems/z-transform-with-roc|z-transform with ROC]]*

> [!abstract] In one breath
> - Shift multiplies by $z^{-k}$, convolution multiplies transforms, $n\,x[n]$ differentiates, $a^nx[n]$ rescales $z$, $x[-n]$ inverts $z$.
> - Every property comes with an ROC rule; track it at each step.
> - Linearity and convolution give **at least** the intersection: a zero can cancel a pole and the ROC grows.

## 1. The table

> [!key] Useful z-transform properties (Lecture 7, Table 1; $x[n] \leftrightarrow X(z)$, ROC $R_x$)
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
> The notes print $\tfrac12[X(z)-X^*(z^*)]$ for the imaginary part; $\mathrm{Im}\{x\}=\frac{x-x^*}{2j}$ gives $\tfrac{1}{2j}$ ([[0-toolkit/05-errata|errata]]).

## 2. Time shifting (eqs. 6–11)

With $y[n]=x[n-k]$, substitute $n=m+k$:

$$
Y(z)=\sum_{n=-\infty}^{\infty}x[n-k]z^{-n}=\sum_{m=-\infty}^{\infty}x[m]z^{-(m+k)}=z^{-k}\sum_{m=-\infty}^{\infty}x[m]z^{-m}=z^{-k}X(z).
$$

Delay ($k>0$) adds $z^{-k}$ (blows up at $z=0$); advance ($k<0$) adds $z^{\lvert k\rvert}$ (blows up at $z=\infty$). Slides, with $u[n]\leftrightarrow\frac{1}{1-z^{-1}}$, $\lvert z\rvert>1$:

- $u[n-3]\leftrightarrow\dfrac{z^{-3}}{1-z^{-1}}$, $\lvert z\rvert>1$ ($z=0$ already excluded).
- $u[n+2]\leftrightarrow\dfrac{z^{2}}{1-z^{-1}}$, $1<\lvert z\rvert<\infty$.

> [!question] Lecture exercise: prove the time-shift property from the convolution property

> [!success]- Answer
> $x[n-k]=x[n]*\delta[n-k]$, so $X(z)\cdot\mathcal{Z}\{\delta[n-k]\}=X(z)\,z^{-k}$; ROC at least $R_x\cap\{z\ne0\}$ ($k>0$) or $R_x\cap\{z\ne\infty\}$ ($k<0$).

## 3. Linearity and convolution (eqs. 12–19)

- ROC $\supseteq R_{x_1}\cap R_{x_2}$: one divergent sum makes the whole diverge (slides: $\lvert z\rvert>1$ and $\lvert z\rvert>3$ give $\lvert z\rvert>3$).
- "At least": a zero of one transform can cancel a pole of the other; the ROC then **grows** ([[concepts/pole-zero-cancellation|pole-zero cancellation]]). Usually it is just the intersection.

> [!derivation]- Convolution becomes multiplication (Lecture 7, eqs. 14–19)
> With $y[n]=x_1[n]*x_2[n]$, split $z^{-n}=z^{-k}z^{-(n-k)}$ and substitute $n=m+k$:
> $$
> \begin{aligned}
> Y(z)&=\sum_{n}\Big(\sum_{k}x_1[k]\,x_2[n-k]\Big)z^{-n}\\
> &=\sum_{n}\sum_{k}x_1[k]z^{-k}\,x_2[n-k]z^{-(n-k)}\\
> &=\sum_{m}\sum_{k}x_1[k]z^{-k}\,x_2[m]z^{-m}\\
> &=\Big(\sum_{k}x_1[k]z^{-k}\Big)\Big(\sum_{m}x_2[m]z^{-m}\Big)=X_1(z)X_2(z).
> \end{aligned}
> $$
> With $x_2=h$: $Y(z)=H(z)X(z)$ ([[concepts/transfer-function|transfer function]]).

> [!question] Example 2 (slides): $x_1[n]=(\tfrac12)^nu[n]-c\,(\tfrac12)^{n-1}u[n-1]$, $x_2[n]=(-1)^nu[n]$, $y=x_1*x_2$, $c\in\mathbb{R}$. $Y(z)$ and ROC for (a) $c=1$, (b) $c=-1$

> [!success]- Answer
> Second term of $x_1$ = first term delayed by one, scaled by $c$:
> $$
> \begin{aligned}
> X_1(z)&=\frac{1}{1-\frac12z^{-1}}-\frac{c\,z^{-1}}{1-\frac12z^{-1}}=\frac{1-cz^{-1}}{1-\frac12z^{-1}},\ \lvert z\rvert>\tfrac12;\qquad \\
> X_2(z)&=\frac{1}{1+z^{-1}},\ \lvert z\rvert>1;
> \end{aligned}
> $$
> $$
> Y(z)=X_1(z)X_2(z)=\frac{1-cz^{-1}}{\left(1-\frac12z^{-1}\right)\left(1+z^{-1}\right)} .
> $$
> - (a) $c=1$: $Y(z)=\dfrac{1-z^{-1}}{\left(1-\frac12z^{-1}\right)\left(1+z^{-1}\right)}$, $\lvert z\rvert>1$ (the intersection).
> - (b) $c=-1$: zero at $-1$ cancels the pole at $-1$: $Y(z)=\dfrac{1}{1-\frac12z^{-1}}$, $\lvert z\rvert>\tfrac12$, **larger** than $R_{x_1}\cap R_{x_2}$; $y[n]=(\tfrac12)^nu[n]$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M25.0,50.0 h280.0 v176.0 h-280.0 Z M227.0,138.0 A62.0,62.0 0 1,0 103.0,138.0 A62.0,62.0 0 1,0 227.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="165.0" cy="138.0" r="62.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="25.0" y="50.0" width="280.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="25.0" y1="138.0" x2="305.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="165.0" y1="50.0" x2="165.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="165.0" cy="138.0" r="62.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="301.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="170.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="211.6" y="90.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="165.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="227.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M191.0,133.0 L201.0,143.0 M191.0,143.0 L201.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="196.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><path d="M98.0,133.0 L108.0,143.0 M98.0,143.0 L108.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="103.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">−1</text><text x="165.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">c = 1</text><text x="165.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">Y = (1 − z⁻¹) / ((1 − ½z⁻¹)(1 + z⁻¹))</text><text x="165.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > 1</text><path d="M335.0,50.0 h280.0 v176.0 h-280.0 Z M506.0,138.0 A31.0,31.0 0 1,0 444.0,138.0 A31.0,31.0 0 1,0 506.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="475.0" cy="138.0" r="31.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="335.0" y="50.0" width="280.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="335.0" y1="138.0" x2="615.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="475.0" y1="50.0" x2="475.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="475.0" cy="138.0" r="62.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="611.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="480.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="521.6" y="90.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="475.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M501.0,133.0 L511.0,143.0 M501.0,143.0 L511.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="506.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><text x="475.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">c = −1</text><text x="475.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">Y = (1 + z⁻¹) / ((1 − ½z⁻¹)(1 + z⁻¹)) = 1 / (1 − ½z⁻¹)</text><text x="475.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > ½  (bigger than R₁ ∩ R₂)</text><g opacity="0.45"><circle cx="413.0" cy="138.0" r="7" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M408.0,133.0 L418.0,143.0 M408.0,143.0 L418.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/></g><text x="413.0" y="160.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">cancelled</text></svg><figcaption><strong>Example 2: a cancelled pole takes its boundary with it.</strong> For c = 1 the ROC is the intersection |z| &gt; 1; for c = −1 the zero of X₁ cancels the pole of X₂ at −1 and the ROC grows to |z| &gt; ½.</figcaption></figure>

## 4. Differentiation (eq. 20)

$n\,x[n]\leftrightarrow-z\,\frac{dX(z)}{dz}$, ROC $R_x$; gives the $n\,a^n$ rows of the [[concepts/z-transform-pairs|table]] and double poles. With $\frac{d}{dz}(1-az^{-1})=az^{-2}$:

$$
n\,a^nu[n]\ \longleftrightarrow\ -z\cdot\Big(-(1-az^{-1})^{-2}\,a z^{-2}\Big)=\frac{az^{-1}}{\left(1-az^{-1}\right)^2},\qquad \lvert z\rvert>\lvert a\rvert .
$$

> [!question] Example 3 (slides): $y[n]=2^n\,n\,x[n]$ with $x[n]=(\tfrac13)^nu[n]$; find $Y(z)$ and ROC

> [!success]- Answer
> $X(z)=\dfrac{1}{1-\frac13z^{-1}}$, $\lvert z\rvert>\tfrac13$.
> - **Differentiate, then scale.** $V(z)=-z\dfrac{d}{dz}\dfrac{1}{1-\frac13z^{-1}}=\dfrac{\frac13z^{-1}}{\left(1-\frac13z^{-1}\right)^2}$; $Y(z)=V(z/2)=\dfrac{\frac13\left(\frac z2\right)^{-1}}{\left(1-\frac13\left(\frac z2\right)^{-1}\right)^2}$.
> - **Scale, then differentiate.** $G(z)=X(z/2)=\dfrac{1}{1-\frac23z^{-1}}$; $Y(z)=-z\,G'(z)$.
>
> Both:
> $$
> Y(z)=\frac{\frac23z^{-1}}{\left(1-\frac23z^{-1}\right)^2},\qquad \lvert z\rvert>\tfrac23 ,
> $$
> the pair $n\,a^nu[n]$ with $a=\tfrac23$.

## 5. Scaling, conjugation, time reversal (eqs. 21–22)

**Scaling.** $\sum_n a^nx[n]z^{-n}=\sum_n x[n]\left(\frac{z}{a}\right)^{-n}=X(z/a)$: pole $p\to a\,p$, ROC $\lvert z\rvert>r\to\lvert z\rvert>\lvert a\rvert\,r$. With Euler, cosines:

$$
\cos(\omega_0n)\,x[n]=\tfrac12e^{j\omega_0n}x[n]+\tfrac12e^{-j\omega_0n}x[n]\ \longleftrightarrow\ \tfrac12X\!\left(e^{-j\omega_0}z\right)+\tfrac12X\!\left(e^{j\omega_0}z\right).
$$

**Conjugation.** $x^*[n]\leftrightarrow X^*(z^*)$, ROC $R_x$. Real signal: $X(z)=X^*(z^*)$, so poles and zeros come in **conjugate pairs** (used by [[concepts/partial-fraction-expansion|PFE]] with complex poles).

**Time reversal.** $x[-n]\leftrightarrow X(z^{-1})$, ROC $1/R_x$ ($\lvert z\rvert>r$ becomes $\lvert z\rvert<1/r$). E.g. $(\tfrac12)^{-n}u[-n]=2^nu[-n]\leftrightarrow\dfrac{1}{1-\frac12z}=\dfrac{-2z^{-1}}{1-2z^{-1}}$, $\lvert z\rvert<2$.

> [!question] Lecture exercise: prove the time-reversal property

> [!success]- Answer
> $m=-n$: $\sum_n x[-n]z^{-n}=\sum_m x[m]\left(z^{-1}\right)^{-m}=X(z^{-1})$, converging when $z^{-1}\in R_x$, i.e. $z\in1/R_x$.

## 6. Using the properties

> [!recipe] z-transform of a signal with properties
> 1. **Base pair**: $a^nu[n]$, $u[n]$, $\delta[n]$, a cosine.
> 2. **Rewrite** as a chain: shift, multiply by $n$, multiply by $a^n$, reverse. Match exponents to shifted steps first.
> 3. **Apply** one property at a time; **update the ROC each step** (shift: maybe drop $0$/$\infty$; scaling: radii × $\lvert a\rvert$; reversal: invert).
> 4. **Combine** by linearity; intersect ROCs; state "$z\ne0$" or "$\lvert z\rvert<\infty$" if a shift introduced them.

> [!question] HW3 #2: $X(z) = \frac{1}{1-\frac13 z^{-1}}$, $\lvert z\rvert>\frac13$. Transform (a) $x[n+3]$, (b) $2^n x[n]$, (c) $\cos(\frac{\pi}{4}n)x[n]$, (d) $n(n-2)x[n-1]$, (e) $\left(\frac15\right)^nu[n]*x[n]$; also $x[-n]$.

> [!success]- Answers
> - (a) $\dfrac{z^3}{1-\frac13 z^{-1}}$, $\ \frac13<\lvert z\rvert<\infty$.
> - (b) $\dfrac{1}{1-\frac23 z^{-1}}$, $\lvert z\rvert>\frac23$.
> - (c) $\dfrac{1-\frac13\cos(\frac{\pi}{4})z^{-1}}{1-\frac23\cos(\frac{\pi}{4})z^{-1}+\frac19 z^{-2}}$, $\lvert z\rvert>\frac13$.
> - (d) $G(z)=z^{-1}X(z)=\frac{1}{z-\frac13}$; $n(n-2)g[n]\leftrightarrow 3zG'(z) + z^2G''(z)$:
> $$
> \frac{z-z^2}{(z-\frac13)^3} = \frac{z^{-2}-z^{-1}}{\left(1-\frac13 z^{-1}\right)^3}, \qquad \lvert z\rvert>\tfrac13 .
> $$
> - (e) $\dfrac{1}{(1-\frac15 z^{-1})(1-\frac13 z^{-1})}$, $\lvert z\rvert>\frac13$.
> - $x[-n]=3^nu[-n]\leftrightarrow\dfrac{1}{1-\frac13 z}$, $\lvert z\rvert<3$.

> [!trap] Match the exponent to the step before shifting
> - $a^nu[n-k]$ is not $a^nu[n]$ delayed: $a^nu[n-k]=a^k\cdot a^{n-k}u[n-k]\ \longleftrightarrow\ \dfrac{a^kz^{-k}}{1-az^{-1}}$, $\lvert z\rvert>\lvert a\rvert$.
> - $2^nu[n-1]\leftrightarrow\dfrac{2z^{-1}}{1-2z^{-1}}$ but $2^{n-1}u[n-1]\leftrightarrow\dfrac{z^{-1}}{1-2z^{-1}}$ (both $\lvert z\rvert>2$).
> - An advance excludes $z=\infty$: state "$\lvert z\rvert<\infty$"; a shift changes the ROC only at $0$ and $\infty$.
> - Scaling moves poles $p\to ap$; $e^{j\omega_0 n}x[n]$ rotates the pole-zero plot. Time reversal inverts the ROC: $\lvert z\rvert>\frac13$ becomes $\lvert z\rvert<3$.
> - Differentiation is $-z\,\frac{d}{dz}$ in $z$, not $z^{-1}$; product rule when applied twice.

> [!exam] z-transform with ROC — 6 of 7 past exams, 9–15 points
> Shift with advances, $(n+1)x[n]$, Euler + scaling; ROC True/False. The convolution property drives every LCCDE and pole-cancellation problem.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #5a, #5c]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #1c, #5a]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #5a]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #1b, #5]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]] · family: [[problems/z-transform-with-roc|z-transform with ROC]]

**Where it appears:** [[2-z-transform/07-z-transform-properties|L7]] §2 (eqs. 6–22, Table 1, Examples 2–3), [[2-z-transform/09-transfer-functions|L9]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra|L10]]; [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/infinite-length-convolution|Infinite-length convolution]]; [[homework/hw3|HW3]] #1–#2; [[supplements/transform-tables|transform tables]].

## Related
[[concepts/z-transform]] · [[concepts/z-transform-pairs]] · [[concepts/region-of-convergence]] · [[concepts/convolution]] · [[concepts/pole-zero-cancellation]] · [[concepts/sided-sequences]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]]

### Sources for this page
Lecture 7 notes §2 (eqs. 6–22, Table 1, derivations, exercises) and slides (Examples 2–3, shift and intersection examples); HW3 #2 solution; SP2021 #4 key; transform tables Table 9; past exams above.
