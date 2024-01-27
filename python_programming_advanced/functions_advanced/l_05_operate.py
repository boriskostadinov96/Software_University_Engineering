from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x}{operator}{y}"), args)

# 1.1
# def operate(operator, *args):
#
#     if operator == "+":
#         return reduce(lambda x, y: x + y, args)
#
#     elif operator == "-":
#         return reduce(lambda x, y: x - y, args)
#
#     elif operator == "*":
#         return reduce(lambda x, y: x * y, args)
#
#     elif operator == "/":
#         return reduce(lambda x, y: x / y, args)
