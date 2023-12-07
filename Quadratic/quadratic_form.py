import numpy as np
import matplotlib.pyplot as plt

S = [[ 1,  3, -2],
     [ 0,  3,  4],
     [-5, -2,  4] ]

w = np.transpose([[-2,4,3]])

qf = w.T@S@w

n = len(w)

plt.subplot(131)
plt.imshow(S)
plt.axis('off')
plt.title('Matrix S')

plt.subplot(132)
plt.imshow(w)
plt.axis('off')
plt.title('Vector w')

plt.subplot(133)
plt.imshow(qf)
plt.axis('off')
plt.title('Quadratic Form')

plt.show()