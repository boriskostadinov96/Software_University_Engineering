rows = int(input())

square_matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

primary = [square_matrix[r][r] for r in range(rows)]
second = [square_matrix[r][rows - r - 1] for r in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")