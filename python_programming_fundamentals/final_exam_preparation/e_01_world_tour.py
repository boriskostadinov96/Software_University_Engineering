stops = input()
command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        country = command[2]

        if 0 <= index <= len(stops):
            stops = stops[:index] + country + stops[index:]
        print(stops)

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)

    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]

        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")
