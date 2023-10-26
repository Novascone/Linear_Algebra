import numpy as np

a = np.random.randint(100,size=(100))
b = np.random.randint(100, size=(100))

c = np.random.randint(100,size=2)
d = np.random.randint(100,size=2)

print('a dot b: ',np.dot(a,b))
print()
print('b dot a: ',np.dot(b,a))


print(c)
print()
print(d)
print('c dot d: ',np.dot(c,d))
print()
print('b dot a: ',np.dot(d,c))