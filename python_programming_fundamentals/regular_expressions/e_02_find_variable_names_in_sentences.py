import re

pattern = r"\b_([A-Za-z0-9]+)\b"

names = input()

matches = re.findall(pattern, names)
print(*matches, sep=',')