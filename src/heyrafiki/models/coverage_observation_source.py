from typing import Literal

CoverageObservationSource = Literal["batch_file", "payer_api"]

COVERAGE_OBSERVATION_SOURCE_VALUES: set[CoverageObservationSource] = {
    "batch_file",
    "payer_api",
}


def check_coverage_observation_source(value: str) -> CoverageObservationSource:
    if value in COVERAGE_OBSERVATION_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COVERAGE_OBSERVATION_SOURCE_VALUES!r}"
    )
