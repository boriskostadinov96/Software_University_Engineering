def player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")

def check_valid_index(row, col):
    return 0 <= row < rows and 0 <= col < cols

def check_player_is_alive(row, col):
    if matrix[row][col] == "B":
        show_results("dead")

def bunnies_positions():
    positions_matrix = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                positions_matrix.append([row, col])

    return positions_matrix

def bunnies_movement():
    new_bunny_positions = []
    for row, col in bunnies_positions():
        for bunnie_move in directions.values():
            new_row, new_col = row + bunnie_move[0], col + bunnie_move[1]

            if check_valid_index(new_row, new_col):
                new_bunny_positions.append((new_row, new_col))

    for new_row, new_col in new_bunny_positions:
        matrix[new_row][new_col] = "B"

def show_results(status):
    [print(''.join(row)) for row in matrix]
    print(f"{status}: {player_row} {player_col}")
    raise SystemExit

# Input and setup
rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = input()

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

# Find initial player position
player_row, player_col = player_position()
matrix[player_row][player_col] = '.'  # Remove player from the current spot for now

# Process each command
for command in commands:
    # Move player
    new_player_row = player_row + directions[command][0]
    new_player_col = player_col + directions[command][1]

    if not check_valid_index(new_player_row, new_player_col):
        # Player escapes the lair
        bunnies_movement()  # Bunnies still move after the player escapes
        show_results("won")

    # Check if the player dies by moving into a bunny
    if matrix[new_player_row][new_player_col] == "B":
        player_row, player_col = new_player_row, new_player_col
        bunnies_movement()  # Bunnies still move after the player dies
        show_results("dead")

    # Update player's position
    player_row, player_col = new_player_row, new_player_col

    # Spread bunnies after player's move
    bunnies_movement()

    # Check if the player dies after bunnies move
    if matrix[player_row][player_col] == "B":
        show_results("dead")

# If no result yet (i.e., player hasn't won or died by end of moves)
show_results("won")
