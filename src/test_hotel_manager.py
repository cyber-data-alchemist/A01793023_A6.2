import unittest
from hotel import Hotel
from hotel_manager import HotelManager


class TestHotelManager(unittest.TestCase):
    def setUp(self):
        self.hotel1 = Hotel(
            "001", "Test Hotel", [{"101": "Available"}, {"102": "Booked"}]
            )
        self.hotel2 = Hotel(
            "002", "Sample Hotel", [{"201": "Occupied"}, {"202": "Available"}]
            )
        self.manager = HotelManager()
        self.manager.create_hotel(self.hotel1)
        self.manager.create_hotel(self.hotel2)

    def test_create_hotel(self):
        self.manager.create_hotel(self.hotel1)
        expected_hotel = self.hotel1.to_json()
        self.assertIn(expected_hotel,
                      self.manager.hotels, "Hotel should be added")

    def test_get_hotel(self):
        hotel = self.manager.get_hotel("001")
        self.assertIsNotNone(hotel, "Hotel should be retrieved by ID")

    def test_update_hotel(self):
        updated = self.manager.update_hotel("001", name="Updated Hotel")
        self.assertTrue(updated, "Hotel should be updated")

    def test_delete_hotel(self):
        deleted = self.manager.delete_hotel("001")
        self.assertTrue(deleted, "Hotel should be deleted")


if __name__ == '__main__':
    unittest.main()
