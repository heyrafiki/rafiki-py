from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.practitioner_availability_weekly_hours_item import (
        PractitionerAvailabilityWeeklyHoursItem,
    )


T = TypeVar("T", bound="PractitionerAvailability")


@_attrs_define
class PractitionerAvailability:
    object_: Literal["availability"]
    practitioner_id: str
    timezone: str
    weekly_hours: list[PractitionerAvailabilityWeeklyHoursItem]

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        practitioner_id = self.practitioner_id

        timezone = self.timezone

        weekly_hours = []
        for weekly_hours_item_data in self.weekly_hours:
            weekly_hours_item = weekly_hours_item_data.to_dict()
            weekly_hours.append(weekly_hours_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "practitioner_id": practitioner_id,
                "timezone": timezone,
                "weekly_hours": weekly_hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.practitioner_availability_weekly_hours_item import (
            PractitionerAvailabilityWeeklyHoursItem,
        )

        d = dict(src_dict)
        object_ = cast(Literal["availability"], d.pop("object"))
        if object_ != "availability":
            raise ValueError(f"object must match const 'availability', got '{object_}'")

        practitioner_id = d.pop("practitioner_id")

        timezone = d.pop("timezone")

        weekly_hours = []
        _weekly_hours = d.pop("weekly_hours")
        for weekly_hours_item_data in _weekly_hours:
            weekly_hours_item = PractitionerAvailabilityWeeklyHoursItem.from_dict(
                weekly_hours_item_data
            )

            weekly_hours.append(weekly_hours_item)

        practitioner_availability = cls(
            object_=object_,
            practitioner_id=practitioner_id,
            timezone=timezone,
            weekly_hours=weekly_hours,
        )

        return practitioner_availability
