algebraic_expression = input()
parentheses = []

for index in range(len(algebraic_expression)):
    if algebraic_expression[index] == "(":
        parentheses.append(index)

    elif algebraic_expression[index] == ")":
        last_parentheses = parentheses.pop()
        print(algebraic_expression[last_parentheses:index+1])