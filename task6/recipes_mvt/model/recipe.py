class Recipe:
    def __init__(self, id, title, desc, ingredients, steps):
        self.id = id
        self.title = title
        self.desc = desc
        self.ingredients = ingredients
        self.steps = steps

    def to_dict(self):
        return self.__dict__