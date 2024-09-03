sequence = input().split()

for char in sequence:
    print(char * len(char), end="")