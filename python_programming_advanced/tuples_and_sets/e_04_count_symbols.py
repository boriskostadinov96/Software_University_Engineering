text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")


# 1.2
# text = input()
# occurrences = {}
#
# for chr in text:
#     if chr not in occurrences:
#         occurrences[chr] = 1
#
#     else:
#         occurrences[chr] += 1
#
# [print(f"{key}: {value} time/s") for key, value in sorted(occurrences.items())]
