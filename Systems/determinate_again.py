import numpy as np

# m = 3
# A = np.random.randint(1,10,size=(m,m))
# B = np.random.randint(1,10,size=(m,m))

# det_A = np.linalg.det(A)
# det_B = np.linalg.det(B)

# print('det AB: \n', np.linalg.det(A@B)), print(' ')
# print('det A * det B: \n', det_A * det_B), print(' ')

for i in range(2,41):
    A = np.random.randint(1,10,size=(i,i))
    B = np.random.randint(1,10,size=(i,i))
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    print('det AB: \n', np.linalg.det(A@B)), print(' ')
    print('det A * det B: \n', det_A * det_B), print(' ')