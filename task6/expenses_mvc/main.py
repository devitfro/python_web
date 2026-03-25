from controller.expense_controller import ExpenseController

app = ExpenseController()

app.add_expense(1, "Coffee", 50)
app.add_expense(2, "Taxi", 200)

app.show_expenses()
app.show_total()

app.delete_expense(1)

app.show_expenses()
app.show_total()