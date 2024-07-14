import json
from book import Book

class LibrarySystem:
    def __init__(self, data_file = 'books.json'):
      self.data_file = data_file
      self.books = []
      self.load_data()

    def load_data(self):
      try:
        with open(self.data_file, 'r') as file:
          data = json.load(file)
          for book_data in data['books']:
            book = Book(book_data['title'], book_data['authors'], book_data['isbn'], book_data['year'], book_data['price'], book_data['quantity'], book_data['lent_to'])
            self.books.append(book)

      except FileNotFoundError:
        self.save_data()

    def save_data(self):
      data = {'books':[book.__dict__ for book in self.books]}
      with open(self.data_file, 'w') as file:
        json.dump(data, file)

    def add_book(self, book):
      self.books.append(book)
      self.save_data()

    def view_all_books(self):
      for book in self.books:
        print(book.output_book())

    def search_books(self, term):
      found_books = []
      for book in self.books:
        if term.lower() in book.title.lower() or term.lower() in book.isbn.lower():
          found_books.append(book)
      if found_books:
        print("Search Results:")
        for book in found_books:
          print(book.output_book())
      else:
        print("No books found.")

    def search_books_by_author(self, author):
      found_books = []
      for book in self.books:
        if author.lower() in [a.lower() for a in book.authors]:
          found_books.append(book)
      if found_books:
        print("\nSearch Results:")
        for book in found_books:
          print(book.output_book())
      else:
        print("No books found.")

    def remove_book(self, isbn):
      for book in self.books:
        if book.isbn == isbn:
          self.books.remove(book)
          self.save_data()
          print("Book removed successfully.")
          return
        print("Book not found.")

    def lend_book(self, isbn, person):
      for book in self.books:
        if book.isbn == isbn:
          if book.quantity > 0:
            book.quantity -= 1
            book.lent_to = person
            self.save_data()
            print("Book lent successfully.")
            return
          else:
            print("Book is not available to lend.")
            return
      print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.lent_to is None:
                    print("Book is not lent.")
                    return
                book.quantity += 1
                book.lent_to = None
                self.save_data()
                print("Book returned successfully.")
                return
        print("Book not found.")

    def view_lent_books(self):
        for book in self.books:
            if book.lent_to is not None:
                print(f"Title: {book.title}, ISBN: {book.isbn}, Lent to: {book.lent_to}, Quanity Remain: {book.quantity}")

