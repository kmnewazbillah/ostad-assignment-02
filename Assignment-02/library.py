# library.py
from book import Book
from library_system import LibrarySystem

def main():
    library = LibrarySystem()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Search Books by Author")
        print("5. Remove Book")
        print("6. Lend Book")
        print("7. View Lent Books")
        print("8. Return Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            authors = input("Enter authors (comma separated): ").split(',')
            isbn = input("Enter ISBN: ")
            year = input("Enter publishing year: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            book = Book(title, authors, isbn, year, price, quantity)
            library.add_book(book)
        elif choice == '2':
            library.view_all_books()
        elif choice == '3':
            term = input("Enter title or ISBN to search: ")
            library.search_books(term)
        elif choice == '4':
            author = input("Enter author to search: ")
            library.search_books_by_author(author)
        elif choice == '5':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)
        elif choice == '6':
            isbn = input("Enter ISBN of the book to lend: ")
            person = input("Enter the name of the person: ")
            library.lend_book(isbn, person)
        elif choice == '7':
            library.view_lent_books()
        elif choice == '8':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()