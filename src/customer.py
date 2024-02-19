"""
    Customer class
"""
# pylint: disable=too-few-public-methods


class Customer:
    """
    Customer model
    """
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def to_json(self):
        """
        Get a dictionary of the customer
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name
        }
