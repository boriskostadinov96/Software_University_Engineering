from collections import deque

money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())
foods = 0

while money and prices:
    last_money = money.pop()
    first_price = prices.popleft()

    if last_money > first_price:
        change = last_money - first_price
        if money:
            money[-1] += change
        foods += 1

    elif last_money == first_price:
        foods += 1

if foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")

elif foods == 1:
    print(f"Henry ate: {foods} food.")

elif not foods:
    print("Henry remained hungry. He will try next weekend again.")

else:
    print(f"Henry ate: {foods} foods.")


# 1.1
#
# from collections import deque
#
# amount_of_money = [int(x) for x in input().split()]
# price_of_foods = deque([int(x) for x in input().split()])
# foods = 0
#
# while amount_of_money and price_of_foods:
#     last_money_amount = amount_of_money[-1]
#     first_price = price_of_foods[0]
#
#     if last_money_amount == first_price:
#         amount_of_money.pop()
#         price_of_foods.popleft()
#         foods += 1
#
#     elif last_money_amount > first_price:
#         change = last_money_amount - first_price
#         amount_of_money.pop()
#         price_of_foods.popleft()
#
#         if amount_of_money:
#             next_amount = amount_of_money[-1] + change
#             amount_of_money[-1] = next_amount
#         foods += 1
#
#     elif last_money_amount < first_price:
#         amount_of_money.pop()
#         price_of_foods.popleft()
#
# if foods >= 4:
#     print(f"Gluttony of the day! Henry ate {foods} foods.")
# elif foods > 0:
#     print(f"Henry ate: {foods} {'foods' if foods > 1 else 'food'}.")
# else:
#     print("Henry remained hungry. He will try next weekend again.")