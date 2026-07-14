
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_book(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display_patron(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)

class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"'{book.title}' borrowed by {patron.name}.")

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)
            book.is_borrowed = False
            print(f"'{book.title}' returned successfully.")
        else:
            print(f"{patron.name} has not borrowed '{book.title}'.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            book.display_book()

    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            patron.display_patron()

library = Library()

book1 = Book(101, "Software Engineering: A Practioner's Approach", "Roger S Pressman")
book2 = Book(102, "Software Engineering", "Ian Sommerville")

library.add_book(book1)
library.add_book(book2)

patron1 = Patron(1, "Rahul")
patron2 = Patron(2, "Nikhil")

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book(1, 101)

library.display_books()

library.return_book(1, 101)

library.display_books()

library.display_patrons()

#Output

"""
Book 'Software Engg.:A Practioner's Approach' added successfully.
Book 'Software Engg.' added successfully.
Patron 'Rahul' registered successfully.
Patron 'Nikhil' registered successfully.
'Software Engg.:A Practioner's Approach' borrowed by Rahul.

Library Books:
ID: 101, Title: Software Engg.:A Practioner's Approach, Author: Roger S Pressman, Status: Borrowed
ID: 102, Title: Software Engg., Author: Ian Sommerville, Status: Available
'Software Engg.:A Practioner's Approach' returned successfully.

Library Books:
ID: 101, Title: Software Engg.:A Practioner's Approach, Author: Roger S Pressman, Status: Available
ID: 102, Title: Software Engg., Author: Ian Sommerville, Status: Available

Registered Patrons:
Patron ID: 1, Name: Rahul
Borrowed Books: []
Patron ID: 2, Name: Nikhil
Borrowed Books: []

"""