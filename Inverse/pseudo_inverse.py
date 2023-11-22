import numpy as np

m = 5

A = np.random.randint(1,5,size=(m,m))

print('Inverse: \n', np.linalg.inv(A)),print(' ')
print('Pseudoinverse: \n', np.linalg.pinv(A)),print(' ')

# its the same!

print('Inverse - pseudoinverse: \n', np.round(np.linalg.inv(A) - np.linalg.pinv(A),5))