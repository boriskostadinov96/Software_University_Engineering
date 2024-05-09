fat_percentage = int(input())
protein_percentage = int(input())
carbohydrate_percentage = int(input())
calories_total = int(input())
water_percentage = int(input())

total_fat = (calories_total * fat_percentage / 100) / 9
total_protein = (calories_total * protein_percentage / 100) / 4
total_carbohydrate = (calories_total * carbohydrate_percentage / 100) / 4

food_weight = total_fat + total_protein + total_carbohydrate

calories_per_one_gram = calories_total / food_weight

total_water = 100 - water_percentage
one_gram = (calories_per_one_gram * total_water) / 100

print(f"{one_gram:.4f}")


