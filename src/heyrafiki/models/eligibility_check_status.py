from typing import Literal

EligibilityCheckStatus = Literal["eligible", "ineligible"]

ELIGIBILITY_CHECK_STATUS_VALUES: set[EligibilityCheckStatus] = {
    "eligible",
    "ineligible",
}


def check_eligibility_check_status(value: str) -> EligibilityCheckStatus:
    if value in ELIGIBILITY_CHECK_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ELIGIBILITY_CHECK_STATUS_VALUES!r}"
    )
