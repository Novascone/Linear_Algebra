import numpy as np
m = 4
n = 4

A = np.random.randint(0,6,size=(m,n))
B = np.random.randint(0,6,size=(m,n))

A = A@A.T
B = B@B.T

diffAB = A - B

D,V = np.linalg.eig(diffAB)

D2,V2 = np.linalg.eig(diffAB@diffAB)

print(D),print(' '),print(V),print(' ')
print(D**2),print(' ')
print(D2),print(' '),print(V2)

