import numpy as np

# test whether the dot product sign is invariant to scalar multiplication

v = np.random.rand(3)*10
w = np.random.rand(3)*10

a = np.random.randint(10)

b = np.random.randint(10)*-1

print(a,b)

vTw = np.dot(v,w)

svTw = np.dot((a*v),(b*w))

print('v dot w:', vTw)
print('scaled v dot w:', svTw)

# the product sign is not invariant to scalar multiplication