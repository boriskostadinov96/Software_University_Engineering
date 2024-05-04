floors_count = int(input())
rooms_count = int(input())
floor_type = ""

for current_floor in range(floors_count, 0, -1):
    if current_floor == floors_count:
        floor_type = "L"

    elif current_floor % 2 == 0:
        floor_type = "O"

    else:
        floor_type = "A"

    for current_room in range(rooms_count):
        print(f"{floor_type}{current_floor}{current_room}", end=" ")
    print()
