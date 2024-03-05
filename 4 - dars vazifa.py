from collections import namedtuple

Book = namedtuple("Book", ["id", "nomi", "autori", "yili", "janiri"])

books = [
    (1, "1984", "George Orwell", 1949, "Dystopian"),
    (2, "To Kill a Mockingbird", "Harper Lee", 1960, "Novel"),
    (3, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
]
book_records = [Book(*book) for book in books]

for book in book_records:
    print(book.id, book.nomi, book.autori, book.yili, book.janiri)
