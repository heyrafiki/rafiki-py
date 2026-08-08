from typing import Literal

RemittanceInputCurrency = Literal["EUR", "GBP", "KES", "USD"]

REMITTANCE_INPUT_CURRENCY_VALUES: set[RemittanceInputCurrency] = {
    "EUR",
    "GBP",
    "KES",
    "USD",
}


def check_remittance_input_currency(value: str) -> RemittanceInputCurrency:
    if value in REMITTANCE_INPUT_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_INPUT_CURRENCY_VALUES!r}"
    )
