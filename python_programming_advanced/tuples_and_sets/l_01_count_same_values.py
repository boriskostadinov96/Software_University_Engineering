numbers = tuple([float(x) for x in input().split()])
count_nums = {}

for num in numbers:
    if num not in count_nums:
        count_nums[num] = numbers.count(num)

for key, value in count_nums.items():
    print(f"{key} - {value} times")
