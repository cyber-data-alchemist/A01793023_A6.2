"""
    Reservation class
"""
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments


class Reservation:
    """
    Hotel model
    """
    def __init__(
            self, reservation_id, customer_id, hotel_id,
            room_number, start_date, end_date
            ):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def to_json(self):
        """
        Get a dictionary of the hotel
        """
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
            "room_number": self.room_number,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
