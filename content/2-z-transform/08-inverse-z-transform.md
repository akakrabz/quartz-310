---
title: "Lecture 8 — The inverse z-transform"
description: "x[n] from X(z) without the contour integral: finite pieces by inspection, table pairs plus shifts, partial fractions with cover-up, conjugate poles into cosines, and the side of every term from the ROC (all possible ROCs)."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 8
---

*Lecture 8 · Fri Sep 11, 2026 · notes + slides "Inverse z-transform" · prev: [[2-z-transform/07-z-transform-properties|Lecture 7]] · next: [[2-z-transform/09-transfer-functions|Lecture 9]]*

> [!abstract] In one breath
> - Reshape $X(z)$ into table entries: polynomial → impulses; proper rational → partial fractions $\sum_k \frac{A_k}{1-p_kz^{-1}}$, each $A_k$ by cover-up.
> - Conjugate pole pair → one real (decaying, steady or growing) sinusoid.
> - The ROC picks each term's side: poles inside the inner circle → right-sided, outside the outer circle → left-sided.

## 1. Common forms of the z-transform

### 1.1 Finite-length signals

$x[n]=\sum_{k=n_s}^{n_e}x[k]\,\delta[n-k]\ \leftrightarrow\ X(z)=\sum_{k=n_s}^{n_e}x[k]\,z^{-k}$ (impulse decomposition of Lecture 4, then the shift property).

### 1.2 Infinite-length signals

Table transforms are **rational**: a ratio of polynomials in $z^{-1}$. **Proper**: numerator degree < denominator degree ($N-1<M$).

$$
\begin{gathered}
\underbrace{X(z)=\frac{\sum_{k=0}^{N-1}b_kz^{-k}}{1+\sum_{k=1}^{M}a_kz^{-k}}}_{(1)\ \text{polynomials}}
\qquad
\underbrace{X(z)=\frac{\prod_{k=1}^{N-1}\left(1-q_kz^{-1}\right)}{\prod_{k=1}^{M}\left(1-p_kz^{-1}\right)}}_{(2)\ \text{factored: zeros } q_k,\ \text{poles } p_k}
\\[8pt]
\underbrace{X(z)=\sum_{k=1}^{M}\frac{A_k}{1-p_kz^{-1}}}_{(3)\ \text{partial fractions}}
\end{gathered}
$$

- $N$ input terms, $M$ feedback terms; form (2) as drawn has $b_0=1$ (else a constant $b_0$ multiplies it).
- Form (3) is the goal: every term is a table entry.

## 2. The inverse z-transform

Formal definition: $x[n]=\frac{1}{j2\pi}\oint_C X(z)\,z^{n-1}\,dz$. Never used in the course ("Don't worry, we won't use this formula!").

> [!key] Everything is built from three facts
> $$
> \begin{gathered}
> \delta[n-k]\ \leftrightarrow\ z^{-k},\qquad
> a^nu[n]\ \leftrightarrow\ \frac{1}{1-az^{-1}}\ \ (|z|>|a|),\\[4pt]
> -a^nu[-n-1]\ \leftrightarrow\ \frac{1}{1-az^{-1}}\ \ (|z|<|a|),
> \end{gathered}
> $$
> plus the time shift $x[n-k]\leftrightarrow z^{-k}X(z)$ ([[2-z-transform/07-z-transform-properties|Lecture 7]]): a factor $z^{-k}$ delays its term by $k$.

### 2.1 Finite-length signals

The pair of §1.1 is the inverse: read the coefficients of $z^{-k}$.

### 2.2 Infinite-length signals

> [!question] Example 1(a)–(c) (slides) — by inspection
> (a) $X(z)=1-\tfrac14z^{-1}+\tfrac1{16}z^{-2}$ (b) $X(z)=\dfrac{1}{1+\frac13z^{-1}}$, $|z|<\tfrac13$ (c) $X(z)=\dfrac{1}{1-\frac12z^{-1}}-\dfrac{3z^{-1}}{1+\frac15z^{-1}}$, $|z|>\tfrac12$

> [!success]- Answers
> (a) $x[n]=\delta[n]-\tfrac14\delta[n-1]+\tfrac1{16}\delta[n-2]=\{\underset{\uparrow}{1},-\tfrac14,\tfrac1{16}\}$.
> (b) Left-sided pair, $a=-\tfrac13$: $x[n]=-\left(-\tfrac13\right)^nu[-n-1]$.
> (c) Poles $\tfrac12$, $-\tfrac15$ both inside $|z|=\tfrac12$: both right-sided; $z^{-1}$ delays the second term:
> $$
> x[n]=\left(\tfrac12\right)^nu[n]-3\left(-\tfrac15\right)^{n-1}u[n-1].
> $$

Why form (3): with $A_1=3,\ p_1=\tfrac12,\ A_2=-1,\ p_2=-2$, causal, each term is one lookup:

$$
\frac{3}{1-\frac12z^{-1}}-\frac{1}{1+2z^{-1}}\ \longmapsto\ 3\left(\tfrac12\right)^nu[n]-(-2)^nu[n].
$$

> [!recipe] Partial fraction expansion, cover-up (proper $X(z)$, distinct poles)
> 1. **Factor the denominator** into $\prod_k(1-p_kz^{-1})$ (multiply by $z^M$, find roots in $z$). Write $X(z)=\sum_k\frac{A_k}{1-p_kz^{-1}}$.
> 2. **Multiply both sides** by the full denominator: numerator $=\sum_k A_k\prod_{j\ne k}(1-p_jz^{-1})$.
> 3. **Set $z=p_k$** ($z^{-1}=1/p_k$): all products but the $k$-th vanish. Shortcut (**cover-up**): delete $(1-p_kz^{-1})$ from $X(z)$, evaluate the rest at $z=p_k$:
> $$
> A_k=\Big[\left(1-p_kz^{-1}\right)X(z)\Big]_{z=p_k}.
> $$
> 4. **Check**: $\sum_kA_k=b_0$ (set $z^{-1}=0$).

> [!question] Exercise 1 (notes): $H(z)=\dfrac{2-z^{-1}}{1-\frac73z^{-1}+\frac23z^{-2}}$ — find $h[n]$
> ROC not given (so the factorization does not reveal the poles): give every case.

> [!success]- Answer
> $1-\tfrac73z^{-1}+\tfrac23z^{-2}=\left(1-\tfrac13z^{-1}\right)\left(1-2z^{-1}\right)$. Cover-up: $A_1=\left.\dfrac{2-z^{-1}}{1-2z^{-1}}\right|_{z^{-1}=3}=\dfrac{-1}{-5}=\dfrac15$ (pole $\tfrac13$), $A_2=\left.\dfrac{2-z^{-1}}{1-\frac13z^{-1}}\right|_{z^{-1}=1/2}=\dfrac{3/2}{5/6}=\dfrac95$ (pole $2$). Check: $\tfrac15+\tfrac95=2=b_0$ ✓.
> - $|z|>2$ (right-sided): $h[n]=\tfrac15\left(\tfrac13\right)^nu[n]+\tfrac95\,2^nu[n]$
> - $|z|<\tfrac13$ (left-sided): $h[n]=-\tfrac15\left(\tfrac13\right)^nu[-n-1]-\tfrac95\,2^nu[-n-1]$
> - $\tfrac13<|z|<2$ (two-sided, mentioned in words): $h[n]=\tfrac15\left(\tfrac13\right)^nu[n]-\tfrac95\,2^nu[-n-1]$

> [!question] Example 2 (slides): $X(z)=\dfrac{2-z^{-1}}{1+\frac23z^{-1}-\frac13z^{-2}}$, $x[n]$ right-sided

> [!success]- Answer
> Roots of $z^2+\tfrac23z-\tfrac13$: $z=\dfrac{-\frac23\pm\sqrt{\frac49+\frac43}}{2}=\dfrac{-\frac23\pm\frac43}{2}=\tfrac13,\ -1$.
> $$
> X(z)=\frac{2-z^{-1}}{\left(1+z^{-1}\right)\left(1-\frac13z^{-1}\right)}=\frac{A_1}{1+z^{-1}}+\frac{A_2}{1-\frac13z^{-1}}.
> $$
> $2-z^{-1}=A_1\left(1-\tfrac13z^{-1}\right)+A_2\left(1+z^{-1}\right)$. $z^{-1}=-1$: $3=\tfrac43A_1$, $A_1=\tfrac94$. $z^{-1}=3$: $-1=4A_2$, $A_2=-\tfrac14$. Check: $\tfrac94-\tfrac14=2=b_0$ ✓.
> $$
> x[n]=\tfrac94(-1)^nu[n]-\tfrac14\left(\tfrac13\right)^nu[n].
> $$

> [!question] Example 1(d) (slides): $X(z)=\dfrac{1-2z^{-1}+3z^{-2}}{\left(1-z^{-1}\right)\left(1+\frac23z^{-1}\right)\left(1-2z^{-1}\right)}$, $|z|>2$

> [!success]- Answer
> Poles $1,\ -\tfrac23,\ 2$; numerator degree $2<3$: proper. Cover-up with $w=z^{-1}$:
> - pole $1$ ($w=1$): $A_1=\dfrac{1-2+3}{\left(1+\frac23\right)(1-2)}=\dfrac{2}{-5/3}=-\dfrac65$
> - pole $-\tfrac23$ ($w=-\tfrac32$): $A_2=\dfrac{1+3+\frac{27}{4}}{\left(1+\frac32\right)(1+3)}=\dfrac{43/4}{10}=\dfrac{43}{40}$
> - pole $2$ ($w=\tfrac12$): $A_3=\dfrac{1-1+\frac34}{\left(1-\frac12\right)\left(1+\frac13\right)}=\dfrac{3/4}{2/3}=\dfrac98$
>
> Check: $-\tfrac65+\tfrac{43}{40}+\tfrac98=\tfrac{-48+43+45}{40}=1=b_0$ ✓. $|z|>2$: all right-sided:
> $$
> x[n]=\left[-\tfrac65+\tfrac{43}{40}\left(-\tfrac23\right)^n+\tfrac98\,2^n\right]u[n].
> $$

> [!question] Exercise 2 (notes): $H(z)=\dfrac{3-\frac32z^{-1}}{1-z^{-1}+z^{-2}}$, causal

> [!success]- Answer
> Negative discriminant: $p=\dfrac{1\pm\sqrt{1-4}}{2}=\tfrac12\pm j\tfrac{\sqrt3}{2}=e^{\pm j\pi/3}$. Multiply out:
> $$
> 3-\tfrac32z^{-1}=A_1\left(1-e^{-j\pi/3}z^{-1}\right)+A_2\left(1-e^{j\pi/3}z^{-1}\right).
> $$
> $z=e^{j\pi/3}$: $\tfrac94+j\tfrac{3\sqrt3}{4}=A_1\left(\tfrac32+j\tfrac{\sqrt3}{2}\right)$, so $A_1=\tfrac32$ (multiply by the conjugate $\tfrac32-j\tfrac{\sqrt3}2$, divide by $3$). Likewise $A_2=\tfrac32$:
> $$
> h[n]=\tfrac32\left(e^{j\frac{\pi}{3}n}+e^{-j\frac{\pi}{3}n}\right)u[n]=3\cos\left(\tfrac{\pi}{3}n\right)u[n].
> $$

> [!key] Conjugate pole pair $\Rightarrow$ one real sinusoid
> Poles $p=re^{\pm j\omega_0}$, coefficients $A$, $A^*$ (right-sided):
> $$
> A\,p^n+A^*(p^*)^n=2\,\mathrm{Re}\{A\,p^n\}=2|A|\,r^n\cos\left(\omega_0n+\angle A\right)u[n].
> $$
> $r=1$: on the unit circle, periodic; $r<1$: decaying; $r>1$: growing. One coefficient per pair.

### All possible ROCs (slides, Example 3)

PFE ignores the ROC; the ROC enters only at inversion. Each $\frac{A_k}{1-p_kz^{-1}}$ has two inverses ($|z|>|p_k|$ or $|z|<|p_k|$), and the ROC of $X$ lies inside every term's ROC.

> [!key] Reading the sides off the ROC $r_1<|z|<r_2$
> - Pole **inside** the inner circle ($|p_k|\le r_1$): **right-sided** $A_k\,p_k^n\,u[n]$.
> - Pole **outside** the outer circle ($|p_k|\ge r_2$): **left-sided** $-A_k\,p_k^n\,u[-n-1]$.
> - $M$ distinct pole radii → $M+1$ candidate ROCs, from $|z|<r_{\min}$ (all left) to $|z|>r_{\max}$ (all right).

> [!question] Example 3 (slides): all possible ROCs of $X(z)=\dfrac{1}{\left(1-\frac43z^{-1}\right)\left(1-\frac23z^{-1}\right)}$ and each $x[n]$

> [!success]- Answer
> $1=A_1\left(1-\tfrac23z^{-1}\right)+A_2\left(1-\tfrac43z^{-1}\right)$. $z=\tfrac43$: $1=\tfrac12A_1$, $A_1=2$. $z=\tfrac23$: $1=A_2(1-2)$, $A_2=-1$. So $X(z)=\dfrac{2}{1-\frac43z^{-1}}-\dfrac{1}{1-\frac23z^{-1}}$.
>
> | | $\tfrac23$ right-sided ($\lvert z\rvert>\tfrac23$) | $\tfrac23$ left-sided ($\lvert z\rvert<\tfrac23$) |
> |---|---|---|
> | $\tfrac43$ right-sided ($\lvert z\rvert>\tfrac43$) | $\lvert z\rvert>\tfrac43$ | empty |
> | $\tfrac43$ left-sided ($\lvert z\rvert<\tfrac43$) | $\tfrac23<\lvert z\rvert<\tfrac43$ | $\lvert z\rvert<\tfrac23$ |
>
> 1. $|z|>\tfrac43$: $x_1[n]=2\left(\tfrac43\right)^nu[n]-\left(\tfrac23\right)^nu[n]$
> 2. $\tfrac23<|z|<\tfrac43$: $x_2[n]=-2\left(\tfrac43\right)^nu[-n-1]-\left(\tfrac23\right)^nu[n]$
> 3. $|z|<\tfrac23$: $x_3[n]=-2\left(\tfrac43\right)^nu[-n-1]+\left(\tfrac23\right)^nu[-n-1]$
> 4. $\tfrac43$ right, $\tfrac23$ left: no $z$ works; unbounded as $n\to\pm\infty$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M9.0,50.0 h196.0 v168.0 h-196.0 Z M171.0,134.0 A64.0,64.0 0 1,0 43.0,134.0 A64.0,64.0 0 1,0 171.0,134.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="107.0" cy="134.0" r="64.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="9.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="9.0" y1="134.0" x2="205.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="107.0" y1="50.0" x2="107.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="107.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="201.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="112.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="143.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="107.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="100.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M166.0,129.0 L176.0,139.0 M166.0,139.0 L176.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="171.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M134.0,129.0 L144.0,139.0 M134.0,139.0 L144.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="139.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="107.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| > 4/3</text><text x="107.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms right-sided</text><text x="107.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">2(4/3)ⁿ u[n]</text><text x="107.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">− (2/3)ⁿ u[n]</text><path d="M384.0,134.0 A64.0,64.0 0 1,0 256.0,134.0 A64.0,64.0 0 1,0 384.0,134.0 Z M352.0,134.0 A32.0,32.0 0 1,0 288.0,134.0 A32.0,32.0 0 1,0 352.0,134.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="320.0" cy="134.0" r="32.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="320.0" cy="134.0" r="64.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="222.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="222.0" y1="134.0" x2="418.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="320.0" y1="50.0" x2="320.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="320.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="414.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="325.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="356.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="320.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="313.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M379.0,129.0 L389.0,139.0 M379.0,139.0 L389.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="384.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M347.0,129.0 L357.0,139.0 M347.0,139.0 L357.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="352.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="320.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">2/3 < |z| < 4/3</text><text x="320.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">4/3 left-sided, 2/3 right-sided</text><text x="320.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">−2(4/3)ⁿ u[−n−1]</text><text x="320.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">− (2/3)ⁿ u[n]</text><circle cx="533.0" cy="134.0" r="32.0" fill="var(--accent)" fill-opacity="0.20" stroke="var(--accent)" stroke-width="1.6"/><rect x="435.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="435.0" y1="134.0" x2="631.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="533.0" y1="50.0" x2="533.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="533.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="627.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="538.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="569.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="533.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="526.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M592.0,129.0 L602.0,139.0 M592.0,139.0 L602.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="597.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M560.0,129.0 L570.0,139.0 M560.0,139.0 L570.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="565.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="533.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| < 2/3</text><text x="533.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms left-sided</text><text x="533.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">−2(4/3)ⁿ u[−n−1]</text><text x="533.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">+ (2/3)ⁿ u[−n−1]</text></svg><figcaption><strong>One X(z), three signals (Example 3).</strong> Each ring between the pole circles 2/3 and 4/3 is a valid ROC with its own x[n]; the fourth sign pattern would need |z| &gt; 4/3 and |z| &lt; 2/3 at once.</figcaption></figure>

> [!recipe] "Find all possible ROCs and the corresponding $x[n]$"
> 1. PFE once: $p_k$, $A_k$.
> 2. Sort distinct pole radii $r_1<\dots<r_M$; ROCs: $|z|<r_1$, $r_1<|z|<r_2$, …, $|z|>r_M$. Equal-radius poles (conjugate pair, $\pm a$) go to the same side.
> 3. Per ring: inside/outside rule → $x[n]$.
> 4. If asked: $|z|>r_M$ is causal; the ring containing $|z|=1$ is stable ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]).

> [!trap] Points lost on inverse z
> - Substituting $z^{-1}=p_k$ instead of $z^{-1}=1/p_k$.
> - Mixing forms: $\frac{C}{z-p}=\frac{Cz^{-1}}{1-pz^{-1}}$ is $C\,p^{n-1}u[n-1]$, not $C\,p^nu[n]$. Stay in $z^{-1}$.
> - Cover-up needs a proper $X(z)$ with distinct poles. Improper: divide first ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]). Repeated pole: $n\,a^nu[n]\leftrightarrow\frac{az^{-1}}{(1-az^{-1})^2}$ (Lecture 7).
> - Listing $2^M$ sign patterns: only $M+1$ rings exist; outer pole right + inner pole left is empty.
> - Dropping the minus on left-sided terms: $-A\,p^nu[-n-1]$.

> [!exam] Inverse z / PFE / all possible ROCs — 7 of 7 past exams, 15–20 points
> All ROCs and signals, or "stable/causal — find $h[n]$" (one ring). Show the cover-up arithmetic; write $u[n]$ / $u[-n-1]$. Family: [[problems/all-possible-rocs|all possible ROCs]].
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #7]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #7]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #6]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #6]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #5, #7]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #6, #7]]

## Related

[[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/partial-fraction-expansion|partial fraction expansion]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[0-toolkit/04-factoring-and-long-division|factoring and long division]] · [[0-toolkit/01-complex-numbers|complex numbers]] · [[homework/hw3|HW3]] · [[homework/hw4|HW4]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[demos/python-demos|Python demos]]

### Sources for this page

Snyder, Lecture 8 notes (§1 common forms, §2 inverse transform, Exercises 1–2, PFE procedure) and slides (Examples 1–3, annotated ROC table); past exams above.
