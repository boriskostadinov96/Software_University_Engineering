numbers = [int(x) for x in input().split(', ')]

for num in numbers:
    if num == 0:
        numbers.remove(num)
        numbers.append(num)

print(numbers)

# solution 2
# number_as_string = input().split(", ")
# list_of_zeros = [int(number_as_string[i]) for i in range(len(number_as_string)) if int(number_as_string[i]) == 0]
# list_without_zeros = [int(number_as_string[i]) for i in range(len(number_as_string)) if int(number_as_string[i]) != 0]
# combined_lists = list_without_zeros + list_of_zeros
# print(combined_lists)
