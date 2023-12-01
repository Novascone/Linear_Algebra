import numpy as np

# symmetric matrix

A = np.random.randn(4,4)

A = A+A.T

evals,evecs = np.linalg.eig(A)

v = np.reshape(evecs[:,0],(4,1))

# norm of outer product of v_i

print(np.linalg.norm(v.T@v)), print(' ')

# one layer of A 

print(evals[0]),print(' ')
print(np.linalg.norm(v*evals[0]*v.T)), print(' ')

Arecon = np.zeros(shape=(4,4))
for i in range(len(evecs)):
    v = np.reshape(evecs[:,i],(4,1))
    Arecon += v*evals[i]*v.T
    
print(Arecon)