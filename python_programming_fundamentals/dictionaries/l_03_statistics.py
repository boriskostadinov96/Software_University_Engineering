command = input()
total_products = 0
total_quantity = 0
bakery = {}

while command != 'statistics':
    product, quantity = command.split(': ')
    quantity = int(quantity)

    if product not in bakery:
        bakery[product] = quantity
        total_products += 1

    else:
        bakery[product] += quantity

    total_quantity = sum(bakery.values())

    command = input()

print("Products in stock:")

for key, value in bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
