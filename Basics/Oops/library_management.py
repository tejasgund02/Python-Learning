class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"{book} not found in the library.")    
    def despley_books(self):
        if self.books:
            print("BOOKS IN THE LIBRARY:\n")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

# use while loop to create a menu driven program for library management system where user can add book, remove book and display books in the library.
print("Welcome to the Library Management System")
print("1. Add Book")
print("2. Remove Book")
print("3. Display Books")
print("4. Exit")
input_choice = int(input("Enter your choice: "))
choice = 0
# case match statement to handle user input
library = Library()
while choice != 4:  
    match input_choice:
        case 1:
            book = input("Enter the name of the book to add: ")
            library.add_book(book)
        case 2:
            book = input("Enter the name of the book to remove: ")
            library.remove_book(book)
        case 3:
            library.despley_books()
        case 4:
            print("Exiting the program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Exit")
    input_choice = int(input("Enter your choice: "))
    