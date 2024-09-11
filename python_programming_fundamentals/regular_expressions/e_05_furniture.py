import re

purchases = input()
furniture = []
total_cost = 0
pattern = ">([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

while purchases != "Purchase":
    match = re.search(pattern, purchases)

    if match:
        product, price, quantity = match.groups()
        furniture.append(product)
        total_cost += float(price) * int(quantity)

    purchases = input()

print("Bought furniture:")

for stock in furniture:
    print(stock)

print(f"Total money spend: {total_cost:.2f}")