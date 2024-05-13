word = input()
lower_word = word.lower()

sand_count = lower_word.count("sand")
water_count = lower_word.count("water")
fish_count = lower_word.count("fish")
sun_count = lower_word.count("sun")

counter = sand_count + water_count + fish_count + sun_count
print(counter)

# solution 2
# string = input()
# string = string.lower()
# counter = 0
#
# if string.count('sand') > 0:
#     counter += string.count("sand")
#
# if string.count('water') > 0:
#     counter += string.count("water")
#
# if string.count('fish') > 0:
#     counter += string.count("fish")
#
# if string.count('sun') > 0:
#     counter += string.count("sun")
#
# print(counter)