def check_is_number_a_palindrome(integers):
    for number in integers:
        reversed_num = number[::-1]

        if number == reversed_num:
            print('True')

        else:
            print('False')


nums = input().split(', ')
print(check_is_number_a_palindrome(nums))

# solution 2
# def is_palindrome(some_number_as_string: str) -> bool:
#     return some_number_as_string == some_number_as_string[::-1]
#
#
# numbers_as_string = input().split(", ")
# for number_as_string in numbers_as_string:
#     print(is_palindrome(number_as_string))