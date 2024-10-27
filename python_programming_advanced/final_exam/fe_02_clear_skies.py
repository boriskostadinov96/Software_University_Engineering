def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


size = int(input())
jet_position = None
matrix = []
armor = 300
direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def custom_input():
    return input()


for row_index in range(size):
    data = list(input())

    if "J" in data:
        col_index = data.index("J")
        jet_position = [row_index, col_index]
    matrix.append(data)

direction = custom_input()

while armor > 0:
    current_row_index, current_col_index = jet_position
    row_movement, col_movement = direction_mapper.get(direction, (0, 0))
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    if not armor:
        print("Mission failed! The jetfighter went outside the airspace.")
        break

    symbol = matrix[desired_row_index][desired_col_index]
    matrix[desired_row_index][desired_col_index] = "J"
    matrix[current_row_index][current_col_index] = "-"
    jet_position = [desired_row_index, desired_col_index]

    if symbol == "E":
        armor -= 100
        if armor <= 0:
            print(
                f"Mission failed, your jetfighter was shot down! Last coordinates [{desired_row_index}, {desired_col_index}]!")
            break
        matrix[desired_row_index][desired_col_index] = "-"
    elif symbol == "R":
        armor = min(armor + 200, 300)
        matrix[desired_row_index][desired_col_index] = "-"

    direction = custom_input()

if armor > 0:
    print("Mission accomplished, you neutralized the aerial threat!")

print_matrix(matrix)