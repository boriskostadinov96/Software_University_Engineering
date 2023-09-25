name = input()
place = ""
Voldemort = False

while name != "Welcome!":
    if name == "Voldemort":
        Voldemort = True
        break

    if len(name) < 5:
        place = "Gryffindor."

    elif len(name) == 5:
        place = "Slytherin."

    elif len(name) == 6:
        place = "Ravenclaw."
    else:
        place = "Hufflepuff."
    print(f'{name} goes to {place}')
    name = input()
if Voldemort:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")