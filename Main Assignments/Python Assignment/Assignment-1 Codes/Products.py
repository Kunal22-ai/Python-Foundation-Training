from Customers import Customers

class Products:
    def __init__(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    def get_product_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price}")
        pass

    def update_product_info(self, new_price, new_description):
        # Allows updates to product details (e.g., price, description).
        if new_price:
            self.price = new_price
        if new_description:
            self.description = new_description
        print("Product information updated successfully.")
        pass

