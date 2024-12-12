from item import Item

# Manages customer orders
class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def add_item(self, item, quantity):
        # Adds an item to the order and updates the total price; checks stock availability
        if quantity > item.stock:
            raise ValueError("Not enough stock for this item.")
        self.items.append((item, quantity))
        item.update_stock(-quantity)
        self.total_price += item.price * quantity

    def calculate_total(self):
        # Calculates the total price of the order
        return self.total_price

    def get_order_summary(self):
        # Generates a summary of the order
        summary = "\n".join(
            f"{item.name} x{quantity} - ${item.price * quantity}" for item, quantity in self.items
        )
        return summary + f"\nTotal: ${self.calculate_total()}"