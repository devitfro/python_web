class ExpenseView:
    @staticmethod
    def show_expenses(expenses):
        print("\n--- EXPENSES ---")
        for e in expenses:
            print(f"{e['id']} | {e['title']} | {e['amount']}")

    @staticmethod
    def show_total(total):
        print(f"\nTOTAL: {total}")