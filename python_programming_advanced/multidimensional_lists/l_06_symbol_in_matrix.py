rows = int(input())
square_matrix = []

for _ in range(rows):
    square_matrix.append(list(input()))

searched_symbol = input()

for row_index in range(rows):
    for col_index in range(rows):
        if square_matrix[row_index][col_index] == searched_symbol:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{searched_symbol} does not occur in the matrix")

# 1.1
# import numpy as np
#
# rows = int(input())
# square_matrix = np.array([list(input()) for _ in range(rows)])
#
# searched_symbol = input()
#
# result = np.where(square_matrix == searched_symbol)
#
# if len(result[0]) > 0:
#     print(f"({result[0][0]}, {result[1][0]})")
# else:
#     print(f"{searched_symbol} does not occur in the matrix")
