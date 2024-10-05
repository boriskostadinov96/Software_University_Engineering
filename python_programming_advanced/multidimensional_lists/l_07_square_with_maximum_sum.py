rows, cols = [int(x) for x in input().split(', ')]
matrix = []
biggest_sum = float('-inf')
sub_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row_idx in range(rows-1):
    for col_idx in range(cols-1):
        current_el = matrix[row_idx][col_idx]
        next_el = matrix[row_idx][col_idx+1]
        under_el = matrix[row_idx+1][col_idx]
        diagonal_el = matrix[row_idx+1][col_idx+1]

        total_sum = current_el + next_el + under_el + diagonal_el

        if biggest_sum < total_sum:
            biggest_sum = total_sum
            sub_matrix = [[current_el, next_el], [under_el, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(biggest_sum)
