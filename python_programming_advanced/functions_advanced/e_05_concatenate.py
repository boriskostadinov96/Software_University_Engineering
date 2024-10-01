def concatenate(*args, **kwargs):
    text = "".join(args)

    for key, value in kwargs.items():
        text = text.replace(key, value)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

# 1.1
# def concatenate(*args, **kwargs):
#     result = ''
#
#     for word in args:
#         result += word
#
#     for key, value in kwargs.items():
#         if key in result:
#             result = result.replace(key, value)
#
#     return result
#
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))