class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

class Library:
    def __init__(self):
        self.catalog = []
        self.loans = {}

    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self.catalog):
            print("A book with this ISBN already exists.")
        else:
            self.catalog.append(book)
            print("Book added successfully.")

    def search_by_title(self, keyword):
        return [b for b in self.catalog if keyword.lower() in b.title.lower()]

    def search_by_author(self, keyword):
        return [b for b in self.catalog if keyword.lower() in b.author.lower()]

    def checkout_book(self, isbn, borrower):
        for b in self.catalog:
            if b.isbn == isbn:
                if b.is_available:
                    b.is_available = False
                    self.loans[isbn] = borrower
                    return True
                else:
                    print(f"Book is already checked out by {self.loans.get(isbn)}.")
                    return False
        print("Book with that ISBN not found.")
        return False

    def return_book(self, isbn):
        for b in self.catalog:
            if b.isbn == isbn and not b.is_available:
                b.is_available = True
                if isbn in self.loans:
                    del self.loans[isbn]
                return True
        return False
    
    
    #function to list books and details : KG

     def list_books(self):
        return self.catalog

    def get_borrower(self, isbn):
        return self.loans.get(isbn, "None")

def main():
    library = Library()
