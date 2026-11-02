---
title: "Lobe separation and frequency resolution"
description: "Two equal tones are resolved when their periodic-sinc main lobes (width 4π/N) separate: full-lobe N > 4π/Δω, half-lobe N > 2π/Δω; zero padding does not help. Guitar E2/F2 at 8 kHz: 3200 samples, 0.4 s."
tags: [concept, dft, spectral-analysis, midterm-2]
aliases: ["full-lobe separation", "half-lobe separation", "frequency resolution", "lobe separation", "resolution criteria", "lobe separation criteria"]
---

*Lecture 23 (Mon Oct 26) §2 · Exercise 1(b) and demos Wed Oct 28 · family: [[problems/dft-spectral-analysis|DFT spectral analysis]]*

> [!abstract] In one breath
> - Equal amplitudes, close frequencies: resolved iff the two main lobes (each $\frac{4\pi}{N}$ wide) do not merge.
> - Full-lobe: $\omega_2-\omega_1\gt\frac{4\pi}{N}\iff N\gt\frac{4\pi}{\Delta\omega}$; half-lobe: $N\gt\frac{2\pi}{\Delta\omega}$.
> - Only more samples help; zero padding leaves the DTFT, hence the lobes, unchanged. In seconds: $NT\gt\frac{2}{\Delta f}$ (full), independent of $f_s$.

## 1. Two equal tones (eqs. 5–7)

$x[n]=2\cos(\omega_1n)+2\cos(\omega_2n)$, $0\le n\le N-1$ ($A_1=A_2=2$, so each lobe has height $N$):

$$
X_d(\omega)=C(\omega-\omega_1)+C(\omega+\omega_1)+C(\omega-\omega_2)+C(\omega+\omega_2).
$$

- The signal is real, so Hermitian symmetry puts the mirror lobes on $[-\pi,0]$: on $0\le\omega\le\pi$ only the two [[concepts/periodic-sinc|periodic sincs]] at $\omega_1$, $\omega_2$ matter, and they distort each other through the cross term $2C(\omega-\omega_1)C(\omega-\omega_2)$. That term is a second-order effect once $N$ is not very small (heuristic: $N\gt32$): the side-lobe nulls crowd together and the side lobes decay (for short $N$ the approximation breaks down and the spectrum gets distorted). Eq. 7:
$$
\lvert X_d(\omega)\rvert\approx\lvert C(\omega-\omega_1)\rvert+\lvert C(\omega+\omega_1)\rvert+\lvert C(\omega-\omega_2)\rvert+\lvert C(\omega+\omega_2)\rvert .
$$
- Slide 6: $\lvert C_1+C_2\rvert=\sqrt{C_1^2+C_2^2+2C_1C_2}\approx\lvert C_1\rvert+\lvert C_2\rvert$ for the positive-frequency terms.
- To tell two frequencies apart we must distinguish the two main lobes, each of width $\frac{4\pi}{N}$ (edges $\frac{2\pi}{N}$ either side of the peak).

## 2. The criteria (eqs. 8–10, slide 7)

> [!key] Lobe separation (Lecture 23, eqs. 8–10)
> Take $\omega_1\lt\omega_2$. **Full-lobe separation:** no overlap of the main lobes, right edge of lobe 1 below left edge of lobe 2:
> $$
> \omega_1+\frac{2\pi}{N}\lt\omega_2-\frac{2\pi}{N}\quad\Longleftrightarrow\quad\omega_2-\omega_1\gt\frac{4\pi}{N}\quad\Longleftrightarrow\quad N\gt\frac{4\pi}{\lvert\omega_1-\omega_2\rvert}.
> $$
> **Half-lobe separation:** up to half of each main lobe may overlap (the usual practical relaxation):
> $$
> \omega_2-\omega_1\gt\frac{2\pi}{N}\quad\Longleftrightarrow\quad N\gt\frac{2\pi}{\lvert\omega_1-\omega_2\rvert}.
> $$
> **With a Hamming [[concepts/window-functions|window]]** (main lobe $\frac{8\pi}{N}$, slide 13) every bound doubles: full $N\gt\frac{8\pi}{\lvert\omega_1-\omega_2\rvert}$, half $N\gt\frac{4\pi}{\lvert\omega_1-\omega_2\rvert}$.

> [!lecture] In lecture — L23, Oct 26
> Many components "might seem like a really difficult problem, but in practice we can just focus on separating pairs of frequencies." "If I can separate any pair of components, then I can separate all pairs of components." And not every pair — "just pairs that are close to each other": apply the criterion to your two closest frequencies, written as $\lvert\omega_2-\omega_1\rvert$ so that it does not matter which is larger. When that difference is really, really small, "we are going to require a lot of samples to be able to shrink the width of those main lobes" and guarantee they separate.

> [!lecture] In lecture — L23, Oct 28
> "All of our full-lobe, half-lobe resolution criteria get twice as expensive with the Hamming window because the width is twice as wide." All the math we did is the same, "it just gets doubled." In the demo, two equal tones spaced exactly $\frac{4\pi}{N}$ ($N=128$) had their main lobes just meeting under the rectangular window; with Hamming he could "hardly even notice the side lobes," but the two main lobes ran together into one odd shape — "if we just reduce the spacing just a tiny bit, it'll fully combine into one lobe" — so "if we can't guarantee adequate spacing, we may have that these components absorb into each other."

- Longer signal, closer frequencies resolvable. At exactly $\Delta\omega=\frac{2\pi}{N}$ each peak sits on the other lobe's first null.
- **Zero padding does not help:** it does not change the DTFT of a finite-length signal, so the lobes keep their width ([[concepts/zero-padding|zero padding]]).
- In hertz, $\omega=2\pi f/f_s$, so $\Delta\omega=2\pi\Delta f/f_s$:
$$
\begin{gathered}
N\gt\frac{4\pi}{\Delta\omega}=\frac{2f_s}{\Delta f}\ \text{(full)},\qquad N\gt\frac{f_s}{\Delta f}\ \text{(half)};\\
\text{duration }NT\gt\frac{2}{\Delta f}\ \text{(full)},\qquad NT\gt\frac{1}{\Delta f}\ \text{(half)}.
\end{gathered}
$$

> [!question] Exercise 1 / slide Example 1 — a guitar chord at 8 kHz
> A guitar in standard tuning plays a chord; all notes have similar amplitudes; recorded at $f_s=\frac1T=8$ kHz. The lowest note is E2 $\approx82$ Hz and the next, F2 $\approx87$ Hz. (a) Minimum number of samples, and recording time, to separate every pair of notes with full-lobe separation? (b) Does the time change if $f_s$ doubles or halves?

> [!success]- Answer (eqs. 11–15)
> Notes are a semitone apart, a ratio $2^{1/12}\approx1.059$, so they spread out in hertz as pitch rises: the closest, hardest pair is the lowest, E2/F2.
> $$
> \omega_1=\Omega_1T=\frac{2\pi\cdot82}{8000},\qquad\omega_2=\Omega_2T=\frac{2\pi\cdot87}{8000}\ \text{rad/sample}.
> $$
> (a) $N\gt\dfrac{4\pi}{\omega_2-\omega_1}=\dfrac{4\pi}{\frac{2\pi}{8000}(87-82)}=\dfrac{16000}{5}=3200$ samples; $NT=\frac{3200}{8000}=0.4$ s, under half a second of holding the chord. (E2 and F2 cannot sound together in standard tuning; think of telling an E major chord from an F major one.)
>
> (b) No. $N\gt\frac{4\pi}{2\pi\Delta f\,T}=\frac{2}{\Delta f\,T}=\frac{2f_s}{\Delta f}$ scales with $f_s$ ($6400$ at $16$ kHz, $1600$ at $4$ kHz), but the time $NT=\frac{2}{\Delta f}=\frac25=0.4$ s does not. Resolution is set by how long you listen, not how fast you sample.
>
> Half-lobe: $N\gt1600$, $0.2$ s.

> [!lecture] In lecture — L23, Oct 28
> Double the sampling rate, or cut it in half? "It actually does not matter. You will have to record for the same amount of time." Two effects cancel. Sampling faster makes $T$ smaller, so the separation $\omega_2-\omega_1=(\Omega_2-\Omega_1)T$ gets tighter and $N\gt\frac{4\pi}{\Delta\omega}$ demands more samples — but "because I'm sampling quicker, I don't actually have to sample for longer." Sampling slower spreads the two frequencies apart and needs fewer samples, "but because I'm sampling slower, I need to wait longer to get that fewer number of samples." "How long you have to record actually comes down to only the separation frequency."

## 3. Midterm 2 quick check

> [!question] Q1 · how many samples?
> Two equal-amplitude tones at $\omega_1=0.30\pi$ and $\omega_2=0.34\pi$. (a) Smallest $N$ for full-lobe and for half-lobe separation. (b) With $N=20$, does zero padding to 256 separate them? (c) In hertz: $f_s=2$ kHz, tones $10$ Hz apart; samples and seconds for full-lobe separation?

> [!success]- Answer
> - (a) $\Delta\omega=0.04\pi$. Full: $N\gt\frac{4\pi}{0.04\pi}=100$, so $N=101$. Half: $N\gt50$, so $N=51$.
> - (b) **No.** At $N=20$ the lobes are $\frac{4\pi}{20}=0.2\pi$ wide (half-lobe would need $\Delta\omega\gt0.1\pi$); padding samples the same merged lobe more densely: one peak.
> - (c) $N\gt\frac{2f_s}{\Delta f}=\frac{4000}{10}=400$ samples; $NT\gt\frac{2}{\Delta f}=0.2$ s (half-lobe: 200 samples, $0.1$ s).

> [!question] Q2 · True or false
> (a) Doubling $f_s$ for the same recording time resolves tones closer in hertz. (b) Half-lobe separation needs half as many samples as full-lobe. (c) A Hamming window lets the same $N$ separate closer tones.

> [!success]- Answer
> - (a) **False:** $N$ doubles but $\Delta\omega=\frac{2\pi\Delta f}{f_s}$ halves; the limit $\Delta f\gt\frac{2}{NT}$ depends on the duration only.
> - (b) **True:** $\frac{2\pi}{\Delta\omega}$ vs $\frac{4\pi}{\Delta\omega}$.
> - (c) **False:** Hamming main lobes are twice as wide ([[concepts/window-functions|window functions]]).

> [!trap]
> - $\frac{4\pi}{N}$ is the full lobe width; the edges are $\pm\frac{2\pi}{N}$ from the peak, so full separation needs $\Delta\omega\gt\frac{4\pi}{N}$, not $\frac{2\pi}{N}$.
> - $N$ counts real samples: padding to $N+L$ leaves the lobes $\frac{4\pi}{N}$ wide ([[exams/midterm-2/past-exams/fall-2023|FA2023 #6(c)]]).
> - Convert Hz to rad/sample first ($\omega=\frac{2\pi f}{f_s}$), or use $N\gt\frac{2f_s}{\Delta f}$ directly.
> - The criteria assume similar amplitudes; a weak tone needs a [[concepts/window-functions|window]] even when separated.

> [!exam] Midterm 2
> Fall 2026 MT2 (Wed Nov 4) covers this topic. Resolution appears inside spectral-analysis problems: does padding resolve closer tones, which record length separates two given frequencies. Said Oct 30: the criteria are tested "to the extent they're used on homework." [[exams/midterm-2/past-exams/fall-2023|FA2023 #6]] · [[exams/midterm-2/past-exams/fall-2021|FA2021 #7]] · [[exams/midterm-2/true-false-bank|T/F bank]] §3.

**Where it appears:** [[5-dft-and-fft/23-spectral-analysis-and-window-functions|L23]] §2 (eqs. 5–15, Exercise 1, slides 6–8) · [[problems/dft-spectral-analysis|DFT spectral analysis]].

## Related
[[concepts/spectral-analysis|spectral analysis]] · [[concepts/periodic-sinc|periodic sinc]] · [[concepts/window-functions|window functions]] · [[concepts/zero-padding|zero padding]] · [[concepts/spectral-leakage|spectral leakage]] · [[concepts/sampling|sampling]]

### Sources for this page
Snyder, Lecture 23 notes §2 (eqs. 5–15, Exercise 1) and slides 6–8 (Example 1), 13, Oct 26, 2026; lecture recording Oct 26 (condensed); lecture recording Oct 28 (condensed); lecture recording Oct 30 (condensed).
