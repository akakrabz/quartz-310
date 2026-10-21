---
title: "Convolution"
description: "y[n] = Σ x[k] h[n−k], the output of every LTI system: properties, start/end/length rules, the three hand methods on one example, infinite-length sums, traps."
tags: [concept, convolution, systems, midterm-1]
aliases: ["convolution", "convolution sum", "discrete convolution", "linear convolution", "x*h", "(x*h)[n]"]
---

> [!key] Definition (Lecture 4)
> $$
> y[n]=(x*h)[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]=\sum_{k=-\infty}^{\infty}h[k]\,x[n-k]
> $$
> Flip $h$, shift by $n$, multiply with $x[k]$, sum.
>
> **Start, end, length:** $x$ on $[n_s,n_e]$ (length $N$), $h$ on $[m_s,m_e]$ (length $M$) $\Rightarrow$ $y$ on $[\,n_s+m_s,\ n_e+m_e\,]$, length $N+M-1$.

| property | statement |
|---|---|
| commutative | $x*h=h*x$ |
| associative | $(x*h_1)*h_2=x*(h_1*h_2)$ (series) |
| distributive | $x*(h_1+h_2)=x*h_1+x*h_2$ (parallel) |
| shift | $x*\delta[n-k]=x[n-k]$ |
| z-domain | $Y(z)=X(z)H(z)$, ROC at least $R_x\cap R_h$ |
| DTFT | $Y_d(\omega)=X_d(\omega)H_d(\omega)$ |

> [!example] $x[n]=\{\underset{\uparrow}{1},\ 2,\ 3\}$, $h[n]=\{1,\ \underset{\uparrow}{0},\ -1\}$
> Start $-1$, end $3$, length $5$. Three methods (flip-and-shift table, Toeplitz matrix, superposition $y[n]=x[n+1]-x[n-1]$).

> [!success]- Answer
> $$
> y[n]=\{1,\ \underset{\uparrow}{2},\ 2,\ -2,\ -3\}.
> $$

**Infinite length** (Lecture 4):

$$
a^nu[n]*b^nu[n]=\frac{a^{n+1}-b^{n+1}}{a-b}\,u[n]\ (a\ne b),\qquad a^nu[n]*a^nu[n]=(n+1)\,a^nu[n].
$$

> [!trap]
> - Track the $n=0$ arrow: `np.convolve` returns values only; start index is $n_s+m_s$ (SP2025 #4(a) key slip, [[0-toolkit/05-errata|errata]]).
> - Length counts interior zeros ([[exams/midterm-1/past-exams/fall-2025|FA2025 #3a]]).
> - $x[n]*\delta[n-k]=x[n-k]$ but $x[n]\,\delta[n-k]=x[k]\,\delta[n-k]$.
> - Two-sided sums can diverge: $(\tfrac12)^nu[n]*2^{-n}u[-n]$ ([[homework/hw2|HW2]] #5e).

**Where it appears:** [[1-signals-and-systems/04-impulse-response-and-convolution|Lecture 4]], [[2-z-transform/09-transfer-functions|Lecture 9]], [[3-fourier-analysis/12-convolution-as-template-matching|Lecture 12]], [[3-fourier-analysis/14-dtft-properties|Lecture 14]]; [[homework/hw2|HW2]] #3–#5; [[problems/finite-length-convolution]] (7/7 exams), [[problems/infinite-length-convolution]]; [[demos/convolution-explorer]].

## Related
[[concepts/lti-system|LTI system]] · [[concepts/impulse-response|impulse response]] · [[concepts/step-response|step response]] · [[concepts/system-algebra|system algebra]] · [[concepts/template-matching|template matching]]

### Sources for this page
Lecture 4 notes §2, slides 6–11; Lecture 12 §1; Lecture 14 §3; HW2 #5; Midterm 1 convolution problems.
