days = int(input())
place = input()
grade = input()
price = 0

if place == "room for one person":
    price = (days - 1) * 18

elif place == "apartment":
    price = (days - 1) * 25

    if days < 10:
        price -= price * 0.3

    elif 10 <= days <= 15:
        price -= price * 0.35

    elif days > 15:
        price -= price * 0.5

elif place == "president apartment":
    price = (days - 1) * 35

    if days < 10:
        price -= price * 0.1

    elif 10 <= days <= 15:
        price -= price * 0.15

    elif days > 15:
        price -= price * 0.2

if grade == "positive":
    price += price * 0.25

else:
    price -= price * 0.1

print(f"{price:.2f}")