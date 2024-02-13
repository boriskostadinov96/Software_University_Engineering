from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_indexes = deque([int(x) for x in input().split()])
quantities = deque([int(x) for x in input().split()])
altitudes = 0
max_altitude_count = len(initial_fuel)

while True:
    last_fuel = initial_fuel[-1]
    first_additional_consumption = consumption_indexes[0]
    first_element = quantities[0]

    result = last_fuel - first_additional_consumption

    if result >= first_element:
        initial_fuel.pop()
        consumption_indexes.popleft()
        quantities.popleft()
        altitudes += 1
        print(f"John has reached: Altitude {altitudes}")

    else:
        print(f"John did not reach: Altitude {altitudes + 1}")
        break

if initial_fuel and altitudes:
    print(
        f"John failed to reach the top.\nReached altitudes: {', '.join([f'Altitude {num}' for num in range(1, altitudes + 1)])}")
elif max_altitude_count > altitudes and not altitudes:
    print(f"John failed to reach the top.")
    print(f"John didn't reach any altitude.")

if max_altitude_count == altitudes:
    print(f"John has reached all the altitudes and managed to reach the top!")
