from typing import Literal

BookingInputFormat = Literal["in_person", "online", "phone"]

BOOKING_INPUT_FORMAT_VALUES: set[BookingInputFormat] = {
    "in_person",
    "online",
    "phone",
}


def check_booking_input_format(value: str) -> BookingInputFormat:
    if value in BOOKING_INPUT_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BOOKING_INPUT_FORMAT_VALUES!r}")
