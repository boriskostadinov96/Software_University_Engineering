import re

pattern = "^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"

count = int(input())

for _ in range(count):
    word = input()

    if re.match(pattern, word):
        digits = re.findall(r"\d", word)

        if digits:
            product_group = "".join(digits)

        else:
            product_group = "00"

        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")