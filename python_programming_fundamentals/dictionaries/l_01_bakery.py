food = input().split()
bakery = {}

for index in range(0, len(food), 2):
    key = food[index]
    value = int(food[index + 1])
    bakery[key] = value

print(bakery)
