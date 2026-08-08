from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="EligibilityCheckService")


@_attrs_define
class EligibilityCheckService:
    code: str
    scheduled_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        scheduled_at = self.scheduled_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "scheduled_at": scheduled_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduled_at"))

        eligibility_check_service = cls(
            code=code,
            scheduled_at=scheduled_at,
        )

        return eligibility_check_service
