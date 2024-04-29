budget = int(input())
season = input()
fisherman_count = int(input())
rent = 0

if season == "Spring":
    rent = 3000

    if fisherman_count <= 6:
        rent *= 0.9

    elif 7 <= fisherman_count <= 11:
        rent *= 0.85

    elif fisherman_count >= 12:
        rent *= 0.75

elif season == "Summer":
    rent = 4200

    if fisherman_count <= 6:
        rent *= 0.9

    elif 7 <= fisherman_count <= 11:
        rent *= 0.85

    elif fisherman_count >= 12:
        rent *= 0.75

elif season == "Autumn":
    rent = 4200

    if fisherman_count <= 6:
        rent *= 0.9

    elif 7 <= fisherman_count <= 11:
        rent *= 0.85

    elif fisherman_count >= 12:
        rent *= 0.75

elif season == "Winter":
    rent = 2600

    if fisherman_count <= 6:
        rent *= 0.9

    elif 7 <= fisherman_count <= 11:
        rent *= 0.85

    elif fisherman_count >= 12:
        rent *= 0.75

if fisherman_count % 2 == 0 and season != "Autumn":
    rent *= 0.95

if budget >= rent:
    print(f"Yes! You have {budget - rent:.2f} leva left.")

else:
    print(f"Not enough money! You need {rent - budget:.2f} leva.")

