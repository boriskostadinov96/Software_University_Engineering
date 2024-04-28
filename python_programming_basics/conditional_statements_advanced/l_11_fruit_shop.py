working_days_prices = {"banana": 2.5, "apple": 1.2, "orange": 0.85,
                       "grapefruit": 1.45, "kiwi": 2.7, "pineapple": 5.5, "grapes": 3.85}

weekend_days_prices = {"banana": 2.7, "apple": 1.25, "orange": 0.90,
                       "grapefruit": 1.6, "kiwi": 3.0, "pineapple": 5.6, "grapes": 4.2}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]
result = 0

fruit = input()
day = input()
quantity = float(input())

if fruit in working_days_prices and day in days:
    result = quantity * working_days_prices[fruit]
    print(f"{result:.2f}")

elif fruit in weekend_days_prices and day in weekend_days:
    result = quantity * weekend_days_prices[fruit]
    print(f"{result:.2f}")

else:
    print("error")
