month = input()
sleeps_count = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = sleeps_count * 50
    apartment_price = sleeps_count * 65

    if sleeps_count > 14:
        studio_price -= studio_price * 0.3

    elif sleeps_count > 7:
        studio_price -= studio_price * 0.05

elif month == "June" or month == "September":
    studio_price = sleeps_count * 75.2
    apartment_price = sleeps_count * 68.7

    if sleeps_count > 14:
        studio_price -= studio_price * 0.2

elif month == "July" or month == "August":
    studio_price = sleeps_count * 76
    apartment_price = sleeps_count * 77

if sleeps_count > 14:
    apartment_price -= apartment_price * 0.1

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
