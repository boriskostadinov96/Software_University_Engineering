from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

operations = {
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '/': lambda a, b: a / b if b != 0 else 0,
}

while bees and nectar:
    first_bee = bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar < first_bee:
        bees.appendleft(first_bee)

    else:
        total_honey += abs(operations[symbols.popleft()] (first_bee, last_nectar))

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")