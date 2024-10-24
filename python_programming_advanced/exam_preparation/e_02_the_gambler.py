def valid_board_range(row_idx, col_idx, num):
    return 0 <= row_idx < num and 0 <= col_idx < num


def display_board(matrix):
    for row_idx in matrix:
        print("".join(row_idx))


n = int(input())
board = []
gambler = None
cash = 100

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

for current_row in range(n):
    rows = list(input())
    if "G" in rows:
        current_col = rows.index("G")
        gambler = [current_row, current_col]
    board.append(rows)

direction = input()

while direction != "end":
    row, col = gambler
    row_move, col_move = directions[direction]

    nex_row = row + row_move
    nex_col = col + col_move

    if not valid_board_range(nex_row, nex_col, n):
        print("Game over! You lost everything!")
        raise SystemExit

    element = board[nex_row][nex_col]

    board[nex_row][nex_col] = "G"
    board[row][col] = "-"

    gambler = [nex_row, nex_col]

    if element == "W":
        cash += 100

    elif element == "P":
        cash -= 200

        if cash <= 0:
            print("Game over! You lost everything!")
            raise SystemExit

    elif element == "J":
        cash += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {cash}$")
        display_board(board)
        raise SystemExit

    direction = input()

if cash > 0:
    print(f"End of the game. Total amount: {cash}$")
    display_board(board)