from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClaimServicePeriod")


@_attrs_define
class ClaimServicePeriod:
    starts_at: datetime.datetime
    ends_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "starts_at": starts_at,
                "ends_at": ends_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starts_at = datetime.datetime.fromisoformat(d.pop("starts_at"))

        ends_at = datetime.datetime.fromisoformat(d.pop("ends_at"))

        claim_service_period = cls(
            starts_at=starts_at,
            ends_at=ends_at,
        )

        return claim_service_period
