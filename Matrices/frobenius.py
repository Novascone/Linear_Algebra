import numpy as np 

## Frobenius norm

m = 9
n = 4

# two matrices must be the same size

A = np.random.randn(m,n)
B = np.random.randn(m,n)

# vectorize the matrices
Av = np.reshape( A, m*n, order='F' ) # order = 'F' reshapes to columns instead of rows
Bv = np.reshape( B, m*n, order='F' ) 
frob_dp = np.dot(Av,Bv)

# trace trick
frob_dp2 = np.trace(A.T@B)
print(frob_dp2)
print(frob_dp)

# matrix norm

Anorm = np.linalg.norm(A,'fro') # 'fro' = Frobenius
Anorm2 = np.sqrt(np.trace(A.T@A))
print(Anorm)
print(Anorm2)