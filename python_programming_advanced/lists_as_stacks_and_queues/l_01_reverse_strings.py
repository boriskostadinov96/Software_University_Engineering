text = list(input())
stack = []

for char in range(len(text)):
    stack.append(text.pop())

print(*stack, sep="")

# solution 2
# text = input()
# print(text[::-1])

# solution 3
# text = list(input())
#
# while text:
#     print(text.pop(), end="")