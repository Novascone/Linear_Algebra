import numpy as np

# square vs rectangular matricies
S = np.random.randn(5,5)
R = np.random.randn(5,2) # 5 rows, 2 columns

print(S), print(' ')
print(R)

# identity 
I = np.eye(3)
print(I), print(' ')

# zeros
Z = np.zeros((4,4))
print(Z), print(' ')

# diagonal
D = np.diag([ 1, 2, 3, 5, 2])
print(D), print(' ')

# triangular from full matricies
M = np.random.randn(5,5)
U = np.triu(M)
L = np.tril(M)
print(L), print(' ')

# concatenate matricies
A = np.random.randn(3,2)
B = np.random.randn(3,4)
C = np.concatenate((A,B), axis=1)
print(C), print(' ')