---
title: "Aliasing"
description: "Sampling below the Nyquist rate overlaps the spectral copies; x[n] takes a false appearance and ideal D/A returns a different signal. Spectrum view, sinusoid folding rule, signs, traps."
tags: [concept, sampling, aliasing, nyquist, midterm-2]
aliases: ["aliasing effect", "alias", "aliased", "principal alias", "folding", "folding frequency", "anti-aliasing filter"]
---

> [!key] Definition (Lecture 19)
> Sampled below the Nyquist rate ($f_s\lt2B$), the copies in $X_d(\omega)=\frac1T\sum_kX_a\!\left(\frac{\omega-2\pi k}{T}\right)$ overlap and $x[n]$ takes on a false appearance, an **alias**. Ideal D/A then returns a different signal; aliasing **cannot be undone**. Recovered spectrum:
> $$
> \hat X_a(\Omega)=\sum_kX_a\!\left(\Omega-\frac{2\pi k}{T}\right)\ \text{ for }|\Omega|\le\frac{\pi}{T},\qquad 0\ \text{ beyond}.
> $$

> [!recipe] Folding rule
> Tone at $f_0$ sampled at $f_s$ returns at $\hat f=f_0-kf_s$, the value closest to $0$. In rad: reduce $\Omega_0T$ into $(-\pi,\pi]$ (the **principal alias** $\hat\omega$) and divide by $T$. Keep the sign of $\hat f$ for a sine or a phase.

| sampled signal | same samples as |
|---|---|
| $\cos(\omega_0n)$ | $\cos\big((\pm\omega_0+2\pi k)n\big)$ |
| $\sin(\omega_0n)$ | $\sin\big((\omega_0+2\pi k)n\big)$; $-\omega_0+2\pi k$ gives $-\sin(\omega_0n)$ |

> [!example] Lecture 19: $\sin(100\pi t)$ (50 Hz)
> - $160$, $120$ Hz: returned unchanged.
> - $80$ Hz: $\omega_0=\frac{5\pi}{4}\equiv-\frac{3\pi}{4}$, D/A returns $-\sin(60\pi t)$.
> - $40$ Hz: $\omega_0=\frac{5\pi}{2}\equiv\frac{\pi}{2}$, D/A returns $\sin(20\pi t)$.

- **At exactly $f_s=2B$:** $\sin(\Omega_0t)$ at $f_s=\Omega_0/\pi$ samples to $\sin(\pi n)=0$; hence the strict $f_s\gt2B$.
- **Avoid it:** sample faster, or (practice, Singer–Munson) an analog anti-aliasing low-pass before the A/D. Exams also accept aliasing a digital filter will delete ([[problems/digital-filtering-of-analog-signals|digital filtering of analog signals]]).

> [!trap]
> - Aliasing is the overlap, not the copies; overlap can sum to a constant ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b)) or zero ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(c)).
> - Signs: for a sine, only $+\omega_0$ reproduces the samples ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #8(a), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6(c)).
> - $\hat\Omega$ is in rad/s: $-60\pi$ rad/s is $-30$ Hz.
> - "Which $T$ give these samples" accepts aliased $T$; "which $T$ give this D/A output" usually does not ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6).

**Where it appears:** [[4-sampling-and-reconstruction/19-aliasing|L19]], [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]]; [[problems/sampling-and-the-nyquist-rate|sampling family]]; [[exams/midterm-2/true-false-bank|T/F bank]]; [[demos/sampling-explorer|sampling explorer]].

## Related
[[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/sampling|sampling]] · [[concepts/ideal-reconstruction|ideal reconstruction]] · [[concepts/dtft|DTFT]]

### Sources for this page
Lecture 19 notes §1–2.1 (eqs. 1–17), slides 3–19; Lecture 17 §2; HW7 #4; Singer–Munson §3.2; Midterm 2 keys cited.
