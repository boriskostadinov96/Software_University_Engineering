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