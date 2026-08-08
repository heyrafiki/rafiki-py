from typing import Literal

EligibilityCheckReasonCodesItem = Literal[
    "amount_exceeds_benefit",
    "benefit_exhausted",
    "coordination_required",
    "coverage_inactive",
    "coverage_not_found",
    "eligible",
    "outside_coverage_period",
]

ELIGIBILITY_CHECK_REASON_CODES_ITEM_VALUES: set[EligibilityCheckReasonCodesItem] = {
    "amount_exceeds_benefit",
    "benefit_exhausted",
    "coordination_required",
    "coverage_inactive",
    "coverage_not_found",
    "eligible",
    "outside_coverage_period",
}


def check_eligibility_check_reason_codes_item(value: str) -> EligibilityCheckReasonCodesItem:
    if value in ELIGIBILITY_CHECK_REASON_CODES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ELIGIBILITY_CHECK_REASON_CODES_ITEM_VALUES!r}"
    )
