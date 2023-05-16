import numpy as np

v1 = np.array([2, 2, 0])
v2 = np.array([1, 0, 0])

v3 = np.cross(v1, v2)

print("The eigenvector v3 is: ", v3)
