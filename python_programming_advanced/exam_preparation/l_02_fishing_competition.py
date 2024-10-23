def check_valid_positions(fisherman, directions, command, matrix):
    fisherman_row, fisherman_col = fisherman
    row, col = directions[command]

    next_row = fisherman_row + row
    next_col = fisherman_col + col

    if next_row < 0:
        next_row = len(matrix) - 1
    elif next_row >= len(matrix):
        next_row = 0

    if next_col < 0:
        next_col = len(matrix[0]) - 1
    elif next_col >= len(matrix[0]):
        next_col = 0

    return next_row, next_col


n = int(input())
matrix = []
fisherman = None
fish = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for current_row in range(n):
    rows = list(input())

    if "S" in rows:
        current_col = rows.index("S")
        fisherman = [current_row, current_col]

    matrix.append(rows)

command = input()

while command != "collect the nets":
    current_row_index, current_col_index = fisherman
    desired_row, desired_col = check_valid_positions(fisherman, directions, command, matrix)

    element = matrix[desired_row][desired_col]

    matrix[desired_row][desired_col] = "S"
    matrix[current_row_index][current_col_index] = "-"
    fisherman = [desired_row, desired_col]

    if element.isdigit():
        fish += int(element)
    elif element == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{desired_row},{desired_col}]")
        exit()

    command = input()

if fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish} tons of fish more.")

if fish > 0:
    print(f"Amount of fish caught: {fish} tons.")

for row in matrix:
    print("".join(row))
