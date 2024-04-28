degrees = int(input())
day_time = input()
outfit = ""
shoes = ""

if day_time == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

elif day_time == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"

    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"

    else:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif day_time == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"

    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"

    else:
        outfit = "Swim Suit"
        shoes = "Barefoot"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
