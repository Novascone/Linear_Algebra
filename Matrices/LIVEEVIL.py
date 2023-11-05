import numpy as np

n = 2

L = np.random.randint(0,4,size=(n,n))
I = np.random.randint(0,4,size=(n,n))
V = np.random.randint(0,4,size=(n,n))
E = np.random.randint(0,4,size=(n,n))


res1 = np.transpose(L@I@V@E)

res2 = E.T @ V.T @ I.T @ L.T

print('res1:\n', res1), print('res2:\n', res2)
print('L:\n',L,'\n','L.T:\n',L.T)