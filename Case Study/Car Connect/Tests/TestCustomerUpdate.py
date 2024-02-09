import unittest
from exceptions.InvalidInputException import InvalidInputException
from serviceanddatabase.CustomerService import CustomerService
from serviceanddatabase.DatabaseConnect import DatabaseConnect


class TestCustomerUpdate(unittest.TestCase):
    def setUp(self):
        db_context = DatabaseConnect(database="carconnect")
        db_context.connect()
        self.customer_service = CustomerService(db_context)

    def test_update_customer_info(self):
        existing_customer_id = "1"
        updated_info = {
            'FirstName': 'newVatsal',
            'LastName': 'newPatel',
            'Email': 'newVatsal@gmail.com',
            'PhoneNumber': '+91 1234567890',
            'Address': 'new Address',
            'CustomerID': existing_customer_id
        }

        try:
            self.customer_service.update_customer(updated_info)

            updated_customer = self.customer_service.get_customer_by_id(existing_customer_id)
            self.assertEqual(updated_info['FirstName'], updated_customer.first_name)
            self.assertEqual(updated_info['LastName'], updated_customer.last_name)
            self.assertEqual(updated_info['Email'], updated_customer.email)
            self.assertEqual(updated_info['PhoneNumber'], updated_customer.phone_number)
            self.assertEqual(updated_info['Address'], updated_customer.address)

        except InvalidInputException as e:
            self.fail(f"Unexpected exception raised: {e}")


if __name__ == '__main__':
    unittest.main()