some_numbers = tuple([float(num) for num in input().split()])
same_values = {}

for current_num in some_numbers:
    if current_num not in same_values:
        same_values[current_num] = some_numbers.count(current_num)

for number, count in same_values.items():
    print(f"{number} - {count} times")
