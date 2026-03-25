class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, name):
        self.dishes = [d for d in self.dishes if d.name != name]

    def total_price(self):
        return sum(d.price for d in self.dishes)