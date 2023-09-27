type_flowers = input()
flowers_count = int(input())
budget = int(input())
total_sum = 0

if type_flowers == 'Roses':
    total_sum = 5 * flowers_count
    if flowers_count > 80:
        total_sum = total_sum * 0.9

elif type_flowers == 'Dahlias':
    total_sum = 3.8 * flowers_count
    if flowers_count > 90:
        total_sum = total_sum * 0.85

elif type_flowers == 'Tulips':
    total_sum = 2.8 * flowers_count
    if flowers_count > 80:
        total_sum = total_sum * 0.85

elif type_flowers == 'Narcissus':
    total_sum = 3 * flowers_count
    if flowers_count < 120:
        total_sum = total_sum * 0.85

elif type_flowers == 'Gladiolus':
    total_sum = 2.5 * flowers_count
    if flowers_count < 80:
        total_sum = total_sum * 1.20

diff = abs(total_sum - budget)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {flowers_count} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")