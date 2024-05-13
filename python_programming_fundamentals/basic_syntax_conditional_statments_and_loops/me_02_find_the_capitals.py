word = input()
capital_letters = []

for letter_idx, letter_word in enumerate(word):
    if letter_word.isupper():
        capital_letters.append(letter_idx)

print(capital_letters)

# solution 2
# name = input()
# capital_letter_indices = []
#
# for j in range(len(name)):
#     if name[j].isupper():
#         capital_letter_indices.append(j)
# print(capital_letter_indices)
