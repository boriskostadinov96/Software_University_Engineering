initial_health = 100
bitcoins = 0
rooms = input().split('|')
room_counter = 0
is_dead = False

for room in rooms:
    room_counter += 1

    type_of_room, amount = room.split()
    amount = int(amount)

    if type_of_room == 'potion':
        healed_amount = amount

        if initial_health + amount > 100:
            healed_amount = 100 - initial_health
            initial_health = 100
        else:
            initial_health += amount

        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {initial_health} hp.")

    elif type_of_room == 'chest':
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        initial_health -= amount
        if initial_health > 0:
            print(f"You slayed {type_of_room}.")

        else:
            print(f"You died! Killed by {type_of_room}.")
            print(f"Best room: {room_counter}")
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")
