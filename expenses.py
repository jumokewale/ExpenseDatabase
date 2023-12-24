import uuid
import datetime


class Expense():
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title, amount):
        if self.title is not None:
            self.title = title
        if self.amount is not None:
            self.amount = amount
        self.updated_at = datetime.datetime.utcnow()
        
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    

class ExpenseDatabase():
    def __init__(self):
        self.expenses = []


    def add_expense(self, expense):
        self.expenses.append(expense)


    def remove_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                break

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
            
        return None

    def get_expense_by_title(self, expense_title):
        expense_list = []
        for expense in self.expenses:
            if expense.title == expense_title:
                expense_list.append(expense)
                return expense_list
            
       

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
    



if __name__ == "__main__":
    # Create an expense
    expense = Expense(title="Groceries", amount=50.0)

    # Print the initial expense details
    print("Initial Expense:")
    print(expense.to_dict())

    # Update the expense
    expense.update(title="New Title", amount=75.0)

    # Print the updated expense details
    print("\nUpdated Expense:")
    print(expense.to_dict())



# Example Usage:
if __name__ == "__main__":
    # Create an ExpenseDB instance
    expense_db = ExpenseDatabase()

    # Add expenses to the database
    expense1 = Expense(title="Groceries", amount=50.0)
    expense2 = Expense(title="Dining", amount=30.0)

    expense_db.add_expense(expense1)
    expense_db.add_expense(expense2)

    # Print all expenses in the database
    print("All Expenses:")
    print(expense_db.to_dict())

    # Remove an expense by ID
    expense_db.remove_expense(expense1.id)

    # Print remaining expenses
    print("\nRemaining Expenses:")
    print(expense_db.to_dict())

    # Get an expense by ID
    retrieved_expense = expense_db.get_expense_by_id(expense2.id)
    print("\nRetrieved Expense by ID:")
    print(retrieved_expense.to_dict())

    # Get expenses by title
    expenses_by_title = expense_db.get_expense_by_title("Dining")
    print("\nExpenses with Title 'Dining':")
    print([expense.to_dict() for expense in expenses_by_title])