* * *

**Lab 4 — Low rank at work: filtering the spectrum and aligning point clouds**  
_Module 5. Released Saturday 31 October_

**Due**

**Thursday 16 November, 23:59**

**Defences**

**17-20 Nov**, scheduled per team (20 min); oral, individual, both members present (online)

**Teams**

2 students

**Points**

up to 6 (2 + 2 + 1 + up to 1)

**Late days**

Up to 5 of your 10, declared at submission

**Submit**

Two ipynb notebooks + readme file in Moodle per team

  
**What this lab is for**

Lecture 5.2 claimed that one factorisation, the SVD, answers almost every question we can ask about a matrix, and that each answer is read off the singular values. This lab tests that claim with two problems that look nothing alike: cleaning up an image and putting two 3-D scans of an object into a single coordinate system.

You will predict, from the singular values alone and before computing anything, how much an image loses when it is compressed. You will remove noise by deciding which singular values to trust, and undo a blur with a matrix you are not allowed to build, because it would need about 600 GB of memory. You will watch an exact inverse do worse than doing nothing. Then you will align two point clouds with one 3×3 SVD, see that SVD return a mirror image that fits the data _better_ than the truth, and build the iterative closest point algorithm, which aligns two scans when nobody tells you which point is which. Two cores, one factorisation.

  
**Core A — Filtering the spectrum**  
_Notebook: `Lab4-CoreA-spectrum-filtering.ipynb`_

You compress a greyscale photograph by truncating its SVD and check that the error of every truncation is known in advance (Eckart–Young). You find out how far from “low rank” a real photograph is, and compare the SVD with a competitor that keeps the image's actual columns. You add noise, predict its size from a formula, and compare a rank chosen by a threshold with the best possible rank and with a smooth filter. The last part blurs the image with a periodic Gaussian kernel: the blur is a circulant matrix, so its SVD costs one FFT. You compute its condition number, see why the exact inverse is worthless even without noise, and choose the regularisation parameter without knowing the true image.

**You will need** the SVD, Eckart–Young, truncated SVD and filter factors (Lecture 5.2); circulant matrices and the Fourier basis (Lecture 3.2); ridge regression (Module 1).

  
**Core B — Aligning point clouds**  
_Notebook: `Lab4-CoreB-alignment.ipynb`_

You implement orthogonal Procrustes from one SVD and recover a planted motion of a 3-D object, check the minimum-value formula from the lecture, and find out what happens if you forget to centre, or apply the rotation in the wrong convention. You register the object by six markers on a nearly flat plate, get a reflection instead of a rotation, and fix it with the Kabsch rule, predicting its cost before you measure it. Finally, you build the iterative closest point algorithm (ICP): you map its basin of attraction, give it a better start with PCA, make it survive a partial scan with stray points, and measure where its time goes.

**You will need** the SVD, orthogonal Procrustes and the Kabsch fix (Lecture 5.2); the reduction of Procrustes to a trace (Lecture 2.2); PCA (Lecture 5.1). [Tutorial 5.2](https://learn.ucu.edu.ua/mod/assign/view.php?id=155892 "Tutorial 5.2") proves the Procrustes formula you use here.

  
**Extensions**  
_Attempt at most one seriously. A second adds nothing to your mark, and a shallow attempt at one costs you the point. In the notebooks the extensions are placed at the end of the core each builds on: Extension 1 at the end of Core A, Extension 2 at the end of Core B. End your extension with a short paragraph headed _Finding_._

1.  **Choosing the regularisation parameter when the noise level is unknown.** The discrepancy principle in Core A needs the noise level. Generalised cross-validation does not. Show that the influence matrix of the deblurring problem is diagonal in the Fourier basis, implement GCV, and compare its choice with the oracle and with the discrepancy principle. Then find out why it estimates the noise level almost perfectly and still chooses badly. This topic was not lectured; the notebook gives the introduction you need.
2.  **Shape from a moving camera (Tomasi–Kanade).** A camera circles an object and tracks 300 points through 15 views. Show that the matrix of image coordinates has rank 3, recover the camera motion and the 3-D shape from its SVD up to an unknown linear distortion, and remove the distortion with a small linear system and a Cholesky factorization. Then find out why the data cannot tell the object from its mirror image. This topic was not lectured; the notebook gives the introduction you need.

**What to submit**

One submission per team here in Moodle, containing:

*   **Both notebooks, with all cells executed and outputs saved.** The defence starts from your numbers. A blank notebook means the assistant must run it, and that means extra waste of time.
*   **`README.md`** — team members, who did what, the numpy, scipy, matplotlib and scikit-learn versions your notebooks print, which extension you attempted, and anything you know to be broken or unfinished.
*   Any extra scripts you used.

**Before you submit, run _Restart & Run All_.** A notebook whose cells were executed out of order can display results that no fresh run reproduces, and that is the most common cause of a defence going badly. State in your `README` that the notebooks run top to bottom from a clean kernel. Do not change the random seeds: the defence uses your numbers.

Do not submit PDFs; the assistant will want to make changes and rerun it.

Saying plainly that something does not work is worth marks. A team that writes _“our ICP converges from 120 degrees for some axes and not for others, and we do not know why”_ is doing better science than one that hides it.

  
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

The code point also requires the rules stated at the top of each notebook. In short: nothing anywhere calls `np.linalg.inv` or `np.linalg.pinv`; in Core A the blur matrix of the image is never formed (the only explicit circulant is the small one-dimensional matrix in A3(a)), and `scipy.linalg.circulant` is used only where a cell says _check_; in Core B every rotation comes from `np.linalg.svd` of a 3×3 matrix, nearest neighbours come from `scipy.spatial.cKDTree`, and `scipy.linalg.orthogonal_procrustes` and `scipy.spatial.transform.Rotation` are used only where a cell says _check_.

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

There are no data files to download. Everything is loaded or generated inside the notebooks:

*   **A photograph of a flower** (Core A, Extension 1): `flower.jpg`, bundled with scikit-learn, converted to a 427 × 640 greyscale matrix. The noise and the blur are added from fixed seeds.
*   **A synthetic 3-D “fish”** (Core B, Extension 2): points on the surface of an asymmetric object with a body, a fin and a bent tail, generated by a function in the first cell. Scans, markers and camera views are generated from fixed seeds.

**Environment**

Any recent Python 3 with `numpy`, `scipy`, `matplotlib` and `scikit-learn`; Google Colab works out of the box. Each solved notebook runs top to bottom in well under a minute on a laptop (about 15 s for Core A and 25 s for Core B on ours). Both notebooks print their versions; keep that output. Timings, and last digits of quantities near rounding level, differ between machines. Say so rather than tuning until the numbers match someone else's.

  
**Materials**

*   [Core A notebook](https://drive.google.com/file/d/1QuNyJ94fq_eu9wcfX_8IvCrwwMnYtzCo/view?usp=drive_link) (`Lab4-CoreA-spectrum-filtering.ipynb`)
*   [Core B notebook](https://drive.google.com/file/d/10O5x3AW9QF3gx7rS7cdaxVS25H2hg2P_/view?usp=drive_link) (`Lab4-CoreB-alignment.ipynb`)

  
**Questions**

Ask in the course Slack channel rather than by direct message: if one team is stuck on something, others are too. Useful questions and useful answers both earn QA participation credit.

* * *

**Умови завершення:**

*   Зробити: Здайте роботу
