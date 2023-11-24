import numpy as np

eye2 = np.eye(2,2)

abt = np.outer([1,2],[3,4])

adotb = np.dot([1,2],[3,4])

A = eye2 - abt

A_inv_SM = eye2 + (1/(1-adotb))*abt

print('A: \n', A), print(' ')
print('A Inv: \n', np.linalg.inv(A)), print(' ')
print('A inv SM: \n', A_inv_SM), print(' ')
