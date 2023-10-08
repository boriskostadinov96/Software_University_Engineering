def sum_min_max(number_func):
    number_func = [int(i)for i in number_func]
    min_values = min(number_func)
    max_value = max(number_func)
    list_sum = sum(number_func)

    print(f'The minimum number is {min_values}')
    print(f'The maximum number is {max_value}')
    print(f'The sum number is: {list_sum}')


sum_min_max(input().split())
