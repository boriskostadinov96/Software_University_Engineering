text = input()
result_str = ''.join([char for char in text if char.lower() not in 'aeiou'])
print(result_str)
