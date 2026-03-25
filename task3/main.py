from library.book import Book
from library.library import Library

from restaurant.dish import Dish
from restaurant.order import Order
from restaurant.restaurant import Restaurant

from students.student import Student
from students.database import StudentDatabase


# ---- Library ----
lib = Library()
lib.add_book(Book("1984", "Orwell", 300, 1))
print(lib.find_book("1984"))


# ---- Restaurant ----
restaurant = Restaurant()
dish = Dish("Піца", 200, "Основне")
restaurant.add_dish(dish)

order = Order()
order.add_dish(dish)
print("Сума:", order.total_price())


# ---- Students ----
db = StudentDatabase("data/students.json")
student = Student("Іван", 20, [90, 85, 88])
db.add_student(student)

print(db.find_student("Іван"))