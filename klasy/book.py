class Book:

    def __init__(self, library, publication_date, author_name, author_surname, number_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_pages = number_pages

    def __str__(self):
        return f'Książka, autor: {self.author_name} {self.author_surname}, pages: {self.number_pages}'