import numpy as np

m = 13 
n = 2

# matrices must be the same size
A = np.random.randint(0,5,size=(m,n))
B = np.random.randint(0,5,size=(m,n))
# C = np.random.randint(0,5,size=(m,n))

#  the same!
# print(C*(A+B)), print(' ')
# print(B*C + C*A)

# different syntax when compared to @ for matrix multiplication
C1 = np.multiply(A,B)
C2 = A*B
print(C1), print(' ')
print(C2), print(' ')

print(C1 - C2)