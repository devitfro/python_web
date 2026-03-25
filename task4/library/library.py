from library.book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def __iadd__(self, book):
        self.books.append(book)
        return self

    def __isub__(self, book):
        self.books.remove(book)
        return self

    def __contains__(self, book):
        return book in self.books

    def __len__(self):
        return len(self.books)