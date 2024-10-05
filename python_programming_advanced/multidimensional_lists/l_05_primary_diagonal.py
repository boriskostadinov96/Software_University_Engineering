square = int(input())
matrix = []

for _ in range(square):
    matrix.append(list(map(int, input().split())))

diagonal_sum = 0
for row_idx in range(square):
    diagonal_sum += matrix[row_idx][row_idx]

print(diagonal_sum)

# 1.1
# import numpy as np
# 
# square = int(input())
#
# matrix = np.array([list(map(int, input().split())) for _ in range(square)])
#
# diagonal_sum = np.sum(np.diagonal(matrix))
#
# print(diagonal_sum)
