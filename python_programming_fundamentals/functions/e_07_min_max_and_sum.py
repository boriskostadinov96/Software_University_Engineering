def finds_min_max_sum_of_numbers(integers):
    min_number = min(integers)
    max_number = max(integers)
    sum_numbers = sum(integers)

    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_numbers}")


nums = [int(x) for x in input().split()]
finds_min_max_sum_of_numbers(nums)
