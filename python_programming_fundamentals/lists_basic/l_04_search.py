lines = int(input())
word = input()
all_words = []
filtered_list = []

for _ in range(lines):
    text = input()
    all_words.append(text)

    if word in text:
        filtered_list.append(text)

print(all_words)
print(filtered_list)

