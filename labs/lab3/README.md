# Lab 3 — Positive definite matrices at work: Gaussians and kernel ridge

## Status

Core A is in progress: A1(a–f) and A2(a–b), including covariance, whitening,
Mahalanobis distances and Gaussian log-density, are implemented and checked.
Code cells 1–14 passed in
order from a fresh kernel on 28 October 2026, and their outputs are saved.
A2(c–d) and A3 remain unfinished. Core B in this checkout remains an
unimplemented, unexecuted starter. No extension has been attempted.

## Team

- **Vladyslav Hryhola**
- **Ihor Kashuba**

## Work split

### Core A — The Gaussian, computed

Planned lead: **Vladyslav Hryhola**. A1(a–f) and A2(a–b) are implemented and checked; the rest
is unfinished. Final contributions will be recorded when completed.

### Core B — Kernel ridge regression

Planned lead: **Ihor Kashuba**. The notebook in this checkout remains a starter;
the contribution will be recorded when his completed version is included.

## Extensions

No optional extension has been attempted.

## Environment and startup

Use the shared Python 3.12+ environment described in the [root README](../../README.md).
The lab requires NumPy, SciPy, pandas, Matplotlib, and scikit-learn.

Scikit-learn is included in the shared `requirements.txt` and installed in the
local `.venv`. From the repository root:

```sh
.venv/bin/python -m pip install -r requirements.txt
cd labs/lab3
../../.venv/bin/python -m jupyter lab
```

Choose **Python (.venv: linear-algebra-ucu)** as the notebook kernel. The supplied
notebooks currently request the generic **Python 3** kernel, as do the previous
labs; select the shared environment explicitly if needed.

No external data files are required. The notebooks load bundled scikit-learn
data sets or generate their inputs. The largest Core B timing experiment needs
about 2 GB of memory, according to the assignment.

## Files

- `Lab3-CoreA-gaussian.ipynb` — Core A and extensions 1–2
- `Lab3-CoreB-kernel-ridge.ipynb` — Core B and extension 3
- [lab3-description.md](lab3-description.md) — assignment and submission requirements

## Reproducibility and unfinished work

At the initial setup check, both notebook files passed notebook-format
validation, the environment passed `pip check`, and both import/version cells
passed in fresh kernels using temporary copies.

On 28 October 2026, Core A code cells 1–14 passed in order in a fresh
`linear-algebra-ucu` kernel. The supplied NumPy covariance/correlation
comparisons and whitening assertions passed. Maximum covariance identity
errors were approximately 1.6e-12 (Cholesky), 3.3e-09 (PCA) and 6.2e-09
(ZCA). ZCA had the smallest displacement on both raw and standardised data.
The three Mahalanobis distance arrays agreed (maximum difference about
1.95e-08), and the one-point triangular-solve check passed. Required written
answers for A1(a–f) are filled in, and notebook-format validation passed.

The A1(f) rank-based theoretical prediction was also saved before execution.
The correlation matrix became numerically singular at 30 observations and
below, and the 35-row training experiment demonstrated the amplification
versus shrinkage trade-off on held-out data. Written interpretations are saved.

The condition-number prediction was recorded before its experiment. The saved
condition numbers are 6.322e+11 for covariance and 9.983e+04 for correlation.

Core A's saved import output reports Python 3.14.6, NumPy 2.5.3, SciPy 1.18.1,
pandas 3.0.6, Matplotlib 3.11.2, and scikit-learn 1.9.1. Core B has no saved
version output yet.

The Cholesky Gaussian log-density implementation passed its SciPy comparison.
The Cholesky, naive and SciPy results all round to -38.5492599632 for the
supplied standardised tumour observation. The naive version is the only
implementation using explicit determinant and inverse operations.

Core A code cell 15 onward was not run during this check. A2(c–d), A3 and
notebook team fields are unfinished. Neither notebook has completed a fresh
top-to-bottom run of all required core cells. Do not use Run All while required
tasks still contain placeholders.

Before submission, complete both cores, record each member's contribution and
the versions printed by the notebooks (including scikit-learn), preserve the
supplied seeds, and restart and run all required core cells in order from clean
kernels. Leave unattempted optional extensions unexecuted. Save all required
outputs and update this README with the verified execution scope, status and any
remaining issues.
