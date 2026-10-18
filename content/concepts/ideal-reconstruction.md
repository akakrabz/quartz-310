---
title: "Ideal reconstruction (ideal D/A conversion)"
description: "Ideal digital-to-analog conversion: one pulse per sample, x_a(t) = Σ x[n] g(t − nT), with the ideal pulse g(t) = sinc(πt/T); the two views — sinc interpolation in time, a low-pass of height T on |Ω| ≤ π/T in frequency, Y_a(Ω) = T·Y_d(ΩT) — when it returns the sampled signal exactly (f_s > 2B), a worked two-sample example, the traps, and every lecture, exam problem and family page that uses it."
tags: [concept, sampling, reconstruction, sinc, midterm-2]
aliases: ["ideal reconstruction", "ideal D/A", "ideal D/A conversion", "ideal D/A converter", "D/A conversion", "digital-to-analog conversion", "ideal DAC", "D/C converter", "sinc interpolation", "reconstruction formula", "reconstruction filter", "interpolating pulse"]
---

> [!key] Definition (Lecture 18)
> An ideal digital-to-analog (D/A) converter with period $T$ puts each sample back at its instant $t=nT$ and fills in between with one **interpolating pulse** per sample,
> $$
> x_a(t)=\sum_{n=-\infty}^{\infty}x[n]\,g(t-nT),\qquad g(t)=\mathrm{sinc}\!\left(\frac{\pi t}{T}\right)=\frac{\sin(\pi t/T)}{\pi t/T},
> $$
> with the course's $\mathrm{sinc}(u)=\frac{\sin u}{u}$, $\mathrm{sinc}(0)=1$ (the tables and NumPy write the same pulse $\mathrm{sinc}(t/T)$ with $\frac{\sin\pi x}{\pi x}$). The sum is the convolution of the impulse train $x_s(t)=\sum_nx[n]\delta(t-nT)$ with $g(t)$, so the converter is the analog filter $g\leftrightarrow G_a$ driven by $x_s$; the ideal pulse is the one whose transform is an **ideal low-pass of height $T$**:
> $$
> G_a(\Omega)=\begin{cases}T, & |\Omega|\le\dfrac{\pi}{T}\\[4pt] 0, & |\Omega|\gt\dfrac{\pi}{T}.\end{cases}
> $$
> It keeps the central copy of the sampled spectrum $X_s(\Omega)=\frac1T\sum_kX_a(\Omega-\frac{2\pi k}{T})$, deletes the others, and cancels the $\frac1T$. The past exams also call it the ideal D/C converter or the ideal reconstruction filter.

Two views of the same operation:

| view | formula | what to do with it |
|---|---|---|
| time: **sinc interpolation** | $x_a(t)=\sum_nx[n]\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right)$ | one sinc per sample, centred at $nT$, as tall as $x[n]$, zero at every other $kT$; add them. $x_a(nT)=x[n]$ exactly; between samples every sample contributes |
| frequency: **low-pass of height $T$** | $Y_a(\Omega)=T\,Y_d(\Omega T)$ for $\lvert\Omega\rvert\lt\frac{\pi}{T}$, $0$ outside | take one period of the DTFT, relabel $\Omega=\omega/T$ (so $\pi\mapsto\frac{\pi}{T}$), multiply by $T$; a digital frequency $\omega$ comes out at $\frac{\omega}{2\pi}f_s$ Hz |

The frequency rule holds for any sequence, sampled or not, because $\sum_ny[n]g(t-nT)\leftrightarrow Y_d(\Omega T)G_a(\Omega)$ ([[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|Lecture 18]] §2). Its consequences: the output of an ideal D/A is always bandlimited to $\frac{\pi}{T}$ rad/s ($\frac{f_s}{2}$ Hz), and between an ideal A/D and an ideal D/A a digital filter acts on the analog input like $H_a(\Omega)=H_d(\Omega T)$ on $|\Omega|\lt\frac{\pi}{T}$, as long as no aliasing reaches its passband.

## When it is exact

> [!key] Recovery
> If $x[n]=x_a(nT)$ and $x_a$ is bandlimited to $B$ hertz with $f_s=\frac1T\gt2B$ (the [[concepts/nyquist-criterion|Nyquist criterion]]), the spectral copies do not overlap, $G_a$ cuts out exactly $X_a$, and
> $$
> x_a(t)=\sum_nx_a(nT)\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right)\qquad\text{for every }t .
> $$
> - **At exactly $f_s=2B$** the copies touch at $\pm\frac{\pi}{T}$: exact if $X_a$ vanishes at the band edge (a triangle), not for a sinusoid at exactly $B$ hertz ($\sin(\Omega_0t)$ at $f_s=\Omega_0/\pi$ gives $x[n]=0$).
> - **Below $2B$** the copies overlap, the box cuts out their sum, and the D/A rebuilds a different signal: [[concepts/aliasing|aliasing]] ([[4-sampling-and-reconstruction/19-aliasing|Lecture 19]]). A digital low-pass between the converters can still save the output if the overlap stays in its stopband, $\omega_c\le2\pi-\Omega_{\max}T$.

> [!example] Two samples (checked)
> $x[n]=\delta[n]+\delta[n-1]$, $T=1$ ms. Then $x_a(t)=\mathrm{sinc}\!\left(\frac{\pi t}{T}\right)+\mathrm{sinc}\!\left(\frac{\pi(t-T)}{T}\right)$: $x_a(0)=x_a(T)=1$, $x_a(kT)=0$ for every other integer $k$, and halfway between the two samples $x_a\!\left(\frac T2\right)=2\cdot\frac{2}{\pi}=\frac{4}{\pi}\approx1.27$ — higher than either sample, which straight-line interpolation could never give. In frequency, $X_d(\omega)=1+e^{-j\omega}$, so $X_a(\Omega)=T\left(1+e^{-j\Omega T}\right)$ for $|\Omega|\lt\frac{\pi}{T}=1000\pi$ rad/s and $0$ outside: $|X_a(\Omega)|=2T\cos\frac{\Omega T}{2}$, from $2T=2\cdot10^{-3}$ at $\Omega=0$ down to $0$ at the band edge $\pm1000\pi$, because $X_d(\pi)=1+e^{-j\pi}=0$.

> [!trap]
> - **Two sincs:** $\frac{\sin u}{u}$ (course, Lecture 18 eq. 13) versus $\frac{\sin\pi x}{\pi x}$ (tables, NumPy). Check zero crossings: they must fall at $t=kT$.
> - **A sample becomes a sinc, never an impulse** ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(c), [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(e)), and the sinc peaks at its own $nT$ ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #8(b)).
> - **The gain $T$:** the D/A undoes the sampler's $\frac1T$; $Y_a$ has the heights of $X_a$.
> - **Nothing above $\frac{\pi}{T}$:** $Y_a$ is one copy and stops at $\pm\frac{\pi}{T}$; a digital high-pass between converters is an analog band-pass.
> - **Not causal, not finite:** $g(t)\ne0$ for $t\lt0$ ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(c), False). The zero-order hold of [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #8(a) is a different, practical D/A that Snyder's Lecture 18 does not cover.

**Where it appears.**
- Lectures: [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|L18]] (§1 the reconstruction formula, §2 the convolution, §3 $G_a$ and $g$, §4 the sinc formula, §5 the slide-9 sketch, §6 the frequency rule, §7 the A/D → $H_d$ → D/A chain and the effective analog filter); [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]] (the sampled spectrum it inverts); [[4-sampling-and-reconstruction/19-aliasing|L19]] (what it returns below the Nyquist rate).
- Problem families: [[problems/digital-filtering-of-analog-signals|Digital filtering of analog signals]] · [[problems/sampling-and-the-nyquist-rate|Sampling and the Nyquist rate]].
- Homework: HW7 #4, worked in §5 of the [[exams/quiz-2|Quiz 2 review]].
- Past exams: the ideal D/A of a few samples in [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #8(b), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(c), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(c), [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(e); its non-causality in [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(c); samples read off a D/A output in [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #9(a); $Y_a$ sketches and the effective filter in [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5, [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #5, [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #4–#5, [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #5, [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #9; True/False in the [[exams/midterm-2/true-false-bank|T/F bank]] §5.

Related: [[concepts/sampling|sampling]] · [[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/aliasing|aliasing]] · [[concepts/frequency-response|frequency response]] · [[concepts/convolution|convolution]] · [[concepts/dtft|DTFT]]

### Sources for this page
Lecture 18 notes (eqs. 4–14, Figures 1–3) and slides 4–11 with the annotated deck; course review sheet, DAC entry; Singer & Munson §3.2; past-exam keys cited above. The two-sample example is checked in `verify/L18_lecture.py`.
