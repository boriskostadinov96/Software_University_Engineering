decorations_quantity = int(input())
days_left = int(input())
budget = 0
spirit_points = 0

for current_day in range(1, days_left + 1):

    if current_day % 11 == 0:
        decorations_quantity += 2

    if current_day % 2 == 0:
        budget += decorations_quantity * 2
        spirit_points += 5

    if current_day % 3 == 0:
        budget += decorations_quantity * 8
        spirit_points += 13

    if current_day % 5 == 0:
        budget += decorations_quantity * 15
        spirit_points += 17

        if current_day % 3 == 0:
            spirit_points += 30

    if current_day % 10 == 0:
        spirit_points -= 20
        budget += 23

if days_left % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")
