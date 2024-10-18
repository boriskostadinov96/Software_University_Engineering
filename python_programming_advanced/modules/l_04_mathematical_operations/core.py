sign_mapper = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
    "^": lambda x, y: x ** y
}


def execute_expression(exp):
    num1, sign, num2 = exp.split()
    first_num = float(num1)
    second_num = float(num2)

    return sign_mapper[sign](first_num, second_num)
