from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.coverage_observation_source import (
    CoverageObservationSource,
    check_coverage_observation_source,
)
from ..models.coverage_observation_status import (
    CoverageObservationStatus,
    check_coverage_observation_status,
)

if TYPE_CHECKING:
    from ..models.coverage_observation_amount_limit import CoverageObservationAmountLimit


T = TypeVar("T", bound="CoverageObservation")


@_attrs_define
class CoverageObservation:
    id: str
    object_: Literal["coverage_observation"]
    coverage_id: str
    source: CoverageObservationSource
    source_contract_reference: str
    external_coverage_reference: str
    source_version: str
    snapshot_version: int
    status: CoverageObservationStatus
    service_code: str
    amount_limit: CoverageObservationAmountLimit
    remaining_sessions: int
    authorization_required: bool
    coordination_priority: int | None
    valid_from: datetime.datetime
    valid_until: datetime.datetime
    observed_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        coverage_id = self.coverage_id

        source: str = self.source

        source_contract_reference = self.source_contract_reference

        external_coverage_reference = self.external_coverage_reference

        source_version = self.source_version

        snapshot_version = self.snapshot_version

        status: str = self.status

        service_code = self.service_code

        amount_limit = self.amount_limit.to_dict()

        remaining_sessions = self.remaining_sessions

        authorization_required = self.authorization_required

        coordination_priority: int | None
        coordination_priority = self.coordination_priority

        valid_from = self.valid_from.isoformat()

        valid_until = self.valid_until.isoformat()

        observed_at = self.observed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "coverage_id": coverage_id,
                "source": source,
                "source_contract_reference": source_contract_reference,
                "external_coverage_reference": external_coverage_reference,
                "source_version": source_version,
                "snapshot_version": snapshot_version,
                "status": status,
                "service_code": service_code,
                "amount_limit": amount_limit,
                "remaining_sessions": remaining_sessions,
                "authorization_required": authorization_required,
                "coordination_priority": coordination_priority,
                "valid_from": valid_from,
                "valid_until": valid_until,
                "observed_at": observed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_observation_amount_limit import CoverageObservationAmountLimit

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["coverage_observation"], d.pop("object"))
        if object_ != "coverage_observation":
            raise ValueError(f"object must match const 'coverage_observation', got '{object_}'")

        coverage_id = d.pop("coverage_id")

        source = check_coverage_observation_source(d.pop("source"))

        source_contract_reference = d.pop("source_contract_reference")

        external_coverage_reference = d.pop("external_coverage_reference")

        source_version = d.pop("source_version")

        snapshot_version = d.pop("snapshot_version")

        status = check_coverage_observation_status(d.pop("status"))

        service_code = d.pop("service_code")

        amount_limit = CoverageObservationAmountLimit.from_dict(d.pop("amount_limit"))

        remaining_sessions = d.pop("remaining_sessions")

        authorization_required = d.pop("authorization_required")

        def _parse_coordination_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        coordination_priority = _parse_coordination_priority(d.pop("coordination_priority"))

        valid_from = datetime.datetime.fromisoformat(d.pop("valid_from"))

        valid_until = datetime.datetime.fromisoformat(d.pop("valid_until"))

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        coverage_observation = cls(
            id=id,
            object_=object_,
            coverage_id=coverage_id,
            source=source,
            source_contract_reference=source_contract_reference,
            external_coverage_reference=external_coverage_reference,
            source_version=source_version,
            snapshot_version=snapshot_version,
            status=status,
            service_code=service_code,
            amount_limit=amount_limit,
            remaining_sessions=remaining_sessions,
            authorization_required=authorization_required,
            coordination_priority=coordination_priority,
            valid_from=valid_from,
            valid_until=valid_until,
            observed_at=observed_at,
        )

        return coverage_observation
