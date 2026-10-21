---
title: "DTFT pairs"
description: "The course's DTFT pairs: finite sequences, exponentials, pulses, sinc and sinc², impulse pairs for periodic signals and the step, each with its validity condition."
tags: [concept, dtft, midterm-2]
aliases: ["DTFT pairs", "DTFT table", "common DTFT pairs"]
---

> [!key] Ordinary pairs (absolutely summable)
> | $x[n]$ | $X_d(\omega)$, $-\pi\le\omega\le\pi$ | holds when |
> |---|---|---|
> | $\delta[n-k]$ | $e^{-j\omega k}$ | $k$ integer |
> | $a^n u[n]$ | $\dfrac{1}{1-ae^{-j\omega}}$ | $\lvert a\rvert\lt1$ |
> | $-a^n u[-n-1]$ | $\dfrac{1}{1-ae^{-j\omega}}$ | $\lvert a\rvert>1$ |
> | $n\,a^n u[n]$ | $\dfrac{ae^{-j\omega}}{(1-ae^{-j\omega})^2}$ | $\lvert a\rvert\lt1$ |
> | $(n+1)\,a^n u[n]$ | $\dfrac{1}{(1-ae^{-j\omega})^2}$ | $\lvert a\rvert\lt1$ |
> | $a^{\lvert n\rvert}$ | $\dfrac{1-a^2}{1-2a\cos\omega+a^2}$ | $\lvert a\rvert\lt1$ |
> | $1$ for $0\le n\le L-1$ | $e^{-j\omega(L-1)/2}\,\dfrac{\sin(L\omega/2)}{\sin(\omega/2)}$ | — |
> | $\mathrm{rect}\!\left(\frac{n-k}{L}\right)$ | $\dfrac{\sin(L\omega/2)}{\sin(\omega/2)}\,e^{-j\omega k}$ | $L$ odd |
> | $\mathrm{sinc}^2(Ln)$ | $\dfrac{\pi}{L}\left(1-\dfrac{\lvert\omega\rvert}{2L}\right)$ for $\lvert\omega\rvert\le2L$, else $0$ | $0\lt L\le\frac{\pi}{2}$ |

> [!key] Energy-only pair (ideal low-pass; not absolutely summable)
> | $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ | holds when |
> |---|---|---|
> | $\dfrac{\sin(Wn)}{\pi n}=\dfrac{W}{\pi}\,\mathrm{sinc}(Wn)$ | $1$ for $\lvert\omega\rvert\le W$, else $0$ | $0\lt W\lt\pi$ |
> | $\mathrm{sinc}(Ln)$ | $\dfrac{\pi}{L}$ for $\lvert\omega\rvert\lt L$, else $0$ | $0\lt L\lt\pi$ |

> [!key] Impulse pairs (one period shown)
> | $x[n]$ | $X_d(\omega)$ on $-\pi\le\omega\le\pi$ |
> |---|---|
> | $1$ (all $n$) | $2\pi\,\delta(\omega)$ |
> | $e^{j\omega_0 n}$ | $2\pi\,\delta(\omega-\omega_0)$ |
> | $\cos(\omega_0 n)$ | $\pi\left[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\right]$ |
> | $\sin(\omega_0 n)$ | $-j\pi\left[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\right]$ |
> | $\cos(\omega_0 n+\theta)$ | $\pi\left[e^{j\theta}\delta(\omega-\omega_0)+e^{-j\theta}\delta(\omega+\omega_0)\right]$ |
> | $u[n]$ | $\dfrac{1}{1-e^{-j\omega}}+\pi\,\delta(\omega)$ |
> | $(-1)^n u[n]$ | $\dfrac{1}{1+e^{-j\omega}}+\pi\,\delta(\omega-\pi)$ |

Course $\mathrm{sinc}(x)=\frac{\sin x}{x}$. Routes: geometric series; $X(z)$ at $z=e^{j\omega}$ when the ROC contains $|z|=1$; [[concepts/dtft-properties|properties]] applied to a known pair. No DTFT: $2^nu[n]$, anything whose ROC misses the unit circle without touching it (a pole on $|z|=1$ gives impulses).

> [!trap]
> - $\frac{1}{1-2e^{-j\omega}}$ is not the DTFT of $2^nu[n]$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] 1(a)).
> - Finite length means no impulses: $\cos(\frac{\pi}{32}n)$, $0\le n\le15$ ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] 1(c)).
> - `np.sinc` and the [[supplements/transform-tables|transform tables]] mean $\frac{\sin\pi x}{\pi x}$. Even $L$ rect carries an extra $e^{-j\omega/2}$.
> - $e^{-j\omega/2}$ inverts to $\frac{\sin(\pi(n-\frac12))}{\pi(n-\frac12)}$, not $\delta[n-\frac12]$ ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] 1(b)).

**Where it appears:** [[3-fourier-analysis/13-fourier-analysis-and-the-dtft|L13]], [[3-fourier-analysis/14-dtft-properties|L14]] Table 1; [[problems/dtft-and-inverse-dtft|DTFT family]]; [[homework/hw5|HW5]] #1, [[homework/hw6|HW6]] #3–#5; [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #7.

## Related
[[concepts/dtft|DTFT]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/z-transform-pairs|z-transform pairs]] · [[supplements/transform-tables|transform tables]]

### Sources for this page
Lecture 14 notes §2, Table 1, slides 7–9; Lecture 13 Exercise 2; transform tables Table 6; HW5 #1 solutions; Midterm 2 keys cited.
