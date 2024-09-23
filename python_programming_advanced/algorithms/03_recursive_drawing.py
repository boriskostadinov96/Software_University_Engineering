def recursive_drawing(number):
    if number == 0:
        return

    print('*' * number)

    recursive_drawing(number - 1)

    print('#' * number)


n = int(input())
recursive_drawing(n)