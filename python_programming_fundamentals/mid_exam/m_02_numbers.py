numbers = input().split()

while True:
    line = input().split()
    if "Finish" in line:
        break
    if "Replace" in line:
        command, number_one, number_two = line
        if number_one in numbers:
            for i in range(len(numbers)):
                if numbers[i] == number_one:
                    numbers[i] = number_two
                    break

    else:
        command, number = line

        if command == "Add":
            numbers.append(number)

        elif command == "Remove":
            numbers.remove(number)

        elif command == "Collapse":
            numbers = [numbers[i] for i in range(len(numbers)) if int(numbers[i]) > int(number)]
print(" ".join(numbers))

