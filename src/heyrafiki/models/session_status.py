from typing import Literal

SessionStatus = Literal["cancelled", "confirmed", "delivered", "in_progress", "reserved"]

SESSION_STATUS_VALUES: set[SessionStatus] = {
    "cancelled",
    "confirmed",
    "delivered",
    "in_progress",
    "reserved",
}


def check_session_status(value: str) -> SessionStatus:
    if value in SESSION_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SESSION_STATUS_VALUES!r}")
