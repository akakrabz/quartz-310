---
title: "Lecture 14 — DTFT properties"
description: "The DTFT as the z-transform on the unit circle; impulse DTFTs of periodic signals and Table 1 of pairs; Hermitian symmetry, modulation, Parseval, convolution, windowing."
tags: [lecture, midterm-2, dtft]
lecture: 14
---

*Lecture 14 · Fri Sep 25, 2026 · notes + slides "Discrete-time Fourier transform properties" · prev: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] · next: [[3-fourier-analysis/15-frequency-response|Lecture 15]]*

> [!abstract] In one breath
> - $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ when the ROC contains $|z|=1$. Periodic signals get Dirac impulses: $e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$.
> - Real $x[n]$ $\iff$ Hermitian $X_d$: even magnitude, odd phase. Every DTFT is $2\pi$-periodic.
> - Properties: the z-transform's with $z=e^{j\omega}$, plus modulation, windowing and Parseval. Erratum: $n\,x[n]\leftrightarrow+j\,\frac{dX_d}{d\omega}$, not $-j$.

## What was covered

1. **§1 DTFT and the z-transform** (eqs. 1–6, slides 3–6) → [[concepts/dtft|DTFT]] §3, [[concepts/bibo-stability|BIBO stability]]
2. **§1.1 Linear algebra intuition** (eqs. 7–12, optional) → [[concepts/dtft|DTFT]] §3, [[concepts/template-matching|Template matching]] §6
3. **§2 DTFT of periodic signals** (eqs. 13–25, Table 1, slides 7–9) → [[concepts/dtft-pairs|DTFT pairs]]
4. **§3 Properties of the DTFT** (eqs. 26–51, Table 2, slides 10–15) → [[concepts/dtft-properties|DTFT properties]]

## Exercises from this lecture

- Slide 4, DTFTs of $\{1,\underset{\uparrow}{0},0,-1\}$, $a^nu[n]$ and $\{\underset{\uparrow}{1},2,3\}$ → [[concepts/dtft|DTFT]] §4
- Slide 6, do the DTFTs of $X_1(z)$ and $X_2(z)$ exist → [[concepts/dtft|DTFT]] §4
- Eqs. 16–22, deriving $e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$, cosine and sine → [[concepts/dtft-pairs|DTFT pairs]] §1
- Slide 12, is $x[n]$ real when $X_d(\omega)=\omega^2e^{j\cos\omega}$ · slide 13, five symmetry statements → [[concepts/dtft-properties|DTFT properties]] §2

**Practice:** [[homework/hw5|HW5]] #1–#2 · [[homework/hw6|HW6]] #2–#5 · [[problems/dtft-and-inverse-dtft|DTFT family]] · [[exams/quiz-2|Quiz 2]]

## Related

[[3-fourier-analysis/index|Unit 3]] · prev: [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|Lecture 13]] · next: [[3-fourier-analysis/15-frequency-response|Lecture 15]] · [[concepts/index|Concepts]] · [[0-toolkit/05-errata|errata]]

### Sources for this page

Snyder, Lecture 14 notes (§§1–3, Tables 1–2) and slides (annotated 4–5); transform tables (the $+j$ sign).
