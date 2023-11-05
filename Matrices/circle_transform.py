import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,100)
xy = np.vstack((np.cos(x),np.sin(x))).T
print(np.shape(xy))

plt.plot(xy[:,0], xy[:,1],'o')

T = np.array([[1,.7],[.7,1]])
T2 = np.array([[1,-.7],[-.7,1]])

new_coords = xy@T
new_coords2 = xy@T2

plt.plot(new_coords[:,0], new_coords[:,1],'o')
plt.plot(new_coords2[:,0], new_coords2[:,1],'o')

plt.legend()
plt.title('Circle')
plt.show()