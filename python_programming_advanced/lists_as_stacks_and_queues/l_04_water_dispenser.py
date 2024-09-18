from collections import deque

water = int(input())
name = input()
people = deque()

while name != "Start":
    people.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        liters = int(command)

        if water >= liters:
            person_name = people.popleft()
            water -= liters
            print(f"{person_name} got water")

        else:
            person_name = people.popleft()
            print(f"{person_name} must wait")

    else:
        _, liters = command.split()
        water += int(liters)

    command = input()

print(f"{water} liters left")