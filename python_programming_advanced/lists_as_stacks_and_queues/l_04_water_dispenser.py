from collections import deque

quantity_of_water = int(input())
current_name = input()
queue_of_peoples = deque()

while current_name != "Start":
    queue_of_peoples.append(current_name)

    current_name = input()

command = input()

while command != "End":
    data = command.split()

    if len(data) == 1:
        requested_water = int(data[0])
        current_person = queue_of_peoples.popleft()

        if quantity_of_water >= requested_water:
            print(f"{current_person} got water")
            quantity_of_water -= requested_water

        else:
            print(f"{current_person} must wait")

    elif len(data) > 1:
        _, liters_to_add = data
        quantity_of_water += int(liters_to_add)

    command = input()

print(f"{quantity_of_water} liters left")