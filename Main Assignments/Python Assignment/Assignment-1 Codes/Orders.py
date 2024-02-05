from OrderDetails import OrderDetails

class Orders:
    def __init__(self, order_id, customer, order_date, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_total_amount(self, order_details_list):
        # Calculate the total amount of the order.
        total_amount = 0
        for order_detail in order_details_list:
            total_amount += order_detail.calculate_subtotal()
        return total_amount
        pass

    def get_order_details(self, order_details_list):
        # Retrieves and displays the details of the order (e.g., product list and quantities).
        print(f"Order ID: {self.order_id}")
        print(f"Order Date: {self.order_date}")
        print(f"Total Amount: {self.calculate_total_amount()}")
        print("Order Details:")
        for order_detail in order_details_list:
            order_detail.get_order_detail_info()
        pass

    def update_order_status(self, new_status):
        if new_status in ["Processing", "Shipped", "Delivered", "Cancelled"]:
            self.order_status = new_status
            print(f"Order status updated to: {new_status}")
        else:
            print("Invalid order status.")

        pass

