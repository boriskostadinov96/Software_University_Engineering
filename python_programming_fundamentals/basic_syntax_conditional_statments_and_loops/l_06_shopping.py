budget = int(input())
command = input()

while command != "End":
    product_price = int(command)
    budget -= product_price

    if budget < 0:
        print(f'You went in overdraft!')
        break

    command = input()

else:
    print(f"You bought everything needed.")

# solution 2
# budget = int(input())
# total_price = 0
# overdraft = False
#
# while True:
#     price = input()
#
#     if price == "End":
#         break
#
#     total_price += int(price)
#
#     if budget < total_price:
#         overdraft = True
#         break
#
#     else:
#         overdraft = False
#
# if overdraft:
#     print("You went in overdraft!")
#
# else:
#     print("You bought everything needed.")
