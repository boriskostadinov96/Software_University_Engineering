n = int(input())
counter = 0

for row in range(1, n + 1):
    for col in range(1, row + 1):
        counter += 1

        print(counter, end=" ")
        if counter == n:
            exit()
    print()


# solution 2 with flag

# number = int(input())
# counter = 1
# all_printed = False
#
# for row in range(1, number + 1):
#     for colum in range(1, row + 1):
#         print(counter, end=" ")
#         counter += 1
#
#         if counter > number:
#             all_printed = True
#             break
#
#     if all_printed:
#         break
#     print()