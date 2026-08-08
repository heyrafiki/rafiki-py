from typing import Literal

EligibilityCheckInputCurrency = Literal["EUR", "GBP", "KES", "USD"]

ELIGIBILITY_CHECK_INPUT_CURRENCY_VALUES: set[EligibilityCheckInputCurrency] = {
    "EUR",
    "GBP",
    "KES",
    "USD",
}


def check_eligibility_check_input_currency(value: str) -> EligibilityCheckInputCurrency:
    if value in ELIGIBILITY_CHECK_INPUT_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ELIGIBILITY_CHECK_INPUT_CURRENCY_VALUES!r}"
    )
