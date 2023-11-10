sequence_of_strings = input().split()
result = ""

for char in sequence_of_strings:
    result += char * len(char)

print(result)