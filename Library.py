class Book:
    def __init__(self, title, authors, release_date, page_count, summary):
        self.title = title
        self.authors = authors
        self.release_date = release_date
        self.page_count = page_count
        self.summary = summary

class Character:
    def __init__(self, name, books, involvement_level):
        self.name = name
        self.books = books
        self.involvement_level = involvement_level

class Series:
    def __init__(self, name, books):
        self.name = name
        self.books = books

class Library:
    def __init__(self):
        self.books = []
        self.authors = []

    def add_book(self, book):
        self.books.append(book)

    def edit_book(self, book_title, new_title=None, new_authors=None, new_release_date=None, new_page_count=None, new_summary=None):
        for book in self.books:
            if book.title == book_title:
                if new_title:
                    book.title = new_title
                if new_authors:
                    book.authors = new_authors
                if new_release_date:
                    book.release_date = new_release_date
                if new_page_count:
                    book.page_count = new_page_count
                if new_summary:
                    book.summary = new_summary
                break

    def delete_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                break

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower():
                results.append(book)
        return results

    def add_author(self, author):
        self.authors.append(author)

    def edit_author(self, author_name, new_name):
        for author in self.authors:
            if author == author_name:
                author = new_name
                break

    def delete_author(self, author_name):
        self.authors.remove(author_name)

    def search_authors(self, query):
        results = []
        for author in self.authors:
            if query.lower() in author.lower():
                results.append(author)
        return results

# Создать экземпляр библиотеки
library = Library()

# Добавьте книги в библиотеку
book1 = Book("The Lost Kingdom", ["Emily Roberts"], "January 1, 2022", 300, "A thrilling adventure in the mystical land of Avalon.")
book2 = Book("The Enchanted Forest", ["Emily Roberts"], "July 15, 2023", 350, "Amelia and Benjamin embark on a quest to save the enchanted forest.")
library.add_book(book1)
library.add_book(book2)

# Редактировать книгу
library.edit_book("The Lost Kingdom", new_title="The Kingdom of Avalon")

# Удалить книгу
library.delete_book("The Enchanted Forest")

# Поиск книг
results = library.search_books("Kingdom")
for book in results:
    print("Title:", book.title)
    print("Authors:", ", ".join(book.authors))
    print("Release Date:", book.release_date)
    print("Page Count:", book.page_count)
    print("Summary:", book.summary)
    print()

# Добавить авторов в библиотеку
library.add_author("Emily Roberts")
library.add_author("Michael Anderson")

# Изменить автора
library.edit_author("Emily Roberts", "Emily R.")

# Удалить автора
library.delete_author("Michael Anderson")

# Поиск авторов
results = library.search_authors("Emily")
for author in results:
    print("Author:", author)
