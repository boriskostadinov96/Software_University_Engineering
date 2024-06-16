def calculations(operator, first_num, second_num):
    if operator_symbol == 'subtract':
        return a - b

    elif operator == 'add':
        return a + b

    elif operator == 'multiply':
        return a * b

    else:
        return a // b


operator_symbol = input()
a = int(input())
b = int(input())

print(calculations(operator_symbol, a, b))

# solution 2 
#
# def calculate(command_operator, num_one, num_two):
#     result = 0
#     if command_operator == "multiply":
#         result = num_one * num_two
#
#     elif command_operator == "divide":
#         result = num_one // num_two
#
#     elif command_operator == "add":
#         result = num_one + num_two
#
#     elif command_operator == "subtract":
#         result = num_one - num_two
#
#     return result
#
#
# operator_input = input()
# first_number = int(input())
# second_number = int(input())
#
# total_result = calculate(operator_input, first_number, second_number)
# print(total_result)