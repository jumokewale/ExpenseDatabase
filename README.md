# Expense Management Project
## Description
The Expense Management Project revolves around leveraging Python's Object-Oriented Programming (OOP) paradigm to model and effectively manage financial expenses. This initiative centers on the implementation of two crucial classes: 'Expense' and 'ExpenseDatabase'

# Project Components
* expenses.py - Expense Model:
The expenses.py module encapsulates the expense model. This class, Expense, serves as the blueprint for individual financial transactions. It captures essential attributes such as a unique identifier, title, amount, and timestamps for creation and updates.

* test.py - Use Case File:
The test.py module acts as a use case file, providing scenarios to test the functionalities of the implemented classes. This file is instrumental in verifying the accuracy and reliability of the Expense and ExpenseDatabase classes.

# Clone the project
To copy this project, use this repo link: https://github.com/jumokewale/ExpensesDatabase.git 

and on your terminal navigate to your workind directory with cd [current working directory], and use the code below

```bash
git clone https://github.com/jumokewale/ExpensesDatabase.git 
```

Once cloned you will have the copy of the repo on your local computer

# Requirements
* Ensure you have python 3.7 or above installed on your computer
* Installed Git on your local computer

# How to run the code
To run `expenses.py` on your terminal press the command
```bash
python3 expenses.py
```

To run an example and test the use case, you can run `test.py` using the code below
```bash
python3 expenses.py
```

Using an example of `test.py`
```bash
from expenses import Expense, ExpenseDatabase


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
```

We would get the output below
```bash
Initial Expense:
{'id': '9430a7c9-fbfe-4026-bb3d-88d09d275d7e', 'title': 'Groceries', 'amount': 50.0, 'created_at': '2023-12-24T20:48:46.088983', 'updated_at': '2023-12-24T20:48:46.088983'}

Updated Expense:
{'id': '9430a7c9-fbfe-4026-bb3d-88d09d275d7e', 'title': 'New Title', 'amount': 75.0, 'created_at': '2023-12-24T20:48:46.088983', 'updated_at': '2023-12-24T20:48:46.089590'}
All Expenses:
[{'id': 'e5f35edb-fd93-4b31-9be5-17c357a753ec', 'title': 'Groceries', 'amount': 50.0, 'created_at': '2023-12-24T20:48:46.089622', 'updated_at': '2023-12-24T20:48:46.089622'}, {'id': '27bfa761-70b4-4e3f-b644-3b80f478d9f0', 'title': 'Dining', 'amount': 30.0, 'created_at': '2023-12-24T20:48:46.089629', 'updated_at': '2023-12-24T20:48:46.089629'}]

Remaining Expenses:
[{'id': '27bfa761-70b4-4e3f-b644-3b80f478d9f0', 'title': 'Dining', 'amount': 30.0, 'created_at': '2023-12-24T20:48:46.089629', 'updated_at': '2023-12-24T20:48:46.089629'}]

Retrieved Expense by ID:
{'id': '27bfa761-70b4-4e3f-b644-3b80f478d9f0', 'title': 'Dining', 'amount': 30.0, 'created_at': '2023-12-24T20:48:46.089629', 'updated_at': '2023-12-24T20:48:46.089629'}

Expenses with Title 'Dining':
[{'id': '27bfa761-70b4-4e3f-b644-3b80f478d9f0', 'title': 'Dining', 'amount': 30.0, 'created_at': '2023-12-24T20:48:46.089629', 'updated_at': '2023-12-24T20:48:46.089629'}]
```

