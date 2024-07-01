products = [w for w in input().split() if len(w) % 2 == 0]
print('\n'.join(w for w in products))

# solution 2
# products = input().split()
# for word in products:
#     if len(word) % 2 == 0:
#         print(word)
