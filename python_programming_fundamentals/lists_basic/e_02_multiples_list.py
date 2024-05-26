factor = int(input())
count = int(input())

numbers = [factor * n for n in range(1, count + 1)]
print(numbers)

# solution 2
# factor = int(input())
# count = int(input())
# list_with_numbers = []
#
# for multiplier in range(1, count + 1):
#     list_with_numbers.append(factor * multiplier)
#
# print(list_with_numbers)
