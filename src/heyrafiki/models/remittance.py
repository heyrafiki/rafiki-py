from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.remittance_status import RemittanceStatus, check_remittance_status

if TYPE_CHECKING:
    from ..models.remittance_allocation import RemittanceAllocation
    from ..models.remittance_amount import RemittanceAmount


T = TypeVar("T", bound="Remittance")


@_attrs_define
class Remittance:
    id: str
    object_: Literal["remittance"]
    status: RemittanceStatus
    payer_reference: str
    amount: RemittanceAmount
    allocations: list[RemittanceAllocation]
    received_at: datetime.datetime
    reconciled_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        status: str = self.status

        payer_reference = self.payer_reference

        amount = self.amount.to_dict()

        allocations = []
        for allocations_item_data in self.allocations:
            allocations_item = allocations_item_data.to_dict()
            allocations.append(allocations_item)

        received_at = self.received_at.isoformat()

        reconciled_at: None | str
        if isinstance(self.reconciled_at, datetime.datetime):
            reconciled_at = self.reconciled_at.isoformat()
        else:
            reconciled_at = self.reconciled_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "status": status,
                "payer_reference": payer_reference,
                "amount": amount,
                "allocations": allocations,
                "received_at": received_at,
                "reconciled_at": reconciled_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remittance_allocation import RemittanceAllocation
        from ..models.remittance_amount import RemittanceAmount

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["remittance"], d.pop("object"))
        if object_ != "remittance":
            raise ValueError(f"object must match const 'remittance', got '{object_}'")

        status = check_remittance_status(d.pop("status"))

        payer_reference = d.pop("payer_reference")

        amount = RemittanceAmount.from_dict(d.pop("amount"))

        allocations = []
        _allocations = d.pop("allocations")
        for allocations_item_data in _allocations:
            allocations_item = RemittanceAllocation.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        received_at = parse_datetime(d.pop("received_at"))

        def _parse_reconciled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reconciled_at_type_0 = parse_datetime(data)

                return reconciled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        reconciled_at = _parse_reconciled_at(d.pop("reconciled_at"))

        remittance = cls(
            id=id,
            object_=object_,
            status=status,
            payer_reference=payer_reference,
            amount=amount,
            allocations=allocations,
            received_at=received_at,
            reconciled_at=reconciled_at,
        )

        return remittance
