def type_check(expected_data):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_data):
                    return "Bad Type"

            return function(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
