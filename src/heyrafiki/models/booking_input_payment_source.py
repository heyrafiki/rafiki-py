from typing import Literal

BookingInputPaymentSource = Literal["covered", "self_pay"]

BOOKING_INPUT_PAYMENT_SOURCE_VALUES: set[BookingInputPaymentSource] = {
    "covered",
    "self_pay",
}


def check_booking_input_payment_source(value: str) -> BookingInputPaymentSource:
    if value in BOOKING_INPUT_PAYMENT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BOOKING_INPUT_PAYMENT_SOURCE_VALUES!r}"
    )
