import numpy as np
import matplotlib.pyplot as plt

A = [[3,0,5], [8,1,3]]

U,S,V = np.linalg.svd(A)

print(U), print(' ')
print(S), print(' ')
print(V)

plt.subplot(141)
plt.imshow(A)
plt.title('A')
plt.axis('off')

plt.subplot(142)
plt.imshow(U)
plt.title('U')
plt.axis('off')

plt.subplot(143)
plt.imshow(np.diag(S))
plt.title('$\Sigma$')
plt.axis('off')

plt.subplot(144)
plt.imshow(V)
plt.title('V')
plt.axis('off')

plt.show() 