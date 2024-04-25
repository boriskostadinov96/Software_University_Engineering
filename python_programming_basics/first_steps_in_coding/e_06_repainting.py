nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint + 1.1) * 14.5
thinner_price = thinner * 5

total_price = nylon_price + paint_price + thinner_price + 0.40
workers_price = (total_price * 0.3) * working_hours

final_price = total_price + workers_price
print(final_price)