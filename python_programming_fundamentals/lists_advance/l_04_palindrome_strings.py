words = input().split()
palindrome = input()
found_palindromes = []
counter = 0

for word in words:
    if word == word[::-1]:
        found_palindromes.append(word)

for var in found_palindromes:
    if var == palindrome:
        counter += 1

print(found_palindromes)
print(f"Found palindrome {counter} times")

# solution 2
# words = input().split()
# palindrome = input()
# found_palindromes = []
#
# for p in words:
#     if p in words:
#         found_palindromes.append(p)

# solution 3
# words = input().split()
# searched_palindromes = input()
# print([word for word in words if word == word[::-1]])
# print(f"Found palindrome {words.count(searched_palindromes)} times")