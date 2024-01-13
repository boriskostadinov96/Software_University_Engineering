stack_of_numbers = []
current_number = int(input())

for _ in range(current_number):
    numbers_data = input().split()
    command = numbers_data[0]

    if command == "1":
        stack_of_numbers.append(numbers_data[1])

    elif command == "2":
        stack_of_numbers.pop()

    elif command == "3":
        if stack_of_numbers:
            print(max(stack_of_numbers))

    elif command == "4":
        if stack_of_numbers:
            print(min(stack_of_numbers))

stack_of_numbers.reverse()

print(*stack_of_numbers, sep=", ")