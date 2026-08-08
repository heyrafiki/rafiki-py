from typing import Literal

RemittanceStatus = Literal["exception", "received", "reconciled"]

REMITTANCE_STATUS_VALUES: set[RemittanceStatus] = {
    "exception",
    "received",
    "reconciled",
}


def check_remittance_status(value: str) -> RemittanceStatus:
    if value in REMITTANCE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REMITTANCE_STATUS_VALUES!r}")
