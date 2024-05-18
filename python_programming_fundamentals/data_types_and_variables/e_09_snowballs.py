snowballs = int(input())
highest_value = 0
best_snowball = (0, 0, 0)

for _ in range(snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality

    if value > highest_value:
        highest_value = value
        best_snowball = (weight, time_needed, quality)

weight, time_needed, quality = best_snowball
print(f"{weight} : {time_needed} = {int(highest_value)} ({quality})")