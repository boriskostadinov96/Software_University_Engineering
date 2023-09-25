book_to_find = input()
checked_books = 0
found = False

while True:
    book = input()
    if book == "No More Books":
        break

    checked_books += 1

    if book == book_to_find:
        found = True
        break

if found:
    print(f"You checked {checked_books} book{'s' if checked_books != 1 else ''} and found it.")
else:
    print(f"The book you search is not here!\nYou checked {checked_books} book{'s' if checked_books != 1 else ''}.")
