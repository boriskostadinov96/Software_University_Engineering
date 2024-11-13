def print_upper_part(size):
    for row in range(1, size + 1):
        print(f"{' ' * (size - row)}{'* ' * row}")


def print_bottom_part(size):
    for row in range(size - 1, 0, - 1):
        print(f"{' ' * (size - row)}{'* ' * row}")


def print_figure(size):
    print_upper_part(size)
    print_bottom_part(size)


n = int(input())
print_figure(n)



# n = int(input())
#
# for row in range(1, n + 1):
#     print(f"{' ' * (n - row)}{'* ' * row}")
#
# for row in range(n - 1, 0, - 1):
#     print(f"{' ' * (n - row)}{'* ' * row}")