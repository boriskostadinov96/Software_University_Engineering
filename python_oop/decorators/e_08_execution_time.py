from time import time


def exec_time(function):
    def wrapper(*args, **kwargs):
        start = time()  # gets the current time in seconds
        function(*args, **kwargs)
        end = time()  # gets the current time again

        return end - start  # gives us the total time for the execution of the current function

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))
