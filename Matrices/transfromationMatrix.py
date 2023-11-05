import numpy as np
import matplotlib.pyplot as plt
import math

# vector
v1 = np.array([3, -2])

# 2 x 2 transformation matrix
A1 = np.array([[1, -1], [2, 1]])

# output vector
w1 = A1@np.matrix.transpose(v1)

# plot

plt.plot([0, v1[0]], [0,v1[1]], label='v1')
plt.plot([0, w1[0]], [0,w1[1]], label='Av1')

plt.grid()
plt.axis((-6, 6, -6, 6))

plt.legend()
plt.title('Rotation + Stretching')
plt.show()


## pure rotation

# input vector
v2 = np.array([3 , -2])

# 2x2 rotation matrix
th = 5*np.pi/24
A2 = np.array([[math.cos(th), -math.sin(th),], [math.sin(th), math.cos(th)]])

# output vector
w2 = A2@np.matrix.transpose(v2)

plt.plot([0, v2[0]], [0,v2[1]], label='v2')
plt.plot([0, w2[0]], [0,w2[1]], label='Av2')

plt.grid()
plt.axis((-4, 4, -4, 4))

plt.legend()
plt.title('Rotation')
plt.show()


## eigen

# vector
v = np.array([1, 2])

# 2 x 2 transformation matrix
A =  np.array([[2, 1], [2, 3]])

# output vector
w = A@np.matrix.transpose(v)

# plot

plt.plot([0, v[0]], [0,v[1]], label='v')
plt.plot([0, w[0]], [0,w[1]], label='Av')

plt.grid()
plt.axis((-6, 6, -6, 6))

plt.legend()
plt.title('Eigen')
plt.show()

