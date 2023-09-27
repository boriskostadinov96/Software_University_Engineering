number_of_messages = int(input())
string = ""

for current_number in range(number_of_messages):
    number = int(input())
    if number == 88:
        string = "Hello"
    elif number == 86:
        string = "How are you?"
    elif number < 88:
        string = "GREAT!"
    else:
        string = "Bye."
    print(f'{string}')
