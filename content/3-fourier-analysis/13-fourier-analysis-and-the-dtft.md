---
title: "Lecture 13 — Fourier analysis and the DTFT"
description: "Periodic signals in continuous and discrete time, orthogonal harmonics, the continuous-time Fourier series and transform, the DTFS, and the DTFT X_d(ω) = Σ x[n]e^{−jωn}: definition, inverse, existence, uniqueness, 2π-periodicity."
tags: [lecture, midterm-2, dtft, fourier-series, fourier-analysis]
lecture: 13
---

*Lecture 13 · Wed Sep 23, 2026 · notes + slides "Fourier analysis" · prev: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] · next: [[3-fourier-analysis/14-dtft-properties|Lecture 14]]*

> [!abstract] In one breath
> - Harmonics are orthogonal, so inner products give the Fourier-series weights; letting the period grow gives the Fourier transform.
> - Discrete time: frequencies $2\pi$ apart are the same sequence, so $N_0$ harmonics suffice (DTFS) and every DTFT is $2\pi$-periodic.
> - DTFT $X_d(\omega)=\sum_nx[n]e^{-j\omega n}$; it exists if $\sum_n|x[n]|<\infty$.

> [!note] Starred objectives
> Computing CTFS and DTFS is not required; they lead to the DTFT. Required: periodicity of discrete-time sinusoids, computing a DTFT (or showing it does not exist), and what it represents.

## 1. Periodic signals

### 1.1 Continuous-time signals

- $x(t+T_0)=x(t)$ for all $t$. Smallest such $T_0>0$: **fundamental period**.
- Linear frequency $F_0=1/T_0$ (Hz). Radial frequency $\Omega_0=2\pi F_0$ (rad/s).
- Basic periodic signals: $e^{j\Omega_0t}$, $\cos(\Omega_0t)$. Periodic for every real $\Omega_0\neq0$; every $\Omega_0$ gives a different signal.
- **Harmonically related**: frequencies are integer multiples of one fundamental, $x_k(t)=e^{jk\Omega_0t}$, $k\in\mathbb{Z}$.

> [!key] Orthogonality of harmonics (notes eqs. 6–11)
> $$
> \begin{aligned}
> \int_{T_0}x_k(t)\,x_l^*(t)\,dt&=\int_{0}^{T_0}e^{j\Omega_0(k-l)t}\,dt=\left.\frac{e^{j\Omega_0(k-l)t}}{j\Omega_0(k-l)}\right|_{0}^{T_0}=\frac{e^{j2\pi(k-l)}-1}{j\Omega_0(k-l)}\\
> &=\begin{cases}0,&k\neq l\\ T_0,&k=l\end{cases}
> \end{aligned}
> $$
> For $k=l$ the integrand is $1$. Any interval of length $T_0$ works.

### 1.2 Discrete-time signals

- $x[n+N_0]=x[n]$, $N_0$ a positive integer (samples).
- $f_0=1/N_0$ (cycles/sample), $\omega_0=2\pi f_0$ (rad/sample) (notes eqs. 13–14). Basic signal: $e^{j\omega_0n}$.

> [!key] Frequencies $2\pi$ apart are the same sequence (notes eqs. 16–18)
> $$
> e^{j(\omega_0+2\pi k)n}=e^{j\omega_0n}\,e^{j2\pi kn}=e^{j\omega_0n},
> $$
> since $kn$ is an integer. Unique frequencies: $\omega_0\in[0,2\pi)$; the course plots $[-\pi,\pi]$. Example: $\cos(\tfrac{17\pi}{3}n)=\cos(\tfrac{5\pi}{3}n)=\cos(\tfrac{\pi}{3}n)$.

- "Low" and "high" mean distance to the nearest multiple of $2\pi$: $\omega=0$ is slowest, $\omega=\pi$ (the sequence $(-1)^n$) fastest.

> [!key] A discrete-time sinusoid is periodic only if $\omega_0/2\pi$ is rational (slide 4)
> $\cos(\omega_0n+\phi)$ and $e^{j\omega_0n}$ are periodic $\iff\dfrac{\omega_0}{2\pi}=\dfrac{K}{L}$ for integers $K,L$. With $K/L$ in lowest terms, $N_0=L$: $K$ full cycles in $L$ samples. $N_0$ is generally **not** $2\pi/\omega_0$.

| signal | $\omega_0/2\pi$ | periodic? | $N_0$ |
|---|---|---|---|
| $\cos(\tfrac{\pi}{4}n)$ | $\tfrac18$ | yes | $8$ |
| $\cos(\tfrac{3\pi}{8}n)$ | $\tfrac{3}{16}$ | yes | $16$ (while $2\pi/\omega_0=\tfrac{16}{3}$ is not an integer) |
| $e^{j0.4\pi n}$ | $\tfrac15$ | yes | $5$ |
| $\sin(\tfrac34n)$ | $\tfrac{3}{8\pi}$, irrational | no | none |

> [!question] Slide 6: which signals equal $x[n]=\sin(\tfrac{\pi}{3}n)$? (Select all that apply.)
> (a) $\sin(-\tfrac{\pi}{3}n)$ $\quad$ (b) $\sin(-\tfrac{5\pi}{3}n)$ $\quad$ (c) $\sin(\tfrac{4\pi}{3}n)$ $\quad$ (d) $\sin(\tfrac{13\pi}{3}n)$

> [!success]- Answer: (b) and (d)
> $\tfrac{\pi}{3}-2\pi=-\tfrac{5\pi}{3}$ gives (b); $\tfrac{\pi}{3}+4\pi=\tfrac{13\pi}{3}$ gives (d). (a) $\sin(-\tfrac{\pi}{3}n)=-\sin(\tfrac{\pi}{3}n)$. (c) $\tfrac{4\pi}{3}-2\pi=-\tfrac{2\pi}{3}$, so $\sin(\tfrac{4\pi}{3}n)=-\sin(\tfrac{2\pi}{3}n)$: a different frequency.

## 2. Continuous-time Fourier series

> [!key] Fourier series of a signal with period $T_0=2\pi/\Omega_0$ (notes eqs. 19, 23)
> $$
> x(t)=\sum_{k=-\infty}^{\infty}c_k\,e^{jk\Omega_0t}\qquad\qquad c_k=\frac{1}{T_0}\int_{T_0}x(t)\,e^{-jk\Omega_0t}\,dt
> $$
> Left: **synthesis**. Right: **analysis**. $c_k$ = how much of frequency $k\Omega_0$ is in $x(t)$.

> [!derivation]- Analysis equation (slide 9)
> Multiply the synthesis equation by $e^{-jl\Omega_0t}$, integrate over one period, swap sum and integral; orthogonality keeps only $k=l$:
> $$
> \int_{T_0}x(t)\,e^{-jl\Omega_0t}\,dt=\sum_{k=-\infty}^{\infty}c_k\int_{T_0}e^{jk\Omega_0t}e^{-jl\Omega_0t}\,dt=c_l\,T_0 .
> $$

- **Dirichlet conditions** (sufficient for convergence): $\int_{T_0}|x(t)|\,dt<\infty$; finitely many maxima, minima and finite jumps per period.
- Finite energy per period, $\int_{T_0}|x(t)|^2dt<\infty$, gives a second (energy) convergence.
- If the series exists, it is unique.

> [!question] Notes Fig. 1 / slide 10: Fourier series of the sawtooth $x(t)=t$ on $[0,1)$, period $T_0=1$
> Find $c_k$.

> [!success]- Answer
> $\Omega_0=2\pi$, $c_0=\int_0^1t\,dt=\tfrac12$. By parts:
> $$
> \begin{aligned}
> c_k&=\int_0^1t\,e^{-j2\pi kt}\,dt=\left.\frac{t\,e^{-j2\pi kt}}{-j2\pi k}\right|_0^1+\frac{1}{j2\pi k}\int_0^1e^{-j2\pi kt}\,dt\\
> &=\frac{1}{-j2\pi k}+0=\frac{j}{2\pi k},\qquad k\neq0 .
> \end{aligned}
> $$
> Real form: $x(t)=\tfrac12-\sum_{k=1}^{\infty}\dfrac{\sin(2\pi kt)}{\pi k}$. Erratum: the caption of notes Fig. 1 (and slide 10) prints $c_k=\tfrac{j}{\pi k}$, twice too large; the plotted partial sums use $\tfrac{j}{2\pi k}$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 240" width="680" height="240" role="img" aria-label="sawtooth wave with Fourier partial sums m = 3 and m = 50" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="353.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">partial sums of the Fourier series of the sawtooth x(t) = t, period 1</text><line x1="48.0" y1="115.0" x2="658.0" y2="115.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="58.3" x2="658.0" y2="58.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="171.7" x2="658.0" y2="171.7" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="251.3" y1="30.0" x2="251.3" y2="200.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="168.7" x2="48.0" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="48.0" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="149.7" y1="168.7" x2="149.7" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="149.7" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−½</text><line x1="251.3" y1="168.7" x2="251.3" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="251.3" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="353.0" y1="168.7" x2="353.0" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="353.0" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">½</text><line x1="454.7" y1="168.7" x2="454.7" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="454.7" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="556.3" y1="168.7" x2="556.3" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="556.3" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3/2</text><line x1="658.0" y1="168.7" x2="658.0" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="658.0" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2</text><line x1="248.3" y1="171.7" x2="254.3" y2="171.7" stroke="currentColor" stroke-width="1"/><text x="44.0" y="175.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="248.3" y1="115.0" x2="254.3" y2="115.0" stroke="currentColor" stroke-width="1"/><text x="44.0" y="119.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">½</text><line x1="248.3" y1="58.3" x2="254.3" y2="58.3" stroke="currentColor" stroke-width="1"/><text x="44.0" y="62.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="658.0" y="165.7" text-anchor="end" fill="var(--muted)" style="font-size:12px">t</text><polyline points="48.0,171.7 251.3,58.3" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="251.3,171.7 454.7,58.3" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="454.7,171.7 658.0,58.3" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="48.0,115.0 55.6,139.4 61.7,154.9 64.8,160.4 67.8,164.3 69.3,165.6 72.4,167.0 75.5,166.7 77.0,166.0 78.5,165.1 81.6,162.2 98.3,139.6 101.4,136.4 105.9,133.0 109.0,131.6 112.0,130.9 115.1,130.6 124.2,131.0 127.3,130.8 133.4,129.2 138.0,126.5 142.6,122.6 156.3,107.9 160.8,103.9 163.9,101.9 166.9,100.4 171.5,99.2 186.8,99.2 191.3,98.0 194.4,96.4 199.0,92.6 203.6,87.3 214.2,72.1 217.3,68.3 221.8,64.2 224.9,63.0 227.9,63.3 231.0,65.2 234.0,68.8 237.1,74.1 240.2,80.9 243.2,89.1 256.9,133.3 263.0,150.3 266.1,156.9 269.1,161.9 272.2,165.2 275.2,166.9 278.3,166.9 279.8,166.3 284.4,162.8 289.0,157.2 301.1,140.2 305.7,135.5 308.8,133.3 311.8,131.8 314.9,131.0 317.9,130.6 330.1,130.9 333.2,130.4 336.2,129.4 340.8,126.8 345.4,123.0 359.1,108.4 363.7,104.3 368.2,101.3 372.8,99.6 375.9,99.1 388.1,99.4 391.1,99.0 394.2,98.2 398.8,95.7 401.8,93.1 406.4,87.9 417.1,72.8 421.6,67.2 424.7,64.6 427.7,63.1 430.8,63.1 433.8,64.8 436.9,68.1 439.9,73.1 444.5,83.5 449.1,96.7 459.7,131.7 465.8,149.1 468.9,155.9 471.9,161.2 475.0,164.8 478.0,166.7 481.1,167.0 482.6,166.5 485.7,164.7 487.2,163.3 491.8,157.9 504.0,140.8 507.0,137.4 513.1,132.7 519.2,130.8 523.8,130.6 531.4,131.0 534.5,130.8 539.0,129.6 543.6,127.2 546.7,124.9 552.8,118.9 563.4,107.4 568.0,103.5 571.1,101.6 574.1,100.2 578.7,99.2 581.8,99.0 590.9,99.4 594.0,99.1 598.5,97.8 601.6,96.0 604.6,93.6 607.7,90.4 624.4,67.8 627.5,64.9 630.5,63.3 633.6,63.0 636.6,64.4 639.7,67.4 642.8,72.2 645.8,78.5 648.9,86.3 658.0,115.0" fill="none" stroke="var(--accent2)" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="48.0,115.0 49.2,170.6 50.0,180.7 52.1,163.9 53.7,171.7 54.1,172.0 56.1,164.3 57.8,168.3 58.2,168.3 60.2,163.0 61.8,165.5 62.2,165.3 64.3,161.2 65.9,162.9 66.3,162.7 68.3,159.2 69.6,160.3 70.4,160.2 72.0,157.3 72.8,157.3 73.6,158.0 74.4,157.8 76.1,155.2 76.5,155.0 78.1,155.7 80.1,153.0 82.2,153.3 84.2,150.8 86.2,151.0 88.3,148.6 90.3,148.7 92.3,146.4 94.4,146.4 96.4,144.2 98.4,144.1 100.5,141.9 102.5,141.8 104.5,139.7 106.6,139.5 108.2,137.7 110.6,137.2 112.3,135.4 114.7,134.9 116.7,133.0 118.4,132.9 120.4,130.9 122.4,130.6 124.5,128.7 126.5,128.3 128.5,126.4 130.6,126.0 132.2,124.4 134.6,123.8 136.7,121.9 138.7,121.5 140.7,119.6 142.8,119.2 144.4,117.6 146.8,116.9 148.4,115.3 150.9,114.7 152.5,113.1 155.0,112.4 156.6,110.8 158.6,110.4 160.6,108.5 162.7,108.1 164.7,106.2 166.3,106.0 168.8,104.0 170.8,103.6 172.8,101.7 174.9,101.3 176.9,99.4 178.9,99.1 181.0,97.1 183.0,96.8 184.6,95.1 187.1,94.6 188.7,92.8 191.1,92.3 192.8,90.5 194.8,90.3 196.8,88.2 198.9,88.1 200.9,85.9 202.9,85.8 205.0,83.6 207.0,83.6 209.0,81.3 211.1,81.4 213.1,79.0 215.1,79.2 217.2,76.7 219.2,77.0 221.2,74.3 222.9,75.0 223.3,74.8 224.9,72.2 225.7,72.0 226.5,72.7 227.3,72.7 229.0,69.8 229.8,69.7 231.0,70.8 233.0,67.3 233.4,67.1 235.1,68.8 237.1,64.7 237.5,64.5 239.1,67.0 241.2,61.7 241.6,61.7 243.2,65.7 245.2,58.0 245.6,58.3 247.3,66.1 247.7,64.9 249.3,49.3 250.1,59.4 250.5,73.6 252.1,156.4 253.0,178.6 253.4,180.7 255.0,165.1 255.4,163.9 257.0,171.7 257.4,172.0 259.5,164.3 261.1,168.3 261.5,168.3 263.5,163.0 265.2,165.5 265.6,165.3 267.6,161.2 268.8,162.6 269.6,162.7 271.7,159.2 272.9,160.3 273.7,160.2 275.3,157.3 276.1,157.3 277.0,158.0 277.8,157.8 279.4,155.2 279.8,155.0 281.4,155.7 283.5,153.0 285.5,153.3 287.5,150.8 289.6,151.0 291.6,148.6 293.6,148.7 295.7,146.4 297.7,146.4 299.7,144.2 301.8,144.1 303.8,141.9 305.8,141.8 307.9,139.7 309.9,139.5 311.5,137.7 314.0,137.2 315.6,135.4 318.0,134.9 320.1,133.0 321.7,132.9 323.7,130.9 325.8,130.6 327.8,128.7 329.8,128.3 331.4,126.7 333.9,126.0 336.3,124.0 338.0,123.8 340.0,121.9 342.0,121.5 344.1,119.6 345.7,119.4 347.7,117.6 350.2,116.9 351.8,115.3 354.2,114.7 355.8,113.1 358.3,112.4 359.9,110.8 361.9,110.4 364.0,108.5 366.0,108.1 368.0,106.2 369.7,106.0 372.1,104.0 374.1,103.6 376.2,101.7 378.2,101.3 380.2,99.4 382.3,99.1 384.3,97.1 385.9,97.0 388.0,95.1 390.4,94.6 392.0,92.8 394.5,92.3 396.5,90.3 398.1,90.3 400.2,88.2 402.2,88.1 404.2,85.9 406.3,85.8 408.3,83.6 410.3,83.6 412.4,81.3 414.4,81.4 416.4,79.0 418.5,79.2 420.5,76.7 422.5,77.0 424.6,74.3 426.2,75.0 426.6,74.8 428.2,72.2 429.0,72.0 429.9,72.7 430.7,72.7 432.3,69.8 433.1,69.7 434.3,70.8 436.4,67.3 436.8,67.1 438.4,68.8 440.4,64.7 440.8,64.5 442.5,67.0 444.5,61.7 444.9,61.7 446.5,65.7 448.6,58.0 449.0,58.3 450.6,66.1 451.0,64.9 452.6,49.3 453.0,51.4 453.9,73.6 455.5,156.4 455.9,170.6 456.7,180.7 458.3,165.1 458.7,163.9 460.4,171.7 460.8,172.0 462.8,164.3 464.4,168.3 464.8,168.3 466.9,163.0 468.5,165.5 468.9,165.3 470.9,161.2 472.6,162.9 473.0,162.7 475.0,159.2 476.2,160.3 477.0,160.2 478.7,157.3 479.5,157.3 480.3,158.0 481.1,157.8 482.7,155.2 483.1,155.0 484.8,155.7 486.8,153.0 488.8,153.3 490.9,150.8 492.9,151.0 494.9,148.6 497.0,148.7 499.0,146.4 501.0,146.4 503.1,144.2 505.1,144.1 507.1,141.9 509.2,141.8 511.2,139.7 513.2,139.5 514.9,137.7 517.3,137.2 518.9,135.4 521.4,134.9 523.0,133.2 525.0,132.9 527.1,130.9 529.1,130.6 531.1,128.7 533.2,128.3 535.2,126.4 537.2,126.0 538.8,124.4 541.3,123.8 543.3,121.9 545.4,121.5 547.4,119.6 549.4,119.2 551.0,117.6 553.5,116.9 555.1,115.3 557.6,114.7 559.2,113.1 561.6,112.4 563.2,110.8 565.3,110.4 567.3,108.5 569.3,108.1 571.4,106.2 573.8,105.6 575.4,104.0 577.5,103.6 579.5,101.7 581.5,101.3 583.6,99.4 585.6,99.1 587.6,97.1 589.3,97.0 591.3,95.1 593.7,94.6 595.4,92.8 597.8,92.3 599.4,90.5 601.5,90.3 603.5,88.2 605.5,88.1 607.6,85.9 609.6,85.8 611.6,83.6 613.7,83.6 615.7,81.3 617.7,81.4 619.8,79.0 621.8,79.2 623.8,76.7 625.9,77.0 627.9,74.3 629.5,75.0 629.9,74.8 631.6,72.2 632.4,72.0 633.2,72.7 634.0,72.7 635.6,69.8 636.4,69.7 637.7,70.8 639.7,67.3 640.1,67.1 641.7,68.8 643.8,64.7 644.2,64.5 645.8,67.0 647.8,61.7 648.2,61.7 649.9,65.7 651.9,58.0 652.3,58.3 653.9,66.1 656.0,49.3 656.8,59.4 658.0,115.0" fill="none" stroke="var(--accent)" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="125.3" y="52.7" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600">m = 3</text><text x="296.1" y="52.7" text-anchor="middle" fill="var(--accent)" style="font-size:12px;font-weight:600">m = 50</text></svg><figcaption><strong>Fourier partial sums of the sawtooth x(t) = t, period 1 (notes Fig. 1).</strong> With m = 3 (orange) only the trend appears; with m = 50 (teal) the fit is within 0.01 away from the jumps, but next to each jump the sum overshoots by 8% of the jump (Gibbs) and at the jump it lands on the midpoint ½.</figcaption></figure>

### 2.1 Continuous-time Fourier transform

Aperiodic signal = limit $T_0\to\infty$, so $\Omega_0\to0$ and the harmonics fill the real line. Informally (notes eqs. 26–28; the notes write $X(\Omega)$, the exams $X_c(\Omega)$ or $X_a(\Omega)$):

> [!key] Continuous-time Fourier transform (CTFT)
> $$
> X_c(\Omega)=\int_{-\infty}^{\infty}x(t)\,e^{-j\Omega t}\,dt\qquad\qquad x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X_c(\Omega)\,e^{j\Omega t}\,d\Omega
> $$
> Versus the series: integral over all time; $k\Omega_0\to\Omega$; no $1/T_0$; the synthesis sum becomes an integral.

- Exists under the Dirichlet conditions on every finite interval (notes); slide 12: finite energy $\int|x(t)|^2dt<\infty$. Unique if it exists.
- Tells how much of every frequency is in a signal, periodic or not.

## 3. Discrete-time Fourier series

Discrete-time harmonics $e^{j\frac{2\pi}{N_0}kn}$: only $N_0$ are distinct, since $k=N_0$ gives $e^{j2\pi n}=1$, the same as $k=0$ (notes eqs. 29–31).

> [!key] DTFS of a sequence with period $N_0$ (notes eqs. 32–33)
> $$
> x[n]=\sum_{k=0}^{N_0-1}c_k\,e^{j\frac{2\pi k}{N_0}n}\qquad\qquad c_k=\frac{1}{N_0}\sum_{n=0}^{N_0-1}x[n]\,e^{-j\frac{2\pi k}{N_0}n}
> $$
> Finite sums: the DTFS always exists, synthesis recovers $x$ exactly, coefficients are unique, $c_{k+N_0}=c_k$. Analysis follows from discrete orthogonality:
> $$
> \sum_{n=0}^{N_0-1}e^{j\frac{2\pi}{N_0}kn}\,e^{-j\frac{2\pi}{N_0}ln}=\begin{cases}N_0,&k-l\ \text{a multiple of } N_0\\ 0,&\text{otherwise.}\end{cases}
> $$

> [!question] Exercise 1 (notes): periodic pulse
> One period: $x[n]=1$ for $0\le n<L$, $0$ for $L\le n<N_0$. Find $c_k$.

> [!success]- Answer
> Finite geometric series, then factor out half-angle exponentials (Euler):
> $$
> \begin{aligned}
> c_k&=\frac{1}{N_0}\sum_{n=0}^{L-1}e^{-j\frac{2\pi k}{N_0}n}=\frac{1}{N_0}\,\frac{1-e^{-j2\pi kL/N_0}}{1-e^{-j2\pi k/N_0}}\\
> &=\frac{1}{N_0}\,e^{-j\frac{\pi k}{N_0}(L-1)}\,\frac{\sin(\pi kL/N_0)}{\sin(\pi k/N_0)},\qquad c_0=\frac{L}{N_0}.
> \end{aligned}
> $$
> $N_0=12$, $L=4$: $\lvert c_k\rvert=0.333,\ 0.279,\ 0.144,\ 0,\ 0.083,\ 0.075,\ 0$ for $k=0,\dots,6$, mirrored for $k=7,\dots,11$.

> [!trap] Traps
> - Notes eq. 40, $\angle c_k=-\frac{\pi k}{N_0}(L-1)$, is only the exponential's angle: where the sine ratio is negative, add $\pm\pi$.
> - $N_0=12$, $L=4$: $c_4=\frac{1}{12}\,e^{-j\pi}\,(-1)=+\frac{1}{12}$, so $\angle c_4=0$ (as in notes Fig. 2(e)), not $-\pi$.
> - Discrete-time period: $N_0=L$ from $\omega_0/2\pi=K/L$, not $2\pi/\omega_0$.
> - A z-transform formula is a DTFT only if its ROC contains $|z|=1$: $2^nu[n]$ has no DTFT.

## 4. Discrete-time Fourier transform

Let $N_0\to\infty$: the harmonic frequencies $\frac{2\pi k}{N_0}$ fill a continuum $\omega$ (notes eqs. 41–42).

> [!key] The DTFT and its inverse
> $$
> X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}\qquad\qquad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega
> $$
> $\omega$ in radians per sample. $\lvert X_d(\omega)\rvert$: **magnitude spectrum**; $\angle X_d(\omega)$: **phase spectrum**. The inverse may use any interval of length $2\pi$. Manolakis and Ingle write $X(e^{j\omega})$.

> [!key] Existence and uniqueness (notes eq. 43)
> If $\sum_n|x[n]|<\infty$, the sum converges for every $\omega$:
> $$
> |X_d(\omega)|\le\sum_{n=-\infty}^{\infty}|x[n]|<\infty .
> $$
> Sufficient, not necessary. If the DTFT exists, it is unique.

- Like the CTFT: complex-valued, continuous in $\omega$, says how much of each frequency is in $x[n]$.
- Unlike the CTFT: **$2\pi$-periodic**, so one period ($[-\pi,\pi]$) says everything:

$$
X_d(\omega+2\pi)=\sum_n x[n]\,e^{-j\omega n}\,e^{-j2\pi n}=X_d(\omega).
$$

> [!question] Exercise 2 (notes): the pulse $x[n]=1$ for $0\le n<L$, $0$ otherwise
> Find $X_d(\omega)$ and compare with Exercise 1.

> [!success]- Answer
> $$
> \begin{aligned}
> X_d(\omega)&=\sum_{n=0}^{L-1}e^{-j\omega n}=\frac{1-e^{-j\omega L}}{1-e^{-j\omega}}
> =\frac{e^{-j\omega L/2}}{e^{-j\omega/2}}\cdot\frac{e^{j\omega L/2}-e^{-j\omega L/2}}{e^{j\omega/2}-e^{-j\omega/2}}\\
> &=e^{-j\omega(L-1)/2}\,\frac{\sin(\omega L/2)}{\sin(\omega/2)},\qquad X_d(0)=L .
> \end{aligned}
> $$
> (Notes eq. 47 prints the numerator as $e^{j\omega L/2}-e^{j\omega L/2}$; the second exponent needs a minus sign.) At $\omega_k=\frac{2\pi k}{N_0}$ this is $N_0\,c_k$ (notes eq. 49): **DTFS coefficients are DTFT samples divided by $N_0$**.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 370" width="680" height="370" role="img" aria-label="periodic DTFT magnitude of a 4-sample pulse with DTFS samples, and periodic impulses for a cosine" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="353.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(a) |X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| for x[n] = u[n] − u[n−4], with 12·|c<tspan baseline-shift="sub" style="font-size:75%">k</tspan>| of its period-12 version</text><rect x="251.3" y="28.0" width="203.3" height="120.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="48.0" y1="96.9" x2="658.0" y2="96.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="45.9" x2="658.0" y2="45.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="148.0" x2="658.0" y2="148.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="353.0" y1="28.0" x2="353.0" y2="148.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="145.0" x2="48.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="48.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="149.7" y1="145.0" x2="149.7" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="149.7" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="251.3" y1="145.0" x2="251.3" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="251.3" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="353.0" y1="145.0" x2="353.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="353.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="454.7" y1="145.0" x2="454.7" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="454.7" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="556.3" y1="145.0" x2="556.3" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="556.3" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="658.0" y1="145.0" x2="658.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="658.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><line x1="350.0" y1="148.0" x2="356.0" y2="148.0" stroke="currentColor" stroke-width="1"/><text x="44.0" y="152.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="350.0" y1="96.9" x2="356.0" y2="96.9" stroke="currentColor" stroke-width="1"/><text x="44.0" y="100.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="350.0" y1="45.9" x2="356.0" y2="45.9" stroke="currentColor" stroke-width="1"/><text x="44.0" y="49.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">4</text><text x="658.0" y="142.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="48.0,148.0 55.6,136.3 62.2,127.8 67.8,122.8 71.9,120.7 74.4,120.2 76.0,120.2 79.5,121.1 82.1,122.6 85.6,125.7 88.7,129.4 91.2,133.2 94.8,139.5 98.8,148.0 106.5,129.3 123.2,83.8 129.8,68.3 135.4,57.8 140.5,50.9 144.6,47.4 146.6,46.4 148.7,45.9 152.7,46.4 156.8,48.9 161.9,54.7 167.0,63.2 174.6,80.0 194.4,133.3 200.5,148.0 207.1,134.9 211.7,128.1 215.2,124.2 217.8,122.2 220.8,120.7 223.4,120.2 224.9,120.2 229.0,121.3 232.5,123.5 235.1,125.7 240.7,132.1 251.3,148.0 262.0,132.1 265.6,127.8 269.6,123.9 275.2,120.7 277.8,120.2 281.8,120.7 284.9,122.2 287.4,124.2 292.0,129.4 297.1,137.6 302.2,148.0 308.3,133.3 325.0,87.8 330.1,75.1 334.2,66.2 338.8,57.8 343.3,51.5 347.9,47.4 352.0,45.9 356.1,46.4 360.1,48.9 362.2,50.9 365.2,54.7 370.3,63.2 374.9,72.8 380.5,86.4 397.7,133.3 403.8,148.0 410.4,134.9 415.0,128.1 418.6,124.2 421.1,122.2 424.2,120.7 426.7,120.2 429.8,120.5 432.3,121.3 435.9,123.5 438.4,125.7 444.0,132.1 454.7,148.0 465.3,132.1 470.9,125.7 474.5,122.8 478.6,120.7 481.1,120.2 485.2,120.7 488.2,122.2 490.8,124.2 495.3,129.4 500.4,137.6 505.5,148.0 514.7,125.2 529.9,83.8 537.5,66.2 543.1,56.2 547.2,50.9 551.2,47.4 555.3,45.9 557.4,45.9 559.9,46.6 562.4,48.1 565.5,50.9 570.6,57.8 575.7,67.3 582.8,83.8 599.5,129.3 607.2,148.0 611.2,139.5 617.3,129.4 620.4,125.7 623.9,122.6 627.5,120.7 630.0,120.2 631.6,120.2 635.6,121.3 639.2,123.5 641.7,125.7 648.9,134.2 658.0,148.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="48.0" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="64.9" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="81.9" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="98.8" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="115.8" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="132.7" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="149.7" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="166.6" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="183.6" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="200.5" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="217.4" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="234.4" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="251.3" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="268.3" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="285.2" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="302.2" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="319.1" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="336.1" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="353.0" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="369.9" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="386.9" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="403.8" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="420.8" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="437.7" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="454.7" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="471.6" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="488.6" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="505.5" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="522.4" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="539.4" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="556.3" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="573.3" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="590.2" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="607.2" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="624.1" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="641.1" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="658.0" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="383.0" y="49.9" text-anchor="start" fill="var(--accent)" style="font-size:11px">one period</text><text x="353.0" y="208.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(b) X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) for cos(πn/3): impulses of area π at ±π/3, repeated every 2π</text><rect x="251.3" y="214.0" width="203.3" height="120.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="48.0" y1="334.0" x2="658.0" y2="334.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="353.0" y1="214.0" x2="353.0" y2="334.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="331.0" x2="48.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="48.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="149.7" y1="331.0" x2="149.7" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="149.7" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="251.3" y1="331.0" x2="251.3" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="251.3" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="353.0" y1="331.0" x2="353.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="353.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="454.7" y1="331.0" x2="454.7" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="454.7" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="556.3" y1="331.0" x2="556.3" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="556.3" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="658.0" y1="331.0" x2="658.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="658.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><text x="658.0" y="328.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><line x1="115.8" y1="334.0" x2="115.8" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M110.8,260.3 L115.8,252.3 L120.8,260.3 Z" fill="var(--muted)"/><line x1="183.6" y1="334.0" x2="183.6" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M178.6,260.3 L183.6,252.3 L188.6,260.3 Z" fill="var(--muted)"/><line x1="319.1" y1="334.0" x2="319.1" y2="258.3" stroke="var(--hi)" stroke-width="2"/><path d="M314.1,260.3 L319.1,252.3 L324.1,260.3 Z" fill="var(--hi)"/><text x="325.1" y="256.3" text-anchor="start" fill="var(--hi)" style="font-size:11px">π</text><line x1="386.9" y1="334.0" x2="386.9" y2="258.3" stroke="var(--hi)" stroke-width="2"/><path d="M381.9,260.3 L386.9,252.3 L391.9,260.3 Z" fill="var(--hi)"/><text x="392.9" y="256.3" text-anchor="start" fill="var(--hi)" style="font-size:11px">π</text><line x1="522.4" y1="334.0" x2="522.4" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M517.4,260.3 L522.4,252.3 L527.4,260.3 Z" fill="var(--muted)"/><line x1="590.2" y1="334.0" x2="590.2" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M585.2,260.3 L590.2,252.3 L595.2,260.3 Z" fill="var(--muted)"/><text x="386.9" y="360.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px">π/3</text><text x="319.1" y="360.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px">−π/3</text></svg><figcaption><strong>DTFS coefficients sample the DTFT (cf. notes Fig. 2).</strong> (a) |X<sub>d</sub>(ω)| = |sin(2ω)/sin(ω/2)| of the 4-sample pulse repeats every 2π, and the dots are 12·|c<sub>k</sub>| of its period-12 version at ω<sub>k</sub> = 2πk/12; (b) cos(πn/3) is not absolutely summable, and its DTFT is impulses of area π at ±π/3, repeated every 2π (Lecture 14).</figcaption></figure>

> [!question] Slide 15: DTFT of $x[n]=\{\underset{\uparrow}{1},0,1,0,1\}$

> [!success]- Answer
> $x[n]=\delta[n]+\delta[n-2]+\delta[n-4]$:
> $$
> X_d(\omega)=1+e^{-j2\omega}+e^{-j4\omega}=e^{-j2\omega}\big(e^{j2\omega}+1+e^{-j2\omega}\big)=e^{-j2\omega}\big(1+2\cos(2\omega)\big).
> $$
> $X_d(0)=3$, $X_d(\frac{\pi}{2})=e^{-j\pi}(1-2)=1$, $X_d(\pi)=3$.

> [!question] Slide 16: $X_d(\omega)=2j\sin\omega$. Which sequence is $x[n]$?
> (a) $\{\underset{\uparrow}{1},0,-1\}$ $\quad$ (b) $\{1,\underset{\uparrow}{0},-1\}$ $\quad$ (c) $\{\underset{\uparrow}{2},0,-2\}$ $\quad$ (d) $\{2,\underset{\uparrow}{0},-2\}$

> [!success]- Answer: (b)
> $2j\sin\omega=e^{j\omega}-e^{-j\omega}$: $x[-1]=1$, $x[1]=-1$. Others: (a) $1-e^{-j2\omega}$, (c) $2-2e^{-j2\omega}$, (d) $2e^{j\omega}-2e^{-j\omega}=4j\sin\omega$.

> [!exam] Exam
> Midterm 2: DTFTs of short sequences from the definition; true/false on existence, uniqueness, $2\pi$-periodicity and zero-padding (it leaves $X_d$ unchanged). Family: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]].
> - MT2: [[exams/midterm-2/past-exams/fall-2024|FA2024]] #1(a), (b), (d), #3(a) · [[exams/midterm-2/past-exams/fall-2023|FA2023]] #1(a), (b), (f) · [[exams/midterm-2/past-exams/spring-2023|SP2023]] #1(c), #3 · [[exams/midterm-2/past-exams/spring-2025|SP2025]] #1(a), (d) · [[exams/midterm-2/past-exams/spring-2021|SP2021]] #3 · [[exams/midterm-2/past-exams/fall-2019|FA2019]] #1(a)–(c), (e)
> - MT1: [[exams/midterm-1/past-exams/spring-2023|SP2023]] #1(d), #8 · homework: [[homework/hw5|HW5]] #1, [[homework/hw6|HW6]] #1

## Related

[[concepts/dtft|DTFT]] · [[concepts/fourier-series|Fourier series]] · [[concepts/complex-exponential|complex exponential]] · [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] · [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · [[3-fourier-analysis/index|Unit 3]] · [[supplements/transform-tables|transform tables]]

### Sources for this page

Snyder, ECE 310 Lecture 13 notes (§§1–4, Exercises 1–2, Figs. 1–2) and slides of Sep 23, 2026 (annotated slides 5, 6, 15, 16); Singer–Munson §2.3; HW5–HW6; past Midterm 2 exams.
