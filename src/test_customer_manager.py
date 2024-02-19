import unittest
from customer import Customer
from customer_manager import CustomerManager


class TestCustomerManager(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("001", "John Doe")
        self.customer2 = Customer("002", "Krista Doe")
        self.manager = CustomerManager()
        self.manager.create_customer(self.customer1)
        self.manager.create_customer(self.customer2)

    def test_create_customer(self):
        self.manager.create_customer(self.customer1)
        expected_customer = self.customer1.to_json()
        self.assertIn(
            expected_customer,
            self.manager.customers,
            "Customer should be added"
            )

    def test_get_customer(self):
        customer = self.manager.get_customer("001")
        self.assertIsNotNone(customer, "Customer should be retrieved by ID")

    def test_update_customer(self):
        updated = self.manager.update_customer("001", name="John Smith")
        self.assertTrue(updated, "Customer should be updated")

    def test_delete_customer(self):
        deleted = self.manager.delete_customer("001")
        self.assertTrue(deleted, "Customer should be deleted")


if __name__ == '__main__':
    unittest.main()
