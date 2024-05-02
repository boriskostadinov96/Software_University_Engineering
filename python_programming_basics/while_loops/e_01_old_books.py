book = input()
count = 0
is_found = False
input_line = input()
while input_line != "No More Books":
    if input_line == book:
        is_found = True
        break

    count = count + 1
    input_line = input()

if is_found:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")


# solution 2
# searched_book = input()
# books_counter = 0
#
# while True:
#     current_book = input()
#     if current_book != searched_book and current_book != "No More Books":
#         books_counter += 1
#
#     if current_book == "No More Books":
#         print(f"The book you search is not here!\nYou checked {books_counter} books.")
#         break
#
#     elif current_book == searched_book:
#         print(f"You checked {books_counter} books and found it.")
#         break
