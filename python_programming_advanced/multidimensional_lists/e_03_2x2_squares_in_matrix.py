rows, columns = [int(x) for x in input().split()]

square_matrix = [input().split() for _ in range(rows)]
count = 0

for row_idx in range(rows - 1):
    for col_idx in range(columns - 1):
        current_el = square_matrix[row_idx][col_idx]
        next_el = square_matrix[row_idx][col_idx + 1]
        under_el = square_matrix[row_idx + 1][col_idx]
        diagonal_el = square_matrix[row_idx + 1][col_idx + 1]

        if current_el == next_el == under_el == diagonal_el:
            count += 1

print(count)

# 1.1
# rows, columns = [int(x) for x in input().split()]
# 
# square_matrix = [input().split() for _ in range(rows)]
# count = 0
#
# for row_idx in range(rows - 1):
#     for col_idx in range(columns - 1):
#         current_symbol = square_matrix[row_idx][col_idx]
#
#         if current_symbol == square_matrix[row_idx][col_idx + 1] and current_symbol == square_matrix[row_idx + 1][col_idx]\
#                 and current_symbol == square_matrix[row_idx + 1][col_idx + 1]:
#             count += 1
#
# print(count)


# 1.2
# import numpy as np
#
# rows, columns = [int(x) for x in input().split()]
# count = 0
#
# square_matrix = np.array([input().split() for _ in range(rows)])
#
# for i in range(rows - 1):
#     for j in range(columns - 1):
#         block = square_matrix[i:i+2, j:j+2]
#         if np.all(block == block[0, 0]):
#             count += 1
#
# print(count)
