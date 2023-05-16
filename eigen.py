import numpy as np

# Define the eigenvalues
y_1 = 5
y_2 = 4

v1 = np.array([-1, 1, 3])
v2 = np.array([0, 3, 3])
v3 = np.array([-1, -1, 2])

P = np.column_stack((v1, v2, v3))

P_inv = np.linalg.inv(P)

D = np.diag([y_1, y_1, y_2])

A = P @ D @ P_inv

print("Original matrix A:")
print(A)
