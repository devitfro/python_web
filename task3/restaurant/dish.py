class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def description(self):
        return f"{self.name} - {self.price} грн ({self.category})"