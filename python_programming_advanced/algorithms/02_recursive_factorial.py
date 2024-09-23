def get_factorial(number):
    if number == 0:
        return 1

    return number * get_factorial(number - 1)


n = int(input())
print(get_factorial(n))
