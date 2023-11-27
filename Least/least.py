import numpy as np
from sympy import *

m = 10
n = 3

# create data

A = np.random.randint(0,6,size=(m,n))
b = np.random.ran


dint(0,6,size=(m,1))

# Ab = Matrix( np.concatenate([A, b], axis=1))
# print((Ab.rref()))



# normal equations
AtA = A.T@A
Atb = A.T@b

normEQ = Matrix( np.concatenate([AtA,Atb], axis=1))

Asol = normEQ.rref()
Asol = Asol[0]
x = Asol[:,-1]

print(np.array(Asol)), print(' ')
print(x), print(' ')

# compare to left-inverse

x2 = np.linalg.inv(AtA) @ Atb
print(x2), print(' ')

# python solver
x3 = np.linalg.solve(AtA,Atb)
print(x3)