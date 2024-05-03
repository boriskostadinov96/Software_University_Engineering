command = input()
min_number = float("inf")

while command != "Stop":
    current_number = int(command)

    if current_number < min_number:
        min_number = current_number

    command = input()

print(min_number)