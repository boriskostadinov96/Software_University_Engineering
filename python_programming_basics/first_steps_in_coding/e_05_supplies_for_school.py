pens = int(input())
markers = int(input())
liquid = int(input())
discount_percentage = int(input())

total_sum = pens * 5.8 + markers * 7.2 + liquid * 1.2
discount = total_sum * discount_percentage / 100

print(total_sum - discount)