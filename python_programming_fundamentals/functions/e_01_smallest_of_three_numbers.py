def find_smallest_number(first_num, second_num, third_num):
    result = 0

    if first_num < second_num and first_num < third_num:
        result = first_num

    elif second_num < first_num and second_num < third_num:
        result = second_num

    else:
        result = third_num

    return result


a = int(input())
b = int(input())
c = int(input())

print(find_smallest_number(a, b, c))

# solution 2
# def smallest_of_three_numbers(num_one, num_two, num_three):
#     if num_one < num_two and num_one < num_three:
#         print(num_one)
#     elif num_two < num_one and num_two < num_three:
#         print(num_two)
#     else:
#         print(num_three)
#
#
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
#
# smallest_of_three_numbers(first_num, second_num, third_num)
