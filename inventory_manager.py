from item import Item

# Manages the inventory of items
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        # Adds a new item to the inventory; raises an error if it already exists
        if item.name in self.items:
            raise ValueError("Item already exists in inventory.")
        self.items[item.name] = item

    def update_stock(self, item_name, quantity):
        # Updates the stock of a specific item; raises an error if item not found
        if item_name not in self.items:
            raise ValueError("Item not found in inventory.")
        self.items[item_name].update_stock(quantity)

    def check_stock(self, item_name):
        # Checks the stock of a specific item
        if item_name not in self.items:
            return 0
        return self.items[item_name].stock

    def __str__(self):
        # Returns a string representation of the entire inventory
        return "\n".join(str(item) for item in self.items.values())