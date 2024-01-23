square_matrix_size = int(input())
matrix = []

for _ in range(square_matrix_size):
    matrix.append([int(el) for el in input().split()])
diagonal_sum = 0

for row_index in range(square_matrix_size):
    diagonal_sum += matrix[row_index][row_index]

print(diagonal_sum)
