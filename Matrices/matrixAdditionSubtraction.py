import numpy as np

# create random matrices 

A = np.random.randn(5,4)
B = np.random.randn(5,3)
C = np.random.randn(5,4)

# A+B won't work, not the same number of elements
A+C

# shifting a matrix

l = .3 # lambda
N =  5 # size of square matrix
D = np.random.randn(N,N) # can only shift a square matrix

Ds = D + l*np.eye(N)

print(D), print(' '), print(Ds)