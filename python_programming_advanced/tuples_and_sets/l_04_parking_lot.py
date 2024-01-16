cars_count = int(input())
unique_car_numbers = set()

for _ in range(cars_count):
    cars_data = input().split(", ")
    car_action, car_number = cars_data

    if car_action == "IN":
        unique_car_numbers.add(car_number)

    elif car_action == "OUT":

        if car_number in unique_car_numbers:
            unique_car_numbers.remove(car_number)

if unique_car_numbers:
    for unique_car in unique_car_numbers:
        print(unique_car)

else:
    print("Parking Lot is Empty")