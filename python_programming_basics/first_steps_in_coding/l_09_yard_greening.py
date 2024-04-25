square_meters = float(input())
yard_price = (square_meters * 7.61)
discount = yard_price * 0.18

total_price = yard_price - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")