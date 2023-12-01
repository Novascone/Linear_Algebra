import numpy as np
from math import prod

A = np.random.randn(4,4)

# trace = sum(evals)

evals,evecs = np.linalg.eig(A)

print('trace: ', np.trace(A)),print(' ')
print('sum evals: ', sum(evals)),print(' ')

# det = prod(evals)

print('det: ', np.linalg.det(A)),print(' ')
print('sum evals: ', prod(evals))