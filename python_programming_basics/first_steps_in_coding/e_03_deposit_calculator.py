deposit = float(input())
months = int(input())
annual_interest_percent = float(input())

year_interest = deposit * annual_interest_percent / 100  # Това ще ни даде парите които ще получим за една година
monthly_interest = year_interest / 12  # Това ще ни даде парите които ще получим за една месец

total_sum = deposit + months * monthly_interest
print(total_sum)

