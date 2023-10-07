numbers_as_string = input().split()
list_of_numbers = []

for x in numbers_as_string:
    list_of_numbers.append(abs(float(x)))

print (list_of_numbers)


