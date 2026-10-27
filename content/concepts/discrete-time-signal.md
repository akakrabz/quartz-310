---
title: "Discrete-time signal"
description: "A sequence x[n] defined only at integers n: what a signal is, continuous vs. discrete time, analog vs. digital, sampling x[n] = x(nT), the n = 0 marker and the index maps exams use."
tags: [concept, signals, midterm-1]
aliases: ["discrete-time signal", "sequence", "digital signal", "x[n]", "signal", "sample", "continuous-time signal", "analog signal", "sampling period", "index map"]
---

*Lectures 1 (Mon Aug 24) and 2 (Wed Aug 26) · [[homework/hw1|HW1]] #1–#3 · family: [[problems/finite-length-convolution|Finite-length convolution]] (the $n = 0$ bookkeeping)*

> [!abstract] In one breath
> - Continuous-time $x(t)$, $t\in\mathbb{R}$; discrete-time $x[n]$, $n\in\mathbb{Z}$; ideal sampling $x[n] = x(nT)$.
> - Digital = discrete-time and discrete-valued; the course treats values as continuous.
> - Write finite sequences with the $n = 0$ arrow; index maps $x[an+b]$ never change values, only where they sit.

## 1. What is a signal?

> [!key] Signal (Lecture 1 §1)
> Any measurable quantity that varies over time, space, or any other variable that orders or organizes the measurements.

Notes Fig. 1:
- **Audio**: acoustic vibration vs time (the word "Goodbye").
- **Financial**: stock price vs time; not physical, still a signal.
- **Image**: three RGB values at each integer $(x, y)$; video adds time.
- **Graph signal**: values on vertices (e.g. traffic at road intersections), edges encode relations; beyond this course.

## 2. Continuous-time vs. discrete-time

- **Continuous-time** $x(t)$, $t \in \mathbb{R}$: observed at every instant; any interval holds uncountably many values.
- **Discrete-time** $x[n]$, $n \in \mathbb{Z}$: observed at regularly spaced instants; the time axis is discretized. Square brackets, integer index.

> [!key] Ideal sampling (Lecture 1, eq. 1)
> $$
> x[n] = x(nT), \qquad n \in \mathbb{Z},
> $$
> sampling period $T$, sampling rate $f_s = 1/T$. Music at $f_s = 44.1$ kHz: 44,100 samples per second, $T = 1/44100 \approx 2.2675\times10^{-5}$ s.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 230" width="640" height="230" role="img" aria-label="A continuous-time cosine and its samples x[n] = x(nT) = cos(pi n/8)" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><polyline points="14.5,81.4 24.8,72.5 37.8,63.0 50.7,55.6 55.9,53.3 63.7,50.6 68.9,49.3 76.6,48.2 87.0,48.2 97.4,49.9 107.7,53.3 115.5,56.9 125.9,63.0 138.8,72.5 146.6,79.1 154.4,86.2 167.3,99.0 198.4,131.7 216.5,149.8 224.3,156.9 237.3,167.5 245.0,173.0 250.2,176.2 260.6,181.6 265.8,183.7 273.5,186.1 283.9,187.8 289.1,188.0 296.9,187.5 302.0,186.7 309.8,184.6 317.6,181.6 322.8,179.1 328.0,176.2 338.3,169.4 346.1,163.5 361.6,149.8 379.8,131.7 403.1,107.0 418.6,91.2 429.0,81.4 439.4,72.5 452.3,63.0 462.7,56.9 473.0,52.3 483.4,49.3 491.2,48.2 496.4,48.0 504.1,48.5 511.9,49.9 519.7,52.3 524.9,54.4 532.6,58.3 540.4,63.0 553.4,72.5 568.9,86.2 581.9,99.0 607.8,126.2" fill="none" stroke="var(--muted)" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="10.0" y1="118.0" x2="628.0" y2="118.0" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><polygon points="630.0,118.0 623.0,114.2 623.0,121.8" fill="currentColor"/><text x="628.0" y="136.0" text-anchor="end" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">n</text><line x1="81.8" y1="34.0" x2="81.8" y2="196.0" stroke="currentColor" stroke-width="1" opacity="0.35" stroke-linecap="round"/><line x1="30.0" y1="115.0" x2="30.0" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="30.0" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">−2</text><line x1="55.9" y1="115.0" x2="55.9" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="81.8" y1="115.0" x2="81.8" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="81.8" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">0</text><line x1="107.7" y1="115.0" x2="107.7" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="133.6" y1="115.0" x2="133.6" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="133.6" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">2</text><line x1="159.5" y1="115.0" x2="159.5" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="185.5" y1="115.0" x2="185.5" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="185.5" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">4</text><line x1="211.4" y1="115.0" x2="211.4" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="237.3" y1="115.0" x2="237.3" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="237.3" y="111.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">6</text><line x1="263.2" y1="115.0" x2="263.2" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="289.1" y1="115.0" x2="289.1" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="289.1" y="111.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">8</text><line x1="315.0" y1="115.0" x2="315.0" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="340.9" y1="115.0" x2="340.9" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="340.9" y="111.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">10</text><line x1="366.8" y1="115.0" x2="366.8" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="392.7" y1="115.0" x2="392.7" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="392.7" y="111.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">12</text><line x1="418.6" y1="115.0" x2="418.6" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="444.5" y1="115.0" x2="444.5" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="444.5" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">14</text><line x1="470.5" y1="115.0" x2="470.5" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="496.4" y1="115.0" x2="496.4" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="496.4" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">16</text><line x1="522.3" y1="115.0" x2="522.3" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="548.2" y1="115.0" x2="548.2" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="548.2" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">18</text><line x1="574.1" y1="115.0" x2="574.1" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><line x1="600.0" y1="115.0" x2="600.0" y2="121.0" stroke="currentColor" stroke-width="1" stroke-linecap="round"/><text x="600.0" y="135.0" text-anchor="middle" fill="currentColor" style="font-size:11.5px;" opacity="0.8">20</text><line x1="30.0" y1="118.0" x2="30.0" y2="68.5" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="30.0" cy="68.5" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="55.9" y1="118.0" x2="55.9" y2="53.3" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="55.9" cy="53.3" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="81.8" y1="118.0" x2="81.8" y2="48.0" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="81.8" cy="48.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="107.7" y1="118.0" x2="107.7" y2="53.3" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="107.7" cy="53.3" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="133.6" y1="118.0" x2="133.6" y2="68.5" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="133.6" cy="68.5" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="159.5" y1="118.0" x2="159.5" y2="91.2" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="159.5" cy="91.2" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="185.5" y1="118.0" x2="185.5" y2="118.0" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="185.5" cy="118.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="211.4" y1="118.0" x2="211.4" y2="144.8" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="211.4" cy="144.8" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="237.3" y1="118.0" x2="237.3" y2="167.5" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="237.3" cy="167.5" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="263.2" y1="118.0" x2="263.2" y2="182.7" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="263.2" cy="182.7" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="289.1" y1="118.0" x2="289.1" y2="188.0" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="289.1" cy="188.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="315.0" y1="118.0" x2="315.0" y2="182.7" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="315.0" cy="182.7" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="340.9" y1="118.0" x2="340.9" y2="167.5" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="340.9" cy="167.5" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="366.8" y1="118.0" x2="366.8" y2="144.8" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="366.8" cy="144.8" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="392.7" y1="118.0" x2="392.7" y2="118.0" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="392.7" cy="118.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="418.6" y1="118.0" x2="418.6" y2="91.2" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="418.6" cy="91.2" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="444.5" y1="118.0" x2="444.5" y2="68.5" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="444.5" cy="68.5" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="470.5" y1="118.0" x2="470.5" y2="53.3" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="470.5" cy="53.3" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="496.4" y1="118.0" x2="496.4" y2="48.0" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="496.4" cy="48.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="522.3" y1="118.0" x2="522.3" y2="53.3" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="522.3" cy="53.3" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="548.2" y1="118.0" x2="548.2" y2="68.5" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="548.2" cy="68.5" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="574.1" y1="118.0" x2="574.1" y2="91.2" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="574.1" cy="91.2" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="600.0" y1="118.0" x2="600.0" y2="118.0" stroke="var(--accent)" stroke-width="2.0" stroke-linecap="round"/><circle cx="600.0" cy="118.0" r="4.4" fill="var(--accent)" stroke="none" stroke-width="1.4"/><line x1="392.7" y1="155.0" x2="392.7" y2="165.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="418.6" y1="155.0" x2="418.6" y2="165.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="392.7" y1="160.0" x2="418.6" y2="160.0" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><text x="405.7" y="178.0" text-anchor="middle" fill="currentColor" style="font-size:14px;font-family:'STIX Two Math','Latin Modern Math','Cambria Math','Times New Roman',serif;font-style:italic;">T</text><line x1="18.0" y1="18.0" x2="44.0" y2="18.0" stroke="var(--muted)" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/><text x="50.0" y="22.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">x(t) = cos(2πf₀t),  f₀ = 1/(16T)</text><line x1="300.0" y1="24.0" x2="300.0" y2="12.0" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/><circle cx="300.0" cy="12.0" r="4.0" fill="var(--accent)" stroke="none" stroke-width="1.4"/><text x="310.0" y="22.0" text-anchor="start" fill="currentColor" style="font-size:12.5px;">samples x[n] = x(nT) = cos(πn/8)</text><text x="622.0" y="154.0" text-anchor="end" fill="currentColor" style="font-size:12px;" opacity="0.85">n (t = nT)</text></svg><figcaption><strong>Notes Fig. 2: sampling keeps x(t) only at t = nT.</strong> Dashed: a cosine with f₀ = f<sub>s</sub>/16; stems: its samples x[n] = cos(πn/8), defined only at integer n.</figcaption></figure>

Values:
- **Continuous-valued**: any value. **Discrete-valued**: quantized to a predefined set.
- **Analog** = continuous-time, continuous-valued. **Digital** = discrete-time, discrete-valued.
- Computers store a fixed number of bits, so real digital signals are quantized. Floating point is precise enough that ECE 310 treats values as continuous; "digital" and "discrete-time" are used interchangeably.
- A/D and D/A conversion in detail: [[concepts/sampling|sampling]], [[concepts/ideal-reconstruction|ideal reconstruction]] ([[4-sampling-and-reconstruction/index|Unit 4]]).

## 3. Why use digital signals?

1. **Math is easier**: multiplication, exponentiation, matrix operations, square roots (slide: $e^{x[n]}$ vs $e^{x(t)}$).
2. **More reliable**: no drift with environment or component aging; repeatable; error correction.
3. **Cheap storage**: a 12-inch vinyl holds one album; a thumbnail-sized chip holds tens of thousands of songs, plus images and text.
4. **Design flexibility**: change numbers or code, not parts, PCB space and simulations.

Analog remains essential (power electronics, acoustics, RF); mixed-signal systems are common.

## 4. Writing a sequence: the n = 0 marker

> [!key] Notation (Lecture 2 §2)
> A finite sequence is listed with the $n=0$ sample marked (arrow, bold or underline); $x[n] = 0$ outside the list:
> $$
> x[n]=\{0,\ \underset{\uparrow}{4},\ -2,\ 0,\ 3,\ 1\}\quad\Longleftrightarrow\quad x[-1]=0,\ x[0]=4,\ x[1]=-2,\ \dots
> $$
> Slide 13: $x[n] = \{1, \underset{\uparrow}{4}, -2, 0, 3, 1, 2\} = \{x[n]\}_{n=-1}^{5}$, so $x[-1] = 1$, $x[0] = 4$, $x[5] = 2$.

Building blocks (Lecture 2, eqs. 21–24; notes Fig. 2: $2\delta[n+3] - 3\delta[n-1]$, $5u[2-n]$, $\cos(\frac{\pi}{10}n - \frac{\pi}{3})$, $2(-\tfrac34)^n$):
- [[concepts/kronecker-delta|Kronecker delta]] $\delta[n]$ and [[concepts/unit-step|unit step]] $u[n]$; $\delta[n-k]$ and the edge of $u[n-k]$ sit where the argument is zero, $n = k$.
- Sinusoids $A\sin(\omega_0 n+\theta)$, $\omega_0$ in radians per sample, and [[concepts/complex-exponential|exponentials]] $Ba^n$.
- Every signal is a sum of scaled, shifted impulses, $x[n]=\sum_k x[k]\,\delta[n-k]$.

## 5. Index maps: shift, flip, decimate

HW1 assumes these (beyond the notes). Values never change; only their positions do.

| operation | formula | effect |
|---|---|---|
| delay / advance | $x[n-n_0]$ / $x[n+n_0]$ ($n_0>0$) | shift right / left by $n_0$ |
| flip | $x[-n]$ | mirror about $n=0$ |
| flip and shift | $x[-n+n_0]=x[-(n-n_0)]$ | flip, then shift **right** by $n_0$ |
| decimate / compress | $x[Mn]$ | keep every $M$-th sample, squeezed together |
| fold | $x[\lvert n\rvert]$ | copy the right half onto the left |

> [!key] Order of operations for $y[n] = x[an+b]$
> - Shift first, then flip/compress: $v[n] = x[n+b]$, $y[n] = v[an]$.
> - Flip/compress first ⇒ shift by $b/a$: $x[-n+3] = x[-(n-3)]$ is flip, then shift **right** by 3.
> - Always safe: for each $n$, read off $x[an+b]$; check one sample, $y[0] = x[b]$.

> [!recipe] Sketching $y[n]=x[f(n)]$
> Do not guess the order of operations: tabulate. For each $n$ compute $f(n)$, read $x$ there, and mark the new $n=0$.
>
> [[homework/hw1|HW1]] #2: $x[n]=\{2,\ 4,\ \underset{\uparrow}{1},\ 0,\ -2,\ 5,\ 7,\ 3\}$. Then $y[n]=x[-n+3]$ has $y[0]=x[3]=5$, $y[-2]=x[5]=3$, $y[5]=x[-2]=2$:
> $$
> y[n]=\{3,\ 7,\ \underset{\uparrow}{5},\ -2,\ 0,\ 1,\ 4,\ 2\}\quad(-2\le n\le5),
> $$
> the flip of $x$ moved right by 3. And $z[n]=x[2n+1]=\{4,\ \underset{\uparrow}{0},\ 5,\ 3\}$ on $-1\le n\le2$: the samples $x[-2],x[0],x[2],x[4]$ are gone. Worked with figures: [[0-toolkit/03-sketching-and-transforming-signals|sketching and transforming signals]].

> [!trap]
> - **Always mark $n=0$.** $\{1,2,3\}$ without an arrow is not an answer; convolution results are graded on where the arrow sits.
> - **Wrong order**: flip then shift left by 3 is $x[-n-3]$, not $x[-n+3]$; compress then shift left by 1 is $x[2n+2]$, not $x[2n+1]$. Check $y[0] = x[b]$.
> - **Decimation loses samples**: $x[2n]$ cannot be undone, and $x[n/2]$ is undefined for odd $n$.
> - **$n$ is an integer**: $\cos(2\pi n)=1$ and $\sin(\pi n)=0$ for every $n$ ([[exams/midterm-1/past-exams/spring-2021|SP2021 #1e]]), and frequencies $\omega$ and $\omega+2\pi$ produce the same samples.
> - **Bounded is not summable**: $\lvert u[n]\rvert\le1$, yet $\sum_n u[n]=\infty$: the bounded-but-unstable $h$ of [[concepts/bibo-stability|BIBO stability]].
> - "Signal" vs. "sample": $x[n]$ may mean the whole sequence or the single number at index $n$ (course summary).

> [!exam] No standalone problem; graded everywhere
> The $n = 0$ arrow in every finite convolution, index maps like $x[\lvert n\rvert + n]$ in property tables, shifted steps setting sum limits.
> [[exams/midterm-1/past-exams/spring-2025|SP2025 #2, #3]] · [[exams/midterm-1/past-exams/fall-2019|FA2019 #2]] · [[exams/midterm-1/past-exams/fall-2025|FA2025 #3b, #5(a)]] · [[exams/midterm-1/past-exams/spring-2021|SP2021 #1e]] · [[homework/hw1|HW1]] #1–#3

**Where it appears:** [[1-signals-and-systems/01-digital-signals|Lecture 1]] §1–3, [[1-signals-and-systems/02-complex-numbers-and-elementary-signals|Lecture 2]] §2; [[homework/hw1|HW1]] #1–#3; [[0-toolkit/03-sketching-and-transforming-signals|sketching signals]]; [[problems/finite-length-convolution|finite-length convolution]] (e.g. FA2025 #3b, $x[n]=n\,u[n+1]\,u[-n+1]=\{-1,\ \underset{\uparrow}{0},\ 1\}$), [[problems/classifying-system-properties|classifying system properties]] ($x[2n]$, $x[\lvert n\rvert]$).

## Related
[[concepts/kronecker-delta|Kronecker delta]] · [[concepts/unit-step|unit step]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/sampling|sampling]] · [[concepts/sided-sequences|sided sequences]] · [[concepts/convolution|convolution]] · [[concepts/time-invariance|time-invariance]]

### Sources for this page
Lecture 1 notes §1–3 (eq. 1, Figs. 1–2) and slides; Lecture 2 §2 (notation, eqs. 21–24, Fig. 2) and slide 13; HW1 #1–#3 and solutions; course summary; FA2025 #3b; SP2021 #1e.
