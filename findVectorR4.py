import numpy as np

# Define the given vectors as columns of a matrix
V = np.array([[-2, -4, -2], [2, -2, 0], [0, -2, -1], [0, 2, -2]])

# Use the Gram-Schmidt process to find an orthonormal basis for the column space of V
Q, R = np.linalg.qr(V)

# The last column of Q will be a non-zero vector orthogonal to all of the columns of V
W = Q[:, -1]

# Print the resulting vector W
print("The vector orthogonal to v1, v2, and v3 is:", W)