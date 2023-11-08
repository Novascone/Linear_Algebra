import numpy as np
import matplotlib.pyplot as plt

# size of matrix
m = 4
n = 4
# creating random matrix
A = np.random.randint(1,6,size=(4,4))
Al = np.tril(A)
Au = np.triu(A)
# creating  a symmetric matrix
Asymm = A@A.T/2
# creating skew-symetric from symmetric A by multiplying
# the lower triangular matrix by -2 and adding it
# to upper triangular symmetric A
Askew = -2*np.tril(Asymm) + np.triu(Asymm)
# calculating norms and antis 
Anorm = np.linalg.norm(A)
Asymmnorm = np.linalg.norm(Asymm)
Askewnorm = np.linalg.norm(Askew)
Aanti = (A - A.T)/2
Aantisymm = (Asymm - Asymm.T)/2
Aantiskew = (Askew - Askew.T)/2
Aanti_norm = np.linalg.norm(Aanti)
Aantisymm_norm = np.linalg.norm(Aantisymm)
Aantiskew_norm  = np.linalg.norm(Aantiskew)

# calculating asymmetry matrix
ai = Aanti_norm/Anorm
aisymm = Aantisymm_norm/Asymmnorm
aiskew = Aantiskew_norm/Askewnorm

print("Aanti:\n", Aanti)
print("ai:\n", ai), print(' ')

print("Aanti Symmetric:\n", Aantisymm)
print("ai:\n", aisymm), print(' ')

print("Aanti Skew-symmetric:\n", Aantiskew)
print("ai:\n", aiskew), print(' ')

# creating a matrix with specified proportion of
# symmetric and skew-symmetric
B = (1 - .5)*(A + A.T) + .5*(A - A.T)

print("B:\n", B)

