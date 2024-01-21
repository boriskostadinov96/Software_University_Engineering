rows = int(input())
matrix = []

for row in range(rows):
    columns_elements = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(columns_elements)

print(matrix)