text = input()
vowels = 'aoueiAOUEI'
print(*[w for w in text if w not in vowels], sep='')

# solution 2
# print("".join([char for char in input() if char.lower() not in "'a', 'o', 'u', 'e', 'i'"]))