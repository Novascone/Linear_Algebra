import numpy as np

m = 30

# square symmetric
A = np.random.randint(1,11,size=(m,m))
A = A.T@A/2

A[:,0] = A[0:,1]
# A[:,2] = A[0:,3]

l = .01

B = A + l*np.eye(m,m)
rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

print("Rank A: \n", rank_A), print(' ')
print("Rank A: \n", rank_B), print(' ')