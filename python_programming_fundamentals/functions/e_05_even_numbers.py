def find_even_numbers(numbers):
    even_numbers = []

    for x in numbers:
        if x % 2 == 0:
            even_numbers.append(x)

    return even_numbers


nums = [int(x) for x in input().split()]
print(find_even_numbers(nums))

# solution 2
# numbers_as_string = input().split()
# numbers_as_digits = []
#
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
#
# is_even = lambda x: x % 2 == 0
#
# result = list(filter(is_even, numbers_as_digits))
# print(result)


# solution 3
# integers = print([int(x) for x in input().split() if int(x) % 2 == 0])
