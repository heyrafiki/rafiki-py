from typing import Literal

CoverageObservationInputStatus = Literal["active", "exhausted", "expired", "paused"]

COVERAGE_OBSERVATION_INPUT_STATUS_VALUES: set[CoverageObservationInputStatus] = {
    "active",
    "exhausted",
    "expired",
    "paused",
}


def check_coverage_observation_input_status(value: str) -> CoverageObservationInputStatus:
    if value in COVERAGE_OBSERVATION_INPUT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COVERAGE_OBSERVATION_INPUT_STATUS_VALUES!r}"
    )
