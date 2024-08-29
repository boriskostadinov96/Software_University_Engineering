command = input()
store = {}

while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in store:
        store[name] = [price, quantity]

    else:
        store[name][0] = price
        store[name][1] += quantity

    command = input()

for key, value in store.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")