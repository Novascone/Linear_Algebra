import numpy as np
import matplotlib.pyplot as plt
# m>n for left inverse
# m<n for right inverse

m = 3
n = 6

A = np.random.randint(1,5,size=(m,n))

AtA = A.T@A

AAt = A@A.T

# inspect ranks
print('Shape of A^TA', np.shape(AtA))
print('rank of A^TA:', np.linalg.matrix_rank(AtA))
print('Shape of AA^T', np.shape(AAt))
print('rank of AA^T:', np.linalg.matrix_rank(AAt))

# left inverse
Aleft = np.linalg.inv(AtA)@A.T

# right inverse
Aright = A.T@np.linalg.inv(AAt)

I_left = Aleft @ A
I_right = A @ Aright

print(I_left), print(' ')
print(I_right), print(' ')


# inverse function

AtA_inv = np.linalg.inv(AtA)
I_AtA   = AtA_inv @ AtA

AAt_inv = np.linalg.inv(AAt)
I_AAt   = AAt_inv @ AAt


print(I_AtA), print(' ')
print(I_AAt)

# show images

plt.subplot(331)
plt.imshow(A), plt.axis('off')
plt.title('A')

plt.subplot(332)
plt.imshow(AtA), plt.axis('off')
plt.title('A$^T$A')

plt.subplot(333)
plt.imshow(AAt), plt.axis('off')
plt.title('AA$^T$')

plt.subplot(335)
plt.imshow(Aleft), plt.axis('off')
plt.title('[ $(A^TA)^{-1}A^T ]$ A')

plt.subplot(336)
plt.imshow(Aright), plt.axis('off')
plt.title('$A^T(AA^T)^{-1}$')

plt.subplot(338)
plt.imshow(I_left), plt.axis('off')
plt.title('[ $(A^TA)^{-1}A^T ]$ A')

plt.subplot(339)
plt.imshow(I_right), plt.axis('off')
plt.title('$A^T(AA^T)^{-1}$')

plt.show()