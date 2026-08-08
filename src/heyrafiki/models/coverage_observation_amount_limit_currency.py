from typing import Literal

CoverageObservationAmountLimitCurrency = Literal["EUR", "GBP", "KES", "USD"]

COVERAGE_OBSERVATION_AMOUNT_LIMIT_CURRENCY_VALUES: set[CoverageObservationAmountLimitCurrency] = {
    "EUR",
    "GBP",
    "KES",
    "USD",
}


def check_coverage_observation_amount_limit_currency(
    value: str,
) -> CoverageObservationAmountLimitCurrency:
    if value in COVERAGE_OBSERVATION_AMOUNT_LIMIT_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COVERAGE_OBSERVATION_AMOUNT_LIMIT_CURRENCY_VALUES!r}"
    )
