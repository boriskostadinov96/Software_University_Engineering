def check_data_type(command_data, number):
    result = 0

    if command_data == 'int':
        result = int(number) * 2

    elif command_data == 'real':
        result = f"{float(number) * 1.5:.2f}"

    else:
        result = f'${number}$'

    return result


data = input()
num = input()
print(check_data_type(data, num))
