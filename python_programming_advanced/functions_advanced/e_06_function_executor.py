def func_executor(*funcs_data):
    return "\n".join(f"{func.__name__} - {func(*args)}" for func, args in funcs_data)


#1.1
# def func_executor(*funcs_data):
#     result = []
#
#     for func, args in funcs_data:
#         result.append(f"{func.__name__} - {func(*args)}")
#
#     return "\n".join(result)