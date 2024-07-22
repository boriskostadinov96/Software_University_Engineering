nums = [int(x) for x in input().split(", ")]
current_group = 10

while nums:
    filtered_numbers = [n for n in nums if n <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers}")

    current_group += 10
    nums = [n for n in nums if n not in filtered_numbers]