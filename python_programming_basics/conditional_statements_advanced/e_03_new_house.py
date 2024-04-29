flower_type = input()
flowers_count = int(input())
budget = int(input())
result = 0

if flower_type == "Roses":
    result = flowers_count * 5

    if flowers_count > 80:
        result -= result * 0.1

elif flower_type == "Dahlias":
    result = flowers_count * 3.8

    if flowers_count > 90:
        result -= result * 0.15

elif flower_type == "Tulips":
    result = flowers_count * 2.8

    if flowers_count > 80:
        result -= result * 0.15

elif flower_type == "Narcissus":
    result = flowers_count * 3

    if flowers_count < 120:
        result += result * 0.15

elif flower_type == "Gladiolus":
    result = flowers_count * 2.5

    if flowers_count < 80:
        result += result * 0.2

if budget >= result:
    print(f"Hey, you have a great garden with {flowers_count} {flower_type} and {budget - result:.2f} leva left.")

else:
    print(f"Not enough money, you need {result - budget:.2f} leva more.")
