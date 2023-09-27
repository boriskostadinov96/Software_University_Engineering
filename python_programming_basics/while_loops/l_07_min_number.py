min_number = 0
first_input = True

while True:
    user_input = input()

    if user_input == "Stop":
        break

    number = int(user_input)
    if first_input or number < min_number:
        min_number = number
        first_input = False

print(min_number)
