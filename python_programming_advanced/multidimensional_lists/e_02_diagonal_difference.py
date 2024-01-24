rows = int(input())
primary_diagonals = []
secondary_diagonals = []

square_matrix = [[int(el) for el in input().split()] for _ in range(rows)]

for current_row_and_column in range(rows):
    primary_diagonals.append(square_matrix[current_row_and_column][current_row_and_column])
    secondary_diagonals.append(square_matrix[current_row_and_column][rows - 1 - current_row_and_column])

primary_diagonals_sum = sum(primary_diagonals)
secondary_diagonals_sum = sum(secondary_diagonals)

print(*{abs(primary_diagonals_sum - secondary_diagonals_sum)})
