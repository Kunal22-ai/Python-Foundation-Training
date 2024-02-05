class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

    def get_product(self):
        # A method to retrieve the product associated with this inventory item.
        return self.product

    def get_quantity_in_stock(self):
        # A method to get the current quantity of the product in stock.
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        if quantity > 0:
            self.quantity_in_stock += quantity
            print(f"{quantity} units of {self.product.product_name} added to inventory.")
        else:
            print("Invalid quantity.")

    def remove_from_inventory(self, quantity):
        # A method to remove a specified quantity of the product from the inventory.
        if 0 < quantity <= self.quantity_in_stock:
            self.quantity_in_stock -= quantity
            print(f"{quantity} units of {self.product.product_name} removed from inventory.")
        else:
            print("Invalid quantity or insufficient stock.")

    def update_stock_quantity(self, new_quantity):
        # A method to update the stock quantity to a new value.
        if new_quantity >= 0:
            self.quantity_in_stock = new_quantity
            print(f"Stock quantity updated to: {new_quantity}")
        else:
            print("Invalid stock quantity.")

    def is_product_available(self, quantity_to_check):
        # A method to check if a specified quantity of the product is available in the inventory.
        return quantity_to_check <= self.quantity_in_stock

    def get_inventory_value(self):
        # A method to calculate the total value of the products in the inventory based on their prices and quantities.
        return self.product.price * self.quantity_in_stock

    def list_low_stock_products(self, threshold):
        # A method to list products with quantities below a specified threshold, indicating low stock.
        if self.quantity_in_stock < threshold:
            print(f"{self.product.product_name} is low on stock ({self.quantity_in_stock} units).")

    def list_out_of_stock_products(self):
        # A method to list products that are out of stock.
        if self.quantity_in_stock == 0:
            print(f"{self.product.product_name} is out of stock.")

    def list_all_products(self):
        # A method to list all products in the inventory, along with their quantities.
        print(f"Product: {self.product.product_name}, Quantity in Stock: {self.quantity_in_stock}")

