numbers = input().split()
stack = []

for num in range(len(numbers)):
    stack.append(numbers.pop())

print(*stack)

# solution 2
# numbers = input().split()
# print(*numbers[::-1])