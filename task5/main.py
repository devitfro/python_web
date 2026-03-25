from models.bank_account import BankAccount

from models.shapes import Circle, Rectangle, Triangle, print_area
from models.person_book import Person, Book, serialize_object

from metaclasses.hello_meta import HelloMeta


print("---- DESCRIPTORS ----")
acc = BankAccount("Alice", 100)
print(acc.owner)
print(acc.balance)


print("\n---- SHAPES ----")
print_area(Circle(5))
print_area(Rectangle(2, 3))
print_area(Triangle(4, 6))


print("\n---- SERIALIZE ----")
p = Person("John", 25)
b = Book("Python", "Guido")

print(serialize_object(p))
print(serialize_object(b))