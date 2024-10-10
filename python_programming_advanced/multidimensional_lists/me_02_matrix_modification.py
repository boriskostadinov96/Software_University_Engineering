rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input().split()

while command[0] != "END":
    action = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if not (0 <= row < rows and 0 <= col < rows):
        print("Invalid coordinates")

    elif action == "Add":
        matrix[row][col] += value

    elif action == "Subtract":
        matrix[row][col] -= value

    command = input().split()

[print(*row) for row in matrix]