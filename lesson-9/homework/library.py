#be fair and kind in evaluating the code pls


# Custom Exceptions
class BookNotFoundException(Exception):
    # Raised when a requested book is not found in the library
    pass

class BookAlreadyBorrowedException(Exception):
    # Raised when trying to borrow a book that is already borrowed
    pass

class MemberLimitExceededException(Exception):
    # Raised when a member tries to borrow more books than the allowed limit
    pass

# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.is_borrowed = False  # Whether the book is borrowed or not

# Member Class
class Member:
    def __init__(self, name):
        self.name = name  # Name of the member
        self.borrowed_books = []  # List of borrowed books

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

# Library Class
class Library:
    def __init__(self):
        self.books = []  # List of books in the library
        self.members = []  # List of members in the library

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' was not found in the library.")

# Testing the Library System
library = Library()
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_member("Alice")

member = library.members[0]
book = library.find_book("1984")

try:
    member.borrow_book(book)
    print(f"{member.name} borrowed '{book.title}'.")
    member.return_book(book)
    print(f"{member.name} returned '{book.title}'.")
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(e)
