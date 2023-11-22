import numpy as np

m = 3

A = np.random.randint(1,10,size=(m,m))
minors = np.zeros((m,m))
h = np.zeros((m,m))

for i in range(m):
    for j in range(m):
        rows = [True]*m
        cols = [True]*m
        rows[i] = False
        cols[i] = False
        
        minors[i,j] = np.linalg.det(A[rows,:][:,cols])
        h[i,j] = (-1)**(i+j)

C = minors*h

A = C.T*(1/np.linalg.det(A))

print(A)
        