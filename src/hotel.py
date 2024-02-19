"""
    Hotel class
"""
# pylint: disable=too-few-public-methods


class Hotel:
    """
    Hotel model
    """
    def __init__(self, hotel_id, name, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms

    def to_json(self):
        """
        Get a dictionary of the hotel
        """
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "rooms": self.rooms
        }
