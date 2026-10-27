---
title: "Lecture 15 — Frequency response"
description: "H_d(ω) as the DTFT of h[n]; e^{jω₀n} → H_d(ω₀)e^{jω₀n} for any LTI system; the cosine rule for real h; aperiodic inputs via Y_d = X_dH_d."
tags: [lecture, midterm-2, frequency-response, dtft]
lecture: 15
---

*Lecture 15 · Fri Oct 2, 2026 · notes + slides "Frequency response" · prev: [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · next: [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]]*

> [!abstract] In one breath
> - Frequency response $H_d(\omega)$ = DTFT of $h[n]$ = $H(z)$ on the unit circle for a stable system.
> - Any LTI system: $Ae^{j\omega_0 n}\to H_d(\omega_0)\,Ae^{j\omega_0 n}$.
> - Real $h$: $A\cos(\omega_0 n+\theta)\to A|H_d(\omega_0)|\cos(\omega_0 n+\theta+\angle H_d(\omega_0))$. Any input: $Y_d=X_dH_d$.

## What was covered

1. **§1 Frequency response** (eqs. 1–2, slide 4) → [[concepts/frequency-response|Frequency response]] §1, [[concepts/transfer-function|Transfer function]]
2. **§1.1 LTI response to periodic exponential signals** (eqs. 3–8, slides 5–6) → [[concepts/frequency-response|Frequency response]] §2, [[concepts/eigenfunctions-of-lti-systems|Eigenfunctions]]
3. **§1.2 LTI response to sinusoids** (eqs. 9–15, slides 7–11) → [[concepts/frequency-response|Frequency response]] §3
4. **§1.3 LTI response to aperiodic inputs** (eqs. 16–22, Figure 1) → [[concepts/frequency-response|Frequency response]] §4, [[concepts/dtft-properties|DTFT properties]]

## Exercises from this lecture

- Slide 6, $|H_d|=|\omega|$, $\angle H_d=-\frac{\omega}{2}$: write $H_d$, respond to two exponentials → [[concepts/frequency-response|Frequency response]] §2
- Slide 8, why the cosine rule needs real $h$ · slide 10 (concept check), $|H_d|=\cos^2\omega$, $\angle H_d=\sin\omega$, three input terms · slide 11, read $H_d$ off one input–output pair → §3

**Practice:** [[homework/hw6|HW6]] #5–#7 · [[problems/lti-response-to-sinusoids|LTI response to sinusoids]] · [[demos/frequency-response-explorer|explorer]] · [[exams/quiz-2|Quiz 2]]

## Related

[[3-fourier-analysis/index|Unit 3]] · prev: [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · next: [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] · [[concepts/index|Concepts]]

### Sources for this page

Snyder, Lecture 15 notes (§1–1.3, Figure 1) and slides (unannotated; answers worked on the concept page).
