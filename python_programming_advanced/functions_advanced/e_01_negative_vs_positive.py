def odd_even_numbers(nums):
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

# 1. 1
# nums = [int(x) for x in input().split()]
# negative_nums = sum([n for n in nums if n < 0])
# positive_nums = sum([n for n in nums if n > 0])
#
# print(negative_nums)
# print(positive_nums)
#
# if abs(negative_nums) > abs(positive_nums):
#     print("The negatives are stronger than the positives")
#
# else:
#     print("The positives are stronger than the negatives")