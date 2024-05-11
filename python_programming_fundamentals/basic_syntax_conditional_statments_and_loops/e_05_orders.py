orders = int(input())
total_price = 0

for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue

    elif days < 1 or days > 31:
        continue

    elif capsules_needed < 1 or capsules_needed > 2000:
        continue

    coffee_price = price_per_capsule * capsules_needed * days
    total_price += coffee_price

    print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_price:.2f}")