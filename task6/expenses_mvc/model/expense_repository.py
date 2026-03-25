import json
import os
from model.expense import Expense


class ExpenseRepository:
    def __init__(self, filename="data/expenses.json"):
        self.filename = filename
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def add(self, expense: Expense):
        data = self._load()
        data.append(expense.to_dict())
        self._save(data)

    def delete(self, expense_id):
        data = self._load()
        data = [e for e in data if e["id"] != expense_id]
        self._save(data)

    def get_all(self):
        return self._load()

    def get_total(self):
        data = self._load()
        return sum(e["amount"] for e in data)