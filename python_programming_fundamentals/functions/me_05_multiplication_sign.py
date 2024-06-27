def check_result(first_num, second_num, third_num):
    if first_num == 0 or second_num == 0 or third_num == 0:
        print('zero')

    else:
        negative_count = 0

        if first_num < 0:
            negative_count += 1

        if second_num < 0:
            negative_count += 1

        if third_num < 0:
            negative_count += 1

        if negative_count % 2 == 1:
            print('negative')
        else:
            print('positive')


first_number = int(input())
second_number = int(input())
third_number = int(input())

check_result(first_number, second_number, third_number)


# def check_result(first_num, second_num, third_num):
#     result = first_num * second_num * third_num
# 
#     if result < 0:
#         print('negative')
#
#     elif result > 0:
#         print('positive')
#
#     else:
#         print('zero')
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# check_result(first_number, second_number, third_number)
