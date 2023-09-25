target = int(input())
earned_money = 0

while True:
    command = input()

    if command == "closed":
        break

    if command == "haircut":
        service = input()
        if service == "mens":
            earned_money += 15
        elif service == "ladies":
            earned_money += 20
        elif service == "kids":
            earned_money += 10

    elif command == "color":
        service = input()
        if service == "touch up":
            earned_money += 20
        elif service == "full color":
            earned_money += 30

    if earned_money >= target:
        print("You have reached your target for the day!")
        break

if earned_money < target:
    needed_money = target - earned_money
    print(f"Target not reached! You need {needed_money}lv. more.")
print(f"Earned money: {earned_money}lv.")