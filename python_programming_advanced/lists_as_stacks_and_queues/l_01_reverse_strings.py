text = list(input())
reversed_text_stack = []

for _ in range(len(text)):
    reversed_text_stack.append(text.pop())

print("".join(reversed_text_stack))


# 1.1
#
# text = input()
# print(text[::-1])


# 1.2
#
# text = list(input())
#
# while text:
#     print(text.pop(), end="")
