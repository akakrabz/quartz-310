---
title: "Course demo notebooks"
description: "Catalog of the eleven Jupyter notebooks in the course's ece310-demos folder: what each one demonstrates, which lecture it belongs to, whether it is Midterm 1 material, and how to run it (numpy, scipy, matplotlib, scikit-image; the resources folder with the audio and image files is not in the uploaded copy)."
tags: [supplement, demo]
---

*Supplement · `ece310-demos-main/*.ipynb` (11 notebooks + `requirements.txt`)*

The course ships its Python demos as Jupyter notebooks. Five of them are Midterm 1 material and run in seconds; the rest belong to the second half of the course. Short runnable snippets taken from them — with the outputs pasted — are on [[demos/python-demos|Python demos]]; the interactive browser demos on this site ([[demos/convolution-explorer|convolution explorer]], [[demos/pole-zero-and-roc-explorer|pole-zero and ROC explorer]], [[demos/difference-equation-simulator|difference-equation simulator]]) cover the same ideas without installing anything.

## Catalog

| notebook | what it demonstrates | lecture | Midterm 1? |
|---|---|---|---|
| `demo_signals` | an audio file as a sequence (plot, zoom in, play); $\delta[n]$ and $\delta[n-m]$ as stem plots; a sampled 261.6 Hz sine (middle C) | [[1-signals-and-systems/01-digital-signals\|L1]], [[1-signals-and-systems/02-complex-numbers-and-elementary-signals\|L2]] | yes (light) |
| `demo_convolution` | $\delta[n]*h[n] = h[n]$, $\delta[n-n_0]*h[n] = h[n-n_0]$, a two-sample pulse convolved with a ramp, and "LTI ⇒ convolution" rebuilt from shifted impulse responses (`scipy.signal.convolve`) | [[1-signals-and-systems/04-impulse-response-and-convolution\|L4]] | **yes** |
| `demo_difference_equations` | $y[n] = \tfrac12y[n-1] + x[n]$: impulse response by a direct loop and by `lfilter` (identical), responses to $\delta[n-1]$ and to $\delta[n] - \tfrac12\delta[n-1]$ (whose zero cancels the pole: output $\delta[n]$) | [[1-signals-and-systems/05-difference-equations-and-block-diagrams\|L5]], [[2-z-transform/09-transfer-functions\|L9]] | **yes** |
| `demo_pfe_residuez` | `residuez` on $\dfrac{\frac15 z^{-1} - \frac{1}{15}z^{-2}}{1-\frac15 z^{-1}}$ (improper: `K` holds the long-division terms) and on $\dfrac{1}{(1-z^{-1})^2}$ (repeated pole) | [[2-z-transform/08-inverse-z-transform\|L8]], [[2-z-transform/10-improper-transfer-functions-and-system-algebra\|L10]] | **yes** |
| `demo_stability` | 2nd-order Butterworth low-pass: pole-zero plot, impulse response, filtering audio; then change one coefficient ($a_2 = 0.1716 \to 1.01$) so the poles move to $\pm j1.005$ — the impulse response and the output blow up | [[2-z-transform/11-bibo-stability-and-causality\|L11]] | **yes** |
| `demo_filtering` | Butterworth low-/high-pass from `signal.butter`: pole-zero plot, impulse response (Midterm 1), then frequency response $H_d(\omega)$ and DTFT of filtered audio (after) | L9, L11; L13–14 | partly |
| `demo_inverse_filter` | undoing an FIR blur: factor $B(z)$ into roots inside and outside the unit circle, run the inside part causally and the outside part **anti-causally** (flip, filter, flip back); 1-D and 2-D (image) | L10–L11 ideas, applied later | background |
| `demo_DTFT` | computing and plotting $\lvert X(e^{j\omega})\rvert$ of short sequences and of audio | [[3-beyond-midterm-1/index\|L13–14]] | no |
| `demo_sampling` | sampling a 30 Hz cosine at 100 Hz and its aliases at 70, 130, 170 Hz | after | no |
| `demo_DFT` | DFT/IDFT by hand, circular shift, zero padding, compression by discarding coefficients, spectral analysis and windowing | after | no |
| `demo_filter_design` | FIR design by windowing, equiripple (`remez`), IIR (`iirfilter`), applying the filters to audio | after | no |
| `demo_adaptivefilter` | LMS adaptive filter identifying an unknown FIR $h = \{1,2,3,4,5\}$ from noisy input–output data | end of course | no |

> [!exam] Why `demo_inverse_filter` is worth five minutes anyway
> Running an unstable-looking pole "backwards in time" is exactly [[0-midterm-1/past-exams/fall-2025|FA2025 #7(b)]]: the anti-causal part $H_1 = \dfrac{9/4}{1+2z^{-1}}$ is implemented as $y_1[n-1] = -\tfrac12y_1[n] + \tfrac98x[n]$, run from large $n$ down. See [[problems/two-sided-systems-as-recursions|two-sided systems as recursions]].

## Midterm 1 numbers from the notebooks (re-run here)

- `demo_pfe_residuez`: `R = [-0.667]`, `P = [0.2]`, `K = [0.667, 0.333]`, i.e. $\dfrac{\frac15 z^{-1} - \frac{1}{15}z^{-2}}{1-\frac15 z^{-1}} = \tfrac23 + \tfrac13 z^{-1} - \dfrac{2/3}{1-0.2z^{-1}}$. For $\dfrac{1}{(1-z^{-1})^2}$: `R = [0, 1]`, `P = [1, 1]` — the second residue belongs to the squared term. Current SciPy prints `K = []` where the saved notebook shows `K = [0.]`.
- `demo_difference_equations`: $h[n] = (\tfrac12)^n u[n]$; the loop and `lfilter` agree to the last bit.
- `demo_stability`: `butter(2, 0.5)` gives `a = [1, 0, 0.1716]`, poles $\pm j0.414$; with `a[2] = 1.01` the poles are $\pm j\sqrt{1.01}$, just outside the unit circle — a causal system with a pole outside the unit circle is unstable ([[concepts/bibo-stability|BIBO stability]]).

(`verify/hub/supp_demos.py` executes every code cell of every notebook headless and checks these values.)

## How to run them

1. Python 3 with the packages in `requirements.txt`: **numpy, matplotlib, scipy, scikit-image**, plus Jupyter: `pip install -r requirements.txt jupyterlab`.
2. In the folder: `jupyter lab`, open a notebook, *Run → Run All Cells*.
3. **Missing data:** the uploaded copy contains only the `.ipynb` files. Cells that read `resources/handel.wav` (signals, stability, filtering, DTFT, DFT, filter design) or `resources/test-image.jpg` (inverse filter) — and the cells that use their results — fail with `FileNotFoundError`/`NameError`; get the `resources/` folder from the course's demo repository, or skip those cells. Every other cell runs as is (checked with Python 3.11, NumPy 2.4, SciPy 1.17, Matplotlib 3.10). `Audio(...)` needs Jupyter (IPython) to play sound.
4. Quirks: `demo_filter_design` ends with a stray cell containing just `pri` (a harmless `NameError`); two notebooks still say "running Python 3.6.6", which does not matter.

### Sources for this page

`ece310-demos-main/*.ipynb` (markdown and code cells read with Python's `json` module) and `requirements.txt`; every code cell executed in this container by `verify/hub/supp_demos.py`.
