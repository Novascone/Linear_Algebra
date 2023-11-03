import numpy as np

# random matrices and lambda
A = np.random.randint(10,size=(4,4))
B = np.random.randint(10,size=(4,4))
l = np.random.randint(3)

print('tr(A) + tr(B): \n', np.trace(A) + np.trace(B)), print(' ')
print('tr(A+b): \n', np.trace(A+B)), print(' ')
print('tr(l*A): \n', np.trace(l*A)), print(' ')
print('l*tr(A): \n', l*np.trace(A)), print(' ')

# the trace is linear