max_number = 0

while True:
    user_input = input()

    if user_input == "Stop":
        break

    number = int(user_input)
    if number > max_number:
        max_number = number

print(max_number)
