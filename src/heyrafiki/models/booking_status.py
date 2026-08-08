from typing import Literal

BookingStatus = Literal["cancelled", "confirmed", "reserved"]

BOOKING_STATUS_VALUES: set[BookingStatus] = {
    "cancelled",
    "confirmed",
    "reserved",
}


def check_booking_status(value: str) -> BookingStatus:
    if value in BOOKING_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BOOKING_STATUS_VALUES!r}")
