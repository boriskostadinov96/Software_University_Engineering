from functools import reduce

def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)

    elif operator == "-":
        return reduce(lambda x, y: x - y, args)

    elif operator == "*":
        return reduce(lambda x, y: x * y, args)

    elif operator == "/":
        return reduce(lambda x, y: x / y, args)

# 1.1 solution with eval
# from functools import reduce
#
# def operate(operator, *args):
#     return reduce(lambda x, y: eval(f"{x}{operator}{y}"), args)