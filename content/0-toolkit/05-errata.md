---
title: "Errata in the course materials"
description: "Slips found in the past Midterm 1 answer keys, the lecture notes and slides, the homework solutions and the official transform table while building this site — each with the source, what it says, the correct version and why. None of them is propagated into this site."
tags: [toolkit, exam, midterm-1]
aliases: ["errata", "known errors in the exam keys", "answer key mistakes"]
---

Course materials are written fast, and old exam keys are often handwritten under time pressure. This page lists every slip found while checking the sources for Lectures 1–11, HW1–HW4 and the seven past Midterm 1 exams, so that you (a) do not copy one onto your cheat sheet and (b) do not lose ten minutes on exam night convinced that *you* are wrong. Only substantive items are listed — things that change a number, a sign or a definition.

> [!tip] How to read this page
> "Key" means the official solutions of a past Midterm 1 (see [[0-midterm-1/past-exams/index|past exams]]); "notes" means Prof. Snyder's typed lecture notes; "slides" the lecture decks; "HW sol." the Fall 2026 homework solutions. Every correction below was recomputed in Python (`verify/hub/toolkit_errata.py` and `verify/exams/*.py`); the exam pages on this site already use the corrected versions.

## Past Midterm 1 answer keys

| exam, problem | the key says | correct | why / how to see it |
|---|---|---|---|
| [[0-midterm-1/past-exams/spring-2025\|SP2025 #4(a)]] | boxed $y = \{2,-5,6,0,-5,10,-4,3\}$ for $x = \{1,-2,\underset{\uparrow}{0},3,-1,1\}$, $h = \{\underset{\uparrow}{2},-1,3\}$ | $y = \{2,-5,\underset{\uparrow}{5},0,-5,12,-4,3\}$, starting at $n=-2$ | the key's own matrix computation produces the right column; the boxed answer was copied wrong. `np.convolve` agrees with the matrix. |
| [[0-midterm-1/past-exams/spring-2021\|SP2021 #6]] | for $y[n] = 2y[n-3] - x[n] + x[n-3]$: $h[0] = 1$, $h[3] = 3$ | $h[0] = -1$, $h[1] = 0$, $h[3] = -1$, $h[4] = 0$; $H(z) = \dfrac{-1+z^{-3}}{1-2z^{-3}}$ | the key's first line evaluates $-\delta[0]$ as $+1$, and $h[3] = 2h[0] + \delta[0]$ inherits the slip. Run the recursion: $h[0] = -\delta[0] = -1$, $h[3] = 2h[0] + 1 = -1$. |
| [[0-midterm-1/past-exams/fall-2019\|FA2019 #5(b)]] | $e^{-91}$; answer labelled $X_d(\omega)$ | $X(z) = e^{-64}z^{-8} + e^{-81}z^{-9} + e^{-100}z^{-10}$, ROC $z\neq0$ | $9^2 = 81$; and the question asks for the z-transform $X(z)$, not the DTFT $X_d(\omega)$. |
| [[0-midterm-1/past-exams/spring-2023\|SP2023 #6(c)]] | difference equation with both feedback terms on $y[n-1]$ | $y[n] = \tfrac34 y[n-1] - \tfrac18 y[n-2] + x[n] - 2x[n-1]$ | the denominator is $(1-\tfrac12 z^{-1})(1-\tfrac14 z^{-1}) = 1 - \tfrac34 z^{-1} + \tfrac18 z^{-2}$; the second term is a two-sample delay. |
| [[0-midterm-1/past-exams/fall-2025\|FA2025 #5(a)]] | handwritten denominator with a stray $n$ | $X(z) = \dfrac{e^{-j4\pi/3}z^{4}}{1-e^{j\pi/3}z^{-1}}$, ROC $1<\lvert z\rvert<\infty$ | $x[n] = e^{j\pi n/3}u[n+4]$ starts at $n=-4$: the $z^4$ removes $\infty$ from the ROC, the pole on the unit circle sets $\lvert z\rvert>1$. |
| [[0-midterm-1/past-exams/fall-2024\|FA2024 #8(a)]] | "$\lvert a\rvert > 1$" | $\lvert\alpha\rvert > 1$ | the parameter is $\alpha$ in $y[n] + \alpha y[n-1] = x[n] + 3x[n-1]$ (non-causal, ROC $\lvert z\rvert < \lvert\alpha\rvert$); stable iff that disc contains the unit circle. |
| [[0-midterm-1/past-exams/fall-2024\|FA2024 #4(b)]] | the boxed result is labelled "$x[n] = \dots$" | it is $y[n] = (x*h)[n]$ | the right-hand side is correct; only the label is wrong. |
| [[0-midterm-1/past-exams/spring-2025\|SP2025 #3(b)]], [[0-midterm-1/past-exams/fall-2024\|FA2024 #3(b)]] | "not causal because $h[n] \neq 0$ for all $n<0$" | "…because $h[n] \neq 0$ for **some** $n<0$" (here $h[-1] \neq 0$) | causality fails as soon as a single $h[n]$ with $n<0$ is nonzero; "for all" would be a much stronger (and false) claim. |

## Lecture notes and slides

| where | as written | should be | why it matters |
|---|---|---|---|
| L2 notes §2 | the example $x[n]$ is written $[0\ 4\ {-2}\ 0\ 3\ 1\ 0]$, then $\{0,4,-2,0,3,1\}$, then $\{0,4,-2,0,3,0\}$ | one sequence throughout | harmless: the point is only where the $n=0$ marker goes ($x[0]=4$) |
| L2 notes Eq. 24 | exponentials "$Ba^n,\ \infty<n<\infty$" | $-\infty<n<\infty$ | typo |
| L3 notes, Exercise 3 | $T(x[n-n_0]) = x[\lvert n\rvert - n_0\rvert]$ | $x[\lvert n\rvert - n_0]$ | a stray bar; the argument (time-varying, because $x[\lvert n-n_0\rvert] \neq x[\lvert n\rvert-n_0]$) is right — see [[concepts/time-invariance\|time invariance]] |
| L4 notes §1.1 | $x[3] = \dots = x[3]\delta[0] = \delta[3]$ | $= x[3]$ | the sifting sum returns the sample value; $\delta[3] = 0$ |
| L5 vs L9 notes | L5: $y[n] = \sum_i b_i\,y[n-i] + \sum_j c_j\,x[n-j]$; L9: $y[n] + \sum_k a_k\,y[n-k] = \sum_k b_k\,x[n-k]$ | both fine, but $a_k = -b_i$ and L5's $b$ are *feedback* while L9's $b$ are *feedforward* | this site uses L9's form (it matches `lfilter(b, a, x)`); flip the feedback signs when you move a term across — see [[concepts/lccde\|LCCDE]] |
| L7 slide 7 | left-sided: "$x[n] = 0,\ n < n_0$" | $x[n] = 0,\ n > n_0$ | as printed it repeats the right-sided definition — see [[concepts/sided-sequences\|sided sequences]] |
| L7 notes, Table 1 | $\mathrm{Im}\{x[n]\} \leftrightarrow \tfrac12\big[X(z) - X^*(z^*)\big]$ | $\tfrac{1}{2j}\big[X(z) - X^*(z^*)\big]$ | $\mathrm{Im}\{x\} = (x - x^*)/(2j)$; the printed form is off by a factor $j$ (checked numerically) — see [[0-toolkit/01-complex-numbers\|complex numbers]] |
| L10 notes, Exercise 1 (long division) | second product line $-\big(-\tfrac59 - \tfrac{10}{9}z^{-1} - \tfrac53 z^{-1}\big)$ | $-\big(\tfrac59 - \tfrac{10}{9}z^{-1} - \tfrac53 z^{-2}\big)$, i.e. $\tfrac59(1-2z^{-1}-3z^{-2})$ | two slips in one line (sign of $\tfrac59$, exponent of the last term); the remainder $\tfrac49 - \tfrac59 z^{-1}$, $C_0 = \tfrac59$, $C_1 = -\tfrac43$, $A_1 = \tfrac{7}{36}$, $A_2 = \tfrac14$ are all right — worked in [[0-toolkit/04-factoring-and-long-division\|factoring and long division]] |
| L11 notes §1.1 | "Non-causal – a system is causal if it depends on some future inputs…" | "a system is **non-causal** if…" | the definition is right, the word is wrong — see [[concepts/causality\|causality]] |
| L5 notes, FIR/IIR rule | "$K>0$ (feedback terms) ⇒ IIR" | feedback usually gives an infinite $h[n]$, but not always | the notes' own recursive moving average (Eq. 4) has feedback yet a finite impulse response — its pole at $z=1$ is cancelled by a zero. Decide FIR/IIR from $h[n]$ (or from $H(z)$ after cancelling), not from the form of the recursion — see [[concepts/fir-and-iir\|FIR and IIR]] |
| L9 notes §1.2 | "the transfer function has $N$ poles and $M$ zeros" | with input terms $b_0,\dots,b_{M-1}$ the numerator has $M-1$ finite zeros | an off-by-one in the count; count roots of the actual polynomials (and remember poles/zeros at $0$ or $\infty$) — see [[concepts/poles-and-zeros\|poles and zeros]] |
| L10 slide 11 | "Determine the frequency response $H(z)$" | "Determine the transfer function $H(z)$" | the frequency response is $H$ on the unit circle (a DTFT idea, after Midterm 1); the slide means the system function |

## Homework solutions

| where | as written | should be |
|---|---|---|
| HW1 #5(b) | $T(x_1)+T(x_2) = \{\dots,5,4,2,\underset{\uparrow}{1},2,4,5,\dots\}$ for $x_1 = 1$, $x_2 = n^2$, clip to $[0,4]$ | $\{\dots,5,5,2,\underset{\uparrow}{1},2,5,5,\dots\}$: at $n=\pm2$ it is $1 + \mathrm{clip}(4) = 5$. The conclusion (not linear) is unchanged, and the two sides already differ at $n=\pm2$. See [[homework/hw1\|HW1]]. |
| HW3 #1(b) | middle line $X_2(z) = \dfrac{(3/4)^3 z^{-2}}{1-(3/4)z^{-1}}$ | $\dfrac{(3/4)^5 z^{-2}}{1-(3/4)z^{-1}}$, ROC $\lvert z\rvert>\tfrac34$ — as in the line before it and the final answer. See [[homework/hw3\|HW3]] and [[0-toolkit/02-geometric-series\|geometric series]]. |
| HW1 #6(c) | the last line compares the unshifted output $y[n] = \{\underset{\uparrow}{0},1,2,3\}$ with $T\{x[n-1]\}$ | compare $y[n-1] = \{\underset{\uparrow}{0},0,1,2,3\}$ with $T\{x[n-1]\} = \{\underset{\uparrow}{-1},0,1,2\}$: they differ at $n=0$ and $n=4$. The verdict (time-varying) is unchanged. See [[homework/hw1\|HW1]]. |
| HW3 #4(a) | lists only the zero at $z = 3$ | $H(z) = \dfrac{z(z-3)}{(z-\frac12)(z+\frac23)}$ also has a zero at $z = 0$ (the key's own plot shows it). See [[homework/hw3\|HW3]] and [[concepts/poles-and-zeros\|poles and zeros]]. |
| HW4 #2 (necessity) | bounded input $x[n] = \mathrm{sgn}(h[-n]) = h[-n]/\lvert h[-n]\rvert$ | $x[n] = h^*[-n]/\lvert h[-n]\rvert$ (and $0$ where $h[-n]=0$). For real $h$ the two agree; for complex $h$ only the conjugate makes $y[0] = \sum\lvert h\rvert$ (e.g. $h = j^n u[n]$). See [[homework/hw4\|HW4]] and [[concepts/bibo-stability\|BIBO stability]]. |
| HW4 #3(d) | the output grows like $n\cos(\tfrac{\pi}{4}n+\varphi)$ | $H$ has complex coefficients, so only the $e^{-j\pi n/4}$ half of the cosine resonates: the growing part is $C(n+1)e^{-j\pi n/4}$ with $\lvert C\rvert = \tfrac12\sin\tfrac{\pi}{8} \approx 0.19$. The verdict (unbounded) and the chosen input are right. See [[homework/hw4\|HW4]]. |
| HW5 header (and HW2 statement) | due "Oct. 4, 2025"; HW2 #1 says "two systems" and lists three | due Sun Oct 4, **2026**; three systems | typos only |

## The official transform table

| where | as written | should be |
|---|---|---|
| `transform_tables.pdf`, Table 10, pair 3 | $u[-n-1] \leftrightarrow \dfrac{1}{1-z^{-1}}$, $\lvert z\rvert<1$ | $-u[-n-1] \leftrightarrow \dfrac{1}{1-z^{-1}}$, $\lvert z\rvert<1$ — pair 6 with $\alpha=1$. Without the minus sign every left-sided inverse comes out with the wrong sign. See [[supplements/transform-tables\|transform tables]]. |

> [!trap] The one to remember
> The left-sided pair carries a minus sign: $-\alpha^n u[-n-1] \leftrightarrow \dfrac{1}{1-\alpha z^{-1}}$, $\lvert z\rvert<\lvert\alpha\rvert$. The course summary sheet and Lecture 6 have it right; the printed Table 10 drops it for $\alpha=1$.

## Not errors, but read them carefully

- **FA2025 #8(b) — $e^{j2/3}$.** The pole is at angle $2/3$ rad, *not* $2\pi/3$. That is why $\cos(\tfrac{2\pi}{3}n)u[n]$ gives a bounded output (key: False). The key is right; the trap is in your eyes. See [[problems/unbounded-outputs-and-pole-matching|pole matching]].
- **FA2025 #1(d) — "an LTI system with a left-sided impulse response can never be causal" (key: True).** Correct with the Lecture 7 meaning of "left-sided" (an infinite-length sequence extending to $n=-\infty$). Read as the bare condition "$x[n]=0$ for $n>n_0$" it would also cover finite sequences such as $\delta[n]$, which is causal — so answer True, and add the one-line assumption only if you feel you must. See [[0-midterm-1/true-false-bank|true/false bank]].
- **FA2019 #4 and SP2021 #2 — the $n=0$ labels are right.** A draft errata list claimed these keys mislabel the first row of the convolution matrix as $n=0$. On the scans they do not. In FA2019 #4 *both* arrows sit under the first entries — $\{\underset{\uparrow}{1},-4,2,-1,3,1\} * \{\underset{\uparrow}{-1},1,-1\}$ (the arrow is under the "1" of "$-1$") — so $y = \{\underset{\uparrow}{-1},5,-7,7,-6,3,-2,-1\}$ starts at $n=0$, exactly as the key says. In SP2021 #2 ($h$ starts at $n=-1$) the key's "$\leftarrow n=0$" points at the *second* entry, $y[0] = 2$. The lesson is the reverse: read where each arrow really is before you start. See [[problems/finite-length-convolution|finite-length convolution]].
- **HW2 #1(a),(b) — linearity of a recursion needs "initially at rest".** The key checks only the right-hand side of each difference equation. That is enough *if* the system starts at rest; with a nonzero initial condition (say $y[-5]=1$) a zero input gives a nonzero output, which no linear system can do. See [[homework/hw2|HW2]] and [[concepts/lccde|LCCDE]].
- **FA2023 #8(b) — "stable for all $\alpha$".** True for the two-sided system whenever both poles survive; at the special values of $\alpha$ where a zero cancels a pole there is no annulus left between two poles, so the "two-sided" system of the question does not exist. See [[0-midterm-1/past-exams/fall-2023|FA2023]] and [[problems/parameters-for-stability|parameters for stability]].
- **Lecture 3 slides, Example 4.** The posted deck uses $y[n] = \max\{0, x[n]\}$; the annotated in-class deck uses $y[n] = x[n]\,x[0]$. Both are worked on [[1-signals-and-systems/03-system-properties|Lecture 3]].
- **"LSI" = "LTI".** Older keys and the Singer & Munson notes say linear shift-invariant; the lectures say linear time-invariant. Same thing — see [[supplements/notation-translation|notation translation]].
- **$X_d(\omega)$ vs $X(e^{j\omega})$, $(x*h)[n]$ vs $x[n]*h[n]$.** Course notation vs textbook notation for the DTFT and convolution; not a mistake.

### Sources for this page

Past Midterm 1 keys FA2025, SP2025, FA2024, SP2023, SP2021, FA2019 (checked by `verify/exams/run_all.py`); Lecture 2, 3, 4, 5, 7, 9, 10, 11 notes and Lecture 7 slides (pages rendered where the text extraction was ambiguous); HW1–HW4 solutions and the HW2/HW5 statements; `suppliment/transform_tables.pdf` p. 10 and `suppliment/review.pdf` p. 3. Corrections recomputed in `verify/hub/toolkit_errata.py`.
