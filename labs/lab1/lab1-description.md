**Lab 1 — Least squares, conditioning, and the Fourier basis**  
_Module 2. Released Monday, 21 September 2026_

**Due**

**Thursday 1 October 2026, 23:59**

**Defences**

Week of Monday 5 to Friday 9 October, scheduled per team (20 min); oral, individual, both members present (online)

**Teams**

2 students

**Points**

up to 6 (2 + 2 + 1 + up to 1)

**Late days**

Up to 5 of your 10, declared at submission

**Submit**

Two ipynb notebooks + readme file in Moodle (or github repository) per team

  
**What this lab is for**

Module 2 argued that a correct formula is not an algorithm, and that choosing a good basis is most of what numerical linear algebra does. This lab is where both claims stop being claims.

You will fit a model to 166 years of temperature data and watch two mathematically identical solvers disagree by nearly ten orders of magnitude. Then you will hand the same signal to a basis that was not designed for it, and find that it locates the structure you had to supply by hand the first time. Two cores, one dataset, two lenses.

  
**Core A — Least squares, conditioning, and QR**  
_Notebook: `lab1-coreA-least_squares.ipynb`_

You implement least squares in three ways: through the normal equation, QR with your own back substitution, and `lstsq` as a trusted reference, and then fit a trend-plus-seasonality model and raise the polynomial degree until the fit improves. The second half is about why different approaches yield different answers, which to believe, and a one-line change that turns the problem from hopeless to routine.

**You will need** the normal equation and its QR form (Module 1.2, [Tutorial 1.2](https://learn.ucu.edu.ua/mod/assign/view.php?id=148573 "Tutorial 1.2")), condition numbers and the argument 𝜅⁡(𝐴⊤⁢𝐴) \=𝜅⁡(𝐴)2 (Module 2.1), and residual orthogonality (Module 1.1).

  
**Core B — The DFT as a change of basis**  
_Notebook: `lab1-coreB-fourier.ipynb`_

You build the Fourier matrix, verify that it is unitary, transform the series and read its period off the coordinates. Then the standard FFT, implemented and timed against the matrix form, and finally coefficient thresholding — used once for compression and once for denoising, with the same three lines of code.

**You will need** orthonormal bases and Parseval's identity (Module 1.1), unitary matrices (Module 2.1), and the DFT (Module 2.2, [Tutorial 2](https://learn.ucu.edu.ua/mod/assign/view.php?id=150009 "Tutorial 2")).

  
**Extensions**  
_Attempt at most one seriously. A second adds nothing to your mark, and a shallow attempt at one costs you the point. In the notebooks the extensions are marked with a star and placed at the end of the core each builds on: Extensions 1 and 2 at the end of Core A, Extension 3 at the end of Core B._

1.  **Weighted least squares on the full record.** A second data file, supplied with the lab, runs back to 1750 and adds each month's uncertainty, which is many times larger in the early record. Ordinary least squares assumes every observation is equally trustworthy. Refit with 𝑊 \=diag⁡(1/𝜎2) and report what changes — including what you had to do about the twelve missing months, and why the choice matters.
2.  **Minimum-norm and ridge on a rank-deficient design.** Add a column to your design matrix that is an exact linear combination of others. The normal equation now has no unique solution. Compare what `lstsq` returns with what ridge returns as the penalty goes to zero, and explain the relationship.
3.  **DCT against DFT.** The DCT is the workhorse of image and audio compression, and the usual claim is that its coefficients decay faster than the DFT's. Test it on the full series and on the residual left after removing the annual cycle. The claim holds for only one of the two; find which, and explain why.

**What to submit**

One submission per team here in Moodle or one git repository, containing:

*   **Both notebooks, with all cells executed and outputs saved.** The defence starts from your numbers. A blank notebook means the assistant must run it, and that means extra waste of time.
*   **`README.md`** — team members, who did what, the numpy and pandas versions your notebooks print, which extension you attempted, and anything you know to be broken or unfinished.
*   Any extra scripts or data you used.

**Before you submit, run _Restart & Run All_.** A notebook whose cells were executed out of order can display results that no fresh run reproduces, and that is the most common cause of a defence going badly. State in your `README` that the notebooks run top to bottom from a clean kernel.

Do not submit PDFs; the assistant will want to make changes and rerun it.

Saying plainly that something does not work is worth marks. A team that writes _“our back substitution fails when R is near-singular and we did not fix it”_ is doing better science than one that hides it.

  
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

More points are available across the five labs than are credited, so one weak lab need not cost you anything.

  
**The defence**

Oral and individual. **Both members must be able to explain any part of the submission, including sections** they did not write. The assistant will ask you to interpret a number, to say why a step was taken, and in at least one case to change something and predict the outcome before running it.

Divide the _work_ however suits you — that is what a team is for, and the `README` should say who did what. Do not divide the _understanding_. Before you submit, walk each other through the parts you did not write until both of you could defend them alone. Teams that skip this step are the ones that lose marks, and they lose them on the half of the lab they were confident about.

Work you cannot explain does not receive credit.

  
**Deadlines and late days**

You have **10 late days in total** across the five labs, of which you may spend **up to 5 on this one**. Declare them at submission. Beyond that the standard penalty applies: 25% up to a week late, 50% from one to two weeks, and normally nothing accepted after that.

  
**AI assistants**

You may use them to help you learn. The defence is oral and individual, and you are expected to explain every line you submit. In practice: use them the way you would use a textbook or a classmate, and do not submit anything you could not reconstruct on a whiteboard.

**The data**

[`land-temp-1850-2015.csv`]([TBD - data file link]) — 1992 monthly readings, January 1850 to December 2015, no gaps.

This is the `LandAverageTemperature` column of `GlobalTemperatures.csv` from Berkeley Earth's _Climate Change: Earth Surface Temperature Data_, distributed on [Kaggle](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) under CC BY-NC-SA 4.0. It is a **global land average** built from roughly 1.6 billion station reports — not a city, not a country, and not a place you can say anything local about.

The original series begins in 1750. We use it from 1850 because the earlier portion has twelve missing months scattered through 1750–52 and much larger stated uncertainties. Core B needs uniform monthly spacing absolutely: a transform has no way to represent a month that is not there.

Extension 1 uses a second supplied file, [`land-temp-1750-2015-with-uncertainty.csv`]([TBD - extension data file link]): the same series from January 1750, with a third column giving each month's 95% uncertainty. The twelve missing months are left in as blanks, and from 1850 on the temperatures are identical to the core file.

**Environment**

Any recent Python 3 with `numpy`, `pandas` and `matplotlib`. Both notebooks print their versions; keep that output. The last digits in Core A §3 depend on the LAPACK build behind your numpy, so two correct submissions can differ slightly — say so rather than tuning until the numbers match someone else's.

  
**Materials**

*   [Core A notebook](https://drive.google.com/file/d/1YTWt-4MUWngnj4bwW3YTJ_dVXgFVRt38/view?usp=sharing) (`lab1-coreA-least_squares.ipynb`)
*   [Core B notebook](https://drive.google.com/file/d/1ZW3Sxfvz7MICMLq37vs2RpQToZhSTolP/view?usp=sharing) (`lab1-coreB-fourier.ipynb`)
*   [Data file](https://drive.google.com/file/d/1uw7PJrWZ1rxmk5y4hth7WDzaYbNlgMwL/view?usp=sharing) (`land-temp-1850-2015.csv`)
*   [Extension 1 data file](https://drive.google.com/file/d/17HYciPuRhwvM8nAzCTyn-rALcw5YC42O/view?usp=sharing) (`land-temp-1750-2015-with-uncertainty.csv`

  
**Questions**

Ask in the course Slack channel rather than by direct message: if one team is stuck on something, others are too. Useful questions and useful answers both earn QA participation credit.
