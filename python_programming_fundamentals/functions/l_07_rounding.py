def rounding_numbers(nums):
    result = []

    for num in nums:
        result.append(round(num))

    return result


numbers = [float(x) for x in input().split()]
print(rounding_numbers(numbers))

# solution 2 without function
# print([round(float(x)) for x in input().split()])
