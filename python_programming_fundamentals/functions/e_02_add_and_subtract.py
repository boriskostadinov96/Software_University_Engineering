def sum_numbers(num_one, num_two):
    sum_of_two_nums = num_one + num_two
    return sum_of_two_nums


def subtract(result, num_three):
    return result - num_three


def add_and_subtract(num_one, num_two, num_three):
    returned_result = sum_numbers(num_one, num_two)
    final_result = subtract(returned_result, num_three)
    return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))