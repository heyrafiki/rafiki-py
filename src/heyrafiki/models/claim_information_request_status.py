from typing import Literal

ClaimInformationRequestStatus = Literal["cancelled", "fulfilled", "open"]

CLAIM_INFORMATION_REQUEST_STATUS_VALUES: set[ClaimInformationRequestStatus] = {
    "cancelled",
    "fulfilled",
    "open",
}


def check_claim_information_request_status(value: str) -> ClaimInformationRequestStatus:
    if value in CLAIM_INFORMATION_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLAIM_INFORMATION_REQUEST_STATUS_VALUES!r}"
    )
