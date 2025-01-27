class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
            
    def __str__(self):
        return "{} by {}".format(self.title, self.author)
    
class Member():
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def __str__(self):
        return "Member: {} ID: {}".format(self.name, self.member_id)
    
class Library():
    def __init__(self):
        self.books = []
        self.member = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def register_member(self, member):
        self.member.append(member)
    
    def lend_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print("{} is rented by {}".format(book.title, member.name))
        else:
            print("{} is currently rented by another member".format(book.title))
    
    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print("The {} has been returned by {}".format(book.title, member.name))
        else:
            print("{} did not borrow {}".format(member.name, book.title))
            
# ----------------------
# Adding examples

# Create instances of Book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("Pride and Prejudice", "Jane Austen")
book3 = Book("The Catcher in the Rye", "J.D. Salinger")

# Create instances of Member
member1 = Member("Charlie", 1)
member2 = Member("Daisy", 2)

# Create an instance of Library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register member to the library
library.register_member(member1)
library.register_member(member2)

# Lend books to member
library.lend_book(book1, member1)  
library.lend_book(book2, member1)  
library.lend_book(book3, member2)  

# Return books
library.return_book(book1, member1)  
library.return_book(book3, member2)  
