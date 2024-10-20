from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem ,QMessageBox

class TableSection:
    def __init__(self, parent, cursor):
        self.parent = parent
        self.cursor = cursor  # Database cursor
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Expense", "Price"])
        
        # Load existing data from the database
        self.load_data()

    def load_data(self):
        # Retrieve data from the database
        self.cursor.execute("SELECT name, price FROM expenses")
        rows = self.cursor.fetchall()

        # Populate the table
        self.table.setRowCount(0)
        for row_data in rows:
            self.add_expense(row_data[0], row_data[1])

    def add_expense(self, expense_name, price):
        try:
            expense_name = expense_name.strip()
            price = float(price)  # Validate that price is a float
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Price must be a valid number.")
            return
        # Insert a new row in the table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(expense_name))
        self.table.setItem(row_position, 1, QTableWidgetItem(f"{price:.2f}"))

        # Insert the expense into the database
        self.cursor.execute("INSERT INTO expenses (name, price) VALUES (?, ?)", (expense_name, price))
        self.parent.conn.commit()

    def calculate_total(self):
        # Calculate the total of all expenses in the table
        total = 0.0
        for row in range(self.table.rowCount()):
            price_item = self.table.item(row, 1)
            if price_item:
                total += float(price_item.text())
        return total
