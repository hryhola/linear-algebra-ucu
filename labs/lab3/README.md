# Lab 3 — Positive definite matrices at work: Gaussians and kernel ridge

## Team

- **Vladyslav Hryhola** — Core A: implementation, predictions, written answers,
  verification. AI assistants were used as a study aid during learning and review.
- **Ihor Kashuba** — Core B (planned). His notebook is not yet included in this
  checkout; his contribution will be recorded when it is.

## Status

- **Core A:** A1–A3 complete. All 20 required code cells run top to bottom from a
  clean `linear-algebra-ucu` kernel (28 October 2026); outputs saved, both plots
  inspected.
- **Core B:** unimplemented starter in this checkout, no saved outputs.
- **Extension:** none attempted. Extension cells are left as supplied and
  unexecuted, so a full *Restart & Run All* stops at the first E1 placeholder
  after cell 20.
- **Late days:** 0.

## Versions (printed by Core A)

Python 3.14.6, NumPy 2.5.3, SciPy 1.18.1, pandas 3.0.6, Matplotlib 3.11.2,
scikit-learn 1.9.1. Core B has no saved version output yet.

## Notes

- `np.linalg.det` and `np.linalg.inv` appear only in `gauss_logpdf_naive` and the
  A2(c) sweep, as the notebook requires; `scipy.stats.multivariate_normal` only
  in the check cell. Supplied cells, seeds and scaffolding are unchanged.
- This NumPy build emits warnings from `np.linalg.det` even for well-conditioned
  matrices; they are silenced inside `gauss_logpdf_naive` and the A2(c) sweep only.
- A2(d) timings differ between machines and runs; the saved naive/Cholesky ratios
  are 4.5, 6.5, 8.6 and 9.2.

## Environment

Shared environment from the [root README](../../README.md). From the repository root:

```sh
.venv/bin/python -m pip install -r requirements.txt
cd labs/lab3
../../.venv/bin/python -m jupyter lab
```

Select the **linear-algebra-ucu** kernel. No data files are needed; the data sets
load from scikit-learn.

## Files

- `Lab3-CoreA-gaussian.ipynb` — Core A (extensions E1–E2 unattempted)
- `Lab3-CoreB-kernel-ridge.ipynb` — Core B (extension E3 unattempted)
- `lab3-description.md` — assignment text
