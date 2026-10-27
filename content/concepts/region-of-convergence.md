---
title: "Region of convergence (ROC)"
description: "The set of z where the z-transform sum converges: a ring bounded by pole radii that makes X(z) unique and decides causality and BIBO stability; all possible ROCs of one X(z)."
tags: [concept, z-transform, roc, stability]
aliases: ["ROC", "region of convergence", "all possible ROCs"]
---

*Lectures 6 (Fri Sep 4), 7 (Wed Sep 9) §1, 8 (Fri Sep 11) and 11 (Fri Sep 18) §1.1 · [[homework/hw3|HW3]] #1, [[homework/hw4|HW4]] #1 · families: [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/all-possible-rocs|all possible ROCs]]*

> [!abstract] In one breath
> - The ROC is part of $X(z)$: outside it the transform is undefined, even where the formula returns a number.
> - No poles, connected; right-sided → outside the largest pole, left-sided → inside the smallest, two-sided → a ring.
> - $M$ distinct pole radii → $M+1$ candidate ROCs, each a different $x[n]$; the one containing $\lvert z\rvert=1$ is stable, the outermost is causal.

## 1. Definition

> [!key] Definition (Lecture 6 §2)
> The ROC of $X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n}$ is the set of $z$ where the sum converges: a **ring**
> $$
> r_1 < \lvert z\rvert < r_2, \qquad 0 \le r_1 < r_2 \le \infty ,
> $$
> possibly with $z=0$ or $z=\infty$. Formula **plus** ROC is one signal: $u[n]$ and $-u[-n-1]$ share $\dfrac{1}{1-z^{-1}}$ ($\lvert z\rvert>1$ vs $\lvert z\rvert<1$).

**Undefined outside the ROC** (Lecture 7, eqs. 2–5). $x[n]=(\tfrac12)^nu[n]\leftrightarrow X(z)=\frac{1}{1-\frac12z^{-1}}$, $\lvert z\rvert>\tfrac12$. At $z=\tfrac14$ the formula gives $\frac{1}{1-\frac12\cdot4}=-1$, but the sum is $\sum_{n\ge0}(\tfrac12)^n(\tfrac14)^{-n}=\sum_{n\ge0}2^n$: divergent, consistent with $z=\tfrac14$ outside the ROC.

## 2. ROC rules

> [!key] ROC rules (Lecture 7 §1)
> 1. Zeros: $X(z)=0$. Poles: $X(z)\to\infty$. The ROC contains **no poles**; zeros allowed.
> 2. The ROC is **connected**.
> 3. Infinite-length: **right-sided** ($x[n]=0$ for $n<n_0$) $\Rightarrow \lvert z\rvert>a$; **left-sided** ($x[n]=0$ for $n>n_0$) $\Rightarrow \lvert z\rvert<a$; **two-sided** $\Rightarrow a<\lvert z\rvert<b$ ([[concepts/sided-sequences|sided sequences]]).
> 4. Finite-length: whole plane, except perhaps $z=0$ (causal) or $z=\infty$ (non-causal). $\delta[n]+\delta[n-1]\leftrightarrow1+z^{-1}$, $\lvert z\rvert>0$; $\delta[n+1]+\delta[n]\leftrightarrow z+1$, $\lvert z\rvert<\infty$; their sum: $0<\lvert z\rvert<\infty$.
> 5. Rational $X(z)$: right-sided starting at $n\ge0$ → $\lvert z\rvert>\lvert p_{\max}\rvert$; left-sided ending at $n\le-1$ → $\lvert z\rvert<\lvert p_{\min}\rvert$. (Typed slide 7 writes "left-sided: $x[n]=0,\ n<n_0$"; read $n>n_0$ — [[0-toolkit/05-errata|errata]].)
>
> **Stable $\iff$ ROC contains $\lvert z\rvert=1$. Causal $\iff$ ROC is outside a circle and includes $z=\infty$** (Lecture 11, §4 below).

> [!question] Lecture 7, Example 1 (slides): ROC of $X(z)=\dfrac{1+3z^{-1}}{1+\frac74z^{-1}-\frac12z^{-2}}$ if $x[n]$ is right-sided? Left-sided?

> [!success]- Answer
> Roots of $z^2+\tfrac74z-\tfrac12$:
> $$
> z=\frac{-\frac74\pm\sqrt{\frac{49}{16}+\frac{32}{16}}}{2}=\frac{-\frac74\pm\frac94}{2}=\tfrac14,\ -2 .
> $$
> $X(z)=\dfrac{z(z+3)}{\left(z-\frac14\right)(z+2)}$; zeros $0$, $-3$ play no role.
> - Right-sided: $\lvert z\rvert>2$. Left-sided: $\lvert z\rvert<\tfrac14$. Two-sided: $\tfrac14<\lvert z\rvert<2$.
>
> With the PFE $X(z) = \dfrac{-\frac49}{1+2z^{-1}} + \dfrac{\frac{13}{9}}{1-\frac14 z^{-1}}$, the three signals:
> - $\lvert z\rvert>2$ (causal, unstable): $x[n] = -\tfrac49(-2)^n u[n] + \tfrac{13}{9}\left(\tfrac14\right)^n u[n]$.
> - $\lvert z\rvert<\tfrac14$ (anti-causal, unstable): $x[n] = \tfrac49(-2)^n u[-n-1] - \tfrac{13}{9}\left(\tfrac14\right)^n u[-n-1]$.
> - $\tfrac14<\lvert z\rvert<2$ (two-sided, stable): $x[n] = \tfrac{13}{9}\left(\tfrac14\right)^n u[n] + \tfrac49(-2)^n u[-n-1]$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 270" width="660" height="270" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:14px"><defs><marker id="ahroc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs><clipPath id="rocout"><rect x="23.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M23.0,18.0 h184.0 v184.0 h-184.0 Z M141.00,110.00 A26.00,26.00 0 1,0 89.00,110.00 A26.00,26.00 0 1,0 141.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocout)"/><circle cx="115.0" cy="110.0" r="26.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="23.0" y1="110.0" x2="207.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="115.0" y1="18.0" x2="115.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="115.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="109.0" y1="78.0" x2="121.0" y2="90.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="90.0" x2="121.0" y2="78.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="130.0" x2="121.0" y2="142.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="109.0" y1="142.0" x2="121.0" y2="130.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="205.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="121.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="115.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(a) causal: |z| &gt; ½</text><text x="115.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">h = (½)ⁿ cos(πn/2) u[n]</text><clipPath id="rocin"><rect x="238.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M408.00,110.00 A78.00,78.00 0 1,0 252.00,110.00 A78.00,78.00 0 1,0 408.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocin)"/><circle cx="330.0" cy="110.0" r="78.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="238.0" y1="110.0" x2="422.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="330.0" y1="18.0" x2="330.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="330.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="402.0" y1="104.0" x2="414.0" y2="116.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="402.0" y1="116.0" x2="414.0" y2="104.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="420.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="336.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="330.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(b) left-sided: |z| &lt; 3/2</text><text x="330.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">h = −(3/2)ⁿ u[−n−1]</text><clipPath id="rocann"><rect x="453.0" y="18.0" width="184.0" height="184.0"/></clipPath><path d="M623.00,110.00 A78.00,78.00 0 1,0 467.00,110.00 A78.00,78.00 0 1,0 623.00,110.00 Z M571.00,110.00 A26.00,26.00 0 1,0 519.00,110.00 A26.00,26.00 0 1,0 571.00,110.00 Z" fill="var(--accent)" fill-opacity="0.22" fill-rule="evenodd" stroke="none" clip-path="url(#rocann)"/><circle cx="545.0" cy="110.0" r="26.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><circle cx="545.0" cy="110.0" r="78.0" fill="none" stroke="var(--accent)" stroke-width="1.4"/><line x1="453.0" y1="110.0" x2="637.0" y2="110.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><line x1="545.0" y1="18.0" x2="545.0" y2="202.0" stroke="currentColor" stroke-width="1.1" opacity="0.8" stroke-linecap="round"/><circle cx="545.0" cy="110.0" r="52.0" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="539.0" y1="78.0" x2="551.0" y2="90.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="90.0" x2="551.0" y2="78.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="130.0" x2="551.0" y2="142.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="539.0" y1="142.0" x2="551.0" y2="130.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="617.0" y1="104.0" x2="629.0" y2="116.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><line x1="617.0" y1="116.0" x2="629.0" y2="104.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="635.0" y="135.0" text-anchor="end" fill="var(--muted)" style="font-size:12px;">Re</text><text x="551.0" y="31.0" text-anchor="start" fill="var(--muted)" style="font-size:12px;">Im</text><text x="545.0" y="224.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-weight:600;">(c) two-sided: ½ &lt; |z| &lt; 3/2</text><text x="545.0" y="242.0" text-anchor="middle" fill="var(--muted)" style="font-size:13px;">sum of (a) and (b)</text></svg><figcaption><strong>The three ROC shapes (Lecture 11, Fig. 2).</strong> (a) causal: outside the largest pole; (b) left-sided: inside the smallest pole; (c) their sum: the annulus, here containing the unit circle, so stable.</figcaption></figure>

## 3. All possible ROCs of one X(z) (Lecture 8)

[[concepts/partial-fraction-expansion|PFE]] ignores the ROC; the ROC enters only at inversion. Each $\frac{A_k}{1-p_kz^{-1}}$ has two inverses ($\lvert z\rvert>\lvert p_k\rvert$ or $\lvert z\rvert<\lvert p_k\rvert$), and the ROC of $X$ lies inside every term's ROC.

> [!key] Reading the sides off the ROC $r_1<\lvert z\rvert<r_2$ (Lecture 8 slides, Example 3)
> - Pole **inside** the inner circle ($\lvert p_k\rvert\le r_1$): **right-sided** $A_k\,p_k^n\,u[n]$.
> - Pole **outside** the outer circle ($\lvert p_k\rvert\ge r_2$): **left-sided** $-A_k\,p_k^n\,u[-n-1]$.
> - $M$ distinct pole radii → $M+1$ candidate ROCs, from $\lvert z\rvert<r_{\min}$ (all left) to $\lvert z\rvert>r_{\max}$ (all right).

> [!question] Lecture 8, Example 3 (slides): all possible ROCs of $X(z)=\dfrac{1}{\left(1-\frac43z^{-1}\right)\left(1-\frac23z^{-1}\right)}$ and each $x[n]$

> [!success]- Answer
> $1=A_1\left(1-\tfrac23z^{-1}\right)+A_2\left(1-\tfrac43z^{-1}\right)$. $z=\tfrac43$: $1=\tfrac12A_1$, $A_1=2$. $z=\tfrac23$: $1=A_2(1-2)$, $A_2=-1$. So $X(z)=\dfrac{2}{1-\frac43z^{-1}}-\dfrac{1}{1-\frac23z^{-1}}$.
>
> | | $\tfrac23$ right-sided ($\lvert z\rvert>\tfrac23$) | $\tfrac23$ left-sided ($\lvert z\rvert<\tfrac23$) |
> |---|---|---|
> | $\tfrac43$ right-sided ($\lvert z\rvert>\tfrac43$) | $\lvert z\rvert>\tfrac43$ | empty |
> | $\tfrac43$ left-sided ($\lvert z\rvert<\tfrac43$) | $\tfrac23<\lvert z\rvert<\tfrac43$ | $\lvert z\rvert<\tfrac23$ |
>
> 1. $\lvert z\rvert>\tfrac43$: $x_1[n]=2\left(\tfrac43\right)^nu[n]-\left(\tfrac23\right)^nu[n]$
> 2. $\tfrac23<\lvert z\rvert<\tfrac43$ (stable): $x_2[n]=-2\left(\tfrac43\right)^nu[-n-1]-\left(\tfrac23\right)^nu[n]$
> 3. $\lvert z\rvert<\tfrac23$: $x_3[n]=-2\left(\tfrac43\right)^nu[-n-1]+\left(\tfrac23\right)^nu[-n-1]$
> 4. $\tfrac43$ right, $\tfrac23$ left: no $z$ works; unbounded as $n\to\pm\infty$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M9.0,50.0 h196.0 v168.0 h-196.0 Z M171.0,134.0 A64.0,64.0 0 1,0 43.0,134.0 A64.0,64.0 0 1,0 171.0,134.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="107.0" cy="134.0" r="64.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="9.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="9.0" y1="134.0" x2="205.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="107.0" y1="50.0" x2="107.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="107.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="201.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="112.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="143.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="107.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="100.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M166.0,129.0 L176.0,139.0 M166.0,139.0 L176.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="171.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M134.0,129.0 L144.0,139.0 M134.0,139.0 L144.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="139.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="107.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| > 4/3</text><text x="107.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms right-sided</text><text x="107.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">2(4/3)ⁿ u[n]</text><text x="107.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">− (2/3)ⁿ u[n]</text><path d="M384.0,134.0 A64.0,64.0 0 1,0 256.0,134.0 A64.0,64.0 0 1,0 384.0,134.0 Z M352.0,134.0 A32.0,32.0 0 1,0 288.0,134.0 A32.0,32.0 0 1,0 352.0,134.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="320.0" cy="134.0" r="32.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="320.0" cy="134.0" r="64.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="222.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="222.0" y1="134.0" x2="418.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="320.0" y1="50.0" x2="320.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="320.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="414.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="325.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="356.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="320.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="313.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M379.0,129.0 L389.0,139.0 M379.0,139.0 L389.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="384.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M347.0,129.0 L357.0,139.0 M347.0,139.0 L357.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="352.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="320.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">2/3 < |z| < 4/3</text><text x="320.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">4/3 left-sided, 2/3 right-sided</text><text x="320.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">−2(4/3)ⁿ u[−n−1]</text><text x="320.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">− (2/3)ⁿ u[n]</text><circle cx="533.0" cy="134.0" r="32.0" fill="var(--accent)" fill-opacity="0.20" stroke="var(--accent)" stroke-width="1.6"/><rect x="435.0" y="50.0" width="196.0" height="168.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="435.0" y1="134.0" x2="631.0" y2="134.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="533.0" y1="50.0" x2="533.0" y2="218.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="533.0" cy="134.0" r="48.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="627.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="538.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="569.6" y="96.4" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="533.0" cy="134.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><text x="526.0" y="127.0" text-anchor="end" fill="var(--accent2)" style="font-size:11px;">2</text><path d="M592.0,129.0 L602.0,139.0 M592.0,139.0 L602.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="597.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">4/3</text><path d="M560.0,129.0 L570.0,139.0 M560.0,139.0 L570.0,129.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="565.0" y="152.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">2/3</text><text x="533.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">|z| < 2/3</text><text x="533.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">both terms left-sided</text><text x="533.0" y="235.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">−2(4/3)ⁿ u[−n−1]</text><text x="533.0" y="251.0" text-anchor="middle" fill="var(--accent)" style="font-size:12.5px;font-weight:600;">+ (2/3)ⁿ u[−n−1]</text></svg><figcaption><strong>One X(z), three signals (Example 3).</strong> Each ring between the pole circles 2/3 and 4/3 is a valid ROC with its own x[n]; the fourth sign pattern would need |z| &gt; 4/3 and |z| &lt; 2/3 at once.</figcaption></figure>

> [!recipe] "Find all possible ROCs and the corresponding $x[n]$"
> 1. PFE once: $p_k$, $A_k$.
> 2. Sort distinct pole radii $r_1<\dots<r_M$; ROCs: $\lvert z\rvert<r_1$, $r_1<\lvert z\rvert<r_2$, …, $\lvert z\rvert>r_M$. Equal-radius poles (conjugate pair, $\pm a$) go to the same side.
> 3. Per ring: inside/outside rule → $x[n]$.
> 4. If asked: $\lvert z\rvert>r_M$ is causal; the ring containing $\lvert z\rvert=1$ is stable.

## 4. ROC shape ⇔ causality ⇔ stability (Lecture 11)

> [!key] Lecture 11, Table 1
> | ROC of $H(z)$ | causality type | right-sided | left-sided | BIBO stable iff |
> |---|---|---|---|---|
> | $\lvert z\rvert > \lvert p_{\max}\rvert$ | causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
> | $\lvert z\rvert < \lvert p_{\min}\rvert$ | anti-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
> | $\lvert p_{\max}\rvert < \lvert z\rvert < \infty$ | non-causal | ✓ | ✗ | $\lvert p_{\max}\rvert < 1$ |
> | $0 < \lvert z\rvert < \lvert p_{\min}\rvert$ | non-causal | ✗ | ✓ | $\lvert p_{\min}\rvert > 1$ |
> | $a < \lvert z\rvert < b$ | non-causal (two-sided) | ✓ | ✓ | $a = \lvert p_{\max,h_r}\rvert < 1$ and $b = \lvert p_{\min,h_l}\rvert > 1$ |
>
> **Causal: stable iff all poles inside the unit circle; anti-causal: iff all outside; two-sided: iff the unit circle runs through the ring.** $p_{\max}$, $p_{\min}$: largest/smallest-magnitude **finite** poles; the ROC stops at the first pole. Details: [[concepts/bibo-stability|BIBO stability]], [[concepts/causality|causality]].

> [!trap]
> - Every z-transform answer needs its ROC; every inverse needs the ROC to choose each term's side.
> - Poles on the same circle ($\pm j/2$) go to the same side; listing $2^M$ sign patterns is wrong, only $M+1$ rings exist.
> - Right-sided is not causal: $\delta[n+1]+\delta[n]\leftrightarrow z+1$, ROC $\lvert z\rvert<\infty$.
> - After [[concepts/pole-zero-cancellation|pole-zero cancellation]] the ROC can be larger than $R_1\cap R_2$; an everlasting $e^{j\pi n/4}$ has an **empty** ROC.
> - $X_d(\omega)=X(e^{j\omega})$ only when the ROC contains $\lvert z\rvert=1$ ([[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #1(d)).

> [!exam] All possible ROCs: 7 of 7 past exams, 15–20 points
> All ROCs and signals, or "stable/causal — find $h[n]$" (one ring); ROC True/False items.
> [[exams/midterm-1/past-exams/fall-2025|FA2025 #7]] · [[exams/midterm-1/past-exams/spring-2025|SP2025 #8]] · [[exams/midterm-1/past-exams/fall-2024|FA2024 #7]] · [[exams/midterm-1/past-exams/fall-2023|FA2023 #6]] · [[exams/midterm-1/past-exams/spring-2023|SP2023 #6]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #5, #7]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #6, #7]] · family: [[problems/all-possible-rocs|all possible ROCs]]

**Where it appears:** [[2-z-transform/06-the-z-transform|L6]] §2, [[2-z-transform/07-z-transform-properties|L7]] §1 (eqs. 1–5, Example 1), [[2-z-transform/08-inverse-z-transform|L8]] (Example 3), [[2-z-transform/11-bibo-stability-and-causality|L11]] §1.1 (Table 1, Fig. 2); [[problems/z-transform-with-roc|z-transform with ROC]], [[problems/all-possible-rocs|All possible ROCs (inverse z by partial fractions)]], [[problems/parameters-for-stability|Parameters for stability]]; [[homework/hw3|HW3]], [[homework/hw4|HW4]] #1; [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]].

## Related
[[concepts/z-transform]] · [[concepts/poles-and-zeros]] · [[concepts/sided-sequences]] · [[concepts/bibo-stability]] · [[concepts/causality]] · [[concepts/inverse-z-transform]] · [[concepts/partial-fraction-expansion]]

### Sources for this page
Lecture 6 §2; Lecture 7 §1 (eqs. 1–5) and slides Example 1; Lecture 8 slides (Example 3, annotated ROC table); Lecture 11 §1.1 (Table 1, Fig. 2); Lecture 14 §1; past exams above.
