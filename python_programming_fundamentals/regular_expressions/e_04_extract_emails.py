import re

text = input()
pattern = "(^|(?<=\\s))(([a-zA-Z0-9]+)([.-]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([.-][A-Za-z]+)+))(\\b|(?=\\s))"
emails = re.finditer(pattern, text)

for email in emails:
    print(email.group())