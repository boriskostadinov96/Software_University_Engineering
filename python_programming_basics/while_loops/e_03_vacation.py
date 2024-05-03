money_needed = float(input())
owned_money = float(input())
days_spending = 0
days_saving = 0
total_days = 0

while owned_money < money_needed:
    action = input()
    action_money = float(input())
    total_days += 1

    if action == "spend":
        owned_money -= action_money
        if owned_money < 0:
            owned_money = 0

    elif action == "save":
        owned_money += action_money

if days_spending == 5:
    print(f"You can't save the money.\n{total_days}")

else:
    print(f"You saved the money for {total_days} days.")
