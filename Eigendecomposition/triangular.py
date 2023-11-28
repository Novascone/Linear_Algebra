import numpy as np

m = 10
n = 10

A = np.random.randint(0,6,size=(4))
B = np.random.randint(0,6,size=(m))
A = np.diag(A)
B = np.diag(B)

print(A),print(' ')
print(np.linalg.eig(A)[0]),print(' ')
print(B),print(' ')
print(np.linalg.eig(B)[0]),print(' ')

C = np.random.randint(0,6,size=(m,n))
C = np.triu(C)
D = np.random.randint(0,6,size=(m,n))
D = np.tril(D)

print(C),print(' ')
print(np.linalg.eig(C)[0]),print(' ')
print(D),print(' ')
print(np.linalg.eig(D)[0]),print(' ')