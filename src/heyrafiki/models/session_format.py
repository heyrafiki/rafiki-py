from typing import Literal

SessionFormat = Literal["in_person", "online", "phone"]

SESSION_FORMAT_VALUES: set[SessionFormat] = {
    "in_person",
    "online",
    "phone",
}


def check_session_format(value: str) -> SessionFormat:
    if value in SESSION_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SESSION_FORMAT_VALUES!r}")
