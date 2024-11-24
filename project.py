class Library:
    def __init__(self,name):
        self.name = name


class Books:
    def __init__(self,name,author,genre,number_of_copies,book_link):
        self.name = name
        self.author = author
        self.genre = genre
        self.book_link = book_link
        self.number_of_copies = number_of_copies




class Student:
    def __init__(self,name,access_number):
        self.name = name
        self.access_number = access_number
        self.books_borrowed = []

    def borrow_book(self, book):
        self.books_borrowed.append(book)
        return f"{self.name} has borrowed {book}"  

class Librarian:
    pass




