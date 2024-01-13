from collections import deque
numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")

# solution 2

# numbers = deque(input().split())
# numbers.reverse()
# print(*numbers)

# solution 3

# numbers = [int(num_as_string) for num_as_string in input().split()]
# print(*numbers[::-1])
#
