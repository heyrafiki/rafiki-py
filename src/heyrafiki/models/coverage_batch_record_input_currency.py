from typing import Literal

CoverageBatchRecordInputCurrency = Literal["EUR", "GBP", "KES", "USD"]

COVERAGE_BATCH_RECORD_INPUT_CURRENCY_VALUES: set[CoverageBatchRecordInputCurrency] = {
    "EUR",
    "GBP",
    "KES",
    "USD",
}


def check_coverage_batch_record_input_currency(value: str) -> CoverageBatchRecordInputCurrency:
    if value in COVERAGE_BATCH_RECORD_INPUT_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COVERAGE_BATCH_RECORD_INPUT_CURRENCY_VALUES!r}"
    )
