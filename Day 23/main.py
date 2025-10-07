class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "available" if not self.is_borrowed else "borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}\n")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def view_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("\n-- Library Catalog --")
            for book in self.books:
                book.display_info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f"Book '{title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"Book '{title}' has been borrowed. Enjoy reading!")
                return
        print(f"Book '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Book '{title}' has been returned. Thank you!")
                else:
                    print(f"Book '{title}' was not borrowed.")
                return
        print(f"Book '{title}' is not found in the library.")


# Main program loop
library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        book = Book(title, author)
        library.add_book(book)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ").strip()
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ").strip()
        library.return_book(title)
    elif choice == "5":
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
