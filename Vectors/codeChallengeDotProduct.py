import numpy as np

M1 = np.random.randint(100,size=(4,6))
M2 = np.random.randint(100,size=(4,6))
MD = np.empty(int(M1.shape[1]))

# --------------------------------------
# below shows the correct algorith for computing the dot product between the columns of matricies
# the commented out code shows the process used to make the fuction
# it includes a lot of print statements that I used to debug
# --------------------------------------

# dotProduct = 0

# print('M1', M1)
# print('-------------------------')
# print('M2', M2)
# print('-------------------------')
# print('MD', MD)

# for i in range(M1.shape[1]):
#     columnM1 = M1[:,i]
#     columnM2 = M2[:,i]
#     print('MD', MD)
#     print('----------------:')
#     dotProduct = 0
#     print('column 1:', columnM1)
#     print('column 2:', columnM2)
#     # print('----------------:')
#     print('i:',i)
#     print('----------------:')
#     for j in range(len(columnM1)):
#         print('dot product', dotProduct)
#         print('----------------:')
#         elementProduct = columnM1[j] * columnM2[j]
#         print(columnM1[j],'*',columnM2[j])
#         print('product:', elementProduct)
#         dotProduct += elementProduct
#         print('dot product', dotProduct)
#         print('j:',j)
#         print('----------------:')
#         MD[i] = dotProduct
        

# print('-------------------------')
# print('Dot Products by Column:', MD)
        
    
def dotProductsByMatrixColumn(Matrix1,Matrix2,dotProductArray,dotProduct): # function to take dot product of columns of vectors
    for i in range(Matrix1.shape[1]): # go over nunber of columns in the passed matrix
        columnM1 = Matrix1[:,i] # takes the columns of the first matrix
        columnM2 = Matrix2[:,i] # takes the columbs of the second matrix
        dotProduct = 0 # resets the dot product
        for j in range(len(columnM1)): # goes over the elements in each column the columns must be the same size so we can use column one
            elementProduct = columnM1[j] * columnM2[j] # takes the element wise product of the columns
            dotProduct += elementProduct # adds that product to the dotproduct total for that column
            dotProductArray[i] = dotProduct # sets the dotproduct matrix equal to the dotproduct of the column for the correct column
    return dotProductArray # returns an array of dot products of each column

print(dotProductsByMatrixColumn(M1,M2,MD,0))