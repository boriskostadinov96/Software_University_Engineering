lines = int(input())
letters_sum = 0

for _ in range(lines):
    current_letter = input()
    letters_sum += ord(current_letter)

print(f"The sum equals: {letters_sum}")
