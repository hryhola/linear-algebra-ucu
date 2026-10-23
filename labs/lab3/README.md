# Lab 3 — Positive definite matrices at work: Gaussians and kernel ridge

## Status

Both notebooks are supplied starters, unimplemented and unexecuted. The lab is
not completed. No extension has been attempted.

## Team

- **Vladyslav Hryhola**
- **Ihor Kashuba**

## Work split

### Core A — The Gaussian, computed

Not started. Contribution to be recorded when completed.

### Core B — Kernel ridge regression

Not started. Contribution to be recorded when completed.

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

Both notebook files passed notebook-format validation. The existing environment
passed `pip check`. Installed versions at the setup check were Python 3.14.6,
NumPy 2.5.3, SciPy 1.18.1, pandas 3.0.6, Matplotlib 3.11.2, and scikit-learn
1.9.1. These are environment-check versions, not saved notebook outputs.

Both notebooks' initial import/version cells passed in fresh
`linear-algebra-ucu` kernels using temporary copies; the notebook files were not
modified. All lab tasks, written answers, and notebook team fields remain
unfinished. Neither notebook has been run from top to bottom. Do not use Run All
until the required tasks are implemented.

Before submission, complete both cores, record each member's contribution and
the versions printed by the notebooks (including scikit-learn), preserve the
supplied seeds, and restart and run both notebooks from clean kernels. Save all
outputs and update this README with the verified status and any remaining issues.
