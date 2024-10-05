rows, cols = [int(x) for x in input().split(', ')]
matrix = []
biggest_sum = float('-inf')
sub_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row_idx in range(rows-1):
    for col_idx in range(cols-1):
        current_el = matrix[row_idx][col_idx]
        next_el = matrix[row_idx][col_idx+1]
        under_el = matrix[row_idx+1][col_idx]
        diagonal_el = matrix[row_idx+1][col_idx+1]

        total_sum = current_el + next_el + under_el + diagonal_el

        if biggest_sum < total_sum:
            biggest_sum = total_sum
            sub_matrix = [[current_el, next_el], [under_el, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(biggest_sum)


# 1.1
# import numpy as np
#
# rows, cols = [int(x) for x in input().split(', ')]
#
# matrix = np.array([list(map(int, input().split(', '))) for _ in range(rows)])
#
# biggest_sum = float('-inf')
# sub_matrix = None
#
# for row_idx in range(rows - 1):
#     for col_idx in range(cols - 1):
#         current_sub_matrix = matrix[row_idx:row_idx + 2, col_idx:col_idx + 2]
#         total_sum = np.sum(current_sub_matrix)
#
#         if total_sum > biggest_sum:
#             biggest_sum = total_sum
#             sub_matrix = current_sub_matrix
#
# print(sub_matrix[0][0], sub_matrix[0][1])
# print(sub_matrix[1][0], sub_matrix[1][1])
# print(biggest_sum)
