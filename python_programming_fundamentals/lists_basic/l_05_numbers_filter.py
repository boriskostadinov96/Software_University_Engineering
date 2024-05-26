lines = int(input())
even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []

for _ in range(lines):
    current_number = int(input())

    if current_number % 2 == 0:
        even_numbers.append(current_number)
    else:
        odd_numbers.append(current_number)

    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)

command = input()

if command == 'negative':
    print(negative_numbers)

elif command == 'positive':
    print(positive_numbers)

elif command == 'odd':
    print(odd_numbers)

elif command == 'even':
    print(even_numbers)