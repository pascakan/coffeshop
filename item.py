
# Represents an individual item with a name, price, and stock level
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        # Updates the stock level; raises an error if insufficient stock
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Not enough stock to remove.")
        self.stock += quantity

    def __str__(self):
        # Returns a string representation of the item
        return f"{self.name} - ${self.price} ({self.stock} in stock)"
