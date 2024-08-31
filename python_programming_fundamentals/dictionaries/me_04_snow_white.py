dwarfs = {}
command = input().split(" <:> ")

while command[0] != "Once upon a time":
    name = command[0]
    hat_color = command[1]
    physics = int(command[2])

    key = (name, hat_color)

    if key not in dwarfs or dwarfs[key] < physics:
        dwarfs[key] = physics

    command = input().split(" <:> ")

hat_color_count = {}

for (name, hat_color), physics in dwarfs.items():

    if hat_color not in hat_color_count:
        hat_color_count[hat_color] = 0
    hat_color_count[hat_color] += 1

ordered_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1], -hat_color_count[x[0][1]]))

for (name, hat_color), physics in ordered_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")
