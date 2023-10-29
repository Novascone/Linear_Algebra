import numpy as np
import matplotlib.pyplot as plt 

# set of vectors
s1 = np.array([ 1, 1, 0])
s2 = np.array([ 1, 7, 0])

# two vectors
v = np.array([ 1, 2, 0])
w = np.array([ 3, 2, 1])

fig = plt.figure()

ax = fig.add_subplot(projection='3d')
ax.plot([0, s1[0]], [0, s1[1]], [.1, s1[2]+.1], 'r', linewidth=3)
ax.plot([0, s2[0]], [0, s2[1]], [.1, s2[2]+.1], 'r', linewidth=3)

ax.plot([0, v[0]], [0, v[1]], [.1, v[2]+.1], 'g', linewidth=3)
ax.plot([0, w[0]], [0, w[1]], [0, w[2]], 'b')

# draw plane
xx, yy = np.meshgrid(range(-15,16), range(-15,16))
cp = np.cross(s1,s2)
z1 = (-cp[0]*xx - cp[1]*yy*1./cp[2])
ax.plot_surface(xx,yy,z1)

plt.show()