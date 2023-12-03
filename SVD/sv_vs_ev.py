import numpy as np

# case 1: eig(A'A) vs. svd(A)

# A = np.array([[3,1,0],[1,1,0]])

# print(np.sort(np.linalg.eig(A.T@A)[0]))
# print(np.sort(np.linalg.svd(A)[1])**2)

# case 2: eig(A'A) vs. svd(A'A)



# print(np.sort(np.linalg.eig(A.T@A)[0]))
# print(np.sort(np.linalg.svd(A.T@A)[1]))

# case 3a: eig(A) vs. svd(A), real-valued eigs

# A = np.array([[3,1,0],[1,1,0], [1,1,1]])

# print(np.sort(np.linalg.eig(A)[0]))
# print(np.sort(np.linalg.svd(A)[1]))

# case 3b: eig(A) vs svd(A), complex eigs

A = np.random.randn(3,3)

print(np.sort(np.linalg.eig(A)[0]))
print(np.sort(np.linalg.svd(A)[1]))