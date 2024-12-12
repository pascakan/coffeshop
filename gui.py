import customtkinter as ctk
from inventory_manager import Inventory
from item import Item
from order import Order

# Main GUI application for the Coffee Shop Management System
class CoffeeShopApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Shop Management System")
        self.geometry("600x400")

        # Initialize inventory and order management
        self.inventory = Inventory()
        self.order = Order()

        self.setup_gui()

    def setup_gui(self):
        # Sets up the GUI components for managing inventory and orders
        self.add_item_frame = ctk.CTkFrame(self)
        self.add_item_frame.pack(pady=10)

        # Input fields for adding new items to the inventory
        ctk.CTkLabel(self.add_item_frame, text="Item Name:").grid(row=0, column=0, padx=5)
        self.item_name_entry = ctk.CTkEntry(self.add_item_frame)
        self.item_name_entry.grid(row=0, column=1, padx=5)

        ctk.CTkLabel(self.add_item_frame, text="Price:").grid(row=1, column=0, padx=5)
        self.item_price_entry = ctk.CTkEntry(self.add_item_frame)
        self.item_price_entry.grid(row=1, column=1, padx=5)

        ctk.CTkLabel(self.add_item_frame, text="Stock:").grid(row=2, column=0, padx=5)
        self.item_stock_entry = ctk.CTkEntry(self.add_item_frame)
        self.item_stock_entry.grid(row=2, column=1, padx=5)

        # Button to add a new item to the inventory
        self.add_item_button = ctk.CTkButton(self.add_item_frame, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Display for the current inventory
        self.inventory_label = ctk.CTkLabel(self, text="Inventory:")
        self.inventory_label.pack(pady=10)
        self.inventory_display = ctk.CTkTextbox(self, width=500, height=100)
        self.inventory_display.pack()

        # Input fields and button for placing an order
        self.order_frame = ctk.CTkFrame(self)
        self.order_frame.pack(pady=10)

        ctk.CTkLabel(self.order_frame, text="Order Item:").grid(row=0, column=0, padx=5)
        self.order_item_entry = ctk.CTkEntry(self.order_frame)
        self.order_item_entry.grid(row=0, column=1, padx=5)

        ctk.CTkLabel(self.order_frame, text="Quantity:").grid(row=1, column=0, padx=5)
        self.order_quantity_entry = ctk.CTkEntry(self.order_frame)
        self.order_quantity_entry.grid(row=1, column=1, padx=5)

        self.add_order_button = ctk.CTkButton(self.order_frame, text="Add to Order", command=self.add_to_order)
        self.add_order_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Button to display the order summary
        self.order_summary_button = ctk.CTkButton(self, text="Show Order Summary", command=self.show_order_summary)
        self.order_summary_button.pack(pady=10)

        # Display for the order summary
        self.order_display = ctk.CTkTextbox(self, width=500, height=100)
        self.order_display.pack()

    def add_item(self):
        try:
            name = self.item_name_entry.get()
            price = float(self.item_price_entry.get())
            stock = int(self.item_stock_entry.get())
            item = Item(name, price, stock)
            self.inventory.add_item(item)
            self.update_inventory_display()
        except ValueError as e:
            self.show_error(str(e))

    def add_to_order(self):
        try:
            name = self.order_item_entry.get()
            quantity = int(self.order_quantity_entry.get())
            if name not in self.inventory.items:
                raise ValueError("Item not found in inventory.")
            item = self.inventory.items[name]
            self.order.add_item(item, quantity)
            self.update_inventory_display()
        except ValueError as e:
            self.show_error(str(e))

    def show_order_summary(self):
        self.order_display.delete("1.0", "end")
        self.order_display.insert("1.0", self.order.get_order_summary())

    def update_inventory_display(self):
        self.inventory_display.delete("1.0", "end")
        self.inventory_display.insert("1.0", str(self.inventory))

    def show_error(self, message):
        error_window = ctk.CTkToplevel(self)
        error_window.title("Error")
        ctk.CTkLabel(error_window, text=message).pack(pady=10)
        ctk.CTkButton(error_window, text="OK", command=error_window.destroy).pack(pady=10)

if __name__ == "__main__":
    app = CoffeeShopApp()
    app.mainloop()