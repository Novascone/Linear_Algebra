import numpy as np

m = 4
n = 3
k = 6


# matricies

A = np.random.randn(m,n)
B = np.random.randn(n,k)
C = np.random.randn(m,k)

# which are valid ?

np.matmul(A,B)
# np.matmul(A,A) # not valid
np.matmul(A.T,C)
np.matmul(B,B.T)
np.matmul(np.matrix.transpose(B),B)
# np.matmul(B,C) # not valid
# np.matmul(C,B) # not valid
# np.matmul(C.T,B) # not valid
np.matmul(C,B.T) 

