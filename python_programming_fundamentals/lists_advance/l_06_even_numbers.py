nums = [int(x) for x in input().split(', ')]
print([index for index, num in enumerate(nums) if num % 2 == 0])

# double comprehension
# print([index for index, num in enumerate([int(num) for num in input().split(", ")]) if num % 2 == 0])

# solution 3
# nums = list(map(int, input().split(", ")))
# print([index for index in range(len(nums)) if nums[index] % 2 == 0])
