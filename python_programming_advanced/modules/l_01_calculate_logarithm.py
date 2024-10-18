from math import log

num = int(input())

try:
    base = int(input())
    print(f"{log(base):.2f}")

except ValueError:
    print(f"{log(num)}:.2f")


# 1.1
# from math import log
#
# num = int(input())
# logarithm = input()
#
# if logarithm == "natural":
#     print(f"{log(num):.2f}")
#
# else:
#     print(f"{log(num, int(logarithm)):.2f}")

