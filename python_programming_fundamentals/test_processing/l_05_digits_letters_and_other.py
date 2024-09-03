word = input()
digits = ""
chars = ""
all = ""

for char in word:
    if char.isdigit():
        digits += char

    elif char.isalpha():
        chars += char

    else:
        all += char

print(digits)
print(chars)
print(all)