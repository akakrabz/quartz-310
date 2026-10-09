---
title: "Lecture 14 — DTFT properties"
description: "The DTFT is the z-transform on the unit circle when the ROC contains |z| = 1 (2ⁿu[n] has none, u[n] needs an impulse); impulse pairs for periodic signals and the table of common pairs; 2π-periodicity; Hermitian symmetry and how to test real-valuedness from X_d(ω); time and frequency shift, modulation, reversal, conjugation, differentiation (with the table's sign erratum), convolution, windowing and Parseval."
tags: [lecture, midterm-2, dtft]
lecture: 14
---

*Lecture 14 · Fri Sep 25, 2026 · notes + slides "Discrete-time Fourier transform properties" · prev: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] · next: [[3-fourier-analysis/15-frequency-response|Lecture 15]]*

> [!abstract] In one breath
> The DTFT is the z-transform walked around the unit circle: $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ **when the ROC contains $|z|=1$**. When it does not, do not substitute: $2^n u[n]$ has no DTFT at all, and bounded signals that are not summable — $u[n]$ (a pole *on* the unit circle), and $\cos(\omega_0 n)$, $e^{j\omega_0 n}$ for all $n$ (no z-transform at all) — get one only with Dirac impulses, $e^{j\omega_0 n}\leftrightarrow 2\pi\delta(\omega-\omega_0)$. Every DTFT is $2\pi$-periodic, and the DTFT of a **real** signal is **Hermitian**, $X_d(-\omega)=X_d^*(\omega)$: even magnitude, odd phase — and conversely, which is how you decide from $X_d(\omega)$ alone whether $x[n]$ is real. The properties are the z-transform's with $z=e^{j\omega}$ (shift → linear phase, convolution → product), plus three that only make sense in frequency: modulation shifts the spectrum, windowing convolves it, and Parseval measures energy. One sign to fix in the official table: $n\,x[n]\leftrightarrow +j\,\dfrac{dX_d}{d\omega}$.

## 1. The DTFT is the z-transform on the unit circle

[[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] defined the DTFT and its inverse ([[concepts/dtft|DTFT]]),

$$
X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n},\qquad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega ,
$$

and guaranteed it exists when $\sum_n|x[n]|\lt\infty$. The z-transform measures how much of every exponential $z^n$ is in a signal ([[2-z-transform/06-the-z-transform|Lecture 6]]); the DTFT measures how much of every periodic exponential $e^{j\omega n}$ is. The exponentials that are both are $z^n$ with $|z|=1$, so put $z=e^{j\omega}$ into the z-transform sum:

$$
X(z)\Big|_{z=e^{j\omega}}=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}=X_d(\omega).
$$

That is the whole connection, and the reason the textbook writes the DTFT as $X(e^{j\omega})$. (Annotated slide 5: "The DTFT is the z-transform evaluated on the unit circle!")

> [!key] When you may substitute $z=e^{j\omega}$
> $$
> X_d(\omega)=X(z)\Big|_{z=e^{j\omega}}\qquad\text{if the ROC of } X(z) \text{ contains the unit circle } |z|=1 .
> $$
> For an LTI system this closes a loop with [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]: BIBO stable $\iff\sum_n|h[n]|\lt\infty\iff$ the ROC of $H(z)$ contains $|z|=1\iff$ the DTFT sum of $h$ converges **absolutely**. On the unit circle $|z^{-n}|=1$, so "the z-transform converges absolutely there" and "$h$ is absolutely summable" are the same sentence. The word *absolutely* matters: the ideal low-pass $h[n]=\frac{\sin(Wn)}{\pi n}$ has a DTFT (a rectangle, §3) but is not absolutely summable, and is not stable.

| ROC of $X(z)$ | example | DTFT |
|---|---|---|
| contains $\lvert z\rvert=1$ | $(\tfrac12)^n u[n]$, ROC $\lvert z\rvert>\tfrac12$ | substitute: $\dfrac{1}{1-\frac12 e^{-j\omega}}$ |
| misses it (a pole outside, right-sided signal) | $2^n u[n]$, ROC $\lvert z\rvert>2$ | **none**: $\sum_n\lvert x[n]\rvert=\infty$ |
| only touches it (a pole on $\lvert z\rvert=1$) | $u[n]$, ROC $\lvert z\rvert>1$ | only with an impulse: $\dfrac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$ (§2) |
| empty — no z-transform at all | $e^{j\omega_0 n}$ for all $n$ | an impulse: $2\pi\delta(\omega-\omega_0)$ (§2) |

Why keep the z-transform, then? Because it describes a signal against *every* $z$: $2^n u[n]$ has the perfectly good $X(z)=\frac{1}{1-2z^{-1}}$, $|z|>2$, but no DTFT. (The notes' optional linear-algebra view: $X_d(\omega)$ is the inner product of $x$ with $e^{j\omega n}$ — how strongly frequency $\omega$ is present.)

> [!question] Slide 4 — compute the DTFT
> (a) $x[n]=\{1,\underset{\uparrow}{0},0,-1\}$ $\qquad$ (b) $x[n]=a^n u[n]$, $a\in\mathbb{C}$, $|a|\lt1$ $\qquad$ (c) $x[n]=\{\underset{\uparrow}{1},2,3\}$

> [!success]- Answers (the in-class solutions on the annotated slide; checked numerically)
> **(a)** The samples are $x[-1]=1$ and $x[2]=-1$, so $X_d(\omega)=e^{j\omega}-e^{-j2\omega}$. Pull out the phase of the midpoint $n=\tfrac12$ of the two samples:
> $$
> X_d(\omega)=e^{-j\omega/2}\left(e^{j3\omega/2}-e^{-j3\omega/2}\right)=2j\,e^{-j\omega/2}\sin\!\left(\tfrac{3}{2}\omega\right).
> $$
> **(b)** A geometric series in $ae^{-j\omega}$, which has magnitude $|a|\lt1$ for every $\omega$:
> $$
> X_d(\omega)=\sum_{n=0}^{\infty}\left(ae^{-j\omega}\right)^n=\frac{1}{1-ae^{-j\omega}} ,
> $$
> the same as $X(z)=\frac{1}{1-az^{-1}}$ (ROC $|z|>|a|$, which contains the unit circle) at $z=e^{j\omega}$.
>
> **(c)** A finite sequence reads off as a polynomial in $e^{-j\omega}$: $X_d(\omega)=1+2e^{-j\omega}+3e^{-j2\omega}$.

> [!tip] The midpoint trick
> For a pair of samples (or any symmetric pattern), factor out $e^{-j\omega m}$ with $m$ the midpoint: what remains is cosines (equal signs) or $j$ times sines (opposite signs). [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #3 asks for exactly this: $3\delta[n+1]-3\delta[n-7]$ has $X_d=3e^{j\omega}-3e^{-j7\omega}=3e^{-j3\omega}\left(e^{j4\omega}-e^{-j4\omega}\right)=6j\,e^{-j3\omega}\sin(4\omega)$, so $A=6j$, $B=3$, $C=4$ in "$Ae^{-jB\omega}\sin(C\omega)$".

> [!question] Slide 6 (concept check) — do these DTFTs exist?
> $$
> X_1(z)=\frac{1-z^{-1}}{1-\frac12 z^{-1}},\ |z|>\tfrac12 \qquad\qquad X_2(z)=\frac{1+z^{-1}}{1-2z^{-1}-3z^{-2}},\ |z|>2
> $$
> For each: (a) does not exist; (b) replace $z^{-1}$ by $e^{-j\omega}$; (c) replace $z^{-1}$ by $j\omega$.

> [!success]- Answer (the annotated deck has no ink on this slide; checked numerically)
> **$X_1$: (b).** The ROC $|z|>\tfrac12$ contains the unit circle, so $X_1(\omega)=\dfrac{1-e^{-j\omega}}{1-\frac12 e^{-j\omega}}$.
>
> **$X_2$: (a).** Factor first: $1-2z^{-1}-3z^{-2}=(1-3z^{-1})(1+z^{-1})$, and the numerator's zero at $-1$ cancels the pole at $-1$. What is left, $\frac{1}{1-3z^{-1}}$, is the right-sided $3^n u[n]$, whose ROC is $|z|>3$: no unit circle, samples growing like $3^n$, no DTFT. (The slide's "$|z|>2$" cannot be an ROC — it contains the pole $z=3$ — but either way the unit circle is outside it.)
>
> Option (c) is never right: $s=j\Omega$ is the Laplace habit; in discrete time the unit circle is $z=e^{j\omega}$.

> [!trap] Substituting $z=e^{j\omega}$ without looking at the ROC
> "$2^n u[n]\leftrightarrow\frac{1}{1-2z^{-1}}$, $|z|>2$, therefore $X_d(\omega)=\frac{1}{1-2e^{-j\omega}}$" — **False** ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] 1(a)); "a signal with a z-transform always has the finite DTFT $X(e^{j\omega})$" — **False** ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(a), and [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] 1(d)). With a pole *on* the unit circle the formula $H(e^{j\omega})$ is missing an impulse: [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2(c) and [[homework/hw6|HW6]] #5(c) ask "is $H_d(\omega)=H(z)|_{z=e^{j\omega}}$?" for causal systems with a pole on the unit circle (at $-1$ once the pole at $1$ cancels, and at $1$, respectively) — no.

## 2. Periodic signals: impulses in frequency

A periodic signal is never absolutely summable, yet we want its spectrum. Take $x[n]=e^{j\omega_0 n}$: it contains exactly one frequency, so $X_d(\omega)$ should vanish except at $\omega=\omega_0+2\pi k$. The tool is the **Dirac delta** $\delta(\omega)$: zero except at $\omega=0$, with unit area and the sifting property $\int f(\omega)\,\delta(\omega-a)\,d\omega=f(a)$. Parentheses and a continuous argument: it is not the Kronecker $\delta[n]$.

**Finding the constant** (slide 8; no ink there, so here is the notes' argument, eqs. 16–19). Guess $X_d(\omega)=c\,\delta(\omega-\omega_0)$ on one period and invert:

$$
\frac{1}{2\pi}\int_{-\pi}^{\pi}c\,\delta(\omega-\omega_0)\,e^{j\omega n}\,d\omega=\frac{c}{2\pi}\,e^{j\omega_0 n}\stackrel{!}{=}e^{j\omega_0 n}\quad\Longrightarrow\quad c=2\pi .
$$

> [!key] Impulse pairs (one period shown; every one repeats at $\omega+2\pi k$)
> $$
> \begin{aligned}
> e^{j\omega_0 n}&\ \longleftrightarrow\ 2\pi\,\delta(\omega-\omega_0) & 1&\ \longleftrightarrow\ 2\pi\,\delta(\omega)\\
> \cos(\omega_0 n)&\ \longleftrightarrow\ \pi\left[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\right] & u[n]&\ \longleftrightarrow\ \frac{1}{1-e^{-j\omega}}+\pi\,\delta(\omega)\\
> \sin(\omega_0 n)&\ \longleftrightarrow\ -j\pi\left[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\right] & &
> \end{aligned}
> $$
> The cosine and sine rows are Euler's formula applied to the first: $\cos=\frac12(e^{j\omega_0 n}+e^{-j\omega_0 n})$ gives two impulses of area $\pi$; $\sin=\frac{1}{2j}(\cdots-\cdots)$ gives $\frac{2\pi}{2j}=-j\pi$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 215" width="640" height="215" role="img" aria-label="Impulses of area pi at plus and minus pi/3 and at their 2 pi periodic copies" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="322.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) for x[n] = cos(πn/3)</text><rect x="222.7" y="30.0" width="198.7" height="140.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="24.0" y1="170.0" x2="620.0" y2="170.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="322.0" y1="30.0" x2="322.0" y2="170.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="24.0" y1="167.0" x2="24.0" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="24.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="123.3" y1="167.0" x2="123.3" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="123.3" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="222.7" y1="167.0" x2="222.7" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="222.7" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="288.9" y1="167.0" x2="288.9" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="288.9" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/3</text><line x1="355.1" y1="167.0" x2="355.1" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="355.1" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/3</text><line x1="421.3" y1="167.0" x2="421.3" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="421.3" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="520.7" y1="167.0" x2="520.7" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="520.7" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="620.0" y1="167.0" x2="620.0" y2="173.0" stroke="currentColor" stroke-width="1"/><text x="620.0" y="184.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><text x="620.0" y="164.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><line x1="90.2" y1="170.0" x2="90.2" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M85.2,75.7 L90.2,67.7 L95.2,75.7 Z" fill="var(--muted)"/><text x="96.2" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><line x1="156.4" y1="170.0" x2="156.4" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M151.4,75.7 L156.4,67.7 L161.4,75.7 Z" fill="var(--muted)"/><text x="162.4" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><line x1="288.9" y1="170.0" x2="288.9" y2="73.7" stroke="var(--accent)" stroke-width="2"/><path d="M283.9,75.7 L288.9,67.7 L293.9,75.7 Z" fill="var(--accent)"/><text x="294.9" y="71.7" text-anchor="start" fill="var(--accent)" style="font-size:11px">π</text><line x1="355.1" y1="170.0" x2="355.1" y2="73.7" stroke="var(--accent)" stroke-width="2"/><path d="M350.1,75.7 L355.1,67.7 L360.1,75.7 Z" fill="var(--accent)"/><text x="361.1" y="71.7" text-anchor="start" fill="var(--accent)" style="font-size:11px">π</text><line x1="487.6" y1="170.0" x2="487.6" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M482.6,75.7 L487.6,67.7 L492.6,75.7 Z" fill="var(--muted)"/><text x="493.6" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><line x1="553.8" y1="170.0" x2="553.8" y2="73.7" stroke="var(--muted)" stroke-width="2"/><path d="M548.8,75.7 L553.8,67.7 L558.8,75.7 Z" fill="var(--muted)"/><text x="559.8" y="71.7" text-anchor="start" fill="var(--muted)" style="font-size:11px">π</text><text x="226.5" y="41.4" text-anchor="start" fill="var(--accent)" style="font-size:11px">one period</text><text x="226.5" y="52.8" text-anchor="start" fill="var(--accent)" style="font-size:11px">−π ≤ ω ≤ π</text><text x="123.3" y="41.4" text-anchor="middle" fill="var(--muted)" style="font-size:11px">copy (k = −1)</text><text x="520.7" y="41.4" text-anchor="middle" fill="var(--muted)" style="font-size:11px">copy (k = 1)</text></svg><figcaption><strong>A sinusoid's DTFT is a pair of impulses, repeated every 2π.</strong> For x[n] = cos(πn/3) the spectrum is π[δ(ω − π/3) + δ(ω + π/3)] on the shaded period −π ≤ ω ≤ π, and the same pair sits around every multiple of 2π (grey) because every DTFT is 2π-periodic. An arrow's height marks the impulse's <em>area</em> (π), not a function value; between the impulses X<sub>d</sub>(ω) is zero.</figcaption></figure>

> [!derivation]- Where the $\pi\delta(\omega)$ in the $u[n]$ pair comes from
> Split $u[n]=\tfrac12+v[n]$ with $v[n]=u[n]-\tfrac12$ ($+\tfrac12$ for $n\ge0$, $-\tfrac12$ for $n\le-1$). The constant $\tfrac12$ contributes $\tfrac12\cdot2\pi\delta(\omega)=\pi\delta(\omega)$. The rest has no DC (its average is $0$) and satisfies $v[n]-v[n-1]=\delta[n]$, so by the time-shift property $(1-e^{-j\omega})V_d(\omega)=1$:
> $$
> V_d(\omega)=\frac{1}{1-e^{-j\omega}}=\frac12-\frac{j}{2}\cot\frac{\omega}{2},\qquad\omega\neq0 .
> $$
> (Checked by Abel summation, $\sum_n v[n]\,r^{|n|}e^{-j\omega n}$ with $r\to1$, at four frequencies.) Shifting the whole pair in frequency (§5) gives $e^{j\omega_0 n}u[n]\leftrightarrow\frac{1}{1-e^{-j(\omega-\omega_0)}}+\pi\delta(\omega-\omega_0)$ ([[homework/hw6|HW6]] #4b) and $(-1)^n u[n]\leftrightarrow\frac{1}{1+e^{-j\omega}}+\pi\delta(\omega-\pi)$ ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2c).

> [!question] HW5 #1(c): the DTFT of $x[n]=\cos\!\left(\frac{\pi}{3}n+\frac{\pi}{4}\right)$

> [!success]- Answer (matches the official HW5 solution)
> $x[n]=\tfrac12e^{j\pi/4}e^{j\pi n/3}+\tfrac12e^{-j\pi/4}e^{-j\pi n/3}$, so on $-\pi\le\omega\lt\pi$
> $$
> X_d(\omega)=\pi e^{j\pi/4}\,\delta\!\left(\omega-\tfrac{\pi}{3}\right)+\pi e^{-j\pi/4}\,\delta\!\left(\omega+\tfrac{\pi}{3}\right),
> $$
> repeated every $2\pi$. The phase $\theta$ of the cosine rides on the impulses as $e^{\pm j\theta}$ — conjugates of each other, as §4 says they must be for a real signal.

## 3. The table of common pairs

> [!key] Table 1 of the notes, with the conditions under which each pair holds
> | $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ | holds when |
> |---|---|---|
> | $\delta[n]$ | $1$ | always |
> | $u[n]$ | $\dfrac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$ | (pole on $\lvert z\rvert=1$: impulse) |
> | $a^n u[n]$ | $\dfrac{1}{1-ae^{-j\omega}}$ | $\lvert a\rvert\lt1$; none for $\lvert a\rvert>1$ |
> | $e^{j\omega_0 n}$ | $2\pi\delta(\omega-\omega_0)$ | (periodic: impulse) |
> | $\cos(\omega_0 n)$ | $\pi\left[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\right]$ | (impulses) |
> | $\sin(\omega_0 n)$ | $-j\pi\left[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\right]$ | (impulses) |
> | $\mathrm{rect}\!\left(\frac{n-k}{L}\right)$ ($L$ ones centred at $k$) | $\dfrac{\sin(L\omega/2)}{\sin(\omega/2)}\,e^{-j\omega k}$ | $L$ odd (see below) |
> | $\mathrm{sinc}(Ln)=\dfrac{\sin(Ln)}{Ln}$ | $\dfrac{\pi}{L}\,\mathrm{rect}\!\left(\frac{\omega}{2L}\right)$: $\dfrac{\pi}{L}$ for $\lvert\omega\rvert\lt L$, else $0$ | $0\lt L\lt\pi$ |
> | $\mathrm{sinc}^2(Ln)$ | $\dfrac{\pi}{L}\,\Delta\!\left(\frac{\omega}{2L}\right)=\dfrac{\pi}{L}\left(1-\dfrac{\lvert\omega\rvert}{2L}\right)$ for $\lvert\omega\rvert\le2L$ | $0\lt L\le\pi/2$ |
>
> Every entry repeats every $2\pi$. The $\mathrm{sinc}$ row is not absolutely summable (it decays only like $1/n$), yet has a DTFT that converges in energy; that is why the ideal filters of later lectures exist on paper but are not BIBO stable. $\mathrm{sinc}^2$ decays like $1/n^2$ and is an ordinary, absolutely summable pair. More pairs, each checked numerically: [[concepts/dtft-pairs|DTFT pairs]].

Two fine points the table hides (both checked numerically):

- **The rect row needs $L$ odd.** The notes define $\mathrm{rect}\!\left(\frac{n-k}{L}\right)=1$ for $k-\frac L2\lt n\le k+\frac L2$. For odd $L$ that is $k-\frac{L-1}{2},\dots,k+\frac{L-1}{2}$, centred at $k$, and the formula is exact. For even $L$ the ones run from $k-\frac L2+1$ to $k+\frac L2$, centred at $k+\frac12$, and the DTFT carries an extra $e^{-j\omega/2}$. Lecture 13's one-sided pulse ($1$ for $0\le n\lt L$) is centred at $\frac{L-1}{2}$: $e^{-j\omega(L-1)/2}\frac{\sin(L\omega/2)}{\sin(\omega/2)}$.
- **The $\mathrm{sinc}^2$ row needs $L\le\pi/2$.** The triangle has half-width $2L$; if $2L>\pi$ its $2\pi$-periodic copies overlap and the true DTFT is their sum.

> [!trap] Two different sincs
> The course writes $\mathrm{sinc}(x)=\dfrac{\sin x}{x}$. NumPy's `np.sinc(x)` and the official transform tables ([[supplements/transform-tables|transform tables]]) use $\dfrac{\sin(\pi x)}{\pi x}$. The ideal low-pass pair is the same object in both: $\dfrac{\sin(Wn)}{\pi n}\leftrightarrow1$ for $|\omega|\le W$ is $\dfrac{W}{\pi}\mathrm{sinc}(Wn)$ in the course's notation. The exam keys use the course's ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #7, [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #2).

## 4. Periodicity and Hermitian symmetry

**$2\pi$-periodicity** holds for every DTFT, finite or infinite signal, real or complex:

$$
X_d(\omega+2\pi k)=\sum_n x[n]\,e^{-j\omega n}\underbrace{e^{-j2\pi kn}}_{=1}=X_d(\omega),\qquad k\in\mathbb{Z}.
$$

So one period carries all the information; by convention it is $-\pi\le\omega\le\pi$, where the symmetry below is easiest to see.

**Hermitian symmetry.** Write $x[n]=\mathrm{Re}\{x[n]\}+j\,\mathrm{Im}\{x[n]\}$ and $e^{-j\omega n}=\cos(\omega n)-j\sin(\omega n)$. For a real signal the real part of $X_d$ is built from cosines (even in $\omega$) and the imaginary part from sines (odd in $\omega$), which is the whole proof.

> [!key] Real signal $\iff$ Hermitian DTFT
> $$
> x[n]\ \text{real}\quad\Longleftrightarrow\quad X_d(-\omega)=X_d^*(\omega)\ \text{ for all }\omega\quad\Longleftrightarrow\quad |X_d(-\omega)|=|X_d(\omega)|\ \text{and}\ \angle X_d(-\omega)=-\angle X_d(\omega).
> $$
> Magnitude even, phase odd (and $\mathrm{Re}\,X_d$ even, $\mathrm{Im}\,X_d$ odd). Slide 11 stresses it is **if and only if**: a Hermitian $X_d$ always comes from a real $x$. Consequences you use constantly: $X_d(0)$ and $X_d(\pi)$ are **real** for real $x$ (because $X_d(\pi)=X_d(-\pi)=X_d^*(\pi)$); real and even $x$ ⇒ $X_d$ real and even; real and odd $x$ ⇒ $X_d$ purely imaginary and odd; purely imaginary $x$ ⇒ $X_d(-\omega)=-X_d^*(\omega)$.

> [!derivation]- The real and imaginary parts (notes eqs. 26–33)
> $$
> \begin{aligned}
> \mathrm{Re}\{X_d(\omega)\}&=\sum_n \mathrm{Re}\{x[n]\}\cos(\omega n)+\mathrm{Im}\{x[n]\}\sin(\omega n),\\
> \mathrm{Im}\{X_d(\omega)\}&=\sum_n \mathrm{Im}\{x[n]\}\cos(\omega n)-\mathrm{Re}\{x[n]\}\sin(\omega n).
> \end{aligned}
> $$
> With $\mathrm{Im}\{x[n]\}=0$ the first line is even in $\omega$ and the second odd, so $X_d(-\omega)=\mathrm{Re}\,X_d(\omega)-j\,\mathrm{Im}\,X_d(\omega)=X_d^*(\omega)$. (The notes' eq. 27 has a lower limit "$n=\infty$"; read $-\infty$.)

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" aria-label="Magnitude and phase of the DTFT of 0.8^n u[n] and of its frequency-shifted complex version" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="174.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)|</text><line x1="34.0" y1="186.1" x2="314.0" y2="186.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="152.1" x2="314.0" y2="152.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="118.2" x2="314.0" y2="118.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="84.3" x2="314.0" y2="84.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="50.4" x2="314.0" y2="50.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="220.0" x2="314.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="174.0" y1="30.0" x2="174.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="34.0" y1="217.0" x2="34.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="34.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="104.0" y1="217.0" x2="104.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="104.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="174.0" y1="217.0" x2="174.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="174.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="244.0" y1="217.0" x2="244.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="244.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="314.0" y1="217.0" x2="314.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="314.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="171.0" y1="186.1" x2="177.0" y2="186.1" stroke="currentColor" stroke-width="1"/><text x="30.0" y="190.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="171.0" y1="152.1" x2="177.0" y2="152.1" stroke="currentColor" stroke-width="1"/><text x="30.0" y="156.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="171.0" y1="118.2" x2="177.0" y2="118.2" stroke="currentColor" stroke-width="1"/><text x="30.0" y="122.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">3</text><line x1="171.0" y1="84.3" x2="177.0" y2="84.3" stroke="currentColor" stroke-width="1"/><text x="30.0" y="88.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">4</text><line x1="171.0" y1="50.4" x2="177.0" y2="50.4" stroke="currentColor" stroke-width="1"/><text x="30.0" y="54.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">5</text><text x="314.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="34.0,199.6 53.1,200.9 78.1,201.1 98.9,200.1 119.9,197.7 132.7,195.2 145.1,191.6 156.3,186.7 165.4,180.8 170.3,176.5 174.5,171.9 180.1,163.9 185.0,154.4 189.9,141.2 193.4,128.5 196.9,112.1 205.7,58.8 207.1,53.3 207.8,51.5 208.8,50.4 209.5,50.5 210.2,51.5 212.3,58.8 220.4,108.4 223.2,122.4 226.7,136.5 230.2,147.4 233.0,154.4 237.2,162.7 241.4,169.2 247.0,175.8 252.6,180.8 260.1,185.8 268.0,189.7 276.2,192.7 286.2,195.4 298.1,197.7 314.0,199.6" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="34.0,201.2 52.2,200.8 69.7,199.6 87.9,197.2 101.7,194.2 111.7,191.0 121.3,186.7 130.4,180.8 137.4,174.3 143.0,167.2 147.2,160.2 151.4,151.0 155.6,138.9 159.1,125.5 162.6,108.4 170.7,58.8 172.1,53.3 172.8,51.5 173.8,50.4 174.5,50.5 175.2,51.5 177.3,58.8 185.4,108.4 188.9,125.5 192.4,138.9 196.6,151.0 200.8,160.2 205.0,167.2 210.6,174.3 217.6,180.8 226.7,186.7 236.3,191.0 246.3,194.2 260.1,197.2 278.3,199.6 295.8,200.8 314.0,201.2" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><line x1="209.0" y1="30.0" x2="209.0" y2="220.0" stroke="var(--accent2)" stroke-width="0.8" stroke-dasharray="2 3"/><text x="500.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="370.0" y1="220.0" x2="630.0" y2="220.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="172.5" x2="630.0" y2="172.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="77.5" x2="630.0" y2="77.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="30.0" x2="630.0" y2="30.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="125.0" x2="630.0" y2="125.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="500.0" y1="30.0" x2="500.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="370.0" y1="122.0" x2="370.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="370.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="435.0" y1="122.0" x2="435.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="435.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="500.0" y1="122.0" x2="500.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="500.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="565.0" y1="122.0" x2="565.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="565.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="630.0" y1="122.0" x2="630.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="497.0" y1="220.0" x2="503.0" y2="220.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="224.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="497.0" y1="172.5" x2="503.0" y2="172.5" stroke="currentColor" stroke-width="1"/><text x="366.0" y="176.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="497.0" y1="77.5" x2="503.0" y2="77.5" stroke="currentColor" stroke-width="1"/><text x="366.0" y="81.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="497.0" y1="30.0" x2="503.0" y2="30.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="34.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/2</text><text x="630.0" y="119.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="370.0,146.0 439.5,101.1 467.9,83.9 477.2,78.8 488.7,73.3 497.4,70.2 504.8,68.9 510.6,69.5 515.0,71.6 519.1,75.9 522.8,82.7 525.6,90.9 528.0,100.5 535.5,142.1 539.6,159.8 542.2,167.3 544.6,172.1 547.2,175.8 551.1,179.1 555.7,180.8 561.5,181.0 567.6,179.8 576.3,176.7 587.8,171.2 597.1,166.1 630.0,146.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="370.0,125.0 409.4,99.6 439.5,81.6 449.9,76.2 458.2,72.5 466.4,69.8 472.3,68.9 475.5,69.0 478.8,69.7 483.1,72.1 486.6,75.9 490.5,83.2 493.1,90.9 495.7,101.5 503.2,143.2 507.1,159.8 509.5,166.8 513.6,174.4 517.5,178.4 521.2,180.3 524.5,181.0 527.7,181.1 533.6,180.2 543.8,176.7 553.5,172.1 567.2,164.6 586.9,152.7 630.0,125.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="40" y="250" fill="var(--accent)" style="font-size:12px">━ real: 0.8ⁿu[n]</text><text x="250" y="250" fill="var(--accent2)" style="font-size:12px">╌ complex: e<tspan baseline-shift="super" style="font-size:75%">jπn/4</tspan>·0.8ⁿu[n]</text></svg><figcaption><strong>Real signal ⇒ even magnitude, odd phase.</strong> Solid: x[n] = 0.8ⁿu[n], X<sub>d</sub>(ω) = 1/(1 − 0.8e<sup>−jω</sup>). Its magnitude is a mirror image about ω = 0 (5 at ω = 0, 5/9 at ω = ±π) and its phase is point-symmetric (extremes ±arcsin 0.8 ≈ ±53°). Dashed: the complex signal e<sup>jπn/4</sup>·0.8ⁿu[n]; by the frequency-shift property its DTFT is the solid curve moved right by π/4 (peak at the dotted line), which is neither even nor odd — a complex signal owes no symmetry.</figcaption></figure>

> [!recipe] Is $x[n]$ real? Decide from $X_d(\omega)$
> 1. Use the formula on the **whole** period $-\pi\le\omega\le\pi$ (Hermitian symmetry relates $\omega$ to $-\omega$).
> 2. Compute $X_d(-\omega)$ and $X_d^*(\omega)$ (conjugating flips every $j$; $\omega$ is real and stays). Equal for all $\omega$ ⇒ real; different anywhere ⇒ complex.
> 3. Shortcut in polar form $X_d=M(\omega)e^{j\Phi(\omega)}$ with $M\ge0$: real $\iff$ $M$ even and $\Phi$ odd (mod $2\pi$). A sign hidden in a factor like $\omega$ is phase: $\omega=|\omega|e^{j\pi}$ for $\omega\lt0$.
> 4. Quick necessary checks: $X_d(0)$ and $X_d(\pi)$ must be real.

> [!question] Slide 12 — $X_d(\omega)=\omega^2 e^{j\cos\omega}$ (on $-\pi\le\omega\le\pi$). Is $x[n]$ real-valued?

> [!success]- Answer (no ink on this slide; checked by computing $x[n]$ numerically)
> **No.** The magnitude $\omega^2$ is even, as it should be, but the phase $\cos\omega$ is **even**, not odd:
> $$
> X_d(-\omega)=\omega^2e^{j\cos\omega}\qquad\text{but}\qquad X_d^*(\omega)=\omega^2e^{-j\cos\omega},
> $$
> which differ wherever $\cos\omega\neq0$. So $x[n]$ is complex. In fact $X_d(-\omega)=X_d(\omega)$ says $x$ is *even*, $x[-n]=x[n]$: the inverse DTFT gives $x[0]\approx2.403-1.752j$ and $x[\pm1]\approx-1.276+1.656j$.

> [!question] Slide 13 (concept check) — $x[n]$ is real. Which are true?
> (a) $X_d(0)=X_d(2\pi)$ $\quad$ (b) $X_d(\frac{\pi}{3})=X_d(-\frac{\pi}{3})$ $\quad$ (c) $X_d(\frac{\pi}{3})=X_d^*(-\frac{\pi}{3})$ $\quad$ (d) $X_d(\pi)=X_d(7\pi)$ $\quad$ (e) $X_d(\frac{2\pi}{3})=X_d^*(\frac{4\pi}{3})$

> [!success]- Answer: (a), (c), (d), (e) (checked on a random real signal)
> (a) periodicity. (b) **not in general**: Hermitian symmetry equates the *magnitudes* at $\pm\frac{\pi}{3}$; the values are conjugates, equal only if $X_d(\frac{\pi}{3})$ happens to be real. (c) Hermitian symmetry itself. (d) $7\pi=\pi+3\cdot2\pi$. (e) both properties at once: $\frac{4\pi}{3}=-\frac{2\pi}{3}+2\pi$, so $X_d(\frac{4\pi}{3})=X_d(-\frac{2\pi}{3})=X_d^*(\frac{2\pi}{3})$; conjugate both sides.

> [!question] Two exam items to try (SP2023 MT2 #2–#3, FA2019 MT2 #6)
> (i) $x[n]$ is real and $X_d(\omega)=j\omega$ for $0\le\omega\le\pi$. What is $X_d(\omega)$ for $-\pi\le\omega\le0$? And if $x[n]$ is arbitrary, what is $X_d(\omega)$ for $2\pi\le\omega\le3\pi$?
> (ii) $x[n]$ has $X_d(\omega)=e^{-j\omega^2/3}$ and is the input to the LTI system $h[n]=(\frac13)^n u[n]$. Can the output be real?

> [!success]- Answers
> (i) For $-\pi\le\omega\le0$: $X_d(\omega)=X_d^*(-\omega)=\left(j(-\omega)\right)^*=j\omega$ — the same formula, so $X_d(\omega)=j\omega$ on the whole period (option (c) of [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #2). For $2\pi\le\omega\le3\pi$ only periodicity applies: $X_d(\omega)=X_d(\omega-2\pi)=j(\omega-2\pi)$, which is none of the offered options (#3, answer (e)).
>
> (ii) **No.** $X_d^*(\omega)=e^{j\omega^2/3}$ but $X_d(-\omega)=e^{-j\omega^2/3}$, so $x$ is complex. The output has $Y_d=X_dH_d$ with $H_d$ Hermitian (real $h$) and never zero ($|H_d(\omega)|\ge\frac34$); if $Y_d$ were Hermitian, so would be $X_d=Y_d/H_d$. Hence $y$ is complex ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #6). The key's shorter "x complex ⇒ y complex" needs that $H_d$ never vanishes: a filter that zeroes the offending frequencies could return a real output.

## 5. The properties table

> [!key] DTFT properties (Table 2 of the notes, sign corrected)
> | property | signal | DTFT | inherited from the z-transform? |
> |---|---|---|---|
> | linearity | $a\,x_1[n]+b\,x_2[n]$ | $aX_1(\omega)+bX_2(\omega)$ | yes |
> | time shift | $x[n-k]$, $k\in\mathbb{Z}$ | $e^{-j\omega k}X_d(\omega)$ | $z^{-k}X(z)$ |
> | frequency shift | $e^{j\omega_0 n}x[n]$ | $X_d(\omega-\omega_0)$ | $a^n x[n]\leftrightarrow X(z/a)$, $a=e^{j\omega_0}$ |
> | modulation | $x[n]\cos(\omega_0 n)$ | $\tfrac12X_d(\omega-\omega_0)+\tfrac12X_d(\omega+\omega_0)$ | Euler + frequency shift |
> | time reversal | $x[-n]$ | $X_d(-\omega)$ | $X(1/z)$ |
> | conjugation | $x^*[n]$ | $X_d^*(-\omega)$ | $X^*(z^*)$ |
> | differentiation | $n\,x[n]$ | $+j\,\dfrac{dX_d(\omega)}{d\omega}$ ⚠ | $-z\,\dfrac{dX}{dz}$ |
> | convolution | $x[n]*h[n]$ | $X_d(\omega)H_d(\omega)$ | $X(z)H(z)$ |
> | windowing | $x[n]\,w[n]$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}X_d(\theta)W_d(\omega-\theta)\,d\theta$ | DTFT only |
> | Hermitian symmetry | $x[n]$ real | $X_d^*(\omega)=X_d(-\omega)$ | — |
> | Parseval | $\sum_n\lvert x[n]\rvert^2$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$ | DTFT only |
>
> Full table with proofs and traps: [[concepts/dtft-properties|DTFT properties]].

> [!warning] Erratum — the differentiation row
> The notes' Table 2 and slide 15 print $n\,x[n]\leftrightarrow-j\,\dfrac{dX_d(\omega)}{d\omega}$. The correct sign is $+j$. Differentiate the definition term by term:
> $$
> \frac{dX_d}{d\omega}=\sum_n x[n]\cdot(-jn)\,e^{-j\omega n}=-j\sum_n n\,x[n]e^{-j\omega n}\quad\Longrightarrow\quad\sum_n n\,x[n]e^{-j\omega n}=j\,\frac{dX_d}{d\omega}.
> $$
> Check with $a^n u[n]$: $j\frac{d}{d\omega}\frac{1}{1-ae^{-j\omega}}=\frac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$, which is the z-domain pair $n\,a^nu[n]\leftrightarrow\frac{az^{-1}}{(1-az^{-1})^2}$ on the unit circle; the table's $-j$ gives its negative. The official transform tables print $+j$. Listed on [[0-toolkit/05-errata|errata]].

**Time shift.** A delay multiplies by $e^{-j\omega k}$: the magnitude is untouched and the phase gains the straight line $-\omega k$. That slope is the seed of group delay ([[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]). It needs an **integer** $k$: $e^{-j\omega/2}$ on $-\pi\le\omega\le\pi$ is not "$\delta[n-\frac12]$" ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(b), False) but the shifted sinc $\frac{\sin(\pi(n-\frac12))}{\pi(n-\frac12)}$, the same family as [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #5 and [[homework/hw6|HW6]] #3(b).

**Frequency shift and modulation.** Multiplying by $e^{j\omega_0 n}$ slides the whole spectrum by $\omega_0$ (the dashed curve in the figure above). The proof is one line: $\sum_n x[n]e^{j\omega_0 n}e^{-j\omega n}=\sum_n x[n]e^{-j(\omega-\omega_0)n}$. A real cosine is two exponentials, so $x[n]\cos(\omega_0 n)$ makes **two half-height copies** at $\pm\omega_0$, the principle behind AM radio. Copies that run past $\pm\pi$ come back in from the other side, because the spectrum is periodic.

> [!question] Two exam items to try (FA2024 MT2 #2, SP2025 MT2 #2)
> (i) $X_d(\omega)=1$ for $\frac{\pi}{2}\le|\omega|\le\pi$ and $0$ for $|\omega|\lt\frac{\pi}{2}$ (a high-pass). Find a real $x[n]$ by writing $X_d$ as a low-pass shifted to $\pm\frac{3\pi}{4}$.
> (ii) $X_d(\omega)=1$ for $|\omega|\le\frac{\pi}{3}$, $0$ elsewhere in $[-\pi,\pi]$. Sketch the DTFTs of $y[n]=x[n]\cos(\frac{2\pi}{5}n)$ and $v[n]=x[n]\cos^2(\frac{2\pi}{5}n)$.

> [!success]- Answers (checked numerically)
> (i) The band $\frac{\pi}{2}\le\omega\le\pi$ is a width-$\frac{\pi}{2}$ block centred at $\frac{3\pi}{4}$, so $X_d(\omega)=Y_d(\omega-\frac{3\pi}{4})+Y_d(\omega+\frac{3\pi}{4})$ with $Y_d=1$ on $|\omega|\le\frac{\pi}{4}$. The sinc pair gives $y[n]=\frac{\sin(\pi n/4)}{\pi n}=\frac14\mathrm{sinc}(\frac{\pi}{4}n)$, and modulation ($2\cos$ makes two full copies):
> $$
> x[n]=2\cos\!\left(\tfrac{3\pi}{4}n\right)y[n]=\tfrac12\cos\!\left(\tfrac{3\pi}{4}n\right)\mathrm{sinc}\!\left(\tfrac{\pi}{4}n\right).
> $$
> The key also accepts $\delta[n]-\frac12\mathrm{sinc}(\frac{\pi}{2}n)$ (all-pass minus low-pass) and $(-1)^n\frac12\mathrm{sinc}(\frac{\pi}{2}n)$ (a low-pass shifted by $\pi$); all three are the same sequence.
>
> (ii) $Y_d(\omega)=\frac12X_d(\omega-\frac{2\pi}{5})+\frac12X_d(\omega+\frac{2\pi}{5})$: height $\frac12$ on $\frac{\pi}{15}\le|\omega|\le\frac{11\pi}{15}$. Since $\cos^2\theta=\frac12+\frac12\cos2\theta$, $V_d(\omega)=\frac12X_d(\omega)+\frac14X_d(\omega-\frac{4\pi}{5})+\frac14X_d(\omega+\frac{4\pi}{5})$. The copy at $\frac{4\pi}{5}$ covers $\frac{7\pi}{15}$ to $\frac{17\pi}{15}$, beyond $\pi$, so periodicity folds its tail onto $-\pi\le\omega\le-\frac{13\pi}{15}$, where it meets the mirror copy:
>
> <figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 330" width="640" height="330" role="img" aria-label="Spectra of x[n] cos(2 pi n/5) and x[n] cos squared (2 pi n/5) for the SP2025 problem" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="325.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">Y<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω), y[n] = x[n] cos(2πn/5)</text><line x1="30.0" y1="50.3" x2="620.0" y2="50.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="30.0" y1="135.0" x2="620.0" y2="135.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="325.0" y1="30.0" x2="325.0" y2="135.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="30.0" y1="132.0" x2="30.0" y2="138.0" stroke="currentColor" stroke-width="1"/><text x="30.0" y="149.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="108.7" y1="132.0" x2="108.7" y2="138.0" stroke="currentColor" stroke-width="1"/><text x="108.7" y="149.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−11π/15</text><line x1="305.3" y1="132.0" x2="305.3" y2="138.0" stroke="currentColor" stroke-width="1"/><text x="305.3" y="149.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/15</text><line x1="344.7" y1="132.0" x2="344.7" y2="138.0" stroke="currentColor" stroke-width="1"/><text x="344.7" y="149.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/15</text><line x1="541.3" y1="132.0" x2="541.3" y2="138.0" stroke="currentColor" stroke-width="1"/><text x="541.3" y="149.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">11π/15</text><line x1="620.0" y1="132.0" x2="620.0" y2="138.0" stroke="currentColor" stroke-width="1"/><text x="620.0" y="149.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="322.0" y1="50.3" x2="328.0" y2="50.3" stroke="currentColor" stroke-width="1"/><text x="26.0" y="54.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">½</text><text x="620.0" y="129.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="108.7,135.0 108.7,50.3 305.3,50.3 305.3,135.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="344.7,135.0 344.7,50.3 541.3,50.3 541.3,135.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="207.0" y="45.2" text-anchor="middle" fill="var(--muted)" style="font-size:10px">centre −2π/5</text><text x="443.0" y="45.2" text-anchor="middle" fill="var(--muted)" style="font-size:10px">centre 2π/5</text><text x="325.0" y="189.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">V<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω), v[n] = x[n] cos²(2πn/5)</text><line x1="30.0" y1="257.7" x2="620.0" y2="257.7" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="30.0" y1="215.3" x2="620.0" y2="215.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="30.0" y1="300.0" x2="620.0" y2="300.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="325.0" y1="195.0" x2="325.0" y2="300.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="30.0" y1="297.0" x2="30.0" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="30.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="69.3" y1="297.0" x2="69.3" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="69.3" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−13π/15</text><line x1="187.3" y1="297.0" x2="187.3" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="187.3" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−7π/15</text><line x1="226.7" y1="297.0" x2="226.7" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="226.7" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/3</text><line x1="423.3" y1="297.0" x2="423.3" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="423.3" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/3</text><line x1="462.7" y1="297.0" x2="462.7" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="462.7" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">7π/15</text><line x1="580.7" y1="297.0" x2="580.7" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="580.7" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">13π/15</text><line x1="620.0" y1="297.0" x2="620.0" y2="303.0" stroke="currentColor" stroke-width="1"/><text x="620.0" y="314.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="322.0" y1="257.7" x2="328.0" y2="257.7" stroke="currentColor" stroke-width="1"/><text x="26.0" y="261.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">¼</text><line x1="322.0" y1="215.3" x2="328.0" y2="215.3" stroke="currentColor" stroke-width="1"/><text x="26.0" y="219.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">½</text><polyline points="30.0,300.0 30.0,215.3 69.3,215.3 69.3,257.7 187.3,257.7 187.3,300.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="226.7,300.0 226.7,215.3 423.3,215.3 423.3,300.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="462.7,300.0 462.7,257.7 580.7,257.7 580.7,215.3 620.0,215.3 620.0,300.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><rect x="580.7" y="195.0" width="39.3" height="105.0" fill="var(--accent2)" fill-opacity="0.18" stroke="none"/><rect x="30.0" y="195.0" width="39.3" height="105.0" fill="var(--accent2)" fill-opacity="0.18" stroke="none"/><text x="599.4" y="205.2" text-anchor="middle" fill="var(--accent2)" style="font-size:10px">overlap</text><text x="50.6" y="205.2" text-anchor="middle" fill="var(--accent2)" style="font-size:10px">overlap</text></svg><figcaption><strong>Modulation shifts copies; periodicity wraps them.</strong> Top: Y<sub>d</sub>(ω) = ½X<sub>d</sub>(ω − 2π/5) + ½X<sub>d</sub>(ω + 2π/5), two half-height copies of the rectangle |ω| ≤ π/3. Bottom: V<sub>d</sub>(ω) = ½X<sub>d</sub>(ω) + ¼X<sub>d</sub>(ω − 4π/5) + ¼X<sub>d</sub>(ω + 4π/5). The copy centred at 4π/5 spans 7π/15 … 17π/15, past π; its overhang reappears at −π … −13π/15 (and the copy at −4π/5 wraps to 13π/15 … π), so the shaded edges carry ¼ + ¼ = ½.</figcaption></figure>

**Time reversal and conjugation.** $x[-n]\leftrightarrow X_d(-\omega)$ (substitute $m=-n$) and $x^*[n]\leftrightarrow X_d^*(-\omega)$ (conjugate the sum; the $-\omega$ appears because $e^{-j\omega n}$ is conjugated too). Together, $x^*[-n]\leftrightarrow X_d^*(\omega)$ ([[homework/hw6|HW6]] #2). Hermitian symmetry is just "$x=x^*$" read through the conjugation row.

**Convolution** carries over from the z-transform: $x*h\leftrightarrow X_dH_d$. With $h$ the impulse response of an LTI system, $H_d(\omega)$ is its **frequency response**, the subject of [[3-fourier-analysis/15-frequency-response|Lecture 15]].

**Windowing** is the mirror image: multiplying in time convolves in frequency, over one period and divided by $2\pi$ (proof in the notes, eqs. 47–51). Multiplying by a fixed $w[n]$ is **not** an LTI operation. HW5 #1(d) uses it with $g[n]=e^{j\omega_0 n}$, $G_d=2\pi\delta(\omega-\omega_0)$: the convolution integral collapses by sifting to the frequency-shift property, $\alpha^n e^{j\omega_0 n}u[n]\leftrightarrow\frac{1}{1-\alpha e^{-j(\omega-\omega_0)}}$.

**Parseval** says energy can be counted in either domain: $\sum_n|x[n]|^2=\frac{1}{2\pi}\int_{-\pi}^{\pi}|X_d(\omega)|^2d\omega$. Together with three evaluations of the definitions it lets you read numbers off $X_d$ without ever computing it:

> [!recipe] Four numbers without computing $X_d(\omega)$
> $$
> X_d(0)=\sum_n x[n],\qquad X_d(\pi)=\sum_n(-1)^n x[n],\qquad \int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0],\qquad \int_{-\pi}^{\pi}|X_d(\omega)|^2d\omega=2\pi\sum_n|x[n]|^2 .
> $$
> The first two set $\omega=0$ and $\omega=\pi$ ($e^{-j\pi n}=(-1)^n$) in the DTFT; the third sets $n=0$ in the inverse DTFT; the fourth is Parseval. [[homework/hw5|HW5]] #2 ($x=\{2,-1,\underset{\uparrow}{1},-1,2\}$) gives $3$, $7$, $2\pi$, $22\pi$; the HW5 rubric gives less than half credit for computing $X_d(\omega)$ first.

> [!question] FA2019 MT2 #3 and SP2023 MT1 #9
> (i) $x[n]=\delta[n+3]-3\delta[n+2]+5\delta[n+1]-7\delta[n]+5\delta[n-1]-3\delta[n-2]+\delta[n-3]$: find $X_d(0)$, $X_d(\pi)$ and $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$.
> (ii) $\{x[n]\}_{n=-1}^{2}=\{1-j,\ 1,\ -1-j,\ 2j\}$: find $X_d(0)$ and $X_d(\frac{\pi}{2})$.

> [!success]- Answers (checked numerically)
> (i) $X_d(0)=1-3+5-7+5-3+1=-1$. For $X_d(\pi)$ flip the signs at odd $n$: $-1-3-5-7-5-3-1=-25$. $\int X_d=2\pi x[0]=-14\pi$ ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #3).
>
> (ii) $X_d(0)=(1-j)+1+(-1-j)+2j=1$. With $e^{-j\pi n/2}=(-j)^n$: $X_d(\frac{\pi}{2})=(1-j)(j)+1+(-1-j)(-j)+(2j)(-1)=(1+j)+1+(-1+j)-2j=1$ ([[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #9, from a term when the DTFT came before the first midterm). The signal is complex, so nothing forces these values to be real; they happen to be.

The same four numbers in Python, together with a check of the differentiation sign, using the course demo's `DTFT(x, n0, w)` convention:

```python
import numpy as np

def dtft(x, n0, w):
    """X_d(w) = sum_n x[n] e^{-jwn}; the first entry of x sits at n = n0 (as in the course demo)."""
    n = n0 + np.arange(len(x))
    return np.exp(-1j * np.outer(w, n)) @ x

x, n0 = np.array([2, -1, 1, -1, 2.0]), -2        # HW5 #2: x[-2..2], with x[0] = 1
w = 2 * np.pi * np.arange(64) / 64 - np.pi        # 64 equally spaced frequencies covering one period
X = dtft(x, n0, w)
print("X_d(0), X_d(pi)  :", X[32].real, X[0].real)           # w[32] = 0, w[0] = -pi
print("int X_d dw / pi  :", round((2 * np.pi * X.mean()).real / np.pi, 12))
print("int |X_d|^2 / pi :", round(2 * np.pi * np.mean(abs(X) ** 2) / np.pi, 12), "  2*sum|x|^2 =", 2 * np.sum(x ** 2))

n = n0 + np.arange(len(x))
d = 1e-5
dX = (dtft(x, n0, w + d) - dtft(x, n0, w - d)) / (2 * d)    # dX_d/dw by a central difference
Y = dtft(n * x, n0, w)                                      # the DTFT of n x[n]
print("max|DTFT{n x} - (+j dX/dw)|:", np.abs(Y - 1j * dX).max())
print("max|DTFT{n x} - (-j dX/dw)|:", np.abs(Y + 1j * dX).max())
```

```text
X_d(0), X_d(pi)  : 3.0 7.0
int X_d dw / pi  : 2.0
int |X_d|^2 / pi : 22.0   2*sum|x|^2 = 22.0
max|DTFT{n x} - (+j dX/dw)|: 5.421609827749307e-10
max|DTFT{n x} - (-j dX/dw)|: 18.828427124237763
```

The integrals are exact here: for a finite sequence $X_d$ is a trigonometric polynomial, and averaging one over $N$ equally spaced frequencies is exact once $N$ exceeds its highest power of $e^{\pm j\omega}$. The last two lines settle the sign: $+j$ agrees to rounding error, $-j$ misses by twice the size of the transform.

## 6. How this lecture is tested

> [!exam] How Lecture 14 is tested (Midterm 2)
> - **Does the DTFT exist, and is it $X(e^{j\omega})$?** True/false on most exams: [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] 1(a) (F, $2^nu[n]$), [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(a) (F), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] 1(d) (F); impulses for poles on the unit circle in [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2(c) and [[homework/hw6|HW6]] #4–#5; [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #6(a) ("computed easily from the z-transform when absolutely summable": the DTFT).
> - **Periodicity and symmetry:** [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] 1(b) (T: finite signals have periodic DTFTs too), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(b) and 1(e) (F, F: copies at $2\pi$; every DTFT is periodic), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #2–#3, [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(c) (T), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] 1(e) (T: $|X_d|$ even for real $x$), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #6 (can the output be real?).
> - **Numbers without $X_d$:** [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #3, [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #2 ($u[n+2]-u[n-3]$: $X_d(0)=5$, $X_d(\pi)=1$), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #9, [[homework/hw5|HW5]] #2.
> - **Pairs and properties in a computation:** [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #3 (midpoint trick) and #7 (sinc pair: $A_1=\frac13$, $A_2=\frac23$, $\omega_0=\frac{\pi}{3}$), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8 (which sequence has $X_d=1+2\cos2\omega-2j\sin4\omega$: $\{-1,0,1,0,\underset{\uparrow}{1},0,1,0,1\}$), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #2 and [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #2 (modulation), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #4 (sifting an impulse: $\frac{5}{2\pi}e^{j\omega_0(\pi+n)}$).
>
> Method and more instances: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].

## Related

- Concepts: [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/frequency-response|frequency response]] · [[concepts/region-of-convergence|region of convergence]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/bibo-stability|BIBO stability]] · [[concepts/complex-exponential|complex exponential]]
- Lectures: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] (the DTFT) · [[3-fourier-analysis/15-frequency-response|Lecture 15]] (frequency response) · [[3-fourier-analysis/index|Unit 3]]
- Practice: [[homework/hw5|HW5]] · [[homework/hw6|HW6]] · [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]] · [[supplements/transform-tables|transform tables]] · [[0-toolkit/02-geometric-series|geometric series]]

### Sources for this page

Snyder, ECE 310 Lecture 14 notes ("Discrete-time Fourier transform properties": §1 DTFT and the z-transform, §1.1, §2 DTFT of periodic signals with Table 1, §3 properties with Table 2) and slides of Sep 25, 2026. The annotated ("Complete") deck has ink only on slides 4–5 (the three DTFT computations and "the DTFT is the z-transform on the unit circle"); the answers to slides 6, 8, 12 and 13 are worked out here and verified numerically. HW5 #1–#2 with the official solutions; HW6 #2–#5 (no official solutions yet). Past exams: FA2024 MT2 #1, #2; FA2023 MT2 #1, #2; SP2023 MT2 #2–#4; SP2025 MT2 #2; SP2021 MT2 #3, #6, #7; FA2021 MT2 #2; FA2019 MT2 #1, #3, #5, #6; SP2023 MT1 #1, #8, #9 — with their keys. `transform_tables.pdf` Table 5 (the $+j$ sign). Every number and claim above is checked in `verify/LB_l14.py` (96 checks); the figures come from `verify/LB_figs.py`.
