command = input()
events_lower = ["coding", "dog", "cat", "movie"]
events_upper = ["CODING", "DOG", "CAT", "MOVIE"]
total_coffees = 0

while command != "END":
    coffee_counter = 0

    if command in events_lower:
        coffee_counter += 1

    elif command in events_upper:
        coffee_counter += 2

    else:
        command = input()
        continue

    total_coffees += coffee_counter

    command = input()

if total_coffees > 5:
    print("You need extra sleep")

else:
    print(total_coffees)

# solution 2
# command = input()
# coffe_counter = 0
#
# while command != "END":
#     if command.lower() == "coding" or \
#             command.lower() == "dog" or \
#             command.lower() == "cat" or \
#             command.lower() == "movie":
#
#         if command.islower():
#             coffe_counter += 1
#
#         else:
#             coffe_counter += 2
#
#     command = input()
#
# if coffe_counter > 5:
#     print("You need extra sleep")
#
# else:
#     print(coffe_counter)