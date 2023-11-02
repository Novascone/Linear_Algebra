import numpy as np

# scalar and two matricies hand created
# s = 3
# M = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
# N = np.matrix([[8, 9, 10, 11], [11, 12, 13, 14]])

# random scalar and two random matricies
s = np.random.randint(9)
M = np.random.randint(10,size=(2,4))
N = np.random.randint(10,size=(2,4))

print('s(M+N): \n', s*(M+N)), print(' '), print('sM + sN: \n', s*M+s*N)