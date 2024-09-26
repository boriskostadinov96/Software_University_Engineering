n = int(input())
people = set()

for _ in range(n):
    codes = input()

    if len(codes) == 8:
        people.add(codes)

guests = input()

while guests != "END":
    if guests in people:
        people.remove(guests)

    guests = input()

print(len(people))
print(*sorted(people), sep='\n')