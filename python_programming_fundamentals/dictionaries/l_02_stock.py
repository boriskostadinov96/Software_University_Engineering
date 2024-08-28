products = input().split()
searched_products = input().split()
bakery = {}

for el in range(0, len(products), 2):
    key = products[el]
    value = int(products[el + 1])
    bakery[key] = value

for current_product in searched_products:
    if current_product in bakery:
        print(f"We have {bakery[current_product]} of {current_product} left")

    else:
        print(f"Sorry, we don't have {current_product}")