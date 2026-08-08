from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.eligibility_check_reason_codes_item import (
    EligibilityCheckReasonCodesItem,
    check_eligibility_check_reason_codes_item,
)
from ..models.eligibility_check_status import EligibilityCheckStatus, check_eligibility_check_status

if TYPE_CHECKING:
    from ..models.eligibility_check_amount import EligibilityCheckAmount
    from ..models.eligibility_check_service import EligibilityCheckService


T = TypeVar("T", bound="EligibilityCheck")


@_attrs_define
class EligibilityCheck:
    id: str
    object_: Literal["eligibility_check"]
    status: EligibilityCheckStatus
    reason_codes: list[EligibilityCheckReasonCodesItem]
    service: EligibilityCheckService
    amount: EligibilityCheckAmount
    authorization_required: bool
    remaining_sessions: int | None
    coverage_valid_until: datetime.datetime | None
    checked_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        status: str = self.status

        reason_codes = []
        for reason_codes_item_data in self.reason_codes:
            reason_codes_item: str = reason_codes_item_data
            reason_codes.append(reason_codes_item)

        service = self.service.to_dict()

        amount = self.amount.to_dict()

        authorization_required = self.authorization_required

        remaining_sessions: int | None
        remaining_sessions = self.remaining_sessions

        coverage_valid_until: None | str
        if isinstance(self.coverage_valid_until, datetime.datetime):
            coverage_valid_until = self.coverage_valid_until.isoformat()
        else:
            coverage_valid_until = self.coverage_valid_until

        checked_at = self.checked_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "status": status,
                "reason_codes": reason_codes,
                "service": service,
                "amount": amount,
                "authorization_required": authorization_required,
                "remaining_sessions": remaining_sessions,
                "coverage_valid_until": coverage_valid_until,
                "checked_at": checked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eligibility_check_amount import EligibilityCheckAmount
        from ..models.eligibility_check_service import EligibilityCheckService

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["eligibility_check"], d.pop("object"))
        if object_ != "eligibility_check":
            raise ValueError(f"object must match const 'eligibility_check', got '{object_}'")

        status = check_eligibility_check_status(d.pop("status"))

        reason_codes = []
        _reason_codes = d.pop("reason_codes")
        for reason_codes_item_data in _reason_codes:
            reason_codes_item = check_eligibility_check_reason_codes_item(reason_codes_item_data)

            reason_codes.append(reason_codes_item)

        service = EligibilityCheckService.from_dict(d.pop("service"))

        amount = EligibilityCheckAmount.from_dict(d.pop("amount"))

        authorization_required = d.pop("authorization_required")

        def _parse_remaining_sessions(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remaining_sessions = _parse_remaining_sessions(d.pop("remaining_sessions"))

        def _parse_coverage_valid_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                coverage_valid_until_type_0 = datetime.datetime.fromisoformat(data)

                return coverage_valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        coverage_valid_until = _parse_coverage_valid_until(d.pop("coverage_valid_until"))

        checked_at = datetime.datetime.fromisoformat(d.pop("checked_at"))

        eligibility_check = cls(
            id=id,
            object_=object_,
            status=status,
            reason_codes=reason_codes,
            service=service,
            amount=amount,
            authorization_required=authorization_required,
            remaining_sessions=remaining_sessions,
            coverage_valid_until=coverage_valid_until,
            checked_at=checked_at,
        )

        return eligibility_check
