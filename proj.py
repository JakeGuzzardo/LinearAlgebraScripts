import numpy as np

w1_x = 1
w1_y = 0
w1_z = -4

w2_x = -44
w2_y = -68
w2_z = -11

w1 = np.array([w1_x, w1_y, w1_z])
w2 = np.array([w2_x, w2_y, w2_z])

V = np.array([-1, -2, -3])

proj_V_W = ((V.dot(w1) / w1.dot(w1)) * w1) + ((V.dot(w2) / w2.dot(w2)) * w2)

N = V - proj_V_W
print(N)