---
title: "Lecture 13 — Fourier analysis and the DTFT"
description: "Periodic signals in continuous and discrete time (a discrete-time sinusoid is periodic only if ω₀/2π is rational, and frequencies 2π apart are the same signal); orthogonal harmonics; the continuous-time Fourier series and, as the period grows, the Fourier transform; the DTFS of a periodic sequence; the DTFT X_d(ω) = Σ x[n]e^{−jωn} and its inverse; 2π-periodicity, existence (absolute summability) and uniqueness; impulses for e^{jω₀n}; rect ↔ sinc; the worked examples of notes and slides, and how Midterm 2 tests them."
tags: [lecture, midterm-2, dtft, fourier-series, fourier-analysis]
lecture: 13
---

*Lecture 13 · Wed Sep 23, 2026 · notes + slides "Fourier analysis" · prev: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] · next: [[3-fourier-analysis/14-dtft-properties|Lecture 14]]*

> [!abstract] In one breath
> A periodic signal is a sum of **harmonics** $e^{jk\Omega_0 t}$, and because harmonics are orthogonal, the weight of each one is found by an inner product: that is the **Fourier series**. Let the period grow without bound and the harmonics crowd into a continuum: the **Fourier transform**. Discrete time adds one twist that shapes everything after it: $e^{j(\omega+2\pi)n}=e^{j\omega n}$, so frequencies $2\pi$ apart are the same sequence. Hence a discrete-time sinusoid is periodic only when $\omega_0/2\pi$ is rational, a periodic sequence needs only $N_0$ harmonics (the DTFS), and the **discrete-time Fourier transform** $X_d(\omega)=\sum_n x[n]e^{-j\omega n}$ is $2\pi$-periodic, so its inverse integrates over one period, $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)e^{j\omega n}d\omega$. The DTFT surely exists when $\sum_n|x[n]|<\infty$; everlasting sinusoids are not absolutely summable, and their DTFTs are impulses, $e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$ on each period. Exams ask you to compute $X_d(\omega)$ for short sequences, read off $X_d(0)$, $X_d(\pi)$ and $\int X_d$, invert sketched rectangles into sincs, and answer true/false questions on periodicity and existence.

> [!note] What you are expected to compute
> The notes star two learning objectives: you will **not** be asked to compute continuous- or discrete-time Fourier series in this course. They are here because they lead, step by step, to the DTFT. What you must be able to do: decide whether a discrete-time sinusoid is periodic and which frequencies are equivalent; compute a DTFT from the definition or show that it does not exist; and say what it means. Lecture 14 reaches the DTFT a second way, from the z-transform.

## 1. Periodic signals

**Continuous time.** $x(t)$ is periodic with period $T_0$ (seconds) if $x(t+T_0)=x(t)$ for all $t$; the smallest such $T_0>0$ is the **fundamental period**. It comes with the linear frequency $F_0=1/T_0$ (cycles per second, Hz) and the radial frequency $\Omega_0=2\pi F_0$ (radians per second). The basic examples are $\cos(\Omega_0t)$ and $e^{j\Omega_0t}$, periodic with $T_0=2\pi/|\Omega_0|$ for **every** real $\Omega_0\neq0$, and every $\Omega_0\in(-\infty,\infty)$ gives a different signal (annotated slide 5). Signals are **harmonically related** when their frequencies are integer multiples of one fundamental frequency: $x_k(t)=e^{jk\Omega_0t}$, $k\in\mathbb{Z}$, all share the period $T_0$.

**Discrete time.** $x[n]$ is periodic with period $N_0$ if $x[n+N_0]=x[n]$ for all $n$, where $N_0$ is a positive **integer** (samples). As in continuous time, a period $N_0$ goes with the linear frequency $f_0=1/N_0$ (cycles per sample) and the radial frequency $2\pi f_0$ (radians per sample) (notes eqs. 13–14). Two things are different from continuous time.

> [!key] Frequencies $2\pi$ apart are the same sequence (annotated slide 5)
> $$
> e^{j(\omega_0+2\pi k)n}=e^{j\omega_0n}\,e^{j2\pi kn}=e^{j\omega_0n},
> $$
> because $k$ and $n$ are integers, so $kn$ is an integer and $e^{j2\pi kn}=1$. Only one interval of length $2\pi$ holds distinct frequencies: the notes use $[0,2\pi)$, and the course plots $[-\pi,\pi]$. Example from the notes: $\cos(\tfrac{17\pi}{3}n)=\cos(\tfrac{5\pi}{3}n)=\cos(\tfrac{\pi}{3}n)$, since $\tfrac{17\pi}{3}-4\pi=\tfrac{5\pi}{3}=2\pi-\tfrac{\pi}{3}$ and cosine is even.

So "low" and "high" frequency mean distance to the nearest multiple of $2\pi$: $\omega=0$ (a constant) is the slowest sequence, $\omega=\pi$ (the sequence $(-1)^n$) is the fastest, and $\omega=2\pi-0.1$ is just as slow as $\omega=-0.1$.

> [!key] A discrete-time sinusoid is periodic only if $\omega_0/2\pi$ is rational (slide 4)
> $\cos(\omega_0n+\phi)$ and $e^{j\omega_0n}$ repeat after $N$ samples exactly when $\omega_0N$ is a multiple of $2\pi$, i.e. $\dfrac{\omega_0}{2\pi}=\dfrac{K}{N}$. So they are periodic if and only if $\dfrac{\omega_0}{2\pi}=\dfrac{K}{L}$ for integers $K,L$, and with $K/L$ in lowest terms the fundamental period is $N_0=L$, which is generally **not** $2\pi/\omega_0$: in $L$ samples the sinusoid completes $K$ full cycles. ($\cos(\tfrac{3\pi}{8}n)$ repeats every $16$ samples, after exactly $3$ cycles.)

| signal | $\omega_0/2\pi$ | periodic? | $N_0$ |
|---|---|---|---|
| $\cos(\tfrac{\pi}{4}n)$ | $\tfrac18$ | yes | $8$ |
| $\cos(\tfrac{3\pi}{8}n)$ | $\tfrac{3}{16}$ | yes | $16$ (while $2\pi/\omega_0=\tfrac{16}{3}$ is not an integer) |
| $e^{j0.4\pi n}$ | $\tfrac15$ | yes | $5$ |
| $\sin(\tfrac34n)$ | $\tfrac{3}{8\pi}$, irrational | no | none |

The last row is Singer and Munson's example (their Fig. 2.4, next to the periodic $\sin(\tfrac{\pi}{4}n)$). Its continuous-time parent $\sin(\tfrac34t)$ *is* periodic: sampling a periodic signal does not guarantee a periodic sequence.

> [!question] Slide 6: which signals are equal to $x[n]=\sin(\tfrac{\pi}{3}n)$? (Select all that apply.)
> (a) $\sin(-\tfrac{\pi}{3}n)$ $\quad$ (b) $\sin(-\tfrac{5\pi}{3}n)$ $\quad$ (c) $\sin(\tfrac{4\pi}{3}n)$ $\quad$ (d) $\sin(\tfrac{13\pi}{3}n)$

> [!success]- Answer: (b) and (d) (annotated slide 6; checked for $\lvert n\rvert\le50$)
> Add multiples of $2\pi$ to $\tfrac{\pi}{3}$: $k=-1$ gives $\tfrac{\pi}{3}-2\pi=-\tfrac{5\pi}{3}$, which is (b), and $k=2$ gives $\tfrac{\pi}{3}+4\pi=\tfrac{13\pi}{3}$, which is (d). (a) is $\sin(-\tfrac{\pi}{3}n)=-\sin(\tfrac{\pi}{3}n)$, the negative of $x$. (c) $\tfrac{4\pi}{3}-2\pi=-\tfrac{2\pi}{3}$, so $\sin(\tfrac{4\pi}{3}n)=-\sin(\tfrac{2\pi}{3}n)$: a different frequency.

## 2. Harmonics are orthogonal

One fact makes every Fourier formula work (notes eqs. 6–11). Over one period,

$$
\begin{aligned}
\int_{T_0}x_k(t)\,x_l^*(t)\,dt&=\int_{0}^{T_0}e^{j\Omega_0(k-l)t}\,dt=\left.\frac{e^{j\Omega_0(k-l)t}}{j\Omega_0(k-l)}\right|_{0}^{T_0}=\frac{e^{j2\pi(k-l)}-1}{j\Omega_0(k-l)}\\
&=\begin{cases}0,&k\neq l\\ T_0,&k=l\end{cases}
\end{aligned}
$$

(the case $k=l$ directly: the integrand is $1$). For $k\neq l$ the integrand turns $k-l$ full circles in one period and averages to zero; any interval of length $T_0$ gives the same result. The discrete-time twin is a sum of roots of unity, a finite geometric series:

$$
\sum_{n=0}^{N_0-1}e^{j\frac{2\pi}{N_0}kn}\,e^{-j\frac{2\pi}{N_0}ln}=\begin{cases}N_0,&k-l\ \text{a multiple of } N_0\\ 0,&\text{otherwise.}\end{cases}
$$

In the language of [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]]: harmonics are templates that do not respond to one another at all, so an inner product with one harmonic picks out exactly that harmonic's share of a signal.

## 3. The continuous-time Fourier series

Build a periodic signal from harmonics (synthesis), then recover the weights by inner products (analysis):

> [!key] Fourier series of a signal with period $T_0=2\pi/\Omega_0$ (notes eqs. 19 and 23)
> $$
> x(t)=\sum_{k=-\infty}^{\infty}c_k\,e^{jk\Omega_0t}\qquad\qquad c_k=\frac{1}{T_0}\int_{T_0}x(t)\,e^{-jk\Omega_0t}\,dt
> $$
> $c_k$ represents how much of the frequency $k\Omega_0$ is in $x(t)$ (annotated slide 8). The left formula is the **synthesis** equation, the right one the **analysis** equation.

> [!derivation]- Where the analysis equation comes from (slide 9)
> Multiply the synthesis equation by $e^{-jl\Omega_0t}$ and integrate over one period. The sum and the integral swap, and orthogonality kills every term except $k=l$:
> $$
> \int_{T_0}x(t)\,e^{-jl\Omega_0t}\,dt=\sum_{k=-\infty}^{\infty}c_k\int_{T_0}e^{jk\Omega_0t}e^{-jl\Omega_0t}\,dt=c_l\,T_0 .
> $$
> Divide by $T_0$ and rename $l$ as $k$.

**When it works.** The **Dirichlet conditions** guarantee convergence: $x$ is absolutely integrable over one period, $\int_{T_0}|x(t)|\,dt<\infty$, and has finitely many maxima, minima and finite jumps per period. The series then equals $x(t)$ wherever $x$ is continuous and the midpoint of the jump at a discontinuity. Finite energy per period, $\int_{T_0}|x(t)|^2dt<\infty$, gives convergence in a second (energy) sense. When the series exists it is unique.

> [!example] The sawtooth (notes Fig. 1, slide 10)
> $x(t)=t$ on $[0,1)$, repeated with $T_0=1$, $\Omega_0=2\pi$. Then $c_0=\int_0^1t\,dt=\tfrac12$ and, integrating by parts,
> $$
> \begin{aligned}
> c_k&=\int_0^1t\,e^{-j2\pi kt}\,dt=\left.\frac{t\,e^{-j2\pi kt}}{-j2\pi k}\right|_0^1+\frac{1}{j2\pi k}\int_0^1e^{-j2\pi kt}\,dt\\
> &=\frac{1}{-j2\pi k}+0=\frac{j}{2\pi k},\qquad k\neq0 .
> \end{aligned}
> $$
> Pairing $k$ with $-k$ gives the real form $x(t)=\tfrac12-\sum_{k=1}^{\infty}\dfrac{\sin(2\pi kt)}{\pi k}$. The caption of the notes' Fig. 1 (and slide 10) prints $c_k=\tfrac{j}{\pi k}$, twice too large; the plotted partial sums use the correct $\tfrac{j}{2\pi k}$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 240" width="680" height="240" role="img" aria-label="sawtooth wave with Fourier partial sums m = 3 and m = 50" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="353.0" y="24.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">partial sums of the Fourier series of the sawtooth x(t) = t, period 1</text><line x1="48.0" y1="115.0" x2="658.0" y2="115.0" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="58.3" x2="658.0" y2="58.3" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="171.7" x2="658.0" y2="171.7" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="251.3" y1="30.0" x2="251.3" y2="200.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="168.7" x2="48.0" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="48.0" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−1</text><line x1="149.7" y1="168.7" x2="149.7" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="149.7" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−½</text><line x1="251.3" y1="168.7" x2="251.3" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="251.3" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="353.0" y1="168.7" x2="353.0" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="353.0" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">½</text><line x1="454.7" y1="168.7" x2="454.7" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="454.7" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">1</text><line x1="556.3" y1="168.7" x2="556.3" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="556.3" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3/2</text><line x1="658.0" y1="168.7" x2="658.0" y2="174.7" stroke="currentColor" stroke-width="1"/><text x="658.0" y="214.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2</text><line x1="248.3" y1="171.7" x2="254.3" y2="171.7" stroke="currentColor" stroke-width="1"/><text x="44.0" y="175.7" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="248.3" y1="115.0" x2="254.3" y2="115.0" stroke="currentColor" stroke-width="1"/><text x="44.0" y="119.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">½</text><line x1="248.3" y1="58.3" x2="254.3" y2="58.3" stroke="currentColor" stroke-width="1"/><text x="44.0" y="62.3" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="658.0" y="165.7" text-anchor="end" fill="var(--muted)" style="font-size:12px">t</text><polyline points="48.0,171.7 251.3,58.3" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="251.3,171.7 454.7,58.3" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="454.7,171.7 658.0,58.3" fill="none" stroke="var(--muted)" stroke-width="1.4" stroke-dasharray="5 4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="48.0,115.0 55.6,139.4 61.7,154.9 64.8,160.4 67.8,164.3 69.3,165.6 72.4,167.0 75.5,166.7 77.0,166.0 78.5,165.1 81.6,162.2 98.3,139.6 101.4,136.4 105.9,133.0 109.0,131.6 112.0,130.9 115.1,130.6 124.2,131.0 127.3,130.8 133.4,129.2 138.0,126.5 142.6,122.6 156.3,107.9 160.8,103.9 163.9,101.9 166.9,100.4 171.5,99.2 186.8,99.2 191.3,98.0 194.4,96.4 199.0,92.6 203.6,87.3 214.2,72.1 217.3,68.3 221.8,64.2 224.9,63.0 227.9,63.3 231.0,65.2 234.0,68.8 237.1,74.1 240.2,80.9 243.2,89.1 256.9,133.3 263.0,150.3 266.1,156.9 269.1,161.9 272.2,165.2 275.2,166.9 278.3,166.9 279.8,166.3 284.4,162.8 289.0,157.2 301.1,140.2 305.7,135.5 308.8,133.3 311.8,131.8 314.9,131.0 317.9,130.6 330.1,130.9 333.2,130.4 336.2,129.4 340.8,126.8 345.4,123.0 359.1,108.4 363.7,104.3 368.2,101.3 372.8,99.6 375.9,99.1 388.1,99.4 391.1,99.0 394.2,98.2 398.8,95.7 401.8,93.1 406.4,87.9 417.1,72.8 421.6,67.2 424.7,64.6 427.7,63.1 430.8,63.1 433.8,64.8 436.9,68.1 439.9,73.1 444.5,83.5 449.1,96.7 459.7,131.7 465.8,149.1 468.9,155.9 471.9,161.2 475.0,164.8 478.0,166.7 481.1,167.0 482.6,166.5 485.7,164.7 487.2,163.3 491.8,157.9 504.0,140.8 507.0,137.4 513.1,132.7 519.2,130.8 523.8,130.6 531.4,131.0 534.5,130.8 539.0,129.6 543.6,127.2 546.7,124.9 552.8,118.9 563.4,107.4 568.0,103.5 571.1,101.6 574.1,100.2 578.7,99.2 581.8,99.0 590.9,99.4 594.0,99.1 598.5,97.8 601.6,96.0 604.6,93.6 607.7,90.4 624.4,67.8 627.5,64.9 630.5,63.3 633.6,63.0 636.6,64.4 639.7,67.4 642.8,72.2 645.8,78.5 648.9,86.3 658.0,115.0" fill="none" stroke="var(--accent2)" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><polyline points="48.0,115.0 49.2,170.6 50.0,180.7 52.1,163.9 53.7,171.7 54.1,172.0 56.1,164.3 57.8,168.3 58.2,168.3 60.2,163.0 61.8,165.5 62.2,165.3 64.3,161.2 65.9,162.9 66.3,162.7 68.3,159.2 69.6,160.3 70.4,160.2 72.0,157.3 72.8,157.3 73.6,158.0 74.4,157.8 76.1,155.2 76.5,155.0 78.1,155.7 80.1,153.0 82.2,153.3 84.2,150.8 86.2,151.0 88.3,148.6 90.3,148.7 92.3,146.4 94.4,146.4 96.4,144.2 98.4,144.1 100.5,141.9 102.5,141.8 104.5,139.7 106.6,139.5 108.2,137.7 110.6,137.2 112.3,135.4 114.7,134.9 116.7,133.0 118.4,132.9 120.4,130.9 122.4,130.6 124.5,128.7 126.5,128.3 128.5,126.4 130.6,126.0 132.2,124.4 134.6,123.8 136.7,121.9 138.7,121.5 140.7,119.6 142.8,119.2 144.4,117.6 146.8,116.9 148.4,115.3 150.9,114.7 152.5,113.1 155.0,112.4 156.6,110.8 158.6,110.4 160.6,108.5 162.7,108.1 164.7,106.2 166.3,106.0 168.8,104.0 170.8,103.6 172.8,101.7 174.9,101.3 176.9,99.4 178.9,99.1 181.0,97.1 183.0,96.8 184.6,95.1 187.1,94.6 188.7,92.8 191.1,92.3 192.8,90.5 194.8,90.3 196.8,88.2 198.9,88.1 200.9,85.9 202.9,85.8 205.0,83.6 207.0,83.6 209.0,81.3 211.1,81.4 213.1,79.0 215.1,79.2 217.2,76.7 219.2,77.0 221.2,74.3 222.9,75.0 223.3,74.8 224.9,72.2 225.7,72.0 226.5,72.7 227.3,72.7 229.0,69.8 229.8,69.7 231.0,70.8 233.0,67.3 233.4,67.1 235.1,68.8 237.1,64.7 237.5,64.5 239.1,67.0 241.2,61.7 241.6,61.7 243.2,65.7 245.2,58.0 245.6,58.3 247.3,66.1 247.7,64.9 249.3,49.3 250.1,59.4 250.5,73.6 252.1,156.4 253.0,178.6 253.4,180.7 255.0,165.1 255.4,163.9 257.0,171.7 257.4,172.0 259.5,164.3 261.1,168.3 261.5,168.3 263.5,163.0 265.2,165.5 265.6,165.3 267.6,161.2 268.8,162.6 269.6,162.7 271.7,159.2 272.9,160.3 273.7,160.2 275.3,157.3 276.1,157.3 277.0,158.0 277.8,157.8 279.4,155.2 279.8,155.0 281.4,155.7 283.5,153.0 285.5,153.3 287.5,150.8 289.6,151.0 291.6,148.6 293.6,148.7 295.7,146.4 297.7,146.4 299.7,144.2 301.8,144.1 303.8,141.9 305.8,141.8 307.9,139.7 309.9,139.5 311.5,137.7 314.0,137.2 315.6,135.4 318.0,134.9 320.1,133.0 321.7,132.9 323.7,130.9 325.8,130.6 327.8,128.7 329.8,128.3 331.4,126.7 333.9,126.0 336.3,124.0 338.0,123.8 340.0,121.9 342.0,121.5 344.1,119.6 345.7,119.4 347.7,117.6 350.2,116.9 351.8,115.3 354.2,114.7 355.8,113.1 358.3,112.4 359.9,110.8 361.9,110.4 364.0,108.5 366.0,108.1 368.0,106.2 369.7,106.0 372.1,104.0 374.1,103.6 376.2,101.7 378.2,101.3 380.2,99.4 382.3,99.1 384.3,97.1 385.9,97.0 388.0,95.1 390.4,94.6 392.0,92.8 394.5,92.3 396.5,90.3 398.1,90.3 400.2,88.2 402.2,88.1 404.2,85.9 406.3,85.8 408.3,83.6 410.3,83.6 412.4,81.3 414.4,81.4 416.4,79.0 418.5,79.2 420.5,76.7 422.5,77.0 424.6,74.3 426.2,75.0 426.6,74.8 428.2,72.2 429.0,72.0 429.9,72.7 430.7,72.7 432.3,69.8 433.1,69.7 434.3,70.8 436.4,67.3 436.8,67.1 438.4,68.8 440.4,64.7 440.8,64.5 442.5,67.0 444.5,61.7 444.9,61.7 446.5,65.7 448.6,58.0 449.0,58.3 450.6,66.1 451.0,64.9 452.6,49.3 453.0,51.4 453.9,73.6 455.5,156.4 455.9,170.6 456.7,180.7 458.3,165.1 458.7,163.9 460.4,171.7 460.8,172.0 462.8,164.3 464.4,168.3 464.8,168.3 466.9,163.0 468.5,165.5 468.9,165.3 470.9,161.2 472.6,162.9 473.0,162.7 475.0,159.2 476.2,160.3 477.0,160.2 478.7,157.3 479.5,157.3 480.3,158.0 481.1,157.8 482.7,155.2 483.1,155.0 484.8,155.7 486.8,153.0 488.8,153.3 490.9,150.8 492.9,151.0 494.9,148.6 497.0,148.7 499.0,146.4 501.0,146.4 503.1,144.2 505.1,144.1 507.1,141.9 509.2,141.8 511.2,139.7 513.2,139.5 514.9,137.7 517.3,137.2 518.9,135.4 521.4,134.9 523.0,133.2 525.0,132.9 527.1,130.9 529.1,130.6 531.1,128.7 533.2,128.3 535.2,126.4 537.2,126.0 538.8,124.4 541.3,123.8 543.3,121.9 545.4,121.5 547.4,119.6 549.4,119.2 551.0,117.6 553.5,116.9 555.1,115.3 557.6,114.7 559.2,113.1 561.6,112.4 563.2,110.8 565.3,110.4 567.3,108.5 569.3,108.1 571.4,106.2 573.8,105.6 575.4,104.0 577.5,103.6 579.5,101.7 581.5,101.3 583.6,99.4 585.6,99.1 587.6,97.1 589.3,97.0 591.3,95.1 593.7,94.6 595.4,92.8 597.8,92.3 599.4,90.5 601.5,90.3 603.5,88.2 605.5,88.1 607.6,85.9 609.6,85.8 611.6,83.6 613.7,83.6 615.7,81.3 617.7,81.4 619.8,79.0 621.8,79.2 623.8,76.7 625.9,77.0 627.9,74.3 629.5,75.0 629.9,74.8 631.6,72.2 632.4,72.0 633.2,72.7 634.0,72.7 635.6,69.8 636.4,69.7 637.7,70.8 639.7,67.3 640.1,67.1 641.7,68.8 643.8,64.7 644.2,64.5 645.8,67.0 647.8,61.7 648.2,61.7 649.9,65.7 651.9,58.0 652.3,58.3 653.9,66.1 656.0,49.3 656.8,59.4 658.0,115.0" fill="none" stroke="var(--accent)" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="125.3" y="52.7" text-anchor="middle" fill="var(--accent2)" style="font-size:12px;font-weight:600">m = 3</text><text x="296.1" y="52.7" text-anchor="middle" fill="var(--accent)" style="font-size:12px;font-weight:600">m = 50</text></svg><figcaption><strong>A periodic signal is a sum of harmonics; more harmonics, closer fit.</strong> Sawtooth x(t) = t on [0, 1), repeated (dashed); its coefficients are c<sub>0</sub> = ½ and c<sub>k</sub> = j/(2πk), so S<sub>m</sub>(t) = Σ<sub>|k|≤m</sub> c<sub>k</sub>e<sup>j2πkt</sup> = ½ − Σ<sub>k=1</sub><sup>m</sup> sin(2πkt)/(πk). With m = 3 (orange) only the trend is there; with m = 50 (teal) the fit is within 0.01 away from the jumps, but next to each jump the sum still overshoots by 8% of the jump (Gibbs), approaching 9% as m → ∞, and at the jump itself it lands on the midpoint ½.</figcaption></figure>

## 4. From series to transform: the continuous-time Fourier transform

A signal that never repeats is a periodic signal whose period has grown without bound: $T_0\to\infty$, so the harmonic spacing $\Omega_0\to0$ and the frequencies $k\Omega_0$ fill the whole real line. Informally this turns the series into an integral (notes eqs. 26–27; the notes write $X(\Omega)$, the exams $X_c(\Omega)$ or $X_a(\Omega)$):

> [!key] Continuous-time Fourier transform (CTFT)
> $$
> X_c(\Omega)=\int_{-\infty}^{\infty}x(t)\,e^{-j\Omega t}\,dt\qquad\qquad x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X_c(\Omega)\,e^{j\Omega t}\,d\Omega
> $$
> Compared with the series: the integral runs over all time; $k\Omega_0$ becomes the continuous variable $\Omega$; the factor $1/T_0$ is gone from the analysis equation, and the sum in the synthesis equation becomes an integral.

> [!derivation]- Where the $\frac{1}{2\pi}$ comes from
> Define $X_c(k\Omega_0)=T_0\,c_k=\int_{T_0}x(t)e^{-jk\Omega_0t}dt$. With $\frac{1}{T_0}=\frac{\Omega_0}{2\pi}$ the synthesis equation reads
> $$
> \begin{aligned}
> x(t)&=\sum_k\frac{X_c(k\Omega_0)}{T_0}e^{jk\Omega_0t}=\frac{1}{2\pi}\sum_kX_c(k\Omega_0)\,e^{jk\Omega_0t}\,\Omega_0\\
> &\xrightarrow{\ \Omega_0\to0\ }\ \frac{1}{2\pi}\int_{-\infty}^{\infty}X_c(\Omega)\,e^{j\Omega t}\,d\Omega ,
> \end{aligned}
> $$
> a Riemann sum with spacing $\Omega_0$ turning into an integral.

The CTFT exists under the Dirichlet conditions on every finite interval, together with absolute integrability (notes); slide 12 states the other common sufficient condition, finite energy $\int|x(t)|^2dt<\infty$. If it exists it is unique. It says how much of *every* frequency is in a signal, periodic or not, and it is your background from earlier courses: %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #1 practises it. The one pair worth having next to the DTFT is the pulse:

$$
\begin{aligned}
u(t)-u(t-T)\ \longleftrightarrow\ X_c(\Omega)&=\int_0^Te^{-j\Omega t}\,dt=\frac{1-e^{-j\Omega T}}{j\Omega}\\
&=e^{-j\Omega T/2}\,\frac{2\sin(\Omega T/2)}{\Omega},\qquad X_c(0)=T .
\end{aligned}
$$

Keep it in mind for §6: the discrete-time pulse has almost the same transform, but with $\sin(\omega/2)$ in the denominator, which makes it repeat every $2\pi$.

## 5. The discrete-time Fourier series

Harmonics in discrete time are $e^{j\frac{2\pi}{N_0}kn}$, and only $N_0$ of them are distinct: $k=N_0$ gives $e^{j2\pi n}=1$, the same as $k=0$ (notes eqs. 29–31). So a sequence with period $N_0$ needs only $k=0,\dots,N_0-1$:

> [!key] Discrete-time Fourier series (DTFS) of a sequence with period $N_0$ (notes eqs. 32–33)
> $$
> x[n]=\sum_{k=0}^{N_0-1}c_k\,e^{j\frac{2\pi k}{N_0}n}\qquad\qquad c_k=\frac{1}{N_0}\sum_{n=0}^{N_0-1}x[n]\,e^{-j\frac{2\pi k}{N_0}n}
> $$
> Both sums are finite, so the DTFS exists for every periodic sequence, the synthesis recovers $x$ exactly, and the coefficients are unique. They are themselves $N_0$-periodic: $c_{k+N_0}=c_k$. (The analysis equation follows from the discrete orthogonality of §2, exactly as in §3.)

> [!example] Exercise 1 of the notes: a periodic pulse
> One period: $x[n]=1$ for $0\le n<L$ and $0$ for $L\le n<N_0$. The analysis sum is a finite geometric series; factoring out half-angle exponentials and using Euler,
> $$
> \begin{aligned}
> c_k&=\frac{1}{N_0}\sum_{n=0}^{L-1}e^{-j\frac{2\pi k}{N_0}n}=\frac{1}{N_0}\,\frac{1-e^{-j2\pi kL/N_0}}{1-e^{-j2\pi k/N_0}}\\
> &=\frac{1}{N_0}\,e^{-j\frac{\pi k}{N_0}(L-1)}\,\frac{\sin(\pi kL/N_0)}{\sin(\pi k/N_0)},\qquad c_0=\frac{L}{N_0}.
> \end{aligned}
> $$
> For $N_0=12$, $L=4$: $\lvert c_k\rvert=0.333,\ 0.279,\ 0.144,\ 0,\ 0.083,\ 0.075,\ 0$ for $k=0,\dots,6$, mirrored for $k=7,\dots,11$.

> [!trap] The phase is not always $-\frac{\pi k}{N_0}(L-1)$
> The notes' eq. 40 gives $\angle c_k=-\frac{\pi k}{N_0}(L-1)$. That is the angle of the exponential factor only. The ratio $\frac{\sin(\pi kL/N_0)}{\sin(\pi k/N_0)}$ is real but can be negative, and wherever it is, the phase gains $\pm\pi$. For $N_0=12$, $L=4$: $c_4=\frac{1}{12}\,e^{-j\pi}\,(-1)=+\frac{1}{12}$, so $\angle c_4=0$, not $-\pi$ (the notes' own Fig. 2(e) plots $0$), and $\angle c_5=-\frac{5\pi}{4}+\pi=-\frac{\pi}{4}$. Where the ratio is zero ($k=3,6,9$) the phase is undefined. Magnitudes are never negative; [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] makes this the rule for every phase plot.

## 6. The discrete-time Fourier transform

Now let the period of a sequence grow without bound, $N_0\to\infty$: the harmonic frequencies $\frac{2\pi k}{N_0}$ crowd into a continuum $\omega$, and the DTFS becomes (notes eqs. 41–42):

> [!key] The DTFT and its inverse
> $$
> X_d(\omega)=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\omega n}\qquad\qquad x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X_d(\omega)\,e^{j\omega n}\,d\omega
> $$
> $\omega$ is in radians per sample. $X_d(\omega)$ is complex: $\lvert X_d(\omega)\rvert$ is the **magnitude spectrum**, $\angle X_d(\omega)$ the **phase spectrum**. The notes integrate over "$2\pi$": any interval of length $2\pi$ gives the same $x[n]$. (Manolakis and Ingle write $X(e^{j\omega})$ for $X_d(\omega)$.)

Read it with [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] in mind. $X_d(\omega)=\langle x,e^{j\omega n}\rangle$ is the score of $x$ against the template of frequency $\omega$: how much of that frequency the signal contains. The inverse rebuilds $x$ from all the frequencies in one period, each weighted by $X_d(\omega)\,\frac{d\omega}{2\pi}$.

> [!derivation]- Why the inverse formula returns $x[n]$
> Substitute the definition and swap sum and integral (fine for absolutely summable $x$):
> $$
> \frac{1}{2\pi}\int_{-\pi}^{\pi}\Big(\sum_m x[m]e^{-j\omega m}\Big)e^{j\omega n}\,d\omega=\sum_m x[m]\,\underbrace{\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{j\omega(n-m)}\,d\omega}_{=\,\delta[n-m]}=x[n].
> $$
> The underbraced integral is orthogonality once more, now with $\omega$ as the variable: it is $1$ for $m=n$ and $\frac{\sin(\pi(n-m))}{\pi(n-m)}=0$ for every other integer $m$.

### 6.1 Every DTFT is 2π-periodic

$$
X_d(\omega+2\pi)=\sum_n x[n]\,e^{-j\omega n}\,e^{-j2\pi n}=X_d(\omega),
$$

because the exponentials the DTFT is built from repeat every $2\pi$ (§1). So one period, conventionally $[-\pi,\pi]$, says everything; $X_d(-\pi)=X_d(\pi)$; and a formula given "for $|\omega|\le\pi$" defines $X_d$ everywhere by periodic extension. The notes contrast this with the CTFT, which is not periodic.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 370" width="680" height="370" role="img" aria-label="periodic DTFT magnitude of a 4-sample pulse with DTFS samples, and periodic impulses for a cosine" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="353.0" y="22.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(a) |X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω)| for x[n] = u[n] − u[n−4], with 12·|c<tspan baseline-shift="sub" style="font-size:75%">k</tspan>| of its period-12 version</text><rect x="251.3" y="28.0" width="203.3" height="120.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="48.0" y1="96.9" x2="658.0" y2="96.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="45.9" x2="658.0" y2="45.9" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="48.0" y1="148.0" x2="658.0" y2="148.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="353.0" y1="28.0" x2="353.0" y2="148.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="145.0" x2="48.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="48.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="149.7" y1="145.0" x2="149.7" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="149.7" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="251.3" y1="145.0" x2="251.3" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="251.3" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="353.0" y1="145.0" x2="353.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="353.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="454.7" y1="145.0" x2="454.7" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="454.7" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="556.3" y1="145.0" x2="556.3" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="556.3" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="658.0" y1="145.0" x2="658.0" y2="151.0" stroke="currentColor" stroke-width="1"/><text x="658.0" y="162.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><line x1="350.0" y1="148.0" x2="356.0" y2="148.0" stroke="currentColor" stroke-width="1"/><text x="44.0" y="152.0" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="350.0" y1="96.9" x2="356.0" y2="96.9" stroke="currentColor" stroke-width="1"/><text x="44.0" y="100.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">2</text><line x1="350.0" y1="45.9" x2="356.0" y2="45.9" stroke="currentColor" stroke-width="1"/><text x="44.0" y="49.9" text-anchor="end" fill="var(--muted)" style="font-size:11px">4</text><text x="658.0" y="142.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="48.0,148.0 55.6,136.3 62.2,127.8 67.8,122.8 71.9,120.7 74.4,120.2 76.0,120.2 79.5,121.1 82.1,122.6 85.6,125.7 88.7,129.4 91.2,133.2 94.8,139.5 98.8,148.0 106.5,129.3 123.2,83.8 129.8,68.3 135.4,57.8 140.5,50.9 144.6,47.4 146.6,46.4 148.7,45.9 152.7,46.4 156.8,48.9 161.9,54.7 167.0,63.2 174.6,80.0 194.4,133.3 200.5,148.0 207.1,134.9 211.7,128.1 215.2,124.2 217.8,122.2 220.8,120.7 223.4,120.2 224.9,120.2 229.0,121.3 232.5,123.5 235.1,125.7 240.7,132.1 251.3,148.0 262.0,132.1 265.6,127.8 269.6,123.9 275.2,120.7 277.8,120.2 281.8,120.7 284.9,122.2 287.4,124.2 292.0,129.4 297.1,137.6 302.2,148.0 308.3,133.3 325.0,87.8 330.1,75.1 334.2,66.2 338.8,57.8 343.3,51.5 347.9,47.4 352.0,45.9 356.1,46.4 360.1,48.9 362.2,50.9 365.2,54.7 370.3,63.2 374.9,72.8 380.5,86.4 397.7,133.3 403.8,148.0 410.4,134.9 415.0,128.1 418.6,124.2 421.1,122.2 424.2,120.7 426.7,120.2 429.8,120.5 432.3,121.3 435.9,123.5 438.4,125.7 444.0,132.1 454.7,148.0 465.3,132.1 470.9,125.7 474.5,122.8 478.6,120.7 481.1,120.2 485.2,120.7 488.2,122.2 490.8,124.2 495.3,129.4 500.4,137.6 505.5,148.0 514.7,125.2 529.9,83.8 537.5,66.2 543.1,56.2 547.2,50.9 551.2,47.4 555.3,45.9 557.4,45.9 559.9,46.6 562.4,48.1 565.5,50.9 570.6,57.8 575.7,67.3 582.8,83.8 599.5,129.3 607.2,148.0 611.2,139.5 617.3,129.4 620.4,125.7 623.9,122.6 627.5,120.7 630.0,120.2 631.6,120.2 635.6,121.3 639.2,123.5 641.7,125.7 648.9,134.2 658.0,148.0" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><circle cx="48.0" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="64.9" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="81.9" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="98.8" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="115.8" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="132.7" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="149.7" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="166.6" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="183.6" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="200.5" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="217.4" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="234.4" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="251.3" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="268.3" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="285.2" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="302.2" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="319.1" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="336.1" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="353.0" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="369.9" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="386.9" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="403.8" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="420.8" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="437.7" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="454.7" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="471.6" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="488.6" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="505.5" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="522.4" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="539.4" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="556.3" cy="45.9" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="573.3" cy="62.6" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="590.2" cy="103.8" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="607.2" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="624.1" cy="122.5" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="641.1" cy="125.1" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><circle cx="658.0" cy="148.0" r="2.8" fill="var(--hi)" stroke="var(--hi)" stroke-width="1.5"/><text x="383.0" y="49.9" text-anchor="start" fill="var(--accent)" style="font-size:11px">one period</text><text x="353.0" y="208.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">(b) X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) for cos(πn/3): impulses of area π at ±π/3, repeated every 2π</text><rect x="251.3" y="214.0" width="203.3" height="120.0" fill="var(--accent)" fill-opacity="0.1" stroke="none"/><line x1="48.0" y1="334.0" x2="658.0" y2="334.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="353.0" y1="214.0" x2="353.0" y2="334.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="48.0" y1="331.0" x2="48.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="48.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−3π</text><line x1="149.7" y1="331.0" x2="149.7" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="149.7" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−2π</text><line x1="251.3" y1="331.0" x2="251.3" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="251.3" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="353.0" y1="331.0" x2="353.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="353.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="454.7" y1="331.0" x2="454.7" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="454.7" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="556.3" y1="331.0" x2="556.3" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="556.3" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">2π</text><line x1="658.0" y1="331.0" x2="658.0" y2="337.0" stroke="currentColor" stroke-width="1"/><text x="658.0" y="348.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">3π</text><text x="658.0" y="328.0" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><line x1="115.8" y1="334.0" x2="115.8" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M110.8,260.3 L115.8,252.3 L120.8,260.3 Z" fill="var(--muted)"/><line x1="183.6" y1="334.0" x2="183.6" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M178.6,260.3 L183.6,252.3 L188.6,260.3 Z" fill="var(--muted)"/><line x1="319.1" y1="334.0" x2="319.1" y2="258.3" stroke="var(--hi)" stroke-width="2"/><path d="M314.1,260.3 L319.1,252.3 L324.1,260.3 Z" fill="var(--hi)"/><text x="325.1" y="256.3" text-anchor="start" fill="var(--hi)" style="font-size:11px">π</text><line x1="386.9" y1="334.0" x2="386.9" y2="258.3" stroke="var(--hi)" stroke-width="2"/><path d="M381.9,260.3 L386.9,252.3 L391.9,260.3 Z" fill="var(--hi)"/><text x="392.9" y="256.3" text-anchor="start" fill="var(--hi)" style="font-size:11px">π</text><line x1="522.4" y1="334.0" x2="522.4" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M517.4,260.3 L522.4,252.3 L527.4,260.3 Z" fill="var(--muted)"/><line x1="590.2" y1="334.0" x2="590.2" y2="258.3" stroke="var(--muted)" stroke-width="2"/><path d="M585.2,260.3 L590.2,252.3 L595.2,260.3 Z" fill="var(--muted)"/><text x="386.9" y="360.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px">π/3</text><text x="319.1" y="360.0" text-anchor="middle" fill="var(--muted)" style="font-size:10px">−π/3</text></svg><figcaption><strong>Every DTFT repeats every 2π, so one period (shaded) says everything.</strong> (a) The four-sample pulse of Exercise 2 has |X<sub>d</sub>(ω)| = |sin(2ω)/sin(ω/2)|: height 4 at ω = 0, zeros at ±π/2 and π, and the same shape around every multiple of 2π. The dots are 12·|c<sub>k</sub>| at ω<sub>k</sub> = 2πk/12 for the period-12 version of the pulse (Exercise 1): the DTFS coefficients are samples of the DTFT, divided by N<sub>0</sub> = 12. (b) cos(πn/3) is not absolutely summable; its DTFT is a pair of Dirac impulses π[δ(ω − π/3) + δ(ω + π/3)] on [−π, π], copied to every period (grey).</figcaption></figure>

> [!question] SP2023 MT2 #3: for an arbitrary sequence, $X_d(\omega)=j\omega$ for $0\le\omega\le\pi$. Then for $2\pi\le\omega\le3\pi$:
> (a) $X_d(\omega)=\omega$ $\quad$ (b) $X_d(\omega)=-\omega$ $\quad$ (c) $X_d(\omega)=j\omega$ $\quad$ (d) $X_d(\omega)=-j\omega$ $\quad$ (e) none of the above

> [!success]- Answer: (e)
> Periodicity alone: $X_d(\omega)=X_d(\omega-2\pi)=j(\omega-2\pi)$ there, which is none of the four. Problem #2 of the same exam asks for $-\pi\le\omega\le0$ when $x$ is *real*; that needs the conjugate symmetry $X_d(-\omega)=X_d^*(\omega)$ of [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (answer: $j\omega$).

### 6.2 When does the DTFT exist?

> [!key] Absolute summability is enough (notes eq. 43)
> If $\sum_n|x[n]|<\infty$, the sum converges for every $\omega$, and since $|e^{-j\omega n}|=1$,
> $$
> |X_d(\omega)|\le\sum_{n=-\infty}^{\infty}|x[n]|<\infty .
> $$
> $X_d$ is then a bounded, continuous function of $\omega$, and it is **unique**: two different sequences never share a DTFT. The condition is sufficient, not necessary.

Three kinds of sequences:

1. **Finite-length**: always absolutely summable. $X_d(\omega)$ is a finite sum of powers of $e^{-j\omega}$ (§6.3).
2. **Decaying exponentials**, $a^nu[n]$ with $|a|<1$: a geometric series, $X_d(\omega)=\sum_{n\ge0}(ae^{-j\omega})^n=\dfrac{1}{1-ae^{-j\omega}}$.
3. **Not absolutely summable.** Growing sequences such as $2^nu[n]$ have no DTFT at all. Sequences that neither grow nor decay, such as $e^{j\omega_0n}$, $\cos(\omega_0n)$ and $u[n]$, have no DTFT as an ordinary function but get one with impulses (§7, and [[3-fourier-analysis/14-dtft-properties|Lecture 14]] for $u[n]$). In between, $\frac{\sin(\omega_cn)}{\pi n}$ decays only like $1/n$: not absolutely summable, but of finite energy, and its DTFT is a rectangle (§8).

The test is the same sum that decided BIBO stability in [[2-z-transform/11-bibo-stability-and-causality|Lecture 11]]: on the unit circle $|x[n]z^{-n}|=|x[n]|$, so $x$ is absolutely summable exactly when the ROC of $X(z)$ contains $|z|=1$, and then $X_d(\omega)=X(z)\big|_{z=e^{j\omega}}$ — the bridge [[3-fourier-analysis/14-dtft-properties|Lecture 14]] builds on (see [[concepts/dtft|DTFT]]). For an impulse response this reads: the sum defining the frequency response converges absolutely $\iff$ the system is stable (an unstable system can still be given a frequency response with impulses, as $h[n]=(-1)^nu[n]$ is in [[exams/midterm-2/past-exams/fall-2021|FA2021 MT2]] #2(c)).

> [!trap] A z-transform formula is a DTFT only if the ROC contains the unit circle
> [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(a): "$2^nu[n]\leftrightarrow\frac{1}{1-2z^{-1}}$, $|z|>2$, therefore $X_d(\omega)=\frac{1}{1-2e^{-j\omega}}$" is **False**: the ROC misses the unit circle, $\sum|x[n]|=\infty$, and there is no DTFT. The formula still returns numbers on the unit circle; they mean nothing. "Always" versions of the claim are False too ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(a), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #1(d)).

### 6.3 Worked examples

> [!example] Exercise 2 of the notes: the pulse $x[n]=u[n]-u[n-L]$
> $$
> \begin{aligned}
> X_d(\omega)&=\sum_{n=0}^{L-1}e^{-j\omega n}=\frac{1-e^{-j\omega L}}{1-e^{-j\omega}}
> =\frac{e^{-j\omega L/2}}{e^{-j\omega/2}}\cdot\frac{e^{j\omega L/2}-e^{-j\omega L/2}}{e^{j\omega/2}-e^{-j\omega/2}}\\
> &=e^{-j\omega(L-1)/2}\,\frac{\sin(\omega L/2)}{\sin(\omega/2)},\qquad X_d(0)=L .
> \end{aligned}
> $$
> The middle step is the "popular trick" of the notes: factor the half-angle exponential out of the numerator and out of the denominator so that each bracket becomes $2j\sin(\cdot)$. (The notes' eq. 47 prints the numerator as $e^{j\omega L/2}-e^{j\omega L/2}$; the second exponent needs a minus sign.) The magnitude, $|\sin(\omega L/2)/\sin(\omega/2)|$, is panel (a) of the figure above for $L=4$: height $4$ at $\omega=0$, zeros at $\pm\frac{\pi}{2}$ and $\pi$.
>
> Compare with Exercise 1: at $\omega_k=\frac{2\pi k}{N_0}$ this is exactly $N_0\,c_k$ (notes eq. 49). **The DTFS coefficients of the periodic pulse are samples of the DTFT of one period, divided by $N_0$**: the dots in panel (a).

> [!example] Slide 15 (annotated): $x[n]=\{\underset{\uparrow}{1},0,1,0,1\}$
> $x[n]=\delta[n]+\delta[n-2]+\delta[n-4]$, so
> $$
> X_d(\omega)=1+e^{-j2\omega}+e^{-j4\omega}=e^{-j2\omega}\big(e^{j2\omega}+1+e^{-j2\omega}\big)=e^{-j2\omega}\big(1+2\cos(2\omega)\big).
> $$
> Values: $X_d(0)=3$, $X_d(\frac{\pi}{2})=e^{-j\pi}(1-2)=1$, $X_d(\pi)=3$. The same samples centred on $n=0$, $\delta[n+2]+\delta[n]+\delta[n-2]$, give $1+2\cos(2\omega)$ with no exponential factor: real, because the sequence is symmetric about $n=0$. That centred sequence is the impulse response of [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3 ($H_d(0)=3$, $H_d(\frac{\pi}{2})=-1$, $H_d(\pi)=3$), and the factor $e^{-j2\omega}$ is the shift by two samples (Lecture 14's time-shift property).

> [!recipe] DTFT of a finite sequence in four steps
> 1. Read it off: one term $x[k]\,e^{-j\omega k}$ per nonzero sample, with the sample's index in the exponent.
> 2. Factor out $e^{-j\omega M}$, where $M$ is the midpoint of the nonzero samples, so that the remaining exponents pair up as $\pm$.
> 3. Pair the terms with Euler, $e^{j\theta}+e^{-j\theta}=2\cos\theta$ and $e^{j\theta}-e^{-j\theta}=2j\sin\theta$; for a run of equal samples, sum the geometric series and use the half-angle trick.
> 4. Check $X_d(0)=\sum_nx[n]$ and $X_d(\pi)=\sum_n(-1)^nx[n]$ against your closed form.

> [!tip] Appending zeros changes nothing
> Zero-padding a finite sequence (appending zeros) adds only zero terms to $\sum_nx[n]e^{-j\omega n}$, so its DTFT is unchanged. Exams ask this often, usually next to the DFT of a later lecture (which does change: it samples the same DTFT at more frequencies). True: [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(f), [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #1(c), [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(d). False: "zero padding can change its DTFT" ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(a)) and "$X_d(\omega)=Y_d(3\omega)$ after padding to length $3N$" ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(d)).

> [!question] Slide 16: $X_d(\omega)=2j\sin\omega$. Which sequence is $x[n]$?
> (a) $\{\underset{\uparrow}{1},0,-1\}$ $\quad$ (b) $\{1,\underset{\uparrow}{0},-1\}$ $\quad$ (c) $\{\underset{\uparrow}{2},0,-2\}$ $\quad$ (d) $\{2,\underset{\uparrow}{0},-2\}$

> [!success]- Answer: (b) (annotated slide 16)
> $2j\sin\omega=e^{j\omega}-e^{-j\omega}$: the coefficient of $e^{-j\omega n}$ is $+1$ at $n=-1$ and $-1$ at $n=1$. The others: (a) $1-e^{-j2\omega}$ (the same pair delayed by one sample, $2j\,e^{-j\omega}\sin\omega$), (c) $2-2e^{-j2\omega}$, (d) $2e^{j\omega}-2e^{-j\omega}=4j\sin\omega$. (The ink on the slide writes "$2-e^{-j2\omega}$" for (c); the factor 2 is missing.)

> [!question] Practice: SP2021 MT2 #3 and HW5 #1(a), (b)
> (i) The DTFT of $x[n]=3\delta[n+1]-3\delta[n-7]$ can be written $Ae^{-jB\omega}\sin(C\omega)$; find $A$, $B$, $C$. $\quad$ (ii) $x[n]=\{1,0,\underset{\uparrow}{0},0,-1\}$. $\quad$ (iii) $x[n]=u[n]-u[n-4]$.

> [!success]- Answers (checked numerically on a grid of 1201 frequencies)
> (i) The midpoint of $n=-1$ and $n=7$ is $3$: $X_d(\omega)=3e^{j\omega}-3e^{-j7\omega}=3e^{-j3\omega}\big(e^{j4\omega}-e^{-j4\omega}\big)=6j\,e^{-j3\omega}\sin(4\omega)$, so $A=6j$, $B=3$, $C=4$ ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #3).
> (ii) $x[n]=\delta[n+2]-\delta[n-2]$: $X_d(\omega)=e^{j2\omega}-e^{-j2\omega}=2j\sin(2\omega)$.
> (iii) Exercise 2 with $L=4$: $X_d(\omega)=e^{-j3\omega/2}\dfrac{\sin(2\omega)}{\sin(\omega/2)}=2e^{-j3\omega/2}\big(\cos(\tfrac{\omega}{2})+\cos(\tfrac{3\omega}{2})\big)$.

The same computations in Python, with the course notebook's `DTFT(x, n0, w)` written in vectorized form:

```python
import numpy as np

def dtft(x, n0, w):
    """X_d(w) = sum_n x[n] e^{-jwn} for a finite sequence whose first entry sits at n = n0
    (the arguments of DTFT(x, n0, w) in the course notebook demo_DTFT)."""
    n = n0 + np.arange(len(x))
    return np.exp(-1j * np.outer(w, n)) @ np.asarray(x, dtype=complex)

x = [1, 0, 1, 0, 1]                                    # slide 15, first sample at n = 0
w = np.linspace(-np.pi, np.pi, 1001)
X = dtft(x, 0, w)
print(np.allclose(X, np.exp(-2j*w) * (1 + 2*np.cos(2*w))))    # the slide's closed form
print(np.allclose(dtft(x, 0, w + 2*np.pi), X))                # 2*pi-periodic
print(dtft(x, 0, np.array([0, np.pi/2, np.pi])).real.round(12))   # X_d(0), X_d(pi/2), X_d(pi)
print(np.abs(X).max(), "<=", np.sum(np.abs(x)))               # |X_d(w)| <= sum |x[n]|
```

```text
True
True
[3. 1. 3.]
3.0 <= 3
```

### 6.4 Three values you can read without the closed form

> [!key] $X_d(0)$, $X_d(\pi)$ and the area under one period
> $$
> X_d(0)=\sum_n x[n],\qquad X_d(\pi)=\sum_n(-1)^n\,x[n],\qquad \int_{-\pi}^{\pi}X_d(\omega)\,d\omega=2\pi\,x[0].
> $$
> The first two set $\omega=0$ and $\omega=\pi$ ($e^{-j\pi n}=(-1)^n$) in the definition; the third is the inverse DTFT at $n=0$. (The energy $\int_{-\pi}^{\pi}|X_d|^2d\omega=2\pi\sum|x[n]|^2$ is Parseval's relation, [[3-fourier-analysis/14-dtft-properties|Lecture 14]].)

> [!question] Three exam items
> (i) [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #2: $x[n]=u[n+2]-u[n-3]$; find $X_d(0)$ and $X_d(\pi)$.
> (ii) [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #3: $x[n]=\delta[n+3]-3\delta[n+2]+5\delta[n+1]-7\delta[n]+5\delta[n-1]-3\delta[n-2]+\delta[n-3]$; find $X_d(0)$, $X_d(\pi)$ and $\int_{-\pi}^{\pi}X_d(\omega)\,d\omega$.
> (iii) [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #9: $\{x[n]\}_{n=-1}^{2}=\{1-j,\ 1,\ -1-j,\ 2j\}$; find $X_d(0)$ and $X_d(\frac{\pi}{2})$.

> [!success]- Answers (checked against the keys and numerically)
> (i) Five ones at $n=-2,\dots,2$: $X_d(0)=5$, $X_d(\pi)=1-1+1-1+1=1$.
> (ii) $X_d(0)=1-3+5-7+5-3+1=-1$. Multiplying by $(-1)^n$ flips the signs at odd $n$, which turns every sample negative: $X_d(\pi)=-(1+3+5+7+5+3+1)=-25$. And $\int X_d\,d\omega=2\pi x[0]=-14\pi$.
> (iii) $X_d(0)=(1-j)+1+(-1-j)+2j=1$. At $\omega=\frac{\pi}{2}$, $e^{-j\pi n/2}=(-j)^n$: $X_d(\frac{\pi}{2})=j(1-j)+1+(-j)(-1-j)+(-1)(2j)=(1+j)+1+(-1+j)-2j=1$.

## 7. Signals that are not absolutely summable: impulses in frequency

$e^{j\omega_0n}$ (for all $n$) has $\sum_n|e^{j\omega_0n}|=\infty$, and the DTFT sum does not converge. Yet a single frequency should have a spectrum concentrated at that frequency, and the inverse DTFT confirms it if we allow a **Dirac impulse** $\delta(\omega)$ (zero width, unit area; the sifting property $\int f(\omega)\delta(\omega-\omega_0)\,d\omega=f(\omega_0)$). For $\omega_0$ inside $(-\pi,\pi)$:

$$
\frac{1}{2\pi}\int_{-\pi}^{\pi}2\pi\,\delta(\omega-\omega_0)\,e^{j\omega n}\,d\omega=e^{j\omega_0n}.
$$

> [!key] DTFTs with impulses (one period shown; each repeats every $2\pi$)
> $$
> \begin{aligned}
> e^{j\omega_0n}&\ \longleftrightarrow\ 2\pi\,\delta(\omega-\omega_0)\\
> \cos(\omega_0n)&\ \longleftrightarrow\ \pi\big[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)\big]\\
> \sin(\omega_0n)&\ \longleftrightarrow\ -j\pi\big[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\big]\\
> 1\ (\text{all } n)&\ \longleftrightarrow\ 2\pi\,\delta(\omega)
> \end{aligned}
> $$
> Over all $\omega$: $e^{j\omega_0n}\leftrightarrow2\pi\sum_k\delta(\omega-\omega_0-2\pi k)$. The Dirac $\delta(\omega)$, with a continuous argument in parentheses, is not the Kronecker $\delta[n]$. Lecture 14 derives these formally and adds $u[n]\leftrightarrow\frac{1}{1-e^{-j\omega}}+\pi\delta(\omega)$; the table is on [[concepts/dtft-pairs|DTFT pairs]].

The pair mirrors $\delta[n]\leftrightarrow1$: a spike in time is flat in frequency, and a signal that is "flat" in time (one frequency, forever) is a spike in frequency. Panel (b) of the periodicity figure shows the cosine's two impulses and their copies.

> [!question] HW5 #1(c) and SP2023 MT2 #4
> (i) Find the DTFT of $x[n]=\cos(\frac{\pi}{3}n+\frac{\pi}{4})$, using $e^{j\omega_0n}\leftrightarrow2\pi\delta(\omega-\omega_0)$. $\quad$ (ii) Find the inverse DTFT of $X_d(\omega)=5e^{j\pi\omega}\delta(\omega-\omega_0)$, where $\omega_0$ is a constant.

> [!success]- Answers
> (i) Euler: $x[n]=\frac12e^{j\pi/4}e^{j\pi n/3}+\frac12e^{-j\pi/4}e^{-j\pi n/3}$, so
> $$
> X_d(\omega)=\pi e^{j\pi/4}\,\delta(\omega-\tfrac{\pi}{3})+\pi e^{-j\pi/4}\,\delta(\omega+\tfrac{\pi}{3}),\qquad -\pi\le\omega<\pi,
> $$
> repeated every $2\pi$. The cosine's phase rides on the (complex) impulse areas.
> (ii) Sifting: $x[n]=\frac{1}{2\pi}\int_{-\pi}^{\pi}5e^{j\pi\omega}\delta(\omega-\omega_0)e^{j\omega n}d\omega=\frac{5}{2\pi}e^{j\omega_0(\pi+n)}$, for $\omega_0$ inside the integration period ([[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #4). The factor $e^{j\pi\omega}$ is just a function of $\omega$ evaluated at $\omega_0$; it is *not* a time shift, since a shift by $\pi$ samples does not exist.

> [!trap] Two things that are not what they look like
> - **A finite piece of a cosine is not a pair of impulses.** $x[n]=\cos(\frac{\pi}{32}n)$ for $n=0,\dots,15$ only is finite-length, so its DTFT is an ordinary bounded function (here a single broad bump of height $10.7$ centred at $\omega=0$: sixteen samples are too few to separate $\pm\frac{\pi}{32}$), not $\pi[\delta(\omega-\frac{\pi}{32})+\delta(\omega+\frac{\pi}{32})]$ ([[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(c), False). Impulses need the cosine for all $n$.
> - **$e^{-j\omega/2}$ is not a half-sample delay.** It is a perfectly good DTFT on $[-\pi,\pi]$, but $\delta[n-\frac12]$ is not a sequence ([[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(b), False). Its inverse DTFT is $x[n]=\frac{\sin(\pi(n-\frac12))}{\pi(n-\frac12)}$, for instance $\frac{2}{\pi}=0.637$ at both $n=0$ and $n=1$. %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #3(b) asks the same about $e^{-j3.5\omega}$.

## 8. Inverse DTFT of a sketched spectrum: rectangles and sincs

The inverse DTFT of a piecewise-constant spectrum is one integral of an exponential per piece. The basic piece is the ideal low-pass shape:

> [!key] Rectangle in frequency ⟷ sinc in time
> $$
> \begin{gathered}
> X_d(\omega)=\begin{cases}1,&|\omega|\le\omega_c\\0,&\omega_c<|\omega|\le\pi\end{cases}\\[6pt]
> \Longrightarrow\quad x[n]=\frac{1}{2\pi}\int_{-\omega_c}^{\omega_c}e^{j\omega n}\,d\omega=\frac{e^{j\omega_cn}-e^{-j\omega_cn}}{2\pi jn}=\frac{\sin(\omega_cn)}{\pi n},
> \end{gathered}
> $$
> with $x[0]=\frac{\omega_c}{\pi}$ (the area of one period divided by $2\pi$). In the course's notation $\mathrm{sinc}(\theta)=\frac{\sin\theta}{\theta}$, this is $x[n]=\frac{\omega_c}{\pi}\,\mathrm{sinc}(\omega_cn)$. Careful in Python: `np.sinc(v)` is $\frac{\sin(\pi v)}{\pi v}$.

<figure class="ece-fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250" width="680" height="250" role="img" aria-label="rectangular spectrum and its sinc sequence" style="font-family:'Source Sans 3','Source Sans Pro',system-ui,sans-serif;font-size:13px"><text x="175.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">X<tspan baseline-shift="sub" style="font-size:75%">d</tspan>(ω) = 1 for |ω| ≤ π/4 (one period)</text><line x1="40.0" y1="69.2" x2="310.0" y2="69.2" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="40.0" y1="186.4" x2="310.0" y2="186.4" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="175.0" y1="34.0" x2="175.0" y2="204.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="40.0" y1="183.4" x2="40.0" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="40.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π</text><line x1="141.2" y1="183.4" x2="141.2" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="141.2" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−π/4</text><line x1="208.8" y1="183.4" x2="208.8" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="208.8" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π/4</text><line x1="310.0" y1="183.4" x2="310.0" y2="189.4" stroke="currentColor" stroke-width="1"/><text x="310.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">π</text><line x1="172.0" y1="186.4" x2="178.0" y2="186.4" stroke="currentColor" stroke-width="1"/><text x="36.0" y="190.4" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="172.0" y1="69.2" x2="178.0" y2="69.2" stroke="currentColor" stroke-width="1"/><text x="36.0" y="73.2" text-anchor="end" fill="var(--muted)" style="font-size:11px">1</text><text x="310.0" y="180.4" text-anchor="end" fill="var(--muted)" style="font-size:12px">ω</text><polyline points="40.0,186.4 141.2,186.4 141.2,69.2 208.8,69.2 208.8,186.4 310.0,186.4" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" opacity="1.0"/><text x="515.0" y="28.0" text-anchor="middle" fill="currentColor" style="font-size:13px;font-weight:600">x[n] = sin(πn/4)/(πn)</text><line x1="370.0" y1="55.8" x2="660.0" y2="55.8" stroke="var(--muted)" stroke-width="0.6" stroke-dasharray="3 3" opacity="0.6"/><line x1="370.0" y1="164.8" x2="660.0" y2="164.8" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="515.0" y1="34.0" x2="515.0" y2="204.0" stroke="currentColor" stroke-width="1" opacity="0.75"/><line x1="376.9" y1="161.8" x2="376.9" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="376.9" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−16</text><line x1="446.0" y1="161.8" x2="446.0" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="446.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−8</text><line x1="480.5" y1="161.8" x2="480.5" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="480.5" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">−4</text><line x1="515.0" y1="161.8" x2="515.0" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="515.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">0</text><line x1="549.5" y1="161.8" x2="549.5" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="549.5" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">4</text><line x1="584.0" y1="161.8" x2="584.0" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="584.0" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">8</text><line x1="653.1" y1="161.8" x2="653.1" y2="167.8" stroke="currentColor" stroke-width="1"/><text x="653.1" y="218.0" text-anchor="middle" fill="var(--muted)" style="font-size:11px">16</text><line x1="512.0" y1="164.8" x2="518.0" y2="164.8" stroke="currentColor" stroke-width="1"/><text x="366.0" y="168.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">0</text><line x1="512.0" y1="55.8" x2="518.0" y2="55.8" stroke="currentColor" stroke-width="1"/><text x="366.0" y="59.8" text-anchor="end" fill="var(--muted)" style="font-size:11px">¼</text><text x="660.0" y="158.8" text-anchor="end" fill="var(--muted)" style="font-size:12px">n</text><line x1="376.9" y1="164.8" x2="376.9" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="376.9" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="385.5" y1="164.8" x2="385.5" y2="171.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="385.5" cy="171.3" r="2.4" fill="var(--accent)"/><line x1="394.2" y1="164.8" x2="394.2" y2="174.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="394.2" cy="174.7" r="2.4" fill="var(--accent)"/><line x1="402.8" y1="164.8" x2="402.8" y2="172.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="402.8" cy="172.3" r="2.4" fill="var(--accent)"/><line x1="411.4" y1="164.8" x2="411.4" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="411.4" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="420.1" y1="164.8" x2="420.1" y2="155.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="420.1" cy="155.9" r="2.4" fill="var(--accent)"/><line x1="428.7" y1="164.8" x2="428.7" y2="150.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="428.7" cy="150.9" r="2.4" fill="var(--accent)"/><line x1="437.3" y1="164.8" x2="437.3" y2="153.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="437.3" cy="153.9" r="2.4" fill="var(--accent)"/><line x1="446.0" y1="164.8" x2="446.0" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="446.0" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="454.6" y1="164.8" x2="454.6" y2="178.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="454.6" cy="178.8" r="2.4" fill="var(--accent)"/><line x1="463.2" y1="164.8" x2="463.2" y2="187.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="463.2" cy="187.9" r="2.4" fill="var(--accent)"/><line x1="471.8" y1="164.8" x2="471.8" y2="184.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="471.8" cy="184.4" r="2.4" fill="var(--accent)"/><line x1="480.5" y1="164.8" x2="480.5" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="480.5" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="489.1" y1="164.8" x2="489.1" y2="132.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="489.1" cy="132.1" r="2.4" fill="var(--accent)"/><line x1="497.7" y1="164.8" x2="497.7" y2="95.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="497.7" cy="95.4" r="2.4" fill="var(--accent)"/><line x1="506.4" y1="164.8" x2="506.4" y2="66.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="506.4" cy="66.7" r="2.4" fill="var(--accent)"/><line x1="515.0" y1="164.8" x2="515.0" y2="55.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="515.0" cy="55.8" r="2.4" fill="var(--accent)"/><line x1="523.6" y1="164.8" x2="523.6" y2="66.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="523.6" cy="66.7" r="2.4" fill="var(--accent)"/><line x1="532.3" y1="164.8" x2="532.3" y2="95.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="532.3" cy="95.4" r="2.4" fill="var(--accent)"/><line x1="540.9" y1="164.8" x2="540.9" y2="132.1" stroke="var(--accent)" stroke-width="1.6"/><circle cx="540.9" cy="132.1" r="2.4" fill="var(--accent)"/><line x1="549.5" y1="164.8" x2="549.5" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="549.5" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="558.2" y1="164.8" x2="558.2" y2="184.4" stroke="var(--accent)" stroke-width="1.6"/><circle cx="558.2" cy="184.4" r="2.4" fill="var(--accent)"/><line x1="566.8" y1="164.8" x2="566.8" y2="187.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="566.8" cy="187.9" r="2.4" fill="var(--accent)"/><line x1="575.4" y1="164.8" x2="575.4" y2="178.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="575.4" cy="178.8" r="2.4" fill="var(--accent)"/><line x1="584.0" y1="164.8" x2="584.0" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="584.0" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="592.7" y1="164.8" x2="592.7" y2="153.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="592.7" cy="153.9" r="2.4" fill="var(--accent)"/><line x1="601.3" y1="164.8" x2="601.3" y2="150.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="601.3" cy="150.9" r="2.4" fill="var(--accent)"/><line x1="609.9" y1="164.8" x2="609.9" y2="155.9" stroke="var(--accent)" stroke-width="1.6"/><circle cx="609.9" cy="155.9" r="2.4" fill="var(--accent)"/><line x1="618.6" y1="164.8" x2="618.6" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="618.6" cy="164.8" r="2.4" fill="var(--accent)"/><line x1="627.2" y1="164.8" x2="627.2" y2="172.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="627.2" cy="172.3" r="2.4" fill="var(--accent)"/><line x1="635.8" y1="164.8" x2="635.8" y2="174.7" stroke="var(--accent)" stroke-width="1.6"/><circle cx="635.8" cy="174.7" r="2.4" fill="var(--accent)"/><line x1="644.5" y1="164.8" x2="644.5" y2="171.3" stroke="var(--accent)" stroke-width="1.6"/><circle cx="644.5" cy="171.3" r="2.4" fill="var(--accent)"/><line x1="653.1" y1="164.8" x2="653.1" y2="164.8" stroke="var(--accent)" stroke-width="1.6"/><circle cx="653.1" cy="164.8" r="2.4" fill="var(--accent)"/></svg><figcaption><strong>A rectangle in frequency is a sinc in time.</strong> The inverse DTFT of the ideal low-pass shape is x[n] = (1/2π)∫<sub>−π/4</sub><sup>π/4</sup> e<sup>jωn</sup> dω = sin(πn/4)/(πn): height ω<sub>c</sub>/π = ¼ at n = 0, zeros at n = ±4, ±8, …, and a tail that decays only like 1/n. That tail is why x is not absolutely summable — yet its energy is finite (¼), and its DTFT is this rectangle (the partial sums converge in energy, with Gibbs ripples at the edges).</figcaption></figure>

This sinc decays only like $1/n$: $\sum_n|x[n]|$ grows without bound (like $\log N$ over $|n|\le N$), so it is not absolutely summable. Its energy is finite, though: $\sum_nx[n]^2=\frac{\omega_c}{\pi}$, which is $\frac14$ for $\omega_c=\frac{\pi}{4}$. Its DTFT exists in the energy sense, and partial sums of $\sum x[n]e^{-j\omega n}$ show Gibbs ripples at $\pm\omega_c$, just like the sawtooth's series at its jumps.

> [!recipe] Inverse DTFT of a piecewise-constant sketch
> 1. Write the period $[-\pi,\pi]$ as a sum of rectangles centred at $\omega=0$; heights add. A band $\omega_a\le|\omega|\le\omega_b$ is the rectangle of half-width $\omega_b$ minus the one of half-width $\omega_a$.
> 2. A centred rectangle of height $A$ and half-width $W$ gives $A\,\dfrac{\sin(Wn)}{\pi n}$.
> 3. Check $n=0$: $x[0]=\frac{1}{2\pi}\times$(area under one period).
> 4. Exams ask for a real closed form: if you integrated band by band, combine conjugate exponentials into sines and cosines.

> [!question] FA2024 MT2 #2 (8 pts): $X_d(\omega)=1$ for $\frac{\pi}{2}\le|\omega|\le\pi$ and $0$ for $|\omega|<\frac{\pi}{2}$. Find $x[n]$ as a real-valued expression.

> [!success]- Answer (checked by numerical integration for several $n$)
> "Everything minus the low band": the all-ones spectrum is $\delta[n]$, so
> $$
> x[n]=\delta[n]-\frac{\sin(\frac{\pi}{2}n)}{\pi n}=\delta[n]-\tfrac12\,\mathrm{sinc}(\tfrac{\pi}{2}n),\qquad x[0]=\tfrac12 .
> $$
> The key accepts two equivalent forms: $(-1)^n\,\frac12\,\mathrm{sinc}(\frac{\pi}{2}n)$ (the low-pass sinc moved to $\omega=\pi$, since $(-1)^n=e^{j\pi n}$; a band centred at $\pi$ wraps around the period's edge) and $\frac12\cos(\frac{3\pi}{4}n)\,\mathrm{sinc}(\frac{\pi}{4}n)$ (two bands of width $\frac{\pi}{2}$ centred at $\pm\frac{3\pi}{4}$). All three agree for every $n$ ([[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #2).

> [!question] SP2021 MT2 #7 (14 pts): the spectrum is $2$ for $|\omega|\le\frac{\pi}{3}$, $1$ for $\frac{\pi}{3}<|\omega|\le\frac{2\pi}{3}$ and $0$ for $\frac{2\pi}{3}<|\omega|\le\pi$, and $x[n]=A_1\frac{\sin(\omega_0n)}{\omega_0n}+A_2\frac{\sin(2\omega_0n)}{2\omega_0n}$. Find $A_1$, $A_2$, $\omega_0$.

> [!success]- Answer
> Rewrite each term as "height × $\frac{\sin(Wn)}{\pi n}$": $A_1\frac{\sin(\omega_0n)}{\omega_0n}=\frac{A_1\pi}{\omega_0}\cdot\frac{\sin(\omega_0n)}{\pi n}$ is a rectangle of height $\frac{A_1\pi}{\omega_0}$ on $|\omega|\le\omega_0$, and the second term a rectangle of height $\frac{A_2\pi}{2\omega_0}$ on $|\omega|\le2\omega_0$. The edges give $\omega_0=\frac{\pi}{3}$; the outer step gives $\frac{A_2\pi}{2\omega_0}=1$, so $A_2=\frac23$; the inner step gives $\frac{A_1\pi}{\omega_0}+1=2$, so $A_1=\frac13$ ([[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #7).

## 9. How this lecture is tested

> [!exam] How Lecture 13 is tested
> The DTFT is the backbone of Midterm 2; this lecture supplies its definition-level problems. Family page: [[problems/dtft-and-inverse-dtft|computing DTFTs and inverse DTFTs]].
> - **DTFT of a short sequence, factored**: [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #3 ($A$, $B$, $C$ above, 9 pts); [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #3(a) (the centred slide-15 sequence as a frequency response); [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #8 (which sequence has $X_d(\omega)=1+2\cos2\omega-2j\sin4\omega$: read the coefficients of $e^{\mp j2\omega}$, $e^{\mp j4\omega}$; answer $\{-1,0,1,0,\underset{\uparrow}{1},0,1,0,1\}$).
> - **Values without the closed form**: [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #2 (6 pts), [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #3 (9 pts), [[exams/midterm-1/past-exams/spring-2023|SP2023 MT1]] #9.
> - **Inverse DTFT of a sketched spectrum**: [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #2 (8 pts), [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #7 (14 pts). ([[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #2 also starts from a sketched rectangle, but it asks for the spectrum after modulation, a Lecture 14 property; its part (b) needs the $2\pi$-periodicity of this lecture to place the copies that wrap around $\pm\pi$.)
> - **Inverse DTFT with impulses**: [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #4 (5 pts).
> - **True/false on periodicity, existence, uniqueness**: [[exams/midterm-2/past-exams/fall-2024|FA2024 MT2]] #1(a) (False: no DTFT for $2^nu[n]$) and #1(b) (True: every DTFT is $2\pi$-periodic); [[exams/midterm-2/past-exams/fall-2023|FA2023 MT2]] #1(a), (b) (both False); [[exams/midterm-2/past-exams/spring-2025|SP2025 MT2]] #1(a) (True: $X_d=1+2e^{-j\omega}+3e^{-j2\omega}+4e^{-j3\omega}$ forces $x=\{\underset{\uparrow}{1},2,3,4\}$, by uniqueness); [[exams/midterm-2/past-exams/spring-2023|SP2023 MT2]] #3 (periodicity, above); [[exams/midterm-2/past-exams/fall-2019|FA2019 MT2]] #1(b) (False: a sequence "bandlimited to $\frac{\pi}{4}$" still has spectral copies near $\pm2\pi$), #1(c) (False: finite cosine) and #1(e) (False: every DTFT is periodic, not only those of infinite-length signals); [[exams/midterm-2/past-exams/spring-2021|SP2021 MT2]] #6 (which transform is periodic, which follows from the z-transform); zero-padding leaves the DTFT unchanged (five items, listed in §6.3).
>
> Homework: [[homework/hw5|HW5]] #1 (DTFTs from the definition: the three sequences above and $\alpha^ne^{j\omega_0n}u[n]$, which is $\frac{1}{1-\alpha e^{-j(\omega-\omega_0)}}$) and #2(a)–(c) (values without the closed form); %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #1 (CTFTs) and #3 (inverse DTFTs, including $\cos^2\omega$ and $e^{-j3.5\omega}$).

## Related

- Concepts: [[concepts/dtft|DTFT]] · [[concepts/fourier-series|Fourier series]] · [[concepts/dtft-pairs|DTFT pairs]] · [[concepts/dtft-properties|DTFT properties]] · [[concepts/complex-exponential|complex exponential]] · [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]] · [[concepts/template-matching|template matching]]
- Lectures: [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]] (inner products) · [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (DTFT from the z-transform, pairs and properties) · [[3-fourier-analysis/15-frequency-response|Lecture 15]] (frequency response) · unit: [[3-fourier-analysis/index|Unit 3]]
- Practice: [[problems/dtft-and-inverse-dtft|computing DTFTs and inverse DTFTs]] · [[homework/hw5|HW5]] · %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% · [[supplements/transform-tables|transform tables]] (DTFT Tables 5–6) · [[supplements/demo-notebooks|demo notebooks]] (`demo_DTFT`) · toolkit: [[0-toolkit/02-geometric-series|geometric series]], [[0-toolkit/01-complex-numbers|complex numbers]]

### Sources for this page

Snyder, *ECE 310 Lecture 13* notes ("Fourier analysis": §1 periodic signals, eqs. 1–18; §2 continuous-time Fourier series, eqs. 19–25 and Fig. 1; §2.1 continuous-time Fourier transform, eqs. 26–28; §3 discrete-time Fourier series with Exercise 1, eqs. 29–40; §4 DTFT with Exercise 2, eqs. 41–49 and Fig. 2) and slides 1–16 of Sep 23, 2026, including the annotated slides 5 (2π-periodicity proof), 6 (concept check), 8 (what $c_k$ means), 9 (orthogonality), 15 (DTFT example) and 16 (concept check). Lecture 14 notes §2 for the impulse pairs. Singer and Munson (2019), §2.3 and Fig. 2.4, for the periodicity examples. Slips in the notes noted on this page: the Fig. 1 caption ($c_k=\frac{j}{2\pi k}$), eq. 40 (phase), eq. 47 (sign); two more are harmless typos (eq. 29 should read $0\le k\le N_0-1$, as the slide does; the sum in eq. 35 runs over $n$, not $k$). HW5 with its official solutions; HW6. Past exams: FA2024, SP2025, FA2023, SP2023, SP2021, FA2019 Midterm 2 and SP2023 Midterm 1, with their keys. Every number on this page is checked in `verify/LA_l13.py` (133 checks: periodicity, orthogonality, Fourier coefficients and Gibbs overshoot, DTFS and DTFT closed forms against direct sums, every exam value, inverse DTFTs by numerical integration); the figures come from `verify/LA_figs.py`, and the code block was run as shown.
