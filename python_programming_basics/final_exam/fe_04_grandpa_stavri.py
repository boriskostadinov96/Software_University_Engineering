days = int(input())
total_alcohol = 0
total_degrees = 0

for _ in range(1, days + 1):
    alcohol = float(input())
    current_degrees = float(input())

    total_degrees += alcohol * current_degrees
    total_alcohol += alcohol

average_degrees = total_degrees / total_alcohol

print(f"Liter: {total_alcohol:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")

elif 38 <= average_degrees <= 42:
    print("Super!")

else:
    print("Dilution with distilled water!")