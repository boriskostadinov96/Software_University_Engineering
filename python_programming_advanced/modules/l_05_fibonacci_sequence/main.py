from Labs.l_05_fibonacci_sequence.core import create_sequence, locate_number

command = input()

while command != "Stop":
    if "Create" in command:
        _, _, number = command.split()
        number = int(number)
        sequence = create_sequence(number)
        print(*sequence)

    else:
        _, number = command.split()
        number = int(number)
        result = locate_number(number, sequence)
        print(result)

    command = input()
