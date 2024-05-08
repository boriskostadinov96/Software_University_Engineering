days_count = int(input())
total_food = float(input())
total_eaten_dog_food = 0
total_eaten_cat_food = 0
total_biscuits = 0

for current_day in range(1, days_count + 1):
    dog_food = int(input())
    cat_food = int(input())

    total_eaten_dog_food += dog_food
    total_eaten_cat_food += cat_food

    if current_day % 3 == 0:
        biscuits = (dog_food + cat_food) * 0.1
        total_biscuits += biscuits

final_food = total_eaten_cat_food + total_eaten_dog_food

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{(final_food / total_food) * 100:.2f}% of the food has been eaten.")
print(f"{(total_eaten_dog_food / final_food) * 100:.2f}% eaten from the dog.")
print(f"{(total_eaten_cat_food / final_food) * 100:.2f}% eaten from the cat.")
