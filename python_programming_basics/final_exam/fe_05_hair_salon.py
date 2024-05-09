target = int(input())
command = input()
profit = 0
target_reached = False

while command != "closed":
    type_service = input()

    if command == "haircut":
        if type_service == "mens":
            profit += 15

        elif type_service == "ladies":
            profit += 20

        elif type_service == "kids":
            profit += 10

    elif command == "color":
        if type_service == "touch up":
            profit += 20

        elif type_service == "full color":
            profit += 30

    if profit >= target:
        target_reached = True
        break

    else:
        target_reached = False

    command = input()

if target_reached:
    print("You have reached your target for the day!")
    print(f"Earned money: {profit}lv.")

else:
    print(f"Target not reached! You need {target - profit}lv. more.")
    print(f"Earned money: {profit}lv.")