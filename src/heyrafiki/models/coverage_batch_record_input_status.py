from typing import Literal

CoverageBatchRecordInputStatus = Literal["active", "exhausted", "expired", "paused"]

COVERAGE_BATCH_RECORD_INPUT_STATUS_VALUES: set[CoverageBatchRecordInputStatus] = {
    "active",
    "exhausted",
    "expired",
    "paused",
}


def check_coverage_batch_record_input_status(value: str) -> CoverageBatchRecordInputStatus:
    if value in COVERAGE_BATCH_RECORD_INPUT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COVERAGE_BATCH_RECORD_INPUT_STATUS_VALUES!r}"
    )
