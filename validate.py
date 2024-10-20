
class ValidateInput:
    def init(self):
        pass

    def validate_expenseName(self, expense_name):
        if not expense_name.strip():
            raise ValueError("Expense name cannot be empty.")
        return True

    def validate_price(self, price):
        if not price.strip():
            raise ValueError("Price cannot be empty.")
        try:
            price_value = float(price)
            if price_value < 0:
                raise ValueError("Price cannot be negative.")
        except ValueError:
            raise ValueError("Price must be a valid number.")
        return True