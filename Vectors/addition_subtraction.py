import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# create arrays in numpy so we can do addition on them easily
v1 = np.array([3, -1])
v2 = np.array([2, 4])

v3 = v1 + v2

# [0, v1[0]], [0, v1[1]] - tail and head respectively of v1
plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v1')
# adding the two vectors elements
plt.plot([0, v2[0]]+v1[0], [0, v2[1]]+v1[1], 'r', label='v2')
# ploting the line from tail of the first vector v1 to the head of the transposed vector v2
plt.plot([0, v3[0]], [0, v3[1]], 'k',label='v1+v2')

plt.legend()
plt.axis('square')
plt.axis((-6, 6, -6, 6))
plt.grid()
plt.show()