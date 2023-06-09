class Book:
    def __init__(self, title, author, pubyear):
        self.title = title
        self.author = author
        self.pubyear = pubyear
        self.is_available = True

    #Title
    def get_title(self):
        return self.title

    #Author
    def get_author(self):
        return self.author

    #Publication Year
    def get_pubyear(self):
        return self.pubyear

    #Availability
    def bookAvailability(self):
        return self.is_available

    #Borrowing
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} by {self.author} has been lent to someone else. Try again next time.")
        else:
            print(f"{self.title} by {self.author} is not available. Try again next time.")

    #returns
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.title} by {self.author} is now returned.")
        else:
            print(f"{self.title} by {self.author} is now available.")


bookLibrary = []


def display_available():
    if not bookLibrary:
        print("No Books Available")
    else:
        print("\nAvailable Books:")
        for index, book in enumerate(bookLibrary):
            if book.bookAvailability():
                print(f"{index}: {book.get_title()} by {book.get_author()} ({book.get_pubyear()})")


def main():
    while True:
        print("1. Add a book to the library")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display available books")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        #Adding a book
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            pubyear = input("Enter the publication year of the book: ")

            book = Book(title, author, pubyear)
            bookLibrary.append(book)
            print("Book added to the library.")


        elif choice == "2":

            #Borrows
            display_available()
            if bookLibrary:
                try:
                    index = int(input("Enter the index of the book to borrow: "))
                    if index < 0 or index >= len(bookLibrary):
                        print("Invalid book index.")
                        continue
                    book = bookLibrary[index]
                    book.borrow_book()
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
            else:
                print("No books available to borrow.")


        elif choice == "3":
            #Returns
            display_available()

            if bookLibrary:
                try:
                    index = int(input("Please enter the index of the book you wish to return: "))
                    if index < 0 or index >= len(bookLibrary):
                        print("Invalid! Please enter a valid input.")
                        continue
                    book = bookLibrary[index]
                    book.return_book()
                except ValueError:
                    print("Invalid input. Please enter a valid input.")
            else:
                print("No books available to return.")
        #Book availability display
        elif choice == "4":
            display_available()

        #Program Closure
        elif choice == "5":
            break

        else:
            print("Invalid! Enter again a valid input.")


if __name__ == "__main__":
    main()