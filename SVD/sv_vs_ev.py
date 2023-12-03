import numpy as np

# case 1: eig(A'A) vs svd(A)

A = np.array([[3,1,0],[1,1,0]])

print(np.sort(np.linalg.eig(A.T@A)[0]))
print(np.sort(np.linalg.svd(A)[1])**2)

# case 2: