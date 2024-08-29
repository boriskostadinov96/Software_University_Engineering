words = input().replace(" ", "")
occurrences = dict.fromkeys(words, 0)

for word in words:
    occurrences[word] += 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")

# solution 2
# symbols = [character for character in input() if character != " "]
# letters = {}
#
# for symbol in symbols:
#     if symbol not in letters.keys():
#         letters[symbol] = 0
#
#     letters[symbol] += 1
#
# for symbol, occurrences in letters.items():
#     print(f"{symbol} -> {occurrences}")