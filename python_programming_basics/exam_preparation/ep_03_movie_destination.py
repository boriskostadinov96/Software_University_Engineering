budget = float(input())
destination = input()
season = input()
days_count = int(input())
total_price = 0

if season == "Winter":
    if destination == "Dubai":
        total_price = (days_count * 45_000) * 0.7

    elif destination == "Sofia":
        total_price = (days_count * 17_000) * 1.25

    elif destination == "London":
        total_price = (days_count * 24_000)

elif season == "Summer":
    if destination == "Dubai":
        total_price = (days_count * 40_000) * 0.7

    elif destination == "Sofia":
        total_price = (days_count * 12_500) * 1.25

    elif destination == "London":
        total_price = (days_count * 20_250)

if budget >= total_price:
    print(f"The budget for the movie is enough! We have {budget - total_price:.2f} leva left!")

else:
    print(f"The director needs {total_price - budget:.2f} leva more!")



