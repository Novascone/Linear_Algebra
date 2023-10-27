import numpy as np

v1 = np.array([1, 2, 3, 4, 5, 6])

vl1 = np.sqrt(sum(np.multiply(v1,v1)))

vl2 = np.linalg.norm(v1)

print(vl1)
print()
print(vl2)