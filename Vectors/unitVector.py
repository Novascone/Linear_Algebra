import numpy as np
import matplotlib.pyplot as plt

# vector length > 1 and length < 1

# v = np.array([ -3, 6 ])
v = np.array([ -.3, .6 ])

# mu
# because out vector v has a length greater than one, to create a unit vector our mu will need to shrink v to be be one, so mu must be less than one
mu = 1/np.linalg.norm(v)

# if our vector v has a length less than one, to create a unit vector we need a mu that will stretch our vector to one, so mu must be greater than one

vn = v * mu

plt.plot([0, vn[0]], [0, vn[1]], 'r', label='v-norm', linewidth=5)
plt.plot([0, v[0]], [0, v[1]], 'b', label='v')

plt.axis('square')
plt.axis((-6, 6, -6, 6))
plt.grid()
plt.legend()
plt.show()
