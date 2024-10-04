row, col = [int(x) for x in input().split(', ')]
total_sum = 0
matrix = []

for _ in range(row):
    rows = [int(x) for x in input().split(', ')]
    total_sum += sum(rows)
    matrix.append(rows)

print(total_sum)
print(matrix)