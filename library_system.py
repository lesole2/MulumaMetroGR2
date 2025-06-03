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

    def list_books(self):
        return self.catalog

    def get_borrower(self, isbn):
        return self.loans.get(isbn, "None")

def main():
    library = Library()

    while True:
        print("\n--- Community Library Menu ---")
        print("1. Add a Book")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Check Out a Book")
        print("5. Return a Book")
        print("6. List All Books")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == "2":
            keyword = input("Enter title keyword: ")
            results = library.search_by_title(keyword)
            if results:
                for b in results:
                    print(f"{b.title} by {b.author} (ISBN: {b.isbn}) - {'Available' if b.is_available else 'Checked Out by ' + library.get_borrower(b.isbn)}")
            else:
                print("No books found with that title.")

        elif choice == "3":
            keyword = input("Enter author keyword: ")
            results = library.search_by_author(keyword)
            if results:
                for b in results:
                    print(f"{b.title} by {b.author} (ISBN: {b.isbn}) - {'Available' if b.is_available else 'Checked Out by ' + library.get_borrower(b.isbn)}")
            else:
                print("No books found by that author.")

        elif choice == "4":
            isbn = input("Enter ISBN to check out: ")
            borrower = input("Enter borrower's name: ")
            if library.checkout_book(isbn, borrower):
                print("Book checked out.")

        elif choice == "5":
            isbn = input("Enter ISBN to return: ")
            if library.return_book(isbn):
                print("Book returned.")
            else:
                print("Book not found or already returned.")

        elif choice == "6":
            books = library.list_books()
            if not books:
                print("No books in the catalog.")
            else:
                for b in books:
                    status = "Available" if b.is_available else f"Checked Out by {library.get_borrower(b.isbn)}"
                    print(f"{b.title} by {b.author} (ISBN: {b.isbn}) - {status}")

        elif choice == "7":
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                print("Goodbye!")
                break

        else:
            print("Invalid option. Please try again.")

main()
