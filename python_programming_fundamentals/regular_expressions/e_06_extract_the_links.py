import re

pattern = "\\bw{3}.[a-zA-Z0-9\\-]+\\.[a-z]+(?:.[a-z]+)+\\b"
text = input()

while True:

    if not text:
        break

    sites = re.findall(pattern, text)

    if sites:
        print("".join(sites))

    text = input()