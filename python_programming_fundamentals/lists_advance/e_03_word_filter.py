nums = [int(n) for n in input().split(", ")]
positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []
for n in nums:
    if n >= 0:
        positive_nums.append(n)
    if n < 0:
        negative_nums.append(n)
    if n % 2 == 0:
        even_nums.append(n)
    else:
        odd_nums.append(n)
print(f'Positive: {", ".join([str(num) for num in positive_nums])}')
print(f'Negative: {", ".join([str(num) for num in negative_nums])}')
print(f'Even: {", ".join([str(num) for num in even_nums])}')
print(f'Odd: {", ".join([str(num) for num in odd_nums])}')