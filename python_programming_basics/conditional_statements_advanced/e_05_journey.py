budget = float(input())
season = input()
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        place = "Camp"
        budget *= 0.3

    else:
        place = "Hotel"
        budget *= 0.7

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        place = "Camp"
        budget *= 0.4

    else:
        place = "Hotel"
        budget *= 0.8

else:
    destination = "Europe"
    place = "Hotel"
    budget *= 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")



