import numpy as np

A = np.array([[2, 4],
               [0, 3]])

B = np.array([[2, 1],
               [2, 3]])
v = np.array([2,3])

print(np.dot(v.T,B))
