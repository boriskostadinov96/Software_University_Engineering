def multiply(times):
    def decorator(function):  # refers to the function add_ten()

        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
