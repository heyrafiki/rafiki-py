from typing import Literal

PreauthorizationStatus = Literal["approved", "cancelled", "denied", "expired", "pending"]

PREAUTHORIZATION_STATUS_VALUES: set[PreauthorizationStatus] = {
    "approved",
    "cancelled",
    "denied",
    "expired",
    "pending",
}


def check_preauthorization_status(value: str) -> PreauthorizationStatus:
    if value in PREAUTHORIZATION_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PREAUTHORIZATION_STATUS_VALUES!r}"
    )
