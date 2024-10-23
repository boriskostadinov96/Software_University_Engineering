from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque(int(x) for x in input().split())
quantities_needed = deque(int(x) for x in input().split())
altitudes = 0
starting_fuel = len(fuel)

while fuel and consumption:
    last_fuel = fuel[-1]
    first_consumption = consumption[0]
    current_quantity = quantities_needed[0]

    if last_fuel - first_consumption >= current_quantity:
        fuel.pop()
        consumption.popleft()
        quantities_needed.popleft()
        altitudes += 1
        print(f"John has reached: Altitude {altitudes}")

    else:
        print(f"John did not reach: Altitude {altitudes + 1}")
        break

if fuel and altitudes:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, altitudes + 1)])}")

if not altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

if starting_fuel == altitudes:
    print("John has reached all the altitudes and managed to reach the top!")