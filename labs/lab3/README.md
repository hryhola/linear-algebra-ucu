# Lab 3 — Positive definite matrices at work: Gaussians and kernel ridge

## Team and contributions

- **Vladyslav Hryhola** — Core A: implementation, predictions, written answers and verification.
- **Ihor Kashuba** — Core B and Extension E3: implementation, predictions, written answers and verification.

AI assistants were used as a study aid during learning and review.

## Completion and reproducibility

- Core A (A1–A3) and Core B (B1–B4) are complete, with outputs saved.
- Both notebooks run top to bottom from a clean kernel.
- **Extension attempted:** E3 — Gaussian-process regression is kernel ridge, completed in Notebook B. E1 and E2 are unattempted.
- **Late days used:** 0.

## Library versions printed in the saved notebooks

| Library | Core A | Core B |
|---|---|---|
| NumPy | 2.5.3 | 2.1.3 |
| SciPy | 1.18.1 | 1.16.3 |
| pandas | 3.0.6 | Not used or printed |
| scikit-learn | 1.9.1 | 1.6.1 |

## Known limitations and unfinished work

- A2(c): the original prediction was qualitative; the numerical underflow thresholds were calculated afterward and are included in the answer.
- No known execution failures in the completed sections. Timings and results for severely ill-conditioned matrices can differ between environments.
