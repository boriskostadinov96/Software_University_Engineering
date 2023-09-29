key = int(input())
number_of_lines = int(input())
end_result = ""

for index in range(number_of_lines):
    current_character = input()
    ascii_letter = ord(current_character)
    ascii_letter += key
    end_result = chr(ascii_letter)
    print(end_result, end="")