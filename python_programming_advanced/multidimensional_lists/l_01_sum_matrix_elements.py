matrix = []
total_amount = 0

rows, columns = [int(el) for el in input().split(", ")]

for row in range(rows):
    rows_columns_data = [int(el) for el in input().split(", ")]
    total_amount += sum(rows_columns_data)
    matrix.append(rows_columns_data)

print(total_amount)
print(matrix)