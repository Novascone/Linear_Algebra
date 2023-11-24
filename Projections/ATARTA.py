import numpy as np

m = 2
n = 2

A = np.random.randint(0,5,size=(m,n))

Q,R = np.linalg.qr(A,'complete')

print('A.T@A: \n', A.T@A)
print('R.T@R: \n', R.T@R)

print('----------')
print((A@A).T)
print(A.T@A.T)
print('----------')
print('A inverse times A; \n',np.linalg.inv(A)@A)