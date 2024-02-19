# A6.2 - Programming Exercise 3

## Overview

**TC470.10**

**A01793023 - Jorge Luis Arroyo Chavelas**

# Unit tests: Hotel Reservation System

## Overview
This project implements a hotel reservation system with three main abstractions: `Hotel`, `Reservation`, and `Customers`. It provides a comprehensive solution for managing hotels, customers, and reservations with persistence behaviors stored in files.

### Features
- **Hotel Management**: Create, delete, display, and modify hotel information, along with room reservation and cancellation functionalities.
- **Customer Management**: Create, delete, display, and modify customer information.
- **Reservation Management**: Create and cancel reservations.

## Test Cases

**TestHotelManager**: Tests related to hotel management functionalities.
- test_create_hotel()
- test_delete_hotel()
- test_get_hotel()
- test_update_hotel()

**TestCustomerManager**: Tests related to customer management functionalities.
- test_create_customer()
- test_delete_customer()
- test_get_customer()
- test_update_customer()

**TestHotelAndReservationManager**: Tests related to reservation management functionalities.
- test_create_and_get_reservation()
- test_update_and_delete_reservation()

 ## Tests Coverage:
| Module                     | Statements | Missing | Excluded | Coverage |
|----------------------------|------------|---------|----------|----------|
| `customer.py`              | 6          | 0       | 0        | 100%     |
| `hotel.py`                 | 7          | 0       | 0        | 100%     |
| `reservation.py`           | 10         | 0       | 0        | 100%     |
| `test_reservation_manager.py` | 47      | 1       | 0        | 98%      |
| `test_customer_manager.py` | 25         | 1       | 0        | 96%      |
| `test_hotel_manager.py`    | 25         | 1       | 0        | 96%      |
| `hotel_manager.py`         | 41         | 3       | 0        | 93%      |
| `reservation_manager.py`   | 41         | 3       | 0        | 93%      |
| `customer_manager.py`      | 40         | 3       | 0        | 92%      |
| **Total**                  | 242        | 12      | 0        | 95%      |
