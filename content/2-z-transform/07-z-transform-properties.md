---
title: "Lecture 7 — Properties of the z-transform"
description: "X(z) is undefined outside its ROC even where the formula gives a number; the ROC rules (no poles, connected, finite/right/left/two-sided shapes); and the properties table with its ROC rules — time shift, linearity, convolution (ROC at least the intersection, bigger after a pole-zero cancellation), differentiation, scaling, time reversal, conjugation — each with a worked example."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 7
---

*Lecture 7 · Wed Sep 9, 2026 · notes + slides "z-transform properties" · prev: [[2-z-transform/06-the-z-transform|Lecture 6]] · next: [[2-z-transform/08-inverse-z-transform|Lecture 8]]*

> [!abstract] In one breath
> Two ideas. **The ROC is part of $X(z)$**: outside it the transform is undefined even if the formula returns a number — $(\tfrac12)^nu[n]$ "gives" $X(\tfrac14)=-1$, while its sum at $z=\tfrac14$ is $\sum 2^n=\infty$. **Properties turn five table pairs into everything else**: a shift multiplies by $z^{-k}$ (and can add or remove $z=0$ or $z=\infty$), convolution multiplies transforms (ROC at least the intersection — bigger if a pole cancels), multiplying by $n$ differentiates ($-z\,\frac{d}{dz}$), multiplying by $a^n$ rescales $z\to z/a$ (ROC and poles scale by $|a|$ and $a$), and time reversal swaps $z\to z^{-1}$ (ROC inverts). Every exam z-transform is a chain of these, with the ROC tracked at each step.

## 1. A closer look at the ROC

The ROC is where $\sum_n x[n]z^{-n}$ converges, and **$X(z)$ is not defined anywhere else** — even where the closed-form expression computes a finite value. The lecture's example:

$$
x[n]=\left(\tfrac12\right)^nu[n]\ \longleftrightarrow\ X(z)=\frac{1}{1-\frac12z^{-1}},\quad |z|>\tfrac12 .
$$

At $z=\tfrac14$ the formula gives $\dfrac{1}{1-\frac12\cdot4}=-1$. The actual sum is $\sum_{n\ge0}(\tfrac12)^n(\tfrac14)^{-n}=\sum_{n\ge0}2^n$, which diverges — consistent with $z=\tfrac14$ lying outside the ROC. In Python:

```python
import numpy as np
X = lambda z: 1 / (1 - 0.5 / z)            # (1/2)^n u[n], ROC |z| > 1/2
n = np.arange(60)
N = [4, 19, 59]                            # partial sums after 5, 20 and 60 terms
for z in [1.0, 0.25]:                      # inside / outside the ROC
    partial = np.cumsum(0.5 ** n * z ** -n.astype(float))
    print(f"z = {z}: formula {X(z):+.3f}, partial sums", partial[N])
```

```text
z = 1.0: formula +2.000, partial sums [1.9375     1.99999809 2.        ]
z = 0.25: formula -1.000, partial sums [3.1000000e+01 1.0485750e+06 1.1529215e+18]
```

Inside the ROC the partial sums settle on the formula's value; outside they run away while the formula quietly prints $-1$.

> [!key] ROC rules (Lecture 7 notes, §1)
> 1. Zeros: $X(z)=0$. Poles: $X(z)\to\infty$.
> 2. The ROC contains **no poles**.
> 3. The ROC is **connected** (no two separate pieces).
> 4. Infinite-length signals: **right-sided** ($x[n]=0$ for $n<n_0$) $\Rightarrow |z|>a$; **left-sided** ($x[n]=0$ for $n>n_0$) $\Rightarrow |z|<a$; **two-sided** $\Rightarrow a<|z|<b$.
> 5. Finite-length signals: the whole plane, except perhaps $z=0$ (samples at $n>0$) or $z=\infty$ (samples at $n<0$). E.g. $\delta[n]+\delta[n-1]\leftrightarrow1+z^{-1}$, $|z|>0$; $\delta[n+1]+\delta[n]\leftrightarrow z+1$, $|z|<\infty$; their sum has $0<|z|<\infty$.
>
> Consequently, for a rational $X(z)$: a right-sided signal starting at $n\ge0$ has ROC $|z|>|p_{\max}|$ (outside its **largest** pole), and a left-sided signal ending at $n\le-1$ has ROC $|z|<|p_{\min}|$ (inside its **smallest** pole). Pictures and worked examples: [[2-z-transform/06-the-z-transform|Lecture 6 §6]]. (The typed slide 7 writes "left-sided: $x[n]=0,\ n<n_0$"; it means $n>n_0$, as the notes and the annotated slide say — [[0-toolkit/05-errata|errata]].)

> [!example] Example 1 (slides): the ROC from the poles
> $X(z)=\dfrac{1+3z^{-1}}{1+\frac74z^{-1}-\frac12z^{-2}}$. What is the ROC if $x[n]$ is right-sided? Left-sided?
>
> Poles are the roots of the denominator. Multiply it by $z^2$ and use the quadratic formula on $z^2+\tfrac74z-\tfrac12$:
> $$
> z=\frac{-\frac74\pm\sqrt{\frac{49}{16}+\frac{32}{16}}}{2}=\frac{-\frac74\pm\frac94}{2}=\tfrac14,\ -2 .
> $$
> In positive powers $X(z)=\dfrac{z(z+3)}{\left(z-\frac14\right)(z+2)}$: zeros at $0$ and $-3$, which play no role in the ROC.
> - Right-sided: $|z|>|p_{\max}|=2$.
> - Left-sided: $|z|<|p_{\min}|=\tfrac14$.
>
> (The third possibility, a two-sided signal with $\tfrac14<|z|<2$, is where [[2-z-transform/08-inverse-z-transform|Lecture 8]] picks up.)

## 2. Time shifting

> [!key] Time shift
> $$
> \begin{gathered}
> x[n-k]\ \longleftrightarrow\ z^{-k}X(z),\qquad k\in\mathbb{Z},\qquad \\
> \text{ROC}=R_x\ \text{except possibly } z=0 \text{ or } z=\infty .
> \end{gathered}
> $$

Derivation (notes): with $y[n]=x[n-k]$, substitute $n=m+k$:

$$
Y(z)=\sum_{n=-\infty}^{\infty}x[n-k]z^{-n}=\sum_{m=-\infty}^{\infty}x[m]z^{-(m+k)}=z^{-k}\sum_{m=-\infty}^{\infty}x[m]z^{-m}=z^{-k}X(z).
$$

The fine print is about the new factor: a **delay** ($k>0$) adds $z^{-k}$, which blows up at $z=0$; an **advance** ($k<0$) adds $z^{|k|}$, which blows up at $z=\infty$. The annotated slide, with $u[n]\leftrightarrow\frac{1}{1-z^{-1}}$, $|z|>1$:

- $u[n-3]\leftrightarrow\dfrac{z^{-3}}{1-z^{-1}}$, ROC $|z|>1$ — the new pole at $z=0$ is already outside the ROC.
- $u[n+2]\leftrightarrow\dfrac{z^{2}}{1-z^{-1}}$, ROC $1<|z|<\infty$ — the advance puts a pole at $z=\infty$, which must be excluded.

> [!trap] Make the exponent match the step before you shift
> $a^nu[n-k]$ is **not** $a^n u[n]$ delayed. Rewrite it as $a^k\cdot a^{n-k}u[n-k]$, which is a delayed copy scaled by $a^k$:
> $$
> a^nu[n-k]\ \longleftrightarrow\ \frac{a^kz^{-k}}{1-az^{-1}},\qquad |z|>|a| .
> $$
> Compare $2^nu[n-1]\leftrightarrow\dfrac{2z^{-1}}{1-2z^{-1}}$ with $2^{n-1}u[n-1]\leftrightarrow\dfrac{z^{-1}}{1-2z^{-1}}$ (both $|z|>2$). [[homework/hw3|HW3]] #1b: $(\tfrac34)^{n+3}u[n-2]=(\tfrac34)^5\,(\tfrac34)^{n-2}u[n-2]\leftrightarrow\dfrac{(\frac34)^5z^{-2}}{1-\frac34z^{-1}}$, $|z|>\tfrac34$.

> [!question] FA2025 #5(a): $x[n]=e^{j\frac{\pi}{3}n}\,u[n+4]$ — z-transform and ROC

> [!success]- Answer
> The step starts at $n=-4$, so rewrite the exponent to match: $e^{j\frac\pi3n}=e^{-j\frac{4\pi}{3}}\,e^{j\frac\pi3(n+4)}$. The pair $e^{j\frac\pi3n}u[n]\leftrightarrow\dfrac{1}{1-e^{j\pi/3}z^{-1}}$ ($|z|>1$) advanced by 4 samples gives
> $$
> X(z)=\frac{e^{-j4\pi/3}\,z^{4}}{1-e^{j\pi/3}z^{-1}},\qquad 1<|z|<\infty
> $$
> (the advance excludes $z=\infty$; $e^{-j4\pi/3}=e^{j2\pi/3}$). The handwritten [[exams/midterm-1/past-exams/fall-2025|FA2025]] key has a stray $n$ in the denominator — [[0-toolkit/05-errata|errata]].

> [!question] Lecture exercise: prove the time-shift property using the convolution property (§3)

> [!success]- Answer
> $x[n-k]=x[n]*\delta[n-k]$ (convolving with a shifted impulse shifts the signal). The convolution property gives $X(z)\cdot\mathcal{Z}\{\delta[n-k]\}=X(z)\,z^{-k}$, and the ROC is (at least) $R_x\cap\{z\ne0\}$ for $k>0$ or $R_x\cap\{z\ne\infty\}$ for $k<0$ — exactly the "except possibly $0$ or $\infty$" clause.

## 3. Linearity and convolution

> [!key] Linearity and convolution
> $$
> \begin{aligned}
> a\,x_1[n]+b\,x_2[n]&\ \longleftrightarrow\ a\,X_1(z)+b\,X_2(z),\qquad \\
> x_1[n]*x_2[n]&\ \longleftrightarrow\ X_1(z)\,X_2(z),
> \end{aligned}
> $$
> both with $\text{ROC}\supseteq R_{x_1}\cap R_{x_2}$ ("at least the intersection").

The intersection is natural: one divergent sum is enough to make the whole thing diverge (slide 10: $R_{x_1}=\{|z|>1\}$, $R_{x_2}=\{|z|>3\}$ give $|z|>3$). "At least" covers the exception: if a zero of one transform cancels a pole of the other, that pole's circle is no longer a boundary and the ROC can **grow**. Most of the time the ROC is simply the intersection.

> [!derivation]- Why convolution becomes multiplication (notes)
> With $y[n]=x_1[n]*x_2[n]$, split $z^{-n}=z^{-k}z^{-(n-k)}$ and substitute $n=m+k$:
> $$
> \begin{aligned}
> Y(z)&=\sum_{n}\Big(\sum_{k}x_1[k]\,x_2[n-k]\Big)z^{-n}\\
> &=\sum_{n}\sum_{k}x_1[k]z^{-k}\,x_2[n-k]z^{-(n-k)}\\
> &=\sum_{m}\sum_{k}x_1[k]z^{-k}\,x_2[m]z^{-m}\\
> &=\Big(\sum_{k}x_1[k]z^{-k}\Big)\Big(\sum_{m}x_2[m]z^{-m}\Big)=X_1(z)X_2(z).
> \end{aligned}
> $$
> Convolution in time is multiplication in $z$. With $x_2=h$ this is $Y(z)=H(z)X(z)$, the foundation of [[2-z-transform/09-transfer-functions|Lecture 9]].

> [!example] Example 2 (slides): a cancellation that enlarges the ROC
> $x_1[n]=(\tfrac12)^nu[n]-c\,(\tfrac12)^{n-1}u[n-1]$, $x_2[n]=(-1)^nu[n]$, $y[n]=x_1[n]*x_2[n]$, $c\in\mathbb{R}$. Find $Y(z)$ and its ROC for (a) $c=1$, (b) $c=-1$.
>
> The second term of $x_1$ is the first one delayed by one sample and scaled by $c$, so
> $$
> \begin{aligned}
> X_1(z)&=\frac{1}{1-\frac12z^{-1}}-\frac{c\,z^{-1}}{1-\frac12z^{-1}}=\frac{1-cz^{-1}}{1-\frac12z^{-1}},\ |z|>\tfrac12;\qquad \\
> X_2(z)&=\frac{1}{1+z^{-1}},\ |z|>1;
> \end{aligned}
> $$
> $$
> Y(z)=X_1(z)X_2(z)=\frac{1-cz^{-1}}{\left(1-\frac12z^{-1}\right)\left(1+z^{-1}\right)} .
> $$
> - (a) $c=1$: $Y(z)=\dfrac{1-z^{-1}}{\left(1-\frac12z^{-1}\right)\left(1+z^{-1}\right)}$, ROC $|z|>1$ (the intersection).
> - (b) $c=-1$: the zero at $-1$ cancels the pole at $-1$: $Y(z)=\dfrac{1}{1-\frac12z^{-1}}$, ROC $|z|>\tfrac12$ — **larger** than $R_{x_1}\cap R_{x_2}$. In time, $y[n]=(\tfrac12)^nu[n]$.
>
> (Checked with `np.convolve`; for (a) the time signal is $y[n]=-\tfrac13(\tfrac12)^nu[n]+\tfrac43(-1)^nu[n]$ by the partial fractions of Lecture 8.)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M25.0,50.0 h280.0 v176.0 h-280.0 Z M227.0,138.0 A62.0,62.0 0 1,0 103.0,138.0 A62.0,62.0 0 1,0 227.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="165.0" cy="138.0" r="62.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="25.0" y="50.0" width="280.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="25.0" y1="138.0" x2="305.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="165.0" y1="50.0" x2="165.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="165.0" cy="138.0" r="62.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="301.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="170.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="211.6" y="90.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="165.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><circle cx="227.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M191.0,133.0 L201.0,143.0 M191.0,143.0 L201.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="196.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><path d="M98.0,133.0 L108.0,143.0 M98.0,143.0 L108.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="103.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">−1</text><text x="165.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">c = 1</text><text x="165.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">Y = (1 − z⁻¹) / ((1 − ½z⁻¹)(1 + z⁻¹))</text><text x="165.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > 1</text><path d="M335.0,50.0 h280.0 v176.0 h-280.0 Z M506.0,138.0 A31.0,31.0 0 1,0 444.0,138.0 A31.0,31.0 0 1,0 506.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="475.0" cy="138.0" r="31.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="335.0" y="50.0" width="280.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="335.0" y1="138.0" x2="615.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="475.0" y1="50.0" x2="475.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="475.0" cy="138.0" r="62.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="611.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="480.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="521.6" y="90.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="475.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M501.0,133.0 L511.0,143.0 M501.0,143.0 L511.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="506.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><text x="475.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">c = −1</text><text x="475.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">Y = (1 + z⁻¹) / ((1 − ½z⁻¹)(1 + z⁻¹)) = 1 / (1 − ½z⁻¹)</text><text x="475.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > ½  (bigger than R₁ ∩ R₂)</text><g opacity="0.45"><circle cx="413.0" cy="138.0" r="7" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M408.0,133.0 L418.0,143.0 M408.0,143.0 L418.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/></g><text x="413.0" y="160.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px;">cancelled</text></svg><figcaption><strong>“At least the intersection”: a cancelled pole takes its boundary with it.</strong> Example 2 convolves x₁ (ROC |z| &gt; ½, zero at c) with x₂ = (−1)ⁿu[n] (pole at −1, ROC |z| &gt; 1). For c = 1 nothing cancels and the ROC is the intersection |z| &gt; 1. For c = −1 the zero of X₁ sits on the pole of X₂; they cancel, the only pole left is ½, and the ROC grows to |z| &gt; ½ — y[n] = (½)ⁿu[n].</figcaption></figure>

## 4. Differentiation: multiplying by n

> [!key] Differentiation in $z$
> $$
> n\,x[n]\ \longleftrightarrow\ -z\,\frac{dX(z)}{dz},\qquad \text{ROC}=R_x .
> $$

It produces the $n\,a^n$ rows of the table (and, in Lectures 9–11, double poles). With $X(z)=(1-az^{-1})^{-1}$ and $\frac{d}{dz}(1-az^{-1})=az^{-2}$:

$$
n\,a^nu[n]\ \longleftrightarrow\ -z\cdot\Big(-(1-az^{-1})^{-2}\,a z^{-2}\Big)=\frac{az^{-1}}{\left(1-az^{-1}\right)^2},\qquad |z|>|a| .
$$

> [!example] Example 3 (slides): $y[n]=2^n\,n\,x[n]$ with $x[n]=(\tfrac13)^nu[n]$
> $X(z)=\dfrac{1}{1-\frac13z^{-1}}$, $|z|>\tfrac13$. The class did it both ways.
>
> **Option 1 — differentiate, then scale.** $v[n]=n\,x[n]$: $V(z)=-z\dfrac{d}{dz}\dfrac{1}{1-\frac13z^{-1}}=\dfrac{\frac13z^{-1}}{\left(1-\frac13z^{-1}\right)^2}$. Then $y[n]=2^nv[n]$, so $Y(z)=V(z/2)=\dfrac{\frac13\left(\frac z2\right)^{-1}}{\left(1-\frac13\left(\frac z2\right)^{-1}\right)^2}$.
>
> **Option 2 — scale, then differentiate.** $g[n]=2^nx[n]$: $G(z)=X(z/2)=\dfrac{1}{1-\frac23z^{-1}}$. Then $Y(z)=-z\,G'(z)$.
>
> Both give
> $$
> Y(z)=\frac{\frac23z^{-1}}{\left(1-\frac23z^{-1}\right)^2},\qquad |z|>\tfrac23 ,
> $$
> which is just the table pair $n\,a^nu[n]$ with $a=\tfrac23$ — because $y[n]=n\,(\tfrac23)^nu[n]$.

> [!question] SP2021 #4 (10 pts): $x[n]\leftrightarrow X(z)=\dfrac{1}{1-\frac12z^{-1}}$, ROC $|z|>\tfrac12$. Find the z-transform of $(n+1)\,x[n]$ and its ROC

> [!success]- Answer
> Linearity: $(n+1)x[n]=n\,x[n]+x[n]$, and $n\,x[n]\leftrightarrow-z\frac{dX}{dz}=\dfrac{\frac12z^{-1}}{\left(1-\frac12z^{-1}\right)^2}$. So
> $$
> \mathcal{Z}\{(n+1)x[n]\}=\frac{\frac12z^{-1}}{\left(1-\frac12z^{-1}\right)^2}+\frac{1}{1-\frac12z^{-1}}=\frac{1}{\left(1-\frac12z^{-1}\right)^2},\qquad |z|>\tfrac12 .
> $$
> ([[exams/midterm-1/past-exams/spring-2021|SP2021]] #4. The same pattern with shifts: [[exams/midterm-1/past-exams/fall-2024|FA2024]] #5a, $(n+1)u[n-1]\leftrightarrow\frac{z^{-2}}{(1-z^{-1})^2}+\frac{2z^{-1}}{1-z^{-1}}$, $|z|>1$; [[exams/midterm-1/past-exams/fall-2023|FA2023]] #5, $n\,u[n+1]\leftrightarrow\frac{1}{(1-z^{-1})^2}-\frac{z}{1-z^{-1}}$, $1<|z|<\infty$.)

## 5. Scaling: multiplying by aⁿ

> [!key] Scaling in $z$
> $$
> a^n\,x[n]\ \longleftrightarrow\ X\!\left(\frac{z}{a}\right),\qquad a\in\mathbb{C},\qquad \text{ROC}=|a|\,R_x .
> $$
> One line: $\sum_n a^nx[n]z^{-n}=\sum_n x[n]\left(\frac{z}{a}\right)^{-n}$. A pole at $p$ moves to $a\,p$; an ROC $|z|>r$ becomes $|z|>|a|\,r$.

With $|a|=1$, $a=e^{j\omega_0}$ **rotates** the pole-zero plot by $\omega_0$ — that is modulation. Combined with Euler's formula it transforms any cosine-times-signal:

$$
\cos(\omega_0n)\,x[n]=\tfrac12e^{j\omega_0n}x[n]+\tfrac12e^{-j\omega_0n}x[n]\ \longleftrightarrow\ \tfrac12X\!\left(e^{-j\omega_0}z\right)+\tfrac12X\!\left(e^{j\omega_0}z\right).
$$

[[homework/hw3|HW3]] #2 with $x[n]=(\tfrac13)^nu[n]$: $2^nx[n]\leftrightarrow\dfrac{1}{1-\frac23z^{-1}}$, $|z|>\tfrac23$; and $\cos(\tfrac\pi4n)x[n]\leftrightarrow\dfrac12\Big[\dfrac{1}{1-\frac13e^{j\pi/4}z^{-1}}+\dfrac{1}{1-\frac13e^{-j\pi/4}z^{-1}}\Big]=\dfrac{1-\frac{\sqrt2}{6}z^{-1}}{1-\frac{\sqrt2}{3}z^{-1}+\frac19z^{-2}}$, $|z|>\tfrac13$.

> [!question] FA2025 #5(c): $x[n]=\cos^2\!\left(\tfrac{\pi}{4}n\right)u[n]$ — z-transform and ROC

> [!success]- Answer
> $\cos^2\theta=\tfrac12+\tfrac12\cos2\theta$, and $\cos(\tfrac\pi2n)=\tfrac12\left(e^{j\frac\pi2n}+e^{-j\frac\pi2n}\right)=\tfrac12(j^n+(-j)^n)$:
> $$
> \begin{aligned}
> x[n]&=\left(\tfrac12+\tfrac14j^n+\tfrac14(-j)^n\right)u[n]\\
> &\ \longleftrightarrow\ \frac{\frac12}{1-z^{-1}}+\frac{\frac14}{1-jz^{-1}}+\frac{\frac14}{1+jz^{-1}}\\
> &=\frac{\frac12}{1-z^{-1}}+\frac{\frac12}{1+z^{-2}},\qquad |z|>1 .
> \end{aligned}
> $$
> All three poles ($1,\ \pm j$) are on the unit circle, so the ROC is $|z|>1$. ([[exams/midterm-1/past-exams/fall-2025|FA2025]] #5c.)

## 6. Time reversal and conjugation

> [!key] Time reversal
> $$
> x[-n]\ \longleftrightarrow\ X\!\left(z^{-1}\right),\qquad \text{ROC}=1/R_x\quad(|z|>r\ \text{becomes}\ |z|<1/r).
> $$

> [!success]- Lecture exercise: prove it
> Substitute $m=-n$: $\sum_n x[-n]z^{-n}=\sum_m x[m]z^{m}=\sum_m x[m]\left(z^{-1}\right)^{-m}=X(z^{-1})$, which converges when $z^{-1}\in R_x$, i.e. $z\in1/R_x$.

Reversal turns right-sided pairs into left-sided ones: $x[n]=(\tfrac12)^nu[n]$ gives $x[-n]=2^nu[-n]\leftrightarrow\dfrac{1}{1-\frac12z}=\dfrac{-2z^{-1}}{1-2z^{-1}}$, ROC $|z|<2$; and $u[-n]\leftrightarrow\dfrac{1}{1-z}$, $|z|<1$. It is a quick route for signals like [[homework/hw3|HW3]] #1c's $3^nu[-n]$.

> [!key] Conjugation
> $x^*[n]\leftrightarrow X^*(z^*)$ with ROC $R_x$. For a **real** signal $x^*[n]=x[n]$, so $X(z)=X^*(z^*)$: poles and zeros come in **complex-conjugate pairs** — the fact [[2-z-transform/08-inverse-z-transform|Lecture 8]] uses to turn conjugate poles into a cosine. The Re/Im rows of the table follow: $\mathrm{Re}\{x[n]\}\leftrightarrow\tfrac12[X(z)+X^*(z^*)]$.

## 7. The properties table

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
> (The notes' table prints $\tfrac12[X(z)-X^*(z^*)]$ for the imaginary part; since $\mathrm{Im}\{x\}=\frac{x-x^*}{2j}$ the factor is $\tfrac{1}{2j}$.)

> [!recipe] z-transform of an exam signal with properties
> 1. **Name the base pair**: which table entry is hiding ($a^nu[n]$, $u[n]$, $\delta[n]$, a cosine)?
> 2. **Rewrite** the signal as a chain of operations on it: "shift by $k$", "multiply by $n$", "multiply by $a^n$", "reverse". Fix exponents to match shifted steps first (§2 trap).
> 3. **Apply** the properties one at a time and **update the ROC at each step**: shifts may drop $0$ or $\infty$, scaling multiplies radii by $|a|$, reversal inverts them, $n\,x[n]$ keeps them.
> 4. **Combine** pieces with linearity, intersect ROCs, and state the final ROC — including "$z\ne0$" or "$|z|<\infty$" when a shift introduced them.

> [!exam] How Lecture 7 is tested
> The "z-transform with ROC" problem (6 of 7 exams, 9–15 pts — [[problems/z-transform-with-roc|z-transform with ROC]]) is mostly this lecture: [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]] ($(n+1)x[n]$: differentiation + linearity), [[exams/midterm-1/past-exams/fall-2024|FA2024 #5a]] and [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]] (differentiation + shift; watch the advance in $n\,u[n+1]$ excluding $z=\infty$), [[exams/midterm-1/past-exams/fall-2025|FA2025 #5a, #5c]] (shift with an advance; Euler + scaling), [[exams/midterm-1/past-exams/spring-2025|SP2025 #5a]] ($\sum_{k=0}^{2}(\tfrac12)^ku[n-k]\leftrightarrow\frac{1+\frac12z^{-1}+\frac14z^{-2}}{1-z^{-1}}$, $|z|>1$: shift + linearity) and [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]]. The convolution property is the engine of every LCCDE and pole-cancellation problem later ([[problems/lccde-to-transfer-function-and-response|LCCDE ↔ H(z)]], [[problems/unbounded-outputs-and-pole-matching|pole matching]]), and ROC facts are True/False regulars: [[exams/midterm-1/past-exams/spring-2025|SP2025]] 1c ("the z-transform of $e^{j\frac\pi4n}$ does not exist because the ROC is empty" — True: the right half needs $|z|>1$, the left half $|z|<1$) and [[exams/midterm-1/past-exams/fall-2023|FA2023]] 1b ("the ROC cannot contain any poles or zeros" — False: zeros are allowed, e.g. $1-z^{-1}$ has ROC $z\ne0$, which contains its zero at $1$). [[homework/hw3|HW3]] #2 is this lecture in five parts.

## Related

- Concepts: [[concepts/z-transform-properties|z-transform properties]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/pole-zero-cancellation|pole-zero cancellation]] · [[concepts/convolution|convolution]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/sided-sequences|sided sequences]]
- Practice: [[problems/z-transform-with-roc|z-transform with ROC]] · [[homework/hw3|HW3]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[supplements/transform-tables|transform tables]]

### Sources for this page
Snyder, ECE 310 Lecture 7 notes ("z-transform properties": §1 overview and ROC rules 1–5, §2 properties with the shift and convolution derivations, Table 1) and slides of Sep 9, 2026, including the annotated slides 4 ($X(\tfrac14)$), 5–7 (ROC rules and sidedness examples), 8 (Example 1), 9 (shift examples), 10 (intersection), 13 (Example 2) and 15 (Example 3, both options). HW3 #1b, #2. Past exams FA2025 #5, SP2025 #5a, FA2024 #5a, FA2023 #5, SP2021 #4 with keys. All transforms checked numerically (`verify/lectures/l7_verify.py`, 44 checks); the Python output above is pasted from a real run.
