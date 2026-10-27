---
title: "DTFT properties"
description: "Shift, modulation, reversal, conjugation, differentiation, convolution, windowing; 2π-periodicity, Hermitian symmetry, Parseval; four free numbers; the sign erratum in Lecture 14's differentiation row."
tags: [concept, dtft, midterm-2]
aliases: ["DTFT properties", "properties of the DTFT", "DTFT property table", "Hermitian symmetry", "modulation property", "Parseval's relation", "windowing"]
---

*Lecture 14 (Fri Sep 25) §3 · [[homework/hw5|HW5]] #1–#2, [[homework/hw6|HW6]] #2, #7 · family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]]*

> [!abstract] In one breath
> - Most rows are the z-transform's with $z=e^{j\omega}$; new ones: modulation, windowing (periodic convolution), Parseval.
> - Real $x[n]$ $\iff$ Hermitian $X_d$: even magnitude, odd phase. Every DTFT is $2\pi$-periodic.
> - Four numbers come free: $X_d(0)$, $X_d(\pi)$, $\int X_d$, $\int|X_d|^2$.

## 1. The table

> [!key] Property table (Lecture 14, Table 2, differentiation sign corrected)
> | property | signal | DTFT | inherited from the z-transform? |
> |---|---|---|---|
> | linearity | $a\,x_1[n]+b\,x_2[n]$ | $aX_1(\omega)+bX_2(\omega)$ | yes |
> | periodicity | any $x[n]$ | $X_d(\omega+2\pi k)=X_d(\omega)$ | — |
> | time shift | $x[n-k]$, $k\in\mathbb{Z}$ | $e^{-j\omega k}X_d(\omega)$ | $z^{-k}X(z)$ |
> | frequency shift | $e^{j\omega_0 n}x[n]$ | $X_d(\omega-\omega_0)$ | $a^n x[n]\leftrightarrow X(z/a)$, $a=e^{j\omega_0}$ |
> | modulation | $x[n]\cos(\omega_0 n)$ | $\tfrac12X_d(\omega-\omega_0)+\tfrac12X_d(\omega+\omega_0)$ | Euler + frequency shift |
> | time reversal | $x[-n]$ | $X_d(-\omega)$ | $X(1/z)$ |
> | conjugation | $x^*[n]$ | $X_d^*(-\omega)$ | $X^*(z^*)$ |
> | differentiation | $n\,x[n]$ | $+j\,\dfrac{dX_d(\omega)}{d\omega}$ ⚠ | $-z\,\dfrac{dX}{dz}$ |
> | convolution | $x[n]*h[n]$ | $X_d(\omega)H_d(\omega)$ | $X(z)H(z)$ |
> | windowing | $x[n]\,w[n]$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}X_d(\theta)W_d(\omega-\theta)\,d\theta$ | DTFT only |
> | Hermitian symmetry | $x[n]$ real | $X_d^*(\omega)=X_d(-\omega)$ | — |
> | Parseval | $\sum_n\lvert x[n]\rvert^2$ | $\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega$ | DTFT only |

> [!warning] Erratum: $n\,x[n]\leftrightarrow+j\,\frac{dX_d}{d\omega}$, not $-j$
> Lecture 14 Table 2 and slide 15 print $-j$. Differentiating the definition term by term, $\frac{dX_d}{d\omega}=-j\sum_n n\,x[n]e^{-j\omega n}$, so the sign is $+j$ (transform tables Table 5 agree). See [[0-toolkit/05-errata|errata]].

## 2. Hermitian symmetry

> [!key] Real signal $\iff$ Hermitian DTFT (Lecture 14, eqs. 31–33)
> $$
> \begin{aligned}
> x[n]\ \text{real}\quad&\Longleftrightarrow\quad X_d(-\omega)=X_d^*(\omega)\\
> &\Longleftrightarrow\quad |X_d(-\omega)|=|X_d(\omega)|\ \text{and}\ \angle X_d(-\omega)=-\angle X_d(\omega).
> \end{aligned}
> $$
> Magnitude even, phase odd. "If and only if" (slide 11). For real $x$: $X_d(0)$ and $X_d(\pi)$ are real.

> [!derivation]- Real and imaginary parts (eqs. 26–30)
> With $e^{-j\omega n}=\cos(\omega n)-j\sin(\omega n)$:
> $$
> \begin{aligned}
> \mathrm{Re}\{X_d(\omega)\}&=\sum_n \mathrm{Re}\{x[n]\}\cos(\omega n)+\mathrm{Im}\{x[n]\}\sin(\omega n),\\
> \mathrm{Im}\{X_d(\omega)\}&=\sum_n \mathrm{Im}\{x[n]\}\cos(\omega n)-\mathrm{Re}\{x[n]\}\sin(\omega n).
> \end{aligned}
> $$
> With $\mathrm{Im}\{x[n]\}=0$ the first line is even in $\omega$ and the second odd, so $X_d(-\omega)=X_d^*(\omega)$. (Notes eq. 27's lower limit "$n=\infty$" should read $-\infty$.)

| $x[n]$ | $X_d(\omega)$ |
|---|---|
| real | Hermitian: $\lvert X_d\rvert$ even, $\angle X_d$ odd; $X_d(0)$, $X_d(\pi)$ real |
| real and even | real and even |
| real and odd | purely imaginary and odd |
| conjugate-symmetric, $x[-n]=x^*[n]$ | real |

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 262" width="640" height="262" role="img" aria-label="Magnitude and phase of the DTFT of 0.8^n u[n] and of its frequency-shifted complex version" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="174.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">|X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)|</text><line x1="34.0" y1="186.1" x2="314.0" y2="186.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="152.1" x2="314.0" y2="152.1" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="118.2" x2="314.0" y2="118.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="84.3" x2="314.0" y2="84.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="50.4" x2="314.0" y2="50.4" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="34.0" y1="220.0" x2="314.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="174.0" y1="30.0" x2="174.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="34.0" y1="217.0" x2="34.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="34.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="104.0" y1="217.0" x2="104.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="104.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="174.0" y1="217.0" x2="174.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="174.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="244.0" y1="217.0" x2="244.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="244.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="314.0" y1="217.0" x2="314.0" y2="223.0" stroke="currentColor" stroke-width="1"/><text x="314.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="171.0" y1="186.1" x2="177.0" y2="186.1" stroke="currentColor" stroke-width="1"/><text x="30.0" y="190.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><line x1="171.0" y1="152.1" x2="177.0" y2="152.1" stroke="currentColor" stroke-width="1"/><text x="30.0" y="156.1" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="171.0" y1="118.2" x2="177.0" y2="118.2" stroke="currentColor" stroke-width="1"/><text x="30.0" y="122.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">3</text><line x1="171.0" y1="84.3" x2="177.0" y2="84.3" stroke="currentColor" stroke-width="1"/><text x="30.0" y="88.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">4</text><line x1="171.0" y1="50.4" x2="177.0" y2="50.4" stroke="currentColor" stroke-width="1"/><text x="30.0" y="54.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">5</text><text x="314.0" y="214.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="34.0,199.6 53.1,200.9 78.1,201.1 98.9,200.1 119.9,197.7 132.7,195.2 145.1,191.6 156.3,186.7 165.4,180.8 170.3,176.5 174.5,171.9 180.1,163.9 185.0,154.4 189.9,141.2 193.4,128.5 196.9,112.1 205.7,58.8 207.1,53.3 207.8,51.5 208.8,50.4 209.5,50.5 210.2,51.5 212.3,58.8 220.4,108.4 223.2,122.4 226.7,136.5 230.2,147.4 233.0,154.4 237.2,162.7 241.4,169.2 247.0,175.8 252.6,180.8 260.1,185.8 268.0,189.7 276.2,192.7 286.2,195.4 298.1,197.7 314.0,199.6" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="34.0,201.2 52.2,200.8 69.7,199.6 87.9,197.2 101.7,194.2 111.7,191.0 121.3,186.7 130.4,180.8 137.4,174.3 143.0,167.2 147.2,160.2 151.4,151.0 155.6,138.9 159.1,125.5 162.6,108.4 170.7,58.8 172.1,53.3 172.8,51.5 173.8,50.4 174.5,50.5 175.2,51.5 177.3,58.8 185.4,108.4 188.9,125.5 192.4,138.9 196.6,151.0 200.8,160.2 205.0,167.2 210.6,174.3 217.6,180.8 226.7,186.7 236.3,191.0 246.3,194.2 260.1,197.2 278.3,199.6 295.8,200.8 314.0,201.2" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><line x1="209.0" y1="30.0" x2="209.0" y2="220.0" stroke="var(--accent2)" stroke-width="0.8" stroke-dasharray="2 3"/><text x="500.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">∠X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)</text><line x1="370.0" y1="220.0" x2="630.0" y2="220.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="172.5" x2="630.0" y2="172.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="77.5" x2="630.0" y2="77.5" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="30.0" x2="630.0" y2="30.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="125.0" x2="630.0" y2="125.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="500.0" y1="30.0" x2="500.0" y2="220.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="370.0" y1="122.0" x2="370.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="370.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="435.0" y1="122.0" x2="435.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="435.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="500.0" y1="122.0" x2="500.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="500.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="565.0" y1="122.0" x2="565.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="565.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/2</text><line x1="630.0" y1="122.0" x2="630.0" y2="128.0" stroke="currentColor" stroke-width="1"/><text x="630.0" y="234.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="497.0" y1="220.0" x2="503.0" y2="220.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="224.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/2</text><line x1="497.0" y1="172.5" x2="503.0" y2="172.5" stroke="currentColor" stroke-width="1"/><text x="366.0" y="176.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="497.0" y1="77.5" x2="503.0" y2="77.5" stroke="currentColor" stroke-width="1"/><text x="366.0" y="81.5" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="497.0" y1="30.0" x2="503.0" y2="30.0" stroke="currentColor" stroke-width="1"/><text x="366.0" y="34.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">π/2</text><text x="630.0" y="119.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="370.0,146.0 439.5,101.1 467.9,83.9 477.2,78.8 488.7,73.3 497.4,70.2 504.8,68.9 510.6,69.5 515.0,71.6 519.1,75.9 522.8,82.7 525.6,90.9 528.0,100.5 535.5,142.1 539.6,159.8 542.2,167.3 544.6,172.1 547.2,175.8 551.1,179.1 555.7,180.8 561.5,181.0 567.6,179.8 576.3,176.7 587.8,171.2 597.1,166.1 630.0,146.0" fill="none" stroke="var(--accent2)" stroke-width="1.8" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="370.0,125.0 409.4,99.6 439.5,81.6 449.9,76.2 458.2,72.5 466.4,69.8 472.3,68.9 475.5,69.0 478.8,69.7 483.1,72.1 486.6,75.9 490.5,83.2 493.1,90.9 495.7,101.5 503.2,143.2 507.1,159.8 509.5,166.8 513.6,174.4 517.5,178.4 521.2,180.3 524.5,181.0 527.7,181.1 533.6,180.2 543.8,176.7 553.5,172.1 567.2,164.6 586.9,152.7 630.0,125.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="40" y="250" fill="var(--accent)" style="font-size:12px">━ real: 0.8ⁿu[n]</text><text x="250" y="250" fill="var(--accent2)" style="font-size:12px">╌ complex: e<tspan baseline-shift="super" style="font-size:75%">jπn/4</tspan>·0.8ⁿu[n]</text></svg><figcaption><strong>Real signal ⇒ even magnitude, odd phase.</strong> Solid: x[n] = 0.8ⁿu[n], X<sub>d</sub>(ω) = 1/(1 − 0.8e<sup>−jω</sup>); dashed: e<sup>jπn/4</sup>·0.8ⁿu[n], the same spectrum shifted right by π/4 (frequency shift), with neither symmetry.</figcaption></figure>

Plot and compute on $\omega\in[-\pi,\pi]$, where the symmetry is easiest to see.

> [!question] Slide 12: $X_d(\omega)=\omega^2 e^{j\cos\omega}$ (on $-\pi\le\omega\le\pi$). Is $x[n]$ real-valued?

> [!success]- Answer: no
> Magnitude $\omega^2$ is even, but the phase $\cos\omega$ is **even**, not odd:
> $$
> X_d(-\omega)=\omega^2e^{j\cos\omega}\qquad\text{but}\qquad X_d^*(\omega)=\omega^2e^{-j\cos\omega},
> $$
> different wherever $\cos\omega\neq0$. So $x[n]$ is complex (and even: $x[0]\approx2.403-1.752j$, $x[\pm1]\approx-1.276+1.656j$).

> [!question] Slide 13: $x[n]$ is real. Which are true?
> (a) $X_d(0)=X_d(2\pi)$ $\quad$ (b) $X_d(\frac{\pi}{3})=X_d(-\frac{\pi}{3})$ $\quad$ (c) $X_d(\frac{\pi}{3})=X_d^*(-\frac{\pi}{3})$ $\quad$ (d) $X_d(\pi)=X_d(7\pi)$ $\quad$ (e) $X_d(\frac{2\pi}{3})=X_d^*(\frac{4\pi}{3})$

> [!success]- Answer: (a), (c), (d), (e)
> (a) periodicity. (b) not in general: the values at $\pm\frac{\pi}{3}$ are conjugates; only the magnitudes are equal. (c) Hermitian symmetry. (d) $7\pi=\pi+3\cdot2\pi$. (e) $\frac{4\pi}{3}=-\frac{2\pi}{3}+2\pi$, so $X_d(\frac{4\pi}{3})=X_d(-\frac{2\pi}{3})=X_d^*(\frac{2\pi}{3})$.

## 3. Periodicity, shifting, modulation

$$
X_d(\omega+2\pi k)=\sum_n x[n]\,e^{-j\omega n}\underbrace{e^{-j2\pi kn}}_{=1}=X_d(\omega),\qquad k\in\mathbb{Z}.
$$

- $e^{j\omega_0n}x[n]\leftrightarrow X_d(\omega-\omega_0)$: $\sum_n x[n]e^{j\omega_0 n}e^{-j\omega n}=\sum_n x[n]e^{-j(\omega-\omega_0)n}$ (eqs. 39–42).
- Euler gives modulation: $x[n]\cos(\omega_0n)\leftrightarrow\frac12X_d(\omega-\omega_0)+\frac12X_d(\omega+\omega_0)$, two half-height copies (eq. 43). Key in digital and wireless communications.
- Copies that run past $\pm\pi$ re-enter from the other side (periodicity).

## 4. Parseval, convolution, windowing

> [!recipe] Four numbers without computing $X_d(\omega)$
> $$
> \begin{gathered}
> X_d(0)=\sum_n x[n],\qquad X_d(\pi)=\sum_n(-1)^n x[n],\\
> \int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0],\qquad \int_{-\pi}^{\pi}\lvert X_d(\omega)\rvert^2d\omega=2\pi\sum_n\lvert x[n]\rvert^2 .
> \end{gathered}
> $$
> The first three are the definitions at $\omega=0$, $\omega=\pi$ and $n=0$; the last is **Parseval's relation**. [[homework/hw5|HW5]] #2: $x=\{2,-1,\underset{\uparrow}{1},-1,2\}$ gives $3$, $7$, $2\pi$, $22\pi$.

- **Convolution:** $x[n]*h[n]\leftrightarrow X_d(\omega)H_d(\omega)$ ($z=e^{j\omega}$ in the z-transform property). With $h$ an impulse response, $H_d(\omega)$ is the [[concepts/frequency-response|frequency response]].
- **Windowing** (multiplication in time), eqs. 47–51:

$$
x[n]\,w[n]\ \longleftrightarrow\ \frac{1}{2\pi}X_d(\omega)*W_d(\omega)=\frac{1}{2\pi}\int_{2\pi}X_d(\phi)\,W_d(\omega-\phi)\,d\phi .
$$

- Continuous (periodic) convolution in frequency. Proof: substitute the inverse DTFT of $X_d$ and swap sum and integral. Multiplying by a fixed $w[n]$ is **not** LTI. Returns as [[concepts/spectral-leakage|spectral leakage]] (Unit 5).

> [!trap]
> - Integer shifts only; $e^{-j\omega k}$ with non-integer $k$ is a shifted sinc, not $\delta[n-k]$.
> - Conjugation flips $\omega$ too: $x^*[n]\leftrightarrow X_d^*(-\omega)$.
> - Modulation halves heights; copies past $\pm\pi$ wrap and can overlap ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #2(b)).
> - Real $x$: $X_d(\omega)$ and $X_d(-\omega)$ are conjugates, not equal; test magnitude even and phase odd on the whole period ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #4(a), [[homework/hw6|HW6]] #7).
> - Substitute $z=e^{j\omega}$ only if the ROC contains $|z|=1$ ([[concepts/dtft|DTFT]]).

> [!exam] Exam
> Symmetry and periodicity true/false, values without $X_d$, modulation sketches, property chains. Family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].
> - MT2: [[exams/midterm-2/past-exams/fall-2024|FA2024]] #1(a), (b), #2, #4(a) · [[exams/midterm-2/past-exams/fall-2023|FA2023]] #1(a)–(c), #2 · [[exams/midterm-2/past-exams/spring-2023|SP2023]] #2–#4 · [[exams/midterm-2/past-exams/spring-2025|SP2025]] #2 · [[exams/midterm-2/past-exams/spring-2021|SP2021]] #6, #7 · [[exams/midterm-2/past-exams/fall-2021|FA2021]] #2(c) · [[exams/midterm-2/past-exams/fall-2019|FA2019]] #1(b), (e), #3, #5, #6
> - MT1: [[exams/midterm-1/past-exams/spring-2023|SP2023]] #1(d), (e), #9 · homework: [[homework/hw5|HW5]] #1–#2, [[homework/hw6|HW6]] #2–#5, #7

**Where it appears:** [[3-fourier-analysis/14-dtft-properties|L14]] §3 (slides 10–15), [[3-fourier-analysis/15-frequency-response|L15]], [[3-fourier-analysis/16-magnitude-and-phase-response|L16]]; [[problems/dtft-and-inverse-dtft|DTFT family]]; [[homework/hw5|HW5]] #1–#2, [[homework/hw6|HW6]] #2, #7; [[exams/quiz-2|Quiz 2]].

## Related
[[concepts/dtft|DTFT]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/z-transform-properties|z-transform properties]] · [[concepts/frequency-response|frequency response]] · [[concepts/window-functions|window functions]] · [[supplements/transform-tables|transform tables]]

### Sources for this page
Lecture 14 notes §3 (eqs. 26–51), Table 2, slides 10–15; transform tables Table 5; HW5 #1–#2 solutions; Midterm 2 keys cited.
