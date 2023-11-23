import numpy as np
import matplotlib.pyplot as plt

w = np.array([2,3])

v = np.array([4,0])

# w parallel to v

beta = np.dot(w,v)/np.dot(v,v)
w_para = beta*v


# w orthogonal to v
w_orth = w - w_para

print(w_para + w_orth)

plt.plot([0,w[0]], [0,w[1]], 'r', linewidth=3)
plt.plot([0,v[0]], [0,v[1]], 'b', linewidth=2)
plt.plot([0,w_para[0]], [0,w_para[1]], 'r--', linewidth=3)
plt.plot([0,w_orth[0]], [0,w_orth[1]], 'r:', linewidth=3)

plt.legend(['w', 'v', 'w$_{||v}$', 'w$_{\perp v}$'])
plt.axis('square')
plt.grid()
plt.axis([-5,5,-5,5])
plt.show()