from collections import deque

current_name = input()
customer_names = deque()

while current_name != "End":

    if current_name == "Paid":
        while customer_names:
            print(customer_names.popleft())

    else:
        customer_names.append(current_name)

    current_name = input()

print(f"{(len(customer_names))} people remaining.")

# 1.1
# This is a result without the import of a deck
#
# current_name = input()
# customer_names = []
#
# while current_name != "End":
#
#     if current_name == "Paid":
#         while customer_names:
#             print(customer_names.pop(0))
#
#     else:
#         customer_names.append(current_name)
#
#     current_name = input()
#
# print(f"{(len(customer_names))} people remaining.")