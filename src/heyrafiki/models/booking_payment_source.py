from typing import Literal

BookingPaymentSource = Literal["covered", "self_pay"]

BOOKING_PAYMENT_SOURCE_VALUES: set[BookingPaymentSource] = {
    "covered",
    "self_pay",
}


def check_booking_payment_source(value: str) -> BookingPaymentSource:
    if value in BOOKING_PAYMENT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BOOKING_PAYMENT_SOURCE_VALUES!r}"
    )
