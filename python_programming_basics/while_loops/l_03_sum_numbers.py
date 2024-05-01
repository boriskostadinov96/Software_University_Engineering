number = int(input())
total_sum = 0

while total_sum < number:
    some_numbers = int(input())
    total_sum += some_numbers

    if total_sum >= number:
        print(total_sum)


# solution 2
# number = int(input())
# number_sum = 0
#
# while True:
#     some_numbers = int(input())
#     number_sum += some_numbers
#
#     if number_sum >= number:
#         break
#
# print(number_sum)