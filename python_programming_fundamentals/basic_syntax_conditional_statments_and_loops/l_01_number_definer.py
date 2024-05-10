number = float(input())

if number == 0:
    print("zero")

elif number > 0:
    if number < 1 and number != 0:
        print("small positive")

    elif number > 1_000_000:
        print("large positive")

    else:
        print("positive")

elif number < 0:
    if abs(number) < 1 and abs(number) != 0:
        print("small negative")

    elif abs(number) > 1_000_000:
        print("large negative")

    else:
        print("negative")

# solution 2
#
# number = float(input())
# 
# if number == 0:
#     print("zero")
# elif number > 0:
#     if number < 1:
#         print("small positive")
#     elif number > 1000000:
#         print("large positive")
#     else:
#         print("positive")
#
# else:
#     if abs(number) < 1:
#         print("small negative")
#     elif abs(number) > 1000000:
#         print("large negative")
#     else:
#         print("negative")
