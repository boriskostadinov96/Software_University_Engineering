number = int(input())
even_nums = []
odd_nums = []
positive_nums = []
negative_nums = []

for _ in range(number):
    current_number = int(input())

    if current_number >= 0:
        positive_nums.append(current_number)
    else:
        negative_nums.append(current_number)

    if current_number % 2 == 0:
        even_nums.append(current_number)
    else:
        odd_nums.append(current_number)

command = input()
if command == 'positive':
    print(positive_nums)
elif command == 'negative':
    print(negative_nums)
elif command == 'even':
    print(even_nums)
else:
    print(odd_nums)