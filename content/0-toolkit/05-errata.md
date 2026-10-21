---
title: "Errata in the course materials"
description: "Slips in the past Midterm 1 and 2 keys, lecture notes and slides, homework solutions and the transform table: what each says, the correction, and why. None is propagated into this site."
tags: [toolkit, exam, midterm-1, midterm-2]
aliases: ["errata", "known errors in the exam keys", "answer key mistakes"]
---

Slips that change a number, sign, label or definition; the site's pages use the corrections.

> [!tip] Labels
> Key: official past-midterm solutions. Notes, slides: lecture materials ("annotated", "ink": in-class handwriting). HW sol.: Fall 2026 homework solutions.

## Past Midterm 1 answer keys

| exam, problem | the key says | correct | why / how to see it |
|---|---|---|---|
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #4(a)]] | boxed $y = \{2,-5,6,0,-5,10,-4,3\}$ for $x = \{1,-2,\underset{\uparrow}{0},3,-1,1\}$, $h = \{\underset{\uparrow}{2},-1,3\}$ | $y = \{2,-5,\underset{\uparrow}{5},0,-5,12,-4,3\}$, starting at $n=-2$ | The key's own matrix gives the right column; the boxed copy is wrong. |
| [[exams/midterm-1/past-exams/spring-2021\|SP2021 #6]] | for $y[n] = 2y[n-3] - x[n] + x[n-3]$: $h[0] = 1$, $h[3] = 3$ | $h[0] = -1$, $h[1] = 0$, $h[3] = -1$, $h[4] = 0$; $H(z) = \dfrac{-1+z^{-3}}{1-2z^{-3}}$ | The key evaluates $-\delta[0]$ as $+1$, and $h[3]$ inherits the slip. |
| [[exams/midterm-1/past-exams/fall-2019\|FA2019 #5(b)]] | $e^{-91}$; answer labelled $X_d(\omega)$ | $X(z) = e^{-64}z^{-8} + e^{-81}z^{-9} + e^{-100}z^{-10}$, ROC $z\neq0$ | $9^2 = 81$, and the question asks for $X(z)$, not $X_d(\omega)$. |
| [[exams/midterm-1/past-exams/spring-2023\|SP2023 #6(c)]] | difference equation with both feedback terms on $y[n-1]$ | $y[n] = \tfrac34 y[n-1] - \tfrac18 y[n-2] + x[n] - 2x[n-1]$ | $(1-\tfrac12 z^{-1})(1-\tfrac14 z^{-1}) = 1 - \tfrac34 z^{-1} + \tfrac18 z^{-2}$: the second term is a two-sample delay. |
| [[exams/midterm-1/past-exams/fall-2025\|FA2025 #5(a)]] | handwritten denominator with a stray $n$ | $X(z) = \dfrac{e^{-j4\pi/3}z^{4}}{1-e^{j\pi/3}z^{-1}}$, ROC $1<\lvert z\rvert<\infty$ | Start $n=-4$: $z^4$ excludes $\infty$; the unit-circle pole sets $\lvert z\rvert>1$. |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #8(a)]] | "$\lvert a\rvert > 1$" | $\lvert\alpha\rvert > 1$ | The parameter is $\alpha$ in $y[n] + \alpha y[n-1] = x[n] + 3x[n-1]$. |
| [[exams/midterm-1/past-exams/fall-2024\|FA2024 #4(b)]] | the boxed result is labelled "$x[n] = \dots$" | it is $y[n] = (x*h)[n]$ | Only the label is wrong. |
| [[exams/midterm-1/past-exams/spring-2025\|SP2025 #3(b)]] | "not causal because $h[n] \neq 0$ for all $n<0$" | "…because $h[n] \neq 0$ for **some** $n<0$" (here $h[-1] \neq 0$) | One nonzero $h[n]$ with $n<0$ already breaks causality. ([[exams/midterm-1/past-exams/fall-2024\|FA2024 #3(b)]]'s "is not zero for all $n<0$" reads correctly as "not zero everywhere on $n<0$".) |

## Past Midterm 2 answer keys

| exam, problem | the key says | correct | why / how to see it |
|---|---|---|---|
| [[exams/midterm-2/past-exams/spring-2025\|SP2025 #4]] | the $(-1)^n$ part of the output is $j\pi(-1)^n$, using $H_d(\pi)=j\pi$ | $0$ | $H_d(\pi)=j\pi$ but $H_d(-\pi)=-j\pi$; real $h$ and real $(-1)^n$ force a real term, the midpoint $0$ — see [[3-fourier-analysis/15-frequency-response\|Lecture 15]]. |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021 #5(b)]] | "$H_a(0)=1$ and $\Omega=0$ … corresponds to $\omega=0$ … As a result, $H_d(0)=0$" | $H_d(0)=H_a(0)=1$ | The key's own formula and plot give $1$. |
| [[exams/midterm-2/past-exams/fall-2019\|FA2019 #8(b)]] | the sketch of $x_a(t)$ for $x[n]=\delta[n-3]$ through an ideal D/A: a sinc peaking at $t=4T$ (zero crossings at $0,T,2T,3T,5T,6T$) | peak at $t=3T$, zero crossings at $0,T,2T,4T,5T,6T$ | An ideal D/A passes through the samples: $x_a(3T)=1$, $x_a(4T)=0$. |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #5(a)]] | $H_d(\omega)=\sum_n x[n]e^{-j\omega n}=1+e^{-j6\omega}=e^{-j3\omega}(e^{j3\omega}+e^{j3\omega})$ | $\sum_n h[n]e^{-j\omega n}$, and $e^{-j3\omega}(e^{j3\omega}+e^{-j3\omega})$ | As printed the bracket is $2$; the boxed $2e^{-j3\omega}\cos(3\omega)$ is right. |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023 #5]] | boxes $T\lt\frac{1}{15000}$ s in (a) and $T\lt\frac{1}{20000}$ s in (b), then designs both filters at the equality as "the largest" $T$ | $T\le\frac{1}{15000}$ s, largest $T=\frac{1}{15000}$ s $\approx66.7\ \mu$s; (b) $T\le\frac{1}{20000}$ s, largest $\frac{1}{20000}$ s | A strict inequality has no largest $T$; equality is allowed. |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024 #5(b)]] | the DTFT sketches are labelled $X_d(\Omega)$, over an $\Omega$ axis | $X_d(\omega)$ over $\omega\in[-\pi,\pi]$ | A DTFT lives on $\omega$; shapes and heights are right. |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #7(b)]] | in both sketches the tick at $-\frac{\pi}{2}$ is labelled "$\frac{\pi}{2}$" | $-\frac{\pi}{2}$ | Only the tick label slipped; the shapes are right. |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #10]] | (b) "$\frac{A_1\cdot24}{2}=6\Rightarrow A_1=\frac12$", "$\frac{A_2\cdot24}{2}=12\Rightarrow A_1=1$", "$\frac{A_2\cdot24}{2}=9\Rightarrow A_1=\frac34$"; (c) $\Omega_1$ for all three frequencies | $A_1,A_2,A_3=\frac12,1,\frac34$ with $\Omega_1,\Omega_2,\Omega_3=1000\pi,6000\pi,9000\pi$ rad/s | The values are right; only the subscripts are inconsistent. |
| [[exams/midterm-2/past-exams/spring-2021\|SP2021 #8(b)]] | the copies are labelled $X_c\big(\frac{\Omega}{F_s}\pm2\pi\big)$ on an $\omega$ axis | $F_s\,X_c\big((\omega\mp2\pi)F_s\big)$, the copies centred at $\omega=\pm2\pi$ | The label mixes analog and digital frequency; $X_d(\omega)=5000$ is right. |

## Lecture notes and slides

| where | as written | should be | why it matters |
|---|---|---|---|
| L2 notes §2 | the example $x[n]$ is written $[0\ 4\ {-2}\ 0\ 3\ 1\ 0]$, then $\{0,4,-2,0,3,1\}$, then $\{0,4,-2,0,3,0\}$ | one sequence throughout | Harmless: only the $n=0$ marker matters ($x[0]=4$). |
| L2 notes Eq. 24 | exponentials "$Ba^n,\ \infty<n<\infty$" | $-\infty<n<\infty$ | Typo. |
| L3 notes, Exercise 3 | $T(x[n-n_0]) = x[\lvert n\rvert - n_0\rvert]$ | $x[\lvert n\rvert - n_0]$ | A stray bar; the argument is right — see [[concepts/time-invariance\|time invariance]]. |
| L4 notes §1.1 | $x[3] = \dots = x[3]\delta[0] = \delta[3]$ | $= x[3]$ | Sifting returns the sample value; $\delta[3] = 0$. |
| L5 vs L9 notes | L5: $y[n] = \sum_i b_i\,y[n-i] + \sum_j c_j\,x[n-j]$; L9: $y[n] + \sum_k a_k\,y[n-k] = \sum_k b_k\,x[n-k]$ | both fine, but $a_k = -b_i$ and L5's $b$ are *feedback* while L9's $b$ are *feedforward* | This site uses L9's form (`lfilter(b, a, x)`) — see [[concepts/lccde\|LCCDE]]. |
| L7 slide 7 | left-sided: "$x[n] = 0,\ n < n_0$" | $x[n] = 0,\ n > n_0$ | As printed it repeats the right-sided definition — see [[concepts/sided-sequences\|sided sequences]]. |
| L7 notes, Table 1 | $\mathrm{Im}\{x[n]\} \leftrightarrow \tfrac12\big[X(z) - X^*(z^*)\big]$ | $\tfrac{1}{2j}\big[X(z) - X^*(z^*)\big]$ | $\mathrm{Im}\{x\} = (x - x^*)/(2j)$ — see [[0-toolkit/01-complex-numbers\|complex numbers]]. |
| L10 notes, Exercise 1 (long division) | second product line $-\big(-\tfrac59 - \tfrac{10}{9}z^{-1} - \tfrac53 z^{-1}\big)$ | $-\big(\tfrac59 - \tfrac{10}{9}z^{-1} - \tfrac53 z^{-2}\big)$, i.e. $\tfrac59(1-2z^{-1}-3z^{-2})$ | Two slips in one line; the remainder and coefficients are right — see [[0-toolkit/04-factoring-and-long-division\|factoring and long division]]. |
| L11 notes §1.1 | "Non-causal – a system is causal if it depends on some future inputs…" | "a system is **non-causal** if…" | Right definition, wrong word — see [[concepts/causality\|causality]]. |
| L5 notes, FIR/IIR rule | "$K>0$ (feedback terms) ⇒ IIR" | feedback usually gives an infinite $h[n]$, but not always | The notes' own recursive moving average has feedback yet a finite $h$ — see [[concepts/fir-and-iir\|FIR and IIR]]. |
| L9 notes §1.2 | "the transfer function has $N$ poles and $M$ zeros" | with input terms $b_0,\dots,b_{M-1}$ the numerator has $M-1$ finite zeros | Off by one; count the actual roots — see [[concepts/poles-and-zeros\|poles and zeros]]. |
| L10 slide 11 | "Determine the frequency response $H(z)$" | "Determine the transfer function $H(z)$" | The frequency response is $H$ on the unit circle ([[3-fourier-analysis/15-frequency-response\|Lecture 15]]). |
| L13 notes Fig. 1 caption, slide 10 | sawtooth $x(t)=t$, $T_0=1$: $c_k=\dfrac{j}{\pi k}$ for $k\neq0$ | $c_k=\dfrac{j}{2\pi k}$ ($c_0=\tfrac12$) | $\int_0^1 t\,e^{-j2\pi kt}\,dt=\tfrac{j}{2\pi k}$ — see [[3-fourier-analysis/13-fourier-analysis-and-the-dtft\|Lecture 13]]. |
| L13 notes §2 (after Eq. 25) | "the magnitude of each $c_k$ value is directly proportional to the amount of energy that harmonic frequency $k\Omega_0$ contributes" | the power of harmonic $k$ is $\lvert c_k\rvert^2$ | Parseval: $\frac{1}{T_0}\int_{T_0}\lvert x(t)\rvert^2dt=\sum_k\lvert c_k\rvert^2$. |
| L13 notes Eq. 29 | $x_k[n]=e^{j\omega_0kn}$, $0\le k\lt N_0-1$ | $0\le k\le N_0-1$ | The synthesis sum (Eq. 32) runs to $k=N_0-1$. |
| L13 notes Eq. 35 (Exercise 1) | $\dfrac{1}{N_0}\displaystyle\sum_{k=0}^{L-1}e^{-j\frac{2\pi k}{N_0}n}$ | $\displaystyle\sum_{n=0}^{L-1}$ | The summation index is $n$; Eqs. 36–38 are right. |
| L13 notes Eq. 40 | $\angle c_k=-\dfrac{\pi k}{N_0}(L-1)$ | add $\pm\pi$ wherever $\dfrac{\sin(\pi Lk/N_0)}{\sin(\pi k/N_0)}\lt0$ | The sine ratio can be negative — see [[concepts/magnitude-and-phase-response\|magnitude and phase]]. |
| L13 notes Eq. 47 | numerator $e^{j\omega L/2}-e^{j\omega L/2}$ (which is $0$) | $e^{j\omega L/2}-e^{-j\omega L/2}$ | Eq. 48 is right. |
| L13 annotated slide 16 (handwriting) | for (c) $\{\underset{\uparrow}{2},0,-2\}$: $X_d(\omega)=2-e^{-j2\omega}$ | $2-2e^{-j2\omega}$ | The sample at $n=2$ is $-2$; the answer is unaffected. |
| L14 notes Table 2, slide 15 | $n\,x[n]\leftrightarrow-j\,\dfrac{dX_d(\omega)}{d\omega}$ | $n\,x[n]\leftrightarrow+j\,\dfrac{dX_d(\omega)}{d\omega}$ | $\dfrac{dX_d}{d\omega}=-j\sum_n n\,x[n]e^{-j\omega n}$ — see [[concepts/dtft-properties\|DTFT properties]]. |
| L14 slide 6 (concept check) | $X_2(z)=\dfrac{1+z^{-1}}{1-2z^{-1}-3z^{-2}}$, $\lvert z\rvert\gt2$ | $\lvert z\rvert\gt3$ | $1-2z^{-1}-3z^{-2}=(1-3z^{-1})(1+z^{-1})$; the conclusion (no DTFT) stands. |
| L14 notes Table 1, rect row | $\mathrm{rect}\big(\frac{n-k}{L}\big)\leftrightarrow\dfrac{\sin(L\omega/2)}{\sin(\omega/2)}e^{-j\omega k}$ | exact for odd $L$; for even $L$ multiply by $e^{-j\omega/2}$ | An even-length pulse is centred at $k+\frac12$. |
| L14 notes Table 1, $\mathrm{sinc}^2$ row | $\mathrm{sinc}^2(Ln)\leftrightarrow\dfrac{\pi}{L}\Delta\big(\frac{\omega}{2L}\big)$ | true only for $L\le\frac{\pi}{2}$ | For $L\gt\frac{\pi}{2}$ the periodic copies overlap — see [[concepts/dtft-pairs\|DTFT pairs]]. |
| L14 notes Eq. 27 | lower limit $n=\infty$ | $n=-\infty$ | Typo. |
| L14 notes §1 | "An LTI system is BIBO stable if the DTFT of its impulse response $h[n]$ exists" | … if the DTFT sum of $h[n]$ converges absolutely, $\sum\lvert h[n]\rvert\lt\infty$ | The ideal low-pass has a DTFT but is not BIBO stable — see [[concepts/bibo-stability\|BIBO stability]]. |
| L15 slide 8, last line | $\lvert H_d(\omega)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$ | $\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$ | The amplitude is the gain at $\omega_0$ — see [[3-fourier-analysis/15-frequency-response\|Lecture 15]]. |
| L16 notes Eq. 24 | $(3+2^{-j\omega}+e^{-j2\omega})(3+2^{j\omega}+e^{j2\omega})$ | $2e^{-j\omega}$ and $2e^{j\omega}$ | Typo; Eqs. 25–26 are right. |
| L16 notes, Exercise 2 (last paragraph) | no $\pm\pi$ jumps "since the expression inside the absolute value signs never goes negative" | no jumps because $\mathrm{Re}\,H_d(\omega)=3+2\cos\omega+\cos2\omega=2(\cos^2\omega+\cos\omega+1)\ge\frac32$ | That expression is $\lvert H_d\rvert^2$, never negative for any system — see [[3-fourier-analysis/16-magnitude-and-phase-response\|Lecture 16]]. |
| L16 slide 4 | "Changes in sign for $\mathrm{Re}\{H_d(\omega)\}$ let to $\pm\pi$ jumps in phase" | "lead to"; and the sign that matters is that of the real amplitude left after the linear-phase factor is pulled out | $\mathrm{Re}\{e^{-j2\omega}\}$ changes sign, yet $e^{-j2\omega}$ has no $\pi$ jump. |
| L16 slide 3 | quadrant rule for $\angle z$ with the cases $a\gt0$; $a\lt0,\ b\gt0$; $a\lt0,\ b\lt0$ | also $a=0$: $\pm\frac{\pi}{2}$ (the sign of $b$); $a\lt0,\ b=0$: $\pi$ | As printed, $j$ and $-1$ get no angle — see [[0-toolkit/01-complex-numbers\|complex numbers]]. |
| L16 slides, title slide | "October 5th and 7th, 2025" | 2026 | Typo. |
| L18 in-class ink, slide 9 | the second sample of $x[n]=3\delta[n-1]+\delta[n-4]$ is labelled "$x[3]$" | $x[4]$ | Drawn correctly at $t=4T$; only the label slipped. |
| L19 slide 7 | "$f_s=f_{\text{nyquist}}=2B=\frac{\Omega_0}{\pi}$ seconds" | hertz | A sampling frequency is in Hz. |
| L20 notes Eq. 36 | $W=e^{-j2\pi}$ | $W_N=e^{-j\frac{2\pi}{N}}$ | $e^{-j2\pi}=1$; Eqs. 37–38 are right. |
| L20 slide 10 | "$x[n]=x[k+mN]$" | $x[n]=x[n+mN]$ | Typo; the proof uses $n+mN$. |
| L21 notes §1 | "For proofs … please refer to lecture 21" | Lecture 20 | The proofs are in [[5-dft-and-fft/20-discrete-fourier-transform\|Lecture 20]]. |
| L21 notes, text under Eq. 25 | "linear in $k$ with slope $-2\pi m/M$" | $-2\pi m/N$ | Eq. 25 itself has $e^{-j\frac{2\pi km}{N}}$. |
| L21 slide 13 (Example 2) | second sequence named $y[n]$ | $h[n]$ | It is the second operand of the circular convolution. |

## Homework solutions

| where | as written | should be |
|---|---|---|
| HW1 #5(b) | $T(x_1)+T(x_2) = \{\dots,5,4,2,\underset{\uparrow}{1},2,4,5,\dots\}$ for $x_1 = 1$, $x_2 = n^2$, clip to $[0,4]$ | $\{\dots,5,5,2,\underset{\uparrow}{1},2,5,5,\dots\}$: at $n=\pm2$ it is $1 + \mathrm{clip}(4) = 5$. Conclusion unchanged. See [[homework/hw1\|HW1]]. |
| HW3 #1(b) | middle line $X_2(z) = \dfrac{(3/4)^3 z^{-2}}{1-(3/4)z^{-1}}$ | $\dfrac{(3/4)^5 z^{-2}}{1-(3/4)z^{-1}}$, ROC $\lvert z\rvert>\tfrac34$. See [[homework/hw3\|HW3]] and [[0-toolkit/02-geometric-series\|geometric series]]. |
| HW1 #6(c) | the last line compares the unshifted output $y[n] = \{\underset{\uparrow}{0},1,2,3\}$ with $T\{x[n-1]\}$ | compare $y[n-1] = \{\underset{\uparrow}{0},0,1,2,3\}$ with $T\{x[n-1]\} = \{\underset{\uparrow}{-1},0,1,2\}$: they differ at $n=0$ and $n=4$. Verdict unchanged. See [[homework/hw1\|HW1]]. |
| HW3 #4(a) | lists only the zero at $z = 3$ | $H(z) = \dfrac{z(z-3)}{(z-\frac12)(z+\frac23)}$ also has a zero at $z = 0$. See [[homework/hw3\|HW3]] and [[concepts/poles-and-zeros\|poles and zeros]]. |
| HW4 #2 (necessity) | bounded input $x[n] = \mathrm{sgn}(h[-n]) = h[-n]/\lvert h[-n]\rvert$ | $x[n] = h^*[-n]/\lvert h[-n]\rvert$ (and $0$ where $h[-n]=0$). For real $h$ the two agree; complex $h$ needs the conjugate. See [[homework/hw4\|HW4]] and [[concepts/bibo-stability\|BIBO stability]]. |
| HW4 #3(d) | the output grows like $n\cos(\tfrac{\pi}{4}n+\varphi)$ | $H$ has complex coefficients, so only the $e^{-j\pi n/4}$ half of the cosine resonates: the growing part is $C(n+1)e^{-j\pi n/4}$ with $\lvert C\rvert = \tfrac12\sin\tfrac{\pi}{8} \approx 0.19$. Verdict unchanged. See [[homework/hw4\|HW4]]. |
| HW5 header (and HW2 statement) | due "Oct. 4, 2025"; HW2 #1 says "two systems" and lists three | due Sun Oct 4, **2026**; three systems (typos only) |

## The official transform table

| where | as written | should be |
|---|---|---|
| `transform_tables.pdf`, Table 10, pair 3 | $u[-n-1] \leftrightarrow \dfrac{1}{1-z^{-1}}$, $\lvert z\rvert<1$ | $-u[-n-1] \leftrightarrow \dfrac{1}{1-z^{-1}}$, $\lvert z\rvert<1$ — pair 6 with $\alpha=1$. See [[supplements/transform-tables\|transform tables]]. |

> [!trap] The one to remember
> The left-sided pair carries a minus: $-\alpha^n u[-n-1] \leftrightarrow \dfrac{1}{1-\alpha z^{-1}}$, $\lvert z\rvert<\lvert\alpha\rvert$; Table 10 drops it for $\alpha=1$.

## Not errors, but read them carefully

- **FA2025 #8(b): $e^{j2/3}$.** Angle $2/3$ rad, not $2\pi/3$, so $\cos(\tfrac{2\pi}{3}n)u[n]$ gives a bounded output (key: False, right). See [[problems/unbounded-outputs-and-pole-matching|pole matching]].
- **FA2025 #1(d): "a left-sided impulse response can never be causal" (key: True).** Right with Lecture 7's infinite-length "left-sided". See [[exams/midterm-1/true-false-bank|true/false bank]].
- **FA2019 #4, SP2021 #2: the $n=0$ labels are right.** FA2019 #4: both arrows sit under the first entries, so $y = \{\underset{\uparrow}{-1},5,-7,7,-6,3,-2,-1\}$. SP2021 #2: "$\leftarrow n=0$" marks $y[0] = 2$. See [[problems/finite-length-convolution|finite-length convolution]].
- **HW2 #1(a),(b): linearity needs "initially at rest".** With $y[-5]=1$ a zero input gives a nonzero output. See [[homework/hw2|HW2]] and [[concepts/lccde|LCCDE]].
- **FA2023 #8(b): "stable for all $\alpha$".** True unless a zero cancels a pole (then no annulus is left). See [[exams/midterm-1/past-exams/fall-2023|FA2023]] and [[problems/parameters-for-stability|parameters for stability]].
- **Lecture 3 slides, Example 4.** Posted deck: $y[n] = \max\{0, x[n]\}$; in-class deck: $y[n] = x[n]\,x[0]$. Both on [[1-signals-and-systems/03-system-properties|Lecture 3]].
- **"LSI" = "LTI".** Linear shift-invariant (older keys, Singer & Munson) means linear time-invariant. See [[supplements/notation-translation|notation translation]].
- **$X_d(\omega)$ vs $X(e^{j\omega})$, $(x*h)[n]$ vs $x[n]*h[n]$.** Course vs textbook notation.
- **Two sincs.** Lectures 14 and 18 and the Midterm 2 keys (FA2019 #5, FA2024 #1(c), #2) use $\mathrm{sinc}(x)=\frac{\sin x}{x}$; `transform_tables.pdf` and `np.sinc` use $\frac{\sin\pi x}{\pi x}$: $\frac{\sin(Wn)}{\pi n}=\frac{W}{\pi}\mathrm{sinc}(Wn)$ vs $\frac{W}{\pi}\mathrm{sinc}\big(\frac{Wn}{\pi}\big)$. See [[concepts/dtft-pairs|DTFT pairs]] and [[supplements/transform-tables|transform tables]].
- **SP2021 MT2 #2: unwrapped phase.** $-4\omega$ drawn down to $-2\pi$, not wrapped into $[-\pi,\pi]$: equal mod $2\pi$. See [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]].

### Sources for this page

Past Midterm 1 and 2 keys; Lecture 2–21 notes and slides (rendered where ambiguous); HW1–HW5 solutions and statements; `transform_tables.pdf` Tables 5 and 10; `review.pdf` p. 3.
