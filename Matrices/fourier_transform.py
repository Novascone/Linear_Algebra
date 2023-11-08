import numpy as np
import matplotlib.pyplot as plt
from math import e
 
m = 4
n = 4

e = np.e
pi = np.pi
w =  e**((-2*pi*1j)/4)
F = np.zeros(shape=(m,n)).astype(complex)
x = np.random.randn(n)

M = 0
for j in range(m):
    for k in range(n):
        M = (j)*(k)
        F[j][k] = w**M

X = F*x

print(X)



