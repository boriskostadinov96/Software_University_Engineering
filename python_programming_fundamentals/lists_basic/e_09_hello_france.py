items = input().split("|")
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150

for item in items:
    type, buying_price = item.split("->")
    buying_price = float(buying_price)
    price_is_valid = False

    if type == "Clothes":
        if buying_price <= 50.00:
            price_is_valid = True

    elif type == "Shoes":
        if buying_price <= 35.00:
            price_is_valid = True

    elif type == "Accessories":
        if buying_price <= 20.50:
            price_is_valid = True

    if price_is_valid:
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.40
            profit += sell_price - buying_price
            sell_prices.append(sell_price)
# Option 1
for sell_price in sell_prices:
    print(f"{sell_price:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")
total_income = budget + sum(sell_prices)

if total_income >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")

# Option 2
# print(" ".join([f"{sell_price:.2f}" for sell_price in sell_prices]))

# Option 3
# sell_prices_as_string = []
# for sell_price in sell_prices:
#     sell_prices_as_string.append(f"{sell_price:.2f}")
# print(" ".join(sell_prices_as_string))

# solution 2
# collection = input().split('|')
# budget = float(input())
# bought_items = []
# train_ticket = 150
# clothes_max_price = 50.00
# shoes_max_price = 35.00
# accessories_max_price = 20.50
#
# for both_parts in collection:
#     item_name, item_price = both_parts.split('->')
#     item_price = float(item_price)
#
#     if budget == 0:
#         break
#
#     if budget < item_price:
#         continue
#
#     if item_name == 'Clothes' and item_price <= clothes_max_price:
#         budget -= item_price
#         bought_items.append(item_price * 1.4)
#
#     elif item_name == 'Shoes' and item_price <= shoes_max_price:
#         budget -= item_price
#         bought_items.append(item_price * 1.4)
#
#     elif item_name == 'Accessories' and item_price <= accessories_max_price:
#         budget -= item_price
#         bought_items.append(item_price * 1.4)
#
# initial_total = sum([price / 1.4 for price in bought_items])
# final_total = sum(bought_items)
# profit = final_total - initial_total
#
#
# budget += final_total
#
#
# final_prices = ' '.join([f'{x:.2f}' for x in bought_items])
# print(final_prices)
# print(f"Profit: {profit:.2f}")
#
# if budget >= train_ticket:
#     print("Hello, France!")
# else:
#     print("Not enough money.")