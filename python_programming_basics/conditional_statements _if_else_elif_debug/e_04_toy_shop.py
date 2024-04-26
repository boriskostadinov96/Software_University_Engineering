trip_price = float(input())
puzzels_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

toys_price = puzzels_count * 2.6 + dolls_count * 3 + bears_count * 4.1 + minions_count * 8.2 + trucks_count * 2
toys_count = puzzels_count + dolls_count + bears_count + minions_count + trucks_count

if toys_count >= 50:
    discount = toys_price * 0.25
else:
    discount = 0

total_price = toys_price - discount
rent_price = total_price * 0.1
profit = total_price - rent_price

if profit >= trip_price:
    print(f"Yes! {profit - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
