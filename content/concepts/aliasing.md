---
title: "Aliasing"
description: "Aliasing (Lecture 19): sampling below the Nyquist rate makes the spectral copies overlap, so x[n] takes on a false appearance and an ideal D/A returns a different signal; the spectrum view (overlapping copies add, frequencies above π/T fold back), the sinusoid view (ω0 + 2πk and, for a cosine, −ω0 + 2πk give the same samples; the principal alias in (−π, π] and the recovered frequency f0 − k·f_s closest to 0), the sign of a sine, sampling at exactly the Nyquist rate, how to avoid it, the traps, and every lecture, exam problem and family page that uses it."
tags: [concept, sampling, aliasing, nyquist, midterm-2]
aliases: ["aliasing effect", "alias", "aliased", "principal alias", "folding", "folding frequency", "anti-aliasing filter"]
---

> [!key] Definition (Lecture 19)
> A bandlimited signal sampled **above** its Nyquist rate, $f_s\gt2B$, can be recovered exactly from its samples by ideal D/A conversion. Sampled **below** it, the spectral copies of $X_d(\omega)=\frac1T\sum_kX_a\!\left(\frac{\omega-2\pi k}{T}\right)$ overlap, the period $[-\pi,\pi]$ no longer holds the shape of $X_a$, and $x[n]$ takes on a false appearance, an **alias**. This is **aliasing**. An ideal D/A then rebuilds a different, corrupted signal, and since different analog signals now have identical samples, **aliasing cannot be undone** from $x[n]$.

## Two views

**The spectrum view** ([[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] §6–7, [[4-sampling-and-reconstruction/19-aliasing|Lecture 19]] §8). Overlapping copies **add**. After an ideal D/A at the same $T$ ([[concepts/ideal-reconstruction|ideal reconstruction]]), the recovered spectrum is
$$
\hat X_a(\Omega)=\sum_kX_a\!\left(\Omega-\frac{2\pi k}{T}\right)\ \text{ for }|\Omega|\le\frac{\pi}{T},\qquad 0\ \text{ beyond}.
$$
It has lost everything above $\frac{\pi}{T}$ (half the sampling frequency, in rad/s), and below $\frac{\pi}{T}$ it carries those high frequencies folded back about $\frac{\pi}{T}$ on top of the true ones. Example: a triangle reaching $100\pi$ rad/s sampled at $75$ Hz comes back as a trapezoid, flat at $\frac12$ on $50\pi\le|\Omega|\le75\pi$ and zero beyond $75\pi$.

**The sinusoid view** (Lecture 19 §4–§6). Sampling $\sin(\Omega_0t)$ or $\cos(\Omega_0t)$ gives frequency $\omega_0=\Omega_0T$, and a sequence only knows its frequency modulo $2\pi$:

| sampled signal | same samples as | the D/A returns |
|---|---|---|
| $\cos(\omega_0n)$ | $\cos\big((\pm\omega_0+2\pi k)n\big)$, any integer $k$ | $\cos(\hat\Omega t)$, $\hat\Omega=\hat\omega/T$ |
| $\sin(\omega_0n)$ | $\sin\big((\omega_0+2\pi k)n\big)$ only; $-\omega_0+2\pi k$ gives $-\sin(\omega_0n)$ | $\sin(\hat\Omega t)$, negative $\hat\Omega$ meaning $-\sin(\lvert\hat\Omega\rvert t)$ |
| $\cos(\omega_0n+\phi)$, $\phi$ not a multiple of $\pi$ | like the sine: only $+\omega_0+2\pi k$ | $\cos(\hat\Omega t+\phi)$, negative $\hat\Omega$ meaning $\cos(\lvert\hat\Omega\rvert t-\phi)$ |

Here $\hat\omega\in(-\pi,\pi]$ is the **principal alias**, $\hat\omega=\omega_0-2\pi k$ with $k$ the integer nearest to $\frac{\omega_0}{2\pi}$.

> [!recipe] The folding rule
> In hertz: **a tone at $f_0$ sampled at $f_s$ comes back at $\hat f=f_0-kf_s$, the value closest to $0$.** The apparent frequency $|\hat f|$ lies in $[0,\frac{f_s}{2}]$; as $f_0$ grows it rises to $\frac{f_s}{2}$, falls back to $0$ at $f_s$, and so on (the frequency axis folded at multiples of $\frac{f_s}{2}$, the "folding frequency"). Keep the sign of $\hat f$ for a sine or a phase. In rad/s: reduce $\Omega_0T$ into $(-\pi,\pi]$ and divide by $T$.

> [!example] The lecture's tone (checked)
> $\sin(100\pi t)$, 50 Hz, Nyquist rate 100 Hz. At $160$ and $120$ Hz it comes back unchanged. At $80$ Hz, $\omega_0=\frac{5\pi}{4}\equiv-\frac{3\pi}{4}$, so $\hat\Omega=-60\pi$ and the D/A returns $\sin(-60\pi t)=-\sin(60\pi t)$, 30 Hz with the sign flipped. At $40$ Hz, $\omega_0=\frac{5\pi}{2}\equiv\frac{\pi}{2}$, and it returns $\sin(20\pi t)$, 10 Hz.

**At exactly the Nyquist rate** the band edge lands on $\omega=\pm\pi$. A spectrum that is zero there loses nothing (the triangle of HW7 #4(b)), but a sinusoid at exactly $B$ hertz is all edge: $\sin(\Omega_0t)$ at $f_s=\Omega_0/\pi$ samples to $\sin(\pi n)=0$, and $\cos(\Omega_0t+\phi)$ to $\cos\phi\,(-1)^n$. Hence the strict inequality $f_s\gt2B$.

**Avoiding it.** Sample faster than the Nyquist rate. *Aside, not in Lecture 19 or the past keys:* in practice a signal that is not exactly bandlimited first goes through an analog **anti-aliasing low-pass filter** that removes everything above $\frac{f_s}{2}$ (Singer & Munson, "Prevention of aliasing at A/D"). The exams instead test a different tolerance: aliasing is acceptable where a digital filter will delete it anyway ([[problems/digital-filtering-of-analog-signals|digital filtering of analog signals]]).

> [!trap]
> - **Aliasing is the overlap, not the copies.** The copies exist at every sampling rate; they hurt only when they overlap. Below the Nyquist rate the overlap can even look harmless: copies that add to a constant ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b)) or cancel to zero ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(c)).
> - **Signs.** $\sin(-\theta)=-\sin\theta$: for a sine, or a cosine with a phase, only $\Omega_0T\equiv+\omega_0$ reproduces the samples ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #8(a), [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6(c)).
> - **Hz versus rad/s.** $\hat\Omega=\hat\omega/T$ is in rad/s; $-60\pi$ rad/s is $-30$ Hz.
> - **Consistent is not unaliased.** "Which $T$ give these samples" accepts aliased $T$ ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6(a)); "which $T$ give this D/A output" usually does not ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6(b)).
> - **Not every signal can avoid it.** Without a band limit there is no Nyquist rate, and every sampling rate aliases ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(d), False).

**Where it appears.**
- Lectures: [[4-sampling-and-reconstruction/19-aliasing|L19]] (the definition, sinusoids, the $\sin(100\pi t)$ example in frequency and time, folding, slide 19, a whole spectrum through the D/A) · [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|L17]] (§6 the overlap, §7 Example 2(c), §8 a sinusoid's frequency modulo $2\pi$) · [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion|L18]] (what the D/A keeps).
- Problem families: [[problems/sampling-and-the-nyquist-rate|Sampling and the Nyquist rate]] (recipe C: which $T$ or $\Omega_0$) · [[problems/digital-filtering-of-analog-signals|digital filtering of analog signals]] (aliasing outside the passband).
- Past exams: sampled sinusoids in [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #3, [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #6, [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #8, [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #9; whole spectra in [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #8(b), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #7(c), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #5(b), [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #4; True/False in the [[exams/midterm-2/true-false-bank|T/F bank]] §4.
- Try it live: [[demos/sampling-explorer|sampling explorer]] (slide $T$ past the Nyquist period and watch the copies overlap) · [[supplements/demo-notebooks|course notebooks]] (`demo_sampling`).

Related: [[concepts/nyquist-criterion|Nyquist criterion]] · [[concepts/sampling|sampling]] · [[concepts/ideal-reconstruction|ideal reconstruction]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft|DTFT]]

### Sources for this page
Lecture 19 notes §1–§2.1 (eqs. 1–17, Figures 1–3) and slides 3–19, with the annotated deck (slide 7 inked); Lecture 17 §6–8; HW7 #4 with its official solution; Singer & Munson, ECE 310 course notes (2019) §3.2 and the scanned ECE 410 notes (prevention of aliasing at the A/D); the past-exam keys cited above. Every number is checked in `verify/L19_lecture.py`.
