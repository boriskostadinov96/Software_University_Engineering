username = input()
correct_password = input()
new_password = input()

while new_password != correct_password:
    new_password = input()

print(f"Welcome {username}!")

# solution 2
# username = input()
# correct_password = input()
#
# while True:
#     password = input()
#     if password != correct_password:
#         continue
#
#     else:
#         print(f"Welcome {username}!")
#         break
