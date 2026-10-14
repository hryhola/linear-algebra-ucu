# Lab 2 — Spectra at work: power iteration and PageRank

## Status

Core A is completed and executed, with outputs saved. Core B is still
unimplemented. The supplied random seeds are preserved. Extensions were skipped.

## Team

- **Vladyslav Hryhola** — Core A: Power iteration and inverse iteration
- **Ihor Kashuba**

## Work split

### Core A — Vladyslav Hryhola

Implemented and investigated:

- power iteration with a residual-based stopping rule;
- convergence-rate predictions and measured eigenvector and eigenvalue errors;
- the effect of an ill-conditioned eigenvector matrix;
- four cases where power iteration fails or converges slowly;
- inverse iteration with a shift and one reused LU factorization;
- all ten eigenpairs of the test matrix;
- convergence rates for different shifts;
- a shift very close to an eigenvalue and the effect of normalization.

### Core B — unassigned

Not yet implemented.

## Extensions

No optional extension was attempted.

## Environment and startup

Use the shared Python 3.12+ environment described in the [root README](../../README.md).
From the repository root:

```sh
.venv/bin/python -m pip install -r requirements.txt
cd labs/lab2
../../.venv/bin/python -m jupyter lab
```

Choose **Python (.venv: linear-algebra-ucu)** as the notebook kernel.
Dependencies include NumPy, SciPy, Matplotlib, and NetworkX 3.x. No external data
files are required; the notebooks define or generate their inputs.

## Files

- `lab2-coreA-power_iteration.ipynb` — Core A and extensions 1–2
- `lab2-coreB-pagerank.ipynb` — Core B and extension 3
- [lab2-description.md](lab2-description.md) — assignment and submission requirements

## Reproducibility and unfinished work

Core A runs from top to bottom in a fresh kernel, with its outputs saved.
Its printed versions are Python 3.14.6, NumPy 2.5.3, SciPy 1.18.1 and
Matplotlib 3.11.2. Iteration counts and last digits may differ across machines.
No unfinished Core A tasks are known; extensions were not attempted.

Core B remains unfinished and has not been verified. Before submitting the whole
lab, complete Core B, record its printed versions (including NetworkX), fill in
the Core B contribution, and run both notebooks from clean kernels.
