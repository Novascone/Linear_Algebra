import numpy as np
from sympy import *

A = np.array([[1, 2],
              [2, 4]])


B = np.array([[1, 2,  4],
              [2, 4,  8],
              [4, 8, 16]])

C = np.array([[23, 13,  5],
              [19, 11,  3],
              [17,  7,  1]])

D = np.array([[1, 2, 1],
              [2, 4, 3],
              [4, 8, 5]])

E = np.array([[1,  7,  17],
              [3, 11,  19],
              [5, 13, 23]])

m = 3
F = np.random.randint(1,10,size=(m,m))
# print(F[0,:])
# print(F[:,0])
# F[:,1] = F[:,0]
F[1,:] = F[0,:]
 


det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_C = np.linalg.det(C)
det_D = np.linalg.det(D)
det_E = np.linalg.det(E)
det_F = np.linalg.det(F)

print("A det:\n", det_A)
print("B det:\n", det_B)
print("C det:\n", det_C)
print("D det:\n", det_D)
print("E det:\n", det_E)
print("F det:\n", det_F) # this should be zero, but because its so computationally intensive this compter calculates it wrong