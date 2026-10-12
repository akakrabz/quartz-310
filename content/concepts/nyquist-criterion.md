---
title: "Nyquist criterion"
description: "Bandlimited signals (X_a(Ω) = 0 for |Ω| > 2πB), the Nyquist criterion f_s > 2B (T < 1/(2B)) derived from non-overlapping spectral copies, the Nyquist rate 2B and Nyquist period 1/(2B), what happens above, at and below the rate (guard band, touching copies, aliasing), a worked two-tone example, the traps, and every lecture, exam problem, family page and demo that uses it."
tags: [concept, sampling, nyquist, aliasing, midterm-2]
aliases: ["Nyquist criterion", "Nyquist rate", "Nyquist frequency", "Nyquist period", "Nyquist interval", "Nyquist sampling theorem", "bandlimited", "bandlimited signal", "guard band", "aliasing"]
---

> [!key] Definition (Lecture 17)
> A continuous-time signal is **bandlimited** to $B$ hertz ($2\pi B$ rad/s) if its CTFT vanishes beyond that frequency:
> $$
> X_a(\Omega)=0\qquad\text{for }|\Omega|\gt2\pi B .
> $$
> Sampling it at $f_s=1/T$ copies $X_a$ every $2\pi/T$ rad/s ([[concepts/sampling|sampling]]). The copies do not overlap if and only if the right edge of the central copy is left of the left edge of the next one:
> $$
> 2\pi B\lt\frac{2\pi}{T}-2\pi B\quad\Longleftrightarrow\quad f_s\gt2B\quad\Longleftrightarrow\quad T\lt\frac{1}{2B}.
> $$
> This is the **Nyquist criterion**. $f_{\text{Nyquist}}=2B$ is the **Nyquist rate** (hertz) and $T_N=\frac{1}{2B}$ the **Nyquist period** (the exams' $T_N$, $T_{NYQ}$, "Nyquist interval"). The lectures to come show that above the Nyquist rate $x_a(t)$ can be recovered exactly from its samples.

Three equivalent ways to say it, all used on the exams:

| in terms of | condition | reading |
|---|---|---|
| hertz | $f_s\gt2B$ | sample faster than twice the highest frequency |
| rad/s | $2\pi B\lt\dfrac{\pi}{T}$ | the band edge lies below half the sampling frequency ($\pi/T=2\pi\cdot\frac{f_s}{2}$) |
| rad/sample | $2\pi BT\lt\pi$ | after $\omega=\Omega T$, the band edge lies inside the DTFT's period $[-\pi,\pi]$ |

The strict inequality matters at the boundary. Some books call $f_s/2$ the "Nyquist frequency" (the folding frequency); in this course **Nyquist rate** means $2B$, a property of the *signal*, and the criterion compares $f_s$ with it.

## Above, at and below

| sampling rate | spectral copies | $X_d(\omega)$ on $[-\pi,\pi]$ |
|---|---|---|
| $f_s\gt2B$ (above) | separated by a **guard band** $2\pi BT\lt\lvert\omega\rvert\lt2\pi-2\pi BT$ | $\frac1T\,X_a(\omega/T)$, zero in the guard band: a faithful, rescaled copy |
| $f_s=2B$ (exactly at) | **touch** at $\omega=\pm\pi$, no overlap, no guard band | $\frac1T\,X_a(\omega/T)$ fills the whole period; a box becomes a flat line, a triangle a zigzag |
| $f_s\lt2B$ (below) | **overlap and add** | a new shape — **aliasing**; the original spectrum cannot be read off |

[[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] draws all three (§6, the notes' Figure 3) and works them with numbers in Example 2 (§7: a $50$ Hz-bandlimited triangle at $150$, $100$ and $75$ Hz). Aliasing is only *named* here; what it does to individual frequencies, and what an ideal D/A converter then returns, is the subject of the next lectures. One consequence is already visible for a sinusoid: $\cos(\Omega_0t)$ sampled at $f_s$ gives the same sequence as $\cos\big((\pm\Omega_0+2\pi f_sk)t\big)$ for every integer $k$, so a tone above $f_s/2$ is indistinguishable from one below it (Lecture 17 §8).

> [!example] Two tones (checked)
> $x_a(t)=\cos(2\pi\cdot60\,t)+\cos(2\pi\cdot440\,t)$ (a mains hum and the A above middle C). The highest frequency is $B=440$ Hz, so the Nyquist rate is $880$ Hz and $T_N=\frac{1}{880}$ s.
> - At $f_s=1$ kHz (above the rate): $\omega_0=2\pi f_0/f_s$ puts the tones at $0.12\pi$ and $0.88\pi$, both inside $(0,\pi)$ in the right order. $x[n]=\cos(0.12\pi n)+\cos(0.88\pi n)$.
> - At $f_s=800$ Hz (below the rate): the $60$ Hz tone lands at $0.15\pi$, but the $440$ Hz tone lands at $2\pi\cdot\frac{440}{800}=1.1\pi\equiv-0.9\pi$, the same digital frequency as a $360$ Hz tone would give ($2\pi\cdot\frac{360}{800}=0.9\pi$, and the cosine is even). The samples $\cos(0.15\pi n)+\cos(0.9\pi n)$ are indistinguishable from those of $\cos(2\pi\cdot60\,t)+\cos(2\pi\cdot360\,t)$: the $440$ Hz tone has aliased to $360$ Hz.
> - At exactly $f_s=880$ Hz the $440$ Hz tone lands at $\omega=\pi$: $\cos(\pi n)=(-1)^n$ survives, but $\sin(2\pi\cdot440\,t)$ would sample to $\sin(\pi n)=0$ — the boundary case is not safe for every phase, which is why the criterion is strict.

> [!trap]
> - **$B$ is in hertz.** "Bandlimited to $\Omega_{\max}=1000\pi$ rad/s" is $B=500$ Hz, Nyquist rate $1000$ Hz, $T_N=1$ ms ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #9(a), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(a)) — not $2000\pi$ "Hz".
> - **Rate or period?** The Nyquist rate is $2B$ (Hz); the Nyquist period is $\frac{1}{2B}$ (s). Read which one is asked ([[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #5(a) asks for the largest $T$: $\frac{1}{8000}$ s for a $4$ kHz signal).
> - **Strict:** at exactly $f_s=2B$ the copies touch; no overlap, but a sine at $B$ samples to all zeros ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6(b)).
> - **The copies are not the aliasing.** Copies exist at every sampling rate; aliasing is their overlap. A flat $X_d$ ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b)) or an $X_d$ that is identically zero ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(c)) can be the sum of overlapping copies.
> - **Time scaling scales the Nyquist rate:** $x_c(2t)$ has twice the bandwidth and twice the Nyquist rate; $x_c(3t)$ three times, not a third ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(b) True, [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(b) False).
> - **Not every signal has one.** A signal that is not bandlimited (a rectangular pulse, say) aliases at every $f_s$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(d), False).
> - **The criterion is about overlap, not about what you keep.** Later problems allow aliasing outside a filter's passband and ask for a *larger* $T$ than $T_N$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(c), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #5(b), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #9(c)); those need the ideal filters and D/A conversion of the next lectures.

**Where it appears.**
- Lectures: [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]] (§6 the definition, the derivation and the three regimes; §7 Example 2 at $150$, $100$ and $75$ Hz; §8 a sinusoid's frequency modulo $2\pi$); the detailed treatment of aliasing and of recovering $x_a(t)$ comes in the lectures to come ([[4-sampling-and-reconstruction/index|Unit 4]]).
- Problem family: [[problems/sampling-and-the-nyquist-rate|Sampling and the Nyquist rate]].
- Past exams: Nyquist rate or period in [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #9(a), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(a), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(a), [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(a), [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #5(a); sampling at and below the rate in [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(b), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(b)–(c), [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b); True/False in the [[exams/midterm-2/true-false-bank|T/F bank]] §4 ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #1(b), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(b), (e), [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(d), [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #1(e)).
- Try it live: [[demos/sampling-explorer|sampling explorer]] (move $T$ across the Nyquist period and watch the copies touch, then overlap) · [[demos/practice-drills|practice drills]].

Related: [[concepts/sampling|sampling]] · [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/complex-exponential|complex exponential]]

### Sources for this page
Lecture 17 notes §2 (eqs. 17–21, Figure 3) and slides 8–12, with the annotated deck (the Nyquist derivation inked on slide 8); past-exam keys cited above. The two-tone example and the exam numbers are checked in `verify/L17_lecture.py`.
