numbers = [int(x) for x in input().split(', ')]

positive_nums = [x for x in numbers if x >= 0]
negative_nums = [x for x in numbers if x < 0]
even_nums = [x for x in numbers if x % 2 == 0]
odd_nums = [x for x in numbers if x % 2 != 0]

print("Positive:", ', '.join(map(str, positive_nums)))
print("Negative:", ', '.join(map(str, negative_nums)))
print("Even:", ', '.join(map(str, even_nums)))
print("Odd:", ', '.join(map(str, odd_nums)))