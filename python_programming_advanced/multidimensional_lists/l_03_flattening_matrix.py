rows = int(input())
flatten_matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    flatten_matrix.extend(data)

print(flatten_matrix)

# 1.1
# rows = int(input())
# matrix = []
# flatten_matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(', ')])
#
# for array in matrix:
#     for el in array:
#         flatten_matrix.append(el)
#
# print(flatten_matrix)