from vehicles.car import Car
from vehicles.boat import Boat
from vehicles.amphibious_vehicle import AmphibiousVehicle

from library.book import Book
from library.library import Library

from cache.cache_decorator import CacheDecorator


# ---- Vehicles ----
car = Car("BMW", 200)
car.start_engine()
car.drive()

boat = Boat("motor", 80)
boat.drive()

av = AmphibiousVehicle("JeepBoat", "motor", 90)
av.drive()
av.is_on_land = False
av.drive()


# ---- Library ----
lib = Library()

b1 = Book("1984", "Orwell", 300)
b2 = Book("HP", "Rowling", 400)

lib += b1
lib += b2

print(len(lib))
print(b1 < b2)
print(b1 in lib)


# ---- Cache ----
class Calc:

    @CacheDecorator
    def add(self, a, b):
        return a + b


calc = Calc()
print(calc.add(2, 3))
print(calc.add(2, 3))
print(calc.add(5, 7))