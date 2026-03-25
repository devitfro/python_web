class Expense:
    def __init__(self, id, title, amount):
        self.id = id
        self.title = title
        self.amount = amount

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount
        }