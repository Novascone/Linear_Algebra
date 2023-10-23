import numpy as np
import matplotlib.pyplot as plt


# Distributive property

# create random vectors
n = 10

a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

result1 = np.dot(a, (b+c))
result2 = np.dot(a,b) + np.dot(a,c)

# compare
print('--------')
print([result1, result2])
print('--------')

# Associative property

# create random vectors
m = 5
d = np.random.randn(m)
e = np.random.randn(m)
f = np.random.randn(m)
# all the same case
# d = np.array([1,2,3,4,5])
# e = np.array([1,2,3,4,5])
# f = np.array([1,2,3,4,5])
# zeros case
# f = np.zeros(m)


result3 = np.dot(d, np.dot(e,f))
result4 = np.dot(np.dot(d,e), f)

# compare
print(result3)
print('--------')
print(result4)
print('--------')

### special cases where associative property works!
# 1) one vector is the zeros vector
# 2 a==b==c