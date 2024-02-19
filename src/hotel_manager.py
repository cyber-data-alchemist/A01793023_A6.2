"""
Class to manage hotels
"""
import json
import os


class HotelManager:
    """
    Manages a collection of hotels
    """
    def __init__(self, filepath='data/hotels.json'):
        self.filepath = filepath
        self.hotels = self._load_hotels()

    def _load_hotels(self):
        if not os.path.exists(self.filepath):
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, 'w', encoding='utf-8') as file:
                json.dump([], file)
        with open(self.filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _save_hotels(self):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(self.hotels, file, indent=4)

    def _find_hotel_index_by_id(self, hotel_id):
        """
        Finds the index of a hotel by its ID in the hotels list.
        Returns the index if found, otherwise returns None.
        """
        return next((i for i, h in enumerate(self.hotels)
                     if h['hotel_id'] == hotel_id), None)

    def create_hotel(self, hotel):
        """
        Adds a new hotel to the collection and saves the file.
        """
        # Delete if it exists
        existing_hotel_index = self._find_hotel_index_by_id(hotel.hotel_id)
        if existing_hotel_index is not None:
            del self.hotels[existing_hotel_index]

        # Create
        self.hotels.append(hotel.to_json())
        self._save_hotels()

    def get_hotel(self, hotel_id):
        """
        Retrieves a hotel by its ID.
        """
        for hotel in self.hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def update_hotel(self, hotel_id, **kwargs):
        """
        Updates properties of a hotel identified by its ID.
        """
        for hotel in self.hotels:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(kwargs)
                self._save_hotels()
                return True

    def delete_hotel(self, hotel_id):
        """
        Removes a hotel from the collection by its ID and saves the file.
        """
        for i, hotel in enumerate(self.hotels):
            if hotel['hotel_id'] == hotel_id:
                del self.hotels[i]
                self._save_hotels()
                return True
