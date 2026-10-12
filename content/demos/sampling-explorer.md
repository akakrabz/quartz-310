---
title: "Demo — Sampling explorer (ideal A/D conversion)"
description: "Pick an analog spectrum X_a(Ω) and a bandlimit B, slide the sampling rate from below to far above the Nyquist rate, and watch the sampled spectrum X_s(Ω) = (1/T) Σ X_a(Ω − 2πn/T), the DTFT X_d(ω) = X_s(ω/T) with its band edge 2πBT, the guard band or the aliasing overlap, and the samples x[n] = x_a(nT) themselves — with presets for the Lecture 17 examples and past Midterm 2 problems."
tags: [demo, sampling, nyquist, ctft, dtft]
---

*Demo · pairs with [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · concepts: [[concepts/sampling]], [[concepts/nyquist-criterion]], [[concepts/dtft]] · problem family: [[problems/sampling-and-the-nyquist-rate]]*

<div class="ece-demo">
<iframe src="/static/demos/sampling/" title="Sampling explorer — interactive demo" loading="lazy" style="height:1560px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/sampling/) if the frame is cramped on your screen.

**What it shows.** Choose a bandlimited analog spectrum $X_a(\Omega)$ (a brick wall, a triangle, a trapezoid, a raised-cosine bump, or two pure tones) and its bandlimit $B$ in hertz, then set the sampling rate $f_s = 1/T$ with the slider (from $0.4\times$ to $6\times$ the Nyquist rate $2B$), by typing $f_s$ or $T$, or with the jump buttons $B$, $1.5B$, $2B$, $3B$, $4B$. Four panels update together:

1. $X_a(\Omega)$ with its band edge $\pm 2\pi B$;
2. the spectrum of the impulse-train-sampled signal, $X_s(\Omega) = \frac1T\sum_n X_a\!\left(\Omega - \frac{2\pi}{T}n\right)$: every shifted copy in orange and their **sum** in teal, with the guard band shaded (teal) or the overlap shaded (red);
3. the DTFT of the samples, $X_d(\omega) = X_s(\omega/T)$ on $-3\pi \le \omega \le 3\pi$, with the band edge at $\omega = 2\pi BT$ and the next copy's edge at $2\pi - 2\pi BT$;
4. $x_a(t)$ with its samples $x[n] = x_a(nT)$, so you can see how many samples a lobe gets.

A verdict line says whether $f_s$ is above, at or below the Nyquist rate and shows the inequality that decides it, $2\pi B \lt \frac{2\pi}{T} - 2\pi B$, i.e. $T \lt \frac{1}{2B}$; a formula card substitutes the current numbers into the Lecture 17 equations.

> [!exam] How this is tested
> Every past Midterm 2 has a sampling problem that starts with "sketch $X_d(\omega)$" for a given $X_a(\Omega)$ and $T$, or asks for the Nyquist rate or the largest $T$ that avoids aliasing: [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2 #5]] and [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2 #9]] are presets, [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2 #5–6]], [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2 #7–8]], [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2 #3]] and [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2 #8–9]] are the same question with other numbers. On the exam you draw the sketch yourself, and the points are in the labels: the height $1/T$, the band edge $2\pi BT$, the position of the next copy, and the sum where copies overlap. Use the demo to check a sketch after you have drawn it. The recipe is in [[problems/sampling-and-the-nyquist-rate]].

## What to try

1. **Lecture 17, Example 1 (the inked slide 6).** Preset *Example 1(a)*: the brick wall $X_a(\Omega) = \operatorname{rect}(\Omega/20\pi)$ sampled at $T = \frac1{20}$ s. The copies in panel (b) sit every $\frac{2\pi}{T} = 40\pi$ rad/s, each of height $\frac1T = 20$ and width $20\pi$, with a gap of $20\pi$ between neighbours. Switch to *Example 1(b)*, $T = \frac1{10}$ s: the spacing halves to $20\pi$, the height to $10$, and the boxes **touch** — the sum in panel (b) is the flat line $10$, and $X_d(\omega)$ in panel (c) is flat too. Nothing overlaps, so this is sampling exactly at the Nyquist rate ($f_s = 10$ Hz $= 2 \cdot 5$ Hz), and yet the copies have lost their shape as separate boxes. Panel (d) explains it in time: the samples of the sinc pulse at $t = n/10$ are $x_a(0) = 10$ and then zeros.
2. **Lecture 17, Example 2: the same triangle at 150, 100 and 75 Hz.** The three presets sample $X_a(\Omega) = 1 - \frac{|\Omega|}{100\pi}$ ($B = 50$ Hz) above, at and below the Nyquist rate of $100$ Hz. At $150$ Hz the band edge lands at $\omega = 2\pi BT = \frac{2\pi}{3}$ and the next copy starts at $2\pi - \frac{2\pi}{3} = \frac{4\pi}{3}$: a guard band of width $\frac{2\pi}{3}$, shaded teal. At $100$ Hz the edge is exactly $\pi$ and the copies touch. At $75$ Hz the edge is $\frac{4\pi}{3} \gt \pi$, the copies overlap on $\frac{2\pi}{3} \le |\omega| \le \frac{4\pi}{3}$ (shaded red), and the teal sum is **flat at $37.5$** there: the two overlapping ramps of height $75$ add to a constant, $75\left(2 - \frac{3}{2}\right) = 37.5$ at $\omega = \pi$ and the same everywhere on the overlap. The orange dashed copies show the pieces; the teal line is what $X_d(\omega)$ actually is. That merged shape is aliasing: you can no longer read $X_a$ off it.
3. **Slide the rate and watch the three numbers move.** Start from *Example 2(a)* and drag $f_s$ down. The copies in panel (b) slide inward (spacing $2\pi/T$ shrinks) and get shorter (height $1/T$); in panel (c) the copies stay $2\pi$ apart but the band edge $2\pi BT$ moves out toward $\pi$. The guard band closes exactly when $2\pi BT = \pi$, i.e. $f_s = 2B$ — the Nyquist tick on the slider snaps there. The preset menu follows the settings, so sliding 2(a) down to $1/75$ s shows the 2(c) note.
4. **The past exams.** *FA2024 #5*: a triangle out to $1000\pi$ rad/s ($B = 500$ Hz) at $T = T_N = 1$ ms gives a triangle of height $1000$ reaching $0$ at $\pm\pi$ — the copies touch; at $T = 2T_N$ they overlap completely and $X_d(\omega)$ is **flat at $500$**, which is the key's sketch. *FA2019 #9(a)* asks only for the Nyquist interval of a signal bandlimited to $1000\pi$ rad/s: $T_N = \frac{1}{2 \cdot 500} = 1$ ms; the shape in the preset is a stand-in, since the exam gives none.
5. **Two tones: which frequencies a sampler cannot tell apart.** Preset *Two tones 20 Hz + 50 Hz, $f_s = 150$ Hz*: impulses at $\omega_1 = \frac{2\pi \cdot 20}{150} = \frac{4\pi}{15}$ and $\omega_2 = \frac{2\pi \cdot 50}{150} = \frac{2\pi}{3}$, both inside $|\omega| \lt \pi$, and their copies $2\pi$ away. Now *$f_s = 80$ Hz*: the $50$ Hz tone's impulse lands at $\omega_2 = \frac{5\pi}{4} \gt \pi$, and its copy from $-2\pi$ appears at $-\frac{3\pi}{4}$, which is where a $30$ Hz tone would be — the samples of $\cos(2\pi \cdot 50\,t)$ at $80$ Hz are identical to those of $\cos(2\pi \cdot 30\,t)$. That is the sinusoid version of aliasing in Lecture 17 §8, and the trap behind [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2 #8]] and [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2 #6]].
6. **Shapes to explore.** The brick wall at $3\times$ Nyquist shows the widest guard band and six samples per main lobe in panel (d); drag $f_s$ to $2B$ and only two remain. The trapezoid and the raised-cosine bump show that the Nyquist criterion depends only on where $X_a$ **ends** ($2\pi B$), not on its shape: at $f_s = 2B$ every shape's copies touch exactly at $\omega = \pm\pi$.

> [!tip] Reading the sketch
> Three labels carry a sampling sketch: the **height** of each copy, $\frac1T \cdot \max X_a$; the **band edge** in $\omega$, $2\pi BT$ (half the sampling rate maps to $\pi$); and the **position of the next copy's edge**, $2\pi - 2\pi BT$. If the second is bigger than $\pi$ the copies overlap and you must draw their sum, not the pieces. The demo prints all three for the current settings.

## What the demo is (and isn't)

It implements the ideal A/D conversion of Lecture 17 and nothing after it: there is no reconstruction, no filter between A/D and D/A, and no quantisation. The spectra are the formulas evaluated on a grid: $X_s(\Omega) = \frac1T\sum_{n=-N}^{N} X_a\!\left(\Omega - \frac{2\pi}{T}n\right)$ with enough copies to cover the plotted window, and $X_d(\omega) = X_s(\omega/T)$. The two-tone spectrum is drawn with impulses (arrows) whose areas add when two land on the same frequency. The time signal in panel (d) is the exact inverse CTFT of each shape ($2B\,\operatorname{sinc}(2Bt)$ for the brick wall, $B\,\operatorname{sinc}^2(Bt)$ for the triangle, and so on), so the samples are $x_a(nT)$ computed from a closed form, not from a numerical transform. Values are shown as fractions or multiples of $\pi$ when such a form matches to $10^{-9}$; that is a display convenience, not exact arithmetic.

Every preset and the plotted curves were checked against numpy from an independent evaluation of the copies formula, the Lecture 17 hand values (Example 1: copies every $40\pi$ of height $20$, every $20\pi$ of height $10$ and flat; Example 2: band edges $\frac{2\pi}{3}$, $\pi$, $\frac{4\pi}{3}$ and the flat segment at $37.5$) and the FA2024 #5 key (height $1000$, flat $500$): `verify/L17_INT_demo_check.py`, `verify/REV_L17_RB_demo.py` and a pixel-level browser check `verify/REV_L17_RB_browser.py`.

## Related

[[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · [[4-sampling-and-reconstruction/index|Unit 4 · Sampling and reconstruction]] · [[concepts/sampling]] · [[concepts/nyquist-criterion]] · [[concepts/dtft]] · [[concepts/fourier-series]] · [[problems/sampling-and-the-nyquist-rate]] · [[demos/frequency-response-explorer|Frequency-response explorer]] · [[demos/python-demos|Python demos]] · [[demos/index|all demos]]

### Sources for this page

Lecture 17 notes (§1 ideal sampling and the impulse train, eqs. 4–11; §1.1 the DTFT after sampling, eqs. 12–16; §2 bandlimited signals and the Nyquist criterion, eqs. 17–21; Figures 1–3) and slides (slides 3–12: the key question, the derivation inked on slide 5, Example 1 inked on slide 6, the Nyquist sketch on slide 8, Example 2 on slides 10–12, which have no ink and were solved here). Past Midterm 2 keys: FA2024 #5, FA2019 #9, SP2025 #5–6, SP2023 #7–8, FA2023 #3, SP2021 #8–9. Numbers verified with numpy (`verify/L17_INT_demo_check.py`, `verify/REV_L17_RB_demo.py`, `verify/REV_L17_RB_browser.py`).
