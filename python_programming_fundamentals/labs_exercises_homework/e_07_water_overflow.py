number_of_lines = int(input())
water_counter = 0
tank_capacity = 255

for line in range(number_of_lines):
    liter_of_water = int(input())
    if tank_capacity - liter_of_water < 0:
        print("Insufficient capacity!" )
        continue

    tank_capacity -= liter_of_water
    water_counter += liter_of_water
print(water_counter)
