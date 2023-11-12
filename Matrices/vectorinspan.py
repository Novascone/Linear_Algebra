import numpy as np

# is this vector
v = np.array([[1, 2, 3, 4]]).T

# in the span of these sets?
S = np.vstack([[4, 3, 6, 2],[0, 4, 0, 1]]).T
T = np.vstack([[1, 2, 2, 2],[0, 0, 1, 2]]).T

# if the vector is in the span of these sets then adding v will create a linearly dependent set because v isn't contributing any unique information to S
# therefore the rank will not change, because the dimensionality of information contained in the new concatenated matrix is the same as before.

# conversely if v is not in the subspace spanned by S then adding it will create a linearly independent matrix and increase the rank by 1
Sv = np.concatenate((S,v),axis=1)

rank_S = np.linalg.matrix_rank(S)
rank_Sv = np.linalg.matrix_rank(Sv)

Tv = np.concatenate((T,v),axis=1)

rank_T = np.linalg.matrix_rank(T)
rank_Tv = np.linalg.matrix_rank(Tv)

print('Rank S: \n', rank_S), print(" ")
print('Rank Sv: \n', rank_Sv), print(" ")
print('Rank T: \n', rank_T), print(" ")
print('Rank Tv: \n', rank_Tv), print(" ")




