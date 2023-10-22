import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open('Einstein_tongue.jpg')

# plt.imshow(pic)
# plt.show()


pic = np.array(pic)
# plt.imshow(pic,cmap='gray')
# plt.show()

# singular devalue compositon

U, S, V = np.linalg.svd(pic)

# plt.plot(S,'s-')
# plt.xlim([0,100])
# plt.xlabel('Component number')
# plt.ylabel("Singualr Value (\sigma)")
# plt.show()

# list component used for reconstruciton
comps = np.arange(20,150)


# reconstruct the low-rank version of the picture
reconPic = U[:,comps]@np.diag(S[comps])@V[comps,:]

plt.figure(figsize=(5,10))
plt.subplot(1,2,1)
plt.imshow(pic,cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(reconPic,cmap='gray')
plt.title('Components %s-%s' %(comps[0],comps[-1]))

plt.show()