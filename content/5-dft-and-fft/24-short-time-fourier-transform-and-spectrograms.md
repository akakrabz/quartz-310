---
title: "Lecture 24 — Short-time Fourier transform and spectrograms"
description: "Bonus lecture: spectra that change with time; the STFT X[t,k] with window length L and stride S; time against frequency resolution; spectrograms of a scale and of chords. Not tested."
tags: [lecture, dft, spectral-analysis]
lecture: 24
---

*Lecture 24 · slides dated Mon Oct 26, shown Wed Oct 28, 2026 · "Short-time Fourier transform and spectrograms" (slides: "Spectral analysis part 3") · prev: [[5-dft-and-fft/23-spectral-analysis-and-window-functions|Lecture 23]] · next: [[5-dft-and-fft/25-fast-fourier-transform|Lecture 25]] · bonus content, not on homework or exams*

> [!abstract] In one breath
> - The spectral analysis model assumes all components start and stop together. Notes in music do not, and one DFT cannot tell their order.
> - STFT: a length-$L$ windowed DFT every $S$ samples gives $X[t,k]$, a spectrum for each moment.
> - Longer windows: finer frequency, coarser time. A spectrogram shows $\lvert X[t,k]\rvert$ as an image.

> [!lecture] In lecture — L24, Oct 28
> Shown after the Lecture 23 demos as "optional content … to get a little bit of a better, more rich understanding of what doing this kind of audio analysis or spectral analysis would look like in practice." Not tested, "because it's a very computational thing, but also there's no reason why we can't teach you."

## What was covered

1. **Recap: the spectral analysis problem and what it leaves out** (eq. 1, slides 3–4) → [[concepts/short-time-fourier-transform|STFT]] §1
2. **§1 Short-time Fourier transform**, with stride (eqs. 2–3, slides 5–6) → [[concepts/short-time-fourier-transform|STFT]] §2
3. **§1.1 Tradeoffs: frequency and temporal resolution** (slide 10) → [[concepts/short-time-fourier-transform|STFT]] §3
4. **§2 Spectrograms** of a C major scale, a C major chord and a chord loop (Figures 1–2, slides 7–9) → [[concepts/short-time-fourier-transform|STFT]] §4

## Examples from this lecture

- Piano scale at 10 kHz, ten windows per 0.5 s note: $L=500$ → [[concepts/short-time-fourier-transform|STFT]] §3
- Guitar scale at 48 kHz, $L=4096$, $S=\frac L3$ → [[concepts/short-time-fourier-transform|STFT]] §4

**Practice:** none; this lecture is not on homework or exams.

## Related
[[5-dft-and-fft/index|Unit 5]] · [[concepts/spectral-analysis|spectral analysis]] · [[concepts/window-functions|window functions]] · [[concepts/index|Concepts]]

### Sources for this page
Snyder, Lecture 24 notes (§1–2, eqs. 1–3, Figures 1–2) and slides 1–10, dated Oct 26, 2026; lecture recording Oct 28 (condensed).
