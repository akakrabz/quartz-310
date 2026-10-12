---
title: "Sampling (ideal A/D conversion)"
description: "Ideal sampling x[n] = x_a(nT) and its impulse-train model x_s(t); what it does to the spectrum — copies of X_a(Ω) every 2π/T scaled by 1/T, then the axis change ω = ΩT that gives the DTFT X_d(ω); the recipe for sketching X_d, a worked triangle at three rates, the traps, and every lecture, exam problem, family page and demo that uses it."
tags: [concept, sampling, ctft, dtft, midterm-2]
aliases: ["sampling", "ideal sampling", "impulse train", "spectral copies", "sampled spectrum", "A/D conversion", "analog-to-digital conversion", "sampling period", "sampling frequency"]
---

> [!key] Definition (Lecture 17)
> Ideal sampling with **sampling period** $T$ (seconds) and **sampling frequency** $f_s=1/T$ (hertz) turns a continuous-time signal into a sequence,
> $$
> x[n]=x_a(nT),\qquad-\infty\lt n\lt\infty .
> $$
> Its model is multiplication by an **impulse train**, $x_s(t)=x_a(t)\sum_n\delta(t-nT)=\sum_nx_a(nT)\,\delta(t-nT)$, a continuous-time signal whose impulse areas are the samples. In the frequency domain,
> $$
> X_s(\Omega)=\frac1T\sum_{n=-\infty}^{\infty}X_a\!\left(\Omega-\frac{2\pi}{T}n\right),\qquad X_d(\omega)=X_s(\Omega)\Big|_{\Omega=\omega/T}=\frac1T\sum_{n=-\infty}^{\infty}X_a\!\left(\frac{\omega-2\pi n}{T}\right),\qquad\omega=\Omega T .
> $$
> Sampling **copies** the analog spectrum every $2\pi/T$ rad/s ($f_s$ Hz), **scales** every copy by $1/T$, and the copies **add** where they overlap. On the digital axis $\omega=\Omega T$ the copies sit every $2\pi$: that is where the $2\pi$-periodicity of the DTFT of a sampled signal comes from.

Three signals, three spectra:

| signal | lives in | spectrum | what it is |
|---|---|---|---|
| $x_a(t)$ | continuous time | CTFT $X_a(\Omega)$, $\Omega$ in rad/s | the analog signal (the notes write $x(t)$; the exams write $x_a(t)$, $X_a(\Omega)$ or $x_c(t)$, $X_c(\Omega)$) |
| $x_s(t)=\sum_nx_a(nT)\,\delta(t-nT)$ | continuous time | CTFT $X_s(\Omega)$, periodic with period $2\pi/T$ | the impulse-train model: zero between samples, impulses of area $x_a(nT)$ |
| $x[n]=x_a(nT)$ | discrete time | DTFT $X_d(\omega)=X_s(\omega/T)$, periodic with period $2\pi$ | the stored sequence; same numbers as the areas of $x_s$ |

The copies formula comes from the windowing property, $x_a(t)f(t)\leftrightarrow\frac{1}{2\pi}X_a*F_a$, with the impulse train's transform $F_a(\Omega)=\frac{2\pi}{T}\sum_n\delta(\Omega-\frac{2\pi}{T}n)$ ([[concepts/dtft-properties|DTFT properties]] has the discrete-time version); the axis change is exact because $X_s(\Omega)=\sum_nx_a(nT)e^{-j\Omega nT}=\sum_nx[n]e^{-j(\Omega T)n}$ is the DTFT sum at $\omega=\Omega T$. Both derivations are in [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] §3 and §5.

## The sketching recipe

> [!recipe] From $X_a(\Omega)$ to $X_d(\omega)$
> 1. **Scale the axis by $T$:** $\omega=\Omega T$; a band edge $2\pi B$ lands at $2\pi BT$, and $\omega=\pi$ corresponds to $\Omega=\pi/T$, i.e. $f_s/2$.
> 2. **Copy every $2\pi$** (every $2\pi/T$ if you are sketching $X_s(\Omega)$ instead).
> 3. **Scale the heights by $1/T$:** a height of $1$ becomes $f_s$.
> 4. **Add the overlaps.** Where two copies are both nonzero, the DTFT is their sum; straight edges add to straight edges, and two triangles can add to a flat segment.
> 5. **Read off $-\pi\le\omega\le\pi$**, the period an exam asks for.
>
> When the copies do not overlap, $X_d(\omega)=\frac1T\,X_a\!\left(\frac{\omega}{T}\right)$ on $|\omega|\le\pi$: the analog spectrum, squeezed by $T$ and raised by $1/T$. When they do, see [[concepts/nyquist-criterion|Nyquist criterion]].

> [!example] A 2 kHz triangle at three sampling rates (checked)
> $X_a(\Omega)=1-\frac{|\Omega|}{4000\pi}$ on $|\Omega|\le4000\pi$ (bandlimit $B=2$ kHz, Nyquist rate $4$ kHz).
> - **$f_s=10$ kHz** ($T=0.1$ ms): the edge $4000\pi$ lands at $4000\pi\cdot10^{-4}=0.4\pi$ and the height is $\frac1T=10^4$. $X_d$ is a triangle of height $10\,000$ on $|\omega|\le0.4\pi$ and zero on $0.4\pi\lt|\omega|\le\pi$ — a guard band.
> - **$f_s=4$ kHz** ($T=0.25$ ms): edge at $\pi$, height $4000$: $X_d(\omega)=4000\left(1-\frac{|\omega|}{\pi}\right)$ on $[-\pi,\pi]$; the copies touch at $\pm\pi$ and nothing overlaps.
> - **$f_s=3$ kHz** ($T=\frac13$ ms): edge at $\frac{4\pi}{3}\gt\pi$, height $3000$. On $\frac{2\pi}{3}\le|\omega|\le\pi$ the copies centred at $0$ and $\pm2\pi$ both contribute and add to the constant $3000\left(2-\frac{2\pi}{4\pi/3}\right)=1500$; $X_d$ is a trapezoid, $3000\left(1-\frac{3|\omega|}{4\pi}\right)$ out to $\frac{2\pi}{3}$ and $1500$ from there to $\pi$. The triangle's shape is gone: aliasing.
>
> A single tone follows the same rule: $\cos(2\pi\cdot1000\,t)$ sampled at $10$ kHz is $\cos(0.2\pi n)$, impulses at $\pm0.2\pi$ (repeated every $2\pi$), because $\omega_0=\Omega_0T=2000\pi\cdot10^{-4}$.

> [!trap]
> - **Forgetting the $1/T$.** $X_d$ of a sampled signal has height $f_s$ times that of $X_a$; the ideal D/A of the next lectures puts the $T$ back. Every key labels it: $1000$ and $500$ in [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(b), $300$ in [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #5(a), $5000$ in [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b).
> - **Two axes, two spacings:** $2\pi/T$ in $\Omega$, $2\pi$ in $\omega$. "$X_d(\Omega)$" is a slip (the FA2024 key makes it).
> - **The copies add.** Drawing overlapping copies side by side instead of summing them is wrong; the sum can be flat ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b): $5000$ everywhere) or zero ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(c): an odd spectrum cancels itself).
> - **A larger $T$ stretches $X_d$ outward** ($\omega=\Omega T$) and lowers it; it does not shrink it ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(e), False).
> - **$x_s(t)$ is not $x[n]$.** It is a continuous-time signal (a train of impulses); $x[n]$ is the list of their areas. $X_s$ and $X_d$ are the same function on two differently labelled axes.
> - **After sampling, a frequency is known only modulo $2\pi$:** $\cos(\Omega_0t)$ and $\cos\big((\Omega_0+2\pi f_sk)t\big)$ give the same samples; so does $\cos(-\Omega_0t)$, and for a sine the sign flips ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #3, [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6(a)).

**Where it appears.**
- Lectures: [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]] (§1–§2 the model, §3 the copies formula and its derivation, §4 Example 1, §5 $\omega=\Omega T$ and $X_d$, §7 Example 2, §8 sampled sinusoids); [[1-signals-and-systems/01-digital-signals|L1]] (sampling defined); [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]] (the CTFT), [[3-fourier-analysis/14-dtft-properties|L14]] (windowing, impulses in frequency). What comes back out of the samples — ideal D/A conversion and aliasing in detail — is in the lectures to come ([[4-sampling-and-reconstruction/index|Unit 4]]).
- Problem family: [[problems/sampling-and-the-nyquist-rate|Sampling and the Nyquist rate]].
- Past exams: sketches of $X_d$ after sampling in [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(b), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #5(a), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(b)–(c), [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b)–(c), [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #4; sampled sinusoids in [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #3, [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6(a), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #8(a), [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(a); True/False in the [[exams/midterm-2/true-false-bank|T/F bank]] §4.
- Try it live: [[demos/sampling-explorer|sampling explorer]] (drag $T$ and watch the copies move) · [[demos/practice-drills|practice drills]] · the course notebook `demo_sampling` ([[supplements/demo-notebooks|demo notebooks]]: a $30$ Hz cosine sampled at $100$ Hz and its aliases at $70$, $130$ and $170$ Hz, all exactly $\cos(0.6\pi n)$, since $1.4\pi\equiv-0.6\pi$, $2.6\pi\equiv0.6\pi$, $3.4\pi\equiv-0.6\pi$ and the cosine is even).

Related: [[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/discrete-time-signal|discrete-time signal]] · [[concepts/complex-exponential|complex exponential]]

### Sources for this page
Lecture 17 notes §1 (eqs. 1–11, Figure 1), §1.1 (eqs. 12–16, Figure 2) and slides 3–7, with the annotated deck (Example 1 inked); course review sheet, ADC entry; Singer & Munson §3.2; past-exam keys cited above. The three-rate example, the tone and the notebook's aliases are checked in `verify/L17_lecture.py`.
