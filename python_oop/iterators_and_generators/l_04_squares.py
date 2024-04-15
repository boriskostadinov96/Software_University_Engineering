def squares(n):
    start_number = 1

    while start_number <= n:
        yield start_number ** 2
        start_number += 1


print(list(squares(5)))
