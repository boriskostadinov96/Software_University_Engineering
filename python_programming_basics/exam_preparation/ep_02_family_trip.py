budget = float(input())
nights_count = int(input())
price_per_one_night = float(input())
expenses = int(input())

if nights_count > 7:
    price_per_one_night = price_per_one_night * 0.95

total_price = nights_count * price_per_one_night
extra_expenses = budget * expenses / 100

needed_money = total_price + extra_expenses

if budget >= needed_money:
    print(f"Ivanovi will be left with {budget - needed_money:.2f} leva after vacation.")

else:
    print(f"{needed_money - budget:.2f} leva needed.")

