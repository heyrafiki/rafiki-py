from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.remittance_input_currency import (
    RemittanceInputCurrency,
    check_remittance_input_currency,
)

if TYPE_CHECKING:
    from ..models.remittance_allocation_input import RemittanceAllocationInput


T = TypeVar("T", bound="RemittanceInput")


@_attrs_define
class RemittanceInput:
    payer_reference: str
    currency: RemittanceInputCurrency
    received_at: datetime.datetime
    allocations: list[RemittanceAllocationInput]

    def to_dict(self) -> dict[str, Any]:
        payer_reference = self.payer_reference

        currency: str = self.currency

        received_at = self.received_at.isoformat()

        allocations = []
        for allocations_item_data in self.allocations:
            allocations_item = allocations_item_data.to_dict()
            allocations.append(allocations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "payer_reference": payer_reference,
                "currency": currency,
                "received_at": received_at,
                "allocations": allocations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remittance_allocation_input import RemittanceAllocationInput

        d = dict(src_dict)
        payer_reference = d.pop("payer_reference")

        currency = check_remittance_input_currency(d.pop("currency"))

        received_at = datetime.datetime.fromisoformat(d.pop("received_at"))

        allocations = []
        _allocations = d.pop("allocations")
        for allocations_item_data in _allocations:
            allocations_item = RemittanceAllocationInput.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        remittance_input = cls(
            payer_reference=payer_reference,
            currency=currency,
            received_at=received_at,
            allocations=allocations,
        )

        return remittance_input
