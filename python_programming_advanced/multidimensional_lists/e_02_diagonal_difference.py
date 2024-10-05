n = int(input())
square_matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = sum([square_matrix[r][r] for r in range(n)])
secondary_diagonal = sum([square_matrix[r][n - r - 1] for r in range(n)])

print(abs(primary_diagonal - secondary_diagonal))

# 1.1
# import numpy as np
#
# n = int(input())
# square_matrix = np.array([[int(x) for x in input().split()] for _ in range(n)])
#
# primary_diagonal = sum(np.diagonal(square_matrix))
# secondary_diagonal = sum(np.diagonal(np.fliplr(square_matrix)))
#
# print(abs(primary_diagonal - secondary_diagonal))