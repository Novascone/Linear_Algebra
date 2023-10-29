import numpy as np

# complex number
z = complex(3,4)
print(z)

# magnitude
print(np.linalg.norm(z))
# magnitude by standard transpose
print(np.sqrt(np.transpose(z)*z))
# magnitude by Hermitian transpose
print(np.sqrt(np.transpose(z.conjugate()*z)))


# complex vector
v = np.array([3, 4j, 5+2j, complex(2,-5)])
print(v.T)
print(np.transpose(v))
print(np.transpose(v.conjugate()))
