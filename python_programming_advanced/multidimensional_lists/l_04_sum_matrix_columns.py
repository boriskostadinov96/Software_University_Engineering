rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col_idx in range(cols):
    total_cols = 0

    for row_idx in range(rows):
        total_cols += matrix[row_idx][col_idx]

    print(total_cols)