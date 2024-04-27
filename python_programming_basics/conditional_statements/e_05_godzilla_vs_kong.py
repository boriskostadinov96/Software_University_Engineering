movie_budget = float(input())
people_count = int(input())
price_per_cloth = float(input())

decor = movie_budget * 0.1
price_for_clothing = people_count * price_per_cloth


if people_count > 150:
    price_for_clothing -= price_for_clothing * 0.1

total_sum = price_for_clothing + decor

if total_sum > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - movie_budget:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - total_sum:.2f} leva left.")
