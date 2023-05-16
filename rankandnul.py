import numpy as np

A = np.array([[4, 6, -6, 4, 3, -7],
            [0, 18, -10, 8, 5, -11], 
            [0, -7, 5, -2, -5, 9], 
            [12, 0, -4, 8, -7, 7], 
            [8, -3, -3, 2, 0, -2]]
)

rank = np.linalg.matrix_rank(A)
print("Rank of A:", rank)

Q, R = np.linalg.qr(A)
nullity = A.shape[1] - np.linalg.matrix_rank(A)
print("Nullity of A:", nullity)