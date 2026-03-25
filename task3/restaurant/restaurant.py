class Restaurant:
    def __init__(self):
        self.menu = []

    def add_dish(self, dish):
        self.menu.append(dish)

    def show_menu(self):
        for dish in self.menu:
            print(dish.description())