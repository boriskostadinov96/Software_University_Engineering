rest_days = int(input())
room_type = input()
grade = input()
price = 0

if room_type == "room for one person":
    rest_days -= 1
    price = rest_days * 18

elif room_type == "apartment":
    rest_days -= 1

    if rest_days < 10:
        price = (rest_days * 25) * 0.7

    elif 10 <= rest_days <= 15:
        price = (rest_days * 25) * 0.65

    elif rest_days > 15:
        price = (rest_days * 25) * 0.5

elif room_type == "president apartment":
    rest_days -= 1

    if rest_days < 10:
        price = (rest_days * 35) * 0.9

    elif 10 <= rest_days <= 15:
        price = (rest_days * 35) * 0.85

    elif rest_days > 15:
        price = (rest_days * 35) * 0.8

if grade == "positive":
    print(f"{price * 1.25:.2f}")

else:
    print(f"{price * 0.9:.2f}")
