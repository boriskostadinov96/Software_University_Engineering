word = input()
reversed_word = ""

for i in range(len(word) -1, -1, -1):
    reversed_word += word[i]
print(reversed_word)

# Second way:
#
# word = input()
# print(word[::-1])

# Third way:
#
# word = input()
# for index in range(len(word)-1, -1, -1):
#     print(word[index], end= "")

