* * *

**Lab 3 — Positive definite matrices at work: Gaussians and kernel ridge**  
_Module 4. Released 17 October 2026_

**Due**

**29 Oct 2026, 23:59**

**Defences**

02-06 Nov 2026, scheduled per team (20 min); oral, individual, both members present (online)

**Teams**

2 students

**Points**

up to 6 (2 + 2 + 1 + up to 1)

**Late days**

Up to 5 of your 10, declared at submission

**Submit**

Two ipynb notebooks + a readme file in Moodle per team

  
**What this lab is for**

Module 4 claimed that one property, positive definiteness, sits under covariance, the Gaussian, kernels and much else, and that one factorization, Cholesky, computes everything those objects need. This lab is where that claim gets tested on real numbers.

You will whiten real medical data three ways and find out which one moves the data least. You will predict, before running it, the exact dimension at which `np.linalg.det` returns zero for a perfectly healthy covariance matrix, and then compute the same quantity with no trouble at all. You will fit a regression in a feature space you never construct, check that it agrees with the explicit one to the last digit, and watch the ridge parameter decide whether the answer can be trusted. Two cores, one factorization, two uses.

  
**Core A — The Gaussian, computed**  
_Notebook: `Lab3-CoreA-gaussian.ipynb`_

You build the sample covariance of 569 breast tumours with 30 features, and find out how much of its terrible conditioning is just the units. You whiten the data with the Cholesky factor, the eigenvectors and the symmetric square root, check that all three give the same Mahalanobis distances, and find the most unusual tumours. You then shrink the sample until there are barely more tumours than features, and see what whitening does to directions that are mostly noise, and what shrinkage does about it. The second half evaluates the Gaussian log-density with one Cholesky factorization and one triangular solve, races it against the naive formula with `det` and `inv`, and samples from a Gaussian, including one whose covariance is singular and has no Cholesky factor at all.

**You will need** the spectral theorem, the matrix square root and the Cholesky factorization (Module 4.1); covariance, whitening, the Mahalanobis distance and the Gaussian computed from _L_ (Module 4.2).

  
**Core B — Kernel ridge regression**  
_Notebook: `Lab3-CoreB-kernel-ridge.ipynb`_

You implement kernel ridge regression with one Cholesky factorization and check it against scikit-learn. For a polynomial kernel you write out the feature map by hand, fit ordinary ridge regression on it, and show that the two routes give the same predictions, and that one of them becomes hopeless as the degree grows. With the Gaussian kernel you look at the spectrum of the kernel matrix, find a case where Cholesky fails on a matrix that is positive semidefinite in exact arithmetic, and find out why a tiny shift that "fixes" it is not a fix at all. You predict the condition number of _K_ + λ_I_ from the eigenvalues alone, choose λ by validation, and measure how the cost grows with the number of points.

**You will need** kernels, the representer theorem and kernel ridge (Module 4.2); Cholesky (Module 4.1); ridge regression (Module 1).

  
**Extensions**  
_Attempt at most one seriously. A second adds nothing to your mark, and a shallow attempt at one costs you the point. In the notebooks the extensions are placed at the end of the core each builds on: Extensions 1 and 2 at the end of Core A, Extension 3 at the end of Core B. End your extension with a short paragraph headed _Finding_._

1.  **Repairing a correlation matrix.** Correlations computed from data with missing values are often not positive semidefinite, and then everything downstream breaks. Delete 10% of the breast cancer data, see the damage, and prove which PSD matrix is nearest to the broken one. Then find the nearest _correlation_ matrix with Higham's alternating projections, and find out what Dykstra's correction is for. This topic was not lectured; the notebook gives the introduction you need.
2.  **Fisher's discriminant.** Separate three wine cultivars by solving a generalised eigenproblem in two ways, one symmetric and one not. Then add a feature that is an almost exact copy of another, and find the point at which the arithmetic loses the information, and why it is exactly there.
3.  **Gaussian-process regression is kernel ridge.** Show, with the conditional-Gaussian formula of Module 4.2, that the posterior mean of a Gaussian process is the kernel ridge prediction. Then compute the error bars from the same Cholesky factor, and explain where they are wide, using the Schur complement.

**What to submit**

One submission per team here in Moodle or one git repository, containing:

*   **Both notebooks, with all cells executed and outputs saved.** The defence starts from your numbers. A blank notebook means the assistant must run it, and that means extra waste of time.
*   **`README.md`** — team members, who did what, the numpy, scipy, pandas and scikit-learn versions your notebooks print, which extension you attempted, and anything you know to be broken or unfinished.
*   Any extra scripts you used.

**Before you submit, run _Restart & Run All_.** A notebook whose cells were executed out of order can display results that no fresh run reproduces, and that is the most common cause of a defence going badly. State in your `README` that the notebooks run top to bottom from a clean kernel. Do not change the random seeds: the defence uses your numbers.

Do not submit PDFs; the assistant will want to make changes and rerun it.

Saying plainly that something does not work is worth marks. A team that writes _“our alternating projections converge, but not to the same matrix as Higham's, and we do not know why”_ is doing better science than one that hides it.

  
**Marking**

Core A, at defence

2

Core B, at defence

2

Code — runs, reproducible, readable

1

Extension, at the defence

up to 1

  
The **code point** is for work an assistant can run and read: a clean run from a fresh kernel, functions that do what their docstrings say, no dead cells, and no hard-coded numbers that should have been computed. It is not a style prize, and it is not awarded for length.

The code point also requires the rules stated at the top of each notebook. In short: nothing in the functions you implement calls `np.linalg.inv` or `np.linalg.det` (the one exception is the naive log-density in Core A, which exists to be compared); and `scipy.stats.multivariate_normal`, scikit-learn's `KernelRidge` and `GaussianProcessRegressor` are used only where a cell says _check_.

More points are available across the five labs than are credited, so one weak lab need not cost you anything.

  
**The defence**

Oral and individual. **Both members must be able to explain any part of the submission, including sections** they did not write. The assistant will ask you to interpret a number, to say why a step was taken, and in at least one case to change something and predict the outcome before running it.

Divide the _work_ however suits you — that is what a team is for, and the `README` should say who did what. Do not divide the _understanding_. Before you submit, walk each other through the parts you did not write until both of you could defend them alone. Teams that skip this step are the ones that lose marks, and they lose them on the half of the lab they were confident about.

Work you cannot explain does not receive credit.

  
**Deadlines and late days**

You have **10 late days in total** across the five labs, of which you may spend **up to 5 on this one**. Declare them at submission. Beyond that the standard penalty applies: 25% up to a week late, 50% from one to two weeks, and normally nothing accepted after that.

  
**AI assistants**

You may use them to help you learn. The defence is oral and individual, and you are expected to explain every line you submit. In practice: use them the way you would use a textbook or a classmate, and do not submit anything you could not reconstruct on a whiteboard.

**The data**

There are no data files to download. All data sets come with scikit-learn and are loaded inside the notebooks:

*   **Breast cancer** (Core A, Extension 1): 569 tumours, 30 measurements of the cell nuclei in very different units.
*   **Friedman #1** (Core B): a standard synthetic regression benchmark with ten features, of which five matter, through a nonlinear formula that a linear model cannot capture. It is generated from a fixed seed.
*   **Wine** (Extension 2): 178 wines from three cultivars, 13 chemical measurements.

The other matrices (an AR(1) covariance, a small one-dimensional data set with a gap) are defined in the notebooks.

**Environment**

Any recent Python 3 with `numpy`, `scipy`, `pandas`, `matplotlib` and `scikit-learn`; Google Colab works out of the box. Most cells run in well under a second. The largest computation, the timing in Core B §4 at 8000 points, takes a few seconds and needs about 2 GB of memory. Both notebooks print their versions; keep that output. Timings, and last digits of quantities near rounding level, differ between machines. Say so rather than tuning until the numbers match someone else's.

  
**Materials**

*   [Core A notebook](https://drive.google.com/file/d/1hocRe0c2clyqTpKXqSwU60-_OL_K72wA/view?usp=drive_link) (`Lab3-CoreA-gaussian.ipynb`)
*   [Core B notebook](https://drive.google.com/file/d/1DOVdFXrzadRXnXUxtmrVemFuQ2VqLkOZ/view?usp=drive_link) (`Lab3-CoreB-kernel-ridge.ipynb`)

  
**Questions**

Ask in the course Slack channel rather than by direct message: if one team is stuck on something, others are too. Useful questions and useful answers both earn QA participation credit.

* * *