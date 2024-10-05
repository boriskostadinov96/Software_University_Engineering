rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col_idx in range(cols):
    total_cols = 0

    for row_idx in range(rows):
        total_cols += matrix[row_idx][col_idx]

    print(total_cols)

# 1.1
# import numpy as np
#
# rows, cols = map(int, input().split(', '))
#
# matrix = np.array([list(map(int, input().split())) for _ in range(rows)])
#
# col_sums = np.sum(matrix, axis=0)
#
# for col_sum in col_sums:
#     print(col_sum)
