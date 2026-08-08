from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="EligibilityCheckAmount")


@_attrs_define
class EligibilityCheckAmount:
    requested: int
    currency: str
    maximum_per_session: int | None

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        currency = self.currency

        maximum_per_session: int | None
        maximum_per_session = self.maximum_per_session

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requested": requested,
                "currency": currency,
                "maximum_per_session": maximum_per_session,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requested = d.pop("requested")

        currency = d.pop("currency")

        def _parse_maximum_per_session(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        maximum_per_session = _parse_maximum_per_session(d.pop("maximum_per_session"))

        eligibility_check_amount = cls(
            requested=requested,
            currency=currency,
            maximum_per_session=maximum_per_session,
        )

        return eligibility_check_amount
