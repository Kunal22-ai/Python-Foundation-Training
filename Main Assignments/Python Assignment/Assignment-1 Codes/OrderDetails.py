
class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.quantity * self.product.price

    def get_order_detail_info(self):
        print(f"Order Detail ID: {self.order_detail_id}")
        print(f"Product: {self.product.product_name}")
        print(f"Quantity: {self.quantity}")
        print(f"Subtotal: ${self.calculate_subtotal()}")

    def update_quantity(self, new_quantity):

        if new_quantity > 0:
            self.quantity = new_quantity
            print(f"Quantity updated to: {new_quantity}")
        else:
            print("Invalid quantity.")

    def add_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            discount_amount = (discount_percentage / 100) * self.calculate_subtotal()
            discounted_subtotal = self.calculate_subtotal() - discount_amount
            print(f"Discount applied: {discount_percentage}%")
            print(f"Discounted Subtotal: ${discounted_subtotal}")
        else:
            print("Invalid discount percentage.")

