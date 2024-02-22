class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("Clean Code", "Robert C. Martin", 464)
print(book.name)
print(book.author)
print(book.pages)
