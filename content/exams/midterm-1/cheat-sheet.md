---
title: "Midterm 1 cheat sheet"
description: "Draft for your one handwritten two-sided Midterm 1 sheet: signal basics, property tests, convolution, LTI facts, LCCDE ⇄ H(z), z-transform pairs and properties, ROC ⇔ causality/stability, PFE, unbounded outputs."
tags: [midterm-1, exam]
---

*Midterm 1 · reference page · one handwritten two-sided 8.5″×11″ sheet allowed; copy what you need by hand. Order follows the exam: properties → convolution → z-transforms → LCCDE → PFE → stability.*

## 1. Signal basics

| item | rule |
|---|---|
| impulse | $\delta[n] = 1$ at $n = 0$, else $0$; $\;\delta[n] = u[n]-u[n-1]$ |
| step | $u[n] = 1$ for $n \ge 0$, else $0$; $\;u[n] = \sum_{k=0}^{\infty}\delta[n-k]$; $\;u[3-n] = 1$ for $n \le 3$ |
| sifting | $x[n]\,\delta[n-n_0] = x[n_0]\,\delta[n-n_0]$ and $\sum_n x[n]\,\delta[n-n_0] = x[n_0]$ |
| decomposition | $x[n] = \sum_k x[k]\,\delta[n-k]$ — every signal is a sum of scaled, shifted impulses |
| windows | $u[n]-u[n-N]$ = ones on $0,\dots,N-1$; $\;u[n-a]\,u[b-n]$ = ones on $a,\dots,b$ (FA24 #5b: $u[n-1]u[3-n] = \delta[n-1]+\delta[n-2]+\delta[n-3]$) |
| sifting trap | $\sum_n x[n]\,\delta[2^n u[n]-8] = x[3]$: the impulse fires where its **argument** is $0$ (FA19 #1g) |

**Shifts and reversal.** $x[n-n_0]$, $n_0>0$: delay (right). $x[-n+n_0] = x[-(n-n_0)]$: flip, then shift right by $n_0$; $x[0]$ lands at $n = n_0$.

**Complex numbers.** $e^{j\theta} = \cos\theta + j\sin\theta$, $\;\cos\theta = \dfrac{e^{j\theta}+e^{-j\theta}}{2}$, $\;\sin\theta = \dfrac{e^{j\theta}-e^{-j\theta}}{2j}$, $\;\lvert e^{j\theta}\rvert = 1$; $a + jb = re^{j\theta}$, $r = \sqrt{a^2+b^2}$; $e^{j7\pi/3} = e^{j\pi/3}$. $e^{j\pi} = -1$, $e^{\pm j\pi/2} = \pm j$, $j^n = e^{j\pi n/2}$, $(-1)^n = e^{j\pi n} = \cos(\pi n)$, $\cos^2\theta = \tfrac12 + \tfrac14 e^{j2\theta} + \tfrac14 e^{-j2\theta}$.

**Roots.** $z^N = 1 \iff z = e^{j2\pi k/N}$, $k = 0,\dots,N-1$ (equally spaced on the unit circle); $z^N = c \iff z = \lvert c\rvert^{1/N}e^{j(\angle c+2\pi k)/N}$. Example: $1 + z^{-2} = 0 \iff z = \pm j$. Also $\sum_{k=0}^{N-1} e^{j2\pi km/N} = N$ if $N$ divides $m$, else $0$.

**Geometric sums:**

$$
\begin{gathered}
\sum_{n=0}^{N-1} a^n = \begin{cases}\dfrac{1-a^N}{1-a}, & a\neq 1\\[4pt] N, & a = 1\end{cases}
\qquad
\sum_{n=N_1}^{N_2} a^n = \frac{a^{N_1}-a^{N_2+1}}{1-a}
\\[6pt]
\sum_{n=0}^{\infty} a^n = \frac{1}{1-a},\qquad \sum_{n=0}^{\infty} n\,a^n = \frac{a}{(1-a)^2}\qquad(\lvert a\rvert<1)
\end{gathered}
$$

## 2. System properties — tests and fast rules

| property | test | fails when you see … | holds even with … |
|---|---|---|---|
| [[concepts/linearity\|linear]] | $T\{ax_1+bx_2\} = aT\{x_1\}+bT\{x_2\}$; quick necessary check $T\{0\} = 0$ | an **additive constant** ($x[n]+3$, $2x[\lvert n\rvert]+10$); a nonlinear function of $x$: $x^2$, $\lvert x\rvert$, $e^{x}$, $\log x$, $\sin x$, $x[n]x[n+1]$, $x[3]\,x[n]$, $x[n]/x[2]$, clipping, median | coefficients depending on $n$ ($\lvert n\rvert x[n]$, $\cos^2(\tfrac{\pi}{2}n)\,x[n]$); index warps $x[\lvert n\rvert]$, $x[2n]$; any convolution |
| [[concepts/time-invariance\|time-invariant]] | compare $y[n-n_0]$ (replace **every** $n$) with $T\{x[n-n_0]\}$ (shift only inside $x$) | **$n$ outside the brackets** ($n\,x[n]$, $\cos(\tfrac{\pi(n-2)}{3})x[n]$, $(0.8+0.8j)^n x[n]$); index warps $x[2n]$, $x[-n]$, $x[\lvert n\rvert]$, $x[\lvert n\rvert+n]$; fixed samples $x[0]$, $x[2]$, $x[3]$ | constant coefficients + shifts; maps with no explicit $n$ and only fixed shifts ($\lvert x[n]-x[n-1]\rvert$, $e^{x[n]+1}$, $x[n]+3$); convolution with a fixed $h$ (e.g. $x[n]*2^nu[-n]$) |
| [[concepts/causality\|causal]] | $y[n]$ uses only $x[m]$ with $m \le n$, **for every $n$** | a future sample; a warp that looks ahead at **negative $n$** ($x[\lvert n\rvert]$ at $n=-3$ needs $x[3]$; $x[-n]$, $x[\lvert n\rvert+n]$); a warp that looks ahead at positive $n$ ($x[2n]$, $n\,x[3n]$); a fixed later sample ($x[2]$ at $n = 0$) | LTI: causal ⇔ $h[n] = 0$ for $n<0$ ($x*2^nu[-n]$ and $x*u[n+1]$ are not) |
| [[concepts/bibo-stability\|BIBO stable]] | every bounded input gives a bounded output | growing coefficients ($n\,x[n]$, $\log(\lvert n\rvert+1)\,x[n]$, $(0.8+0.8j)^n x[n]$ since $\lvert 0.8+0.8j\rvert\approx1.13$); division by $x$, $\log x$ (bounded $x$ can approach $0$); running sums; LTI with $\sum\lvert h\rvert = \infty$ ($x*j^nu[n]$, $x*(-1)^nu[n]$) | bounded coefficients ($\cos^2(\cdot)$, $(\tfrac12)^{\lvert n\rvert}$, $\tfrac{1}{\lvert n\rvert+1}$); bounded nonlinear maps ($e^{x}$, $\lvert\cdot\rvert$, $\sin x$); FIR |

> [!trap] Property-table point losers
> Columns are independent ($x[n]+3$: N Y Y Y). Test $x[f(n)]$ at negative **and** positive $n$ ($x[2n]$: $y[1]=x[2]$). Fixed samples ($x[3]\,x[n]$, $x[n]/x[2]$) ⇒ time-varying and non-causal. All past rows: [[exams/midterm-1/system-property-bank|property bank]].

## 3. Convolution

$$
y[n] = x[n]*h[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k] = \sum_{k=-\infty}^{\infty} h[k]\,x[n-k]
$$

| rule | statement |
|---|---|
| algebra | commutative, associative ($x*(h_1*h_2)$), distributive ($x*(h_1+h_2)$) |
| impulses | $x*\delta = x$; $\;x*\delta[n-n_0] = x[n-n_0]$; if $x*h = y$ then $x[n-a]*h[n-b] = y[n-a-b]$ |
| finite lengths | $x$ on $[N_1,N_2]$, $h$ on $[M_1,M_2]$ ⇒ $y$ on $[N_1+M_1,\;N_2+M_2]$, length $L_x+L_h-1$ — **start index = sum of start indices** |
| steps | $x*u = \sum_{k\le n}x[k]$ (running sum); $\;u*u = (n+1)\,u[n]$ |
| exponentials | $a^nu[n]*b^nu[n] = \dfrac{a^{n+1}-b^{n+1}}{a-b}\,u[n]$ ($a\neq b$); $\;a^nu[n]*a^nu[n] = (n+1)\,a^n u[n]$ |
| 10-second checks | $\sum_n y = \big(\sum_n x\big)\big(\sum_n h\big)$ and $\sum_n(-1)^n y = \big(\sum_n(-1)^n x\big)\big(\sum_n(-1)^n h\big)$ (these are $Y(\pm1) = X(\pm1)H(\pm1)$) |

> [!recipe] Which method?
> Short $x$ or $h$: sum of shifted, scaled copies ([[problems/finite-length-convolution|finite-length convolution]]). Infinite: split $n$ into cases and use a geometric sum, or multiply z-transforms ([[problems/infinite-length-convolution|infinite-length convolution]]). State where $n = 0$ is.

## 4. LTI facts

- $h[n] = T\{\delta[n]\}$ determines an **LTI** system ($y = x*h$), not an arbitrary one (FA19 #1b).
- **Causal ⇔ $h[n] = 0$ for $n<0$.** **Stable ⇔ $\sum_n\lvert h[n]\rvert<\infty$** ⇔ ROC contains $\lvert z\rvert = 1$.
- FIR ⇒ stable. Bounded $h$ ≠ stable: $h = u[n]$ (FA25 #1a, FA19 #1c).
- Series: $h_1*h_2$, $H_1H_2$ (cancellations possible: FA19 #1d); parallel: $h_1+h_2$, $H_1+H_2$.
- Step response $s[n] = h*u = \sum_{k\le n}h[k]$, $S(z) = \dfrac{H(z)}{1-z^{-1}}$, $h[n] = s[n]-s[n-1]$.
- Eigenfunctions (Lecture 6): $x[n] = z_0^n$ ⇒ $y[n] = H(z_0)\,z_0^n$, $z_0$ in the ROC ([[concepts/eigenfunctions-of-lti-systems|eigenfunctions]]).

## 5. LCCDE ⇄ H(z)

> [!key] Standard form (Lecture 9) — matches `scipy.signal.lfilter(b, a, x)` with `a[0] = 1`
> $$
> \begin{gathered}
> y[n] + \sum_{k=1}^{N} a_k\,y[n-k] = \sum_{k=0}^{M-1} b_k\,x[n-k]
> \\[4pt]
> \Big\Updownarrow
> \\[4pt]
> H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{k=0}^{M-1} b_k z^{-k}}{1+\sum_{k=1}^{N} a_k z^{-k}}
> \end{gathered}
> $$

- **LCCDE → H:** $x[n-k] \leftrightarrow z^{-k}X(z)$, collect, divide.
- **H → LCCDE:** $Y(z)\,A(z) = X(z)\,B(z)$; run as $y[n] = -\sum a_k y[n-k] + \sum b_k x[n-k]$ (**flipped signs**; SP23 #6c: $y[n] = \tfrac34 y[n-1] - \tfrac18 y[n-2] + x[n] - 2x[n-1]$).
- **Sign trap:** Lecture 5's $y[n] = \sum_i b_i\,y[n-i] + \sum_j c_j\,x[n-j]$ gives $A(z) = 1 - \sum_i b_i z^{-i}$ (L10 Ex. 1: $y[n] = 2y[n-1]+3y[n-2]+\dots$, $A(z) = 1-2z^{-1}-3z^{-2}$).
- One LCCDE, several ROCs. Causal: outside the outermost pole, run forward; anti-causal pieces run backward (FA25 #7b, [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]]).
- No feedback ($A = 1$) ⇒ FIR, $h[n] = b_n$. From data: $H = Y/X$ (SP23 #6a), cancel, choose the ROC.

## 6. z-transform pairs (with ROC)

$X(z) = \sum_n x[n]\,z^{-n}$. **No ROC = half an answer** (HW3 rubric: 3/6).

| # | $x[n]$ | $X(z)$ | ROC | note |
|---|---|---|---|---|
| 1 | $\delta[n]$ | $1$ | all $z$ | |
| 2 | $\delta[n-k]$ | $z^{-k}$ | all $z$ except $0$ ($k>0$) or $\infty$ ($k<0$) | finite sequences: sum of these |
| 3 | $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $\lvert z\rvert>1$ | |
| 4 | $-u[-n-1]$ | $\dfrac{1}{1-z^{-1}}$ | $\lvert z\rvert<1$ | same formula, other ROC |
| 5 | $a^n u[n]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ | the workhorse |
| 6 | $-a^n u[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert<\lvert a\rvert$ | **minus sign, $u[-n-1]$** |
| 7 | $n\,a^n u[n]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert>\lvert a\rvert$ | from $-z\,\frac{d}{dz}$ |
| 8 | $-n\,a^n u[-n-1]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert<\lvert a\rvert$ | |
| 9 | $(n+1)\,a^n u[n]$ | $\dfrac{1}{(1-az^{-1})^2}$ | $\lvert z\rvert>\lvert a\rvert$ | $= a^nu*a^nu$; left-sided twin: $-(n+1)a^nu[-n-1]$, $\lvert z\rvert<\lvert a\rvert$ |
| 10 | $a^{n-k}\,u[n-k]$ | $\dfrac{z^{-k}}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ (also $\ne\infty$ if $k<0$) | shifted #5 |
| 11 | $a^{n}\,u[n-k]$ | $\dfrac{a^{k}z^{-k}}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ | **write $a^n = a^k\,a^{n-k}$ first** |
| 12 | $b^n u[-n]$ | $\dfrac{1}{1-b^{-1}z} = \dfrac{-bz^{-1}}{1-bz^{-1}}$ | $\lvert z\rvert<\lvert b\rvert$ | FA24 #5c ($b = 3$) |
| 13 | $a^n\big(u[n]-u[n-N]\big)$ | $\dfrac{1-a^Nz^{-N}}{1-az^{-1}}$ | $z\neq0$ | finite: the pole at $a$ is cancelled |
| 14 | $a^{\lvert n\rvert}$, $\lvert a\rvert<1$ | $\dfrac{1}{1-az^{-1}}-\dfrac{1}{1-a^{-1}z^{-1}}$ | $\lvert a\rvert<\lvert z\rvert<\tfrac{1}{\lvert a\rvert}$ | two-sided ⇒ ring |
| 15 | $e^{j\omega_0 n}u[n]$ | $\dfrac{1}{1-e^{j\omega_0}z^{-1}}$ | $\lvert z\rvert>1$ | pole on the unit circle at angle $\omega_0$ |
| 16 | $\cos(\omega_0 n)\,u[n]$ | $\dfrac{1-\cos\omega_0\,z^{-1}}{1-2\cos\omega_0\,z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ | poles $e^{\pm j\omega_0}$ |
| 17 | $\sin(\omega_0 n)\,u[n]$ | $\dfrac{\sin\omega_0\,z^{-1}}{1-2\cos\omega_0\,z^{-1}+z^{-2}}$ | $\lvert z\rvert>1$ | |
| 18 | $r^n\cos(\omega_0 n)\,u[n]$ | $\dfrac{1-r\cos\omega_0\,z^{-1}}{1-2r\cos\omega_0\,z^{-1}+r^2z^{-2}}$ | $\lvert z\rvert>r$ | poles $re^{\pm j\omega_0}$ |
| 19 | $r^n\sin(\omega_0 n)\,u[n]$ | $\dfrac{r\sin\omega_0\,z^{-1}}{1-2r\cos\omega_0\,z^{-1}+r^2z^{-2}}$ | $\lvert z\rvert>r$ | |

No z-transform: $a^n$ for all $n$ (e.g. $e^{j\pi n/4}$), ROC empty (SP25 #1c). Cosines as exponentials: FA25 #5c, $\cos^2(\tfrac{\pi}{4}n)u[n] = \big(\tfrac12+\tfrac14e^{j\pi n/2}+\tfrac14e^{-j\pi n/2}\big)u[n]$, $\lvert z\rvert>1$. Full table: [[concepts/z-transform-pairs|z-transform pairs]].

## 7. z-transform properties (with ROC)

| property | $x[n]$ | $X(z)$ | ROC |
|---|---|---|---|
| linearity | $ax_1[n]+bx_2[n]$ | $aX_1(z)+bX_2(z)$ | at least $R_1\cap R_2$ (grows if a pole cancels) |
| time shift | $x[n-n_0]$ | $z^{-n_0}X(z)$ | $R$, except possibly adding/removing $0$ or $\infty$ |
| exponential scaling | $a^n x[n]$ | $X(a^{-1}z)$ | $\lvert a\rvert R$ (poles move from $p$ to $ap$) |
| modulation | $e^{j\omega_0 n}x[n]$ | $X(e^{-j\omega_0}z)$ | $R$ (poles rotate by $\omega_0$) |
| multiply by $n$ | $n\,x[n]$ | $-z\,\dfrac{dX(z)}{dz}$ | $R$ |
| time reversal | $x[-n]$ | $X(z^{-1})$ | $1/R$ (inside ⇄ outside) |
| conjugation | $x^*[n]$ | $X^*(z^*)$ | $R$ |
| convolution | $x_1[n]*x_2[n]$ | $X_1(z)\,X_2(z)$ | at least $R_1\cap R_2$ |
| first difference | $x[n]-x[n-1]$ | $(1-z^{-1})\,X(z)$ | at least $R\cap\{\lvert z\rvert>0\}$ |
| accumulation | $\sum_{k=-\infty}^{n}x[k]$ | $\dfrac{X(z)}{1-z^{-1}}$ | at least $R\cap\{\lvert z\rvert>1\}$ |
| initial value | $x[n] = 0$ for $n<0$ | $x[0] = \lim_{z\to\infty}X(z)$ | |

> [!example] Rewrite into table entries (FA24 #5a)
> $(n+1)u[n-1] = (n-1)u[n-1] + 2u[n-1]$, $g[n] = n\,u[n] \leftrightarrow \dfrac{z^{-1}}{(1-z^{-1})^2}$: $X(z) = \dfrac{z^{-2}}{(1-z^{-1})^2} + \dfrac{2z^{-1}}{1-z^{-1}}$, $\lvert z\rvert>1$.

## 8. ROC rules and what the ROC tells you

- A **ring** centred at 0, **no poles**, bounded by poles (or $0$, $\infty$).
- **Finite length:** all $z$ except possibly $0$ (some $x[n]\neq0$, $n>0$) and/or $\infty$ (some $x[n]\neq0$, $n<0$).
- **Right-sided:** $\lvert z\rvert>\lvert p_{\max}\rvert$; includes $\infty$ iff $x[n] = 0$ for $n<0$. **Left-sided:** $\lvert z\rvert<\lvert p_{\min}\rvert$; includes $0$ iff $x[n] = 0$ for $n>0$. **Two-sided:** a ring, or empty.
- $K$ distinct pole radii ⇒ $K+1$ ROCs (FA19 #7). See [[problems/all-possible-rocs|all possible ROCs]].

| ROC of $H(z)$ | $h[n]$ | causal? | stable iff |
|---|---|---|---|
| $\lvert z\rvert>\lvert p_{\max}\rvert$, including $\infty$ | right-sided, $h[n] = 0$ for $n<0$ | **yes** | $\lvert p_{\max}\rvert<1$ (all poles inside the unit circle) |
| $\lvert p_{\max}\rvert<\lvert z\rvert<\infty$ | right-sided, starts at some $n<0$ | no | $\lvert p_{\max}\rvert<1$ |
| $\lvert z\rvert<\lvert p_{\min}\rvert$, including $0$ | left-sided, $h[n] = 0$ for $n>0$ | no (anti-causal) | $\lvert p_{\min}\rvert>1$ (all poles outside) |
| $0<\lvert z\rvert<\lvert p_{\min}\rvert$ | left-sided, reaches some $n>0$ | no | $\lvert p_{\min}\rvert>1$ |
| $a<\lvert z\rvert<b$ | two-sided | no | $a<1<b$ |
| all $z$ (maybe not $0$ / $\infty$) | finite length (FIR) | iff $h[n] = 0$ for $n<0$ | always |

> [!key] The three equivalences to box on your sheet
> **Stable ⇔ ROC contains the unit circle.** **Causal ⇔ ROC is outside the outermost pole *and* includes $\infty$** — i.e. $H(z)$, as a ratio of polynomials in $z$, has numerator degree ≤ denominator degree. **Causal and stable ⇔ all poles strictly inside the unit circle** (and $H$ proper). A pole *on* the unit circle is never stable ([[concepts/marginal-stability|marginal stability]]).

## 9. Inverse z-transform and PFE

> [!recipe] PFE in five moves (Lectures 8 and 10)
> 1. Write $X(z)$ in powers of $z^{-1}$; factor the denominator into $(1-p_kz^{-1})$ factors.
> 2. **Improper** (numerator degree in $z^{-1}$ ≥ denominator degree)? Long-divide first: $X(z) = \sum_k C_kz^{-k} + \dfrac{R(z)}{A(z)}$, and $C_kz^{-k} \to C_k\,\delta[n-k]$.
> 3. Cover-up on the proper part: $X(z) = \sum_k \dfrac{A_k}{1-p_kz^{-1}}$ with $A_k = \big[(1-p_kz^{-1})\,X(z)\big]_{z = p_k}$.
> 4. Pick each term's direction from the ROC (table below). Repeated pole: $\dfrac{1}{(1-pz^{-1})^2} \leftrightarrow (n+1)\,p^n u[n]$.
> 5. Complex-conjugate pair $p = re^{j\omega_0}$ with coefficients $A$, $A^*$: combine into $2\lvert A\rvert\,r^n\cos(\omega_0 n+\angle A)\,u[n]$ (SP21 #5: $\dfrac{3z^{-1}}{1+z^{-2}} \to 3\sin(\tfrac{\pi}{2}n)\,u[n]$).
>
> Check: for a causal answer, $x[0] = \lim_{z\to\infty}X(z) = C_0+\sum_k A_k$ (SP23 #6b: $-6+7 = 1 = h[0]$ ✓).

| term | ROC relative to its pole | time-domain term |
|---|---|---|
| $\dfrac{A}{1-pz^{-1}}$ | $\lvert z\rvert>\lvert p\rvert$ (ROC outside the pole) | $A\,p^nu[n]$ (right-sided) |
| $\dfrac{A}{1-pz^{-1}}$ | $\lvert z\rvert<\lvert p\rvert$ (ROC inside the pole) | $-A\,p^nu[-n-1]$ (left-sided) |
| $\dfrac{A}{(1-pz^{-1})^2}$ | outside / inside | $A(n+1)p^nu[n]$ / $-A(n+1)p^nu[-n-1]$ |
| $C\,z^{-k}$ | — | $C\,\delta[n-k]$ |
| $z^{-k}F(z)$ | same as $F$ | $f[n-k]$ |

> [!example] One X, three ROCs, three signals
> $X(z) = \dfrac{1}{(1-\frac12z^{-1})(1-2z^{-1})} = \dfrac{-1/3}{1-\frac12z^{-1}} + \dfrac{4/3}{1-2z^{-1}}$
> - $\lvert z\rvert>2$: $\;x[n] = -\tfrac13(\tfrac12)^nu[n] + \tfrac43\,2^nu[n]$ (causal, unstable)
> - $\tfrac12<\lvert z\rvert<2$: $\;x[n] = -\tfrac13(\tfrac12)^nu[n] - \tfrac43\,2^nu[-n-1]$ (two-sided, stable)
> - $\lvert z\rvert<\tfrac12$: $\;x[n] = \tfrac13(\tfrac12)^nu[-n-1] - \tfrac43\,2^nu[-n-1]$ (anti-causal, unstable)

Improper example (L10 Ex. 1): $H(z) = \dfrac{1-3z^{-1}+z^{-2}+4z^{-3}}{1-2z^{-1}-3z^{-2}} = \tfrac59 - \tfrac43z^{-1} + \dfrac{7/36}{1-3z^{-1}} + \dfrac{1/4}{1+z^{-1}}$, so causal $h[n] = \tfrac59\delta[n]-\tfrac43\delta[n-1]+\tfrac{7}{36}3^nu[n]+\tfrac14(-1)^nu[n]$ and $h[0] = \tfrac59+\tfrac{7}{36}+\tfrac14 = 1$ ✓.

## 10. Stability and unbounded outputs

$Y(z) = X(z)H(z)$, ROC at least $\mathrm{ROC}_X\cap\mathrm{ROC}_H$ (larger after cancellation).

| system | input | output |
|---|---|---|
| stable (ROC ∋ unit circle) | any bounded input | bounded — always |
| causal, pole $p$ **outside** the unit circle | almost any bounded input, e.g. $\delta[n]$ | unbounded — **unless $X$ has a zero at $p$** that cancels it: $x = \delta[n]-p\,\delta[n-1]$ gives a bounded $y$ (L11; SP23 #7c) |
| **marginally stable**: poles on the unit circle at $e^{\pm j\omega_1}$, none outside | $e^{j\omega_2n}u[n]$, $\cos(\omega_2 n)u[n]$ with $\omega_2 = \omega_1$ | **unbounded**: the matching input pole makes a double pole, $y \sim n\,e^{j\omega_1 n}$ (e.g. $u*u = (n+1)u$) |
| marginally stable | a different frequency, or a decaying input | bounded |
| any | an unbounded input whose pole is cancelled by a zero of $H$ | can be bounded (SP23 #7b: $3^nu[n]-4\cdot3^{n-1}u[n-1]$ into $\frac{z-3}{z-4}$ gives $\delta[n]$) |

> [!trap] $e^{j2/3}$ is not $e^{j2\pi/3}$
> FA25 #8b has a pole at $e^{j2/3}$ — angle $\tfrac23$ rad ≈ 38°, not $\tfrac{2\pi}{3}$ = 120°. So $\cos(\tfrac{2\pi}{3}n)\,u[n]$ does **not** match it and the output is bounded (key: False). Match the *angle*, exactly, including a real pole at $1$ ($\omega = 0$: $u[n]$) or $-1$ ($\omega = \pi$: $(-1)^nu[n]$). Worked in [[problems/unbounded-outputs-and-pole-matching|unbounded outputs and pole matching]].

Parameters: causal ⇒ every pole inside, or a zero cancels the bad pole (SP25 #7: $\alpha = \pm2$) — [[problems/parameters-for-stability|parameters for stability]].

> [!tip] Make the sheet yourself
> Front: pairs (§6), ROC table (§8), PFE (§9). Back: property rules (§2), convolution (§3), unbounded outputs (§10).

## Related

[[exams/midterm-1/index|Midterm 1 review guide]] · [[exams/midterm-1/true-false-bank|T/F bank]] · [[exams/midterm-1/system-property-bank|property bank]] · [[demos/practice-drills|practice drills]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/partial-fraction-expansion|PFE]] · [[supplements/transform-tables|transform tables]]

### Sources for this page

Snyder's notes, Lectures 2–11; course transform tables (Tables 9–10); Midterm 1 Review slides; HW3 rubric; Midterm 1 keys FA2019–FA2025.
