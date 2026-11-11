---
title: "Lecture 27 — Practical filter design"
description: "Ideal low-pass, high-pass, band-pass and band-stop filters and why they cannot be built; passband ripple, stopband attenuation, transition band; choosing a filter for a scenario; direct form I and II flow graphs."
tags: [lecture, filter-design]
lecture: 27
---

*Lecture 27 · Mon Nov 9, 2026 (§1–3.1; §3.2 and Example 2 announced for Wed Nov 11) · "Practical filter design" · prev: [[5-dft-and-fft/26-fast-convolution-via-the-dft|Lecture 26]] · next: Lecture 28 · first lecture of the filter design unit*

> [!abstract] In one breath
> - Four ideal filters, all built from the low-pass, whose impulse response is an endless two-sided sinc: not implementable.
> - A practical filter has passband ripple, finite stopband attenuation and a transition band; narrower transition costs attenuation.
> - Any filter is an LCCDE; direct form I and II are two ways to wire it, II with fewer delays.

> [!lecture] In lecture — L27, Nov 9
> "This lecture is not meant to be very rigorous … We're just trying to, I would say, set the table for our upcoming lectures on filter design." Announced the same day: the final exam is expected to be one third Midterm 1 content, one third Midterm 2 content and one third post-Midterm 2 content (HW10–HW13).

## What was covered

1. **§1–1.1 Ideal digital filters and the four common structures** (eqs. 1–4, Figure 1, slides 3–4) → [[concepts/ideal-filters|ideal filters]] §1
2. **§1.2 Issues with ideal filters:** the sinc impulse response and its three problems; the other filters from a low-pass (eq. 5, slide 5) → [[concepts/ideal-filters|ideal filters]] §2–4
3. **§2 Digital filter design considerations:** passband, ripple, stopband, attenuation, transition band (Figure 2, slides 6–7) → [[concepts/filter-specifications|filter specifications]] §1–2
4. **§3–3.1 Block diagrams and direct form I** (eqs. 6–8, Figure 3, slides 9–10) → [[concepts/direct-form-structures|direct form I and II]] §1–2
5. **§3.2 Direct form II** (eqs. 9–13, Figure 4, slide 11; from the notes) → [[concepts/direct-form-structures|direct form I and II]] §3

## Exercises from this lecture

- Example 1 (slide 8): (a) thunder, worked in class; (b) 60 Hz hum, left as an exercise → [[concepts/filter-specifications|filter specifications]] §3
- Example 2 (slides 12–13), both diagrams for one LCCDE → [[concepts/direct-form-structures|direct form I and II]] §4
- Asked in class: why not zero the DFT bins? → [[concepts/ideal-filters|ideal filters]] §4

**Practice:** [[homework/hw11|HW11]] (due Fri Nov 13)

## Related
[[6-filter-design/index|Unit 6]] · [[concepts/fir-and-iir|FIR and IIR]] · [[concepts/block-diagram|block diagram]] · [[concepts/index|Concepts]]

### Sources for this page
Snyder, Lecture 27 notes (§1–3.2, eqs. 1–13, Figures 1–4) and annotated slides 1–13, Nov 9, 2026; lecture recording Nov 9 (condensed).
