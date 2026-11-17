# Lab 4 — Low rank at work: filtering the spectrum and aligning point clouds

## Team and contributions

- **Vladyslav Hryhola** — Core A and Extension E1.
- **Ihor Kashuba** — Core B.

AI assistants were used as a study aid during learning and code review.

## Completion and reproducibility

- Core A (A1–A3), Core B (B1–B3) and Extension E1 are implemented, with written answers and saved outputs.
- Core A including E1, and the required B1–B3 sections, run top to bottom from a clean kernel.
- **Extension attempted:** E1 — Generalised cross-validation, in Notebook A. E2 is unattempted.
- **Late days used:** 1.

## Library versions printed in the saved notebooks

| Library | Core A | Core B |
|---|---|---|
| NumPy | 2.5.3 | 2.4.6 |
| SciPy | 1.18.1 | 1.16.3 |
| Matplotlib | 3.11.2 | 3.10.0 |
| scikit-learn | 1.9.1 | Not used |

## Known limitations and unfinished work

- Core B's unattempted E2 contains `NotImplementedError` placeholders; running the entire notebook stops there. B1–B3 run without errors.
- Timings and results for the ill-conditioned naive inverse can differ between environments.
