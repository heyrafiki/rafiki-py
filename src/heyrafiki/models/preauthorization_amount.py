from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PreauthorizationAmount")


@_attrs_define
class PreauthorizationAmount:
    requested: int
    approved: int | None
    currency: str

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        approved: int | None
        approved = self.approved

        currency = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requested": requested,
                "approved": approved,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requested = d.pop("requested")

        def _parse_approved(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        approved = _parse_approved(d.pop("approved"))

        currency = d.pop("currency")

        preauthorization_amount = cls(
            requested=requested,
            approved=approved,
            currency=currency,
        )

        return preauthorization_amount
