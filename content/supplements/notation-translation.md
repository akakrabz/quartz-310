---
title: "Notation translation"
description: "The course's notation translation table (ece310_notation.pdf) — lectures vs Singer & Munson vs Manolakis & Ingle vs Oppenheim & Schafer vs Proakis & Manolakis vs the Kamalabadi videos — plus the Midterm 1 conventions that differ between lectures, old exams, the summary sheet and scipy."
tags: [supplement, signals, systems]
---

*Supplement · `suppliment/ece310_notation.pdf` ("ECE 310 Notation Translation Table, Spring 2019", 1 page)*

Every source writes the same objects differently. The official table below covers signals and transforms across the textbooks; the second table adds the Midterm 1 conventions that trip people up when they mix lecture notes, old exam keys and Python.

## The official table

| | lectures, exams & homework | Singer & Munson notes | Manolakis & Ingle | Oppenheim & Schafer | Proakis & Manolakis* | Kamalabadi videos |
|---|---|---|---|---|---|---|
| continuous-time signal | $x_c(t)$ | $x(t)$ | $x(t)$ | $x_c(t)$ | $x_a(t)$ | $x_a(t)$ |
| discrete-time signal (sequence) | $x[n]$ | $x[n]$ | $x[n]$ | $x[n]$ | $x(n)$ | $x(n)$ |
| CT Fourier transform | $X_c(\Omega)$ | $X_c(\Omega)$ | $X(j\Omega)$ | $X_c(j\Omega)$ | $X(F)$ | $X_a(\Omega)$ |
| DT Fourier transform (DTFT) | $X_d(\omega)$ | $X_d(\omega)$ | $X(e^{j\omega})$ | $X(e^{j\omega})$ | $X(\omega)$ | $X_d(\omega)$ |
| DFT coefficient | $X[k]$ | $X[k]$ | $X[k]$ | $X[k]$ | $X(k)$ | $X(m)$ |
| convolution sum | $(x*h)[n]$ | none | $x[n]*h[n]$ | $x[n]*h[n]$ | $x(n)*h(n)$ | $x(n)*h(n)$ |
| modulo operation | $\langle k\rangle_N$ | $\langle\langle k\rangle\rangle_N$ | $\langle k\rangle_N$ | $((k))_N$ | $k \pmod N$ | $\langle k\rangle_N$ |

\*Proakis & Manolakis often use the natural frequency $F$ (Hz) instead of the radian frequency $\Omega = 2\pi F$ in continuous time.

How to read it: $X_d(\omega)$ and $X(e^{j\omega})$ are the same function — the z-transform evaluated on the unit circle, $X_d(\omega) = X(z)\big|_{z=e^{j\omega}}$, when the ROC contains $\lvert z\rvert = 1$. Parentheses $x(n)$ for a sequence (Proakis) mean exactly $x[n]$. The DTFT, DFT and modulo rows are after Midterm 1.

## Midterm 1 conventions that differ between sources

| object | lectures (this site) | where else you will see something different |
|---|---|---|
| linear time-invariant system | LTI | "LSI" (linear shift-invariant) in older exam keys, the [[supplements/course-summary\|course summary]] and the [[supplements/singer-munson-notes\|Singer & Munson notes]] — identical meaning |
| response to $\delta[n]$ | impulse response $h[n]$ | "unit pulse response" (Singer & Munson) |
| $H(z) = Y(z)/X(z)$ | transfer function | "system function" (Singer & Munson, Oppenheim & Schafer) |
| LCCDE | $y[n] + \sum_{k=1}^{N}a_k y[n-k] = \sum_{k} b_k x[n-k]$ (Lecture 9), $H = \dfrac{\sum b_k z^{-k}}{1+\sum a_k z^{-k}}$ | Lecture 5: $y[n] = \sum_i b_i y[n-i] + \sum_j c_j x[n-j]$ — feedback sign flipped **and** the letter $b$ means feedback. The summary sheet and `scipy.signal.lfilter(b, a, x)` use Lecture 9's signs. |
| convolution | $x[n]*h[n]$, also $(x*h)[n]$ | both appear on exams; same operation |
| the $n=0$ sample | arrow under it: $\{1,\underset{\uparrow}{2},3\}$ | bold or underline (Lecture 2 shows all three); keys sometimes write "$\leftarrow n=0$" beside a column vector |
| imaginary unit | $j$ | $i$ in math courses |
| z-transform | two-sided $\sum_{n=-\infty}^{\infty}x[n]z^{-n}$, always with an ROC | Singer & Munson start with the one-sided $\sum_{n\ge0}$ |
| transforms | written in powers of $z^{-1}$: $\dfrac{1}{1-\alpha z^{-1}}$ | positive powers $\dfrac{z}{z-\alpha}$ in some keys (e.g. SP2025 #6, $H = \dfrac{z}{z-e^{j\pi/4}}$); `scipy.signal.tf2zpk` reads coefficient lists as positive powers — pad to equal length ([[0-toolkit/04-factoring-and-long-division\|factoring]]) |
| ROC | "ROC: $\lvert z\rvert > a$" | "$R_x$", "$\mathrm{ROC}_X$" in property tables; "$z\neq0$" for finite right-sided signals |
| unstable with poles on $\lvert z\rvert=1$ | "marginally stable" = **not** BIBO stable | Singer & Munson: "in our terminology, simply unstable" — same verdict ([[concepts/marginal-stability\|marginal stability]]) |

> [!trap] The one that costs points
> Moving a feedback term across the equals sign flips its sign. From $y[n] = \tfrac43 y[n-1] + \tfrac43 y[n-2] + x[n] - x[n-2]$ ([[0-midterm-1/past-exams/fall-2025|FA2025 #6]]) the denominator is $1 - \tfrac43 z^{-1} - \tfrac43 z^{-2}$, and in Python `a = [1, -4/3, -4/3]`. See [[concepts/lccde|LCCDE]].

### Sources for this page

`suppliment/ece310_notation.pdf` (rendered to confirm every entry); `suppliment/review.pdf` p. 1 (textbook vs class notation); Lecture 2, 5, 9 and 11 notes; Singer & Munson §3.4, §3.8.1, §4.2, §4.14; SP2025 #6 and FA2025 #6 keys.
