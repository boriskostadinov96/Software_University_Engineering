rows = int(input())
primary_diagonal = []
secondary_diagonal = []

square_matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

for row in range(rows):
    primary_diagonal.append(square_matrix[row][row])
    secondary_diagonal.append(square_matrix[row][rows - 1 - row])

print(f"Primary diagonal: {', '.join(str(x) for x in  primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in  secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

# 1.1
# rows = int(input())
#
# square_matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]
#
# primary = [square_matrix[r][r] for r in range(rows)]
# second = [square_matrix[r][rows - r - 1] for r in range(rows)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")

# 1.2
# import numpy as np
#
# rows = int(input())
#
# square_matrix = np.array([list(map(int, input().split(', '))) for _ in range(rows)])
#
# primary_diagonal = np.diag(square_matrix)
# secondary_diagonal = np.diag(np.fliplr(square_matrix))
#
# print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {np.sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {np.sum(secondary_diagonal)}")
