from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
command = input()
cars = deque()
total_cars = 0

while command != "END":
    if command != "green":
        cars.append(command)

    else:
        green = green_light_duration

        while green > 0 and cars:
            car = cars.popleft()
            time = green + free_window_duration

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                exit()

            green -= len(car)
            total_cars += 1

    command = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")