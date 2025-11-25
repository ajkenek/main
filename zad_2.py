class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student {self.name}"

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Bibliotetka w {self.city}, {self.street}, {self.zip_code}, godziny otwarcia: {self.open_hours}, telefon: {self.phone}'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date ,city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name}'

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_pages = number_pages

    def __str__(self):
        return f'Książka, autor: {self.author_name} {self.author_surname}, pages: {self.number_pages}'

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n    - ".join([str(book) for book in self.books])
        return (
            f"=== ZAMÓWIENIE z dnia {self.order_date} ===\n"
            f"Obsługuje: {self.employee}\n"
            f"Dla: {self.student}\n"
            f"Książki:\n    - {books_str}\n"
            f"========================================"
        )

s1 = Student("Mati", [3, 4, 5])
s2 = Student("Wika", [5, 5, 6])
s3 = Student("Tomek", [2, 2, 3])

lib_katowice = Library("Katowice", "Mariacka 1", "40-001", "8:00-16:00", "123-456-789")
lib_gliwice = Library("Gliwice", "Akademicka 2", "44-100", "10:00-18:00", "987-654-321")

emp1 = Employee("Jan", "Kowalski", "2020-01-01", "1980-05-12", "Katowice", "Młyńska", "40-002", "111-222")
emp2 = Employee("Anna", "Nowak", "2021-06-15", "1995-08-20", "Gliwice", "Rynek", "44-102", "333-444")
emp3 = Employee("Piotr", "Zieliński", "2019-11-01", "1975-02-14", "Zabrze", "Wolności", "41-800", "555-666")

b1 = Book(lib_katowice, "2023", "J.K.", "Rowling", 300)
b2 = Book(lib_katowice, "2020", "George", "Orwell", 250)
b3 = Book(lib_gliwice, "2019", "Stephen", "King", 600)
b4 = Book(lib_gliwice, "2021", "Remigiusz", "Mróz", 400)
b5 = Book(lib_katowice, "2018", "Andrzej", "Sapkowski", 350)

order1 = Order(emp1, s1, [b1, b2, b5], "2025-11-25")

order2 = Order(emp2, s2, [b3, b4], "2025-11-26")

# --- FINALE: WYŚWIETLANIE ---
print(order1)
print("\n") # Odstęp
print(order2)