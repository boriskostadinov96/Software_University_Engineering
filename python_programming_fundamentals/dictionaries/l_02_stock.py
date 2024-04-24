products = input().split()
bakery = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    bakery[key] = value

searched_products = input().split()

for product in searched_products:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")

    else:
        print(f"Sorry, we don't have {product}")