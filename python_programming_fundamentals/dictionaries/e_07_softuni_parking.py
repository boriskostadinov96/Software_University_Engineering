n = int(input())
drivers = {}

for _ in range(n):
    clients_data = input().split()

    parking_action = clients_data[0]
    driver_name = clients_data[1]

    if parking_action == 'register':
        car_plate = clients_data[2]
        if driver_name in drivers:
            print(f"ERROR: already registered with plate number {drivers[driver_name]}")

        else:
            drivers[driver_name] = car_plate
            print(f"{driver_name} registered {car_plate} successfully")

    elif parking_action == 'unregister':
        if driver_name not in drivers:
            print(f"ERROR: user {driver_name} not found")

        else:
            del drivers[driver_name]
            print(f"{driver_name} unregistered successfully")

for key, value in drivers.items():
    print(f"{key} => {value}")
