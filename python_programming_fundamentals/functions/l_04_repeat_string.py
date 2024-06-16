def repeat_string(some_str, n):
    return some_str * n


text = input()
counter = int(input())

print(repeat_string(text, counter))

# solution 2 using lambda function
#
# string = input()
# n = int(input())
# 
# repeat_string = lambda a, b: a * b
#
# result = repeat_string(string, n)
# print(result)
