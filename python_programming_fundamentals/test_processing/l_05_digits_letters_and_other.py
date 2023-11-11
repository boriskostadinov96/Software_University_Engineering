text = input()
digits = ""
letters = ""
characters = ""

for digit in text:
    if digit.isdigit():
        digits += digit

    elif digit.isalpha():
        letters += digit

    else:
        characters += digit

print(digits)
print(letters)
print(characters)
