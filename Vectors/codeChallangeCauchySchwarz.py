import numpy as np


a = np.array([1, 2])
b = np.array([3, 4])

ab = np.dot(a,b)

lena = np.linalg.norm(a)

lenb = np.linalg.norm(b)

print(ab, '<=', lena*lenb)

c = np.array([0, 2])
d = np.array([0, 2])

cd = np.dot(c,d)

lenc = np.linalg.norm(c)

lend = np.linalg.norm(d)

print(cd, '<=', lenc*lend)