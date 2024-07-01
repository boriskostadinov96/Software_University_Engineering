first_sequence = input().split(', ')
second_sequence = input().split(', ')
substrings = []

for s1 in first_sequence:
    for s2 in second_sequence:
        if s1 in s2:
            substrings.append(s1)
            break

print(substrings)