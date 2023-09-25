fat_percentage = int(input())
protein_percentage = int(input())
carbohydrates_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())

fat_grams = (fat_percentage / 100) * total_calories / 9
protein_grams = (protein_percentage / 100) * total_calories / 4
carbohydrates_grams = (carbohydrates_percentage / 100) * total_calories / 4

total_weight = fat_grams + protein_grams + carbohydrates_grams

calories_per_gram = total_calories / total_weight
calories_without_water = calories_per_gram * (100 - water_percentage) / 100

print(f"{calories_without_water:.4f}")