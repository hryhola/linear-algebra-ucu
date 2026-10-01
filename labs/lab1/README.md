# Lab 1 — Least Squares, Conditioning, and the Fourier Basis

## Team

- **Vladyslav Hryhola** — Core A: Least squares, conditioning, and QR
- **Ihor Kashuba** — Core B: The DFT as a change of basis

## Environment

- Python 3
- NumPy: `2.5.3`
- pandas: `3.0.6`
- matplotlib

## Work split

### Core A — Vladyslav Hryhola

Implemented and investigated:

- least squares via the normal equations;
- least squares via reduced QR factorization;
- manual back substitution for the upper-triangular system;
- `np.linalg.lstsq` as the reference solver;
- residual orthogonality and the Pythagorean relation;
- trend + seasonal design matrices;
- linear temperature trend and annual seasonality;
- conditioning as polynomial degree increases;
- comparison of the normal-equation and QR solutions;
- rescaling the time variable to improve conditioning;
- comparison of coefficient accuracy and prediction accuracy.

### Core B — Ihor Kashuba

Implemented and investigated:

* the unitary Fourier matrix using numpy broadcasting;
* matrix-based Discrete Fourier Transform (DFT) and its inverse;
* verification of matrix unitarity, perfect conditioning, and Parseval's identity;
* extraction of the annual period and harmonics from the power spectrum;
* radix-2 recursive Fast Fourier Transform (FFT) algorithm;
* asymptotic complexity and performance comparison (Matrix DFT vs. recursive FFT vs. `np.fft.fft`);
* frequency-domain coordinate thresholding;
* signal compression and energy retention analysis;
* signal denoising and optimal RMSE evaluation against a noisy baseline.

## Extensions

No optional extension was attempted.

## Known issues / unfinished work

No known issues in Core A.

Core B implementation and saved outputs are included.

## Reproducibility

Both notebooks have saved outputs. Before submission, restart and run both notebooks from top to bottom from a clean kernel and save all outputs.

## Files

- `lab1-coreA-least_squares.ipynb`
- `lab1-coreB-fourier.ipynb`
- `data/land-temp-1850-2015.csv`
