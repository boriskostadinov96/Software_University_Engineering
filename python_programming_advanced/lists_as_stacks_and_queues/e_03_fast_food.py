from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]

    if food >= current_order:
        orders.popleft()
        food -= current_order

    else:
        print(f"Orders left:", *orders)
        break

else:
    print("Orders complete")
