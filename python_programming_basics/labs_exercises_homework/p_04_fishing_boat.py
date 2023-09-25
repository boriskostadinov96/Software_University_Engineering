budget = int(input())
season = input()
fisherman_count = int(input())
rent_price = 0

if season == 'Spring':
    rent_price = 3000
elif season == 'Summer' or season == 'Autumn':
    rent_price = 4200
elif season == 'Winter':
    rent_price = 2600

if fisherman_count <= 6:
    rent_price = rent_price * 0.90
elif 6 < fisherman_count <= 11:
    rent_price = rent_price * 0.85
elif fisherman_count > 11:
    rent_price = rent_price * 0.75

if fisherman_count % 2 == 0 and season != 'Autumn':
    rent_price = rent_price * 0.95

diff = abs(budget - rent_price)
if budget >= rent_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
