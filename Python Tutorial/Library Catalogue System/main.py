class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if self.available:
            self.available = False
            print(f"The book '{self.title}' has been checked out.\n")
        else:
            print(f"The book '{self.title}' is currently unavailable.\n")

    def return_book(self):
        """Mark the book as available."""
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' has been returned.\n")
        else:
            print(f"The book '{self.title}' was not checked out.\n")

    def display_info(self):
        """Display the book's information."""
        status = "Available" if self.available else "Checked Out"
        print(f"Title: {self.title}\nAuthor: {
              self.author}\nStatus: {status}\n")


class LibraryCatalogue:
    def __init__(self):
        self.catalogue = []

    def add_book(self, title, author):
        """Add a new book to the catalogue."""
        new_book = Book(title, author)
        self.catalogue.append(new_book)
        print(f"Book '{title}' by {author} added to the catalogue.\n")

    def display_all_books(self):
        """Display information for all books in the catalogue."""
        if not self.catalogue:
            print("No books in the catalogue.\n")
            return
        for book in self.catalogue:
            book.display_info()

# Simulating user interactions


def main():
    print("Welcome to the Library Catalogue System!\n")
    catalogue = LibraryCatalogue()

    while True:
        print("Options:\n1. Add a new book\n2. Display all books\n3. Check out a book\n4. Return a book\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            catalogue.add_book(title, author)
        elif choice == "2":
            catalogue.display_all_books()
        elif choice == "3":
            title = input("Enter the title of the book to check out: ")
            for book in catalogue.catalogue:
                if book.title.lower() == title.lower():
                    book.check_out()
                    break
            else:
                print(f"The book '{title}' is not found in the catalogue.\n")
        elif choice == "4":
            title = input("Enter the title of the book to return: ")
            for book in catalogue.catalogue:
                if book.title.lower() == title.lower():
                    book.return_book()
                    break
            else:
                print(f"The book '{title}' is not found in the catalogue.\n")
        elif choice == "5":
            print("Exiting the Library Catalogue System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()