import numpy as np

m = 100
n = 100

A = np.random.randint(0,5,size=(m,n))

Q,R = np.linalg.qr(A,'complete')
A_inv = np.linalg.inv(R)*Q.T
# better version
# np.linalg.solve(R,Q.T)
A_inv_np = np.linalg.inv(A)

