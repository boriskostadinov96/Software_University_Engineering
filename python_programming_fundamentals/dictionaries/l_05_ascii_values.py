characters = [x for x in input().split(', ')]
char_dict = {}

for char in characters:
    if char not in char_dict:
        char_dict[char] = ord(char)

print(char_dict)

# Dictionary comprehension
# characters = input().split(", ")
# print({char: ord(char) for char in characters})
