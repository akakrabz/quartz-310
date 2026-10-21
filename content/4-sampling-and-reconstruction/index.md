---
title: "Unit 4 · Sampling and reconstruction"
description: "Lectures 17–19: ideal A/D conversion (spectral copies, ω = ΩT, Nyquist criterion), ideal D/A conversion (sinc interpolation, A/D → H_d → D/A) and aliasing."
tags: [sampling, nyquist, ctft, dtft]
---

*Unit 4 · Lectures 17–19 · Midterm 2 · prev: [[3-fourier-analysis/index|Unit 3]] · next: [[5-dft-and-fft/index|Unit 5]]*

- Sampling $x[n]=x_a(nT)$ copies the analog spectrum every $2\pi/T$; $\omega=\Omega T$ gives the DTFT. Copies stay apart iff $f_s\gt2B$ (L17).
- Ideal D/A: a sinc per sample = low-pass of height $T$; digital filter between converters acts like $H_d(\Omega T)$ if no aliasing reaches its passband (L18).
- Below Nyquist the copies overlap; a sinusoid returns as its alias (L19).

| # | page | one line |
|---|---|---|
| 17 | [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion\|Ideal analog-to-digital conversion]] | impulse-train model; $X_s(\Omega)$ copies; $\omega=\Omega T$; box and triangle examples; Nyquist rate, guard band, aliasing |
| 18 | [[4-sampling-and-reconstruction/18-ideal-digital-to-analog-conversion\|Ideal digital-to-analog conversion]] | $x_a(t)=\sum_nx[n]g(t-nT)$; sinc interpolation; $Y_a(\Omega)=T\,Y_d(\Omega T)$; A/D → $H_d$ → D/A (HW7 #4) |
| 19 | [[4-sampling-and-reconstruction/19-aliasing\|The aliasing effect]] | sampling at exactly $2B$; principal alias; $\sin(100\pi t)$ at $160,120,80,40$ Hz; folding $f_0-kf_s$ |

> [!key] The unit on one card
> - **Ideal sampling** ([[concepts/sampling|sampling]]): $x[n]=x_a(nT)$, $f_s=\frac1T$. Model $x_s(t)=\sum_nx_a(nT)\,\delta(t-nT)$.
> - **Sampled spectrum:** $X_s(\Omega)=\dfrac1T\displaystyle\sum_{n=-\infty}^{\infty}X_a\!\left(\Omega-\frac{2\pi}{T}n\right)$ — copies every $\frac{2\pi}{T}$ rad/s, scaled $\frac1T$, added where they overlap.
> - **Frequency map:** $\omega=\Omega T$; a tone at $f$ Hz lands at $\omega=2\pi f/f_s$; $f_s/2$ lands at $\pi$.
> - **DTFT of the samples:** $X_d(\omega)=\dfrac1T\displaystyle\sum_{n=-\infty}^{\infty}X_a\!\left(\frac{\omega-2\pi n}{T}\right)$; without overlap $X_d(\omega)=\frac1TX_a(\frac{\omega}{T})$ on $\lvert\omega\rvert\le\pi$.
> - **Nyquist** ([[concepts/nyquist-criterion|Nyquist criterion]]): $X_a(\Omega)=0$ for $\lvert\Omega\rvert\gt2\pi B$. No overlap $\iff f_s\gt2B\iff T\lt\frac{1}{2B}$. At $2B$ copies touch; below, aliasing.
> - **Sampled sinusoid:** $\cos(\Omega_0t)\to\cos(\omega_0n)$, $\omega_0=\Omega_0T$; any $\Omega_0'$ with $\Omega_0'T\equiv\pm\Omega_0T\pmod{2\pi}$ gives the same samples (sine: sign matters).
> - **Ideal D/A** ([[concepts/ideal-reconstruction|ideal reconstruction]]): $x_a(t)=\sum_nx[n]\,\mathrm{sinc}\!\left(\frac{\pi(t-nT)}{T}\right)$, $\mathrm{sinc}(t)=\frac{\sin t}{t}$; $Y_a(\Omega)=T\,Y_d(\Omega T)$ on $\lvert\Omega\rvert\le\frac{\pi}{T}$, $0$ outside. Exact if $f_s\gt2B$.
> - **A/D → $H_d$ → D/A:** digital cutoff $\omega_c$ ↔ analog $\omega_c/T$; no aliasing in the passband ⇒ $H_a(\Omega)=H_d(\Omega T)$ on $\lvert\Omega\rvert\lt\frac{\pi}{T}$.
> - **Aliasing** ([[concepts/aliasing|aliasing]]): $\Omega_0T$ reduced mod $2\pi$ into $(-\pi,\pi]$; D/A returns $\hat\Omega=\hat\omega/T$ (Hz: the $f_0-kf_s$ closest to $0$). $\sin(100\pi t)$ at $80$ Hz returns $-\sin(60\pi t)$. $\sin(\Omega_0t)$ at $f_s=\Omega_0/\pi$ samples to zeros.

> [!exam] Exam
> Sampling on 7/7 past Midterm 2 exams, alone or inside A/D → $H_d$ → D/A. Families: [[problems/sampling-and-the-nyquist-rate|sampling and the Nyquist rate]] · [[problems/digital-filtering-of-analog-signals|digital filtering of analog signals]]. T/F: [[exams/midterm-2/true-false-bank|T/F bank]] §4. Maps: [[exams/midterm-2/index|Midterm 2]] · [[exams/midterm-2/past-exams/index|past exams]].

**Demos:** [[demos/sampling-explorer|sampling explorer]] · [[demos/practice-drills|drills]] · [[supplements/demo-notebooks|notebooks]] (`demo_sampling`)

**Concepts:** [[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/discrete-time-signal|discrete-time signal]]

### Sources for this page
Snyder, ECE 310 Lectures 17–19 notes and slides with inked decks (Fall 2026); past Midterm 2 exams with keys.
