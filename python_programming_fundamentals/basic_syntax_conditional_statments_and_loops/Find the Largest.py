number = int(input())
digits = []
largest_number = ""
number_as_string = str(number)

for i in range(len(number_as_string)):
    digits.append(number_as_string[i])
digits.sort(reverse=True)
for j in range(len(digits)):
    largest_number += str(digits[j])
print(largest_number)

