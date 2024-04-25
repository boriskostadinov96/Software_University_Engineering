pens = int(input())
markers = int(input())
liquid = int(input())
discount_percentage = int(input())

total_price = pens * 5.8 + markers * 7.2 + liquid * 1.2
discount_price = total_price - (total_price * (discount_percentage / 100))
print(discount_price)
