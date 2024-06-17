def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(result, third_num):
    return result - third_num


def add_and_subtract(first_num, second_num, third_num):
    returned_result = sum_numbers(first_num, second_num)
    final_result = subtract(returned_result, third_num)

    return final_result


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
