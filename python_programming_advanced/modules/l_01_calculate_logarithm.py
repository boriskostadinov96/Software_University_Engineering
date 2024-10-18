from math import log

num = int(input())
logarithm = input()

if logarithm == "natural":
    print(f"{log(num):.2f}")

else:
    print(f"{log(num, int(logarithm)):.2f}")