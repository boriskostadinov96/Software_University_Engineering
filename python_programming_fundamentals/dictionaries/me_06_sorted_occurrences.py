my_list = ["a", "b", "a", "c", "c", "a", "c"]
occurrences = {}

for letter in my_list:
    if letter not in occurrences:
        occurrences[letter] = 0

    occurrences[letter] += 1

sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

for key, value in sorted_occurrences:
    print(f"{key} -> {value}")