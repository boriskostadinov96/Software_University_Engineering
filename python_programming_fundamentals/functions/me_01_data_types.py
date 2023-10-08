def data_types(some_text, x):
    result = 0
    if some_text == "int":
        result = int(x) * 2

    elif some_text == "real":
        result = format(float(x) * 1.5, '.2f')

    elif some_text == "string":
        result = f'${x}$'

    return result


text = input()
other_text = input()

total_result = data_types(text, other_text)
print(total_result)




