import numpy as np
import matplotlib.pyplot as plt

S = np.array([ [3,0],
               [5,2],
               [1,2] ])

v = np.array([[-3], [1], [5]])
# v = np.array([[1], [7], [3]])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xx, yy = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
cp = np.cross(S[:,0],S[:,1])
z1 = (-cp[0]*xx - cp[1]*yy)/cp[2]
ax.plot_surface(xx,yy,z1,alpha=.2)


ax.plot([0, S[0,0]],[0, S[1,0]], [0, S[2,0]],'k')
ax.plot([0, S[0,1]],[0, S[1,1]], [0, S[2,1]],'k')

ax.plot([0, v[0]],[0, v[1]], [0, v[2]], 'r')

ax.view_init(elev=150,azim=0)
plt.show()