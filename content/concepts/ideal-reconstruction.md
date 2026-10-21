---
title: "Ideal reconstruction (ideal D/A conversion)"
description: "Ideal D/A: x_a(t) = Σ x[n] g(t − nT), g(t) = sinc(πt/T); sinc interpolation in time, a low-pass of height T on |Ω| ≤ π/T in frequency; exact when f_s > 2B; traps."
tags: [concept, sampling, reconstruction, sinc, midterm-2]
aliases: ["ideal reconstruction", "ideal D/A", "ideal D/A conversion", "ideal D/A converter", "D/A conversion", "digital-to-analog conversion", "ideal DAC", "D/C converter", "sinc interpolation", "reconstruction formula", "reconstruction filter", "interpolating pulse"]
---

> [!key] Definition (Lecture 18)
> $$
> x_a(t)=\sum_{n=-\infty}^{\infty}x[n]\,g(t-nT),\qquad g(t)=\mathrm{sinc}\!\left(\frac{\pi t}{T}\right)=\frac{\sin(\pi t/T)}{\pi t/T},
> $$
> $$
> G_a(\Omega)=\begin{cases}T, & |\Omega|\le\dfrac{\pi}{T}\\[4pt] 0, & |\Omega|\gt\dfrac{\pi}{T}.\end{cases}
> $$
> Keeps the central copy of $X_s(\Omega)$ and cancels its $\frac1T$. Exams also say ideal D/C converter or reconstruction filter.

| view | formula |
|---|---|
| time: **sinc interpolation** | one sinc per sample at $nT$, height $x[n]$, zero at all other $kT$; $x_a(nT)=x[n]$ |
| frequency: **low-pass of height $T$** | $Y_a(\Omega)=T\,Y_d(\Omega T)$ for $\lvert\Omega\rvert\lt\frac{\pi}{T}$, $0$ outside |

- **Exact recovery** if $x_a$ is bandlimited to $B$ and $f_s\gt2B$ ([[concepts/nyquist-criterion|Nyquist criterion]]):

$$
x_a(t)=\sum_nx_a(nT)\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right).
$$

- **Below $2B$:** the box cuts out overlapping copies: [[concepts/aliasing|aliasing]].
- **A/D → $H_d$ → D/A** acts as $H_a(\Omega)=H_d(\Omega T)$ on $|\Omega|\lt\frac{\pi}{T}$ if no aliasing reaches the passband.

> [!example] Two samples: $x[n]=\delta[n]+\delta[n-1]$, $T=1$ ms
> $x_a(0)=x_a(T)=1$, $x_a(kT)=0$ otherwise, $x_a\!\left(\frac T2\right)=\frac{4}{\pi}\approx1.27$. In frequency $X_a(\Omega)=T\left(1+e^{-j\Omega T}\right)$ for $|\Omega|\lt1000\pi$, zero at the band edge since $X_d(\pi)=0$.

> [!trap]
> - Two sincs: $\frac{\sin u}{u}$ (course) vs $\frac{\sin\pi x}{\pi x}$ (tables, NumPy); zero crossings must fall at $t=kT$.
> - A sample becomes a sinc, never an impulse ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(c), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #8(b)).
> - Gain $T$ undoes the sampler's $\frac1T$; output stops at $\pm\frac{\pi}{T}$.
> - $g(t)$ is not causal ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(c)).

**Where it appears:** [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|L18]], [[4-sampling-and-reconstruction/19-aliasing|L19]]; [[problems/digital-filtering-of-analog-signals|digital filtering of analog signals]]; [[exams/quiz-2|Quiz 2 review]] (HW7 #4); [[exams/midterm-2/true-false-bank|T/F bank]].

## Related
[[concepts/sampling|sampling]] · [[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/aliasing|aliasing]] · [[concepts/frequency-response|frequency response]]

### Sources for this page
Lecture 18 notes (eqs. 4–14, Figures 1–3), slides 4–11; Singer–Munson §3.2; Midterm 2 keys cited.
