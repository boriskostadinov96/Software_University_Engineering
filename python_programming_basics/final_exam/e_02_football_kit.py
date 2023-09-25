tshirt_price = float(input())
needed_sum = float(input())

shorts_price = tshirt_price * 0.75
socs_price = shorts_price * 0.20
shoes_price = (tshirt_price + shorts_price) * 2

total_sum = tshirt_price + shorts_price + + socs_price + shoes_price
total_sum -= total_sum * 0.15

if total_sum >= needed_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")

else:
    needed_money = needed_sum - total_sum
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money:.2f} lv. more.")
