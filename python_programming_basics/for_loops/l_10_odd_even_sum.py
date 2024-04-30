numbers = int(input())
even_sum = 0
odd_sum = 0

for num in range(numbers):
    i = int(input())

    if num % 2 == 0:
        even_sum += i

    else:
        odd_sum += i

if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")

else:
    print(f"No\nDiff = {abs(even_sum - odd_sum)}")
