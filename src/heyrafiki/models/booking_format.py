from typing import Literal

BookingFormat = Literal["in_person", "online", "phone"]

BOOKING_FORMAT_VALUES: set[BookingFormat] = {
    "in_person",
    "online",
    "phone",
}


def check_booking_format(value: str) -> BookingFormat:
    if value in BOOKING_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BOOKING_FORMAT_VALUES!r}")
