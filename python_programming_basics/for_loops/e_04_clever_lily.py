age = int(input())
machine_price = float(input())
price_per_toy = int(input())
birthday_toys = 0
birthday_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 != 0:
        birthday_toys += 1

    else:
        birthday_money += int(birthday / 2) * 10
        birthday_money -= 1

sold_toys_money = birthday_toys * price_per_toy
birthday_money += sold_toys_money

if birthday_money >= machine_price:
    print(f"Yes! {birthday_money - machine_price:.2f}")

else:
    print(f"No! {machine_price - birthday_money:.2f}")

