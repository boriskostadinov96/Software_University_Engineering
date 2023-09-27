pens_count = int(input())
markers_count = int(input())
preparation_count = int(input())
discount_percent = int(input())

price_pen = pens_count * 5.80
price_markers = markers_count * 7.20
price_preparation = preparation_count * 1.20

total_price = price_pen + price_markers + price_preparation
discount = total_price * (discount_percent / 100)
price_with_discount = total_price - discount
print(price_with_discount)
