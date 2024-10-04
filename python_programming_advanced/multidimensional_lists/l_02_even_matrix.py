rows = int(input())
matrix = []

for _ in range(rows):
    rows_data = [int(x) for x in input().split(', ')]
    matrix.append([el for el in rows_data if el % 2 == 0])

print(matrix)

# 1.1
# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     rows_elements = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
#     matrix.append(rows_elements)
#
# print(matrix)