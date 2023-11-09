import numpy as np

# matrix

m = 4
n = 6

A = np.random.randint(0,6,size=(m,n))

# what is the largest possible rank?
ra = np.linalg.matrix_rank(A)
print('rank = ' + str(ra))


B = A
# set last column to be equal to penultimate column
# B[:,-1] = B[:,-2]
# set last row to be equal to penultimate row
B[-1,:] = B[-2,:]
rb = np.linalg.matrix_rank(B)
print('rank = ' + str(rb))

## adding noise to rank-deficient matrix

An = np.round(10*np.random.randn(m,m))

# reduce rank
An[:,-1] = An[:,-2]

# noise level
noiseamp = .001

# add noise

Bn = An + noiseamp*np.random.randn(m,m)

print('rank (w/o noise) = ' + str(np.linalg.matrix_rank(An)))
print('rank (w noise) = ' + str(np.linalg.matrix_rank(Bn)))