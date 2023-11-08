import numpy as np

# two square matrices
m = 4
n = 4

A = np.array(
    [[ 1, 0, 0],
     [ 0, 1, 0],
     [ 0, 0, 7]])

B = np.array(
    [[ 2, 4, 6],
     [ 4, 4, 8],
     [ 6, 8, 2]])

A_mult_A = A@A
A_hada_A = A*A

B_mult_B = B@B
B_hada_B = B*B

print('A multiplied by A:\n', A_mult_A)
print('A hadamard A:\n', A_hada_A)
print('B multiplied by B:\n', B_mult_B)
print('B hadamard B:\n', B_hada_B)



