---
title: "LTI response to sinusoids and periodic inputs"
description: "Recipe for the Midterm 2 problems that feed a constant, (−1)ⁿ, complex exponentials and real sinusoids into a system given by h[n], H(z), an LCCDE or a formula for H_d(ω): list the frequencies, evaluate H_d at each, test whether h is real before using the cosine shortcut, and handle zeros of H_d, complex h and the ambiguity at ω = π. On six of seven past exams; four fresh practice problems."
tags: [problem-family, problem, frequency-response, dtft, midterm-2]
family_frequency: "6 of 7 Midterm 2 exams"
typical_points: "8–18"
lectures: [14, 15]
---

*Problem family · a full problem on five of the seven past Midterm 2 exams (FA2019, SP2023, FA2023, FA2024, SP2025) and a True/False part on FA2019 and FA2021 · 8–18 points · uses [[3-fourier-analysis/15-frequency-response|Lecture 15]], with the symmetry test of [[3-fourier-analysis/14-dtft-properties|Lecture 14]] · concepts: [[concepts/frequency-response]], [[concepts/eigenfunctions-of-lti-systems]], [[concepts/dtft-properties]] · see it: [[demos/frequency-response-explorer|frequency-response explorer]] · drill: [sinusoidal response](/static/demos/drills/#sinr)*

> [!abstract] In one breath
> A complex exponential is an eigenfunction: $e^{j\omega_0n}\to H_d(\omega_0)\,e^{j\omega_0n}$. Everything else follows by linearity, one frequency at a time: a constant is $\omega=0$, $(-1)^n$ is $\omega=\pi$, $j^n$ is $\omega=\frac{\pi}{2}$, and a real cosine or sine is **two** exponentials at $\pm\omega_0$. If $h[n]$ is real, $H_d(-\omega)=H_d^*(\omega)$ and the two halves recombine into the shortcut $A\cos(\omega_0n+\theta)\to A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$. If $h$ is complex, that shortcut is wrong and the exponentials must be treated separately. Every recent exam makes you decide which case you are in first.

## What it looks like on the exam

"The frequency response of an LTI system is $H_d(\omega)=\dots$; compute the output for $x[n]=\dots$." The input mixes three or four kinds of term (a constant, a complex exponential, a sine with a phase, sometimes $(-1)^n$ or $j^n$), and $H_d$ is chosen so that one term is blocked, one tests the symmetry, and one needs care with a sign. Recent exams use a formula $H_d$ such as $\lvert\omega\rvert e^{-j\pi\sin\omega}$ whose $h[n]$ is never computed.

| instance | system | input | asked |
|---|---|---|---|
| [[exams/midterm-2/past-exams/fall-2019\|FA2019 #7]] (10) | $H(z)=1+z^{-4}$ | $3+4\cos(\frac{\pi}{4}n)+e^{j\frac{\pi}{2}n}$ | $y[n]$ |
| [[exams/midterm-2/past-exams/spring-2023\|SP2023 #6]] (8) | $H_d=\omega e^{j\pi\cos\omega}$ | $3+e^{j\frac{\pi}{3}n}+\sin(\frac{\pi}{2}n+\frac{\pi}{4})$ | $y[n]$ (complex $h$) |
| [[exams/midterm-2/past-exams/fall-2023\|FA2023 #4(b)]] (18 with the plot) | $H_d=(\frac12+\cos\omega)e^{j\lvert\omega\rvert}$ | $4j-2e^{j(\frac{2\pi}{3}n+\frac{\pi}{4})}+3\sin(\frac{3\pi}{4}n)$ | $y[n]$ (complex $h$) |
| [[exams/midterm-2/past-exams/fall-2024\|FA2024 #4]] (12) | $H_d=\lvert\omega\rvert e^{-j\pi\sin\omega}$ | $3+\cos(\frac{\pi n}{6})+j^n$ | is $h$ real? then $y[n]$ |
| [[exams/midterm-2/past-exams/spring-2025\|SP2025 #4]] (10) | $H_d=j\omega e^{j\pi\sin\omega}$ | $5+2e^{j\frac{\pi}{4}n}+\sin(\frac{\pi}{2}n+\frac{\pi}{4})+(-1)^n$ | $y[n]$ |
| [[exams/midterm-2/past-exams/fall-2019\|FA2019 #1(d)]] | any LSI system | $\cos(\omega_0n+\phi)$ | T/F: the cosine rule for all $\omega_0,\phi$ allows complex $h$ |
| [[exams/midterm-2/past-exams/fall-2021\|FA2021 #1(a)]] | a stable LTI system | $\cos(\omega_0n)$ | T/F: an eigenfunction? |
| %%hw6:W1tob21ld29yay9odzZcfEhXNl1d%%HW6%%/hw6%% | #5 accumulator $y[n]-y[n-1]=x[n]$; #6 comb $y[n]=x[n]+x[n-10]$; #7 $H_d=\omega e^{j\sin\omega}$ | sums of constants, sinusoids and $j^n$ | is $H_d=H(e^{j\omega})$? outputs |

Close relatives on the [[problems/dtft-and-inverse-dtft|DTFT family]] page: FA2021 #2 (a causal LCCDE whose frequency response needs impulses, so $H_d\ne H(e^{j\omega})$) and FA2019 #6 (can the output be real?). The magnitude and phase plots that often come with these systems are the [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]] family.

> [!success]- Answers to the exam instances
> | instance | $y[n]$ |
> |---|---|
> | FA2019 #7 | $H_d=2\cos(2\omega)e^{-j2\omega}$: $H_d(0)=2$, $H_d(\frac{\pi}{4})=0$, $H_d(\frac{\pi}{2})=2$, so $y=6+2e^{j\frac{\pi}{2}n}$ |
> | SP2023 #6 | $\frac{\pi}{3}e^{j(\frac{\pi}{3}n+\frac{\pi}{2})}-j\frac{\pi}{2}\cos(\frac{\pi}{2}n+\frac{\pi}{4})$ (DC blocked; $H_d(\pm\frac{\pi}{2})=\pm\frac{\pi}{2}$) |
> | FA2023 #4(b) | $6j+\frac{3(\sqrt2-1)}{2}\,e^{-j\pi/4}\sin(\frac{3\pi}{4}n)$ (the exponential at $\frac{2\pi}{3}$ sits on a zero; $H_d$ is even, so both halves of the sine see the same factor) |
> | FA2024 #4 | $h$ real (even magnitude, odd phase); $y=\frac{\pi}{6}\sin(\frac{\pi}{6}n)-\frac{\pi}{2}\,j^n$ |
> | SP2025 #4 | key: $\frac{\pi}{2}e^{j(\frac{\pi}{4}n+\frac{\pi}{2}(1+\sqrt2))}+\frac{\pi}{2}\sin(\frac{\pi}{2}n-\frac{\pi}{4})+j\pi(-1)^n$; the last term is ambiguous because $H_d(\pi)=j\pi\ne H_d(-\pi)=-j\pi$, and the real system actually returns 0 for $(-1)^n$ (see the exam page) |
> | FA2019 #1(d) | False: the rule for every $\omega_0,\phi$ forces $H_d(-\omega)=H_d^*(\omega)$, i.e. real $h$ |
> | FA2021 #1(a) | False: a delay turns $\cos\omega_0n$ into $\cos(\omega_0n-\omega_0)$ |
>
> Worked solutions on the exam pages; every row re-checked in `verify/FAM_instances.py`.

## The recipe

> [!recipe] Sinusoids through an LTI system, one frequency at a time
> 1. **Get $H_d(\omega)$.** From $h[n]$: $\sum_nh[n]e^{-j\omega n}$ (factor out the centre). From $H(z)$ or an LCCDE: $H(e^{j\omega})$, **allowed only when the ROC contains the unit circle** (stable system); otherwise there is no steady-state sinusoidal response (FA2021 #2, HW6 #5).
> 2. **Is $h$ real?** Test $H_d(-\omega)\overset{?}{=}H_d^*(\omega)$: the magnitude must be even and the phase odd. $\lvert\omega\rvert e^{-j\pi\sin\omega}$ passes; $\omega e^{j\pi\cos\omega}$ and $(\frac12+\cos\omega)e^{j\lvert\omega\rvert}$ fail (FA2024 #4 vs SP2023 #6, FA2023 #4).
> 3. **List every frequency in the input, with its sign.** Constant $c$: $\omega=0$. $(-1)^n=e^{j\pi n}$: $\omega=\pi$. $j^n=e^{j\frac{\pi}{2}n}$: $\frac{\pi}{2}$ only. $e^{j\omega_0n}$: $\omega_0$ only (no partner). $\cos$, $\sin$: $\pm\omega_0$. Reduce every frequency into $(-\pi,\pi]$.
> 4. **Evaluate $H_d$ at each frequency.** Write each value as a number, or as magnitude and angle. A zero of $H_d$ removes that term.
> 5. **Apply.** Exponentials: $e^{j\omega_0n}\to H_d(\omega_0)e^{j\omega_0n}$, keeping their coefficients. Real $h$: $A\cos(\omega_0n+\theta)\to A\lvert H_d(\omega_0)\rvert\cos\big(\omega_0n+\theta+\angle H_d(\omega_0)\big)$, the same for $\sin$. Complex $h$: $\cos\alpha=\frac{e^{j\alpha}+e^{-j\alpha}}{2}$, $\sin\alpha=\frac{e^{j\alpha}-e^{-j\alpha}}{2j}$, and multiply the two halves by $H_d(\omega_0)$ and $H_d(-\omega_0)$ separately.
> 6. **Assemble and check.** Real $h$ and a real input term give a real output term; $H_d(0)$ and $H_d(\pi)$ are real for real $h$; a term on a zero of $H_d$ is gone. Write which answer form you use (exponentials or cosines).

> [!example] Python: the shortcut against the convolution sum, for a complex $h$
> ```python
> import numpy as np
>
> h = np.array([-0.5j, 1, 0.5j])                  # Practice 2: H_d(w) = (1 + sin w) e^{-jw}, h complex
> n = np.arange(0, 8)
> x = lambda n: 2 * np.cos(np.pi * n / 2)         # a real cosine at w0 = pi/2
> y = sum(h[k] * x(n - k) for k in range(3))      # the convolution sum, exactly
> Hd = lambda w: (1 + np.sin(w)) * np.exp(-1j * w)
> honest = Hd(np.pi / 2) * np.exp(1j * np.pi * n / 2) + Hd(-np.pi / 2) * np.exp(-1j * np.pi * n / 2)
> shortcut = 2 * abs(Hd(np.pi / 2)) * np.cos(np.pi * n / 2 + np.angle(Hd(np.pi / 2)))
> print("convolution :", np.round(y, 3) + 0.0)
> print("split       :", np.round(honest, 3) + 0.0)
> print("shortcut    :", np.round(shortcut, 3) + 0.0)
> ```
> ```text
> convolution : [ 0.-2.j  2.+0.j  0.+2.j -2.+0.j  0.-2.j  2.+0.j  0.+2.j -2.+0.j]
> split       : [ 0.-2.j  2.+0.j  0.+2.j -2.+0.j  0.-2.j  2.+0.j  0.+2.j -2.+0.j]
> shortcut    : [ 0.  4.  0. -4.  0.  4.  0. -4.]
> ```
> Splitting into exponentials reproduces the convolution sum; the real-system shortcut gives a different, real (and wrong) signal.

> [!trap] Where the points go
> - **The real-system shortcut with a complex $h$.** SP2023 #6 and FA2023 #4 are built for this: a real sine goes in, a complex signal must come out. Test the symmetry first (FA2024 #4(a) asks for it explicitly).
> - **$H_d(-\omega_0)$ evaluated carelessly.** In SP2025 #4, $H_d(-\frac{\pi}{2})=-j\frac{\pi}{2}e^{-j\pi}=+j\frac{\pi}{2}$, the conjugate of $H_d(\frac{\pi}{2})$; writing $-j\frac{\pi}{2}$ again is the usual slip.
> - **A lone exponential has no partner.** $j^n$, $e^{j\frac{\pi}{3}n}$ and $2e^{j\frac{\pi}{4}n}$ are multiplied by one value of $H_d$, and their coefficient stays ($2\cdot\frac{\pi}{4}=\frac{\pi}{2}$ in SP2025 #4).
> - **A constant is frequency 0, whatever it looks like:** $4j$ in FA2023 #4 becomes $4j\,H_d(0)=6j$; it is not $j^n$.
> - **Amplitude versus magnitude.** $H_d=2\cos(2\omega)e^{-j2\omega}$ at $\frac{\pi}{2}$ is $(-2)(-1)=+2$ (FA2019 #7): keep the sign of the real factor together with the linear phase, or convert both to magnitude and angle.
> - **$H_d$ that jumps at $\pm\pi$.** SP2025 #4's $H_d$ has $H_d(\pi)\ne H_d(-\pi)$, so the response to $(-1)^n$ is not defined by the formula; the key uses $+\pi$. Say which value you take.
> - **IIR systems:** the formula gives the steady state of an input that has been running forever; a causal input switched on at $n=0$ adds a transient that dies out only if the system is stable (Practice 3).

## Practice problems

> [!question] Practice 1 — a real FIR, four kinds of term
> $h[n]=\{\underset{\uparrow}{1},\ -1,\ 1\}$. Find $y[n]$ for $x[n]=4+2\cos(\frac{\pi}{3}n+\frac{\pi}{6})+3\sin(\frac{\pi}{2}n)+(-1)^n$.

> [!success]- Solution
> $H_d(\omega)=1-e^{-j\omega}+e^{-j2\omega}=e^{-j\omega}\left(e^{j\omega}-1+e^{-j\omega}\right)=e^{-j\omega}(2\cos\omega-1)$; $h$ is real.
> - $\omega=0$: $H_d(0)=1$, so $4\to4$.
> - $\omega=\frac{\pi}{3}$: $2\cos\frac{\pi}{3}-1=0$: the cosine is **blocked**.
> - $\omega=\frac{\pi}{2}$: $H_d=e^{-j\pi/2}(0-1)=e^{j\pi/2}=j$: magnitude 1, angle $\frac{\pi}{2}$, so $3\sin(\frac{\pi}{2}n)\to3\sin(\frac{\pi}{2}n+\frac{\pi}{2})=3\cos(\frac{\pi}{2}n)$.
> - $\omega=\pi$: $H_d(\pi)=e^{-j\pi}(-2-1)=3$, so $(-1)^n\to3(-1)^n$.
> $$
> y[n]=4+3\cos\left(\tfrac{\pi}{2}n\right)+3(-1)^n .
> $$
> Check in the time domain, $y[n]=x[n]-x[n-1]+x[n-2]$, for $-20\le n\lt60$ (`verify/FAM_practice.py`).

> [!question] Practice 2 — a complex $h$: a cosine in, an exponential out
> $h[n]=\{\underset{\uparrow}{-\tfrac{j}{2}},\ 1,\ \tfrac{j}{2}\}$.
> (a) Show that $H_d(\omega)=(1+\sin\omega)\,e^{-j\omega}$. Is $h$ real?
> (b) Find $y[n]$ for $x[n]=3+2\cos(\frac{\pi}{2}n)+e^{j\frac{\pi}{3}n}$.

> [!success]- Solution
> **(a)** $-\frac{j}{2}+e^{-j\omega}+\frac{j}{2}e^{-j2\omega}=e^{-j\omega}\left(1+\frac{e^{j\omega}-e^{-j\omega}}{2j}\right)=(1+\sin\omega)e^{-j\omega}$. The magnitude $1+\sin\omega$ is not even, so $H_d(-\omega)\ne H_d^*(\omega)$: $h$ is complex (as its samples show).
>
> **(b)** $H_d(0)=1$; $H_d(\frac{\pi}{2})=2e^{-j\pi/2}=-2j$; $H_d(-\frac{\pi}{2})=0$; $H_d(\frac{\pi}{3})=(1+\frac{\sqrt3}{2})e^{-j\pi/3}$. Split the cosine: $2\cos(\frac{\pi}{2}n)=e^{j\frac{\pi}{2}n}+e^{-j\frac{\pi}{2}n}\to-2j\,e^{j\frac{\pi}{2}n}+0$.
> $$
> y[n]=3+2e^{j(\frac{\pi}{2}n-\frac{\pi}{2})}+\left(1+\tfrac{\sqrt3}{2}\right)e^{j(\frac{\pi}{3}n-\frac{\pi}{3})} .
> $$
> The system keeps only the positive-frequency half of the cosine. The shortcut would have given $4\sin(\frac{\pi}{2}n)$ for that term, a real signal: wrong (see the Python box).

> [!question] Practice 3 — an IIR resonator
> A causal system obeys $y[n]=-\tfrac14y[n-2]+x[n]-x[n-2]$.
> (a) Is $H_d(\omega)=H(e^{j\omega})$ allowed? (b) Find the output for $x[n]=5+3\sin(\frac{\pi}{2}n+\frac{\pi}{6})+2(-1)^n$, applied for all $n$. (c) What changes if the input is switched on at $n=0$?

> [!success]- Solution
> **(a)** $H(z)=\dfrac{1-z^{-2}}{1+\frac14z^{-2}}$ with poles $\pm\frac{j}{2}$; causal, so the ROC $\lvert z\rvert\gt\frac12$ contains the unit circle: yes, $H_d(\omega)=\dfrac{1-e^{-j2\omega}}{1+\frac14e^{-j2\omega}}$, and $h$ is real.
>
> **(b)** $H_d(0)=\frac{0}{5/4}=0$ and $H_d(\pi)=0$ (the zeros at $z=\pm1$), while $H_d(\frac{\pi}{2})=\frac{1-(-1)}{1-\frac14}=\frac83$, real and positive. Only the sine survives:
> $$
> y[n]=8\sin\left(\tfrac{\pi}{2}n+\tfrac{\pi}{6}\right).
> $$
> **(c)** The answer in (b) becomes the **steady state**: with the input starting at $n=0$, `lfilter` gives an output that differs from $8\sin(\frac{\pi}{2}n+\frac{\pi}{6})$ by $4.5$ at $n=0$, $0.0044$ at $n=10$ and $4\times10^{-6}$ at $n=20$ (a transient decaying like $(\frac12)^n$, the pole radius), and is down to rounding error (about $10^{-14}$) from $n\approx45$ on.

> [!question] Practice 4 — design a null
> A real FIR filter $h[n]=\{\underset{\uparrow}{1},\ a,\ 1\}$ must remove $\cos(\frac{2\pi}{3}n+\theta)$ for every $\theta$. Find $a$, then the output for $x[n]=2+\cos(\frac{\pi}{3}n)+5\cos(\frac{2\pi}{3}n+1)+(-1)^n$.

> [!success]- Solution
> $H_d=e^{-j\omega}(a+2\cos\omega)$; a zero at $\frac{2\pi}{3}$ needs $a+2(-\frac12)=0$, so $a=1$. Then $H_d(0)=3$, $H_d(\frac{\pi}{3})=2e^{-j\pi/3}$, $H_d(\frac{2\pi}{3})=0$, $H_d(\pi)=e^{-j\pi}(1-2)=1$:
> $$
> y[n]=6+2\cos\left(\tfrac{\pi}{3}n-\tfrac{\pi}{3}\right)+(-1)^n .
> $$
> (The three-point moving sum is the classic way to cancel a hum at a known frequency; checked by direct convolution.)

## Related

- Lectures: [[3-fourier-analysis/15-frequency-response|Lecture 15]] (eigenfunctions, the cosine rule and why $h$ must be real, sums of sinusoids, $Y_d=X_dH_d$), [[3-fourier-analysis/14-dtft-properties|Lecture 14]] (Hermitian symmetry), [[3-fourier-analysis/16-magnitude-and-phase-response|Lecture 16]] (reading $\lvert H_d\rvert$ and $\angle H_d$).
- Concepts: [[concepts/frequency-response|frequency response]], [[concepts/eigenfunctions-of-lti-systems|eigenfunctions of LTI systems]], [[concepts/dtft-properties|DTFT properties]], [[concepts/magnitude-and-phase-response|magnitude and phase response]], [[concepts/marginal-stability|marginal stability]] (why the accumulator has no steady state).
- Try it: [[demos/frequency-response-explorer|frequency-response explorer]] (type the taps, move $\omega_0$, watch the output cosine), the [sinusoidal-response drill](/static/demos/drills/#sinr), [[demos/practice-drills|all drills]]; homework %%hw6:W1tob21ld29yay9odzZ8SFc2XV0=%%HW6%%/hw6%% #5–#7.
- Related families: [[problems/dtft-and-inverse-dtft|DTFT and inverse DTFT]], [[problems/magnitude-phase-and-group-delay|magnitude, phase and group delay]]; Units 1–2 background: [[problems/lccde-to-transfer-function-and-response|LCCDE ⇄ H(z) ⇄ response]]. Exams: [[exams/midterm-2/index|Midterm 2 overview]], [[problems/index|all families]].

### Sources for this page

Lecture 15 notes and slides (eigenfunctions, the real-sinusoid rule and its failure for complex $h$, sums of sinusoids; no annotated slides exist for this lecture); Lecture 14 (Hermitian symmetry); HW6 #5–#7 (no official solutions yet); past Midterm 2 exams FA2019 #7 and #1(d), FA2021 #1(a), SP2023 #6, FA2023 #4, FA2024 #4, SP2025 #4 with keys (the SP2025 #4 caveat is documented on its exam page). Practice problems are new; every number is checked in `verify/FAM_practice.py` (direct convolution, `lfilter` for the transient), the answer table in `verify/FAM_instances.py`.
