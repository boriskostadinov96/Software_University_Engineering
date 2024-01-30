def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    if word[idx] != word[-idx - 1]:
        return f"{word} is not a palindrome"

    result = palindrome(word, idx + 1)

    return result


print(palindrome("abcba", 0))

# 1.1
#
#
# def palindrome(word, index):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#
#     else:
#         return f"{word} is not a palindrome"
#
#
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
