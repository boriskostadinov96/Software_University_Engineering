stack = []
count = int(input())

for _ in range(count):
    queries = [int(x) for x in input().split()]

    if queries[0] == 1:
        stack.append(queries[1])

    elif queries[0] == 2:
        if stack:
            stack.pop()

    elif queries[0] == 3:
        if stack:
            print(max(stack))

    elif queries[0] == 4:
        if stack:
            print(min(stack))

print(*stack[::-1], sep=', ')