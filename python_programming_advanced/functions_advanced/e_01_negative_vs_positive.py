from typing import List


def odd_even_numbers(nums: List[int]):
    positive_numbers = sum([num for num in nums if num > 0])
    negative_numbers = sum([num for num in nums if num < 0])

    print(negative_numbers)
    print(positive_numbers)

    if abs(negative_numbers) > positive_numbers:
        print("The negatives are stronger than the positives")

    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
odd_even_numbers(numbers)


# 1.1
# numbers = [int(x) for x in input().split()]
# negative_numbers = []
# positive_numbers = []
#
# for num in numbers:
#     if num < 0:
#         negative_numbers.append(num)
#
#     else:
#         positive_numbers.append(num)
# print(sum(negative_numbers))
# print(sum(positive_numbers))
#
# if (sum(positive_numbers)) > abs(sum(negative_numbers)):
#     print("The positives are stronger than the negatives")
#
# else:
#     print("The negatives are stronger than the positives")

