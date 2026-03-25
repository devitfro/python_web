from model.expense import Expense
from model.expense_repository import ExpenseRepository
from view.expense_view import ExpenseView


class ExpenseController:
    def __init__(self):
        self.repo = ExpenseRepository()
        self.view = ExpenseView()

    def add_expense(self, id, title, amount):
        expense = Expense(id, title, amount)
        self.repo.add(expense)

    def delete_expense(self, expense_id):
        self.repo.delete(expense_id)

    def show_expenses(self):
        data = self.repo.get_all()
        self.view.show_expenses(data)

    def show_total(self):
        total = self.repo.get_total()
        self.view.show_total(total)