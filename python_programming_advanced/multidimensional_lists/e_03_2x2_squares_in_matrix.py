rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
total_squares = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            total_squares += 1

print(total_squares)
