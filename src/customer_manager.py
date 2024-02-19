"""
Class to manage customers
"""

import json
import os


class CustomerManager:
    """
    Manages a collection of customers
    """
    def __init__(self, filepath='data/customers.json'):
        self.filepath = filepath
        self.customers = self._load_customers()

    def _load_customers(self):
        """
        Loads customers from the JSON file
        """
        if not os.path.exists(self.filepath):
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_customers(self):
        """
        Saves the current state of customers to the JSON file.
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(self.customers, file, indent=4)

    def _find_customer_index_by_id(self, customer_id):
        """
        Finds the index of a customer by its ID in the customer list.
        Returns the index if found, otherwise returns None.
        """
        return next((i for i, h in enumerate(self.customers)
                     if h['customer_id'] == customer_id), None)

    def create_customer(self, customer):
        """
        Adds a new customer to the collection and saves the file.
        """
        # Delete if it exists
        existing_customer_index = self._find_customer_index_by_id(
            customer.customer_id)
        if existing_customer_index is not None:
            del self.customers[existing_customer_index]
        # Create
        self.customers.append(customer.to_json())
        self._save_customers()

    def get_customer(self, customer_id):
        """
        Retrieves a customer by their ID.
        """
        for customer in self.customers:
            if customer['customer_id'] == customer_id:
                return customer

    def update_customer(self, customer_id, **kwargs):
        """
        Updates properties of a customer identified by their ID.
        """
        for customer in self.customers:
            if customer['customer_id'] == customer_id:
                customer.update(kwargs)
                self._save_customers()
                return True

    def delete_customer(self, customer_id):
        """
        Removes a customer from the collection by their ID and saves the file.
        """
        for i, customer in enumerate(self.customers):
            if customer['customer_id'] == customer_id:
                del self.customers[i]
                self._save_customers()
                return True
