import numpy as np

# define A and b
A = np.array([[0, -1, 0], [0, 0, 1]])
b = np.array([1, 2, -2])

# compute the orthogonal projection of b onto the column space of A
P = A @ np.linalg.inv(A.T @ A) @ A.T @ b

print(P)


