class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def calculate_total_orders(self):
        # Calculate the total number of orders placed by this customer.
        pass

    def get_customer_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        pass

    def update_customer_info(self, new_email=None, new_phone=None, new_address=None):
        if new_email:
            self.email = new_email
        if new_phone:
            self.phone = new_phone
        if new_address:
            self.address = new_address
        print("Customer information updated successfully.")
        pass
