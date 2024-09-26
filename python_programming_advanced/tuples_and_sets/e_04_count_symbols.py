text = input()
occurrences = {}

for char in text:
    if char not in occurrences:
        occurrences[char] = 1

    else:
        occurrences[char] += 1

for char in sorted(occurrences):
    print(f"{char}: {occurrences[char]} time/s")