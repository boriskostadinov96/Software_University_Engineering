def calculate_the_factorial(number):
    for current_number in range(1, number):
        number *= current_number

    return number


first_number = int(input())
second_number = int(input())

first_number_factorial = calculate_the_factorial(first_number)
second_number_factorial = calculate_the_factorial(second_number)

result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")

# solution 2
# first_num = int(input())
# second_num = int(input())
#
# factorial_one = 1
# factorial_two = 1
#
# if first_num >= 0:
#     for num in range(1, first_num + 1):
#         factorial_one *= num
#
# if second_num >= 0:
#     for num in range(1, second_num + 1):
#         factorial_two *= num
#
# result = factorial_one // factorial_two
# print(f"{result:.2f}")
