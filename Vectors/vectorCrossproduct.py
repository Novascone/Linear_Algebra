import numpy as np
import matplotlib.pyplot as plt

# two 3D arrays
v = np.array([-3,  2, 5])
w = np.array([ 4, -3, 0])

# calculating the cross product with numpy
vxw = np.cross(v,w)

# calculating the cross product manually
vxwM = np.array([
                [v[1] * w[2] - v[2] * w[1]],
                [v[2] * w[0] - v[0] * w[2]],
                [v[0] * w[1] - v[1] * w[0]]
                 ])

# print("np cross:", vxw)
# print("manual cross:", vxwM)


fig = plt.figure()

ax = fig.add_subplot(projection='3d')

xx, yy = np.meshgrid(np.linspace(-10,10,10), np.linspace(-10,10,10))
z1 = (-vxw[0] * xx - vxw[1]*yy)/vxw[2]
ax.plot_surface(xx, yy, z1)

ax.plot([0, v[0]], [0,v[1]], [0,v[2]], 'k')
ax.plot([0, w[0]], [0,w[1]], [0,w[2]], 'k')
ax.plot([0, vxw[0]], [0,vxw[1]], [0,vxw[2]], 'r')

ax.view_init(azim=150,elev=45)
plt.show()