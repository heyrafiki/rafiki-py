from typing import Literal

CoverageObservationStatus = Literal["active", "exhausted", "expired", "paused"]

COVERAGE_OBSERVATION_STATUS_VALUES: set[CoverageObservationStatus] = {
    "active",
    "exhausted",
    "expired",
    "paused",
}


def check_coverage_observation_status(value: str) -> CoverageObservationStatus:
    if value in COVERAGE_OBSERVATION_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COVERAGE_OBSERVATION_STATUS_VALUES!r}"
    )
