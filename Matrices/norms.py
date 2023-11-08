import numpy as np

## Norms

A = np.array([[1,2,3], [4,5,6], [7,7,9]])

# orthogonal matrix
Q,R = np.linalg.qr(np.random.randn(5,5))
A = Q

norm = np.linalg.norm(A)

# Frobenius norm
normFrob = np.linalg.norm(A,'fro')

# induced 2-norm
normInd2 = np.linalg.norm(A,2)


lamb = np.sqrt(np.max(np.linalg.eig(A.T@A)[0]))

# Schatten p-norm
p = 1
s = np.linalg.svd(A)[1] # singular values

normSchat = np.sum(s**p)**(1/p)

print(norm,normFrob,normInd2,normSchat)