from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.claim_status import ClaimStatus, check_claim_status

if TYPE_CHECKING:
    from ..models.claim_adjudication import ClaimAdjudication
    from ..models.claim_amount import ClaimAmount
    from ..models.claim_information_request import ClaimInformationRequest
    from ..models.claim_line import ClaimLine
    from ..models.claim_service_period import ClaimServicePeriod


T = TypeVar("T", bound="Claim")


@_attrs_define
class Claim:
    id: str
    object_: Literal["claim"]
    status: ClaimStatus
    provider_claim_reference: None | str
    submission_version: int
    amount: ClaimAmount
    service_period: ClaimServicePeriod
    lines: list[ClaimLine]
    information_requests: list[ClaimInformationRequest]
    adjudication: ClaimAdjudication | None
    submitted_at: datetime.datetime | None
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        from ..models.claim_adjudication import ClaimAdjudication

        id = self.id

        object_ = self.object_

        status: str = self.status

        provider_claim_reference: None | str
        provider_claim_reference = self.provider_claim_reference

        submission_version = self.submission_version

        amount = self.amount.to_dict()

        service_period = self.service_period.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        information_requests = []
        for information_requests_item_data in self.information_requests:
            information_requests_item = information_requests_item_data.to_dict()
            information_requests.append(information_requests_item)

        adjudication: dict[str, Any] | None
        if isinstance(self.adjudication, ClaimAdjudication):
            adjudication = self.adjudication.to_dict()
        else:
            adjudication = self.adjudication

        submitted_at: None | str
        if isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "status": status,
                "provider_claim_reference": provider_claim_reference,
                "submission_version": submission_version,
                "amount": amount,
                "service_period": service_period,
                "lines": lines,
                "information_requests": information_requests,
                "adjudication": adjudication,
                "submitted_at": submitted_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_adjudication import ClaimAdjudication
        from ..models.claim_amount import ClaimAmount
        from ..models.claim_information_request import ClaimInformationRequest
        from ..models.claim_line import ClaimLine
        from ..models.claim_service_period import ClaimServicePeriod

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["claim"], d.pop("object"))
        if object_ != "claim":
            raise ValueError(f"object must match const 'claim', got '{object_}'")

        status = check_claim_status(d.pop("status"))

        def _parse_provider_claim_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_claim_reference = _parse_provider_claim_reference(
            d.pop("provider_claim_reference")
        )

        submission_version = d.pop("submission_version")

        amount = ClaimAmount.from_dict(d.pop("amount"))

        service_period = ClaimServicePeriod.from_dict(d.pop("service_period"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = ClaimLine.from_dict(lines_item_data)

            lines.append(lines_item)

        information_requests = []
        _information_requests = d.pop("information_requests")
        for information_requests_item_data in _information_requests:
            information_requests_item = ClaimInformationRequest.from_dict(
                information_requests_item_data
            )

            information_requests.append(information_requests_item)

        def _parse_adjudication(data: object) -> ClaimAdjudication | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                adjudication_type_0 = ClaimAdjudication.from_dict(data)

                return adjudication_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClaimAdjudication | None, data)

        adjudication = _parse_adjudication(d.pop("adjudication"))

        def _parse_submitted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = parse_datetime(data)

                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at"))

        updated_at = parse_datetime(d.pop("updated_at"))

        claim = cls(
            id=id,
            object_=object_,
            status=status,
            provider_claim_reference=provider_claim_reference,
            submission_version=submission_version,
            amount=amount,
            service_period=service_period,
            lines=lines,
            information_requests=information_requests,
            adjudication=adjudication,
            submitted_at=submitted_at,
            updated_at=updated_at,
        )

        return claim
