import unittest
from hotel import Hotel
from customer import Customer
from reservation import Reservation
from hotel_manager import HotelManager
from customer_manager import CustomerManager
from reservation_manager import ReservationManager


class TestHotelAndReservationManager(unittest.TestCase):
    def setUp(self):
        self.hotel_manager = HotelManager()
        self.hotel1 = Hotel(
            "H001", "Test Hotel", {"101": "Available", "102": "Booked"}
            )
        self.hotel2 = Hotel(
            "H002", "Sample Hotel", {"201": "Occupied", "202": "Available"}
            )
        self.hotel_manager.create_hotel(self.hotel1)
        self.hotel_manager.create_hotel(self.hotel2)

        self.customer_manager = CustomerManager()
        self.customer1 = Customer("C001", "John Doe")
        self.customer2 = Customer("C002", "Krista Doe")
        self.customer_manager.create_customer(self.customer1)
        self.customer_manager.create_customer(self.customer2)

        self.reservation_manager = ReservationManager()
        self.reservation1 = Reservation(
            "R001", "C001", "H001", "101", "2024-04-01", "2024-04-05"
            )
        self.reservation2 = Reservation(
            "R002", "C002", "H002", "202", "2024-05-01", "2024-05-05"
            )
        self.reservation_manager.create_reservation(self.reservation1)
        self.reservation_manager.create_reservation(self.reservation2)

    def test_create_and_get_hotel(self):
        self.assertIn(self.hotel1.to_json(), self.hotel_manager.hotels,
                      "Hotel should be added")
        hotel = self.hotel_manager.get_hotel("H001")
        self.assertIsNotNone(hotel, "Hotel should be retrievable")

    def test_update_and_delete_hotel(self):
        self.hotel_manager.update_hotel("H001", name="Updated Hotel")
        updated_hotel = self.hotel_manager.get_hotel("H001")
        self.assertEqual(updated_hotel['name'], "Updated Hotel",
                         "Hotel name should be updated")
        self.hotel_manager.delete_hotel("H001")
        self.assertIsNone(self.hotel_manager.get_hotel("H001"),
                          "Hotel should be deleted")

    def test_create_and_get_reservation(self):
        self.assertIn(self.reservation1.to_json(),
                      self.reservation_manager.reservations,
                      "Reservation should be added")
        reservation = self.reservation_manager.get_reservation("R001")
        self.assertIsNotNone(reservation, "Reservation should be retrievable")

    def test_update_and_delete_reservation(self):
        self.reservation_manager.update_reservation(
            "R001", start_date="2024-04-02", end_date="2024-04-06")
        updated_reservation = self.reservation_manager.get_reservation("R001")
        self.assertEqual(updated_reservation['start_date'], "2024-04-02",
                         "Start date should be updated")
        self.assertEqual(updated_reservation['end_date'], "2024-04-06",
                         "End date should be updated")
        self.reservation_manager.delete_reservation("R001")
        self.assertIsNone(self.reservation_manager.get_reservation("R001"),
                          "Reservation should be deleted")


if __name__ == '__main__':
    unittest.main()
