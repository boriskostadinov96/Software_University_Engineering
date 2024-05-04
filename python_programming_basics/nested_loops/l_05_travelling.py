destination = input()

while destination != "End":
    needed_money = float(input())
    total_money = 0

    while needed_money > total_money:
        saved_money = float(input())
        total_money += saved_money

    print(f"Going to {destination}!")
    destination = input()

