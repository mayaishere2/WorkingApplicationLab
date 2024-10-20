import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMenuBar, QMenu, QMessageBox
from input_section import InputSection
from table_section import TableSection
from total_section import TotalSection
import sqlite3

class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 300)

        # Initialize the database connection and cursor
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()

        # Create the expenses table if it doesn't exist
        self.create_table()

        # Create a central widget and set it as the central widget of the QMainWindow
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a menu bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        file_menu = QMenu("File", self)
        edit_menu = QMenu("Edit", self)
        help_menu = QMenu("Help", self)
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(edit_menu)
        menu_bar.addMenu(help_menu)

        # Create the InputSection, TableSection, and TotalSection
        self.input_section = InputSection(self)
        layout.addLayout(self.input_section.layout)

        self.table_section = TableSection(self, self.cursor)
        layout.addWidget(self.table_section.table)

        self.total_section = TotalSection(self)
        layout.addLayout(self.total_section.layout)

        # Initialize with default data
        initial_data = [("Veg", 40.0), ("Fruit", 70.0), ("Fuel", 60.0)]
        for expense, price in initial_data:
            self.table_section.add_expense(expense, price)
        self.update_total()

    def create_table(self):
        """Create the expenses table if it doesn't exist"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_expense(self, expense_name, price_text):
        # Add a new row to the table
        self.table_section.add_expense(expense_name, price_text)
        # Update the total
        self.update_total()

    def remove_expense(self):
        selected_row = self.table_section.table.currentRow()

        if selected_row != -1:
            # Get the expense name and price from the selected row
            expense_name = self.table_section.table.item(selected_row, 0).text()
            price_value = float(self.table_section.table.item(selected_row, 1).text())

            # Remove the item from the database
            self.cursor.execute("DELETE FROM expenses WHERE name = ? AND price = ?", (expense_name, price_value))
            self.conn.commit()

            # Remove the row from the table
            self.table_section.table.removeRow(selected_row)

            # Update the total after removing
            self.update_total()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a row to delete.")

    def update_total(self):
        total = self.table_section.calculate_total()
        self.total_section.update_total(total)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())
