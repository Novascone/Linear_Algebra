import numpy as np

n = 4

# matrices 
A = np.random.randint(0,11,(n,n))
I = np.eye(n,n)
Z = np.zeros((n,n))

# test 

print(np.array_equal(A@I,A)) # true
print(np.array_equal(A,A@I)) # true
print(np.array_equal(A,A+I)) # false

print(np.array_equal(A,A+I)) # false
print(np.array_equal(A+Z, A@I)) # true