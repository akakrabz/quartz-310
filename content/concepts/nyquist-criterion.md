---
title: "Nyquist criterion"
description: "Bandlimited signals (X_a(Ω) = 0 for |Ω| > 2πB), the Nyquist criterion f_s > 2B, Nyquist rate 2B and period 1/(2B), sampling above, at and below the rate, traps."
tags: [concept, sampling, nyquist, aliasing, midterm-2]
aliases: ["Nyquist criterion", "Nyquist rate", "Nyquist frequency", "Nyquist period", "Nyquist interval", "Nyquist sampling theorem", "bandlimited", "bandlimited signal", "guard band"]
---

> [!key] Definition (Lecture 17)
> $x_a(t)$ is **bandlimited** to $B$ Hz if
> $$
> X_a(\Omega)=0\qquad\text{for }|\Omega|\gt2\pi B .
> $$
> Sampling copies $X_a$ every $2\pi/T$ rad/s ([[concepts/sampling|sampling]]). The copies do not overlap iff
> $$
> 2\pi B\lt\frac{2\pi}{T}-2\pi B\quad\Longleftrightarrow\quad f_s\gt2B\quad\Longleftrightarrow\quad T\lt\frac{1}{2B}.
> $$
> **Nyquist rate** $2B$ (Hz); **Nyquist period** $T_N=\frac{1}{2B}$. Equivalent: $2\pi BT\lt\pi$ (band edge inside $[-\pi,\pi]$ after $\omega=\Omega T$).

| sampling rate | copies | $X_d(\omega)$ on $[-\pi,\pi]$ |
|---|---|---|
| $f_s\gt2B$ | separated by a **guard band** | $\frac1T\,X_a(\omega/T)$, faithful |
| $f_s=2B$ | **touch** at $\omega=\pm\pi$ | $\frac1T\,X_a(\omega/T)$ fills the period |
| $f_s\lt2B$ | **overlap and add** | new shape: [[concepts/aliasing|aliasing]] |

> [!example] Two tones
> $x_a(t)=\cos(2\pi\cdot60\,t)+\cos(2\pi\cdot440\,t)$: $B=440$ Hz, Nyquist rate $880$ Hz.
> - $f_s=1$ kHz: tones at $0.12\pi$ and $0.88\pi$.
> - $f_s=800$ Hz: $440$ Hz lands at $1.1\pi\equiv-0.9\pi$, same as a $360$ Hz tone: aliased.
> - $f_s=880$ Hz: $\sin(2\pi\cdot440\,t)$ samples to $\sin(\pi n)=0$; the criterion is strict.

> [!trap]
> - **$B$ is in hertz:** $\Omega_{\max}=1000\pi$ rad/s means $B=500$ Hz, rate $1000$ Hz, $T_N=1$ ms ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(a)).
> - **Rate or period?** [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #5(a) asks for the largest $T$: $\frac{1}{8000}$ s for a $4$ kHz signal.
> - **Copies are not aliasing;** aliasing is their overlap. Overlapping copies can sum to a flat or zero $X_d$ ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(c)).
> - **Time scaling scales the rate:** $x_c(3t)$ has three times the Nyquist rate ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(b)). A non-bandlimited signal aliases at every $f_s$.
> - Some exams allow aliasing outside a filter's passband and ask for $T\gt T_N$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(c)).

**Where it appears:** [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]], [[problems/sampling-and-the-nyquist-rate|sampling family]], [[exams/midterm-2/true-false-bank|T/F bank]], [[demos/sampling-explorer|sampling explorer]].

## Related
[[concepts/sampling|sampling]] · [[concepts/aliasing|aliasing]] · [[concepts/ideal-reconstruction|ideal reconstruction]] · [[concepts/dtft|DTFT]]

### Sources for this page
Lecture 17 notes §2 (eqs. 17–21, Figure 3), slides 8–12; Midterm 2 keys cited.
