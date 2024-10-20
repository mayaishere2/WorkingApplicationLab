from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QHBoxLayout

class InputSection:
    def __init__(self, parent = None):
        self.parent = parent  # Reference to ExpenseApp

        # Create input fields for expense and price
        self.layout = QHBoxLayout()
        self.expense_input = QLineEdit()
        self.price_input = QLineEdit()
        self.parent = parent
        # Add labels and inputs to the layout
        self.layout.addWidget(QLabel("Expense:"))
        self.layout.addWidget(self.expense_input)
        self.layout.addWidget(QLabel("Price:"))
        self.layout.addWidget(self.price_input)

        # Add a button to add the expense
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.handle_add_expense)
        self.layout.addWidget(self.add_button)
        # In InputSection or wherever you want to place the delete button
        self.remove_button = QPushButton("Remove Expense")
        self.remove_button.clicked.connect(self.parent.remove_expense)
        self.layout.addWidget(self.remove_button)


    def handle_add_expense(self):
        # Get the input values
        expense_name = self.expense_input.text()
        price_text = self.price_input.text()

        # Call the add_expense method in the parent (ExpenseApp)
        self.parent.add_expense(expense_name, price_text)

        # Clear the input fields
        self.expense_input.clear()
        self.price_input.clear()
