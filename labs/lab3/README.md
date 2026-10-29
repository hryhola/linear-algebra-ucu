# Lab 3 — Positive definite matrices at work: Gaussians and kernel ridge

## Team

- **Vladyslav Hryhola** — Core A: implementation, predictions, written answers,
  verification. AI assistants were used as a study aid during learning and review.
- **Ihor Kashuba** — Core B & Extension E3: implementation, predictions, written answers, verification. AI assistants were used as a study aid during learning and review.

## Status

* **Core A**: A1–A3 complete. All required code cells run top to bottom from a clean `linear-algebra-ucu` kernel; outputs saved, plots inspected.
* **Core B**: B1–B4 complete. All required code cells run top to bottom from a clean `linear-algebra-ucu` kernel; outputs saved, plots inspected.
* **Extension**: E3 attempted and completed in Notebook B (Gaussian-process regression is kernel ridge). All cells executed, verified against `GaussianProcessRegressor`, and concluded with an empirical **Finding**. (Extensions E1–E2 in Notebook A left unattempted).
* **Late days used**: 0.
* **Runs top to bottom from a clean kernel**: yes.

## Versions

* **Core A**: Python 3.14.6, NumPy 2.5.3, SciPy 1.18.1, pandas 3.0.6, Matplotlib 3.11.2, scikit-learn 1.9.1.
* **Core B**: Python 3.13.18, NumPy 2.1.3, SciPy 1.16.3, Matplotlib 3.10.0, scikit-learn 1.6.1.

## Notes

- `np.linalg.det` and `np.linalg.inv` appear only in `gauss_logpdf_naive` and the
  A2(c) sweep, as the notebook requires; `scipy.stats.multivariate_normal` only
  in the check cell. Supplied cells, seeds and scaffolding are unchanged.
- This NumPy build emits warnings from `np.linalg.det` even for well-conditioned
  matrices; they are silenced inside `gauss_logpdf_naive` and the A2(c) sweep only.
- A2(d) timings differ between machines and runs; the saved naive/Cholesky ratios
  are 4.5, 6.5, 8.6 and 9.2.
* All custom solvers in Core B and Extension E3 strictly adhere to the course rules: no calls to `np.linalg.inv` or `np.linalg.det`; all systems are solved via Cholesky factorizations (`scipy.linalg.cho_factor`/`cho_solve`, `scipy.linalg.cholesky`) and triangular solves (`scipy.linalg.solve_triangular`).
* Scikit-learn's `KernelRidge` and `GaussianProcessRegressor` are used strictly in the provided validation/check cells.
* In Core B, random seeds are untouched (`random_state=0`, `random_state=1`, `rng = np.random.default_rng(7)`), guaranteeing full reproducibility.

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
