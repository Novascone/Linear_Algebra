import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

m = 20
I = np.eye(m)
det_abs = []
mean_absdet = np.zeros(10)
x = []
fig, ax = plt.subplots()
for i in range(10):
    for j in range(1000):
        A = np.random.randint(1,10,size=(m,m))
        A[:,0] = A[:,1]
        shift = (i/100)*I
        As = A + shift
        det_A = np.linalg.det(As)
        det_abs.append(abs(det_A))
    mean_absdet[i] = np.mean(det_abs)
    x.append(i/100)
    print(mean_absdet[i])

plt.plot(x,mean_absdet,'s-')
plt.show()