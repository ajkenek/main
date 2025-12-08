from klasy.employee import Employee
from klasy.book import Book
from klasy.order import Order
from klasy.student import Student
from klasy.library import Library

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


print(order1)
print("\n")
print(order2)
