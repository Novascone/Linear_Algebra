import numpy as np


m = 5
n = 5
A = np .random.randint(0,6,size=(m,n))
b = np .random.randint(0,6,size=(m,n))

Q,R = np.linalg.qr(A,'complete')


R_inv = np.linalg.inv(R)
x = R_inv@Q.T@b

print(R_inv@R)


print(x)
print()
print(np.linalg.lstsq(A,b,rcond=None))