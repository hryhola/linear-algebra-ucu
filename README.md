# Linear algebra

Course materials are organized into separate directories:

- `labs/` for laboratory work
- `workshops/` for workshop exercises

## Environment setup

The project requires Python 3.12 or newer. Create one virtual environment at the
repository root and install all dependencies into it:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --sys-prefix --name linear-algebra-ucu --display-name "Python (.venv: linear-algebra-ucu)"
```

On each new terminal session, activate the existing environment before running
project files:

```sh
source .venv/bin/activate
```

The environment includes NumPy, SciPy, Pandas, Matplotlib, JupyterLab, and the
Jupyter Python kernel. The `.venv/` directory is local and is not committed.

## Workshop 2 Python script

From the repository root, run:

```sh
python workshops/workshop2/tutorial-2-result.py
```

This prints the pivoted QR diagonal and singular values for the perturbed matrix.

## Lab 1 notebooks

The notebooks read files through paths relative to `labs/lab1`, so start
JupyterLab from that directory:

```sh
cd labs/lab1
../../.venv/bin/python -m jupyter lab
```

Open either notebook in the JupyterLab browser interface:

- `lab1-coreA-least_squares.ipynb` — least squares and QR
- `lab1-coreB-fourier.ipynb` — discrete Fourier transform

Choose **Python (.venv: linear-algebra-ucu)** if Jupyter asks for a kernel. The
notebooks are already configured to request this kernel. These are exercise
notebooks with unfinished `...` sections; complete the requested code before
using **Run All**.
