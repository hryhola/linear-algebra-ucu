**Lab 2 — Spectra at work: power iteration and PageRank**  
_Module 3. Released Saturday, 3 October 2026_

**Due**

**Thursday 15 October 2026, 23:59**

**Defences**

Week of Monday 19 to Friday 23 October, scheduled per team (20 min); oral, individual, both members present (online)

**Teams**

2 students

**Points**

up to 6 (2 + 2 + 1 + up to 1)

**Late days**

Up to 5 of your 10, declared at submission

**Submit**

Two ipynb notebooks + readme file in Moodle (or github repository) per team

  
**What this lab is for**

Module 3 claimed that the eigenvalues of a matrix tell you how its powers behave, and that you can find the eigenvector that matters using nothing but matrix-vector products. This lab is where both claims stop being claims.

You will predict how many iterations an algorithm needs before running it, and then watch it take almost exactly that many. You will break it in four different ways and explain each failure from the spectrum. Then you will rank 100 000 web pages with the same algorithm, on a matrix that would need 80 GB to store and that you therefore never form. Two cores, one algorithm, two uses.

  
**Core A — Power iteration and inverse iteration**  
_Notebook: `lab2-coreA-power_iteration.ipynb`_

You implement power iteration with a residual-based stopping rule, predict its convergence rate from |𝜆2/𝜆1| and measure it, and find out what changes when the eigenvector matrix is badly conditioned. You then construct four matrices on which the method fails or crawls, and explain what you see. The second half is inverse iteration with a shift: one LU factorisation reused at every step, all ten eigenvalues of a test matrix, and a shift so close to an eigenvalue that the system is hopelessly ill conditioned — and yet the answer comes out right in two steps.

**You will need** diagonalisation and 𝐴𝑛 \=𝑃⁢𝐷𝑛⁢𝑃−1, the Jordan asymptotics 𝑛𝑘⁢|𝜆|𝑛, and the role of 𝜅⁡(𝑃) (Module 3.1); power iteration and inverse iteration (Module 3.2); LU factorisation (Module 0).

  
**Core B — Markov chains and PageRank**  
_Notebook: `lab2-coreB-pagerank.ipynb`_

You build the random-surfer model, watch probability leak out through dead-end pages, and repair it. Three small graphs then break the naive iteration in three different ways, and the eigenvalues of each explain why. Damping fixes all three at once; you prove how fast the repaired iteration must converge, measure how fast it actually does, and find out when the bound is sharp. Finally you run PageRank matrix-free on a graph with 105 pages and compare the ranking with a simple count of in-links.

**You will need** stochastic matrices, Perron–Frobenius, and PageRank with damping (Module 3.2). Your `power_method` from Core A is the same algorithm; here it gets a matrix-free form.

  
**Extensions**  
_Attempt at most one seriously. A second adds nothing to your mark, and a shallow attempt at one costs you the point. In the notebooks the extensions are marked with a star and placed at the end of the core each builds on: Extensions 1 and 2 at the end of Core A, Extension 3 at the end of Core B. End your extension with a short paragraph headed _Finding_._

1.  **The QR algorithm.** What `numpy.linalg.eig` builds on. Implement the unshifted QR iteration, predict its iteration count from the eigenvalue ratios, then add shifts and deflation and count again. Record how fast the last subdiagonal entry dies, and find out what the method does with a complex pair of eigenvalues.
2.  **Stable, yet it grows.** An iterated map whose eigenvalues are all inside the unit circle must tend to zero, but nothing says it must get there directly. Find a 2 ×2 matrix whose powers grow fifty-fold before they decay, explain the peak from a closed form, and then find a 20 ×20 one whose powers reach 1018. Say why the bound from Module 3.1 is useless for it.
3.  **A random walk on a ring.** The lazy random walk on a cycle is a circulant, so the Fourier basis of Module 2 diagonalises it without any computation. Use that to predict how the time needed to reach equilibrium grows with the length of the ring, test the prediction, explain why the walk has to be lazy, and time the FFT matrix-vector product against the dense one up to 𝑛 \=220.

**What to submit**

One submission per team here in Moodle or one git repository, containing:

*   **Both notebooks, with all cells executed and outputs saved.** The defence starts from your numbers. A blank notebook means the assistant must run it, and that means extra waste of time.
*   **`README.md`** — team members, who did what, the numpy, scipy and networkx versions your notebooks print, which extension you attempted, and anything you know to be broken or unfinished.
*   Any extra scripts you used.

**Before you submit, run _Restart & Run All_.** A notebook whose cells were executed out of order can display results that no fresh run reproduces, and that is the most common cause of a defence going badly. State in your `README` that the notebooks run top to bottom from a clean kernel. Do not change the random seeds: the defence uses your numbers.

Do not submit PDFs; the assistant will want to make changes and rerun it.

Saying plainly that something does not work is worth marks. A team that writes _“our shifted QR stalls on the complex pair and we do not know why”_ is doing better science than one that hides it.

  
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

The code point also requires the rules stated at the top of each notebook. In short: the functions you implement must not call `np.linalg.eig`, `eigvals` or anything built on them (you may use these elsewhere to _check_ results); nothing in the lab calls `np.linalg.inv`; and `networkx` is used only where the Core B notebook says so.

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

There are no data files to download. All test matrices and small graphs are defined in the notebooks. The large graph in Core B §5 (about 100 900 pages and 194 000 links) is generated by `networkx` from a fixed seed: a standard model of web-like graphs with a few very popular pages, plus 300 small groups of pages that link only among themselves, as many sites on the real web do.

Different `networkx` versions may generate a slightly different graph from the same seed. That is fine: the assistant checks your numbers against the versions your notebook prints.

**Environment**

Any recent Python 3 with `numpy`, `scipy`, `matplotlib` and `networkx` 3.x; Google Colab works out of the box. The largest computation takes a few seconds and well under 1 GB of memory. Both notebooks print their versions; keep that output. Iteration counts and last digits can differ slightly between machines — say so rather than tuning until the numbers match someone else's.

  
**Materials**

*   [Core A notebook](https://drive.google.com/file/d/1EJYoHZP5GU7BkFHaGTmN9Dfy_PJPYdLK/view?usp=sharing) (`lab2-coreA-power_iteration.ipynb`)
*   [Core B notebook](https://drive.google.com/file/d/1NlxAlvuXvJ5RoPX0hIe3cpV6r0Ubeyfy/view?usp=sharing) (`lab2-coreB-pagerank.ipynb`)

  
**Questions**

Ask in the course Slack channel rather than by direct message: if one team is stuck on something, others are too. Both useful questions and useful answers earn QA participation credit.

* * *