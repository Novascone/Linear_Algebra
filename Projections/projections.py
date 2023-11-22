import numpy as np
import matplotlib.pyplot as plt


# point b
b = np.array([4,1])

# line a
a = np.array([2, 5])

beta = (a.T@b) / (a.T@a)

# draw

plt.plot(b[0], b[1], 'ko',label='b')
plt.plot([0, a[0]], [0, a[1]], 'b', label='a')

# plot line projection

plt.plot([b[0], beta*a[0]], [b[1], beta*a[1]], 'r--', label=r'b-$\beta$a')
plt.axis('square')
plt.grid()
plt.legend()
plt.axis((-6,6,-6,6))

plt.show()