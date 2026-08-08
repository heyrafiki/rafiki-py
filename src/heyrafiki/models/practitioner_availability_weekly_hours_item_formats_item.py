from typing import Literal

PractitionerAvailabilityWeeklyHoursItemFormatsItem = Literal["in_person", "online", "phone"]

PRACTITIONER_AVAILABILITY_WEEKLY_HOURS_ITEM_FORMATS_ITEM_VALUES: set[
    PractitionerAvailabilityWeeklyHoursItemFormatsItem
] = {
    "in_person",
    "online",
    "phone",
}


def check_practitioner_availability_weekly_hours_item_formats_item(
    value: str,
) -> PractitionerAvailabilityWeeklyHoursItemFormatsItem:
    if value in PRACTITIONER_AVAILABILITY_WEEKLY_HOURS_ITEM_FORMATS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTITIONER_AVAILABILITY_WEEKLY_HOURS_ITEM_FORMATS_ITEM_VALUES!r}"
    )
