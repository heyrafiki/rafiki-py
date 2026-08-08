from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClaimAmount")


@_attrs_define
class ClaimAmount:
    currency: str
    billed: int
    approved: int | None
    remitted: int | None
    """ Payer remittance advice allocated to the Claim. """
    settled: int | None
    """ Money movement confirmed by an authorized settlement observation. """

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        billed = self.billed

        approved: int | None
        approved = self.approved

        remitted: int | None
        remitted = self.remitted

        settled: int | None
        settled = self.settled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "billed": billed,
                "approved": approved,
                "remitted": remitted,
                "settled": settled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        billed = d.pop("billed")

        def _parse_approved(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        approved = _parse_approved(d.pop("approved"))

        def _parse_remitted(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remitted = _parse_remitted(d.pop("remitted"))

        def _parse_settled(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        settled = _parse_settled(d.pop("settled"))

        claim_amount = cls(
            currency=currency,
            billed=billed,
            approved=approved,
            remitted=remitted,
            settled=settled,
        )

        return claim_amount
