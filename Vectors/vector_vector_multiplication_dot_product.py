import numpy as np
import matplotlib.pyplot as plt


v1 = np.array([1, 2, 3, 4, 5])
v2 = np.array([0, -4, -3, 6, 5])

# methods for computing dot product

# method 1

def dot_product_method_one(vector1, vector2):
    dot_product = sum(np.multiply(vector1,vector2))
    return dot_product

# method 2

def dot_product_method_two(vector1, vector2):
    dot_product = np.dot(vector1,vector2)
    return dot_product

# method 3

def dot_product_method_three(vector1, vector2):
    dot_product = np.matmul(vector1,vector2)
    return dot_product

# method 4

def dot_product_method_four(vector1, vector2):
    
    dot_product = 0
    
    # loop over all elements 
    for i in range(0,len(vector1)):
        # multiply element and sum
        dot_product = dot_product + vector1[i]*vector2[i]
    return dot_product

print(dot_product_method_one(v1,v2),
      dot_product_method_two(v1,v2),
      dot_product_method_three(v1,v2),
      dot_product_method_four(v1,v2))