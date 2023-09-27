name = input()
capital_letter_indices = []

for j in range(len(name)):
    if name[j].isupper():
        capital_letter_indices.append(j)
print(capital_letter_indices)