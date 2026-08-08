from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.coverage_batch_record_input_currency import (
    CoverageBatchRecordInputCurrency,
    check_coverage_batch_record_input_currency,
)
from ..models.coverage_batch_record_input_status import (
    CoverageBatchRecordInputStatus,
    check_coverage_batch_record_input_status,
)

T = TypeVar("T", bound="CoverageBatchRecordInput")


@_attrs_define
class CoverageBatchRecordInput:
    coverage_reference: str
    record_version: str
    tenant_reference: str
    member_reference: str
    """ An opaque payer reference. Do not send a name, contact detail or government identifier. """
    plan_name: str
    service_code: str
    status: CoverageBatchRecordInputStatus
    currency: CoverageBatchRecordInputCurrency
    amount_limit: int
    """ Per-Session limit in the currency's minor unit. """
    remaining_sessions: int
    authorization_required: bool
    coordination_priority: int | None
    valid_from: datetime.datetime
    valid_until: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        coverage_reference = self.coverage_reference

        record_version = self.record_version

        tenant_reference = self.tenant_reference

        member_reference = self.member_reference

        plan_name = self.plan_name

        service_code = self.service_code

        status: str = self.status

        currency: str = self.currency

        amount_limit = self.amount_limit

        remaining_sessions = self.remaining_sessions

        authorization_required = self.authorization_required

        coordination_priority: int | None
        coordination_priority = self.coordination_priority

        valid_from = self.valid_from.isoformat()

        valid_until = self.valid_until.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "coverage_reference": coverage_reference,
                "record_version": record_version,
                "tenant_reference": tenant_reference,
                "member_reference": member_reference,
                "plan_name": plan_name,
                "service_code": service_code,
                "status": status,
                "currency": currency,
                "amount_limit": amount_limit,
                "remaining_sessions": remaining_sessions,
                "authorization_required": authorization_required,
                "coordination_priority": coordination_priority,
                "valid_from": valid_from,
                "valid_until": valid_until,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        coverage_reference = d.pop("coverage_reference")

        record_version = d.pop("record_version")

        tenant_reference = d.pop("tenant_reference")

        member_reference = d.pop("member_reference")

        plan_name = d.pop("plan_name")

        service_code = d.pop("service_code")

        status = check_coverage_batch_record_input_status(d.pop("status"))

        currency = check_coverage_batch_record_input_currency(d.pop("currency"))

        amount_limit = d.pop("amount_limit")

        remaining_sessions = d.pop("remaining_sessions")

        authorization_required = d.pop("authorization_required")

        def _parse_coordination_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        coordination_priority = _parse_coordination_priority(d.pop("coordination_priority"))

        valid_from = datetime.datetime.fromisoformat(d.pop("valid_from"))

        valid_until = datetime.datetime.fromisoformat(d.pop("valid_until"))

        coverage_batch_record_input = cls(
            coverage_reference=coverage_reference,
            record_version=record_version,
            tenant_reference=tenant_reference,
            member_reference=member_reference,
            plan_name=plan_name,
            service_code=service_code,
            status=status,
            currency=currency,
            amount_limit=amount_limit,
            remaining_sessions=remaining_sessions,
            authorization_required=authorization_required,
            coordination_priority=coordination_priority,
            valid_from=valid_from,
            valid_until=valid_until,
        )

        return coverage_batch_record_input
