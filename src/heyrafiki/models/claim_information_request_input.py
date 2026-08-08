from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClaimInformationRequestInput")


@_attrs_define
class ClaimInformationRequestInput:
    reason_code: str
    requested_evidence_types: list[str]
    due_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason_code = self.reason_code

        requested_evidence_types = self.requested_evidence_types

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason_code": reason_code,
                "requested_evidence_types": requested_evidence_types,
            }
        )
        if due_at is not UNSET:
            field_dict["due_at"] = due_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason_code = d.pop("reason_code")

        requested_evidence_types = cast(list[str], d.pop("requested_evidence_types"))

        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)

                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        claim_information_request_input = cls(
            reason_code=reason_code,
            requested_evidence_types=requested_evidence_types,
            due_at=due_at,
        )

        return claim_information_request_input
