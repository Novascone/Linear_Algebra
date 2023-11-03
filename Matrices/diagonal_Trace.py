import numpy as np

M = np.random.randint(10,size=(4,4))

# extract diagonals
d = np.diag(M) # matrix in, vector of diagonals out
D = np.diag(d)      # vector in, matrix with diagonal out (the rest of the elements are zero)
print(d), print(' '), print(D), print(' ')

# trace

tr = np.trace(M)
tr2 = sum(d)
print(tr), print(' '), print(tr2)
