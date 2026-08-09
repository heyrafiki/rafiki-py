from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.coverage_observation_input_currency import (
    CoverageObservationInputCurrency,
    check_coverage_observation_input_currency,
)
from ..models.coverage_observation_input_status import (
    CoverageObservationInputStatus,
    check_coverage_observation_input_status,
)

T = TypeVar("T", bound="CoverageObservationInput")


@_attrs_define
class CoverageObservationInput:
    source_contract_reference: str
    external_coverage_reference: str
    source_version: str
    tenant_reference: str
    member_reference: str
    """ An opaque payer reference. Do not send a name, contact detail or government identifier. """
    plan_name: str
    service_code: str
    status: CoverageObservationInputStatus
    currency: CoverageObservationInputCurrency
    amount_limit: int
    """ Per-Session limit in the currency's minor unit. """
    remaining_sessions: int
    authorization_required: bool
    coordination_priority: int | None
    """ 1 is primary. Leave null when coordination does not apply. """
    valid_from: datetime.datetime
    valid_until: datetime.datetime
    observed_at: datetime.datetime
    """ Timestamp carried by the payer source. """
    evidence_references: list[str]

    def to_dict(self) -> dict[str, Any]:
        source_contract_reference = self.source_contract_reference

        external_coverage_reference = self.external_coverage_reference

        source_version = self.source_version

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

        observed_at = self.observed_at.isoformat()

        evidence_references = self.evidence_references

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source_contract_reference": source_contract_reference,
                "external_coverage_reference": external_coverage_reference,
                "source_version": source_version,
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
                "observed_at": observed_at,
                "evidence_references": evidence_references,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_contract_reference = d.pop("source_contract_reference")

        external_coverage_reference = d.pop("external_coverage_reference")

        source_version = d.pop("source_version")

        tenant_reference = d.pop("tenant_reference")

        member_reference = d.pop("member_reference")

        plan_name = d.pop("plan_name")

        service_code = d.pop("service_code")

        status = check_coverage_observation_input_status(d.pop("status"))

        currency = check_coverage_observation_input_currency(d.pop("currency"))

        amount_limit = d.pop("amount_limit")

        remaining_sessions = d.pop("remaining_sessions")

        authorization_required = d.pop("authorization_required")

        def _parse_coordination_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        coordination_priority = _parse_coordination_priority(d.pop("coordination_priority"))

        valid_from = parse_datetime(d.pop("valid_from"))

        valid_until = parse_datetime(d.pop("valid_until"))

        observed_at = parse_datetime(d.pop("observed_at"))

        evidence_references = cast(list[str], d.pop("evidence_references"))

        coverage_observation_input = cls(
            source_contract_reference=source_contract_reference,
            external_coverage_reference=external_coverage_reference,
            source_version=source_version,
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
            observed_at=observed_at,
            evidence_references=evidence_references,
        )

        return coverage_observation_input
