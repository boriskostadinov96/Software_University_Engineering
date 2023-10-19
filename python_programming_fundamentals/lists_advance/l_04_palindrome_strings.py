words = input().split()
searched_palindromes = input()
print([word for word in words if word == word[::-1]])
print(f"Found palindrome {words.count(searched_palindromes)} times")