import numpy as np
from scipy.linalg import qr

A = np.array([
    [1., 2., 3.],
    [1., 3., 4.],
    [1., 4., 5.],
    [1., 5., 6.],
])

# Fixed random matrix
rng = np.random.default_rng(0)
N = rng.standard_normal(A.shape)

# Make N have unit Frobenius norm
N = N / np.linalg.norm(N)

# eta = 1e-10
# A_eta = A + eta * N

# Q, R, P = qr(A_eta, pivoting=True)

# print("Permutation:", P)
# print("diag(R):", np.diag(R))
# print("| diag(R) |:", np.abs(np.diag(R)))

# singular_values = np.linalg.svd(A_eta, compute_uv=False)

# print("Singular values:", singular_values)
eta = 1e-2
A_eta_2 = A + eta * N

Q2, R2, P2 = qr(A_eta_2, pivoting=True)
singular_values_2 = np.linalg.svd(A_eta_2, compute_uv=False)

print("|diag(R)|:", np.abs(np.diag(R2)))
print("Singular values:", singular_values_2)