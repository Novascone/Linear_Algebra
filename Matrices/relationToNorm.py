import numpy as np
import matplotlib.pyplot as plt
import math

# input vector
for i in range(0,10):
    v = np.array([3 , -2])

    # 2x2 rotation matrix
    th = i*np.pi/25
    A = np.array([[i*math.cos(th), -math.sin(th),], [math.sin(th), math.cos(th)]])
    Ar = np.array([[math.cos(th), -math.sin(th),], [math.sin(th), math.cos(th)]])

    # output vector
    w = A@np.matrix.transpose(v)
    wr = Ar@np.matrix.transpose(v)
    plt.plot([0, v[0]], [0,v[1]], label='v')
    plt.plot([0, w[0]], [0,w[1]], label='Av')
    plt.plot([0, wr[0]], [0,wr[1]], label='Arv')
    print('Norm Impure:\n',np.linalg.norm(w))
    print('Norm Pure:\n',np.linalg.norm(wr))



plt.grid()
plt.axis((-4, 4, -4, 4))

plt.legend()
plt.title('Rotation')
plt.show()

