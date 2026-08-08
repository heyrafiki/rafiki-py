from typing import Literal

SessionPaymentSource = Literal["covered", "self_pay"]

SESSION_PAYMENT_SOURCE_VALUES: set[SessionPaymentSource] = {
    "covered",
    "self_pay",
}


def check_session_payment_source(value: str) -> SessionPaymentSource:
    if value in SESSION_PAYMENT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SESSION_PAYMENT_SOURCE_VALUES!r}"
    )
