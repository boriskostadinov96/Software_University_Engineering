words = [el.lower() for el in input().split()]
default = 0
occurrences = dict.fromkeys(words, default)

for word in words:
    occurrences[word] += 1

for key, value in occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")
