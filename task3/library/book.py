class Book:
    def __init__(self, title, author, pages, book_id):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_id = book_id

    def info(self):
        return f"{self.title}, {self.author}, {self.pages} стор., ID: {self.book_id}"