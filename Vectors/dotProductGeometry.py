import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([ 2, 4, -3])
v2 = np.array([ 0, -3, -3])

ang = np.arccos(np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2)))
print(ang)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot([0, v1[0]], [0, v1[1]],[0, v2[2]])
# ax.plot([0, v2[0]], [0, v2[1]],[0, v2[2]])

# plt.axis((-6, 6, -6, 6))
# plt.title('Angle Between Vectors: %s rad.' %ang)
# plt.show()

v3 = np.array([ 16, -2, 4])

v4 = np.array([ .5, 2, -1])

# algebraic
dp_a = np.dot( v3,v4 )
# geometric
dp_g = np.linalg.norm(v1)*np.linalg.norm(v2)*np.cos(ang)

print(dp_a)
