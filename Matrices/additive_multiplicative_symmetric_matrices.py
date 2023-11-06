import numpy as np

# additive

# sizes
ma = 5
na = 5

# create matrices
Aa = np.random.randint(0,5,size=(ma,na))
Sa = (Aa+Aa.T)/2

# A symmetric matrix minus its transpose should be the zero matrix
print(Sa-Sa.T)

# multiplicative method

mm = 5
nm = 3

Am = np.random.randint(0,5,size=(mm,nm))
Sm = (Am.T@Am)
Sm2 = (Am@Am.T)

# A symmetric matrix minus its transpose should be the zero matrix
print(Sm.shape) # 3x3
print(Sm2.shape) # 5x5

print(Sm - Sm.T)
print(Sm2 - Sm2.T)
