command = input().split("||")
cities = {}

while command[0] != "Sail":
    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city not in cities:
        cities[city] = [population, gold]

    else:
        cities[city][0] += population
        cities[city][1] += gold

    command = input().split("||")

events = input().split("=>")

while events[0] != "End":

    if events[0] == "Plunder":
        town = events[1]
        people = int(events[2])
        treasure = int(events[3])
        print(f"{town} plundered! {treasure} gold stolen, {people} citizens killed.")

        cities[town][0] -= people
        cities[town][1] -= treasure

        if cities[town][0] == 0 or cities[town][1] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif events[0] == "Prosper":
        town_name = events[1]
        money = int(events[2])

        if money < 0:
            print("Gold added cannot be a negative number!")

        else:
            cities[town_name][1] += money
            print(f"{money} gold added to the city treasury. {town_name} now has {cities[town_name][1]} gold.")

    events = input().split("=>")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

    for key, value in cities.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")