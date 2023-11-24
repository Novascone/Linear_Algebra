import numpy as np

m = 100
n = 100

A = np.random.randint(0,5,size=(m,n))

A_inv = np.linalg.inv(A)

print(A_inv)