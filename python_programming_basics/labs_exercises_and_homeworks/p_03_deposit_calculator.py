deposite_amount = float(input())

deposit_month_time = int(input())

annual_rate = float(input())

per_year = deposite_amount * (annual_rate / 100)

per_month = per_year / 12

total_sum = deposite_amount + (deposit_month_time * per_month)
print(total_sum)