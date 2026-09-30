---
title: "Lecture 8 — The inverse z-transform"
description: "Getting x[n] back from X(z) without the contour integral: finite pieces by inspection, table pairs plus the shift property, partial fractions with the cover-up rule in z⁻¹ form, long division as a check, complex-conjugate poles into cosines, and choosing a right- or left-sided term for every pole from the ROC (all possible ROCs). With scipy.signal.residuez."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 8
---

*Lecture 8 · Fri Sep 11, 2026 · notes + slides "Inverse z-transform" · prev: [[2-z-transform/07-z-transform-properties|Lecture 7]] · next: [[2-z-transform/09-transfer-functions|Lecture 9]]*

> [!abstract] In one breath
> Nobody computes the inverse z-transform integral. Instead you **reshape** $X(z)$ into pieces the table already knows: polynomial pieces are impulses you read off; a proper rational $X(z)$ is split by **partial fractions** into $\sum_k \frac{A_k}{1-p_kz^{-1}}$, with each $A_k$ found by **cover-up** (delete the factor, set $z=p_k$); a pair of complex-conjugate poles recombines by Euler into a (growing, steady or decaying) cosine. Then the **ROC** decides, pole by pole, whether a term is right-sided, $A_kp_k^nu[n]$, or left-sided, $-A_kp_k^nu[-n-1]$: poles inside the ROC's inner circle go right, poles outside its outer circle go left. $M$ distinct pole radii give $M+1$ possible ROCs — and $M+1$ different signals for the same $X(z)$.

## 1. The forms X(z) comes in

**Finite-length signals** (Lecture 6) give polynomials: $x[n]=\sum_{k=n_s}^{n_e}x[k]\,\delta[n-k]\ \leftrightarrow\ X(z)=\sum_{k=n_s}^{n_e}x[k]\,z^{-k}$.

**Infinite-length signals** from the table give **rational** functions, a ratio of polynomials in $z^{-1}$, written three ways:

$$
\underbrace{X(z)=\frac{\sum_{k=0}^{N-1}b_kz^{-k}}{1+\sum_{k=1}^{M}a_kz^{-k}}}_{(1)\ \text{polynomials}}
\qquad
\underbrace{X(z)=\frac{\prod_{k=1}^{N-1}\left(1-q_kz^{-1}\right)}{\prod_{k=1}^{M}\left(1-p_kz^{-1}\right)}}_{(2)\ \text{factored: zeros } q_k,\ \text{poles } p_k}
\qquad
\underbrace{X(z)=\sum_{k=1}^{M}\frac{A_k}{1-p_kz^{-1}}}_{(3)\ \text{partial fractions}}
$$

($N$ feed-forward coefficients, $M$ feedback coefficients; form (2) is drawn with $b_0=1$, otherwise a constant $b_0$ multiplies it.) The expression is **proper** when the numerator degree is less than the denominator degree ($N-1<M$). Form (3) is the goal, because each of its terms is a table entry.

The formal inverse is a contour integral, $x[n]=\frac{1}{j2\pi}\oint_C X(z)\,z^{n-1}\,dz$. The course never uses it ("Don't worry, we won't use this formula!").

## 2. Inverse by inspection: finite pieces, table pairs, shifts

> [!key] Everything is built from three facts
> $$
> \delta[n-k]\ \leftrightarrow\ z^{-k},\qquad
> a^nu[n]\ \leftrightarrow\ \frac{1}{1-az^{-1}}\ \ (|z|>|a|),\qquad
> -a^nu[-n-1]\ \leftrightarrow\ \frac{1}{1-az^{-1}}\ \ (|z|<|a|),
> $$
> plus the time-shift property $x[n-k]\leftrightarrow z^{-k}X(z)$ from [[2-z-transform/07-z-transform-properties|Lecture 7]]. A factor $z^{-k}$ in front of a term delays that term by $k$.

The slide's Example 1, solved in class:

- (a) $X(z)=1-\tfrac14z^{-1}+\tfrac1{16}z^{-2}$ (all $z\ne0$): read the coefficients, $x[n]=\delta[n]-\tfrac14\delta[n-1]+\tfrac1{16}\delta[n-2]=\{\underset{\uparrow}{1},-\tfrac14,\tfrac1{16}\}$.
- (b) $X(z)=\dfrac{1}{1+\frac13z^{-1}}$, ROC $|z|<\tfrac13$: left-sided pair with $a=-\tfrac13$, so $x[n]=-\left(-\tfrac13\right)^nu[-n-1]$.
- (c) $X(z)=\dfrac{1}{1-\frac12z^{-1}}-\dfrac{3z^{-1}}{1+\frac15z^{-1}}$, ROC $|z|>\tfrac12$: both poles ($\tfrac12$ and $-\tfrac15$) lie inside $|z|=\tfrac12$, so both terms are right-sided; the $z^{-1}$ delays the second one by a sample:

$$
x[n]=\left(\tfrac12\right)^nu[n]-3\left(-\tfrac15\right)^{n-1}u[n-1].
$$

The same move handles exam transforms that mix a polynomial with a fraction — [[0-midterm-1/past-exams/fall-2019|FA2019]] #6: $Y(z)=1+z^{-100}+\dfrac{1}{1-5z^{-1}}$, $|z|>5$, is $y[n]=\delta[n]+\delta[n-100]+5^nu[n]$.

> [!tip] A $z^{-k}$ in the numerator is a shift, not a reason to expand
> In (c), $\dfrac{3z^{-1}}{1+\frac15z^{-1}}=z^{-1}\cdot\dfrac{3}{1+\frac15z^{-1}}$: invert the fraction, then delay. Partial fractions are for denominators with **several** poles.

## 3. Partial fraction expansion

The notes first show why form (3) is the goal. With $A_1=3,\ p_1=\tfrac12,\ A_2=-1,\ p_2=-2$ and a causal signal, each term is one table lookup:

$$
\frac{3}{1-\frac12z^{-1}}-\frac{1}{1+2z^{-1}}\ \longmapsto\ 3\left(\tfrac12\right)^nu[n]-(-2)^nu[n].
$$

So the only real work is getting from form (1) or (2) to form (3).

> [!recipe] Partial fractions, cover-up style (proper $X(z)$, distinct poles)
> 1. **Factor the denominator** into $\prod_k(1-p_kz^{-1})$: multiply it by $z^M$ and find the roots in $z$ (quadratic formula) — those roots are the poles $p_k$. Write $X(z)=\sum_k\frac{A_k}{1-p_kz^{-1}}$.
> 2. **Multiply both sides** by the full denominator: the numerator of $X$ equals $\sum_k A_k\prod_{j\ne k}(1-p_jz^{-1})$.
> 3. **Set $z=p_k$**, i.e. $z^{-1}=1/p_k$: every product except the $k$-th vanishes, leaving $A_k$. Shortcut (**cover-up**): delete the factor $(1-p_kz^{-1})$ from $X(z)$ and evaluate what is left at $z^{-1}=1/p_k$:
> $$
> A_k=\Big[\left(1-p_kz^{-1}\right)X(z)\Big]_{z=p_k}.
> $$
> 4. **Check**: at $z^{-1}=0$ both sides equal $b_0$, so $\sum_kA_k=b_0$ (for a proper $X$).

> [!example] Example 2 (slides): $X(z)=\dfrac{2-z^{-1}}{1+\frac23z^{-1}-\frac13z^{-2}}$, $x[n]$ right-sided
> **Factor.** Multiply the denominator by $z^2$ and use the quadratic formula on $z^2+\tfrac23z-\tfrac13$: $z=\dfrac{-\frac23\pm\sqrt{\frac49+\frac43}}{2}=\dfrac{-\frac23\pm\frac43}{2}=\tfrac13,\ -1$. So
> $$
> X(z)=\frac{2-z^{-1}}{\left(1+z^{-1}\right)\left(1-\frac13z^{-1}\right)}=\frac{A_1}{1+z^{-1}}+\frac{A_2}{1-\frac13z^{-1}}.
> $$
> **Multiply out:** $2-z^{-1}=A_1\left(1-\tfrac13z^{-1}\right)+A_2\left(1+z^{-1}\right)$.
>
> **Cover up.** $z=-1$ ($z^{-1}=-1$): $3=\tfrac43A_1$, so $A_1=\tfrac94$. $z=\tfrac13$ ($z^{-1}=3$): $-1=4A_2$, so $A_2=-\tfrac14$. Check: $\tfrac94-\tfrac14=2=b_0$ ✓.
>
> **Invert** (right-sided, so every term is right-sided):
> $$
> x[n]=\tfrac94(-1)^nu[n]-\tfrac14\left(\tfrac13\right)^nu[n].
> $$

> [!trap] Cover-up slips that cost points
> - Substituting $z^{-1}=p_k$ instead of $z^{-1}=1/p_k$. The factor $(1-p_kz^{-1})$ vanishes at $z=p_k$.
> - Mixing the $z$-form and the $z^{-1}$-form: a term $\frac{C}{z-p}$ equals $\frac{Cz^{-1}}{1-pz^{-1}}$, a **delayed** exponential $C\,p^{n-1}u[n-1]$ — not $C\,p^nu[n]$. Stay in $z^{-1}$ form throughout, as the course does.
> - Using cover-up on an **improper** $X(z)$ (numerator degree $\ge$ denominator degree): the expansion then also needs a polynomial part — divide first ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]).
> - A **repeated** pole $\frac{1}{(1-pz^{-1})^2}$ is not covered by this recipe; it needs the pair $n\,a^nu[n]\leftrightarrow\frac{az^{-1}}{(1-az^{-1})^2}$ from [[2-z-transform/07-z-transform-properties|Lecture 7]].

> [!question] Exercise 1 (notes): $H(z)=\dfrac{2-z^{-1}}{1-\frac73z^{-1}+\frac23z^{-2}}$ — find $h[n]$ for every possible ROC
> The notes leave the ROC unstated on purpose (so the factorization does not give away the poles) and solve the right- and left-sided cases.

> [!success]- Answer
> $1-\tfrac73z^{-1}+\tfrac23z^{-2}=\left(1-\tfrac13z^{-1}\right)\left(1-2z^{-1}\right)$. Cover-up: $A_1=\left.\dfrac{2-z^{-1}}{1-2z^{-1}}\right|_{z^{-1}=3}=\dfrac{-1}{-5}=\dfrac15$ (pole $\tfrac13$), $A_2=\left.\dfrac{2-z^{-1}}{1-\frac13z^{-1}}\right|_{z^{-1}=1/2}=\dfrac{3/2}{5/6}=\dfrac95$ (pole $2$). Check: $\tfrac15+\tfrac95=2=b_0$ ✓.
> - $|z|>2$ (right-sided): $h[n]=\tfrac15\left(\tfrac13\right)^nu[n]+\tfrac95\,2^nu[n]$
> - $|z|<\tfrac13$ (left-sided): $h[n]=-\tfrac15\left(\tfrac13\right)^nu[-n-1]-\tfrac95\,2^nu[-n-1]$
> - $\tfrac13<|z|<2$ (two-sided — the case the notes mention in words): $h[n]=\tfrac15\left(\tfrac13\right)^nu[n]-\tfrac95\,2^nu[-n-1]$

> [!question] Example 1(d) (slides — "too difficult (for now)" in class): $X(z)=\dfrac{1-2z^{-1}+3z^{-2}}{\left(1-z^{-1}\right)\left(1+\frac23z^{-1}\right)\left(1-2z^{-1}\right)}$, $|z|>2$

> [!success]- Answer
> Three distinct poles $1,\ -\tfrac23,\ 2$, numerator degree $2<3$: proper. Cover-up with $w=z^{-1}$:
> - pole $1$ ($w=1$): $A_1=\dfrac{1-2+3}{\left(1+\frac23\right)(1-2)}=\dfrac{2}{-5/3}=-\dfrac65$
> - pole $-\tfrac23$ ($w=-\tfrac32$): $A_2=\dfrac{1+3+\frac{27}{4}}{\left(1+\frac32\right)(1+3)}=\dfrac{43/4}{10}=\dfrac{43}{40}$
> - pole $2$ ($w=\tfrac12$): $A_3=\dfrac{1-1+\frac34}{\left(1-\frac12\right)\left(1+\frac13\right)}=\dfrac{3/4}{2/3}=\dfrac98$
>
> Check: $-\tfrac65+\tfrac{43}{40}+\tfrac98=\tfrac{-48+43+45}{40}=1=b_0$ ✓. ROC $|z|>2$ is outside every pole, so all terms are right-sided:
> $$
> x[n]=\left[-\tfrac65+\tfrac{43}{40}\left(-\tfrac23\right)^n+\tfrac98\,2^n\right]u[n].
> $$

## 4. Long division: the power-series view (and a free check)

A right-sided $X(z)$ is a power series in $z^{-1}$ whose coefficients are $x[0],x[1],x[2],\dots$. Dividing the numerator by the denominator in increasing powers of $z^{-1}$ produces that series one sample at a time. For Example 2:

$$
\frac{2-z^{-1}}{1+\frac23z^{-1}-\frac13z^{-2}}=2-\tfrac73z^{-1}+\tfrac{20}{9}z^{-2}-\tfrac{61}{27}z^{-3}+\cdots
$$

(first step: $2\times$ the denominator leaves $-\tfrac73z^{-1}+\tfrac23z^{-2}$; next: $-\tfrac73z^{-1}\times$ the denominator leaves $\tfrac{20}9z^{-2}-\tfrac79z^{-3}$; and so on). The PFE answer gives $x[0]=\tfrac94-\tfrac14=2$, $x[1]=-\tfrac94-\tfrac1{12}=-\tfrac73$, $x[2]=\tfrac94-\tfrac1{36}=\tfrac{20}9$ — it agrees. Division is the same computation as running the recursion $x[n]=-\tfrac23x[n-1]+\tfrac13x[n-2]+2\delta[n]-\delta[n-1]$ (the LCCDE view of [[2-z-transform/09-transfer-functions|Lecture 9]]).

> [!tip] Use it as a 30-second check on an exam
> After a PFE, compute $x[0]$ and $x[1]$ by division (or the recursion) and compare with your closed form. It catches sign slips and a wrong $A_k$ immediately. Division **never** gives a closed form for an infinite signal, so it is a check, not a method — except for **finite pieces**: when $X(z)$ is improper, dividing first splits off a polynomial (a finite set of impulses, read off by inspection) plus a proper remainder for the PFE. See [[0-toolkit/04-factoring-and-long-division|factoring and long division]] and [[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]].

## 5. Complex-conjugate poles become cosines

> [!example] Exercise 2 (notes): $H(z)=\dfrac{3-\frac32z^{-1}}{1-z^{-1}+z^{-2}}$, causal
> The discriminant of $1-z^{-1}+z^{-2}$ is negative, so the poles are complex: $p=\dfrac{1\pm\sqrt{1-4}}{2}=\tfrac12\pm j\tfrac{\sqrt3}{2}=e^{\pm j\pi/3}$ (on the unit circle). Write $H(z)=\dfrac{A_1}{1-e^{j\pi/3}z^{-1}}+\dfrac{A_2}{1-e^{-j\pi/3}z^{-1}}$ and multiply out:
> $$
> 3-\tfrac32z^{-1}=A_1\left(1-e^{-j\pi/3}z^{-1}\right)+A_2\left(1-e^{j\pi/3}z^{-1}\right).
> $$
> At $z=e^{j\pi/3}$: $3-\tfrac32e^{-j\pi/3}=A_1\left(1-e^{-j2\pi/3}\right)$, i.e. $\tfrac94+j\tfrac{3\sqrt3}{4}=A_1\left(\tfrac32+j\tfrac{\sqrt3}{2}\right)$, so $A_1=\tfrac32$ (multiply by the conjugate $\tfrac32-j\tfrac{\sqrt3}2$ and divide by $3$). Likewise $A_2=\tfrac32$. Then
> $$
> h[n]=\tfrac32\left(e^{j\frac{\pi}{3}n}+e^{-j\frac{\pi}{3}n}\right)u[n]=3\cos\left(\tfrac{\pi}{3}n\right)u[n].
> $$

For a real signal the two conjugate poles always come with conjugate coefficients, and Euler turns the pair into one real sinusoid:

> [!key] Conjugate pole pair $\Rightarrow$ one real sinusoid
> Poles $p=re^{\pm j\omega_0}$ with coefficients $A$ and $A^*$ (right-sided):
> $$
> A\,p^n+A^*(p^*)^n=2\,\mathrm{Re}\{A\,p^n\}=2|A|\,r^n\cos\left(\omega_0n+\angle A\right)u[n].
> $$
> $r=1$: poles on the unit circle, a pure (periodic) sinusoid; $r<1$: decaying; $r>1$: growing. So you only ever compute **one** coefficient per pair. Alternatively match the numerator to the table's $a^n\cos(\omega_0n)u[n]$ and $a^n\sin(\omega_0n)u[n]$ rows ([[2-z-transform/06-the-z-transform|Lecture 6]]): here $\cos\frac\pi3=\frac12$ gives exactly $3\cdot\dfrac{1-\frac12z^{-1}}{1-z^{-1}+z^{-2}}$.

> [!question] [[0-midterm-1/past-exams/spring-2021|SP2021]] #5(a): $H(z)=\dfrac{3z^{-1}}{1+z^{-2}}$, ROC $|z|>1$. Write $h[n]=A\sin(\omega_0 n+\theta)\,u[n]$: find $A$, $\omega_0$, $\theta$

> [!success]- Answer
> Poles $\pm j=e^{\pm j\pi/2}$ ($r=1$), since $1+z^{-2}=(1-jz^{-1})(1+jz^{-1})$. Cover-up at $z=j$ ($z^{-1}=-j$): $A_1=\dfrac{3(-j)}{1+j(-j)}=-\dfrac{3j}{2}$, so $|A_1|=\tfrac32$, $\angle A_1=-\tfrac\pi2$, and $h[n]=3\cos\left(\tfrac\pi2n-\tfrac\pi2\right)u[n]=3\sin\left(\tfrac\pi2n\right)u[n]$: $A=3$, $\omega_0=\tfrac\pi2$, $\theta=0$. (The exam's hint route: the table's $\sin$ row with $\omega_0=\frac\pi2$ is $\frac{z^{-1}}{1+z^{-2}}$, times 3.) Poles on the unit circle mean a bounded $h$ but not a BIBO-stable system ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]): part (b) asks for a bounded input with an unbounded output, and any input at the pole frequency works — $j^nu[n]$, $\cos(\frac\pi2n)u[n]$ or $\sin(\frac\pi2n)u[n]$.

## 6. Choosing the side of every term: all possible ROCs

Partial fractions do not use the ROC; the ROC enters only when each term is inverted. Each term $\frac{A_k}{1-p_kz^{-1}}$ has two possible inverses, with ROCs $|z|>|p_k|$ (right-sided) or $|z|<|p_k|$ (left-sided), and the ROC of $X$ must lie inside the ROC of every term.

> [!key] Reading the sides off the ROC
> For an ROC $r_1<|z|<r_2$:
> - every pole **inside** the inner circle ($|p_k|\le r_1$) gives a **right-sided** term $A_k\,p_k^n\,u[n]$;
> - every pole **outside** the outer circle ($|p_k|\ge r_2$) gives a **left-sided** term $-A_k\,p_k^n\,u[-n-1]$.
>
> Poles cannot sit inside the ROC, so every pole is one or the other. $M$ distinct pole radii cut the plane into $M+1$ candidate ROCs, from $|z|<r_{\min}$ (all left-sided) to $|z|>r_{\max}$ (all right-sided).

> [!example] Example 3 (slides): all possible ROCs of $X(z)=\dfrac{1}{\left(1-\frac43z^{-1}\right)\left(1-\frac23z^{-1}\right)}$
> **Step 1–3 (PFE):** $1=A_1\left(1-\tfrac23z^{-1}\right)+A_2\left(1-\tfrac43z^{-1}\right)$. At $z=\tfrac43$: $1=\tfrac12A_1$, $A_1=2$. At $z=\tfrac23$: $1=A_2(1-2)$, $A_2=-1$. So $X(z)=\dfrac{2}{1-\frac43z^{-1}}-\dfrac{1}{1-\frac23z^{-1}}$.
>
> **Sides.** The in-class table of the four sign patterns (pole $\tfrac43$ = rows, pole $\tfrac23$ = columns):
>
> | | $\tfrac23$ right-sided ($\lvert z\rvert>\tfrac23$) | $\tfrac23$ left-sided ($\lvert z\rvert<\tfrac23$) |
> |---|---|---|
> | $\tfrac43$ right-sided ($\lvert z\rvert>\tfrac43$) | $\lvert z\rvert>\tfrac43$ | empty |
> | $\tfrac43$ left-sided ($\lvert z\rvert<\tfrac43$) | $\tfrac23<\lvert z\rvert<\tfrac43$ | $\lvert z\rvert<\tfrac23$ |
>
> 1. $|z|>\tfrac43$ (both right-sided): $x_1[n]=2\left(\tfrac43\right)^nu[n]-\left(\tfrac23\right)^nu[n]$
> 2. $\tfrac23<|z|<\tfrac43$ ($\tfrac43$ left, $\tfrac23$ right): $x_2[n]=-2\left(\tfrac43\right)^nu[-n-1]-\left(\tfrac23\right)^nu[n]$
> 3. $|z|<\tfrac23$ (both left-sided): $x_3[n]=-2\left(\tfrac43\right)^nu[-n-1]+\left(\tfrac23\right)^nu[-n-1]$
> 4. $\tfrac43$ right-sided with $\tfrac23$ left-sided: the z-transform does not exist for any $z$ — that $x_4[n]$ would be unbounded as $n\to+\infty$ **and** as $n\to-\infty$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M9.0,50.0 h196.0 v168.0 h-196.0 Z M171.0,134.0 A64.0,64.0 0 1,0 43.0,134.0 A64.0,64.0 0 1,0 171.0,134.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="107.0" cy="134.0" r="64.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="9.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="9.0" y1="134.0" x2="205.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="107.0" y1="50.0" x2="107.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="107.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="201.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="112.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="143.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="107.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="100.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M166.0,129.0 L176.0,139.0 M166.0,139.0 L176.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="171.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M134.0,129.0 L144.0,139.0 M134.0,139.0 L144.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="139.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="107.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| > 4/3</text><text x="107.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms right-sided</text><text x="107.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">2(4/3)ⁿ u[n]</text><text x="107.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">− (2/3)ⁿ u[n]</text><path d="M384.0,134.0 A64.0,64.0 0 1,0 256.0,134.0 A64.0,64.0 0 1,0 384.0,134.0 Z M352.0,134.0 A32.0,32.0 0 1,0 288.0,134.0 A32.0,32.0 0 1,0 352.0,134.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="320.0" cy="134.0" r="32.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="320.0" cy="134.0" r="64.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="222.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="222.0" y1="134.0" x2="418.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="320.0" y1="50.0" x2="320.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="320.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="414.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="325.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="356.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="320.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="313.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M379.0,129.0 L389.0,139.0 M379.0,139.0 L389.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="384.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M347.0,129.0 L357.0,139.0 M347.0,139.0 L357.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="352.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="320.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">2/3 < |z| < 4/3</text><text x="320.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">4/3 left-sided, 2/3 right-sided</text><text x="320.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">−2(4/3)ⁿ u[−n−1]</text><text x="320.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">− (2/3)ⁿ u[n]</text><circle cx="533.0" cy="134.0" r="32.0" fill="var(--accent)" fill-opacity="0.20" stroke="var(--accent)" stroke-width="1.6"/><rect x="435.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="435.0" y1="134.0" x2="631.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="533.0" y1="50.0" x2="533.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="533.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="627.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="538.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="569.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="533.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="526.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M592.0,129.0 L602.0,139.0 M592.0,139.0 L602.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="597.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M560.0,129.0 L570.0,139.0 M560.0,139.0 L570.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="565.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="533.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| < 2/3</text><text x="533.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms left-sided</text><text x="533.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">−2(4/3)ⁿ u[−n−1]</text><text x="533.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">+ (2/3)ⁿ u[−n−1]</text></svg><figcaption><strong>One X(z), three signals.</strong> X(z) = 1/((1 − (4/3)z<sup>−1</sup>)(1 − (2/3)z<sup>−1</sup>)) = 2/(1 − (4/3)z<sup>−1</sup>) − 1/(1 − (2/3)z<sup>−1</sup>) has poles at 4/3 and 2/3 (×) and a double zero at 0 (○). The pole circles cut the plane into three rings, and each ring is a valid ROC with its own x[n] (bottom line). A pole <em>inside</em> the ROC's inner edge gives a right-sided term; a pole <em>outside</em> the outer edge gives a left-sided term. The fourth sign pattern (4/3 right-sided, 2/3 left-sided) would need |z| > 4/3 and |z| < 2/3 at once — impossible. Only the middle ROC contains the unit circle (dashed): that is the stable one (Lecture 11).</figcaption></figure>

> [!recipe] "Find all possible ROCs and the corresponding $x[n]$"
> 1. **PFE** (§3): poles $p_k$ and coefficients $A_k$ — done once, shared by every case.
> 2. **List the rings**: sort the distinct pole magnitudes $r_1<\dots<r_M$; the ROCs are $|z|<r_1$, $r_1<|z|<r_2$, …, $|z|>r_M$. Poles of equal magnitude (a conjugate pair, or $\pm a$) share a circle and always go to the same side.
> 3. **For each ring**, apply the inside/outside rule and write $x[n]$.
> 4. **Label** the special ones if asked: $|z|>r_M$ is the causal (right-sided) signal; the ring containing $|z|=1$ is the BIBO-stable one ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]). Never list a pattern whose ring is empty.

> [!trap] Two ways to lose the points
> - **Listing $2^M$ sign patterns.** Only the $M+1$ nested rings are ROCs; "outer pole right-sided, inner pole left-sided" is always empty.
> - **Dropping the minus sign on left-sided terms** — $\frac{A}{1-pz^{-1}}$ with $|z|<|p|$ is $-A\,p^nu[-n-1]$.

> [!question] Practice: [[0-midterm-1/past-exams/fall-2019|FA2019]] #7 and [[homework/hw4|HW4]] #1(a)
> (i) $X(z)=\dfrac{1}{1-e^{j\pi/3}z^{-1}}+\dfrac{1}{1-\frac12z^{-1}}$. $\quad$ (ii) $X(z)=\dfrac{z^2-z}{z^2+3z+2}$. For each, give all possible ROCs and $x[n]$ for each.

> [!success]- Answers
> (i) Already in PFE form; pole radii $1$ and $\tfrac12$.
> - $|z|>1$: $x[n]=e^{j\pi n/3}u[n]+\left(\tfrac12\right)^nu[n]$
> - $\tfrac12<|z|<1$: $x[n]=-e^{j\pi n/3}u[-n-1]+\left(\tfrac12\right)^nu[n]$
> - $|z|<\tfrac12$: $x[n]=-e^{j\pi n/3}u[-n-1]-\left(\tfrac12\right)^nu[-n-1]$
> - ($e^{j\pi/3}$ right-sided with $\tfrac12$ left-sided would need $|z|>1$ and $|z|<\tfrac12$: empty.)
>
> None of the three is BIBO stable: the pole $e^{j\pi/3}$ sits **on** the unit circle, so no ROC can contain $|z|=1$ ([[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]).
>
> (ii) Divide top and bottom by $z^2$: $X(z)=\dfrac{1-z^{-1}}{\left(1+z^{-1}\right)\left(1+2z^{-1}\right)}$, poles $-1$ and $-2$. Cover-up: at $z^{-1}=-1$: $A_1=\dfrac{2}{1-2}=-2$; at $z^{-1}=-\tfrac12$: $A_2=\dfrac{3/2}{1/2}=3$. Check $-2+3=1=b_0$ ✓.
> - $|z|>2$: $x[n]=-2(-1)^nu[n]+3(-2)^nu[n]$
> - $1<|z|<2$: $x[n]=-2(-1)^nu[n]-3(-2)^nu[-n-1]$
> - $|z|<1$: $x[n]=2(-1)^nu[-n-1]-3(-2)^nu[-n-1]$

> [!exam] How Lecture 8 is tested
> "Inverse z / PFE / all possible ROCs" is on **7 of 7** past exams, usually 15–20 points — [[problems/all-possible-rocs|all possible ROCs]]. Typical forms: all ROCs and all signals ([[0-midterm-1/past-exams/fall-2023|FA2023 #6]]: $\frac{1-z^{-1}}{(1-\frac12z^{-1})(1-2z^{-1})}$ with $A=\tfrac13$ at $\tfrac12$ and $\tfrac23$ at $2$; [[0-midterm-1/past-exams/fall-2019|FA2019 #7]] above), or "the system is stable/causal — find $h[n]$", which picks one ring: [[0-midterm-1/past-exams/fall-2025|FA2025 #7]] (stable ⇒ $\tfrac23<|z|<2$, $h[n]=-\tfrac94(-2)^nu[-n-1]-\tfrac54\left(-\tfrac23\right)^nu[n]$), [[0-midterm-1/past-exams/spring-2025|SP2025 #8]] (stable ⇒ $\tfrac12<|z|<\tfrac32$, $h[n]=-\left(\tfrac12\right)^nu[n]-3\left(-\tfrac32\right)^nu[-n-1]$), [[0-midterm-1/past-exams/fall-2024|FA2024 #7]], [[0-midterm-1/past-exams/spring-2023|SP2023 #6]], [[0-midterm-1/past-exams/spring-2021|SP2021 #5, #7]]. Conjugate poles show up as SP2021 #5's $3\sin(\frac\pi2n)u[n]$. Expect to show the cover-up arithmetic; answers must be closed forms with $u[n]$ / $u[-n-1]$ written out.

## 7. Python: `scipy.signal.residuez`

`residuez` does step 1–3 of the recipe numerically for a transform written in powers of $z^{-1}$ (exactly the course's form (1)). Run in this container:

```python
import numpy as np
from scipy.signal import residuez, lfilter

b, a = [2, -1], [1, 2/3, -1/3]          # Example 2: (2 - z^-1)/(1 + (2/3)z^-1 - (1/3)z^-2)
R, P, K = residuez(b, a)
print("R =", R.real, " P =", P.real, " K =", K)

n = np.arange(5)                          # right-sided: x[n] = sum_k R_k P_k^n
x_pfe = (R[:, None] * P[:, None] ** n).sum(axis=0).real
x_div = lfilter(b, a, (n == 0) * 1.0)     # impulse response = long division
print(np.round(x_pfe, 4), np.round(x_div, 4))

R, P, K = residuez([1, 0, -1], [1, -4/3, -4/3])   # improper: numerator degree = denominator degree
print("R =", R.real, " P =", P.real, " K =", K)
```

```text
R = [-0.25  2.25]  P = [ 0.33333333 -1.        ]  K = []
[ 2.     -2.3333  2.2222 -2.2593  2.2469] [ 2.     -2.3333  2.2222 -2.2593  2.2469]
R = [-0.3125  0.5625]  P = [-0.66666667  2.        ]  K = [0.75]
```

How to read it:

- `b`, `a` are the coefficients of $z^0,z^{-1},z^{-2},\dots$ in the numerator and denominator, with `a[0] = 1` — the same lists `lfilter(b, a, x)` uses for the LCCDE (Lecture 9).
- `R` are the $A_k$ and `P` the matching $p_k$, in the same order: here $A=-\tfrac14$ at $p=\tfrac13$ and $A=\tfrac94$ at $p=-1$, as in Example 2.
- `K` holds the **direct terms** $C_0+C_1z^{-1}+\dots$ that appear when $X(z)$ is not proper: $X(z)=\sum_k\frac{R_k}{1-P_kz^{-1}}+\sum_jK_jz^{-j}$. The second call is [[0-midterm-1/past-exams/fall-2025|FA2025 #6]]'s $H(z)=\frac{1-z^{-2}}{(1-2z^{-1})(1+\frac23z^{-1})}$: `K = [0.75]` is a $\tfrac34\delta[n]$ term next to $\frac{9/16}{1-2z^{-1}}$ and $\frac{-5/16}{1+\frac23z^{-1}}$ ([[2-z-transform/10-improper-transfer-functions-and-system-algebra|Lecture 10]]).
- `residuez` knows nothing about the ROC. The line `x_pfe` makes the right-sided choice for every term (and matches `lfilter`, which always computes the causal response); for any other ring you flip the terms whose poles lie outside it, by hand. Complex poles come back as complex conjugate entries of `P` with conjugate `R` — for Exercise 2 both residues are $1.5$.

## Related

- Concepts: [[concepts/inverse-z-transform|inverse z-transform]] · [[concepts/partial-fraction-expansion|partial fraction expansion]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|z-transform pairs]]
- Toolkit: [[0-toolkit/04-factoring-and-long-division|factoring and long division]] · [[0-toolkit/01-complex-numbers|complex numbers]]
- Practice: [[problems/all-possible-rocs|all possible ROCs]] · [[homework/hw3|HW3]] #3–4 · [[homework/hw4|HW4]] #1 · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[demos/python-demos|Python demos]]

### Sources for this page
Snyder, ECE 310 Lecture 8 notes ("Inverse z-transform": §1 common forms, §2 inverse transform, the causal warm-up, Exercises 1–2 and the PFE procedure) and slides of Sep 11, 2026, including the annotated slides for Example 1(a)–(d), Example 2 and Example 3 (the four-pattern ROC table and the three signals). HW3 #3–4 and HW4 #1 with solutions. Past exams FA2025 #6–7, SP2025 #8, FA2023 #6, SP2021 #5, FA2019 #6–7 with keys. Every coefficient and signal on this page was checked numerically (`verify/lectures/l8_verify.py`, 47 checks: `residuez`, `lfilter`, exact fractions, truncated sums inside each ROC); the snippet output above is pasted from a real run.
