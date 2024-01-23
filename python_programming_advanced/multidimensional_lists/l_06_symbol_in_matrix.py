rows = int(input())
square_matrix = []

for _ in range(rows):
    square_matrix.append(list(input()))

some_symbol = input()

for row_index in range(rows):
    for col_index in range(len(square_matrix[row_index])):
        if square_matrix[row_index][col_index] == some_symbol:
            print(f"({row_index}, {col_index})")
            exit()


print(f"{some_symbol} does not occur in the matrix")

