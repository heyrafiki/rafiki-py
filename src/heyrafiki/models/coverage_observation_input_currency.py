from typing import Literal

CoverageObservationInputCurrency = Literal["EUR", "GBP", "KES", "USD"]

COVERAGE_OBSERVATION_INPUT_CURRENCY_VALUES: set[CoverageObservationInputCurrency] = {
    "EUR",
    "GBP",
    "KES",
    "USD",
}


def check_coverage_observation_input_currency(value: str) -> CoverageObservationInputCurrency:
    if value in COVERAGE_OBSERVATION_INPUT_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COVERAGE_OBSERVATION_INPUT_CURRENCY_VALUES!r}"
    )
