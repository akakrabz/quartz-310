---
title: "Lecture 6 — The z-transform and the region of convergence"
description: "Why zⁿ keeps its shape through any LTI system (H(z) = Σ h[k]z⁻ᵏ is its eigenvalue); the z-transform sum and its region of convergence; u[n] vs −u[−n−1] (same X(z), different ROC, different signal); aⁿu[n] and pole-zero plots; finite-length sequences; right-, left- and two-sided ROCs; the table of pairs."
tags: [lecture, midterm-1, z-transform, roc]
lecture: 6
---

*Lecture 6 · Fri Sep 4, 2026 · notes + slides "z-transform" · prev: [[1-signals-and-systems/05-difference-equations-and-block-diagrams|Lecture 5]] · next: [[2-z-transform/07-z-transform-properties|Lecture 7]]*

> [!abstract] In one breath
> Feed an LTI system the exponential $z_0^{\,n}$ (for all $n$) and out comes $H(z_0)\,z_0^{\,n}$: same shape, scaled by the complex number $H(z_0)=\sum_k h[k]z_0^{-k}$. That sum, applied to any signal, is the **z-transform** $X(z)=\sum_n x[n]z^{-n}$. It converges only for some $z$ — the **region of convergence (ROC)** — and the ROC is part of the answer: $u[n]$ and $-u[-n-1]$ have the *same* formula $\frac{1}{1-z^{-1}}$ and differ only in the ROC ($|z|>1$ vs $|z|<1$). Two tools transform almost every exam signal: the geometric series, and the ROC rule "right-sided → outside a circle, left-sided → inside a circle, two-sided → a ring, finite → the whole plane except maybe $0$ or $\infty$".

## 1. Motivation: signals that keep their shape

After Lecture 5 we can compute the output of any LTI system to any input (convolution) and find $h[n]$ for any LCCDE. That still does not tell us *what a system does*: the system $h[n]=(\tfrac12)^n u[n]$ turns $\delta[n]$ into a decaying exponential, and every new input needs a new convolution. So the lecture asks for a class of inputs whose **shape** no LTI system can change — only scale.

Try $x[n]=z_0^{\,n}$ for all $n$, with $z_0$ any complex number (the slide's example: $z_0=1+j2$, a spiral). Because $z_0^{\,n-k}=z_0^{\,n}z_0^{-k}$ splits into an $n$-part and a $k$-part, the convolution sum factors:

$$
\begin{aligned}
y[n]&=\sum_{k=-\infty}^{\infty}h[k]\,x[n-k]=\sum_{k=-\infty}^{\infty}h[k]\,z_0^{\,n-k}\\
&= z_0^{\,n}\underbrace{\sum_{k=-\infty}^{\infty}h[k]\,z_0^{-k}}_{H(z_0)} = H(z_0)\,z_0^{\,n}\qquad\text{for all } n .
\end{aligned}
$$

> [!key] Complex exponentials are eigenfunctions of LTI systems
> $$
> z_0^{\,n}\ \longrightarrow\ \boxed{\text{LTI } h[n]}\ \longrightarrow\ H(z_0)\,z_0^{\,n},\qquad H(z_0)=\sum_{k=-\infty}^{\infty}h[k]\,z_0^{-k}
> $$
> $H(z_0)$ depends only on $h$ and $z_0$ — **not on $n$**. It is the eigenvalue for the eigenfunction $z_0^{\,n}$, and $H(z)$ as a function of $z$ is the system's **transfer function**. Two fine-print conditions: the input must be $z_0^{\,n}$ for **all** $n$ (infinitely long), and the sum defining $H(z_0)$ must converge.

> [!example] One system, three exponentials
> $h[n]=(\tfrac12)^n u[n]$, so $H(z_0)=\sum_{k\ge0}(\tfrac12 z_0^{-1})^k=\dfrac{1}{1-\tfrac12 z_0^{-1}}$ (needs $|z_0|>\tfrac12$).
> - $x[n]=2^n$: $H(2)=\dfrac{1}{1-\frac14}=\dfrac43$, so $y[n]=\tfrac43\,2^n$.
> - $x[n]=1=1^n$: $H(1)=2$, so $y[n]=2$.
> - $x[n]=(-1)^n$: $H(-1)=\dfrac{1}{1+\frac12}=\dfrac23$, so $y[n]=\tfrac23(-1)^n$.
>
> The system doubles a constant and shrinks a fast alternation to $2/3$ of its size — a first glimpse of "low-pass". (All three checked by a direct convolution sum.)

If the input is a sum of exponentials, linearity handles each one separately:

$$
x[n]=\sum_{k=1}^{K}b_k\,z_k^{\,n}\quad\Longrightarrow\quad y[n]=\sum_{k=1}^{K}H(z_k)\,b_k\,z_k^{\,n}.
$$

The annotated slide reads it as a filter: $|H(z_k)|>1$ amplifies the $z_k$ component, $0<|H(z_k)|<1$ attenuates it, $H(z_k)=0$ **removes** it. That last case is the seed of filter design.

> [!trap] $z_0^{\,n}u[n]$ is *not* an eigenfunction
> The derivation used $x[n-k]=z_0^{\,n-k}$ for every $k$. Switch the input on at $n=0$ and a transient appears: with the same $h$, $2^n u[n]\to y[n]=\tfrac43\,2^n u[n]-\tfrac13(\tfrac12)^n u[n]$ — the eigen-part plus a term at the system's own pole $\tfrac12$. One-sided inputs are what the "bounded or unbounded output?" problems use ([[problems/unbounded-outputs-and-pole-matching|pole matching]], Lectures 9–11), so keep the difference in mind.

## 2. The z-transform

> [!key] Definition
> $$
> X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n},\qquad x[n]\ \overset{\mathcal{Z}}{\longleftrightarrow}\ X(z),\qquad z\in\mathbb{C}.
> $$
> The **region of convergence (ROC)** is the set of $z$ for which this sum converges. A **pole** is a $z$ where $X(z)\to\infty$; a **zero** is a $z$ where $X(z)=0$. The transfer function of §1 is exactly the z-transform of the impulse response: $H(z)=\mathcal{Z}\{h[n]\}$.

The course writes transforms in powers of $z^{-1}$ (because $x[n-1]\leftrightarrow z^{-1}X(z)$, Lecture 7) and writes the ROC as "ROC: $|z|>a$". **A z-transform without its ROC is not an answer** — the next section shows why.

> [!intuition] Why every ROC is a disk, a ring, or the outside of a circle
> Write $z=re^{j\omega}$. Then $|x[n]z^{-n}|=|x[n]|\,r^{-n}$: whether the sum converges depends only on $r=|z|$, so the ROC is made of whole circles centred at the origin. For $n\to+\infty$ the factor $r^{-n}$ is small when $r$ is **large** — a right tail wants big $|z|$. For $n\to-\infty$ the factor is $r^{|n|}$, small when $r$ is **small** — a left tail wants small $|z|$. A signal with both tails needs both at once: a ring.

## 3. Same formula, two signals: u[n] and −u[−n−1]

Everything rests on the geometric series (see [[0-toolkit/02-geometric-series|toolkit]]):

$$
\sum_{n=0}^{\infty}a^n=\frac{1}{1-a}\quad\text{if and only if } |a|<1\ \ (\text{otherwise it diverges}).
$$

**Right-sided step.** $u[n]$ is $1$ for $n\ge 0$:

$$
X(z)=\sum_{n=0}^{\infty}z^{-n}=\sum_{n=0}^{\infty}\left(z^{-1}\right)^n=\frac{1}{1-z^{-1}},\qquad |z^{-1}|<1\iff \text{ROC: } |z|>1 .
$$

**Left-sided (negated) step.** $-u[-n-1]$ is $-1$ for $n\le -1$ and $0$ for $n\ge 0$. Substitute $m=-n-1$ (so $n=-1,-2,\dots$ becomes $m=0,1,\dots$):

$$
\begin{aligned}
X(z)&=\sum_{n=-\infty}^{-1}(-1)\,z^{-n}=-\sum_{m=0}^{\infty}z^{m+1}=-z\sum_{m=0}^{\infty}z^{m}\\
&=\frac{-z}{1-z}\cdot\frac{-z^{-1}}{-z^{-1}}=\frac{1}{1-z^{-1}},\qquad \text{ROC: } |z|<1 .
\end{aligned}
$$

> [!key] The z-transform is unique only together with its ROC
> $$
> u[n]\ \longleftrightarrow\ \frac{1}{1-z^{-1}},\ |z|>1 \qquad\qquad -u[-n-1]\ \longleftrightarrow\ \frac{1}{1-z^{-1}},\ |z|<1
> $$
> Same $X(z)$, different ROC $\Rightarrow$ different signal. Always state the ROC. (And the constant $x[n]=1$ for all $n$, which is $u[n]+u[-n-1]$, has **no** z-transform at all: it would need $|z|>1$ and $|z|<1$ at once. [[exams/midterm-1/past-exams/spring-2025|SP2025]] T/F 1c asks exactly this about $e^{j\frac\pi4n}$ for all $n$: its ROC is empty — True.)

> [!trap] The minus sign in $-a^n u[-n-1]$
> The left-sided table entry carries a minus sign: $a^n u[-n-1]$ (no minus) transforms to $-\dfrac{1}{1-az^{-1}}$. Dropping it is the most common sign error in two-sided problems.

## 4. Right-sided exponentials and pole-zero plots

The same computation with $a^n$ inside (the in-class example, $a\in\mathbb{C}$):

$$
X(z)=\sum_{n=0}^{\infty}a^n z^{-n}=\sum_{n=0}^{\infty}\left(\frac{a}{z}\right)^n=\frac{1}{1-az^{-1}},\qquad \left|\frac{a}{z}\right|<1\iff \text{ROC: } |z|>|a| .
$$

Written in positive powers, $\dfrac{1}{1-az^{-1}}=\dfrac{z}{z-a}$: one **pole at $z=a$**, one **zero at $z=0$**, and the ROC is everything outside the pole's circle. Its left-sided partner is $-a^n u[-n-1]\leftrightarrow\dfrac{1}{1-az^{-1}}$ with ROC $|z|<|a|$ (the case $a=1$ is §3).

A **pole-zero plot** shows the z-plane with each zero as ○, each pole as ×, the ROC shaded, and the unit circle $|z|=1$ dashed for reference. The lecture's three examples:

| signal | $X(z)$ | poles | zeros | ROC |
|---|---|---|---|---|
| $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $1$ | $0$ | $\lvert z\rvert>1$ |
| $(-\tfrac13)^n u[n]$ | $\dfrac{1}{1+\frac13 z^{-1}}$ | $-\tfrac13$ | $0$ | $\lvert z\rvert>\tfrac13$ |
| $\cos(\tfrac{2\pi}{3}n)\,u[n]$ | $\dfrac{1+\frac12 z^{-1}}{1+z^{-1}+z^{-2}}$ | $e^{\pm j2\pi/3}$ | $0,\ -\tfrac12$ | $\lvert z\rvert>1$ |

For the cosine, multiply top and bottom by $z^2$: $X(z)=\dfrac{z(z+\frac12)}{z^2+z+1}$, so the zeros are $0$ and $-\tfrac12$ and the poles are the roots of $z^2+z+1$, i.e. $e^{\pm j2\pi/3}$ **on** the unit circle (the ROC starts right at it).

> [!trap] Zeros at $z=0$ hide in the $z^{-1}$ form
> $\dfrac{1-3z^{-1}}{1+\frac16 z^{-1}-\frac13 z^{-2}}=\dfrac{z(z-3)}{z^2+\frac16 z-\frac13}$ has zeros at $3$ **and** $0$ ([[homework/hw3|HW3]] #4). Before listing poles and zeros, rewrite in positive powers of $z$ — the degree difference shows up as poles or zeros at the origin.

## 5. Finite-length sequences

A finite sequence is a sum of shifted impulses, and $\delta[n-k]\leftrightarrow z^{-k}$ (it is $1$ at $n=k$ and the sum picks out $z^{-k}$). So its z-transform is a polynomial you can **read off**:

$$
x[n]=\sum_{k=n_s}^{n_e}x[k]\,\delta[n-k]\ \ \longleftrightarrow\ \ X(z)=\sum_{k=n_s}^{n_e}x[k]\,z^{-k}.
$$

> [!key] ROC of a finite-length signal
> The whole z-plane, except possibly
> - $z=0$ if some sample sits at $n>0$ (a term $z^{-k}$, $k>0$, blows up at $0$), and
> - $z=\infty$ if some sample sits at $n<0$ (a term $z^{|k|}$ blows up at $\infty$).
>
> | signal | $X(z)$ | ROC |
> |---|---|---|
> | $\delta[n]$ | $1$ | all $z$ |
> | $\delta[n]+\delta[n-2]$ | $1+z^{-2}$ | $z\neq 0$ |
> | $\delta[n]+\delta[n+2]$ | $1+z^{2}$ | $\lvert z\rvert<\infty$ |
> | $\delta[n+3]+4\delta[n]-\delta[n-2]$ ([[homework/hw3\|HW3]] #1a) | $z^{3}+4-z^{-2}$ | $0<\lvert z\rvert<\infty$ |

> [!trap] A finite pulse has no pole at $z=1$
> [[exams/midterm-1/past-exams/fall-2025|FA2025]] #5(b): $u[n]-u[n-8]=\{\underset{\uparrow}{1},1,1,1,1,1,1,1\}$ (eight ones, $n=0..7$), so $X(z)=\sum_{k=0}^{7}z^{-k}=\dfrac{1-z^{-8}}{1-z^{-1}}$. The closed form *looks* like it has a pole at $z=1$, but the numerator vanishes there too ($1-1^{-8}=0$): the sum is simply $X(1)=8$. ROC: $z\neq 0$ — **not** $|z|>1$.

## 6. The shape of the ROC: right-, left- and two-sided

Lecture 7 opens by listing these rules; they belong with the definition, so here they are with the in-class examples (annotated slides of Lecture 7). The notes and the annotated slide define "left-sided" as $x[n]=0$ for $n>n_0$; the typed slide's "$n<n_0$" is a typo (see [[0-toolkit/05-errata|errata]]).

> [!key] ROC rules
> 1. The ROC contains **no poles** and is **connected**.
> 2. **Right-sided** ($x[n]=0$ for $n<n_0$): ROC $=|z|>r_{\max}$, outside the circle through the outermost pole. It also contains $z=\infty$ iff $n_0\ge 0$ (causal).
> 3. **Left-sided** ($x[n]=0$ for $n>n_0$): ROC $=|z|<r_{\min}$, inside the circle through the innermost pole. It also contains $z=0$ iff $n_0\le 0$.
> 4. **Two-sided**: ROC $=a<|z|<b$, a ring — the intersection of the right-sided part's ROC and the left-sided part's ROC. **If $a\ge b$ the ring is empty and there is no z-transform.**
> 5. **Finite-length**: all $z$, except possibly $0$ and/or $\infty$ (§5).

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 256" width="640" height="256" role="img" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><path d="M9.0,50.0 h196.0 v176.0 h-196.0 Z M119.0,138.0 A12.0,12.0 0 1,0 95.0,138.0 A12.0,12.0 0 1,0 119.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="107.0" cy="138.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="9.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="9.0" y1="138.0" x2="205.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="107.0" y1="50.0" x2="107.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="107.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="201.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="112.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="126.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="107.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M114.0,133.0 L124.0,143.0 M114.0,143.0 L124.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="119.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><text x="107.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(a) right-sided</text><text x="107.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">(½)ⁿ u[n]</text><text x="107.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| > ½</text><circle cx="320.0" cy="138.0" r="72.0" fill="var(--accent)" fill-opacity="0.20" stroke="var(--accent)" stroke-width="1.6"/><rect x="222.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="222.0" y1="138.0" x2="418.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="320.0" y1="50.0" x2="320.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="320.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="414.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="325.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="339.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="320.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M387.0,133.0 L397.0,143.0 M387.0,143.0 L397.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="392.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">3</text><text x="320.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(b) left-sided</text><text x="320.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">−3ⁿ u[−n−1]</text><text x="320.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: |z| < 3</text><path d="M605.0,138.0 A72.0,72.0 0 1,0 461.0,138.0 A72.0,72.0 0 1,0 605.0,138.0 Z M545.0,138.0 A12.0,12.0 0 1,0 521.0,138.0 A12.0,12.0 0 1,0 545.0,138.0 Z" fill="var(--accent)" fill-opacity="0.20" fill-rule="evenodd" stroke="none"/><circle cx="533.0" cy="138.0" r="12.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><circle cx="533.0" cy="138.0" r="72.0" fill="none" stroke="var(--accent)" stroke-width="1.6"/><rect x="435.0" y="50.0" width="196.0" height="176.0" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.35"/><line x1="435.0" y1="138.0" x2="631.0" y2="138.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><line x1="533.0" y1="50.0" x2="533.0" y2="226.0" stroke="currentColor" stroke-width="1" opacity="0.7"/><circle cx="533.0" cy="138.0" r="24.0" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/><text x="627.0" y="133.0" text-anchor="end" fill="var(--muted)" style="font-size:11px;">Re</text><text x="538.0" y="63.0" text-anchor="start" fill="var(--muted)" style="font-size:11px;">Im</text><text x="552.3" y="117.7" text-anchor="start" fill="var(--muted)" style="font-size:10px;">1</text><circle cx="533.0" cy="138.0" r="5" fill="none" stroke="var(--accent2)" stroke-width="2"/><path d="M540.0,133.0 L550.0,143.0 M540.0,143.0 L550.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="545.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">½</text><path d="M600.0,133.0 L610.0,143.0 M600.0,143.0 L610.0,133.0" stroke="var(--hi)" stroke-width="2.4" stroke-linecap="round"/><text x="605.0" y="156.0" text-anchor="middle" fill="var(--hi)" style="font-size:11px;">3</text><text x="533.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600;">(c) two-sided</text><text x="533.0" y="43.0" text-anchor="middle" fill="currentColor" style="font-size:12px;">(½)ⁿ u[n] + 3ⁿ u[−n−1]</text><text x="533.0" y="243.0" text-anchor="middle" fill="var(--accent)" style="font-size:13px;font-weight:600;">ROC: ½ < |z| < 3</text></svg><figcaption><strong>The ROC's shape is set by which way the signal extends.</strong> Poles are ×, zeros ○, the dashed circle is |z| = 1, the shaded set is the ROC. (a) A right-sided signal converges <em>outside</em> the circle through its outermost pole. (b) A left-sided signal converges <em>inside</em> the circle through its innermost pole. (c) A two-sided signal is a right-sided part plus a left-sided part, so its ROC is the <em>ring</em> where both converge — it exists only if the right-sided part's poles are inside the left-sided part's poles. An ROC never contains a pole.</figcaption></figure>

The slide's examples, worked out:

- $u[n-1]$ is right-sided with $n_0=1$: $X(z)=\sum_{n\ge1}z^{-n}=\dfrac{z^{-1}}{1-z^{-1}}$, ROC $|z|>1$.
- $u[-(n+3)]$ is $1$ for $n\le -3$, left-sided with $n_0=-3$: $X(z)=\sum_{m\ge 3}z^{m}=\dfrac{z^3}{1-z}=\dfrac{-z^{2}}{1-z^{-1}}$, ROC $|z|<1$.
- $(\tfrac12)^n u[n]+3^n u[-n-1]$ is two-sided. The right-sided part needs $|z|>\tfrac12$, the left-sided part $3^n u[-n-1]=-\big(-3^n u[-n-1]\big)$ needs $|z|<3$:

$$
X(z)=\frac{1}{1-\frac12 z^{-1}}-\frac{1}{1-3z^{-1}}=\frac{-\frac52 z^{-1}}{\left(1-\frac12 z^{-1}\right)\left(1-3z^{-1}\right)},\qquad \text{ROC: } \tfrac12<|z|<3 .
$$

Swap which pole goes with which side and the ring disappears: $3^n u[n]+(\tfrac12)^n u[-n-1]$ would need $|z|>3$ **and** $|z|<\tfrac12$, so it has no z-transform. This "which pole is right-sided?" bookkeeping is exactly what the all-possible-ROCs problems of [[2-z-transform/08-inverse-z-transform|Lecture 8]] run backwards.

> [!question] Practice (HW3 #1c, #1d): transform and state the ROC
> (c) $x_3[n]=3^n u[-n]+2^{-n}u[n]$ $\qquad$ (d) $x_4[n]=(\tfrac14)^{|n|}$

> [!success]- Answers
> (c) $3^n u[-n]$ is left-sided (ends at $n=0$): $\sum_{n\le 0}(3z^{-1})^{n}=\sum_{m\ge0}(z/3)^m=\dfrac{1}{1-z/3}$, needs $|z|<3$; $2^{-n}u[n]\leftrightarrow\dfrac{1}{1-\frac12 z^{-1}}$, $|z|>\tfrac12$.
> $X_3(z)=\dfrac{1}{1-\frac13 z}+\dfrac{1}{1-\frac12 z^{-1}}$, ROC $\tfrac12<|z|<3$ (in $z^{-1}$ form $\dfrac{1}{1-\frac13 z}=\dfrac{-3z^{-1}}{1-3z^{-1}}$).
>
> (d) $(\tfrac14)^{|n|}=(\tfrac14)^n u[n]+4^n u[-n-1]$, so $X_4(z)=\dfrac{1}{1-\frac14 z^{-1}}-\dfrac{1}{1-4z^{-1}}$, ROC $\tfrac14<|z|<4$.

## 7. The table of pairs

> [!key] Common z-transform pairs (Table 1 of the notes)
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
> Only the first four need memorizing: the $n\,a^n$ rows follow from the differentiation property ([[2-z-transform/07-z-transform-properties|Lecture 7]]), and the cosine/sine rows from Euler's formula plus the $a^n u[n]$ row ([[2-z-transform/08-inverse-z-transform|Lecture 8]] runs this backwards). Every row was checked against a truncated sum at points inside its ROC.

> [!recipe] z-transform with ROC, by inspection
> 1. **Split** the signal into finite pieces and "exponential × step" pieces; say where each piece lives ($n\ge n_0$ or $n\le n_0$).
> 2. **Finite pieces**: read the coefficients, $x[k]\to x[k]z^{-k}$.
> 3. **Exponential pieces**: match $a^n u[n]\to\frac{1}{1-az^{-1}}$ ($|z|>|a|$) or $a^n u[-n-1]\to-\frac{1}{1-az^{-1}}$ ($|z|<|a|$); if the step is shifted, make the exponent match the step first (time-shift property, [[2-z-transform/07-z-transform-properties|Lecture 7]]), or sum the geometric series directly.
> 4. **ROC** = intersection of all pieces' ROCs, including the $z\neq0$ / $z\neq\infty$ exceptions of finite and shifted pieces. An empty intersection means "no z-transform".

> [!question] Two exam items to try (SP2025 #5b, FA2019 #5b)
> (i) $x[n]=3^n u[-n+2]$. $\qquad$ (ii) $x[n]=e^{-n^2}\,u[n-8]\,u[-n+10]$.

> [!success]- Answers
> (i) Left-sided, ending at $n=2$. With $m=2-n\ge 0$: $\sum_{n\le2}(3z^{-1})^{n}=(3z^{-1})^{2}\sum_{m\ge0}\left(\tfrac{z}{3}\right)^m=\dfrac{9z^{-2}}{1-\frac13 z}$, which needs $|z|<3$; the $n=1,2$ terms put $z^{-1},z^{-2}$ in the sum, so $z=0$ is excluded. $X(z)=\dfrac{9z^{-2}}{1-\frac13 z}=\dfrac{-27z^{-3}}{1-3z^{-1}}$, ROC $0<|z|<3$. ([[exams/midterm-1/past-exams/spring-2025|SP2025]] #5b.)
>
> (ii) The two steps leave only $n=8,9,10$: $X(z)=e^{-64}z^{-8}+e^{-81}z^{-9}+e^{-100}z^{-10}$, ROC $z\neq0$. (The [[exams/midterm-1/past-exams/fall-2019|FA2019]] key writes $e^{-91}$ for $e^{-81}$ and calls the answer $X_d(\omega)$ — both slips, see [[0-toolkit/05-errata|errata]].)

> [!exam] How Lecture 6 is tested
> "Compute the z-transform **and ROC**" is on 6 of 7 past exams, worth 9–15 points — [[problems/z-transform-with-roc|z-transform with ROC]]: [[exams/midterm-1/past-exams/fall-2025|FA2025 #5]] (shifted complex exponential $e^{j\pi n/3}u[n+4]$, the finite pulse above, $\cos^2(\frac{\pi}{4}n)u[n]$), [[exams/midterm-1/past-exams/spring-2025|SP2025 #5]] (a sum of shifted steps, $3^n u[-n+2]$, a two-sided signal with ROC $\frac16<|z|<\frac43$), [[exams/midterm-1/past-exams/fall-2024|FA2024 #5]], [[exams/midterm-1/past-exams/fall-2023|FA2023 #5]], [[exams/midterm-1/past-exams/spring-2021|SP2021 #4]], [[exams/midterm-1/past-exams/fall-2019|FA2019 #5]]. Points go for: a missing ROC, a missing "$z\neq0$" on finite or delayed signals, the sign of left-sided pieces, and forgetting to intersect ROCs. The same-$X(z)$-different-ROC idea returns in every [[problems/all-possible-rocs|all-possible-ROCs]] problem (7/7 exams).

## Related

- Concepts: [[concepts/z-transform|z-transform]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/poles-and-zeros|poles and zeros]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[concepts/sided-sequences|right-, left-, two-sided sequences]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[concepts/transfer-function|transfer function]] · [[concepts/complex-exponential|complex exponential]]
- Toolkit: [[0-toolkit/02-geometric-series|geometric series]] · [[0-toolkit/01-complex-numbers|complex numbers]]
- Practice: [[problems/z-transform-with-roc|z-transform with ROC]] · [[homework/hw3|HW3]] · [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]] · [[supplements/transform-tables|transform tables]]

### Sources for this page
Snyder, ECE 310 Lecture 6 notes ("z-transform", §1 motivation, §2 definition, Exercises 1–2, Table 1, Figure 1) and slides of Sep 4, 2026, including the annotated slides 5–6 (eigenfunction derivation, amplify/attenuate/filter) and 8–9 ($u[n]$, $-u[-n-1]$, $a^nu[n]$). Lecture 7 notes §1 (ROC rules 1–5) and annotated slides 6–7 (finite-length and sided-ROC examples). Lecture 8 notes §1.1 (finite-length form). HW3 #1 and #4. Past exams FA2025 #5, SP2025 #5, FA2019 #5 with their keys. Every transform on this page was checked numerically (`verify/lectures/l6_verify.py`, 53 checks).
