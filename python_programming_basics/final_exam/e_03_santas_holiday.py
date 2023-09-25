# Вход
rest_days = int(input())
room_type = input()
grade = input()

# Цени на помещенията
room_price = 0

if room_type == "room for one person":
    room_price = 18.00
elif room_type == "apartment":
    room_price = 25.00
elif room_type == "president apartment":
    room_price = 35.00

# Пресмятане на цената за престоя
total_price = room_price * (rest_days - 1)  # Защото първия ден не се приспада
if rest_days < 10:
    if room_type == "apartment":
        total_price *= 0.70
    elif room_type == "president apartment":
        total_price *= 0.90
elif 10 <= rest_days <= 15:
    if room_type == "apartment":
        total_price *= 0.65
    elif room_type == "president apartment":
        total_price *= 0.85
elif rest_days > 15:
    if room_type == "apartment":
        total_price *= 0.50
    elif room_type == "president apartment":
        total_price *= 0.80

# Приспадане или добавяне на проценти според оценката
if grade == "positive":
    total_price *= 1.25
elif grade == "negative":
    total_price *= 0.90

# Отпечатване на крайната цена
print(f"{total_price:.2f}")
