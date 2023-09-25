# Четене на броя дни
days = int(input())

total_liters = 0
total_degrees = 0

# Обхождане на всеки ден
for day in range(1, days + 1):
    # Четене на данни за текущия ден
    liters = float(input())
    degrees = float(input())

    # Натрупване на общите литри и градуси
    total_liters += liters
    total_degrees += (liters * degrees)

# Пресмятане на средния градус
average_degrees = total_degrees / total_liters

# Извеждане на резултата
print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

# Проверка за градусите и извеждане на подходящо съобщение
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")