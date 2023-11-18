import numpy as np
from sympy import *

A = Matrix(np.random.randn(4,4))
B = Matrix(np.random.randn(4,3))

C = Matrix(np.array([[1, 2],
                     [2, 4]]))

D = Matrix(np.array([[1, 2, 7],
                     [2, 4, 3],
                     [3, 6, 1]]))

E = Matrix(np.array([[1, 3],
                     [2, 6]]))

F = Matrix(np.array([[1, 2, 7, 21],
                     [2, 4, 3, 17],
                     [3, 6, 1, 13],
                     [4, 8, 1, 11]]))



rrefA = A.rref()
rrefB = B.rref()
rrefC = C.rref()
rrefD = D.rref()
rrefE = E.rref()
rrefF = F.rref()


print('A: \n', np.array(rrefA[0]))
print(' ')
print('B: \n',np.array(rrefB[0]))
print(' ')
print('C: \n',np.array(rrefC[0]))
print(' ')
print('D: \n',np.array(rrefD[0]))
print(' ')
print('E: \n',np.array(rrefE[0]))
print(' ')
print('F: \n',np.array(rrefF[0]))

