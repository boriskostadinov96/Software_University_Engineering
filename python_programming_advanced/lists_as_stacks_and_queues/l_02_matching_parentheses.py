algebraic_expression = input()
parentheses = []

for index in range(len(algebraic_expression)):
    if algebraic_expression[index] == "(":
        parentheses.append(index)

    elif algebraic_expression[index] == ")":
        start_index = parentheses.pop()
        print(algebraic_expression[start_index:index+1])