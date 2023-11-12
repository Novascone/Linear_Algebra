import numpy as np

## rules: rank of AB <= min(rank A, rank B)
#        rank of A+B <= rank A + rank B

A = np.random.randint(0,6,size=(2,5))
B = np.random.randint(0,6,size=(2,5))

ATA = A.T@A
BTB = B.T@B

rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)
rank_ATA = np.linalg.matrix_rank(ATA)
rank_BTB = np.linalg.matrix_rank(BTB)
rank_ATAmulBTB = np.linalg.matrix_rank(ATA@BTB)
rank_ATAplusBTB = np.linalg.matrix_rank(ATA + BTB)

print('Rank A: \n', rank_A), print(' ')
print('Rank B: \n', rank_B), print(' ')
print('Rank ATA: \n', rank_ATA), print(' ')
print('Rank BTB: \n', rank_BTB), print(' ')
print('Rank ATA times BTB: \n', rank_ATAmulBTB), print(' ')
print('Rank ATA plus BTB: \n', rank_ATAplusBTB), print(' ')