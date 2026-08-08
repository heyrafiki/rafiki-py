from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.coverage_batch_record_input import CoverageBatchRecordInput


T = TypeVar("T", bound="CoverageBatchInput")


@_attrs_define
class CoverageBatchInput:
    contract_version: Literal["2026-08-01"]
    batch_reference: str
    batch_version: str
    source_contract_reference: str
    generated_at: datetime.datetime
    records: list[CoverageBatchRecordInput]

    def to_dict(self) -> dict[str, Any]:
        contract_version = self.contract_version

        batch_reference = self.batch_reference

        batch_version = self.batch_version

        source_contract_reference = self.source_contract_reference

        generated_at = self.generated_at.isoformat()

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contract_version": contract_version,
                "batch_reference": batch_reference,
                "batch_version": batch_version,
                "source_contract_reference": source_contract_reference,
                "generated_at": generated_at,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_batch_record_input import CoverageBatchRecordInput

        d = dict(src_dict)
        contract_version = cast(Literal["2026-08-01"], d.pop("contract_version"))
        if contract_version != "2026-08-01":
            raise ValueError(
                f"contract_version must match const '2026-08-01', got '{contract_version}'"
            )

        batch_reference = d.pop("batch_reference")

        batch_version = d.pop("batch_version")

        source_contract_reference = d.pop("source_contract_reference")

        generated_at = datetime.datetime.fromisoformat(d.pop("generated_at"))

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = CoverageBatchRecordInput.from_dict(records_item_data)

            records.append(records_item)

        coverage_batch_input = cls(
            contract_version=contract_version,
            batch_reference=batch_reference,
            batch_version=batch_version,
            source_contract_reference=source_contract_reference,
            generated_at=generated_at,
            records=records,
        )

        return coverage_batch_input
