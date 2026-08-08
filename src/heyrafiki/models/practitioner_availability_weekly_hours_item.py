from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.practitioner_availability_weekly_hours_item_formats_item import (
    PractitionerAvailabilityWeeklyHoursItemFormatsItem,
    check_practitioner_availability_weekly_hours_item_formats_item,
)

T = TypeVar("T", bound="PractitionerAvailabilityWeeklyHoursItem")


@_attrs_define
class PractitionerAvailabilityWeeklyHoursItem:
    weekday: int
    """ Day of week, where Sunday is 0. """
    start: str
    end: str
    formats: list[PractitionerAvailabilityWeeklyHoursItemFormatsItem]

    def to_dict(self) -> dict[str, Any]:
        weekday = self.weekday

        start = self.start

        end = self.end

        formats = []
        for formats_item_data in self.formats:
            formats_item: str = formats_item_data
            formats.append(formats_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "weekday": weekday,
                "start": start,
                "end": end,
                "formats": formats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weekday = d.pop("weekday")

        start = d.pop("start")

        end = d.pop("end")

        formats = []
        _formats = d.pop("formats")
        for formats_item_data in _formats:
            formats_item = check_practitioner_availability_weekly_hours_item_formats_item(
                formats_item_data
            )

            formats.append(formats_item)

        practitioner_availability_weekly_hours_item = cls(
            weekday=weekday,
            start=start,
            end=end,
            formats=formats,
        )

        return practitioner_availability_weekly_hours_item
