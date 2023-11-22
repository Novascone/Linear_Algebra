import numpy as np

m = 10
i = np.random.randint(1,10)

A = np.diag(np.full(m,i))
B = np.diag(np.arange(i,m))

print(np.linalg.inv(B))