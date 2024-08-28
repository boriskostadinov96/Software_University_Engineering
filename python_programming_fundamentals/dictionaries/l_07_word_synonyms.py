words_count = int(input())
synonyms = {}

for _ in range(words_count):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = [synonym]

    else:
        synonyms[word].append(synonym)

for key, values in synonyms.items():
    print(f"{key} - {', '.join(v for v in values)}")

# solution 2
# number = int(input())
# synonyms = {}
#
# for _ in range(number):
#     key = input()
#     value = input()
#     if key not in synonyms:
#         synonyms[key] = []
#     synonyms[key].append(value)
#
# for word in synonyms:
#     print(f"{word} - {', '.join(synonyms[word])}")