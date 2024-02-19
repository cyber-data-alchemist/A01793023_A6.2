"""
Class to manage reservations
"""

import json
import os


class ReservationManager:
    """
    Manages a collection of reservations
    """
    def __init__(self, filepath='data/reservations.json'):
        self.filepath = filepath
        self.reservations = self._load_reservations()

    def _load_reservations(self):
        """
        Loads reservations from the JSON file
        """
        if not os.path.exists(self.filepath):
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, 'w', encoding='utf-8') as fil:
                json.dump([], fil)
        with open(self.filepath, 'r', encoding='utf-8') as fil:
            return json.load(fil)

    def _save_reservations(self):
        """
        Saves the current state of reservations to the JSON file.
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(self.reservations, file, indent=4)

    def _find_reservation_index_by_id(self, reservation_id):
        """
        Finds the index of a reservation by its ID in the reservation list.
        Returns the index if found, otherwise returns None.
        """
        return next((i for i, h in enumerate(self.reservations)
                     if h['reservation_id'] == reservation_id), None)

    def create_reservation(self, reservation):
        """
        Adds a new reservation to the collection and saves the file.
        """
        # Delete if it exists
        existing_res_index = self._find_reservation_index_by_id(
            reservation.reservation_id)
        if existing_res_index is not None:
            del self.reservations[existing_res_index]

        # Create
        self.reservations.append(reservation.to_json())
        self._save_reservations()

    def get_reservation(self, reservation_id):
        """
        Retrieves a reservation by its ID.
        """
        for reservation in self.reservations:
            if reservation['reservation_id'] == reservation_id:
                return reservation
        return None

    def update_reservation(self, reservation_id, **kwargs):
        """
        Updates properties of a reservation identified by its ID.
        """
        for reservation in self.reservations:
            if reservation['reservation_id'] == reservation_id:
                reservation.update(kwargs)
                self._save_reservations()
                return True

    def delete_reservation(self, reservation_id):
        """
        Removes a reservation from the collection by its ID and saves the file.
        """
        for i, reservation in enumerate(self.reservations):
            if reservation['reservation_id'] == reservation_id:
                del self.reservations[i]
                self._save_reservations()
                return True
