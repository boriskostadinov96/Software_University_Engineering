number = int(input())
word = input()
all_words = []
words_containing_given_word = []

for _ in range(number):
    current_word = input()
    all_words.append(current_word)
    if word in current_word:
        words_containing_given_word.append(current_word)

print(all_words)
print(words_containing_given_word)