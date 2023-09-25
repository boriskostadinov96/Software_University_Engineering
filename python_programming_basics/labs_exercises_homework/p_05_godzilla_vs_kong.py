budget_movie = float(input())
statics_count = int(input())
price_per_clothing = float(input())

dekor_price = budget_movie * 0.1

all_clothing_price = statics_count * price_per_clothing

if statics_count > 150:
    all_clothing_price = all_clothing_price * 0.90

total_sum = dekor_price + all_clothing_price
diff = abs(budget_movie - total_sum)
if budget_movie >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

