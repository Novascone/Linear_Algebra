import numpy as np
import matplotlib.pyplot as plt


# vector
v1 = np.array([3, -1])
# scalar, l for lambda
# this scalar will flip our original vector, and shrink it to .3 its original length
l = -.3
# scalar-modulated
v1m = v1*l

plt.plot([0, v1[0]], [0, v1[1]], 'b',label='v_1')
plt.plot([0, v1m[0]],[0, v1m[1]], 'r:',label='\lambda v_1')

plt.axis('square')
# dynamic axis by largest element of the modulated vector multiplied by 1.5
# which changed the size of the plot based on the vectors
axlim = max([abs(max(v1)),abs(max(v1m))])*1.5
plt.axis((-axlim,axlim,-axlim,axlim))
plt.grid()
plt.show()