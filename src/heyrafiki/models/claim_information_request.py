from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.claim_information_request_status import (
    ClaimInformationRequestStatus,
    check_claim_information_request_status,
)

T = TypeVar("T", bound="ClaimInformationRequest")


@_attrs_define
class ClaimInformationRequest:
    id: str
    object_: Literal["claim_information_request"]
    reason_code: str
    requested_evidence_types: list[str]
    status: ClaimInformationRequestStatus
    due_at: datetime.datetime | None
    created_at: datetime.datetime
    resolved_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        reason_code = self.reason_code

        requested_evidence_types = self.requested_evidence_types

        status: str = self.status

        due_at: None | str
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        created_at = self.created_at.isoformat()

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "reason_code": reason_code,
                "requested_evidence_types": requested_evidence_types,
                "status": status,
                "due_at": due_at,
                "created_at": created_at,
                "resolved_at": resolved_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["claim_information_request"], d.pop("object"))
        if object_ != "claim_information_request":
            raise ValueError(
                f"object must match const 'claim_information_request', got '{object_}'"
            )

        reason_code = d.pop("reason_code")

        requested_evidence_types = cast(list[str], d.pop("requested_evidence_types"))

        status = check_claim_information_request_status(d.pop("status"))

        def _parse_due_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = parse_datetime(data)

                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        due_at = _parse_due_at(d.pop("due_at"))

        created_at = parse_datetime(d.pop("created_at"))

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = parse_datetime(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))

        claim_information_request = cls(
            id=id,
            object_=object_,
            reason_code=reason_code,
            requested_evidence_types=requested_evidence_types,
            status=status,
            due_at=due_at,
            created_at=created_at,
            resolved_at=resolved_at,
        )

        return claim_information_request
