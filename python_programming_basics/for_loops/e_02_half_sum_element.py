counts = int(input())
sum_of_numbers = 0
max_number = float("-inf")

for _ in range(counts):
    number = int(input())

    if number > max_number:
        max_number = number

    sum_of_numbers += number

sum_of_numbers -= max_number

if max_number == sum_of_numbers:
    print(f"Yes\nSum = {max_number}")

else:
    print(f"No\nDiff = {abs(max_number - sum_of_numbers)}")