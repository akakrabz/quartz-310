---
title: "Demo — Sampling explorer (ideal A/D conversion)"
description: "Pick X_a(Ω) and bandlimit B, slide f_s across the Nyquist rate, and watch X_s(Ω), X_d(ω) with band edge 2πBT, the guard band or overlap, and the samples x[n] = x_a(nT)."
tags: [demo, sampling, nyquist, ctft, dtft]
---

*Demo · pairs with [[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · concepts: [[concepts/sampling]], [[concepts/nyquist-criterion]], [[concepts/dtft]] · problem family: [[problems/sampling-and-the-nyquist-rate]]*

<div class="ece-demo">
<iframe src="/static/demos/sampling/" title="Sampling explorer — interactive demo" loading="lazy" style="height:1560px"></iframe>
</div>

[Open the demo in its own tab](/static/demos/sampling/).

**Panels.** (a) $X_a(\Omega)$, edge $\pm 2\pi B$. (b) $X_s(\Omega) = \frac1T\sum_n X_a\!\left(\Omega - \frac{2\pi}{T}n\right)$: copies in orange, sum in teal, guard band or overlap shaded. (c) $X_d(\omega) = X_s(\omega/T)$, edge $2\pi BT$. (d) $x_a(t)$ and $x[n] = x_a(nT)$. Rate: slider ($0.4\times$ to $6\times$ Nyquist), typed $f_s$ or $T$, or jump buttons.

## What to try

1. **Lecture 17, Example 1** ([[concepts/sampling|Sampling]] §2)**:** $\operatorname{rect}(\Omega/20\pi)$ at $T = \frac1{20}$ s: copies every $40\pi$, height $20$. At $T = \frac1{10}$ s: copies touch, sum flat at $10$.
2. **Example 2, triangle $B = 50$ Hz at 150, 100, 75 Hz:** edge at $\frac{2\pi}{3}$ (guard band), $\pi$ (touch), $\frac{4\pi}{3}$ (overlap, sum flat at $37.5$ on the overlap).
3. **Slide $f_s$ down:** copies in (b) move in and shrink; in (c) the edge moves out; the guard band closes at $f_s = 2B$.
4. **FA2024 #5:** $T = 1$ ms gives a triangle of height $1000$ touching at $\pm\pi$; $T = 2$ ms gives $X_d$ flat at $500$.
5. **Two tones 20 + 50 Hz:** at $150$ Hz, impulses at $\frac{4\pi}{15}$ and $\frac{2\pi}{3}$. At $80$ Hz, $50$ Hz lands at $\frac{5\pi}{4}$, same samples as $30$ Hz: aliasing (Lecture 19).
6. **Shapes:** at $f_s = 2B$ every shape's copies touch at $\pm\pi$; only the band edge matters.

> [!tip] Three labels carry a sketch
> Height $\frac1T \cdot \max X_a$; band edge $2\pi BT$; next copy's edge $2\pi - 2\pi BT$. If the edge passes $\pi$, draw the sum.

Ideal A/D only: no reconstruction, filtering or quantisation.

> [!exam]
> Every past Midterm 2 asks to sketch $X_d(\omega)$ after sampling, or for the Nyquist rate or largest $T$.
> - [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2 #5]] · [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2 #9]] · [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2 #5–6]] · [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2 #7–8]] · [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2 #3]] · [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2 #8–9]]

## Related
[[4-sampling-and-reconstruction/17-ideal-analog-to-digital-conversion|Lecture 17]] · [[concepts/sampling]] · [[concepts/nyquist-criterion]] · [[concepts/aliasing]] · [[problems/sampling-and-the-nyquist-rate]] · [[demos/index|all demos]]

### Sources for this page
Lecture 17 notes (eqs. 4–21, Figures 1–3) and slides 3–12; Midterm 2 keys FA2024 #5, FA2019 #9, SP2025 #5–6, SP2023 #7–8, FA2023 #3, SP2021 #8–9.
