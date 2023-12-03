import numpy as np

m = 3
n = 6

A = np.random.randn(m,n)

print(A)

Us,Ss,Vs = np.linalg.svd(A)

L,V = np.linalg.eig(A.T@A)

sidx = np.argsort(L)[::-1]
L = L[sidx]
V = V[:,sidx]

print('V - Vs: \n', np.round(Vs.T+V,2)),print(' ')

print(L), print(' ')
print(Ss**2)

U = np.zeros((m,m))
for i in range(m):
    U[:,i] = A@V[:,i].T/np.sqrt(L[i])

print(np.round(U+Us,2))
