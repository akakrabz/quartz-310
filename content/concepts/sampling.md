---
title: "Sampling (ideal A/D conversion)"
description: "Ideal sampling x[n] = x_a(nT), the impulse-train model x_s(t), spectral copies every 2π/T scaled by 1/T, the axis change ω = ΩT, the sketching recipe and traps."
tags: [concept, sampling, ctft, dtft, midterm-2]
aliases: ["sampling", "ideal sampling", "impulse train", "spectral copies", "sampled spectrum", "A/D conversion", "analog-to-digital conversion", "sampling period", "sampling frequency"]
---

> [!key] Definition (Lecture 17)
> Sampling period $T$, sampling frequency $f_s=1/T$:
> $$
> x[n]=x_a(nT),\qquad x_s(t)=\sum_nx_a(nT)\,\delta(t-nT)
> $$
> $$
> X_s(\Omega)=\frac1T\sum_{n=-\infty}^{\infty}X_a\!\left(\Omega-\frac{2\pi}{T}n\right),\qquad X_d(\omega)=X_s(\Omega)\Big|_{\Omega=\omega/T},\qquad\omega=\Omega T .
> $$
> Copies every $2\pi/T$ rad/s (every $2\pi$ in $\omega$), each scaled by $1/T$; overlapping copies **add**.

> [!recipe] From $X_a(\Omega)$ to $X_d(\omega)$
> 1. Scale the axis: $\omega=\Omega T$ (band edge $2\pi B\mapsto2\pi BT$; $\omega=\pi$ is $f_s/2$).
> 2. Copy every $2\pi$.
> 3. Scale heights by $1/T$.
> 4. Add overlaps.
> 5. Read off $[-\pi,\pi]$.

> [!example] 2 kHz triangle $X_a(\Omega)=1-\frac{|\Omega|}{4000\pi}$, $|\Omega|\le4000\pi$
> - $f_s=10$ kHz: triangle of height $10\,000$ on $|\omega|\le0.4\pi$, guard band beyond.
> - $f_s=4$ kHz: $X_d(\omega)=4000\left(1-\frac{|\omega|}{\pi}\right)$; copies touch at $\pm\pi$.
> - $f_s=3$ kHz: trapezoid, $3000\left(1-\frac{3|\omega|}{4\pi}\right)$ out to $\frac{2\pi}{3}$, then $1500$ to $\pi$: aliasing.

> [!trap]
> - **Forgetting $1/T$:** heights scale by $f_s$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(b), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #5(a)).
> - **Two spacings:** $2\pi/T$ in $\Omega$, $2\pi$ in $\omega$.
> - **Copies add**, can sum to flat ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b)) or zero ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(c)).
> - **Larger $T$ stretches $X_d$ outward** and lowers it ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(e)).
> - **Frequency known only modulo $2\pi$:** $\cos(\Omega_0t)$ and $\cos\big((\Omega_0+2\pi f_sk)t\big)$ give the same samples ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #3).

**Where it appears:** [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]], then [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|L18]], [[4-sampling-and-reconstruction/19-aliasing|L19]]; [[problems/sampling-and-the-nyquist-rate|sampling family]]; [[demos/sampling-explorer|sampling explorer]].

## Related
[[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/aliasing|aliasing]] · [[concepts/ideal-reconstruction|ideal reconstruction]] · [[concepts/dtft|DTFT]] · [[concepts/discrete-time-signal|discrete-time signal]]

### Sources for this page
Lecture 17 notes §1–1.1 (eqs. 1–16, Figures 1–2), slides 3–7; Singer–Munson §3.2; Midterm 2 keys cited.
