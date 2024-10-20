from PyQt5.QtWidgets import QLabel, QHBoxLayout

class TotalSection:
    def __init__(self, parent):
        self.parent = parent

        # Create layout and label for displaying the total
        self.layout = QHBoxLayout()
        self.total_label = QLabel("Total: ")
        self.total_value = QLabel("0.00")

        self.layout.addWidget(self.total_label)
        self.layout.addWidget(self.total_value)

    def update_total(self, total):
        # Update the total value displayed
        self.total_value.setText(f"{total:.2f}")
