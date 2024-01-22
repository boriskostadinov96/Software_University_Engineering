rows = int(input())
flatten_matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(", ")]

    for el in elements:
        flatten_matrix.append(el)

print(flatten_matrix)


# 1.1
#
# rows = int(input())
# flatten_matrix = []
#
# for row in range(rows):
#     elements = [int(el) for el in input().split(", ")]
#
#     flatten_matrix.extend(elements)
#
# print(flatten_matrix)